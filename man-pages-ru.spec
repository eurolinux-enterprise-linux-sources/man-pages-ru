%global mpr_version 3.41-2145-1699-20120901
Summary: Russian man pages from the Linux Documentation Project
Name: man-pages-ru
Version: 3.41
Release: 2.20120901%{?dist}
# Multiple man pages are distributed under different licenses.
License: GPL+ and BSD and MIT and GFDL
Group: Documentation
URL: http://sourceforge.net/projects/man-pages-ru/
Source: http://sourceforge.net/projects/man-pages-ru/files/man-pages-ru_%{mpr_version}.tar.bz2

Requires: man-pages-reader

BuildArchitectures: noarch

%description
Manual pages from the Linux Documentation Project, translated into
Russian.

%prep
%setup -q -n man-pages-ru_%{mpr_version}

# remove .so links to nonexisting pages
for exp in $(grep -rw "^\.so" . | tr " " "_"); do
    link=${exp#.*:\.so_}
    [ -f $link ] || rm -f ${exp%:.*}
done

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ru
cp -pr ./man? $RPM_BUILD_ROOT%{_mandir}/ru

%files
%doc README License
%{_mandir}/ru/man*/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.41-2.20120901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Peter Schiffer <pschiffe@redhat.com> - 3.41-1.20120901
- updated to the latest upstream tarball 3.41-2145-1699-20120901
- cleaned .spec file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Alexey Kurov <nucleo@fedoraproject.org> - 0.98-5
- Man-pages-ru 3.32-2087-1553-20110626
- fix build

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Alexey Kurov <nucleo@fedoraproject.org> - 0.98-3
- Man-pages-ru 3.32-2087-1512-20101219

* Fri Aug 13 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 0.98-2
- remove bogus links

* Fri Jul 23 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.98-1
- updated Source to 0.98 (0.97-0.98 patch)
- updated Source1 to 3.25-2064-1352-20100717
- moved encoding converting to prep section

* Tue May 11 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 0.97-10
- add new source (Source1)

* Fri Apr 16 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 0.97-9
- add man-pages-reader dependence

* Wed Mar 17 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 0.97-8
- remove directories from the package
  fix minor spec problems

* Fri Dec 18 2009 Ivana Hutarova Varekova <varekova@redhat.com> - 0.97-7
- fix the source tags

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.97-4
- fix license tag

* Mon Jun 16 2008 Ivana Varekova <varekova@redhat.com> - 0.97-3
- rebuild
- change license tag

* Fri Mar  2 2007 Ivana Varekova <varekova@redhat.com> - 0.97-2
- Resolves: 226129
  incorporate package review feedback

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.97-1.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Oct 21 2004 Adrian Havill <havill@redhat.com> 0.97-1
- Russian translation project active again; newest update merged with
  working Makefile (#131659)

* Wed Sep 29 2004 Elliot Lee <sopwith@redhat.com> 0.7-8
- Rebuild

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 0.7-6
- Convert all manpages to utf-8.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.7-5
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.7-4
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.7-1
- 0.7

* Thu Aug  2 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Own %%{_mandir}/ru

* Wed Apr  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- roff fixes

* Mon Feb  5 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Version 0.6

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
