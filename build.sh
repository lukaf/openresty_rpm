#!/bin/sh

# build.sh -v version [-p prefix] [-d] [-h] [-l]
# -v version        Select version number based on tag.
# -p prefix         Select prefix (default /usr/local/openresty).
# -d                Use --with-debug when building Nginx.
# -l                List available tags for use with -v.
# -h                Display this message.

usage() {
    echo "Usage: ${0##*/} -v version [-p prefix] [-d] -[-h] [-l]"
    echo "-v version        Selection version number based on tag (see -l)."
    echo "-p prefix         Selection prefix (default /usr/local/openresty)."
    echo "-d                Use --with-debug when building Nginx."
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

while getopts ":v:p:dlh" OPT; do
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

# cleanup
(cd ngx_openresty && git checkout master && git branch -d v${VERSION})

rpmbuild ${RPMBUILD_OPTS} -ba ${VERSION_SPEC}
