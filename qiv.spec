Summary: 	Very fast image viewer for X-Window
Summary(pl):	Bardzo szybka przegl±darka plików graficznych dla X Window
Name: 		qiv
Version: 	1.2
Release: 	1
Copyright: 	GPL
Group: 		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
URL: 		http://www.klografx.de/
Source: 	http://www.klografx.de/software/files/%{name}-%{version}.tgz
Patch: 		qiv-misc.patch
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	imlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix		/usr/X11R6

%description
Quick Image Viewer (qiv) is a very small and pretty fast GDK/Imlib image
viewer. Features include zoom, maxpect, scale down, fullscreen,
brightness/contrast/gamma correction, slideshow, flip horizontal/vertical,
rotate left/right, delete (move to .qiv-trash/), jump to image x, jump
forward/backward x images, filename filer and you can use qiv to set
your X11-Desktop background.

%description
Quick Image Viewer (qiv) jest bardzo ma³ym i ca³kiem szybkim programem
do przegl±dania plików graficznych, wykorzystuj±cym biblioteki GDK/Imlib.

%prep
%setup -q
%patch -p0

%build
make OPTS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make install DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}

gzip -9nf README Changes TO-DO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes,TO-DO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
