Summary:	A small collection of Truetype fonts (GPL)
Name:		fonts-ttf-dustismo
Version:	2.0
Release:	13

Source0:	Dustismo.tgz
Source1:	Abogada_loco.zip
Source2:	balker.zip
Source3:	Domestic_Manners.zip
Source4:	El_Abogado_Loco.zip
Source5:	flatline.zip
Source6:	ItWasntMe.zip
Source7:	Junkyard.zip
Source8:	MarkedFool.zip
Source9:	PenguinAttack.zip
Source10:	Progenisis.zip
Source11:	Swift.zip
Source12:	Wargames.zip
Source13:	Winks.zip
License:	GPL
Group:		System/Fonts/True type
URL:		https://www.dustismo.com
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires: fontconfig
Obsoletes:	dustismo-fonts
Provides:	dustismo-fonts
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description 
A small collection of Truetype fonts released under the GPL.
One of the fonts included is Dustismo. The aim is to create a standard,
high quality, all purpose, sans serif font.

%prep
%setup -q -c %name-%version
unzip -o %SOURCE2 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE3 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE4 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE5 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE6 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE7 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE8 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE9 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE10 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE11 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE12 -d $RPM_BUILD_DIR/%name-%version
unzip -o %SOURCE13 -d $RPM_BUILD_DIR/%name-%version

mv "It wasn't me.ttf" It_wasn_t_me.ttf

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/dustismo
cp -f *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/dustismo
{
    pushd $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/dustismo
    ttmkfdir > fonts.dir
    cp fonts.dir fonts.scale
    popd
}

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/dustismo \
	%{buildroot}%_sysconfdir/X11/fontpath.d/ttf-dustismo:pri=50


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc installation.txt license.txt
%dir %_datadir/fonts/ttf/dustismo
%config(noreplace) %{_datadir}/fonts/ttf/dustismo/fonts.dir
%config(noreplace) %{_datadir}/fonts/ttf/dustismo/fonts.scale
%{_datadir}/fonts/ttf/dustismo/*.ttf
%{_sysconfdir}/X11/fontpath.d/ttf-dustismo:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.0-12mdv2011.0
+ Revision: 675517
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-11mdv2011.0
+ Revision: 610727
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.0-10mdv2010.1
+ Revision: 494137
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.0-9mdv2010.0
+ Revision: 428829
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2.0-8mdv2009.0
+ Revision: 240715
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 09 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.0-6mdv2008.0
+ Revision: 50619
- fontpath.d conversion (#31756)
- change font directory to a more standard location
- minor spec cleanups
- Import fonts-ttf-dustismo



* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0-5mdk
- Don't package fontconfig cache file
- Fix prereq

* Thu Apr 28 2005 Marcel Pol <mpol@mandriva.org> 2.0-4mdk
- add more fonts

* Thu Apr 28 2005 Marcel Pol <mpol@mandriva.org> 2.0-3mdk
- rebuild and smal spec cleanup

* Fri Apr 30 2004 Marcel Pol <mpol@mandrake.org> 2.0-2mdk
- rebuild for bot happiness

* Sun Mar 23 2003 Marcel Pol <mpol@gmx.net> 2.0-1mdk
- 2.0

* Wed Feb 19 2003 Marcel Pol <mpol@gmx.net> 1.92-1mdk
- changed name of the rpm
- use real versioning: 1.92

* Fri Jan 24 2003 Marcel Pol <mpol@gmx.net> 20030111-1mdk
- initial mandrake rpm
- run fc-cache in %%post, so fc-list can see them
- can't seem to get the bold and italic fonts right...
