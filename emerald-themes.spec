%define git 20080210

%if  %{git}
%define srcname %{name}-%{git}
%define distname %{name}
%define rel 0.%{git}.4
%else
%define srcname %{name}-%{version}
%define distname %{name}-%{version}
%define rel 1
%endif

Name:		emerald-themes
Version:	0.6.0
Release:	%{rel}
Summary:	Themes for the Emerald Window Decorator
Group:		System/X11
License:	GPLv2
URL:		http://www.compiz-fusion.org/
Source:		%{srcname}.tar.bz2
Requires:	emerald
BuildArch:	noarch

%description
Themes for the Emerald Window Decorator for Compiz.

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

%makeinstall_std

chmod -R a+r %{buildroot}

#----------------------------------------------------------------------------

%files
%dir %{_datadir}/emerald/themes
%{_datadir}/emerald/themes/*

