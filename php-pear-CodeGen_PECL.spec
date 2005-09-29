%include	/usr/lib/rpm/macros.php
%define		_class		CodeGen
%define		_subclass	PECL
%define		_status		beta
%define		_pearname	CodeGen_PECL

Summary:	%{_pearname} - Tool to generate PECL extensions from an XML description
Name:		php-pear-%{_pearname}
Version:	1.0.0
%define	_rc rc1
%define	_rel 0.1
Release:	%{_rc}.%{_rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	15abd632ab1bb575a73950ed89a3c4b2
URL:		http://pear.php.net/package/CodeGen_PECL
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.2
Requires:	php-pear-CodeGen >= 0.9
Obsoletes:	php-pear-PECL_Gen
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CodeGen_PECL (formerly known as PECL_Gen) is a pure PHP replacement
for the ext_skel shell script that comes with the PHP 4 source. It
reads in configuration options, function prototypes and code fragments
from an XML description file and generates a complete ready-to-compile
PECL extension.

In PEAR status of this package is: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
cp -a ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%attr(755,root,root) %{_bindir}/pecl-gen
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
