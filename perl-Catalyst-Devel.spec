#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Devel
Summary:	Catalyst::Devel - Catalyst Development Tools
#Summary(pl.UTF-8):
Name:		perl-Catalyst-Devel
Version:	1.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eb699ccd64718d7c880959831a734599
URL:		http://search.cpan.org/dist/Catalyst-Devel/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Catalyst::Action::RenderView) >= 0.04
BuildRequires:	perl(Catalyst::Plugin::Static::Simple) >= 0.16
BuildRequires:	perl(Config::General) >= 2.42
BuildRequires:	perl(parent)
BuildRequires:	perl-Catalyst >= 5.80000
BuildRequires:	perl-Catalyst-Plugin-ConfigLoader
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-File-ChangeNotify >= 0.07
BuildRequires:	perl-File-Copy-Recursive
BuildRequires:	perl-Module-Install >= 0.91
BuildRequires:	perl-Path-Class >= 0.09
BuildRequires:	perl-Template-Toolkit >= 2.14
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Catalyst-Devel distribution includes a variety of modules useful
for the development of Catalyst applications, but not required to run
them. This is intended to make it easier to deploy Catalyst apps. The
runtime parts of Catalyst are now known as Catalyst::Runtime.

Catalyst-Devel includes the Catalyst::Helper system, which
autogenerates scripts and tests; Module::Install::Catalyst, a
Module::Install extension for Catalyst; and requirements for a variety
of development-related modules. The documentation remains with
Catalyst::Runtime.

# %description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Catalyst/*.pm
%dir %{perl_vendorlib}/Catalyst/Restarter
%{perl_vendorlib}/Catalyst/Restarter/*.pm
%{perl_vendorlib}/Module/Install/*.pm
%{_mandir}/man3/*
