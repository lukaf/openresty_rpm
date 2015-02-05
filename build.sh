#!/bin/sh

# build.sh -v version [-p prefix] [-d] [-h] [-l]
# -v version        Select version number based on tag.
# -p prefix         Select prefix (default /usr/local/openresty).
# -d                Use --with-debug when building Nginx.
# -l                List available tags for use with -v.
# -h                Display this message.

usage() {
    echo "Usage: ${0##*/} -v version [-p prefix] [-d] [-b] [-l] [-h]"
    echo "-v version        Selection version number based on tag (see -l)."
    echo "-p prefix         Selection prefix (default /usr/local/openresty)."
    echo "-d                Use --with-debug when building Nginx."
    echo "-b                Build source bundle."
    echo "-l                List all available tags (for use with -v)"
    echo "-h                Display this message"
    exit 1
}

err() {
    echo "ERROR: ${@}" >&2
}

die() {
    err ${@}
    exit 1
}

list_tags() {
    (cd ngx_openresty && git tag)
    exit 0
}

commit_history() {
    (cd ngx_openresty && \
        git log --pretty=format:"* %cd %aN <%ae>%n- (%h) %s%n" --date=local ${tag} | \
        sed -r 's/([0-9]+) [0-9]+:[0-9]+:[0-9]+ /\1 /')
}

TEMPLATE_SPEC="rpmbuild/SPECS/ngx_openresty.spec"
SOURCE_DIR="rpmbuild/SOURCES"

while getopts ":v:p:dblh" OPT; do
    case "${OPT}" in
        v)
            VERSION=${OPTARG}
            RPMBUILD_OPTS="${RPMBUILD_OPTS} -D \"openresty_version ${OPTARG}\""
            ;;
        p)
            RPMBUILD_OPTS="${RPMBUILD_OPTS} -D \"resty_prefix ${OPTARG}\""
            ;;
        d)
            RPMBUILD_OPTS="${RPMBUILD_OPTS} --with debug"
            ;;
        b)
            SOURCE_BUILD=1
            ;;
        l)
            list_tags
            ;;
        h)
            usage
            ;;
        *)
            usage
            ;;
    esac
done

if [ -z "${VERSION}" ]; then
    err "missing version"
    usage
fi

VERSION_SPEC=${TEMPLATE_SPEC/\.spec/-${VERSION}.spec}

# create branch from tag
(cd ngx_openresty && git checkout -b v${VERSION} v${VERSION}) || \
    die "Wrong version"

cp ${TEMPLATE_SPEC} ${VERSION_SPEC}

# output changelog
commit_history >> ${VERSION_SPEC}

if [ ${SOURCE_BUILD} ]; then
    (cd ngx_openresty && make && \
        mv ngx_openresty-${VERSION}.tar.gz ../${SOURCE_DIR}/.) || \
        die "Building source bundle failed."
fi


# cleanup
(cd ngx_openresty && git checkout master && git branch -d v${VERSION})

eval QA_RPATHS=$[ 0x0002 ] rpmbuild ${RPMBUILD_OPTS} -ba ${VERSION_SPEC}
