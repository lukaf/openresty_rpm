%define openresty_prefix /usr/local/openresty

Name: ngx_openresty
Version: 1.2.6.6
Release: 1
Summary: A fully-fledged web application server built using Nginx and 3rd-party modules.

License: MIT and BSD 2-clause license and BSD 3-clause license
URL: http://openresty.org/
Source0: http://openresty.org/download/%{name}-%{version}.tar.gz

BuildRequires: pcre-devel
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: perl


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
    --prefix=%{openresty_prefix}

make %{?_smp_mflags}


%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__make} -j 2 install DESTDIR=${RPM_BUILD_ROOT}

find ${RPM_BUILD_ROOT}%{openresty_prefix} -printf "%y %%%%attr(0%m,-,-) %p\n" | \
sed -e 's/^d /%%dir /' \
    -e 's/^f \(.*\)\.conf$/%%config(noreplace) \1.conf/' \
    -e 's/^[^d] //' \
    -e "s#${RPM_BUILD_ROOT}##" > %{_tmppath}/%{name}-%{version}-%{release}.f


%clean
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__rm} -r %{_tmppath}/%{name}-%{version}-%{release}.f


%files -f %{_tmppath}/%{name}-%{version}-%{release}.f


%changelog
* Mon Feb 18 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1ca5fb8) bumped version to 1.2.6.6.

* Wed Feb 13 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8496c99) upgraded ngx_lua to 0.7.15.

* Mon Feb 11 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (f1083d8) updated tests to reflect recent changes.

* Fri Feb 8 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (dd4620a) bumped version to 1.2.6.5.

* Tue Feb 5 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (45c5114) upgraded lua-resty-upload to 0.07.

* Tue Feb 5 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (a553009) upgraded ngx_srcache to 0.19.

* Mon Feb 4 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (ed74e3d) bumped version to 1.2.6.3.

* Tue Jan 29 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (c0208b8) upgraded ngx_form_input to 0.07.

* Tue Jan 29 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (2681361) upgraded ngx_lua to 0.7.14.

* Sun Jan 27 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (0a2dcd7) added patches for the nginx 1.3.11 core. also excluded the allow_request_body_updating patch.

* Sat Jan 26 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (3e5b0ee) upgraded ngx_srcache to 0.18.

* Thu Jan 24 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (42d6409) upgraded ngx_echo to 0.42 and ngx_devel_kit ot 0.2.18.

* Thu Jan 24 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8e35463) updated resolver_wev_handler_segfault_with_poll.patch to Ruslan Ermilov's version.

* Wed Jan 23 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (fc1929f) applied the resolver_wev_handler_segfault_with_pol patch to the nginx core 1.2.6 and 1.3.7 by default. see http://mailman.nginx.org/pipermail/nginx-devel/2013-January/003275.html for details.

* Sat Jan 5 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (6d0cbed) bumped version to 1.2.6.1; updated tests to reflect recent changes.

* Fri Jan 4 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (9e4d2c0) upgraded ngx_lua to 0.7.13.

* Wed Jan 2 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1faf158) bugfix: when relative paths are used in --with-zlib=DIR, --with-libatomic=DIR, --with-md5=DIR, and --with-sha1=DIR, the build system could not find DIR at all. thanks LazyZhu for reporting it in github issue #21.

* Wed Jan 2 2013 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (a820d40) updated tests to reflect recent changes.

* Sun Dec 30 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (7569b78) upgraded lua-resty-upload to 0.06.

* Sun Dec 30 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1da1181) upgraded ngx_lua to 0.7.12.

* Sat Dec 29 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (06d3586) upgraded ngx_lua to 0.7.12rc1.

* Fri Dec 28 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (309f0cf) upgraded ngx_lua to 0.7.11 and ngx_srcache to 0.17.

* Wed Dec 26 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (a31b1d0) upgraded ngx_lua to 0.7.10.

* Mon Dec 24 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (f2b37bb) upgraded the nginx core to 1.2.6.

* Sun Dec 23 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (a841caa) updated the test suite to reflect recent changes.

* Sun Dec 23 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1b425e8) bumped version to 1.2.4.14.

* Sun Dec 23 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (d0d0584) upgraded ngx_lua to 0.7.9.

* Thu Dec 13 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (3f21292) upgraded lua-resty-upload to 0.05.

* Tue Dec 11 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (f936d06) updated tests to reflect recent changes.

* Tue Dec 11 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (bdc3c5e) upgraded lua-resty-mysql to 0.12; also bumped version number to 1.2.4.13.

* Sun Dec 9 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (5e881d7) upgraded ngx_lua to 0.7.8.

* Sat Dec 8 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (eabcfb4) updated the test suite to reflect recent changes.

* Sat Dec 8 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (300b788) upgraded ngx_lua to 0.7.7; bumped version to 1.2.4.11.

* Thu Dec 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1f83898) applied slab_alloc_no_memory_as_info.patch to lower the log level of the error message "ngx_slab_alloc() failed: no memory" from "crit" to "info".

* Thu Dec 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (31e4baf) bumped version to 1.2.4.11rc3.

* Thu Dec 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (bb4d9b2) bugfix: the upstream_pipeline patch introduced a regression that when upstream_next is in action, nginx might hang. thanks Kindy Lin for reporting this issue.

* Sun Dec 2 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (2696c9f) upgraded ngx_lua to 0.7.6rc2.

* Thu Nov 29 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (f8eda5d) upgraded ngx_lua to 0.7.6rc1.

* Thu Nov 29 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (2ad093b) include the latest bugfixes for LuaJIT 2.0 from the git repository (up to git commit 2ad9834d).

* Wed Nov 21 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (774a60c) updated tests to reflect recent changes.

* Wed Nov 21 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (9e9a661) bumped version to 1.2.4.9.

* Wed Nov 21 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (46cc366) upgraded ngx_lua to 0.7.5 and ngx_headers_more to 0.19.

* Tue Nov 20 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (611b828) upgraded lua-resty-string to 0.08.

* Tue Nov 20 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (0ae14ee) upgraded ngx_headers_more to 0.19rc1.

* Tue Nov 20 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (35b5f53) upgraded ngx_lua to 0.7.5rc1.

* Thu Nov 15 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (9bd2c1f) checked in the patches for the nginx 1.2.5 core.

* Mon Nov 12 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (d4e5d99) upgraded LuaJIT to 2.0.0 (final).

* Mon Nov 12 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (def1331) updated the test plan in sanity.t.

* Mon Nov 12 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (b447ec4) bugfix: ./configure: --with-pcre=PATH did not accept relative path in PATH. thanks smallfish for reporting this issue.

* Mon Nov 12 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (7265b09) updated the test suite to reflect recent changes.

* Mon Nov 12 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (67745bc) upgraded ngx_lua to 0.7.4; also bumped version of ngx_openresty to 1.2.4.7.

* Sun Nov 11 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8e724d4) upgraded lua-resty-dns to 0.09, lua-resty-memcached to 0.10, lua-resty-redis to 0.15, lua-resty-mysql to 0.11, lua-resty-upload to 0.04, and lua-resty-string to 0.07.

* Fri Nov 9 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (eac1071) upgraded luajit to 2.0.0rc3.

* Tue Nov 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (86a935b) upgraded luajit to 2.0.0rc2.

* Tue Nov 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8950d46) added terminal colors to the output of the util/mirror-tarballs script; also added the upstream_test_connect_kqueue patch for nginx 1.3.7.

* Tue Nov 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (7be71ca) Merge branch 'master' of github.com:agentzh/ngx_openresty

* Tue Nov 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (0e72914) checked in the upstream_test_connect_kqueue patch for the nginx 1.2.4 core and applied it by default.

* Mon Nov 5 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (6ca011f) upgraded luajit to 2.0.0-rc1.

* Wed Oct 31 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (0602a38) bumped version to 1.2.4.5; also updated tests to reflect recent changes.

* Wed Oct 31 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (2c38f84) upgraded ngx_lua to 0.7.3.

* Mon Oct 22 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (c0c25af) applied the hotfix #1 for luajit 2.0.0 beta11.

* Thu Oct 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (ce23e95) upgraded ngx_lua to 0.7.2.

* Thu Oct 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (c6f3705) updated tests to reflect recent changes.

* Thu Oct 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (3482cb3) upgraded lua-resty-memcached to 0.09. also bumped version to 1.2.4.3.

* Wed Oct 17 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (500a205) upgraded luajit to 2.0.0beta11.

* Sun Oct 14 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8ead3be) bumped version to 1.2.4.1; also updated the test suite to reflect recent changes.

* Sun Oct 14 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (b19a7df) upgraded ngx_lua to 0.7.1.

* Fri Oct 12 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (b8bdf87) now we add the ngx_srcache module before both ngx_header_more and ngx_lua, so that the former's output filter will run *after* those of the latter's.

* Thu Oct 11 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1dd6b50) upgraded patches for nginx 1.3.7.

* Thu Oct 11 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (07a3959) upgraded the nginx core to 1.2.4; also upgraded ngx_lua to 0.7.0.

* Mon Oct 8 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (00621a1) bumped version to 1.2.3.8.

