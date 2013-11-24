#### RPM building environment for openresty

*Using a build script (version is mandatory!):*

Set prefix to /opt/openresty:

    $ build.sh -p /opt/openresty -v 1.2.8.1

Debug version:

    $ build.sh -d -v 1.2.8.1

Combined:

    $ build.sh -d -p /opt/openresty -v 1.2.8.1


List available versions (tags):

    $ build.sh -l

Build a source bundle to create RPM from, change prefix and enable debugging:

    $ build.sh -b -p /usr/local/resty -d -v 1.2.8.1


NOTE: last two options require an updated submodule:

    $ cd ngx_openresty
    $ git pull

Help:

    $ build.sh -h
    Usage: build.sh -v version [-p prefix] [-d] [-b] [-l] [-h]
    -v version        Selection version number based on tag (see -l).
    -p prefix         Selection prefix (default /usr/local/openresty).
    -d                Use --with-debug when building Nginx.
    -b                Build source bundle.
    -l                List all available tags (for use with -v)
    -h                Display this message


