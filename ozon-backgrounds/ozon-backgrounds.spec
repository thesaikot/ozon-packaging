%global bgname	ozon

Name:           ozon-backgrounds
Version:        21
Release:        1%{?dist}
Summary:        Ozon desktop backgrounds

Group:          Applications/Multimedia
License:        CC-BY-SA

URL:            http://ozonos.github.io
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Desktop backgrounds for Ozon OS.


%prep
%setup -q


%install
%{__install} -d -m755 %{buildroot}%{_datadir}/backgrounds/%{bgname}
%{__cp} -pr * %{buildroot}%{_datadir}/backgrounds/%{bgname}/
%{__install} -d -m755 %{buildroot}%{_datadir}/glib-2.0/schemas/
cat << EOF >>%{buildroot}%{_datadir}/glib-2.0/schemas/20_org.gnome.desktop.background.ozon.gschema.override
[org.gnome.desktop.background]
picture-uri='file://%{_datadir}/backgrounds/%{bgname}/ozon.jpg'
EOF

%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%doc CC-BY-SA-3.0
%{_datadir}/backgrounds/%{bgname}
%{_datadir}/glib-2.0/schemas/20_org.gnome.desktop.background.ozon.gschema.override

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

