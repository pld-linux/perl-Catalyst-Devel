#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Devel
Summary:	Catalyst::Devel - Catalyst Development Tools
Summary(pl.UTF-8):	Catalyst::Devel - narzędzia programistyczne Catalyst
Name:		perl-Catalyst-Devel
Version:	1.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ea62cae2d555bad770d92359a7df641
URL:		http://search.cpan.org/dist/Catalyst-Devel/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.7000
BuildRequires:	perl-Catalyst-Action-RenderView >= 0.04
BuildRequires:	perl-Catalyst-Plugin-ConfigLoader
BuildRequires:	perl-Catalyst-Plugin-Static-Simple >= 0.14
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-File-Copy-Recursive
BuildRequires:	perl-Module-Install >= 0.63
BuildRequires:	perl-Path-Class >= 0.09
BuildRequires:	perl-Template-Toolkit >= 2.14
BuildRequires:	perl-YAML >= 0.55
BuildRequires:	perl-parent
%endif
Requires:	perl-Catalyst-Plugin-ConfigLoader
Suggests:	perl-Catalyst-Manual
Suggests:	perl-Catalyst-View-TT
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Catalyst::Devel package includes a variety of modules useful for
the development of Catalyst applications, but not required to run
them. This is intended to make it easier to deploy Catalyst apps. The
runtime parts of Catalyst are now known as Catalyst::Runtime. 

Catalyst::Devel includes the Catalyst::Helper system, which
autogenerates scripts and tests; Module::Install::Catalyst, a
Module::Install extension for Catalyst; and requirements for a
variety of development-related modules. The documentation remains with
Catalyst::Runtime.

%description -l pl.UTF-8
Pakiet Catalyst::Devel zawiera wiele różnych modułów przydatnych przy
tworzeniu aplikacji Catalysta, ale nie wymaganych do ich uruchamiania.
Jego celem jest ułatwienie tworzenia aplikacji Catalysta. Elementy
uruchomieniowe Catalysta są znane jako Catalyst::Runtime.

Catalyst::Devel zawiera: system Catalyst::Helper automatycznie
generujący skrypty i testy, Module::Install::Catalyst - rozszerzenie
Module::Install dla Catalysta oraz zależności od wielu różnych modułów
związanych z tworzeniem aplikacji. Dokumentacja pozostaje w
Catalyst::Runtime.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
# ??? there were duplicates
#%{perl_vendorlib}/Catalyst/*.pm
%{perl_vendorlib}/Catalyst/*
%{perl_vendorlib}/Module/Install/*
%{_mandir}/man3/*
