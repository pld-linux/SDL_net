Summary:	Simple DirectMedia Layer - network
Summary(pl):	Biblioteka obs³ugi sieci w SDL
Summary(pt_BR):	Simple DirectMedia Layer - Biblioteca de rede portável
Name:		SDL_net
Version:	1.2.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
URL:		http://www.libsdl.org/projects/SDL_net/
BuildRequires:	SDL-devel >= 1.2.5-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libSDL_net1.2

%description
This is an example portable network library for use with SDL. Note
that this isn't necessarily how you would want to write a chat
program, but it demonstrates how to use the basic features of the
network and GUI libraries.

%description -l pl
Przyk³adowa biblioteka obs³ugi sieci korzystaj±ca z SDL.

%description -l pt_BR
Esta é uma biblioteca portável de rede para uso com o SDL.

%package devel
Summary:	Header files and more to develop SDL_net applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_net
Summary(pt_BR):	Cabeçalhos para desenvolver programas utilizando a SDL_net
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Obsoletes:	libSDL_net1.2-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use SDL_net.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowepotzrebne przy rozwijania aplikacji
u¿ywaj±cych SDL_net.

%description devel -l pt_BR
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL_net.

%package static
Summary:	Static SDL_net libraries
Summary(pl):	Statyczne biblioteki SDL_net
Summary(pt_BR):	Biblioteca estática para desenvolvimento utilizando a SDL_net
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_net libraries.

%description static -l pl
Statyczne biblioteki SDL_net.

%description static -l pt_BR
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
SDL_net.

%prep
%setup -q

%build
#rm -f missing
#%%{__libtoolize}
#%%{__aclocal}
%{__autoconf}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