* Sat Oct 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (676d24e) bumped version to 1.2.3.7 and updated the tests to reflect recent changes.

* Sat Oct 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (25a4bc4) upgraded ngx_lua to 0.6.10.

* Wed Oct 3 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (ab224cb) upgraded ngx_lua to 0.6.9.

* Mon Oct 1 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (eaf7956) bumped version to 1.2.3.5.

* Sat Sep 29 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8f25d89) upgraded ngx_lua to 0.6.8.

* Thu Sep 27 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (4304116) updated the test suite to reflect recent changes.

* Thu Sep 27 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (72f9765) upgraded ngx_lua to 0.6.7 and ngx_openresty to 1.2.3.3.

* Wed Sep 19 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (af4fb37) upgraded lua-redis-parser to 0.10.

* Tue Sep 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (48b0eac) upgraded lua-resty-redis to 0.14.

* Tue Sep 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (82f6eaa) upgraded lua-resty-memcached to 0.08.

* Mon Sep 17 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (c381151) checked in the new patch channel-uninit-params for nginx 1.2.3 and 1.3.6.

* Sat Sep 15 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (e76578e) upgraded ngx_lua to 0.6.5.

* Fri Sep 14 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (e5ba4d3) checked in the patches for nginx 1.3.6.

* Thu Sep 13 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (a5e7da1) upgraded ngx_lua to 0.6.5rc1.

* Tue Sep 11 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (b83fb77) updated the dtrace patch to include new tapset functions ngx_indent, ngx_http_subreq_depth, and ngx_http_req_parent.

* Mon Sep 10 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (9e9cf96) removed an extra line from the nonbuffered-upstream-truncation patch.

* Mon Sep 10 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (02153fd) upgraded ngx_lua to 0.6.4.

* Mon Sep 10 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (5ddb48a) upgraded ngx_srcache to 0.16.

* Sun Sep 9 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (6a37c9b) updated the dtrace patch as well as the nonbuffered-upstream-truncation patch.

* Sun Sep 9 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (3001c7a) upgraded ngx_srcache to 0.15.

* Sun Sep 9 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (0780186) upgraded ngx_redis2 to 0.09.

* Fri Sep 7 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (84917b7) updated the dtrace patch to add new static probe create-pool-done.

* Thu Sep 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (1a90e3f) updated the nonbuffered-upstream-truncation patch to make the error handling more consistent.

* Thu Sep 6 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (ac3efbb) added the nonbuffered-upstream-truncation patch for nginx 1.2.3 to make ngx_http_upstream provide a way in the context of a subrequest to signal the parent of errors when upstream data truncation happens. thanks Bryan Alger for reporting this issue.

* Thu Aug 30 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (2629184) updated the allow_request_body_updating.patch to define the HAVE_ALLOW_REQUEST_BODY_UPDATING_PATCH macro.

* Sun Aug 26 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (62d4082) upgraded lua-resty-dns to 0.08.

* Sun Aug 26 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (6c962fb) upgraded ngx_lua to 0.6.3.

* Sat Aug 25 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (b201032) upgraded lua-resty-dns to 0.07.

* Thu Aug 23 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (dceae9e) updated the test suite to reflect recent changes.

* Thu Aug 23 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (61ae4da) upgraded lua-resty-dns to 0.06 and ngx_lua to 0.6.2.

* Wed Aug 22 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (8f9b404) upgraded lua-resty-redis to 0.13.

* Wed Aug 22 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (ea820f5) upgraded ngx_lua to 0.6.2rc1.

* Wed Aug 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (23ebcbc) updated the dtrace patch for nginx 1.2.3 and 1.3.4 for FreeBSD compatibility.

* Wed Aug 22 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (3e932d8) updated the dtrace patch for nginx 1.2.3 and 1.3.4.

* Tue Aug 21 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (01984ba) updated the dtrace patch for nginx 1.3.4.

* Tue Aug 21 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (248189c) updated the dtrace patch for nginx 1.2.3.

* Mon Aug 20 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (9a7ee9e) upgraded ngx_lua to 0.6.1.

* Mon Aug 20 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (81a9a29) upgraded lua-resty-redis to 0.12.

* Sat Aug 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (6f71631) upgraded ngx_lua to 0.6.0.

* Sat Aug 18 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (2726586) upgraded ngx_drizzle to 0.1.4 and ngx_postgres to 1.0rc2.

* Sat Aug 18 2012 agentzh (章亦春) <agentzh@gmail.com>
- (654bd20) updated the dtrace patches for nginx 1.2.3 and 1.3.4 for FreeBSD. also updated the bundling scripts to make them work on FreeBSD.

* Fri Aug 17 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (afcd9fe) upgraded ngx_drizzle to 0.1.3.

* Thu Aug 16 2012 agentzh (Yichun Zhang) <agentzh@gmail.com>
- (6fe95fb) upgraded the nginx core to 1.2.3; also bumped the version number to 1.2.3.1rc1.

* Wed Aug 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (89bdbc7) updated tests for recent changes.

* Wed Aug 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e1c0786) upgraded the dtrace patches for nginx 1.2.1 and 1.3.4. also bumped the version to 1.2.1.14.

* Tue Aug 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2584e13) updated the dtrace patch for the linking issue on FreeBSD.

* Tue Aug 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (9e49dee) upgraded ngx_lua to 0.5.14.

* Tue Aug 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (5e4d755) added patches for nginx 1.3.4.

* Mon Aug 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (52cf79e) fixed the "ngx_request_t" argument type issue in the dtrace provider for nginx.

* Sun Aug 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (8faebfd) fixed the tests to reflect recent changes.

* Sun Aug 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (655bf32) upgraded ngx_lua to 0.5.13, ngx_echo to 0.41, and lua-resty-dns to 0.05.

* Thu Aug 9 2012 Veniamin Gvozdikov <g.veniamin@googlemail.com>
- (cef05fb) [FreeBSD]: first step of port

* Mon Aug 6 2012 agentzh (章亦春) <agentzh@gmail.com>
- (85b5caf) updated the test suite to reflect recent changes.

* Mon Aug 6 2012 agentzh (章亦春) <agentzh@gmail.com>
- (01a7c53) now we bundle and enable by default the new lua-resty-dns library.

* Mon Aug 6 2012 agentzh (章亦春) <agentzh@gmail.com>
- (65237ea) bumped version to 1.2.1.11.

* Sun Aug 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (6a805a1) upgraded ngx_lua to 0.5.12.

* Sun Aug 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (51fff05) added the new openresty-en mailing list to README.

* Fri Aug 3 2012 agentzh (章亦春) <agentzh@gmail.com>
- (772dc15) upgraded ngx_lua to 0.5.12rc1.

* Fri Aug 3 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4a24efa) upgraded ngx_headers_more to 0.18 and ngx_drizzle to 0.1.2.

* Tue Jul 31 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c885306) upgraded ngx_lua to 0.5.11.

* Mon Jul 30 2012 agentzh (章亦春) <agentzh@gmail.com>
- (dcc95a3) updated tests to reflect recent changes.

* Mon Jul 30 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4367838) added --with-dtrace-probes and --with-dtrace=PATH to the ./configure usgae output.

* Mon Jul 30 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4b236d1) bumped version to 1.2.1.9.

* Mon Jul 30 2012 agentzh (章亦春) <agentzh@gmail.com>
- (b7ffa0d) upgraded ngx_lua to 0.5.10.

* Fri Jul 27 2012 agentzh (章亦春) <agentzh@gmail.com>
- (93a6893) updated the dtrace patch from the nginx-dtrace project.

* Fri Jul 27 2012 agentzh (章亦春) <agentzh@gmail.com>
- (abc99a3) updated the dtrace patch from the nginx-dtrace project.

* Thu Jul 26 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e5d8803) upgraded ngx_lua to 0.5.9.

* Thu Jul 26 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c21b63e) now we apply the dtrace patch by default.

* Thu Jul 26 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e17fa45) synchronized the ./configure option list from the official nginx 1.2.1.

* Thu Jul 26 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c1d79ab) updated the dtrace patch from the nginx-dtrace project.

* Wed Jul 25 2012 agentzh (章亦春) <agentzh@gmail.com>
- (0a1195e) updated the dtrace patch from the dtrace-nginx project.

* Tue Jul 24 2012 agentzh (章亦春) <agentzh@gmail.com>
- (0409ce0) added new patch for the nginx core, nginx-1.2.1-dtrace.patch.

* Sun Jul 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (14167b6) upgraded lua-resty-mysql to 0.10.

* Sun Jul 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ecc5816) fixed an issue regarding subrequests in allow_request_body_updating.patch.

* Sat Jul 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (1aae4c3) removed nginx 1.2.1 patches that are not really used.

* Sat Jul 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (d5fb617) upgraded ngx_lua to 0.5.8.

* Thu Jul 19 2012 agentzh (章亦春) <agentzh@gmail.com>
- (fdfd34c) upgraded ngx_lua to 0.5.8rc1.

* Thu Jul 19 2012 agentzh (章亦春) <agentzh@gmail.com>
- (db1a5fc) mentioned the openresty mailing list.

* Sat Jul 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4ae742c) upgraded ngx_lua to 0.5.7 and lua-resty-mysql to 0.09.

