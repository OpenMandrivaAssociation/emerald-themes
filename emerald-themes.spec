Name:		emerald-themes
Version:	0.8.16
Release:	1
Summary:	Themes for the Emerald Window Decorator
Group:		System/X11
License:	GPLv2
URL:            https://github.com/compiz-reloaded/emerald-themes
Source0:        https://github.com/compiz-reloaded/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	emerald
BuildArch:	noarch

%description
Themes for the Emerald Window Decorator for Compiz.

This package provides some basic themes, although more can be downloaded
automatically once installed.

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure

%make_build

%install
%make_install

%files
%doc NEWS
%license COPYING
%{_datadir}/emerald/themes/*
