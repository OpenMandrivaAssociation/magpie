%define upstream_name    App-Magpie
%define upstream_version 1.113320

Name:       magpie
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    MAGeia Perl Integration Easy
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::Cmd::Setup)
BuildRequires: perl(CPAN::Mini)
BuildRequires: perl(Config::Tiny)
BuildRequires: perl(Encode)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::HomeDir::PathClass)
BuildRequires: perl(File::ShareDir) >= 1.0.0
BuildRequires: perl(File::ShareDir::PathClass)
BuildRequires: perl(File::Temp)
BuildRequires: perl(File::pushd)
BuildRequires: perl(Find::Lib)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Log::Dispatchouli)
BuildRequires: perl(Module::Build) >= 0.360.100
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::SemiAffordanceAccessor)
BuildRequires: perl(MooseX::Singleton)
BuildRequires: perl(Parse::CPAN::Meta) >= 1.440.100
BuildRequires: perl(Parse::CPAN::Packages::Fast)
BuildRequires: perl(Path::Class) >= 0.220.0
BuildRequires: perl(Proc::ParallelLoop)
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(Text::Padding)
BuildRequires: perl(URPM)
BuildRequires: perl(strict)
BuildRequires: perl(version)
BuildRequires: perl(warnings)
BuildRequires: perl-version >= 1:0.870.0
BuildArch:  noarch

Requires:   bm
Requires:   mgarepo
%description
CPAN holds a lot of great modules - but it can be difficult for the user to
install if she's not familiar with the process. Therefore, Linux
distribution usually package quite a lot of them, for them to be easily
installable.

Mageia Linux is no exception, and ships more than 2500 packages holding
Perl distributions (at the time of writing). Maintaining those packages is
a daunting task - and cannot be done only by hand.

This distribution is therefore a set of scripts helping maintaining Perl
packages within Mageia. They can be somehow coupled or used independently.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml README
%{_bindir}/magpie
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*

