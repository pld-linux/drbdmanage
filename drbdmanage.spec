Summary:    DRBD9 distributed resource management utility
Name:       drbdmanage
Version:    0.97
Release:    0.2
Source0:    https://www.drbd.org/download/drbdmanage/%{name}-%{version}.tar.gz
URL:        http://oss.linbit.com/drbdmanage
License:    GPL v3
Group:      Applications/System
Requires:   drbd-utils >= 8.9.4
Requires:   python-dbus
Requires:   python-pygobject
BuildArch:  noarch
BuildRoot:  %{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
drbdmanage is a daemon and a command line utility that manages DRBD9
replicated LVM volumes across a group of machines.
It maintains DRBD9 configuration on the participating machines. It
creates/deletes the backing LVM volumes. It automatically places
the backing LVM volumes among the participating machines.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
    --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/drbdmanage
%attr(755,root,root) %{_bindir}/dbus-drbdmanaged-service
#%{_mandir}/man8/drbdmanage-*
#%{_mandir}/man8/drbdmanage.*
%{_datadir}/dbus-1/system-services/org.drbd.drbdmanaged.service
%config %{_sysconfdir}/dbus-1/system.d/org.drbd.drbdmanaged.conf
%config %{_sysconfdir}/drbd.d/drbdctrl.res_template
%config(noreplace) %{_sysconfdir}/drbd.d/drbdmanage-resources.res
%config(noreplace) %{_sysconfdir}/drbdmanaged.cfg
%{_localstatedir}/lib/drbdmanage
%dir %{_sysconfdir}/dbus-1/
%dir %{_sysconfdir}/dbus-1/system.d/
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system-services/
%{systemdunitdir}/drbdmanaged.service
%{systemdunitdir}/drbdmanaged.socket
%{py_sitescriptdir}/*.py
%{py_sitescriptdir}/*.py?
%{py_sitescriptdir}/drbdmanage
%{py_sitescriptdir}/drbdmanage-%{version}-py*.egg-info

#%files -n 
#%config %{_sysconfdir}/bash_completion.d/drbdmanage


