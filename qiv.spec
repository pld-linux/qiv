Summary:	Very fast image viewer for X-Window
Summary(pl):	Bardzo szybka przegl�darka plik�w graficznych dla X Window
Name:		qiv
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.klografx.de/software/files/%{name}-%{version}.tgz
Patch0:		qiv-misc.patch
URL:		http://www.klografx.de/software/qiv.shtml
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix		/usr/X11R6

%description
Quick Image Viewer (qiv) is a very small and pretty fast GDK/Imlib
image viewer. Features include zoom, maxpect, scale down, fullscreen,
brightness/contrast/gamma correction, slideshow, flip
horizontal/vertical, rotate left/right, delete (move to .qiv-trash/),
jump to image x, jump forward/backward x images, filename filer and
you can use qiv to set your X11-Desktop background.

%description -l pl
Quick Image Viewer (qiv) jest bardzo ma�ym i ca�kiem szybkim programem
do przegl�dania plik�w graficznych, wykorzystuj�cym biblioteki
GDK/Imlib.

%prep
%setup -q
%patch -p1

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
