%define shortname emerald
%define name emerald-themes
%define version 0.6.0
%define rel 1
%define git 20071018

%if  %{git}
%define srcname %{name}-%{git}
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif

Name:	 %name
Version: %version
Release: %release
Summary: Themes for the Emerald Window Decorator
License: GPL
Group:   System/X11
URL: http://www.compiz-fusion.org/
Source: %{srcname}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-build-root
BuildArch: noarch

%description
Themes for the Emerald Window Decorator for Beryl.

This package provides some basic themes, although more can be downloaded 
automatically once installed.

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

%build
%if %{git}
  # This is a GIT snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif

%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

chmod -R a+r %buildroot

%clean
rm -rf %buildroot

#----------------------------------------------------------------------------

%files
%defattr(-,root,root)
%dir %{_datadir}/%{shortname}/themes
%{_datadir}/%{shortname}/themes/*
