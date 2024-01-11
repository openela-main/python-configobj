Name:           python-configobj
Version:        5.0.6
Release:        25%{?dist}
Summary:        Config file reading, writing, and validation
License:        BSD
URL:            http://configobj.readthedocs.org/
# Moved to the github release instead of the pypi one since multiple elements (License and tests)
# are not available using pypi. Two bugs have been filled about this:
# https://github.com/DiffSK/configobj/issues/98
# https://github.com/DiffSK/configobj/issues/99
# Source0:        https://pypi.python.org/packages/source/c/configobj/configobj-5.0.6.tar.gz
Source0:        https://github.com/DiffSK/configobj/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest
%global _description \
ConfigObj is a simple but powerful configuration file reader and writer: an ini\
file round tripper. Its main feature is that it is very easy to use, with a\
straightforward programmers interface and a simple syntax for config files. 
%description %_description

%package     -n python3-configobj
Summary:        %{summary}
%{?python_provide:%python_provide python3-configobj}
Requires:       python3-six
%description -n python3-configobj %_description

%prep
%autosetup -n configobj-%{version}

%build
%py3_build

%install
%py3_install

%check
# this needs to be set for tests.test_configobj.test_options_deprecation
export PYTHONWARNINGS=always
%{__python3} test_configobj.py
py.test-%{python3_version} tests

%files -n python3-configobj
%doc README.md
%license LICENSE
%{python3_sitelib}/_version.py
%{python3_sitelib}/configobj.py
%{python3_sitelib}/validate.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/configobj-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 5.0.6-25
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 5.0.6-24
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 5.0.6-21
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.6-19
- Subpackage python2-configobj has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.6-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 5.0.6-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 5.0.6-13
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 5.0.6-12
- Minor clean up

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.0.6-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

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
