Summary:	DRBD9 distributed resource management utility
Name:		drbdmanage
Version:	0.99.14
Release:	0.2
License:	GPL v3
Group:		Applications/System
Source0:	https://www.drbd.org/download/drbdmanage/%{name}-%{version}.tar.gz
# Source0-md5:	c0b3cd6a7c26014a0a6a92d82d40446b
URL:		http://oss.linbit.com/drbdmanage
BuildRequires:  help2man
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

%package -n bash-completion-drbdmanage
Summary:	Bash completion for drbdmanage command
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-drbdmanage
Bash completion for drbdmanage command.

%prep
%setup -q

%build
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/drbd.d
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
export NORESTART="yes"
%systemd_post drbdmanaged.service

%preun
%systemd_preun drbdmanaged.service

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/drbdmanage
%attr(755,root,root) %{_bindir}/dbus-drbdmanaged-service
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drbdmanaged.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drbd.d/drbdctrl.res_template
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/drbd.d/drbdmanage-resources.res
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/org.drbd.drbdmanaged.conf
%{_datadir}/dbus-1/system-services/org.drbd.drbdmanaged.service
%{systemdunitdir}/drbdmanaged.service
%{py_sitescriptdir}/drbdmanage
%{py_sitescriptdir}/drbdmanage_client.py[co]
%{py_sitescriptdir}/drbdmanage_server.py[co]
%{py_sitescriptdir}/drbdmanage-%{version}-py*.egg-info
%attr(750,root,root) /var/lib/drbd.d
%{_mandir}/man8/drbdmanage-*
%{_mandir}/man8/drbdmanage.*
%dir %{_localstatedir}/lib/drbdmanage

%files -n bash-completion-drbdmanage
%defattr(644,root,root,755)
/etc/bash_completion.d/drbdmanage