* Fri Jul 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (77f9434) upgraded lua-resty-redis to 0.11.

* Thu Jul 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (85b7fca) minor style fixes.

* Thu Jul 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (969d1d1) upgraded ngx_lua to 0.5.7rc1 and lua-resty-mysql to 0.08.

* Tue Jul 10 2012 agentzh (章亦春) <agentzh@gmail.com>
- (efbc3cc) upgraded ngx_lua to 0.5.6 and ngx_headers_more to 0.17.

* Thu Jul 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (5b91b67) committed patches that were not committed.

* Thu Jul 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ebed2ed) upgraded the standard lua interpreter to 5.1.5; also disabled the Lua 5.0 compatibility in this Lua implementation.

* Wed Jul 4 2012 agentzh (章亦春) <agentzh@gmail.com>
- (37bbfd4) updated the tests to reflect recent changes.

* Wed Jul 4 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4118c23) upgraded ngx_lua to 0.5.5 and lua-resty-redis to 0.10.

* Fri Jun 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2d7a4ad) upgraded ngx_lua to 0.5.4.

* Thu Jun 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (28e127d) upgraded ngx_srcache to 0.14.

* Mon Jun 25 2012 agentzh (章亦春) <agentzh@gmail.com>
- (21a9b10) upgraded ngx_echo to 0.40 and ngx_lua to 0.5.3.

* Sun Jun 24 2012 agentzh (章亦春) <agentzh@gmail.com>
- (78e850f) upgraded ngx_echo to 0.40rc1 and ngx_lua to 0.5.3rc1.

* Sun Jun 24 2012 agentzh (章亦春) <agentzh@gmail.com>
- (3373388) bumped version to 1.2.1.3rc1.

* Sun Jun 24 2012 agentzh (章亦春) <agentzh@gmail.com>
- (1921477) applied nginx-1.2.1-location_if_inherits_proxy.patch to the nginx core. see http://mailman.nginx.org/pipermail/nginx-devel/2012-June/002374.html for details.

* Fri Jun 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (8e363e3) we no longer bundle ngx_http_upstream_keepalive_module because it is already part of the nginx 1.2.1 core. released ngx_openresty devel version 1.2.1.1.

* Fri Jun 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c74b535) upgraded the (optional) no-pool patch to the latest version.

* Fri Jun 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e800242) upgraded ngx_echo to 0.39 and ngx_lua to 0.5.2.

* Thu Jun 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (07a2a8d) upgraded ngx_postgres to 1.0rc1.

* Sun Jun 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2a871e5) upgraded the nginx core to 1.2.1. bumped the version of ngx_openresty to 1.2.1.1rc1.

* Sun Jun 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (139b291) upgraded ngx_lua to 0.5.1; bumped version number of ngx_openresty to 1.0.15.13rc1.

* Sat Jun 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (1de4bb9) bumped version number to 1.0.15.11.

* Fri Jun 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (baefa91) upgraded ngx_lua to v0.5.0rc32; bumped version number of ngx_openresty to 1.0.15.11rc1.

* Fri Jun 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2ad1408) updated nginx-1.0.15-poll_del_event_at_exit.patch. thanks Maxim Dounin.

* Wed Jun 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (82a58c9) releng work for the 1.0.15.10 release.

* Mon Jun 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (3d4784c) removed vim backup files from the source code distribution. thanks Xiaoyu Chen.

* Mon Jun 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (a8a9c95) Revert "upgraded ngx_lua to 0.5.0rc31."

* Fri Jun 8 2012 agentzh (章亦春) <agentzh@gmail.com>
- (950eafe) upgraded ngx_lua to 0.5.0rc31.

* Thu Jun 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (d93314a) bumped version to 1.0.15.9.

* Thu Jun 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (585a62a) upgraded ngx_rds_json to 0.12rc10.

* Thu Jun 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (03451f5) upgraded ngx_lua to 0.5.0rc30.

* Thu Jun 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (bfe8fda) bugfix: the no-pool patch might leak memory. now we have updated the no-pool patch to the latest version that is a thorough rewrite.

* Thu Jun 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (914c4c5) applied poll_del_event_at_exit.patch: http://mailman.nginx.org/pipermail/nginx-devel/2012-June/002328.html

* Fri Jun 1 2012 agentzh (章亦春) <agentzh@gmail.com>
- (938d373) applied the resolver_debug_log_overflow.patch: http://mailman.nginx.org/pipermail/nginx-devel/2012-June/002281.html

* Tue May 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (99e1bd7) bumped version to 1.0.15.7 and also updated the test suite to reflect recent changes.

* Mon May 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ba19971) upgraded lua-resty-redis to 0.09 and ngx_rds_json to 0.12rc9.

* Mon May 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (281c06b) upgraded ngx_lua to 0.5.0rc29.

* Tue May 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (921603b) fixed the filter_finalize_hang patch for a regression in the image filter.

* Mon May 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (140c431) removed patches that have already been included in the official nginx core.

* Thu May 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (0a0f70f) applied the add_core_vars_polluting patch to fix a bug in the nginx core: http://mailman.nginx.org/pipermail/nginx-devel/2012-May/002231.html

* Wed May 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (21f8910) bumped version number to 1.0.15.5 and updated the test suite to reflect recent changes.

* Wed May 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (1b11b48) upgraded ngx_lua to 0.5.0rc28.

* Mon May 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (668c00f) upgraded lua-resty-string to 0.06.

* Mon May 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (3f8ad8a) added some tests for the new option --with-luajit-xcflags.

* Mon May 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (eecc501) updated the tests for the new option --with-luajit-xcflags.

* Mon May 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2ee1f58) updated tests to reflect recent changes.

* Mon May 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4145db0) feature: added --with-luajit-xcflags option to ./configure.

* Mon May 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (88c1439) bugfix: ./util/fix-tests could not distingish redis-nginx-module and redis2-nginx-module.

* Sun May 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e8990b7) upgraded LuaJIT to 2.0.0beta10.

* Sun May 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (41d48ab) upgraded ngx_rds_csv to 0.05rc2.

* Sun May 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ba7a3d6) releng for 1.0.15.3.

* Sun May 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (8c5f23d) upgraded lua-redis-parser to 0.09 and lua-rds-parser to 0.05.

* Sat May 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (a3cd675) upgraded lua-redis-parser to 0.09rc8.

* Sat May 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (a56bd55) bumped version number to 1.0.15.3rc3.

* Sat May 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (7c0c2cb) now we bundle Sergey A. Osokin's ngx_http_redis2 module into ngx_openresty.

* Sat May 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (9b1da94) updated tests to reflect recent changes in version numbers.

* Sat May 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (b76f452) upgraded ngx_lua to 0.5.0rc27 and ngx_srcache to 0.13rc8.

* Fri May 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (94f1718) applied the filter_finalize_hang patch to the nginx core. see http://mailman.nginx.org/pipermail/nginx-devel/2012-May/002190.html for details.

* Fri May 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (8294e9b) upgraded lua-resty-memcached to 0.07 and lua-resty-upload to 0.03.

* Fri May 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (558cbf1) upgraded ngx_lua to 0.5.0rc26 and ngx_srcache to 0.13rc7.

* Thu May 10 2012 agentzh (章亦春) <agentzh@gmail.com>
- (8439b51) upgraded ngx_set_misc to 0.22rc8.

* Wed May 2 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2762f39) added the patch for a bug in ngx_http_named_location in the nginx core.

* Sun Apr 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (74d66c1) upgraded ngx_drizzle to 0.1.2rc7 and ngx_lua to 0.5.0rc25.

* Wed Apr 18 2012 agentzh (章亦春) <agentzh@gmail.com>
- (de5e5e2) bugfix: now we also add <openresty_prefix>/lualib/?/init.lua to the default LUA_PATH. thanks bigplum for reporting this issue.

* Wed Apr 18 2012 agentzh (章亦春) <agentzh@gmail.com>
- (479fa18) upgraded ngx_lua to 0.5.0rc24.

* Tue Apr 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (7231e95) upgraded ngx_set_misc to 0.22rc7.

* Tue Apr 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (8b66f41) upgraded ngx_set_misc to 0.22rc6, ngx_rds_json to 0.12rc8, and ngx_lua to 0.5.0rc23.

* Tue Apr 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (deeea16) fixed patches for nginx 1.0.15.

* Tue Apr 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (06c8b65) upgraded the nginx core to 1.0.15.

* Thu Apr 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (74c4865) upgraded ngx_lua to 0.5.0rc22 and lua-resty-mysql to 0.07. also upgraded the nginx core to 1.0.14.

* Sun Mar 25 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ce803e8) bumped version number to 1.0.11.28.

* Thu Mar 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (843fd34) use the best compress level for gzip.

* Thu Mar 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (39cea1c) upgraded ngx_lua to 0.5.0rc21.

* Wed Mar 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (b4f3bd9) improved the upstream_pipelining patch a bit.

* Wed Mar 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (fcb85fb) now we apply the upstream_pipelining patch to the nginx core by default.

* Wed Mar 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (9a75639) added nginx-1.0.11-upstream_pipelining.patch

