%define		snap	125
Summary:	Port of JavaScriptCore JavaScript interpreter to GTK+
Name:		gtk-webcore-jscore
Version:	0.5.3
Release:	0.%{snap}.1
License:	LGPL
Group:		X11/Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	1c87fa5d754e9ce7957c3f52f73301fe
URL:		http://gtk-webcore.sourceforge.net/
BuildRequires:	/usr/bin/perl
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk-webcore-jscore is a port of the JavaScriptCore JavaScript
interpreter to GTK+. JavaScriptCore is a component of Apple's WebCore
HTML rendering engine which is in turn a port of the KDE project's
KHTML rendering engine. The KHTML JavaScript interpreter is KJS.

%package libs
Summary:	Shared library for gtk-webcore-jscore
Group:		X11/Development/Libraries

%description libs
gtk-webcore-jscore is a port of the JavaScriptCore JavaScript
interpreter to GTK+. JavaScriptCore is a component of Apple's WebCore
HTML rendering engine which is in turn a port of the KDE project's
KHTML rendering engine. The KHTML JavaScript interpreter is KJS.

%package libs-devel
Summary:	Development library for gtk-webcore-jscore
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
gtk-webcore-jscore is a port of the JavaScriptCore JavaScript
interpreter to GTK+. JavaScriptCore is a component of Apple's WebCore
HTML rendering engine which is in turn a port of the KDE project's
KHTML rendering engine. The KHTML JavaScript interpreter is KJS.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files libs-devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog-Gtk+WebCore README-Gtk+WebCore THANKS
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_datadir}/%{name}
%{_includedir}/gtk-webcore
%{_pkgconfigdir}/%{name}.pc
