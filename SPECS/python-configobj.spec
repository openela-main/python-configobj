%global pypi_name configobj

Name:           python-%{pypi_name}
Version:        5.0.6
Release:        11%{?dist}
Summary:        Config file reading, writing, and validation

Group:          System Environment/Libraries
License:        BSD
URL:            http://configobj.readthedocs.org/
# Moved to the github release instead of the pypi one since multiple elements (License and tests)
# are not available using pypi. Two bugs have been filled about this:
# https://github.com/DiffSK/configobj/issues/98
# https://github.com/DiffSK/configobj/issues/99
# Source0:        https://pypi.python.org/packages/source/c/configobj/configobj-5.0.6.tar.gz
Source0:        https://github.com/DiffSK/%{pypi_name}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest

%description
ConfigObj is a simple but powerful configuration file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files. 

%package -n python3-configobj
Summary:        Config file reading, writing, and validation for Python 3
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-six
%description -n python3-configobj
ConfigObj is a simple but powerful configuration file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files. 

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
# this needs to be set for tests.test_configobj.test_options_deprecation
export PYTHONWARNINGS=always
%{__python3} test_configobj.py
%{__python3} -m pytest tests

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Jun 05 2018 Petr Viktorin <pviktori@redhat.com> - 5.0.6-11
- Remove the Python 2 version
  https://bugzilla.redhat.com/show_bug.cgi?id=1567146

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 5.0.6-7
- Enable tests

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 5.0.6-6
- Rebuild for Python 3.6
- Disable python3 tests for now

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 5.0.6-3
- Fix descriptions
- Fix for F22

* Thu Jan 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 5.0.6-2
- Simplify spec file
- Improve spec file
- Add tests

* Wed Jan 06 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 5.0.6-1
- Align to current upstream

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 31 2014 Tom Callaway <spot@fedoraproject.org> - 5.0.5-2
- fix license handling

* Thu Jun 26 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 5.0.5-1
- Updated to 5.0.5 (new upstream "with the blessing of original creator")
- Introduced python3-configobj subpackage
- Changed upstream url to documentation written by new upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 17 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 4.7.2-1
- Fix traceback when doing from validate import *
- Upstream bugfix release

* Wed Jan 20 2010 Luke Macken <lmacken@redhat.com> - 4.7.0-2
- Merge a bunch of changes from Gareth Armstrong <gareth.armstrong@hp.com>
    - The src zip file should come either from http://www.voidspace.org.uk/
      downloads/ or http://code.google.com/p/configobj/ as the PyPI tarball is
      not complete.  No docs and no test code.
    - Added docs
    - Remove BR on python-setuptools-devel

* Sun Jan 10 2010 Luke Macken <lmacken@redhat.com> - 4.7.0-1
- Update to 4.7.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Yaakov M. Nemoy <ynemoy@fedoraproject.org> - 4.6.0-1
- updated to latest upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 09 2009 Luke Macken <lmacken@redhat.com> - 4.5.3-4
- Conditionally include the egg-info, when available (#478417)

* Mon Dec 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 4.5.3-3
- Upload Source file so this actually builds.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.5.3-2
- Rebuild for Python 2.6

* Sat Jun 28 2008 Luke Macken <lmacken@redhat.com> - 4.5.3-1
- Update to 4.5.3

* Thu Feb 28 2008 Luke Macken <lmacken@redhat.com> - 4.5.2-1
- Update to 4.5.2

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 4.4.0-2
- Update for python-setuptools changes in rawhide

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 4.4.0-1
- 4.4.0

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 4.3.2-6
- Rebuild for python 2.5

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 4.3.2-5
- Fix dist tag

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 4.3.2-4
- Rebuild for FC6

* Mon Aug 14 2006 Luke Macken <lmacken@redhat.com> - 4.3.2-3
- Include pyo files

* Tue Jul 18 2006 Luke Macken <lmacken@redhat.com> - 4.3.2-2
- Fix typo in the url

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 4.3.2-1
- Initial package
