Name:           perl-File-Which
Version:        1.09
Release:        2%{?dist}
Summary:        Portable implementation of the 'which' utility

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/File-Which/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/File-Which-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::Script)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::Which is a portable implementation (in Perl) of 'which', and can
be used to get the absolute filename of an executable program
installed somewhere in your PATH, or just check for its existence. It
includes the command-line utility 'pwhich' which has the same function
as 'which'.


%prep
%setup -q -n File-Which-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/pwhich
%{perl_vendorlib}/File/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.09-2
- rebuild against perl 5.10.1

* Mon Oct  5 2009 Stepan Kasal <skasal@redhat.com> - 1.09-1
- new upstream version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-4
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-3
- rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.05-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Dec 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-2
- find: fixed arguments order.

* Sun Dec 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.05-1
- First build.
