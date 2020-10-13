Name:           msoar.helper
Version:        1.0
Release:        4
Summary:        Helper Package for demisto with all dependencies and files provided by SIX

Group:          Platform-engineers
BuildArch:      x86_64
License:        Proprietary. Based on a contract.

#BuildRequires:
Requires(pre):  shadow-utils, /usr/sbin/useradd, /usr/sbin/groupadd, /usr/bin/getent, /usr/bin/chage
Requires:       rpm-build samba samba-client samba-common-tools libcap file-devel fontconfig expat libpng freetype lsof cloud-utils-growpart gdisk

%description
Helper Package for Cortex XSOAR with all dependencies and files provided by SIX.
Will install all required settinds to run demisto on a RHEL or Centos v7 or v8 physical or virtial machine.
Requires only plain RHEL and docker EE or Docker CE.

%prep
# Create the build structure so we can use the build command on any system without preparation.
mkdir -p ~/rpmbuild/BUILD
mkdir -p ~/rpmbuild/BUILDROOT
mkdir -p ~/rpmbuild/RPMS
mkdir -p ~/rpmbuild/SOURCES
mkdir -p ~/rpmbuild/SPECS
mkdir -p ~/rpmbuild/SRPMS

%build
### Collect all the files from the current system
# Sudoers
  cp /etc/sudoers .
  cp /etc/sudoers.d/user .
  cp /etc/sudoers.d/demisto sudoers.demisto
# Sysconfig
  cp /etc/selinux/config selinux.config
  cp /etc/profile.d/98_profile.sh .
  cp /etc/profile.d/99_defaults.sh .
# Sysctl
  cp /etc/sysctl.d/999-demisto.conf .
# demisto Home
  cp /home/demisto/.bash_profile demisto.bash_profile
# Conf-files
  cp /opt/demisto/templates/demisto.conf .
  cp /opt/demisto/templates/msoar.helper.spec .
# Install Files
  cp /opt/demisto/install/installer.hint.txt .
# Syslog
  cp /etc/rsyslog.d/demisto.conf demisto.rsyslog.conf
# SSHD
  cp /etc/ssh/sshd_config .
# MOTD
  cp /etc/motd .
    cp /etc/issue.net .
  cp /etc/issue .
# Limits
  cp /etc/security/limits.d/10-demisto.conf .
# Scripts
  cp /opt/demisto/scripts/testmode.sh .
  cp /opt/demisto/scripts/boltbrowser.linux64 .
# Backup
  cp /opt/demisto/scripts/demisto.backup.sh .
  cp /etc/systemd/system/demisto.backup.service .
  cp /etc/systemd/system/demisto.backup.timer .




%pre
### Create the demisto user - if not already there
# Install User and Groups -> UID / GID are fixed and represents the according user from the Dom01 AD.
# Disable selinux
  test -x /usr/sbin/setenforce && /usr/sbin/setenforce 0
# Note there is no userdel on this RPM - It is not recommended to remove technical users in a RPM (even in the remove part).
  getent group demisto > /dev/null || groupadd demisto -frg 3271
  getent passwd demisto > /dev/null || useradd -rmog demisto -G docker -u 3271 -d /home/demisto -s /bin/bash demisto
  getent group user > /dev/null || groupadd user -frg 1000
  getent passwd user > /dev/null || useradd -rmog user -G wheel -u 1000 -d /home/user -s /bin/bash user
# For tecnical users the password will not expire - the user cannot be used for interactive password based logins
  chage -I -1 -m 0 -M 99999 -E -1 demisto




%install
# Create helper folders - Hint: those folders are here already in the target system - but we need to create them for BUILDROOT
  install -d $RPM_BUILD_ROOT/etc
  install -d $RPM_BUILD_ROOT/etc/ssh
  install -d $RPM_BUILD_ROOT/etc/profile.d
  install -d $RPM_BUILD_ROOT/etc/security/limits.d
  install -d $RPM_BUILD_ROOT/etc/selinux
  install -d $RPM_BUILD_ROOT/etc/sudoers.d
  install -d $RPM_BUILD_ROOT/etc/systemd/system
  install -d $RPM_BUILD_ROOT/etc/sysctl.d
  install -d $RPM_BUILD_ROOT/etc/rsyslog.d
# Create helper home dirs
  install -d $RPM_BUILD_ROOT/home/demisto
  install -d $RPM_BUILD_ROOT/home/demisto/.ssh
  install -d $RPM_BUILD_ROOT/home/user
  install -d $RPM_BUILD_ROOT/home/user/.ssh
  # Create Demisto Folders
  install -d $RPM_BUILD_ROOT/opt/demisto
  install -d $RPM_BUILD_ROOT/opt/demisto/install
  install -d $RPM_BUILD_ROOT/opt/demisto/templates
  install -d $RPM_BUILD_ROOT/opt/demisto/scripts
  install -d $RPM_BUILD_ROOT/home/demisto/.ssh
# Install the Files
  install sudoers $RPM_BUILD_ROOT/etc/sudoers.demisto
  install user $RPM_BUILD_ROOT/etc/sudoers.d/user
  install sudoers.demisto $RPM_BUILD_ROOT/etc/sudoers.d/demisto
# Sysconfig
  install selinux.config $RPM_BUILD_ROOT/etc/selinux/config
  install 98_profile.sh $RPM_BUILD_ROOT/etc/profile.d/98_profile.sh
  install 99_defaults.sh $RPM_BUILD_ROOT/etc/profile.d/99_defaults.sh
