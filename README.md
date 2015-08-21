#### RPM building environment for openresty

[![wercker status](https://app.wercker.com/status/980d0b0797bbb998a8c8151111022a92/s/master "wercker status")](https://app.wercker.com/project/bykey/980d0b0797bbb998a8c8151111022a92)

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


NOTE: Updated submodule is required:

    $ git submodule update --init --recursive
    $ git submodule foreach git pull origin master

Help:

    $ build.sh -h
    Usage: build.sh -v version [-p prefix] [-d] [-b] [-l] [-h]
    -v version        Selection version number based on tag (see -l).
    -p prefix         Selection prefix (default /usr/local/openresty).
    -d                Use --with-debug when building Nginx.
    -b                Build source bundle.
    -l                List all available tags (for use with -v)
    -h                Display this message


