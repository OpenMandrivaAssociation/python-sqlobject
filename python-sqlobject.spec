Summary: Object-Relational Manager, aka database wrapper for python
Name: python-sqlobject
Version: 0.10.2
Release: %mkrel 3
URL: http://sqlobject.org/
Source0: http://cheeseshop.python.org/packages/source/S/SQLObject/SQLObject-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
BuildRequires: python-devel python-setuptools
Requires: python

%description
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience.  Works with MySQL, PostgreSQL, SQLite, Firebird.

%prep
%setup -n SQLObject-%version -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT
rm -Rf $RPM_BUILD_ROOT/%_bindir/easy_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs
%{py_puresitedir}/*
%_bindir/*


