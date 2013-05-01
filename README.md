#### RPM building environment for openresty

By default ngx\_openresty is installed in /usr/local/openresty. To change
prefix when building package, set the resty\_prefix variable.

Example: set prefix to /opt/openresty:

    $ rpmbuild -D 'resty_prefix /opt/openresty' -ba ngx_openresty.spec

Debug version can be build using --with debug:

    $ rpmbuild --with debug -ba ngx_openresty.spec

Combined:

    $ rpmbuild -D 'resty_prefix /opt/resty/debug' --with debug -ba ngx_openresty.spec

Or using a build script (version is mandatory!):

Set prefix to /opt/openresty:

    $ build.sh -p /opt/openresty -v 1.2.8.1

Debug version:

    $ build.sh -d -v 1.2.8.1

Combined:

    $ build.sh -d -p /opt/openresty -v 1.2.8.1


List available versions (tags):

    $ build.sh -l

Build a source bundle to create RPM from, change prefix and enable debugging:

    $ buidl.sh -b -p /usr/local/resty -d -v 1.2.8.1


NOTE: last two options require an updated submodule:

    $ cd ngx_openresty
    $ git pull
