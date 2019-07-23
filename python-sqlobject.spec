Summary: Object-Relational Manager, aka database wrapper for python


Name: python-sqlobject
Version:	3.7.2
Release:	1
URL: http://sqlobject.org/
Source0:	https://files.pythonhosted.org/packages/45/af/6da3ecd7da762bb3b533d4b6c8c426b9f9c0723a22c0b943233415f7b61f/SQLObject-3.7.2.tar.gz
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






