Summary:	Simple DirectMedia Layer - network
Summary(pl):	Biblioteka obs³ugi sieci w SDL
Name:		SDL_net
Version:	1.2.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
URL:		http://www.libsdl.org/projects/SDL_net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libSDL_net1.2

%define		_prefix		/usr/X11R6

%description
This is an example portable network library for use with SDL. Note
that this isn't necessarily how you would want to write a chat
program, but it demonstrates how to use the basic features of the
network and GUI libraries.

%description -l pl
Przyk³adowa biblioteka obs³ugi sieci korzystaj±ca z SDL.

%package devel
Summary:	Header files and more to develop SDL_net applications
Summary(pl):	Pliki na³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_net
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Obsoletes:	libSDL_net1.2-devel

%description devel
Header files and more to develop SDL_net applications.

%description -l pl devel
Pliki na³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_net.

%package static
Summary:	Static SDL_net libraries
Summary(pl):	Statyczne biblioteki SDL_net
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_net libraries.

%description -l pl static
Statyczne biblioteki SDL_net.

%prep
%setup -q 

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
