Summary:	Simple DirectMedia Layer - network
Summary(pl.UTF-8):	Biblioteka obsługi sieci w SDL
Summary(pt_BR.UTF-8):	Simple DirectMedia Layer - Biblioteca de rede portável
Name:		SDL_net
Version:	1.2.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
# Source0-md5:	7be5b9ef36129ee187ace96906cd264c
URL:		http://www.libsdl.org/projects/SDL_net/
BuildRequires:	SDL-devel >= 1.2.5-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libSDL_net1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an example portable network library for use with SDL. Note
that this isn't necessarily how you would want to write a chat
program, but it demonstrates how to use the basic features of the
network and GUI libraries.

%description -l pl.UTF-8
Przykładowa biblioteka obsługi sieci korzystająca z SDL.

%description -l pt_BR.UTF-8
Esta é uma biblioteca portável de rede para uso com o SDL.

%package devel
Summary:	Header files and more to develop SDL_net applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL_net
Summary(pt_BR.UTF-8):	Cabeçalhos para desenvolver programas utilizando a SDL_net
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.5-2
Obsoletes:	libSDL_net1.2-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use SDL_net.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowepotzrebne przy rozwijania aplikacji
używających SDL_net.

%description devel -l pt_BR.UTF-8
Este pacote contém os cabeçalhos que programadores vão precisar para
desenvolver aplicações utilizando a SDL_net.

%package static
Summary:	Static SDL_net libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_net
Summary(pt_BR.UTF-8):	Biblioteca estática para desenvolvimento utilizando a SDL_net
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Statis SDL_net libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_net.

%description static -l pt_BR.UTF-8
Este pacote contém a biblioteca estática que programadores vão
precisar para desenvolver aplicações linkados estaticamente com a
SDL_net.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
