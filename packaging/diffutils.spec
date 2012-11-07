#
# spec file for package diffutils
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           diffutils
Version:        3.2
Release:        0
License:        GFDL-1.2 ; GPL-3.0+
Summary:        GNU diff Utilities
Url:            http://www.gnu.org/software/diffutils/
Group:          Productivity/Text/Utilities
Source:         %{name}-%{version}.tar.xz
Patch1:         diffutils-stdio.in.patch
BuildRequires:  xz
Provides:       diff
Obsoletes:      diff

%description
The GNU diff utilities find differences between files. diff is used to
make source code patches, for instance.

%prep
%setup -q
%patch1 -p1

%build
%configure --disable-nls
make %{?_smp_mflags}

%install
%make_install
gzip -9 %{buildroot}%{_infodir}/%{name}.info


%files
%defattr(-,root,root)
%{_bindir}/cmp
%{_bindir}/diff
%{_bindir}/diff3
%{_bindir}/sdiff
%doc %{_infodir}/%{name}.info.gz
%doc %{_mandir}/man1/*.gz