# Sysctl
  install 999-demisto.conf $RPM_BUILD_ROOT/etc/sysctl.d/999-demisto.conf
# demisto Home
  install demisto.bash_profile $RPM_BUILD_ROOT/home/demisto/.bash_profile
# Conf-files
  install demisto.conf $RPM_BUILD_ROOT/opt/demisto/templates/demisto.conf
  install demisto.conf $RPM_BUILD_ROOT/etc/demisto.conf
  install msoar.helper.spec $RPM_BUILD_ROOT/opt/demisto/templates/msoar.helper.spec
# Instaler files
  install installer.hint.txt $RPM_BUILD_ROOT/opt/demisto/install/installer.hint.txt
# Syslog
  install demisto.rsyslog.conf $RPM_BUILD_ROOT/etc/rsyslog.d/demisto.conf
# SSHD
  install sshd_config $RPM_BUILD_ROOT/etc/ssh/sshd_config.demisto
# MOTD
  install motd $RPM_BUILD_ROOT/etc/motd.demisto
  install issue.net $RPM_BUILD_ROOT/etc/issue.net.demisto
  install issue $RPM_BUILD_ROOT/etc/issue.demisto
# Limits
  install 10-demisto.conf $RPM_BUILD_ROOT/etc/security/limits.d/10-demisto.conf
# scripts
  install boltbrowser.linux64 $RPM_BUILD_ROOT/opt/demisto/scripts/boltbrowser.linux64
  install testmode.sh $RPM_BUILD_ROOT/opt/demisto/scripts/testmode.sh
# Backup
  install demisto.backup.sh $RPM_BUILD_ROOT/opt/demisto/scripts/demisto.backup.sh
  install demisto.backup.service $RPM_BUILD_ROOT/etc/systemd/system/demisto.backup.service
  install demisto.backup.timer $RPM_BUILD_ROOT/etc/systemd/system/demisto.backup.timer
  
  %clean
# Copy the RPM to the /opt/demisto/install folder.
mkdir -p /opt/demisto/install
find %{_rpmdir} -name "*rpm" | xargs chmod 666
find %{_rpmdir} -name "*rpm" | xargs chown demisto:demisto
find %{_rpmdir} -name "*rpm" | xargs -I $$ mv $$ /opt/demisto/install
set +x
echo
echo
echo
echo "*************************************************************************************************"
echo "please fid the RPM here: /opt/demisto/install"
echo "*************************************************************************************************"
echo "Here is a list of the rpm files:"
ls -lahs /opt/demisto/install/*help*rpm
echo "*************************************************************************************************"



%files
#Sudoers
                     %attr(440, root, root) /etc/sudoers.demisto
                     %attr(440, root, root) /etc/sudoers.d/user
                     %attr(440, root, root) /etc/sudoers.d/demisto
# Sysconfig
                     %attr(644, root, root) /etc/selinux/config
                     %attr(644, root, root) /etc/profile.d/98_profile.sh
                     %attr(644, root, root) /etc/profile.d/99_defaults.sh
# Sysctl
                     %attr(644, root, root) /etc/sysctl.d/999-demisto.conf
# user HOME
                %dir %attr(755, user, user) /home/demisto
                %dir %attr(700, user, user) /home/demisto/.ssh
# demisto Home
                %dir %attr(755, demisto, demisto) /home/demisto
                     %attr(644, demisto, demisto) /home/demisto/.bash_profile
                %dir %attr(700, demisto, demisto) /home/demisto/.ssh
# Conf-files
                %dir %attr(755, demisto, demisto) /opt/demisto
                %dir %attr(755, demisto, demisto) /opt/demisto/install
                     %attr(644, demisto, demisto) /opt/demisto/install/installer.hint.txt
                %dir %attr(755, demisto, demisto) /opt/demisto/templates
                     %attr(644, demisto, demisto) /opt/demisto/templates/demisto.conf
                     %attr(644, demisto, demisto) /etc/demisto.conf
                     %attr(644, demisto, demisto) /opt/demisto/templates/msoar.helper.spec
# Syslog
                     %attr(644, root, root) /etc/rsyslog.d/demisto.conf
# SSHD
  %config(missingok) %attr(600, root, root) /etc/ssh/sshd_config.demisto
# MOTD
  %config(missingok) %attr(644, root, root) /etc/motd.demisto
  %config(missingok) %attr(644, root, root) /etc/issue.net.demisto
  %config(missingok) %attr(644, root, root) /etc/issue.demisto
# Limits
                     %attr(644, root, root) /etc/security/limits.d/10-demisto.conf
# Scripts
                     %attr(644, demisto, demisto) /opt/demisto/scripts/testmode.sh
                     %attr(755, demisto, demisto) /opt/demisto/scripts/boltbrowser.linux64
# Backup
                     %attr(644, demisto, demisto) /opt/demisto/scripts/demisto.backup.sh
                     %attr(644, demisto, demisto) /etc/systemd/system/demisto.backup.service
                     %attr(644, demisto, demisto) /etc/systemd/system/demisto.backup.timer


#%doc

%post
sysctl --system
systemctl daemon-reload
systemctl restart rsyslog
systemctl disable demisto.backup.timer
cp /etc/motd.demisto /etc/motd
cp /etc/issue.net.demisto  /etc/issue.net
cp /etc/issue.demisto /etc/issue
cp /etc/shells.demisto /etc/shells
cp /etc/sudoers.demisto /etc/sudoers
cp /etc/ssh/sshd_config.demisto /etc/ssh/sshd_config


%changelog
* Thu Apr 30 2020 Alexander Huser 1.0.4
        - Initial Release     

  
