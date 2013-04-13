#### RPM building environment for openresty

By default ngx\_openresty is installed in /usr/local/openresty. To change
prefix when building package, set the resty\_prefix variable.
Example: set prefix to /opt/openresty:

    $ rpmbuild -D 'resty_prefix /opt/openresty' -ba ngx_openresty.spec

Debug version can be build using --with debug:

    $ rpmbuild --with debug -ba ngx_openresty.spec

Combined:

    $ rpmbuild -D 'resty_prefix /opt/resty/debug' --with debug -ba ngx_openresty.spec


TODO:
* automate creation of bundles - tag based
