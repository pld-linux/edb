Summary:	Enlightenment Database Access Library
Summary(pl):	Biblioteka Enlightementa dostêpu do baz danych 
Name:		edb
Version:	1.0.2
Release:	1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	LGPL
URL:		http://www.enlightement.org/
Source0:	http://prdownloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_x11prefix	%{_prefix}/X11R6
%define		_x11bindir	%{_x11prefix}/bin

%description
Edb is a simple, clean high-level db access/storage library.

%description -l pl
Edb jest prost± bibliotek± wysokiego poziomu umo¿liwiaj±c±
dostêp/zapisywanie danych w bazach.

%package devel
Summary:	header files and libraries for %{name} development
Summary(pl):	Pliki nag³ówkowe i dokumentacja dla %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Pliki nag³ówkowe i dokumentacja umo¿liwiaj±ce rozwijanie programów
korzystaj±cych z biblioteki %{name}.

%package static
Summary:	Static version of %{name} libraries
Summary(pl):	Statyczna wersja biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static version of %{name} libraries.

%description -l pl
Statyczna wersja biblioteki %{name}.

%package gtk
Summary:	GTK editor of databases
Summary(pl):	Edytor baz w GTK
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje

%description gtk
GTK editor of databases.

%description -l pl gtk
Edytor baz danych w GTK.

%prep
%setup -q

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure \
	--enable-cxx

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_x11bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/edb_gtk_ed \
   $RPM_BUILD_ROOT%{_x11bindir}/

gzip -9nf AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/edb_ed
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files gtk
%defattr(644,root,root,755)
%{_x11bindir}/*
