Summary:	DRBD9 distributed resource management utility
Name:		drbdmanage
Version:	0.97
Release:	0.3
License:	GPL v3
Group:		Applications/System
Source0:	https://www.drbd.org/download/drbdmanage/%{name}-%{version}.tar.gz
# Source0-md5:	3c248e2914bf23abefe1ed7c98498ab6
URL:		http://oss.linbit.com/drbdmanage
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	drbd-utils >= 8.9.4
Requires:	python-dbus
Requires:	python-pygobject
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
drbdmanage is a daemon and a command line utility that manages DRBD9
replicated LVM volumes across a group of machines. It maintains DRBD9
configuration on the participating machines. It creates/deletes the
backing LVM volumes. It automatically places the backing LVM volumes
among the participating machines.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/drbdmanage
%attr(755,root,root) %{_bindir}/dbus-drbdmanaged-service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drbdmanaged.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drbd.d/drbdctrl.res_template
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drbd.d/drbdmanage-resources.res
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.drbd.drbdmanaged.conf
%{_datadir}/dbus-1/system-services/org.drbd.drbdmanaged.service
%{systemdunitdir}/drbdmanaged.service
%{systemdunitdir}/drbdmanaged.socket
%{py_sitescriptdir}/drbdmanage
%{py_sitescriptdir}/drbdmanage_client.py[co]
%{py_sitescriptdir}/drbdmanage_server.py[co]
%{py_sitescriptdir}/drbdmanage-%{version}-py*.egg-info
%dir %{_localstatedir}/lib/drbdmanage

# bash-completion package
/etc/bash_completion.d/drbdmanage