* Wed Mar 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (922f49f) upgraded ngx_lua to 0.5.0rc20.

* Wed Mar 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (99c37ea) upgraded ngx_echo to 0.38rc2.

* Fri Mar 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (767863f) upgraded ngx_srcache to 0.13rc6.

* Fri Mar 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (45eb5fd) added null_character_fixes patch to nginx 1.1.15.

* Fri Mar 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (926f758) renamed the null character fixes patch.

* Fri Mar 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (0fed5de) bumped version to 1.0.11.25.

* Fri Mar 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (deff216) security: applied the null-character-fixes patch from the mainstream. The bug did result in a disclosure of previously freed memory if upstream server returned specially crafted response, potentially exposing sensitive information.

* Thu Mar 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2d3383e) upgraded ngx_srcache to 0.13rc5.

* Thu Mar 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (f2f8a02) upgraded ngx_lua to 0.5.0rc19.

* Thu Mar 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (d10a7ec) upgraded ngx_srcache to 0.13rc4.

* Mon Mar 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (b01704d) upgraded ngx_lua to 0.5.0rc18.

* Sun Mar 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (fa6683d) upgraded lua-resty-redis to 0.08.

* Sun Mar 11 2012 agentzh (章亦春) <agentzh@gmail.com>
- (7463207) bugfix: the hotfix patch #4 for lua 5.1.4 has been removed from the official lua.org site. now we mirror it in my agentzh.org site. thanks damajor (Xav) for reporting this issue in github issue #10.

* Tue Mar 6 2012 agentzh (章亦春) <agentzh@gmail.com>
- (627f55d) upgraded ngx_lua to 0.5.0rc17.

* Mon Mar 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (4579111) upgraded lua-resty-string to 0.05.

* Mon Mar 5 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c9d5094) upgraded lua-resty-redis to 0.07.

* Thu Mar 1 2012 agentzh (章亦春) <agentzh@gmail.com>
- (de51f31) upgraded lua-redis-parser to 0.09rc7.

* Thu Mar 1 2012 agentzh (章亦春) <agentzh@gmail.com>
- (a4a3c09) upgraded ngx_redis2 to 0.08rc4.

* Wed Feb 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ec23d93) no longer specify -DLUAJIT_USE_VALGRIND when --with-debug is specified. also upgraded lua-resty-* to their latest versions.

* Wed Feb 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (f459d71) raised the default NGX_HTTP_MAX_SUBREQUESTS to 200, in sync with the official repository.

* Tue Feb 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (367a5d8) bundle new components lua-resty-mysql, lua-resty-upload, and lua-resty-string, which are enabled by default. also added options --without-lua_resty_mysql, --without-lua_resty_upload, and --without-lua_resty_string to ./configure for disabling them.

* Tue Feb 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (dfe629a) updated tests to reflect recent changes.

* Tue Feb 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (d41cb71) bundle new component lua-resty-redis which is enabled by default. also added option --without-lua_resty_redis to ./configure for disabling it.

* Tue Feb 28 2012 agentzh (章亦春) <agentzh@gmail.com>
- (7c21017) bundle new component lua-resty-memcached which is enabled by default. also added option --without-lua_resty_memcached to ./configure for disabling it. also upgraded ngx_lua to 0.5.0rc16.

* Fri Feb 24 2012 agentzh (章亦春) <agentzh@gmail.com>
- (51c12f7) now we apply the official hotfix #1 patch for luajit 2.0.0 beta9.

* Thu Feb 23 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e95dc58) upgraded ngx_lua to 0.5.0rc15.

* Wed Feb 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (bb0af04) upgraded ngx_lua to 0.5.0rc14; also bumped version to 1.0.11.15.

* Wed Feb 22 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c528989) now we enable -DLUAJIT_USE_VALGRIND -DLUA_USE_APICHECK -DLUA_USE_ASSERT flags for luajit when --with-debug is specified.

* Tue Feb 21 2012 agentzh (章亦春) <agentzh@gmail.com>
- (71a3060) updated tests for new versions of the components.

* Mon Feb 20 2012 agentzh (章亦春) <agentzh@gmail.com>
- (3ba6ac3) apply the max_subrequests patch to allow the NGX_HTTP_MAX_SUBREQUESTS macro to be overridden from the outside and adjusted the default value from 50 to 100 because 50 is a little too conservative.

* Mon Feb 20 2012 agentzh (章亦春) <agentzh@gmail.com>
- (cc460be) added patches for nginx 1.1.15.

* Sun Feb 19 2012 agentzh (章亦春) <agentzh@gmail.com>
- (134e901) upgraded ngx_lua to 0.5.0rc13.

* Fri Feb 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (fda2e1e) checked in the patches for nginx 1.0.12.

* Wed Feb 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e9a14f8) upgraded ngx_lua to v0.5.0rc10.

* Wed Feb 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (475d430) upgraded ngx_xss to 0.03rc9, ngx_rds_csv to 0.05rc1, ngx_iconv to 0.10rc7, ngx_redis2 to 0.08rc3, and ngx_lua to 0.5.0rc9.

* Tue Feb 14 2012 agentzh (章亦春) <agentzh@gmail.com>
- (ac6b83a) upgraded ngx_lua to v0.5.0rc7.

* Mon Feb 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (c93802b) updated test suite to reflect recent changes.

* Mon Feb 13 2012 agentzh (章亦春) <agentzh@gmail.com>
- (e67456c) upgraded ngx_lua to 0.5.0rc6.

* Wed Feb 8 2012 agentzh (章亦春) <agentzh@gmail.com>
- (966222f) upgraded ngx_coolkit to 0.2rc1.

* Tue Feb 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (67d50a5) added ngx_coolkit to the bundle.

* Tue Feb 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (3b79af7) upgraded ngx_lua to v0.5.0rc5 and bumped version number to 1.0.11.7.

* Tue Feb 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (60d348d) upgraded ngx_lua to 0.5.0rc4.

* Mon Feb 6 2012 agentzh (章亦春) <agentzh@gmail.com>
- (2d2fabc) upgraded ngx_lua to 0.5.0rc3.

* Fri Feb 3 2012 agentzh (章亦春) <agentzh@gmail.com>
- (f6b914d) upgraded ngx_redis2 to 0.09rc6.

* Thu Feb 2 2012 agentzh (章亦春) <agentzh@gmail.com>
- (5ee253a) upgraded ngx_postgres to 0.9.

* Wed Feb 1 2012 agentzh (章亦春) <agentzh@gmail.com>
- (fc78d02) upgraded ngx_lua to 0.5.0rc1.

* Wed Feb 1 2012 agentzh (章亦春) <agentzh@gmail.com>
- (9670d80) upgraded the nginx core to 1.0.11.

* Wed Feb 1 2012 agentzh (章亦春) <agentzh@gmail.com>
- (91fc8d5) upgraded ngx_lua to 0.4.1; also bumped the version number to 1.0.10.48.

* Sun Jan 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (d27c62e) bumped version number to 1.0.10.47.

* Sun Jan 29 2012 agentzh (章亦春) <agentzh@gmail.com>
- (cc57413) upgraded ngx_lua to 0.4.1rc4.

* Thu Jan 19 2012 agentzh (章亦春) <agentzh@gmail.com>
- (a6814b9) upgraded ngx_drizzle to 0.1.2rc6 and ngx_lua to 0.4.1rc3.

* Tue Jan 17 2012 agentzh (章亦春) <agentzh@gmail.com>
- (64da4f2) upgraded ngx_echo to 0.38rc1, ngx_set_misc to 0.22rc5, ngx_headers_more to 0.17rc1, ngx_drizzle to 0.1.2rc5, ngx_lua to 0.4.1rc1, and ngx_memc to 0.13rc3.

* Mon Jan 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (a05b748) updated tests to reflect recent changes.

* Mon Jan 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (722e2e2) bumped version to 1.0.10.44.

* Mon Jan 16 2012 agentzh (章亦春) <agentzh@gmail.com>
- (5712e9b) upgraded ngx_echo to 0.37 and ngx_headers_more to 0.16.

* Sun Jan 15 2012 agentzh (章亦春) <agentzh@gmail.com>
- (f589bfc) Merge pull request #5 from nightsailer/master

* Sun Jan 15 2012 Pan Fan <nightsailer@gmail.com>
- (b76b990) fix sed on osx/darwin issue

* Thu Jan 12 2012 agentzh (章亦春) <agentzh@gmail.com>
- (fb89742) Prepare for the ngx_openresty devel version 1.0.10

* Mon Jan 9 2012 agentzh (章亦春) <agentzh@gmail.com>
- (487eb2e) upgraded ngx_echo to 0.37rc8.

* Mon Jan 9 2012 agentzh (章亦春) <agentzh@gmail.com>
- (6e9ed6f) upgraded ngx_upstream_keepalive to 0.7.

* Sat Jan 7 2012 agentzh (章亦春) <agentzh@gmail.com>
- (9afd5ad) added patches for nginx 1.0.11.

* Wed Jan 4 2012 agentzh (章亦春) <agentzh@gmail.com>
- (bfdd947) upgraded ngx_lua to 0.3.1rc45.

