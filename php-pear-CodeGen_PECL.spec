%include	/usr/lib/rpm/macros.php
%define		_class		CodeGen
%define		_subclass	PECL
%define		_status		stable
%define		_pearname	CodeGen_PECL

Summary:	%{_pearname} - Tool to generate PECL extensions from an XML description
Summary(pl):	%{_pearname} - narzêdzie do generowania rozszerzeñ PECL z opisu XML
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0e8fce6c3773483f937de9a13dff83ba
URL:		http://pear.php.net/package/CodeGen_PECL
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0
Requires:	php-pear
Requires:	php-pear-CodeGen = 1.0.2
Requires:	php-pear-PEAR-core >= 1:1.2
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

%description -l pl
CodeGen_PECL (wcze¶niej znany jako PECL_Gen) to napisany w czystym PHP
zamiennik skryptów pow³oki ext_skel dostarczanych ze ¼ród³ami PHP 4.
Odczytuje opcje konfiguracyjne, prototypy funkcji i fragmenty kodu z
pliku opisu XML, a nastêpnie generuje pe³ne, gotowe do skompilowania
rozszerzenie PECL.

Ta klasa ma w PEAR status: %{_status}.

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
