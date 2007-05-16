Summary:	Very fast image viewer for X Window
Summary(pl.UTF-8):	Bardzo szybka przeglądarka plików graficznych dla X Window
Name:		qiv
Version:	2.1
Release:	0.pre12
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.klografx.net/qiv/download/%{name}-%{version}-pre12.tgz
# Source0-md5:	80ba1e2da5115a3cc3a6f7e19cb620d8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-misc.patch
URL:		http://www.klografx.net/qiv/
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
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
%setup -q -n %{name}-%{version}-pre12
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
