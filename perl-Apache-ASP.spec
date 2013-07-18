%define upstream_name    Apache-ASP
%define upstream_version 2.61

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A perl ASP port to Apache
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.bz2
Source1:	asp.html
Source2:	perl-Apache-ASP.conf

BuildRequires:	perl-devel
BuildRequires:	perl(Apache::Filter)
BuildRequires:	perl-base
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(DB_File)
BuildRequires:	perl(HTML::Clean)
BuildRequires:	perl(MLDBM)
BuildRequires:  perl(MLDBM::Sync)
BuildRequires:  perl(HTML::FillInForm)
BuildRequires:  perl(XML::Sablotron)
BuildRequires:	perl(Tie::Cache)
BuildRequires:	perl(Tie::TextDir)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(XML::XSLT)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:	perl(CGI)
BuildRequires:	perl(DB_File)
BuildRequires:  perl(Apache::Filter)
Provides:	perl(Apache::ASP::Share::CORE)
Provides:	Apache-ASP = %{version}-%{release}
Requires:	apache-mod_perl >= 1:2.0.2
BuildArch:	noarch

%description
Apache::ASP provides an Active Server Pages port to the Apache Web Server
with Perl scripting only, and enables developing of dynamic web applications
with session management and embedded Perl code. There are also many powerful
extensions, including XML taglibs, XSLT rendering, and new events not
originally part of the ASP API!

This module works under the Apache Web Server with the mod_perl module
enabled. See http://www.apache.org and http://perl.apache.org for further
information.

This is a portable solution, similar to ActiveState's PerlScript for NT/IIS
ASP. Work has been done and will continue to make ports to and from this
implementation as smooth as possible.

For Apache::ASP downloading and installation, please read the INSTALL
section. For installation troubleshooting check the FAQ and the SUPPORT
sections.

For database access, ActiveX, scripting languages, and other miscellaneous
issues please read the FAQ section.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# optional test, causes trouble when Devel::Symdump is installed
rm -f t/stat_inc
make test

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_var}/www/perl
cp -pr site %{buildroot}%{_var}/www/perl/%{upstream_name}

install -d -m 755 %{buildroot}%{_var}/www/html/addon-modules/
cp %{SOURCE1} %{buildroot}%{_var}/www/html/addon-modules/%{upstream_name}.html

install -d -m 755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install %{SOURCE2} -m 644  %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/perl-Apache-ASP.conf

%files
%doc CHANGES README
%config(noreplace) %{_webappconfdir}/perl-Apache-ASP.conf
%dir %{_var}/www/perl/%{upstream_name}
%{_var}/www/perl/%{upstream_name}/*
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Bundle/Apache
%{_mandir}/*/*
%{_bindir}/*
%{_var}/www/html/addon-modules/Apache-ASP.html


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.610.0-3mdv2011.0
+ Revision: 680451
- mass rebuild

* Mon Feb 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.610.0-2mdv2011.0
+ Revision: 502378
- rely on filetrigger for reloading apache configuration begining with 2010.1, rpm-helper macros otherwise

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.610.0-1mdv2010.0
+ Revision: 402962
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.61-2mdv2009.0
+ Revision: 268364
- rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.61-1mdv2009.0
+ Revision: 213315
- new version
  uncompress additional sources
  large spec cleanup

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 02 2007 Funda Wang <fwang@mandriva.org> 2.59-4mdv2008.0
+ Revision: 94723
- fix provides

* Mon Jun 25 2007 Oden Eriksson <oeriksson@mandriva.com> 2.59-3mdv2008.0
+ Revision: 43840
- fix deps


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.59-2mdv2007.0
+ Revision: 73193
- import perl-Apache-ASP-2.59-2mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.59-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires
	- URL
	- Source URL

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandrakesoft.com> 2.59-1mdk
- 2.59
- renamed to perl-Apache-ASP
- added apache config

* Fri Feb 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.51-5mdk
- spec file cleanups, remove the ADVX-build stuff

* Tue Mar 02 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.51-4mdk
- rebuild

