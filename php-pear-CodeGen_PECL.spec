%define		_class		CodeGen
%define		_subclass	PECL
%define		_status		stable
%define		_pearname	CodeGen_PECL

Summary:	%{_pearname} - Tool to generate PECL extensions from an XML description
Summary(pl.UTF-8):	%{_pearname} - narzędzie do generowania rozszerzeń PECL z opisu XML
Name:		php-pear-%{_pearname}
Version:	1.1.3
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6e5979ac00ec542f73f8e2d093c104bc
URL:		http://pear.php.net/package/CodeGen_PECL
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0
Requires:	php-pear
Requires:	php-pear-CodeGen >= 1.0.5
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

%description -l pl.UTF-8
CodeGen_PECL (wcześniej znany jako PECL_Gen) to napisany w czystym PHP
zamiennik skryptów powłoki ext_skel dostarczanych ze źródłami PHP 4.
Odczytuje opcje konfiguracyjne, prototypy funkcji i fragmenty kodu z
pliku opisu XML, a następnie generuje pełne, gotowe do skompilowania
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
%{php_pear_dir}/CodeGen/PECL
