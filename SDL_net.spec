Summary:	Simple DirectMedia Layer - network
Summary(pl):	Biblioteka obs�ugi sieci w SDL
Name:		SDL_net
Version:	1.2.3
Release:	2
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
URL:		http://www.libsdl.org/projects/SDL_net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This is an example portable network library for use with SDL. Note
that this isn't necessarily how you would want to write a chat
program, but it demonstrates how to use the basic features of the
network and GUI libraries.

%description -l pl
Przyk�adowa biblioteka obs�ugi sieci korzystaj�ca z SDL.

%package devel
Summary:	Header files and more to develop SDL_net applications
Summary(pl):	Pliki na��wkowe do rozwijania aplikacji u�ywaj�cych SDL_net
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_net applications.

%description -l pl devel
Pliki na��wkowe do rozwijania aplikacji u�ywaj�cych SDL_net.

%package static
Summary:	Static SDL_net libraries
Summary(pl):	Statyczne biblioteki SDL_net
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_net libraries.

%description -l pl static
Statyczne biblioteki SDL_net.

%prep
%setup -q 

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