* Wed Jan 4 2012 agentzh (章亦春) <agentzh@gmail.com>
- (5ef81b5) upgraded ngx_lua to v0.3.1rc44.

* Fri Dec 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6dd8f07) upgraded ngx_lua to 0.3.1rc43.

* Fri Dec 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (06312e6) upgraded ngx_headers_more to 0.16rc7.

* Thu Dec 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1bc8f9b) bugfix: make the "install" phony target depend on the "all" phony target in the Makefile generated by ./configure. thanks Weibin Yao for reporting this issue.

* Thu Dec 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6d1405c) fixed the test plan.

* Thu Dec 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (af701e5) improved Yao Weibin's patch for the --add-module option a bit and also added a test case.

* Thu Dec 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5fb3e86) updated tests to reflect recent changes.

* Thu Dec 29 2011 Weibin Yao <yaoweibin@gmail.com>
- (35afee9) support to add relative path module in configure

* Sun Dec 25 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1a91ab9) re-enable bundling unwind.h for LuaJIT on *BSD and Solaris because we still need to do that.

* Sat Dec 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2b7c818) removed the gzip_ok_invalid_read_fix patch because it is no longer needed.

* Sat Dec 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6081a9b) upgraded ngx_lua to 0.3.1rc42 and ngx_headers_more to 0.16rc6.

* Thu Dec 22 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5fd1a15) upgraded luajit to 2.0.0 beta9 and also applied the patch nginx-1.0.10-gzip_ok_invalid_read_fix.patch.

* Thu Dec 22 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0e98bb3) checked in the gzip_ok_invalid_read_fix patch.

* Fri Dec 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (041652a) upgraded ngx_headers_more to 0.16rc5 and ngx_lua to 0.3.1rc41.

* Fri Dec 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (74c6036) updated .gitignore.

* Fri Dec 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (68fe4b0) upgraded ngx_lua to 0.3.1rc40 and ngx_set_misc to v0.22rc4.

* Fri Dec 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (85a80e8) upgraded ngx_lua to 0.3.1rc39.

* Fri Dec 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d0fc491) bugfix: some old version of "cp" does not support trailing slashes in the destination argument and could break the ./configure script. thanks Weibin Yao for reporting it.

* Wed Dec 14 2011 agentzh (章亦春) <agentzh@gmail.com>
- (893262d) upgraded ngx_srcache to 0.13rc3 and ngx_xss to 0.03rc8.

* Mon Dec 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (89d675f) fixed the link for lua-cjson-1.0.3 in our mirror-tarballs script. thanks Weibin Yao.

* Sun Dec 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0e42b1d) updated the test suite to reflect recent changes.

* Sun Dec 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (16b594b) released stable version 1.0.10.24.

* Mon Dec 5 2011 agentzh (章亦春) <agentzh@gmail.com>
- (fbb9181) upgraded ngx_rds_json to v0.12rc7 and ngx_xss to v0.03rc7.

* Fri Dec 2 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1eb06f1) upgraded ngx_lua to 0.3.1rc38.

* Wed Nov 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f4745c3) fixed a serious regression for linux aio in nginx-1.0.10-epoll_check_stale_wev.patch, thanks Maxim Dounin! released ngx_openresty 1.0.10.21.

* Tue Nov 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (99f0e9f) upgraded ngx_lua to 0.3.1rc37; also released ngx_openresty 1.0.10.19.

* Sat Nov 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (96c2c35) upgraded ngx_lua to 0.3.1rc36; released ngx_openresty 1.0.10.17.

* Sat Nov 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (650f75a) upgraded ngx_lua to 0.3.1rc35; released ngx_openresty 1.0.10.15.

* Fri Nov 25 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c629e23) upgraded ngx_lua to 0.3.1rc34; also released ngx_openresty 1.0.10.13.

* Thu Nov 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d5d36ac) upgraded ngx_lua to 0.3.1rc33.

* Thu Nov 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (e4cddbf) upgraded ngx_lua to 0.3.1rc32; released ngx_openresty 1.0.10.11.

* Thu Nov 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8b23525) upgraded ngx_xss to 0.03rc6 and ngx_memc to 0.13rc2 and ngx_redis2 to 0.08rc2; released ngx_openresty 1.0.10.9.

* Wed Nov 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (69eabd6) upgraded ngx_lua to v0.3.1rc31; released ngx_openresty 1.0.10.7.

* Mon Nov 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (48e6ec6) upgraded ngx_lua to 0.3.1rc30; also released ngx_openresty 1.0.10.5.

* Thu Nov 17 2011 agentzh (章亦春) <agentzh@gmail.com>
- (658ead2) upgraded ngx_lua to v0.3.1rc29; released ngx_openresty 1.0.10.3.

* Wed Nov 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (10d70ab) upgraded the nginx core to 1.0.10.

* Wed Nov 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7215210) fixed the test suite.

* Wed Nov 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (091add6) released ngx_openresty 1.0.9.10.

* Tue Nov 15 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a5ac948) fixed the error message length while ./configure fails.

* Sun Nov 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (099c040) upgraded ngx_drizzle to 0.1.2rc4; also released ngx_openresty 1.0.9.9.

* Fri Nov 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d33c482) improved the missing gmake on BSD error message as per @lhmwzy.

* Thu Nov 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (26d1d6a) added new directives log_escape_non_ascii to prevent escaping 0x7F - 0x1F chars in access log variable values.

* Wed Nov 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8120ad8) upgraded ngx_lua to 0.3.1rc28 and ngx_headers_more to 0.16rc4; also released ngx_openresty 1.0.9.5.

* Wed Nov 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (88b6157) upgraded ngx_lua to 0.3.1rc27 and ngx_drizzle to 0.1.2rc3; released ngx_openresty 1.0.9.3.

* Tue Nov 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8630761) fixed the variable_header_ignore_no_hash patch again. thanks Markus Linnala.

* Tue Nov 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (98893fe) updated the variable_header_ignore_no_hash patch for nginx 1.1.4.

* Tue Nov 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a78b404) fixed a bug in the variable_header_ignore_no_hash patch for nginx 1.0.9.

* Mon Nov 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (95c11ee) upgraded ngx_postgres to 0.9rc2 and also applied the epoll_check_stale_wev patch.

* Mon Nov 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ce8b462) upgraded ngx_lua to 0.3.1rc26 and lua-rds-parser to 0.04; also checked in the epoll_check_stale_wev patch.

* Fri Nov 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4a54fb0) upgraded ngx_lua to 0.3.1rc25 and ngx_xss to 0.03rc5.

* Fri Nov 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (02ecfd1) upgraded patches for nginx 1.0.9.

* Thu Nov 3 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d36afc9) applied the hotfix patch #4 for lua 5.1.4.

* Thu Nov 3 2011 agentzh (章亦春) <agentzh@gmail.com>
- (e6ce800) bumped the version number to 1.0.8.26.

* Thu Nov 3 2011 agentzh (章亦春) <agentzh@gmail.com>
- (93f9f07) now we require gmake for *BSD systems even if luajit is not enabled. thanks @lhmwzy.

* Thu Oct 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (3e2b93c) upgraded ngx_lua to 0.3.1rc23; released ngx_openresty 1.0.8.25; added patches for nginx 0.8.54.

* Thu Oct 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1161f83) upgraded ngx_lua to 0.3.1rc22; released ngx_openresty 1.0.8.23.

* Wed Oct 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (95d2429) upgraded ngx_lua to v0.3.1rc21.

* Mon Oct 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (266f623) upgraded ngx_echo to 0.37rc7.

* Mon Oct 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (bd9c04d) upgraded ngx_lua to 0.3.1rc20; released ngx_openresty 1.0.8.19.

* Sat Oct 22 2011 agentzh (章亦春) <agentzh@gmail.com>
- (91140f3) upgraded ngx_lua to v0.3.1rc19; also released ngx_openresty 1.0.8.17.

* Fri Oct 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b8be9dd) updated patches/nginx-1.0.8-allow_request_body_updating.patch to fix the case when calling ngx_http_read_client_request_body after ngx_http_discard_request_body is called.

* Fri Oct 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b0cfa8d) add -DNGINX_ALLOW_REQUEST_BODY_UPDATING to CFLAGS if ngx_lua is enabled.

* Fri Oct 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2463331) updated nginx-1.0.8-allow_request_body_updating.patch to properly handle the case that all the request body has been preread into r->header_in.

* Fri Oct 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5063f4f) oops! forgot to check in patches/nginx-1.0.8-allow_request_body_updating.patch.

* Fri Oct 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b76e2f4) now we apply the patch to the nginx core so as to allow main request body modifications.

* Wed Oct 19 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b626ebf) upgraded ngx_lua to v0.3.1rc17; released ngx_openresty 1.0.8.15.

* Sun Oct 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (479d89e) upgraded ngx_lua to 0.3.1rc16.

* Sun Oct 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (429ff5b) upgraded ngx_lua to 0.3.1rc15 and released ngx_openresty 1.0.8.13.

* Sun Oct 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f42b061) upgraded ngx_lua to 0.3.1rc14; released ngx_openresty 1.0.8.11.

* Sun Oct 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (876b1ec) upgraded ngx_lua to 0.3.1rc13; released ngx_openresty 1.0.8.9.

