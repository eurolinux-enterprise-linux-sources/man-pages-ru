%define	name	manpages-ru
%define	ver	0.6
%define	rel	1.rl
%define	prefix	/usr

Summary: 	%{name} -- Russian translations of Linux manpages.
Summary(ru):	%{name} -- русские переводы страниц руководства по Linux.

Name: 		%{name}
Version: 	%{ver}
Release: 	%{rel}
Copyright: 	GPL
Group: 		Documentation

Source:		http://alexm.here.ru/manpages/download/%{name}-%{ver}.tar.gz

Url:		http://alexm.here.ru/%{name}/
Docdir:		/usr/doc
BuildArch:	noarch
BuildRoot:	/var/tmp/%{name}-root


%description
A small collection of man pages (documentation) from the Linux Documentation
Project (LDP) translated to russian.  The man pages are organized into the
following sections: Section 1, user commands; Section 2, system
calls; Section 3, libc calls; Section 4, devices (e.g., hd, sd); Section 5,
file formats and protocols (e.g., wtmp, /etc/passwd, nfs); Section 6, games
(intro only); Section 7, conventions, macro packages, etc. (e.g., nroff,
ascii); and Section 8, system administration.

%description(ru)
Небольшая коллекция страниц руководства из Проекта Документации на
Линукс, на русском языке.  Страницы руководства организованы следующим
образом: секция 1, команды пользователя; секция 2, системные вызовы;
секция 3, функции библиотеки языка C; секция 4, устройства (например,
hd, sd); секция 4, форматы файлов и протоколы (например, wtmp,
/etc/passwd, nfs); секция 6, игры (только введение); секция 7,
соглашения, макро-пакеты, и т. п. (например, nroff, ascii); и секция
8, утилиты администратора.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/man/ru/man{1,2,3,4,5,6,7,8,9,n}

for i in man?; do
    install -m0644 $i/* $RPM_BUILD_ROOT%{prefix}/man/ru/$i
done

bzip2 -9f $RPM_BUILD_ROOT%{prefix}/man/ru/*/*

##################
# Build Filelist 
#
find $RPM_BUILD_ROOT -type f -or -type l > files.%{name}.tmp
cat files.%{name}.tmp | sed "s|$RPM_BUILD_ROOT/|/|" > files.%{name}

%files -f files.%{name}
%doc INSTALL INSTALL.ru NEWS README FAQ
%dir %attr (0755, root, root) %{prefix}/man/ru/man1
%dir %attr (0755, root, root) %{prefix}/man/ru/man2
%dir %attr (0755, root, root) %{prefix}/man/ru/man3
%dir %attr (0755, root, root) %{prefix}/man/ru/man4
%dir %attr (0755, root, root) %{prefix}/man/ru/man5
%dir %attr (0755, root, root) %{prefix}/man/ru/man6
%dir %attr (0755, root, root) %{prefix}/man/ru/man7
%dir %attr (0755, root, root) %{prefix}/man/ru/man8
%dir %attr (0755, root, root) %{prefix}/man/ru/man9
%dir %attr (0755, root, root) %{prefix}/man/ru/mann
