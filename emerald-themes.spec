%define rname emerald
%define name %{rname}-themes
%define version 0.2.0
%define release %mkrel 1

Name:	 %name
Version: %version
Release: %release
Summary: Themes for the Emerald Window Decorator for Beryl
License: GPL
Group:   System/X11
URL: http://www.beryl-project.org/
Source: http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-build-root
BuildArch: noarch

# cgwd-themes was renamed to emerald
Provides: cgwd-themes
Obsoletes: cgwd-themes
Obsoletes: cgwd-themes-extra

%description
Themes for the Emerald Window Decorator for Beryl.

This package provides some basic themes, although more can be downloaded 
automatically once installed.

%prep
%setup -q

%build
# Prevent libtoolize running which messes things up.
rm -f configure.in configure.ac

%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std

chmod -R a+r %buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir %{_datadir}/%{rname}/themes
%{_datadir}/%{rname}/themes/*


