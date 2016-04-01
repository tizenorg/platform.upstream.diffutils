Name:           diffutils
Version:        3.3
Release:        0
License:        GPL-3.0+ and GFDL-1.3+
Summary:        GNU diff Utilities
Url:            http://www.gnu.org/software/diffutils/
Group:          System/Utilities
Source:         %{name}-%{version}.tar.xz
Source1001: 	diffutils.manifest
BuildRequires:  xz
Provides:       diff = %{version}
Obsoletes:      diff < %{version}

%description
The GNU diff utilities find differences between files. diff is used to
make source code patches, for instance.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
%configure --disable-nls
make %{?_smp_mflags}

%install
%make_install
gzip -9 %{buildroot}%{_infodir}/%{name}.info


%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_bindir}/cmp
%{_bindir}/diff
%{_bindir}/diff3
%{_bindir}/sdiff
%doc %{_infodir}/%{name}.info.gz
%doc %{_mandir}/man1/*.gz

