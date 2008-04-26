
%define plugin	dvdselect
%define name	vdr-plugin-%plugin
%define version	0.8
%define rel	14

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


