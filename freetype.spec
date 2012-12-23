Summary:	TrueType font rasterizer
Name:		freetype
Version:	2.4.11
Release:	1
Epoch:		1
License:	GPL or FTL
Group:		Libraries
Source0:	http://savannah.nongnu.org/download/freetype/%{name}-%{version}.tar.bz2
# Source0-md5:	b93435488942486c8d0ca22e8f768034
Source1:	http://savannah.nongnu.org/download/freetype/%{name}-doc-%{version}.tar.bz2
# Source1-md5:	20f148103e069093f53584ce5ba16581
URL:		http://www.freetype.org/
BuildRequires:	automake
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

%description devel
This package includes the header files and documentation necessary to
develop applications that use FreeType.

%package static
Summary:	Static freetype library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static freetype library.

%prep
%setup -q -a1

%build
CFLAGS="%{rpmcflags} \
	-DFT_CONFIG_OPTION_SUBPIXEL_RENDERING"	\
%{__make} setup unix \
	CFG="--prefix=%{_prefix} --libdir=%{_libdir}"

%{__make} \
	X11_LIB=

%{__make} refdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/libfreetype.la
%{_includedir}/freetype2
%{_includedir}/*.h
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

