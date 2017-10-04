#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : logutils
Version  : 0.3.5
Release  : 25
URL      : http://pypi.debian.net/logutils/logutils-0.3.5.tar.gz
Source0  : http://pypi.debian.net/logutils/logutils-0.3.5.tar.gz
Summary  : Logging utilities
Group    : Development/Tools
License  : BSD-3-Clause
Requires: logutils-legacypython
Requires: logutils-python3
Requires: logutils-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
library's logging package.
        
        Some of these handlers are out-of-scope for the standard library, and
        so they are packaged here. Others are updated versions which have
        appeared in recent Python releases, but are usable with older versions
        of Python and so are packaged here.

%package legacypython
Summary: legacypython components for the logutils package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the logutils package.


%package python
Summary: python components for the logutils package.
Group: Default
Requires: logutils-legacypython
Requires: logutils-python3

%description python
python components for the logutils package.


%package python3
Summary: python3 components for the logutils package.
Group: Default
Requires: python3-core

%description python3
python3 components for the logutils package.


%prep
%setup -q -n logutils-0.3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507156552
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507156552
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
