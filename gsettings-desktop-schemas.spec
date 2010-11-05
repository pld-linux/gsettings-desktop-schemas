Summary:	A collection of GSettings schemas
Summary(pl.UTF-8):	Zbiór schematów GSettings
Name:		gsettings-desktop-schemas
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gsettings-desktop-schemas/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	468faa60c2d82e02113849c1fda47efa
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	intltool >= 0.40.0
Requires(post,postun):	glib2 >= 1:2.26.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of GSettings schemas.

%description -l pl.UTF-8
Zbiór schematów GSettings.

%package devel
Summary:	Development files for gsettings-desktop-schemas
Summary(pl.UTF-8):	Pliki programistyczne dla gsettings-desktop-schemas
Group:		Development/Libraries

%description devel
Development files for gsettings-desktop-schemas.

%description devel -l pl.UTF-8
Pliki programistyczne dla gsettings-desktop-schemas.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%postun
if [ "$1" = "0" ]; then
	%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README
%{_datadir}/GConf/gsettings/gsettings-desktop-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.sound.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.thumbnail-cache.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.system.proxy.gschema.xml

%files devel
%defattr(644,root,root,755)
%{_includedir}/gsettings-desktop-schemas
%{_npkgconfigdir}/gsettings-desktop-schemas.pc