* Sun Oct 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (25d7c1e) upgraded ngx_lua to v0.3.1rc12.

* Sat Oct 15 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c239151) upgraded ngx_srcache to 0.13rc2; released ngx_openresty 1.0.8.7.

* Thu Oct 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (67879a5) upgraded ngx_lua to v0.3.1rc11 and ngx_echo to 0.37rc6; also applied the named_location_clear_mods_ctx patch; also released ngx_openresty 1.0.8.5.

* Thu Oct 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (170cc51) upgraded ngx_lua to 0.3.1rc10.

* Tue Oct 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7c22476) upgraded ngx_iconv to 0.10rc5.

* Mon Oct 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (39f926d) upgraded ngx_set_misc to 0.22rc3.

* Mon Oct 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2aeb6c6) upgraded ngx_headers_more to v0.16rc3.

* Mon Oct 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b3cd026) upgraded ngx_srcache to v0.13rc1.

* Sun Oct 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (839f490) upgraded ngx_redis2 to 0.08rc1.

* Sun Oct 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c2c1460) upgraded ngx_rds_csv to 0.04.

* Sun Oct 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ec63a3d) upgraded ngx_lua to 0.3.1rc9.

* Sun Oct 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ba6e18d) upgraded ngx_echo to 0.37rc5.

* Sat Oct 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (97ba2da) upgraded ngx_rds_json to 0.12rc6.

* Sat Oct 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f238905) upgraded ngx_drizzle to 0.1.2rc2.

* Sat Oct 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f71188b) upgraded ngx_drizzle to 0.1.2rc1.

* Sat Oct 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7a7fb5f) upgraded ngx_memc to 0.13rc1.

* Fri Oct 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (23506e8) initial work for migrating to the 1.0.8.1 release; applied the variable-header-ignore-no-hash patch.

* Fri Sep 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ee9cf6c) checked in the variable_header_ignore_no_hash patch.

* Fri Sep 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5136657) released ngx_openresty 1.0.6.21.

* Fri Sep 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b5e945f) added new option -jN (e.g., -j8, -j10, and etc.) to ./configure; thanks @Lance.

* Fri Sep 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b821714) upgraded ngx_lua to 0.3.1rc8; released ngx_openresty 1.0.6.19.

* Thu Sep 22 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c2dc7e3) upgraded ngx_lua to 0.3.1rc7; released ngx_openresty 1.0.6.17.

* Thu Sep 22 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4730dea) upgraded ngx_lua to 0.3.1rc5; released ngx_openresty 1.0.6.15.

* Wed Sep 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a13135e) upgraded ngx_lua to 0.3.1rc4; released ngx_openresty 1.0.6.13.

* Wed Sep 21 2011 agentzh (章亦春) <agentzh@gmail.com>
- (beb32b1) released ngx_openresty 1.0.6.12.

* Tue Sep 20 2011 agentzh (章亦春) <agentzh@gmail.com>
- (48635d8) upgraded ngx_rds_json to 0.12rc5 and ngx_rds_csv to 0.03.

* Tue Sep 20 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a3eea31) upgraded ngx_openresty 0.12rc4 and released ngx_openresty 1.0.6.11.

* Mon Sep 19 2011 agentzh (章亦春) <agentzh@gmail.com>
- (06091ef) upgraded lua-cjson to 1.0.3; released ngx_openresty 1.0.6.9.

* Sun Sep 18 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b11711a) added the new option --with-lua51=PATH to the configure script. released ngx_openresty 1.0.6.7.

* Sun Sep 18 2011 agentzh (章亦春) <agentzh@gmail.com>
- (733e37e) added the --with-luajit=PATH option to ./configure per NginxUser's suggestion.

* Thu Sep 15 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1bac07b) upgraded ngx_rds_json to 0.12rc3; released ngx_openresty 1.0.6.5.

* Wed Sep 14 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b371fdf) upgraded ngx_lua to 0.3.1rc3, ngx_echo to 0.37rc4, and ngx_headers_more to 0.16rc2; released ngx_openresty 1.0.6.3.

* Thu Sep 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (98d6ac8) checked in the upgrade-patches.pl script.

* Thu Sep 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f616ce3) upgraded ngx_lua to 0.3.1rc1; released ngx_openresty 1.0.6.1.

* Tue Sep 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (058842e) added the no_error_pages patch for nginx 1.1.2.

* Sun Sep 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (974c82a) upgraded ngx_headers_more to 0.16rc1; released ngx_openresty 1.0.6.0rc2.

* Sun Sep 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (eb28777) released 1.0.6.0rc1.

* Sun Sep 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (aefb915) upgraded ngx_lua to v0.3.0; released ngx_openresty 1.0.5.1.

* Fri Sep 2 2011 agentzh (章亦春) <agentzh@gmail.com>
- (39f8be8) upgraded ngx_lua to v0.2.1rc22; released ngx_openresty 1.0.5.1rc14.

* Thu Sep 1 2011 agentzh (章亦春) <agentzh@gmail.com>
- (36e95ce) updated ngx_lua to rc21.

* Thu Sep 1 2011 agentzh (章亦春) <agentzh@gmail.com>
- (3afa06f) upgraded ngx_lua to v0.2.1rc20 and ngx_echo to 0.37rc2; released 1.0.5.1rc13.

* Wed Aug 31 2011 agentzh (章亦春) <agentzh@gmail.com>
- (da9a356) upgraded lua-rds-parser to 0.03; released ngx_openresty 1.0.5.1rc12.

* Wed Aug 31 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a979e3e) now we bundle lua-rds-parser too :)

* Wed Aug 31 2011 agentzh (章亦春) <agentzh@gmail.com>
- (907bf9f) now we bundle the ngx_rds_csv module as well.

* Tue Aug 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (78674fd) upgraded ngx_rds_json to 0.12rc2; released ngx_openresty 1.0.5.1rc11.

* Mon Aug 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (08d54b1) Merge branch 'master' of github.com:agentzh/ngx_openresty

* Mon Aug 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5c7d2b3) upgraded lua-redis-parser to 1.0.5.1rc10. released ngx_openresty 1.0.5.1rc10.

* Mon Aug 29 2011 liseen <liseen.wan@gmail.com>
- (c07cf89) updated spec file for ngx_openresty

* Sat Aug 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (cd83ed0) upgraded ngx_lua to v0.2.1rc19; released ngx_openresty 1.0.5.1rc9.

* Fri Aug 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (60798ca) upgraded ngx_lua to v0.2.1rc18; released ngx_openresty 1.0.5.1rc8.

* Fri Aug 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (baa293d) upgraded ngx_lua to v0.2.1rc17; released ngx_openresty 1.0.5.1rc7.

* Wed Aug 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b7c7c6e) Merge branch 'master' of github.com:agentzh/ngx_openresty

* Wed Aug 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0140c11) upgraded ngx_lua to 0.2.1rc16; released ngx_openresty 1.0.5.1rc6.

* Wed Aug 24 2011 liseen <liseen.wan@gmail.com>
- (b44ceb7) added spec template for ngx_openresty

* Wed Aug 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7f45ae0) upgraded ngx_lua to v0.2.1rc15; released ngx_openresty 1.0.5.1rc5.

* Wed Aug 24 2011 agentzh (章亦春) <agentzh@gmail.com>
- (50f13ca) upgraded ngx_lua to 0.2.1rc14; released ngx_openresty 1.0.5.1rc4.

* Tue Aug 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (26d6e9a) upgraded ngx_lua to 0.2.1rc13 and ngx_drizzle to 0.1.1rc4; released ngx_openresty 1.0.5.1rc3.

* Thu Aug 18 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ba41f86) upgraded ngx_lua to v0.2.1rc12; released ngx_openresty 1.0.5.1rc2.

* Tue Aug 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (83280c1) upgraded ngx_lua to v0.2.1rc11; released ngx_openresty 1.0.5.1rc1.

* Tue Aug 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5c92a4a) bumped version number to 1.0.5.0.

* Tue Aug 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (85dab85) updated the tet suite to reflect recent changes.

* Sat Aug 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (041548d) upgraded ngx_lua to v0.2.1rc9; released ngx_openresty 1.0.5.0rc7.

* Sat Aug 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1d9549b) upgraded ngx_lua to v0.2.1rc8; released ngx_openresty 1.0.5.0rc6.

* Fri Aug 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1510009) upgraded ngx_lua to v0.2.1rc7; released ngx_openresty 1.0.5.0rc5.

* Fri Aug 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5d875ab) upgraded ngx_lua to v0.2.1rc6; released ngx_openresty 1.0.5.0rc5.

* Fri Aug 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (3a3bcf1) upgraded ngx_lua to v0.2.1rc5; released ngx_openresty 1.0.5.0rc4.

* Thu Aug 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (030ffab) now we bundle the lua-redis-parser library with us and it is enabled by default. tested on Linux i386, Linux x86_64, Mac OS X, FreeBSD 8.2 i386, and Solaris 11; added the new option --without-lua_redis_parser to the ./configure  script; made the test scaffold emit .t_ file with actual outputs as the expected outputs; released ngx_openresty 1.0.5.0rc3.

