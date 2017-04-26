Name:           dolphin-root-actions
Version:        2.9.1
Release:        1%{?dist}
Summary:        Adds delete, copy, open actions in Dolphin to perform as root.

Group:          Applications/Internet
License:        GPL 2.0
URL:            http://kde-apps.org/content/show.php/Root+Actions+Servicemenu?content=48411
Source0:        https://dl.opendesktop.org/api/files/download/id/1485341541/rootactions_servicemenu_%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       kdebase

%description
Root Actions servicemenu provides a convenient way to perform several actions
'as root', from the right-click context menu in KDE filemanagers.

%prep
%setup -q -c

%build
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/kservices5/ServiceMenus/
install -Dp -m 544 rootactions_servicemenu_%{version}/Root_Actions_%{version}/dolphin-KDE4/*.desktop %{buildroot}/%{_datadir}/kservices5/ServiceMenus/
install -Dp -m 755 rootactions_servicemenu_%{version}/Root_Actions_%{version}/rootactions-servicemenu.pl %{buildroot}/%{_bindir}/rootactions-servicemenu.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/kservices5/ServiceMenus/*.desktop
%{_bindir}/rootactions-servicemenu.pl

%changelog
* Wed Apr 26 2017 Ian Firns <firnsy@kororaproject.org> - 2.9.1-1
- Upgrade to 2.9.1 release.

* Thu May 12 2016 Chris Smart <csmart@kororaproject.org> - 2.9-2
- Fix for Plasma 5

* Thu May 12 2016 Chris Smart <csmart@kororaproject.org> - 2.9-1
- Upgrade to 2.9 release.

* Fri Dec 19 2014 Chris Smart <csmart@kororaproject.org> - 2.8.2-1
- Upgrade to 2.8.2 release.

* Wed Mar 26 2014 Chris Smart <csmart@kororaproject.org> - 2.8.1-1
- Upgrade to 2.8.1 release.

* Mon May 21 2012 Chris Smart <chris@kororaa.org> - 2.7.3-1
- Upgrade to 2.7.3 release.

* Tue Apr 26 2011 Chris Smart <chris@kororaa.org> - 2.7-1
- Upgrade to 2.7 release.

* Sun Apr 03 2011 Chris Smart <chris@kororaa.org> - 2.6.99-1
- Initial spec.

