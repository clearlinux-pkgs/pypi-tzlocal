#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tzlocal
Version  : 4.1
Release  : 44
URL      : https://files.pythonhosted.org/packages/f7/cc/5543aa3e3e0c10f5fa6d0010eead722e0a5cc610f543fc6e816648d73ed7/tzlocal-4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f7/cc/5543aa3e3e0c10f5fa6d0010eead722e0a5cc610f543fc6e816648d73ed7/tzlocal-4.1.tar.gz
Summary  : tzinfo object for the local timezone
Group    : Development/Tools
License  : MIT
Requires: pypi-tzlocal-license = %{version}-%{release}
Requires: pypi-tzlocal-python = %{version}-%{release}
Requires: pypi-tzlocal-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pytz_deprecation_shim)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tzdata)
BuildRequires : pypi(wheel)
BuildRequires : python-mock

%description
=======
        
        API CHANGE!
        -----------
        
        With version 3.0 of tzlocal, tzlocal no longer returned `pytz` objects, but
        `zoneinfo` objects, which has a different API. Since 4.0, it now restored
        partial compatibility for `pytz` users through Paul Ganssle's
        `pytz_deprecation_shim`.
        
        tzlocal 4.0 also adds an official function `get_localzone_name()` to get only
        the timezone name, instead of a timezone object. On unix, it can raise an
        error if you don't have a timezone name configured, where `get_localzone()`
        will succeed, so only use that if you need the timezone name.
        
        4.0 also adds way more information on what is going wrong in your
        configuration when the configuration files are unclear or contradictory.
        
        
        Info
        ----
        
        This Python module returns a ``tzinfo`` object (with a pytz_deprecation_shim,
        for pytz compatibility) with the local timezone information, under Unix and
        Windows.
        
        It requires Python 3.6 or later, and will use the ``backports.tzinfo``
        package, for Python 3.6 to 3.8.
        
        This module attempts to fix a glaring hole in the ``pytz`` and ``zoneinfo``
        modules, that there is no way to get the local timezone information, unless
        you know the zoneinfo name, and under several Linux distros that's hard or
        impossible to figure out.
        
        With ``tzlocal`` you only need to call ``get_localzone()`` and you will get a
        ``tzinfo`` object with the local time zone info. On some Unices you will
        still not get to know what the timezone name is, but you don't need that when
        you have the tzinfo file. However, if the timezone name is readily available
        it will be used.
        
        
        Supported systems
        -----------------

%package license
Summary: license components for the pypi-tzlocal package.
Group: Default

%description license
license components for the pypi-tzlocal package.


%package python
Summary: python components for the pypi-tzlocal package.
Group: Default
Requires: pypi-tzlocal-python3 = %{version}-%{release}

%description python
python components for the pypi-tzlocal package.


%package python3
Summary: python3 components for the pypi-tzlocal package.
Group: Default
Requires: python3-core
Provides: pypi(tzlocal)
Requires: pypi(pytz_deprecation_shim)
Requires: pypi(tzdata)

%description python3
python3 components for the pypi-tzlocal package.


%prep
%setup -q -n tzlocal-4.1
cd %{_builddir}/tzlocal-4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641571065
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tzlocal
cp %{_builddir}/tzlocal-4.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-tzlocal/d0e0745ad05aba07ac3481313b59665d4a36017c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tzlocal/d0e0745ad05aba07ac3481313b59665d4a36017c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
