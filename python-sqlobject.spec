Summary: Object-Relational Manager, aka database wrapper for python


Name: python-sqlobject
Version: 1.6.0
Release: 1
URL: http://sqlobject.org/
Source0: http://cheeseshop.python.org/packages/source/S/SQLObject/SQLObject-%{version}.tar.gz
License: LGPL
Group: Development/Python
BuildArch: noarch
BuildRequires: python-devel python-setuptools
Requires: python

%description
Classes created using SQLObject wrap database rows, presenting a
friendly-looking Python object instead of a database/SQL interface.
Emphasizes convenience.  Works with MySQL, PostgreSQL, SQLite, Firebird.

%prep
%setup -n SQLObject-%{version} -q

%build
python setup.py build

%install
python setup.py install --root %{buildroot}
rm -Rf %{buildroot}/%{_bindir}/easy_install

%clean

%files
%doc docs
%{py_puresitedir}/*
%{_bindir}/*






