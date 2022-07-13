%global debug_package %{nil}

%global __strip /bin/true

%global __brp_mangle_shebangs /bin/true

Name: pkg
Epoch: 100
Version: 5.7.0
Release: 1%{?dist}
Summary: Package your Node.js project into an executable
License: MIT
URL: https://github.com/vercel/pkg/tags
Source0: %{name}_%{version}.orig.tar.gz

%description
This command line interface enables you to package your Node.js project
into an executable that can be run even on devices without Node.js
installed.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -t %{buildroot}%{_bindir} usr/bin/pkg

%check

%files
%license LICENSE
%{_bindir}/*

%changelog
