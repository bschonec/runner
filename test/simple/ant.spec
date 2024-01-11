# Usage:   
#
# Download Apache Ant v1.9.0 and build the RPM:
#     rpmbuild -ba --define='_buildver 1.9.0' --undefine=_disable_source_fetch ant.spec
# Download Apache Ant v1.9.7 (this spec file's default) and build the RPM:
#          rpmbuild -ba --undefine=_disable_source_fetch ant.spec

# Don't strip shared object libraries.
%global __os_install_post %{nil}

# Don't autorequire python stuff
%global __requires_exclude ^/usr/bin/(perl|python)$

# From the command line, you can specify what version to package.
# See "usage" above.
%if "0%{?_buildver}" == "0"
%define version 1.9.7
%else
%define version %{_buildver}
%endif

# Override the strange %{dist} behavior on RHEL7 that append the minor version.
%if 0%{?rhel} == 7
  %define dist .el7
%endif 

%define _build_id_links none

Name:		apache-ant
Version:	%{version}
#Release:	1
Release:	1%{?dist}
Summary:	Apache Ant Custom Build for NFII

#Group:		
License:	Apache
URL:		http://ant.apache.org/

Source0:        http://archive.apache.org/dist/ant/binaries/%{name}-%{version}-bin.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Prefix: /usr/local/%{name}

#BuildRequires: systemd-rpm-macros

%description
NFII Apache Ant RPM based installation.

%prep
%setup -q -n %{name}-%{version}

%install

mkdir -p %{buildroot}%{prefix}

cp -R * %{buildroot}%{prefix}

%preun

%clean

#rm -rf %{buildroot}

%files
%{prefix}
#%{prefix}*

%doc


%changelog
