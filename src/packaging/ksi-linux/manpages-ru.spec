#
# $Id: manpages-ru.spec,v 1.2 2000/09/30 11:17:47 alexm Exp $
#
%define name manpages-ru
%define version 0.6
Summary: manpages-ru -- Russian translations of Linux manpages.
Summary(ru): manpages-ru -- ������� �������� ������� ����������� �� Linux
Name: %{name}
Packager: Dmitry N. Hramtsov <hdn@inet.ssc.nsu.ru>
Version: %{version}
Release: 1
Url: http://alexm.here.ru/manpages-ru/
Source: http://alexm.here.ru/%{name}/download/%{name}-%{version}.tar.gz
Copyright: Freely Distributable
Group: Documentation
Group(ru): ������������
Buildroot: /var/tmp/%{name}-root
BuildArchitectures: noarch

%description
A small collection of man pages (documentation) from the Linux Documentation
Project (LDP) translated to russian.  The man pages are organized into the
following sections: Section 1, user commands; Section 2, system
calls; Section 3, libc calls; Section 4, devices (e.g., hd, sd); Section 5,
file formats and protocols (e.g., wtmp, /etc/passwd, nfs); Section 6, games
(intro only); Section 7, conventions, macro packages, etc. (e.g., nroff,
ascii); and Section 8, system administration.

%description(ru)
��������� ��������� ������� ����������� �� ������� ������������ ��
������, �� ������� �����.  �������� ����������� ������������ ���������
�������: ������ 1, ������� ������������; ������ 2, ��������� ������;
������ 3, ������� ���������� ����� C; ������ 4, ���������� (��������,
hd, sd); ������ 4, ������� ������ � ��������� (��������, wtmp,
/etc/passwd, nfs); ������ 6, ���� (������ ��������); ������ 7,
����������, �����-������, � �. �. (��������, nroff, ascii); � ������
8, ������� ��������������.

%prep
mkdir -p $RPM_BUILD_ROOT/usr/man

%setup

%build

%install
make install INSTALLPATH=$RPM_BUILD_ROOT/usr/man LANG_SUBDIR=ru

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README NEWS FAQ
/usr/man/*
