%define openresty_prefix %{?resty_prefix}%{?!resty_prefix:/usr/local/openresty}
%define openresty_release %{?resty_release}%{?!resty_release:1}

# conditionals --with and --without
%bcond_with debug

Name: openresty
Version: %{openresty_version}
Release: %{openresty_release}
Summary: A fully-fledged web application server built using Nginx and 3rd-party modules.

License: MIT and BSD 2-clause license and BSD 3-clause license
URL: http://openresty.org/
Source0: http://openresty.org/download/%{name}-%{version}.tar.gz

BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: perl

Requires: pcre-devel
Requires: zlib-devel
Requires: openssl-devel


%description
OpenResty (aka. ngx_openresty) is a full-fledged web application server by
bundling the standard Nginx core, lots of 3rd-party Nginx modules, as well as
most of their external dependencies.

By taking advantage of various well-designed Nginx modules, OpenResty
effectively turns the nginx server into a powerful web app server, in which
the web developers can use the Lua programming language to script various
existing nginx C modules and Lua modules and construct extremely
high-performance web applications that is capable to handle 10K+ connections.

OpenResty aims to run your server-side web app completely in the Nginx server,
leveraging Nginx's event model to do non-blocking I/O not only with the HTTP
clients, but also with remote backends like MySQL, PostgreSQL, Memcached, and
Redis.

OpenResty is not an Nginx fork. It is just a software bundle. Most of the
patches applied to the Nginx core in OpenResty have already been submitted to
the official Nginx team and most of the patches submitted have also been
accepted. We are trying hard not to fork Nginx and always to use the latest
best Nginx core from the official Nginx team.


%prep
%setup -q


%build
./configure \
    --with-luajit \
    --prefix=%{openresty_prefix} \
    %{?_with_debug}

%{__make} -j 2 %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} -j 2 install DESTDIR=%{buildroot}

find %{buildroot}%{openresty_prefix} -printf "%y %%%%attr(0%m,-,-) %p\n" | \
sed -e 's/^d /%%dir /' \
    -e 's/^f \(.*\)\.conf$/%%config(noreplace) \1.conf/' \
    -e 's/^[^d] //' \
    -e "s#%{buildroot}##" > %{_tmppath}/%{name}-%{version}-%{release}.f


%clean
%{__rm} -rf %{buildroot}
%{__rm} -r %{_tmppath}/%{name}-%{version}-%{release}.f


%files -f %{_tmppath}/%{name}-%{version}-%{release}.f


%changelog
