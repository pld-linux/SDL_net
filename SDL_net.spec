%define name SDL_net
%define version 1.0.2
%define release 1mdk

Summary: Simple DirectMedia Layer - network
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: SDL_net-1.0.1-newm4libtoolize.patch.bz2
Copyright: LGPL
Group: System/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://www.devolution.com/~slouken/SDL/projects/SDL_net/
Prefix: %{_prefix}
Requires: SDL >= 1.0

%description
This is an example portable network library for use with SDL. Note that this
isn't necessarily how you would want to write a chat program, but it
demonstrates how to use the basic features of the network and GUI libraries.

%package devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C
Requires: %{name}
Requires: SDL-devel

%description devel
This is an example portable network library for use with SDL. Note that this
isn't necessarily how you would want to write a chat program, but it
demonstrates how to use the basic features of the network and GUI libraries.

The API can be found in the file SDL_net.h

%prep
rm -rf ${RPM_BUILD_ROOT}

%setup 
%patch0 -p1

%build
aclocal
autoconf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING
%{prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%doc README COPYING
%{prefix}/lib/*a
%{prefix}/include/SDL/
%{prefix}/lib/lib*.so

%changelog
* Fri Jun 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- v1.0.2

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-5mdk
- Use makeinstall macros.

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-4mdk
- Fix m4 macros with new libtoolize.
- Use configure macro.

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-2mdk
- added url
- fixed group
- some minor package build fixes
- built against stable SDL version, previous was using 1.1.x devel

* Fri Feb 11 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Hakan Tandogan <hakan@iconsult.com> 

* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file
