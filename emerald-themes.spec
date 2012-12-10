%define shortname emerald
%define name emerald-themes
%define version 0.6.0
%define rel 3
%define git 20080210

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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-0.20080210.3mdv2011.0
+ Revision: 618225
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0-0.20080210.2mdv2010.0
+ Revision: 428593
- rebuild

* Mon Feb 18 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-0.20080210.1mdv2009.0
+ Revision: 172316
- Update to git master for new compiz

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 19 2007 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-0.20071018.1mdv2008.1
+ Revision: 100102
- Update snapshot from 0.6.0 branch for compiz 0.6.2

* Mon Aug 13 2007 Colin Guthrie <cguthrie@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 62617
- Official Release: 0.5.2

* Wed Aug 01 2007 Colin Guthrie <cguthrie@mandriva.org> 0.3.0-0.20070801.1mdv2008.0
+ Revision: 57845
- Updated snapshot

* Fri Jun 29 2007 Colin Guthrie <cguthrie@mandriva.org> 0.3.0-0.20070627.1mdv2008.0
+ Revision: 45919
- New Snapshot for Compiz Fusion

* Tue Jun 12 2007 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 38102
- New version


* Thu Mar 15 2007 Colin Guthrie <cguthrie@mandriva.org> 0.2.0-1mdv2007.1
+ Revision: 143946
- New Version: 0.2.0

* Wed Feb 14 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.9999.2-1mdv2007.1
+ Revision: 120685
- New Release Candidate 0.1.9999.2 (RC2)
- New Release Candidate: RC1

* Sun Jan 21 2007 Colin Guthrie <cguthrie@mandriva.org> 0.1.99.2-1mdv2007.1
+ Revision: 111379
- New version 0.2.0 Beta 2

* Sat Dec 30 2006 Colin Guthrie <cguthrie@mandriva.org> 0.1.4-1mdv2007.1
+ Revision: 102818
- New Release: 0.1.4

* Sun Dec 10 2006 Colin Guthrie <cguthrie@mandriva.org> 0.1.3-1mdv2007.1
+ Revision: 94446
- The official 0.1.3

  + Sébastien Savarin <plouf@mandriva.org>
    - Add Forgoten sources
    - New rev 0.1.3

* Mon Nov 20 2006 Colin Guthrie <cguthrie@mandriva.org> 0.1.2-1mdv2007.1
+ Revision: 85546
- Spec file cleanup

* Wed Nov 08 2006 Colin Guthrie <cguthrie@mandriva.org> 0.1.2-1mdv2007.0
+ Revision: 78079
- Remove and old SPEC file comment
- New Release 0.1.2

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description format

* Sat Oct 21 2006 Sébastien Savarin <plouf@mandriva.org> 0.1.1-1mdv2007.0
+ Revision: 71598
- New revision 0.1.1

  + Colin Guthrie <cguthrie@mandriva.org>
    - Proper handling of Provides/Obsoletes for package renames
    - First release of Emerald
    - Cgwd becomes Emerald

* Tue Sep 19 2006 Colin Guthrie <cguthrie@mandriva.org> 0.16-1mdv2007.0
+ Revision: 61822
- Import cgwd-themes

