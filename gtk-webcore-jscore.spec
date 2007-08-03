%define		snap	125
Summary:	Port of JavaScriptCore JavaScript interpreter to GTK+
Summary(pl.UTF-8):	Port interpretera JavaScriptu JavaScriptCore do GTK+
Name:		gtk-webcore-jscore
Version:	0.5.3
Release:	0.%{snap}.1
License:	LGPL v2+
Group:		Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	1c87fa5d754e9ce7957c3f52f73301fe
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-webcore-jscore is a port of the JavaScriptCore JavaScript
interpreter to GTK+. JavaScriptCore is a component of Apple's WebCore
HTML rendering engine which is in turn a port of the KDE project's
KHTML rendering engine. The KHTML JavaScript interpreter is KJS.

%description -l pl.UTF-8
gtk-webcore-jscore to port interpretera JavaScriptu JavaScriptCore do
GTK+. JavaScriptCore to element silnika renderującego HTML WebCore
firmy Apple, będącego z kolei portem silnika renderującego KHTML z
projektu KDE. Interpreter Javascriptu w KHTML to KJS.

%package libs
Summary:	Shared library for gtk-webcore-jscore
Summary(pl.UTF-8):	Biblioteka współdzielona gtk-webcore-jscore
Group:		Libraries
Requires:	glib2 >= 1:2.2.0

%description libs
gtk-webcore-jscore is a port of the JavaScriptCore JavaScript
interpreter to GTK+. JavaScriptCore is a component of Apple's WebCore
HTML rendering engine which is in turn a port of the KDE project's
KHTML rendering engine. The KHTML JavaScript interpreter is KJS.

%description libs -l pl.UTF-8
gtk-webcore-jscore to port interpretera JavaScriptu JavaScriptCore do
GTK+. JavaScriptCore to element silnika renderującego HTML WebCore
firmy Apple, będącego z kolei portem silnika renderującego KHTML z
projektu KDE. Interpreter Javascriptu w KHTML to KJS.

%package libs-devel
Summary:	Development files for gtk-webcore-jscore
Summary(pl.UTF-8):	Pliki programistyczne gtk-webcore-jscore
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.2.0
Requires:	libstdc++-devel

%description libs-devel
Development files for gtk-webcore-jscore.

%description libs-devel -l pl.UTF-8
Pliki programistyczne gtk-webcore-jscore.

%package libs-static
Summary:	Static gtk-webcore-jscore library
Summary(pl.UTF-8):	Statyczna biblioteka gtk-webcore-jscore
Group:		Development/Libraries
Requires:	%{name}-libs-devel = %{version}-%{release}

%description libs-static
Static gtk-webcore-jscore library.

%description libs-static -l pl.UTF-8
Statyczna biblioteka gtk-webcore-jscore.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog-Gtk+WebCore README-Gtk+WebCore THANKS
%attr(755,root,root) %{_libdir}/libgtk_webcore_jscore.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtk_webcore_jscore.so
%{_libdir}/libgtk_webcore_jscore.la
%{_datadir}/%{name}
%{_includedir}/gtk-webcore
%{_pkgconfigdir}/%{name}.pc

%files libs-static
%defattr(644,root,root,755)
%{_libdir}/libgtk_webcore_jscore.a
