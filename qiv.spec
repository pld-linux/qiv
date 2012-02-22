Summary:	Very fast image viewer for X Window
Summary(pl.UTF-8):	Bardzo szybka przeglądarka plików graficznych dla X Window
Name:		qiv
Version:	2.2.4
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://spiegl.de/qiv/download/%{name}-%{version}.tgz
# Source0-md5:	1425f89c90f9c045858fccf24d894c97
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-misc.patch
URL:		http://spiegl.de/qiv/
BuildRequires:	gtk+2-devel
BuildRequires:	imlib2-devel
BuildRequires:	libmagic-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXinerama-devel
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
	OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README README.TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
