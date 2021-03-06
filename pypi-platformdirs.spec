#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-platformdirs
Version  : 2.5.2
Release  : 23
URL      : https://files.pythonhosted.org/packages/ff/7b/3613df51e6afbf2306fc2465671c03390229b55e3ef3ab9dd3f846a53be6/platformdirs-2.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/7b/3613df51e6afbf2306fc2465671c03390229b55e3ef3ab9dd3f846a53be6/platformdirs-2.5.2.tar.gz
Summary  : A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".
Group    : Development/Tools
License  : MIT
Requires: pypi-platformdirs-license = %{version}-%{release}
Requires: pypi-platformdirs-python = %{version}-%{release}
Requires: pypi-platformdirs-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatch_vcs)
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
The problem
===========
.. image:: https://github.com/platformdirs/platformdirs/workflows/Test/badge.svg
:target: https://github.com/platformdirs/platformdirs/actions?query=workflow%3ATest

%package license
Summary: license components for the pypi-platformdirs package.
Group: Default

%description license
license components for the pypi-platformdirs package.


%package python
Summary: python components for the pypi-platformdirs package.
Group: Default
Requires: pypi-platformdirs-python3 = %{version}-%{release}

%description python
python components for the pypi-platformdirs package.


%package python3
Summary: python3 components for the pypi-platformdirs package.
Group: Default
Requires: python3-core
Provides: pypi(platformdirs)

%description python3
python3 components for the pypi-platformdirs package.


%prep
%setup -q -n platformdirs-2.5.2
cd %{_builddir}/platformdirs-2.5.2
pushd ..
cp -a platformdirs-2.5.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394612
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-platformdirs
cp %{_builddir}/platformdirs-2.5.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-platformdirs/1a628675f3f38f1d4715ebd772a8160a0ea94dd4
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-platformdirs/1a628675f3f38f1d4715ebd772a8160a0ea94dd4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
