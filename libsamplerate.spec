Summary:	Sample Rate Converter library
Name:		libsamplerate
Version:	0.1.8
Release:	1
License:	GPL
Group:		Libraries
#Source0Download:	http://www.mega-nerd.com/SRC/download.html
Source0:	http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
# Source0-md5:	1c7fb25191b4e6e3628d198a66a84f47
URL:		http://www.mega-nerd.com/SRC/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libsndfile-devel >= 1.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. SRC is capable of arbitrary and time varying conversions; from
downsampling by a factor of 12 to upsampling by the same factor. SRC
provides a small set of converters to allow quality to be traded off
against computation cost. The current best converter provides a
signal-to-noise ratio of 97dB with -3dB passband extending from DC to
96% of the theoretical best bandwidth for a given pair of input and
output sample rates.

%package devel
Summary:	Header file for libsamplerate library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for libsamplerate library.

%package tools
Summary:	libsamplerate utilities
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description tools
libsamplerate utilities - currently include one program to resample
audio files read and written using libsndfile.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I M4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README doc/*.{html,css,png}
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sndfile-resample