* Wed Aug 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a3dfc21) documented the --without-lua_cjson option in the ./configure usage output. released ngx_openresty 1.0.5.0rc2.

* Wed Aug 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d283e90) made lua-cjson honor the --with-debug option; updated the test suite to reflect recent changes.

* Wed Aug 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (3aedf4d) added -d option to util/install and also made the -m option optional. fixed compatibility issue on Solaris with lua-cjson: there is no isinf on Solaris 11.

* Wed Aug 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (32ef993) more progress on lua-cjson bundling. it now works on Mac OS X, FreeBSD, and Linux, at least.

* Tue Aug 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6a75ebc) lua-cjson is now bundled and enabled by default. it is working on Linux.

* Tue Aug 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (636ef91) merged the nginx-1.0.5 branch back to master.

* Tue Aug 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (458b8f5) release 1.0.4.2.

* Mon Aug 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (239d3e4) upgraded the nginx core to 1.0.5.

* Mon Aug 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (95e12ba) added regression tests for recent changes for Solaris and FreeBSD.

* Mon Aug 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (843cb73) now we bundle a perl script to serve as the install script for Solaris. now ngx_openresty 1.0.4.2rc13 builds successfully on Solaris 11 with LuaJIT enabled!

* Mon Aug 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1276fbd) bundled gcc's unwind-generic.h for BSD because unwind.h is missing at least on FreeBSD. released ngx_openresty 1.0.4.2rc12.

* Mon Aug 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5aa4947) use absoluate paths in Makefile to prevent -jN chaos when using bsdmake. released ngx_openresty 1.0.4.2rc11.

* Sun Aug 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (dd2d1d0) upgraded ngx_lua to v0.2.1rc4. released ngx_openresty 1.0.4.2rc10.

* Sun Aug 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b255299) fixed a typo in README.

* Sun Aug 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a50e578) now we use gmake if it is avaialbe in PATH during ./configure; also added the --with-make=PATH option to allow the user to specify a custom make utility. released ngx_openresty 1.0.4.2rc9.

* Sat Aug 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (23d0222) we now use the CC variable instead of HOST_CC while passing the --with-cc option to the luajit build system. thanks @姜大炮 for reporting this issue.

* Fri Aug 5 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6e5f3ce) upgraded ngx_lua to v0.2.1rc3. released ngx_openresty 1.0.4.2rc7.

* Fri Aug 5 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6431074) added the --with-pg_config option to ./configure script as per 罗翼's suggestion. released ngx_openresty 1.0.4.2rc6.

* Fri Aug 5 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2654f60) added the --with-no-pool-patch option to the ./configure  script, to allow enabling the no-pool patch for debugging memory issues with valgrind, for example. released ngx_openresty 1.0.4.2rc5.

* Thu Aug 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (da11207) added the --with-libpq=DIR option to the ./configure script. also released ngx_openresty 1.0.4.2rc4.

* Thu Aug 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5c20832) upgraded ngx_drizzle to v0.1.1rc3. released ngx_openresty 1.0.4.2rc3.

* Thu Aug 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5e2df4b) fixed a regression while specifying --with-http_iconv_module during ./configure. thanks 冯新国 for reporting this issue released ngx_openresty 1.0.4.2rc2.

* Sat Jul 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (106f975) upgraded ngx_set_misc to 0.22rc2; released ngx_openresty 1.0.4.2rc1.

* Sat Jul 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (77e510a) updated the tests for the new release.

* Sat Jul 30 2011 agentzh (章亦春) <agentzh@gmail.com>
- (88272c5) fixed a typo in the patch.

* Thu Jul 28 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4004360) fixed a regression when enabling luajit in 1.0.4.1rc5. thanks @Lance. released ngx_openresty 1.0.4.1rc6.

* Tue Jul 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (177e1bf) we do not specify TARGET_STRIP= when CCDEBUG is set to -g because it will make gmake crash. sigh.

* Tue Jul 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0bf8bbe) upgraded ngx_iconv to 0.10rc3, ngx_form_input to 0.07rc5, ngx_array_var to 0.03rc1, and ngx_set_misc to 0.22rc1; now --with-debug option also affects luajit2.0; disabled target stripping in luajit2.0; released ngx_openresty 1.0.4.1rc5.

* Mon Jul 25 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8ba0a37) ngx_openresty 1.0.4.1rc4.

* Mon Jul 25 2011 agentzh (章亦春) <agentzh@gmail.com>
- (557f527) applied the official hotfix1 patch for LuaJIT 2.0.0 beta8; also released ngx_openresty 1.0.4.1rc4.

* Sat Jul 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b7e7398) now the --with-cc=CC option of ./configure also controls the C compiler used by Lua and LuaJIT. thanks @姜大炮 for reporting the issue; also released ngx_openresty 1.0.4.1rc3.

* Sat Jul 23 2011 agentzh (章亦春) <agentzh@gmail.com>
- (68aac43) upgraded ngx_lua to v0.2.1rc2 and ngx_redis2 to v0.07; also released ngx_openresty 1.0.4.1rc2.

* Thu Jul 14 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d2c3802) upgraded ngx_rds_json to v0.12rc1, ngx_drizzle to v0.1.1rc2, ngx_lua to v0.2.1rc1, ngx_postgres to v0.9rc1, ngx_redis2 to v0.07rc6, and also released ngx_openresty 1.0.4.1rc1.

* Thu Jul 14 2011 agentzh (章亦春) <agentzh@gmail.com>
- (918e884) Merge branch 'master' of github.com:agentzh/ngx_openresty

* Wed Jul 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (cbce5da) no longer enable gcc -O2 by default. -O2 hates backtraces.

* Tue Jul 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8ebcad3) ngx_openresty release 1.0.4.0.

* Tue Jul 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4e2b3dc) upgraded ngx_drizzle to v0.1.1rc1 and released ngx_openresty 1.0.4.0rc5.

* Mon Jul 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ca408fc) Config::Config is missing on CentOS 6 by default. sigh. fixed it by using ":" regardless the current OS.

* Mon Jul 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (092b2f6) upgraded ngx_echo to v0.37rc1 and also marked ngx_openresty 1.0.4.0rc3.

* Mon Jul 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c56e7e8) we no longer depend on ExtUtils::MakeMaker because it is not perl's core module. thanks Lance for reporting this issue on CentOS 6.

* Mon Jul 11 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b401198) upgraded ngx_srcache to v0.12 and marked ngx_openresty 1.0.4.0rc2.

* Fri Jul 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5505eac) upgraded the nginx core to 1.0.4 and released ngx_openresty 1.0.4.0rc1.

* Fri Jul 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (22d6c02) ngx_openresty release 0.8.54.9.

* Fri Jul 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4bd257d) upgraded ngx_echo to v0.36 and ngx_memc to v0.12. marked ngx_openresty 0.8.54.9rc6.

* Thu Jul 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2993992) applied the subrequest loop fix patch from Maxim Dounin and released ngx_openresty 0.8.54.9rc5.

* Thu Jul 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (60109db) added Maxim Dounin's patches.

* Wed Jul 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5714d20) upgraded ngx_rds_json to v0.11, ngx_headers_more to v0.15, and ngx_drizzle to v0.1.0; also marked ngx_openresty 0.8.54.9rc4.

* Tue Jul 5 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a69dd64) upgraded ngx_drizzle to 0.0.15rc14 and ngx_lua to 0.2.0; also released ngx_openresty 0.8.54.9rc3.

* Mon Jul 4 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c7cffaa) upgraded ngx_lua to 0.1.6rc18 and released ngx_openresty 0.8.54.9rc2.

* Sun Jul 3 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ab2cdb5) upgraded ngx_redis2 to 0.07rc5 and released ngx_openresty 0.8.54.9rc1.

* Fri Jul 1 2011 agentzh (章亦春) <agentzh@gmail.com>
- (e101ac7) released ngx_openresty 0.8.54.8; also updated README to point to openresty.org.

* Fri Jul 1 2011 agentzh (章亦春) <agentzh@gmail.com>
- (147dba8) upgraded ngx_echo to 0.36rc6, ngx_lua to 0.1.6rc17, ngx_srcache to 0.12rc6, and ngx_redis2 to 0.07rc4 and also released ngx_openresty 0.8.54.8rc2.

* Tue Jun 28 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5a78900) added --with-libdrizzle option to specify the (lib)drizzle installation prefix. now ngx_drizzle is disabled by default. you need to enable it via the --with-http_drizzle_module option.

* Tue Jun 28 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7fcf5e3) we no longer bundle libdrizzle because libdrizzle 1.0 is distributed with the drizzle server and hard to separate.

* Mon Jun 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2055f54) released ngx_openresty 0.8.54.7.

* Mon Jun 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (cdcfac9) marked ngx_openresty 0.8.54.7rc5.

* Mon Jun 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0597fed) we should preserve timestamps when copying bundle/ to build/.

* Mon Jun 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0556e08) upgraded ngx_xss to 0.03rc3, ngx_drizzle to 0.0.15rc11, ngx_memc to 0.12rc2, ngx_srcache to 0.12rc5, ngx_redis2 to 0.07rc3; also marked ngx_openresty 0.8.54.7rc4.

