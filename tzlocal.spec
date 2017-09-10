#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tzlocal
Version  : 1.4
Release  : 5
URL      : http://pypi.debian.net/tzlocal/tzlocal-1.4.tar.gz
Source0  : http://pypi.debian.net/tzlocal/tzlocal-1.4.tar.gz
Summary  : tzinfo object for the local timezone
Group    : Development/Tools
License  : CC0-1.0 MIT Universal
Requires: tzlocal-legacypython
Requires: tzlocal-python
Requires: pytz
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : setuptools

%description
=======
        
        This Python module returns a `tzinfo` object with the local timezone information under Unix and Win-32.
        It requires `pytz`, and returns `pytz` `tzinfo` objects.
        
        This module attempts to fix a glaring hole in `pytz`, that there is no way to
        get the local timezone information, unless you know the zoneinfo name, and
        under several Linux distros that's hard or impossible to figure out.
        
        Also, with Windows different timezone system using pytz isn't of much use
        unless you separately configure the zoneinfo timezone name.
        
        With `tzlocal` you only need to call `get_localzone()` and you will get a
        `tzinfo` object with the local time zone info. On some Unices you will still
        not get to know what the timezone name is, but you don't need that when you
        have the tzinfo file. However, if the timezone name is readily available it
        will be used.
        
        
        Supported systems
        -----------------

%package legacypython
Summary: legacypython components for the tzlocal package.
Group: Default

%description legacypython
legacypython components for the tzlocal package.


%package python
Summary: python components for the tzlocal package.
Group: Default
Requires: tzlocal-legacypython

%description python
python components for the tzlocal package.


%prep
%setup -q -n tzlocal-1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505072683
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1505072683
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
/usr/lib/python3*/*
