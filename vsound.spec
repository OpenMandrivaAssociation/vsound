Summary:	Virtual loopback cable for audio
Name:		vsound
Version:	0.6
Release:	10
License:	GPL
Group:		Sound
URL:		https://www.vsound.org/
Source0:	http://www.vsound.org/%{name}-%{version}.tar.gz
Patch0:		vsound_0.6-4.diff
Requires:	sox
BuildRequires:	sox
BuildRequires:	autoconf2.5
BuildRequires:	automake
BuildRequires:	libtool

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
install -d %{buildroot}%{_bindir}

%makeinstall
install -d %{buildroot}%{_mandir}/man1
install -m0644 debian/%{name}.1 %{buildroot}%{_mandir}/man1/

# nuke the dev files
rm -f %{buildroot}%{_libdir}/vsound/*.la
rm -f %{buildroot}%{_libdir}/vsound/*.a

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*
