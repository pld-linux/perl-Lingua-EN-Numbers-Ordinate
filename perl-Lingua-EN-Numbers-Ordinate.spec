#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	EN-Numbers-Ordinate
Summary:	Lingua::EN::Numbers::Ordinate - go from cardinal number (3) to ordinal ("3rd")
Summary(pl.UTF-8):	Lingua::EN::Numbers::Ordinate - zamiana liczebników głównych (3) na porządkowe (3rd)
Name:		perl-Lingua-EN-Numbers-Ordinate
Version:	1.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e92078fafd9108a137972c4e9bae9e99
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There are two kinds of numbers in English - cardinals (1, 2, 3...),
and ordinals (1st, 2nd, 3rd...). This library provides functions for
giving the ordinal form of a number, given its cardinal value.

%description -l pl.UTF-8
W języku angielskim są dwa rodzaje liczebników - główne (cardinals: 1,
2, 3...) oraz porządkowe (ordinals: 1st, 2nd, 3rd...). Ta biblioteka
udostępnia funkcje do uzyskiwania formy porządkowej z formy głównej.

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
%doc ChangeLog README
%dir %{perl_vendorlib}/Lingua/EN/Numbers
%{perl_vendorlib}/Lingua/EN/Numbers/Ordinate.pm
%{_mandir}/man3/*
