%define		_snap	20080813
Summary:	Enlightenment Database Access Library
Summary(pl.UTF-8):	Biblioteka Enlightementa dostępu do baz danych
Name:		edb
Version:	1.0.5.043
Release:	0.%{_snap}.4
License:	BSD
Group:		Libraries
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	e5d58d14f0333b2b292a23153cee8da3
URL:		http://enlightenment.org/Libraries/Edb/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
# only for configure
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Edb is a simple, clean high-level db access/storage library.

%description -l pl.UTF-8
Edb jest prostą biblioteką wysokiego poziomu umożliwiającą
dostęp/zapisywanie danych w bazach.

%package devel
Summary:	Header files and libraries for edb development
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla edb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentation needed for developing edb programs.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja umożliwiające rozwijanie programów
korzystających z biblioteki edb.

%package static
Summary:	Static version of edb library
Summary(pl.UTF-8):	Statyczna wersja biblioteki edb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of edb library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki edb.

%package gtk
Summary:	GTK+ editor of databases
Summary(pl.UTF-8):	Edytor baz oparty na GTK+
Group:		X11/Applications

%description gtk
GTK+ editor of databases.

%description gtk -l pl.UTF-8
Edytor baz danych oparty na GTK+.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"; export CFLAGS
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk \
	--enable-ncurses

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_bindir}/edb_ed
%attr(755,root,root) %{_bindir}/edb_vt_ed
%attr(755,root,root) %{_libdir}/libedb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libedb.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedb.so
%{_libdir}/libedb.la
%{_includedir}/Edb.h
%{_pkgconfigdir}/edb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libedb.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edb_gtk_ed
