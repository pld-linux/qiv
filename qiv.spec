Summary:	Very fast image viewer for X Window
Summary(pl.UTF-8):	Bardzo szybka przeglądarka plików graficznych dla X Window
Name:		qiv
Version:	2.3.1
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://spiegl.de/qiv/download/%{name}-%{version}.tgz
# Source0-md5:	93aea7469be64ebd35277a6dac079fc8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		non-24bit.patch
URL:		http://spiegl.de/qiv/
BuildRequires:	gtk+2-devel
BuildRequires:	imlib2-devel
BuildRequires:	lcms2-devel
BuildRequires:	libexif-devel
BuildRequires:	libmagic-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXext-devel
Requires:	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quick Image Viewer (qiv) is a very small and pretty fast GDK/Imlib
image viewer. Features include zoom, maxpect, scale down, fullscreen,
brightness/contrast/gamma correction, slideshow, flip
horizontal/vertical, rotate left/right, delete (move to .qiv-trash/),
jump to image x, jump forward/backward x images, filename filer and
you can use qiv to set your X11-Desktop background.

%description -l pl.UTF-8
Quick Image Viewer (qiv) jest bardzo małym i całkiem szybkim programem
do przeglądania plików graficznych, wykorzystującym biblioteki
GDK/Imlib.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fcaller-saves -ffast-math -fno-strength-reduce -fthread-jumps"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}

install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc Changelog README README.TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
