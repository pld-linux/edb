Summary:	Enlightenment Database Access Library
Summary(pl):	Biblioteka Enlightementa dostępu do baz danych
Name:		edb
Version:	1.0.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
URL:		http://www.enlightement.org/
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
Edb jest prostą biblioteką wysokiego poziomu umożliwiającą
dostęp/zapisywanie danych w bazach.

%package devel
Summary:	header files and libraries for %{name} development
Summary(pl):	Pliki nagłówkowe i dokumentacja dla %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and documentation needed for developing %{name} programs.

%description devel -l pl
Pliki nagłówkowe i dokumentacja umożliwiające rozwijanie programów
korzystających z biblioteki %{name}.

%package static
Summary:	Static version of %{name} libraries
Summary(pl):	Statyczna wersja biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of %{name} libraries.

%description static -l pl
Statyczna wersja biblioteki %{name}.

%package gtk
Summary:	GTK editor of databases
Summary(pl):	Edytor baz w GTK
Group:		X11/Applications

%description gtk
GTK editor of databases.

%description gtk -l pl
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

mv $RPM_BUILD_ROOT%{_bindir}/edb_gtk_ed $RPM_BUILD_ROOT%{_x11bindir}/

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
