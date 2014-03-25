Summary:	Network Injection And Capture Tool
Name:		packit
Version:	1.0
Release:	8
License:	GPL
Group:		Monitoring
Url:		http://www.obtuse.net/software/packit/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.7.1-update-headers-for-new-libpcap.patch.bz2
Patch1:		packit-1.0-no-strip.patch
BuildRequires:	libnet-devel
BuildRequires:	pcap-devel

%description
Packit is a network auditing tool that allows you to monitor, manipulate, and
inject customized IP traffic into your network. Supporting the ability to
define (spoof) all TCP, UDP, ICMP, IP, ARP, RARP and Ethernet header options,
Packit can be valuable for testing firewalls, intrusion detection systems,
port scanning, simulating network traffic and general TCP/IP auditing.

%files
%doc ChangeLog docs/ICMP.txt
%{_mandir}/*/*
%{_sbindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std


