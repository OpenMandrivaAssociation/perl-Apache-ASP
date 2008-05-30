%define module Apache-ASP

Summary:	Apache::ASP - A perl ASP port to Apache
Name:		perl-%{module}
Version:	2.61
Release:	%mkrel 1
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache/%{module}-%{version}.tar.bz2
Source1:	asp.html
Source2:	perl-Apache-ASP.conf
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires(pre):  apache-conf >= 2.2.0
Requires(pre):  apache >= 2.2.0
Requires(pre):	apache-mpm >= 2.2.0
Requires(pre):	apache-mod_perl >= 1:2.0.2
Requires:	apache-conf >= 2.2.0
Requires:	apache-mpm >= 2.2.0
Requires:	apache-mod_perl >= 1:2.0.2
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
Obsoletes:	Apache-ASP
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# optional test, causes trouble when Devel::Symdump is installed
rm -f t/stat_inc
make test

%install
rm -rf %{buildroot}

%makeinstall_std

install -d -m 755 %{buildroot}%{_var}/www/perl
cp -pr site %{buildroot}%{_var}/www/perl/%{module}

install -d -m 755 %{buildroot}%{_var}/www/html/addon-modules/
cp %{SOURCE1} %{buildroot}%{_var}/www/html/addon-modules/%{module}.html

install -d -m 755 %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install %{SOURCE2} -m 644  %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/perl-Apache-ASP.conf

%post
if [ -f %{_var}/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart 1>&2;
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f %{_var}/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart 1>&2
    fi
fi

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/perl-Apache-ASP.conf
%dir %{_var}/www/perl/%{module}
%{_var}/www/perl/%{module}/*
%{perl_vendorlib}/Apache
%{perl_vendorlib}/Bundle/Apache
%{_mandir}/*/*
%{_bindir}/*
%{_var}/www/html/addon-modules/Apache-ASP.html



