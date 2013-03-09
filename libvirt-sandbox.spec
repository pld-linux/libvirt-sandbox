Summary:	API for building application sandboxes using libvirt
Summary(pl.UTF-8):	API do tworzenia sandboksów aplikacyjnych przy użyciu libvirt
Name:		libvirt-sandbox
Version:	0.1.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://libvirt.org/libvirt/sandbox/%{name}-%{version}.tar.gz
# Source0-md5:	1c0bd8f6c85c43d8bf7894266511ce39
URL:		http://libvirt.org/
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gobject-introspection-devel >= 0.10.8
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	libcap-ng-devel >= 0.4.0
BuildRequires:	libselinux-devel
BuildRequires:	libvirt-devel >= 1.0.2
BuildRequires:	libvirt-glib-devel >= 0.0.9
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	glib2 >= 1:2.32.0
Requires:	libcap-ng >= 0.4.0
Requires:	libvirt >= 1.0.2
Requires:	libvirt-glib >= 0.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libvirt-sandbox package provides an API for building application
sandboxes using libvirt. Sandboxes can be based on either container or
machine based virtualization technology. Also included is a simple
command line tool for launching sandboxes for arbitrary commands.

%description -l pl.UTF-8
Libvirt-sandbox udostępnia API do tworzenia sandboksów ("piaskownic")
aplikacyjnych przy użyciu libvirt. Sandboksy mogą być oparte na
wirtualizacji kontenera lub maszyny. Dołączone są także proste
narzędzia uruchamiane z linii poleceń do uruchamiania sandboksów
dowolnych poleceń.

%package devel
Summary:	Header files for libvirt-sandbox library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvirt-sandbox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.32.0
Requires:	libvirt-devel >= 1.0.2
Requires:	libvirt-glib-devel >= 0.0.9

%description devel
Header files for libvirt-sandbox library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvirt-sandbox.

%package static
Summary:	Static libvirt-sandbox library
Summary(pl.UTF-8):	Statyczna biblioteka libvirt-sandbox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvirt-sandbox library.

%description static -l pl.UTF-8
Statyczna biblioteka libvirt-sandbox.

%package -n bash-completion-libvirt-sandbox
Summary:	Bash completion rules for libvirt-sandbox
Summary(pl.UTF-8):	Bashowe uzupełnianie poleceń dla pakietu libvirt-sandbox
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-libvirt-sandbox
Bash completion rules for virt-sandbox-service command.

%description -n bash-completion-libvirt-sandbox -l pl.UTF-8
Bashowe uzupełnianie parametrów dla polecenia virt-sandbox-service.

%prep
%setup -q

# what is it? seems not required
%{__sed} -i -e '/Requires: sandbox-2.0/d' libvirt-sandbox-1.0.pc.in

%build
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvirt-sandbox-1.0.la
# just placeholder, useless in RPM
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/libvirt-sandbox/scratch/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/virt-sandbox
%attr(755,root,root) %{_bindir}/virt-sandbox-service
%attr(755,root,root) %{_libdir}/libvirt-sandbox-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvirt-sandbox-1.0.so.1
%{_libdir}/girepository-1.0/LibvirtSandbox-1.0.typelib
%attr(755,root,root) %{_libexecdir}/libvirt-sandbox-init-common
%attr(755,root,root) %{_libexecdir}/libvirt-sandbox-init-lxc
%attr(755,root,root) %{_libexecdir}/libvirt-sandbox-init-qemu
%attr(755,root,root) %{_libexecdir}/virt-sandbox-service-util
%dir %{_sysconfdir}/libvirt-sandbox
%dir %{_sysconfdir}/libvirt-sandbox/scratch
%dir %{_sysconfdir}/libvirt-sandbox/services
%config(noreplace) %verify(not md5 mtime size) /etc/cron.daily/virt-sandbox-service.logrotate
%{_mandir}/man1/virt-sandbox.1*
%{_mandir}/man1/virt-sandbox-service.1*
%{_mandir}/man1/virt-sandbox-service-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvirt-sandbox-1.0.so
%{_includedir}/libvirt-sandbox-1.0
%{_pkgconfigdir}/libvirt-sandbox-1.0.pc
%{_datadir}/gir-1.0/LibvirtSandbox-1.0.gir
%{_gtkdocdir}/Libvirt-sandbox

%files static
%defattr(644,root,root,755)
%{_libdir}/libvirt-sandbox-1.0.a

%files -n bash-completion-libvirt-sandbox
%defattr(644,root,root,755)
/etc/bash_completion.d/virt-sandbox-service-bash-completion.sh
