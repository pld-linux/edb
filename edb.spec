Summary:	Enlightenment Database Access Library
Summary(pl):	Biblioteka Enlightementa dostępu do baz danych
Name:		edb
Version:	1.0.5
%define	_snap	20050309
Release:	1.%{_snap}.0.1
License:	LGPL
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:        ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{_snap}.tar.gz
# Source0-md5:	afe1bc2c08e7a3de5b624856e56d69f5
Patch0:		%{name}-ac_fix.patch
URL:		http://www.enlightement.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Edb is a simple, clean high-level db access/storage library.

%description -l pl
Edb jest prostą biblioteką wysokiego poziomu umożliwiającą
dostęp/zapisywanie danych w bazach.

%package devel
Summary:	Header files and libraries for edb development
Summary(pl):	Pliki nagłówkowe i dokumentacja dla edb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentation needed for developing edb programs.

%description devel -l pl
Pliki nagłówkowe i dokumentacja umożliwiające rozwijanie programów
korzystających z biblioteki edb.

%package static
Summary:	Static version of edb library
Summary(pl):	Statyczna wersja biblioteki edb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of edb library.

%description static -l pl
Statyczna wersja biblioteki edb.

%package gtk
Summary:	GTK+ editor of databases
Summary(pl):	Edytor baz w GTK+
Group:		X11/Applications

%description gtk
GTK+ editor of databases.

%description gtk -l pl
Edytor baz danych w GTK+.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"; export CFLAGS
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-cxx \
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
%doc AUTHORS
%attr(755,root,root) %{_bindir}/edb_ed
%attr(755,root,root) %{_bindir}/edb_vt_ed
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edb-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/Edb.h
%{_pkgconfigdir}/edb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edb_gtk_ed