* Mon Jun 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (69a2eff) upgraded LuaJIT to 2.0.0beta8, ngx_lua to 0.1.6rc15, and ngx_echo to 0.36rc4; also released ngx_openresty 0.8.54.7rc3.

* Thu Jun 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7244088) upgraded ngx_lua to v0.1.16rc14 and ngx_headers_more to v0.15rc3; also released ngx_openresty 0.8.54.7rc2.

* Wed Jun 15 2011 agentzh (章亦春) <agentzh@gmail.com>
- (9da7200) upgraded ngx_headers_more to v0.15rc2 and ngx_lua to v0.1.6rc13. released ngx_openresty 0.8.54.7rc1.

* Wed Jun 15 2011 agentzh (章亦春) <agentzh@gmail.com>
- (46ec035) released ngx_openresty 0.8.54.6.

* Tue Jun 14 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7d6c400) upgraded ngx_lua to v0.1.6rc12 and ngx_drizzle to v0.0.15rc10; also released ngx_openresty v0.8.54.6rc5.

* Sun Jun 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7df5c5c) fixed a test in sanity.t.

* Sun Jun 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8fa9eb7) upgraded ngx_lua to 0.1.6rc11 and ngx_redis2 to 0.07rc2; also released ngx_openresty 0.8.54.6rc4.

* Sun Jun 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (cd77c67) version 0.8.54.6rc3.

* Fri Jun 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (3702d98) Merge branch 'master' of github.com:agentzh/ngx_openresty

* Fri Jun 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (04709aa) ensure that ldconfig is in PATH on linux *and* luajit is enabled.

* Fri May 27 2011 agentzh (章亦春) <agentzh@gmail.com>
- (70d5876) upgraded ngx_lua to 0.1.6rc10; marked ngx_openresty 0.8.54.6rc2.

* Thu May 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (942411c) emphasized that you need to add the path of your "ldconfig" utility to your PATH env if you want to enable luajit.

* Thu May 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b644d3d) now we create symlinks to luajit library files.

* Thu May 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (087ec65) documented the autoconf.err file for debugging ./configure issues.

* Thu May 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4df2272) documented that for certain Debian systems, it is required to specify --with-ld-opt="-ldl" when luajit is enabled.

* Thu May 26 2011 agentzh (章亦春) <agentzh@gmail.com>
- (73f1309) broke lines that are too long in README.

* Wed May 25 2011 agentzh (章亦春) <agentzh@gmail.com>
- (777da53) upgraded ngx_lua to 0.1.6rc9 and ngx_echo to 0.36rc3; released ngx_openresty 0.8.54.5.

* Fri May 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f43134c) release 0.8.54.4.

* Fri May 13 2011 agentzh (章亦春) <agentzh@gmail.com>
- (400de3c) upgraded LuaJIT2.0, ngx_lua, ngx_headers_more, and ngx_srcache; also bumped the bundle version to 0.8.54.4rc3.

* Thu May 12 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6271d10) added a note for starting the ngx_openresty server.

* Thu Apr 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (9415daf) upgraded ngx_lua to 0.1.16rc4 and ngx_redis2 to 0.07rc1.

* Sat Apr 2 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1f051ab) mentions that make -jN may not work at least for FreeBSD's bsdmake.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (86024a6) upgraded ngx_headers_more to 0.15rc1 and also updated version to 0.8.54.4rc1.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (478518f) added a quick note to fedora/redhat users.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (439af7a) updated tests to reflect recent changes.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (18e0f4f) release 0.8.54.3.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (96f79ef) now we upgrade to ngx_lua v0.1.6rc3 to support mac os x 64-bit better and make configure script detect macosx for darwin system correctly.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2a69e79) added a quick note to Mac OS X users.

* Tue Mar 29 2011 agentzh (章亦春) <agentzh@gmail.com>
- (df07bfb) now we use -Wl,rpath,/some/path rather than -Wl,rpath=/some/path because the latter does not work on platforms like Mac OS X.

* Tue Mar 22 2011 agentzh (章亦春) <agentzh@gmail.com>
- (9e4a02a) added a quick note for debian and ubuntu users.

* Fri Mar 18 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5b9c7b8) now we incorporate the official patch-lua-5.1.4-3 patch for lua5.1.

* Thu Mar 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (873b821) release 0.8.54.2.

* Thu Mar 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (aa77273) now we bundle the redis2 module.

* Thu Mar 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (7a38a9c) fixed the failing tests due to module upgrading.

* Thu Mar 10 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d894280) upgraded NDK to 0.2.17 and ngx_set_misc to 0.21.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (1663e02) now we require at least perl 5.6.0. released 0.8.54.1.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (a608dd1) fixed a test for Solaris.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (292e460) now we apply the makefile install fix patch for Solaris.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (c8505d3) fixed a small warning of uninitialized values.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (dc2394d) added tests for Mac OS X.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4336939) now we disable ngx_drizzle on solaris/sunos by default because libdrizzle is having problems on solaris. sigh.

* Wed Mar 9 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2101781) added a test case for --prefix.

* Tue Mar 8 2011 agentzh (章亦春) <agentzh@gmail.com>
- (67c9590) fixed the email address of chaoslawful in README. thanks Liseen Wan.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (5edab4b) tweaked the sample configure line a bit.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (932803b) mentioned in README that we require a working perl 5.6.x+ in the PATH env.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ffd989f) checked in util/fix-tests.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8efd891) listed all the components that we have bundled.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (244bd03) added more tests for --with-http_postgres_module and --with-http_iconv_module.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2a2a5f4) fixed auto_complate and upgraded various modules.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (e9d0117) use ngx_auth_request 0.2 tarball rather than the hp tip.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (b2acdc5) now we support accumulative --with-ld-opt option.

* Mon Mar 7 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0b2e1ec) now we support accumulative --with-cc-opt.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (eeb106c) now we automatically build the bundled libdrizzle library.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (84989d2) now we also test the generated makefiles in our test suite.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (bff4acb) now we write Makefile.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (87277a3) minor Makefile tweaks.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (215f852) added a test for --with-luajit.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8d2fd89) now we enable ngx_http_ssl_module by default and we also enable ngx_set_misc by default.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (bf6c7ba) added a test for --with-debug.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (50e6dd5) fixed error checking order.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (824c7a4) added test scaffold t::Config.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (37fbb64) added the --dry-run option for testing.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (23f8304) run the test suite in the right way.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (013d886) now we use Text::Diff in t/sanity.t.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (64c3ab1) a lot of work on the util/configure script.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (d9ab992) make util/configure executable.

* Sun Mar 6 2011 agentzh (章亦春) <agentzh@gmail.com>
- (3d56214) checked in util/configure.

* Tue Mar 1 2011 agentzh (章亦春) <agentzh@gmail.com>
- (ad08c26) updated ngx_drizzle to v0.0.15rc9.

* Mon Feb 28 2011 agentzh (章亦春) <agentzh@gmail.com>
- (52fd9ae) updated ngx_drizzle to 0.0.15rc8.

* Thu Feb 17 2011 agentzh (章亦春) <agentzh@gmail.com>
- (05d728d) upgraded ngx_drizzle to 0.0.15rc6.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (4431830) now we also bundle libdrizzle with our patch applied.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (fdeaab2) now we bundle LuaJIT2.0beta6 as well.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0c1f102) now we also bundle the standard lua 5.1 with the official hotfix patch.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2cca7c7) more tweaks of README.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2da93c4) more tweaks of README.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (2d9e6c0) more docs.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (454fb5c) added more docs to README.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (6bcb653) now we bundle ngx_postgres as well.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (baeb020) now "make" produces a tarball but still incomplete yet.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (8331546) ignored unrelated directories for now.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (f46b16a) minor tweaks.

* Wed Feb 16 2011 agentzh (章亦春) <agentzh@gmail.com>
- (0e6b831) checked in README.

* Mon Apr 12 2010 agentzh (章亦春) <agentzh@gmail.com>
- (29d0653) various fixes of the blog demo.

* Tue Feb 9 2010 agentzh (章亦春) <agentzh@gmail.com>
- (dd1d50c) now fixed the comment posting functionality for ngx_openresty :D

* Sun Jan 24 2010 agentzh (章亦春) <agentzh@gmail.com>
- (c5a7c04) checked in mising files in the blog demo.

* Sun Jan 24 2010 agentzh (章亦春) <agentzh@gmail.com>
- (3079df6) the blog demo works now.

* Wed Jan 20 2010 agentzh (章亦春) <agentzh@gmail.com>
- (56e75e0) added mysql/load-data.sh

* Wed Jan 20 2010 agentzh (章亦春) <agentzh@gmail.com>
- (abfff86) added util/import-model.pl.

* Wed Jan 20 2010 agentzh (章亦春) <agentzh@gmail.com>
- (c86a4b7) fixed syntax error in init-db.sql

* Wed Jan 20 2010 agentzh (章亦春) <agentzh@gmail.com>
- (2a91d71) checked init-db.sql for the Blog demo.

* Wed Jan 20 2010 agentzh (章亦春) <agentzh@gmail.com>
- (1e4232e) first commit
