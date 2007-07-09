Summary:	A small collection of Truetype fonts (GPL)
Name:		fonts-ttf-dustismo
Version:	2.0
Release:	5mdk

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
URL:		http://www.dustismo.com
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
Obsoletes:	dustismo-fonts
Provides:	dustismo-fonts
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

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


%post
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = "0" ]; then
  [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

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
