Summary: Very fast image viewer for X-Window.
Name: qiv
Version: 1.0
Release: 1
Copyright: GPL
Group: X11/Applications/Graphics
Vendor: Adam Kopacz <Adam.K@idnet.de>
Url: http://www.klografx.de/
Source: http://www.klografx.de/software/files/%{name}-%{version}.tgz
Patch: %{name}-opt.patch
Requires: gtk+
Requires: imlib
BuildRoot: /tmp/%{name}-%{version}-root

%description
Quick Image Viewer (qiv) is a very small and pretty fast GDK/Imlib image
viewer. Features include zoom, maxpect, scale down, fullscreen,
brightness/contrast/gamma correction, slideshow, flip horizontal/vertical,
rotate left/right, delete (move to .qiv-trash/), jump to image x, jump
forward/backward x images, filename filer and you can use qiv to set
your X11-Desktop background.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
install qiv $RPM_BUILD_ROOT/usr/X11R6/bin/
install qiv.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) /usr/X11R6/bin/qiv
/usr/X11R6/man/man1/qiv.1

%changelog
* Sat Nov 21 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [1.0-1]
- Initial release.
- RPM_OPT patch.
