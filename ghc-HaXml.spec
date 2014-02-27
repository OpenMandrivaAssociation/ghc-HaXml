%define debug_package %{nil}
%define module HaXml

Summary:	Utilities for manipulating XML documents for Haskell
Name:		ghc-%{module}
Version:	1.23.3
Release:	2
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(polyparse)
BuildRequires:	haskell(random)
Requires(post,postun):	ghc
Requires(pre):	haskell(polyparse)
Requires(pre):	haskell(random)
Obsoletes:	haskell-%{module} < 1.23.3-2

%description
Haskell utilities for parsing, filtering, transforming and generating XML
documents.

%files
%{_bindir}/*
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

