
%define plugin	dvdselect
%define name	vdr-plugin-%plugin
%define version	0.8
%define rel	17

Summary:	VDR plugin: virtual dvd-selector
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdr-wiki.de/wiki/index.php/Dvdselect-plugin
Source:		http://www.vdr-wiki.de/vdr/vdr-dvdselect/vdr-%plugin-%version.tar.bz2
Patch0:		dvdselect-default-paths.patch
Patch1:		dvdselect-0.8-i18n-1.6.patch
Patch2:		dvdselect-format-string.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This Plugin is used to mount multiple DVD-Images to the dvd-device.
Doing this, you are able to play these dvds using the dvdplugin.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep
rm -f examples/*~

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY examples




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.8-17mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.8-16mdv2009.1
+ Revision: 359702
- fix format strings (format-string.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.8-15mdv2009.0
+ Revision: 197920
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.8-14mdv2009.0
+ Revision: 197654
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- fix default paths (P0)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.8-13mdv2008.1
+ Revision: 145070
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.8-12mdv2008.1
+ Revision: 103085
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.8-11mdv2008.0
+ Revision: 49991
- rebuild for new vdr

* Fri Jun 22 2007 Anssi Hannula <anssi@mandriva.org> 0.8-10mdv2008.0
+ Revision: 42722
- rebuild due to buildsystem failure

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.8-9mdv2008.0
+ Revision: 42077
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.8-8mdv2008.0
+ Revision: 22740
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.8-7mdv2007.0
+ Revision: 90912
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.8-6mdv2007.1
+ Revision: 73984
- rebuild for new vdr
- Import vdr-plugin-dvdselect

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.8-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.8-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.8-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.8-2mdv2007.0
- rebuild for new vdr

* Thu Jun 22 2006 Anssi Hannula <anssi@mandriva.org> 0.8-1mdv2007.0
- initial Mandriva release

