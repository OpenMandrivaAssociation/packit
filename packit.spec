%define	name	packit
%define	version	1.0
%define	rel	7
%define	release	%mkrel %{rel}

Summary:	Network Injection And Capture Tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.7.1-update-headers-for-new-libpcap.patch.bz2
URL:		http://www.obtuse.net/software/packit/
License:	GPL
Group:		Monitoring
BuildRequires:	libpcap-devel
BuildRequires:	net-devel >= 1.1.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Packit is a network auditing tool that allows you to monitor,
manipulate, and inject customized IP traffic into your
network. Supporting the ability to define (spoof) all TCP, UDP,
ICMP, IP, ARP, RARP and Ethernet header options, Packit can be
valuable for testing firewalls, intrusion detection systems, port
scanning, simulating network traffic and general TCP/IP auditing.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog docs/ICMP.txt
%{_mandir}/*/*
%defattr(755,root,root,755)
%{_sbindir}/*



%changelog
* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2010.0
+ Revision: 382738
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2009.1
+ Revision: 298337
- rebuilt against libpcap-1.0.0

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.0-5mdv2009.0
+ Revision: 141036
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2008.1
+ Revision: 130989
- kill re-definition of %%buildroot on Pixel's request
- import packit


* Sat Apr 01 2006 Guillaume Bedot <littletux@mandriva.org> 1.0-5mdk
- fixed URL, Source0, buildrequires

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdk
- rebuilt against libnet1.1.2

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Thu May 05 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-2mdk
- fix problems with docs
- %%mkrel

* Thu Apr 15 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.0-1mdk
- 1.0

* Tue Mar 02 2004 Per Ãyvind Karlsen <peroyvind@linux-mandrake.com> 0.7.1-1mdk
- 0.7.1
- fix build against newer libpcap (P0)

* Wed Nov 26 2003 Per Ãyvind Karlsen <peroyvind@linux-mandrake.com> 0.7-1mdk
- 0.7

* Sun Apr 13 2003 Marcel Pol <mpol@gmx.net> 0.5.0-0.b.2mdk
- buildrequires

* Mon Apr 07 2003 Per Ãyvind Karlsen <peroyvind@sintrax.net> 0.5.0-0.b.1mdk
- initial mdk release
