Summary:	Very fast image viewer for X Window
Summary(pl):	Bardzo szybka przegl±darka plików graficznych dla X Window
Name:		qiv
Version:	1.7
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.klografx.net/qiv/download/%{name}-%{version}-src.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-misc.patch
URL:		http://www.klografx.net/qiv/
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Quick Image Viewer (qiv) is a very small and pretty fast GDK/Imlib
image viewer. Features include zoom, maxpect, scale down, fullscreen,
brightness/contrast/gamma correction, slideshow, flip
horizontal/vertical, rotate left/right, delete (move to .qiv-trash/),
jump to image x, jump forward/backward x images, filename filer and
you can use qiv to set your X11-Desktop background.

%description -l pl
Quick Image Viewer (qiv) jest bardzo ma³ym i ca³kiem szybkim programem
do przegl±dania plików graficznych, wykorzystuj±cym biblioteki
GDK/Imlib.

%prep
%setup -q
%patch -p1

%build
%{__make} OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}

install %{SOURCE1} RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README README.CHANGES README.TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
