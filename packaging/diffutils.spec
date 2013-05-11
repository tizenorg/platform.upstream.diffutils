Name:           diffutils
Version:        3.2
Release:        0
License:        GFDL-1.2 ; GPL-3.0+
Summary:        GNU diff Utilities
Url:            http://www.gnu.org/software/diffutils/
Group:          Productivity/Text/Utilities
Source:         %{name}-%{version}.tar.xz
BuildRequires:  xz
Provides:       diff
Obsoletes:      diff

%description
The GNU diff utilities find differences between files. diff is used to
make source code patches, for instance.

%prep
%setup -q

%build
%configure --disable-nls
make %{?_smp_mflags}

%install
%make_install
gzip -9 %{buildroot}%{_infodir}/%{name}.info


%files
%license COPYING
%defattr(-,root,root)
%{_bindir}/cmp
%{_bindir}/diff
%{_bindir}/diff3
%{_bindir}/sdiff
%doc %{_infodir}/%{name}.info.gz
%doc %{_mandir}/man1/*.gz

