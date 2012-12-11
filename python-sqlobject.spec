Summary: Object-Relational Manager, aka database wrapper for python
Name: python-sqlobject
Version: 0.15.0
Release: %mkrel 1
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




%changelog
* Mon May 02 2011 Michael Scherer <misc@mandriva.org> 0.15.0-1mdv2011.0
+ Revision: 661927
- update to 0.15.0

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 0.14.1-2mdv2011.0
+ Revision: 599633
- rebuild for py 2.7

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.14.1-1mdv2011.0
+ Revision: 587730
- update to new version 0.14.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.10.2-3mdv2010.0
+ Revision: 442494
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.10.2-2mdv2009.1
+ Revision: 323376
- rebuild

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.10.2-1mdv2009.0
+ Revision: 280566
- New version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8.2-3mdv2009.0
+ Revision: 242464
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdv2008.0
+ Revision: 52598
- update to new version 0.8.2


* Tue Dec 12 2006 Michael Scherer <misc@mandriva.org> 0.7.0-3mdv2007.0
+ Revision: 95738
- add python-setuptools, as the setup.py request it
- rebuild for new python
- Import python-sqlobject

