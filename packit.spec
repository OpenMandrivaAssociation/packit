%define	name	packit
%define	version	1.0
%define	rel	8
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

