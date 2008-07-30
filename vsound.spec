Summary:	Virtual loopback cable for audio
Name:		vsound
Version:	0.6
Release:	%mkrel 5
License:	GPL
Group:		Sound
URL:		http://www.vsound.org/
Source0:	http://www.vsound.org/%{name}-%{version}.tar.bz2
Patch0:		vsound_0.6-4.diff
Requires:	sox
BuildRequires:	sox
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
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
libtoolize --force --copy; aclocal-1.7 -I .; automake-1.7 --add-missing --copy --gnu; autoheader; autoconf

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

