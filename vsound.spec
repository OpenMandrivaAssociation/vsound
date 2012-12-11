Summary:	Virtual loopback cable for audio
Name:		vsound
Version:	0.6
Release:	%mkrel 8
License:	GPL
Group:		Sound
URL:		http://www.vsound.org/
Source0:	http://www.vsound.org/%{name}-%{version}.tar.bz2
Patch0:		vsound_0.6-4.diff
Requires:	sox
BuildRequires:	sox
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
VSound is sort of like a 'virtual audio loopback cable'. That is, it allows
you to record the output audio stream of a program (similar to connecting a
loopback cable to the line in and line out jacks on the sound card, and
recording the sound from the line in jack, but without the DA/AD conversion
losses). One possible use for this application is as part of a RealAudio to
WAV file converter.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1

%build
rm -rf autom4te.cache configure
libtoolize --force --copy; aclocal -I .; automake --add-missing --copy --gnu; autoheader; autoconf

%configure2_5x \
    --disable-static \
    --enable-shared

%make CFLAGS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

%makeinstall

install -d %{buildroot}%{_mandir}/man1
install -m0644 debian/%{name}.1 %{buildroot}%{_mandir}/man1/

# nuke the dev files
rm -f %{buildroot}%{_libdir}/vsound/*.la
rm -f %{buildroot}%{_libdir}/vsound/*.a

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*



%changelog
* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-8mdv2011.0
+ Revision: 627840
- don't force the usage of automake1.7

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.6-7mdv2010.0
+ Revision: 434691
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.6-6mdv2009.0
+ Revision: 261891
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2009.0
+ Revision: 255688
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6-3mdv2008.1
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import vsound


* Thu Jun 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdv2007.0
- make it build
- added P1 (debian)

* Tue Feb 01 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.6-2mdk
- make it work

* Mon Dec 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6-1mdk
- 0.6

* Tue Dec 16 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5-5mdk
- requires sox (Bug 6079)
- fix changelog

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5-4mdk
- rebuild

* Thu Jun 27 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- buildrequires on sox

* Thu Sep 06 2001 Etienne Faure <etienne@mandrakesoft.com> 0.5-2mdk
- rebuild

* Thu Feb 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- updated 0.5

* Mon Dec 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.4-1mdk
- new in contribs
- used srpm from rufus t firefly <rufus.t.firefly@linux-mandrake.com> :
   - v0.4-1mdk (initial packaging)
