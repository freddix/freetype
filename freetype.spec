Summary:	TrueType font rendering library"
Name:		freetype
Version:	2.5.3
Release:	2
Epoch:		1
License:	GPL or FTL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sourceforge/freetype/%{name}-%{version}.tar.bz2
# Source0-md5:	d6b60f06bfc046e43ab2a6cbfd171d65
Patch0:		%{name}-enable-valid.patch
Patch1:		%{name}-options.patch
URL:		http://www.freetype.org/
BuildRequires:	automake
BuildRequires:	bzip2-devel
#BuildRequires:	harfbuzz-devel
BuildRequires:	libpng-devel
BuildRequires:	python
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FreeType engine is a free and portable TrueType font rendering
engine. It has been developed to provide TrueType support to a great
variety of platforms and environments.

%package devel
Summary:	Header files and development documentation
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bzip2-devel

%description devel
This package includes the header files and documentation necessary to
develop applications that use FreeType.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

echo
%build
%configure \
    --disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/{CHANGES,FTL.TXT,LICENSE.TXT,TODO,formats.txt,raster.txt}
%attr(755,root,root) %ghost %{_libdir}/libfreetype.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/DEBUG docs/reference
%attr(755,root,root) %{_bindir}/freetype-config
%attr(755,root,root) %{_libdir}/libfreetype.so
%{_includedir}/freetype2
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/freetype-config.1*

