#
# This is primary Makefile for manpages-ru project
#
# $Id: Makefile,v 1.22 2001/08/11 21:03:08 alexm Exp $
#

#
# This is package version
#
VERSION = 0.7

#
# This is where to install manpages
#
INSTALLPATH = /usr/local/share/man

#
# This is language subdirectory in $INSTALLPATH
# See $LANG description in man(1)
#
LANG_SUBDIR = ${LANG}

#
# How to compress manpages.
# Known compressors are `none', `gzip', `compress', `bzip2'
#
COMPRESS = gzip

#
# Compressor options
#
COMPRESS_OPTIONS = 

#
# Compress manpage only if its size is greater than $COMPRESS_SIZE
#
COMPRESS_SIZE = 4096

#
# `install' command
#
INSTALL = install -m 644


all:
	for d in 1 2 3 4 5 6 7 8; do \
		make -C man$$d all; \
	done

clean:
	for d in 1 2 3 4 5 6 7 8; do \
		make -C man$$d clean; \
	done

install: install-pages install-aliases

install-pages:
	[ -d $(INSTALLPATH) ] || mkdir $(INSTALLPATH)
	[ -d $(INSTALLPATH)/$(LANG_SUBDIR) ] || mkdir $(INSTALLPATH)/$(LANG_SUBDIR)
	if [ x$(COMPRESS) != xgzip -a \
	     x$(COMPRESS) != xbzip2 -a \
	     x$(COMPRESS) != xnone -a \
	     x$(COMPRESS) != xcompress ]; then \
	  echo Error: Invalid compressor $(COMPRESS) ; \
	  exit 1; \
	fi
	for section in 1 2 3 4 5 6 7 8; do \
	  [ -d man$$section ] || continue; \
	  [ -d $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section ] || \
		mkdir $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section; \
	  cd man$$section; \
	  if [ x"`echo *.$$section`" != x\*.$$section ]; then \
	    for manpage in *.$$section; do \
	      rm -f $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section/$$manpage; \
	      for ext in gz Z bz2; do \
	        rm -f $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section/$$manpage.$$ext; \
	      done; \
	      $(INSTALL) $$manpage $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section; \
	      FILESIZE=`ls -l $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section/$$manpage | \
	                tr -s ' ' | cut -d ' ' -f 5`; \
	      if [ $$FILESIZE -gt $(COMPRESS_SIZE) ]; then \
	        if [ x$(COMPRESS) != xnone ]; then \
	          $(COMPRESS) $(COMPRESS_OPTIONS) $(INSTALLPATH)/$(LANG_SUBDIR)/man$$section/$$manpage; \
	        fi; \
	      fi; \
	    done; \
	  fi; \
	  cd ..; \
	done

install-aliases:
	for section in 1 2 3 4 5 6 7 8; do \
	  [ -d man$$section ] || continue; \
	  [ -f man$$section/ALIASES ] || continue; \
	  cd man$$section; \
	  dest_dir=$(INSTALLPATH)/$(LANG_SUBDIR)/man$$section; \
	  sed -e "/^#/d" -e "s,^\(.\+\)	\(.\+\)$$,\
	    rm -f $$dest_dir/\2.$$section $$dest_dir/\2.$$section.gz \
		$$dest_dir/\2.$$section.Z $$dest_dir/\2.$$section.bz2; \
		echo .so man$$section/\1.$$section \> $$dest_dir/\2.$$section," \
			< ALIASES > tmp-run; \
	  . tmp-run; \
	  rm -f tmp-run; \
	  cd ..; \
	done

html:
	./mkindex.html.sh > index.html
	for d in 1 2 3 4 5 6 7 8; do \
		make -C man$$d html; \
	done

dist:	all
	TARFILE=download/manpages-ru-$(VERSION).tar; \
	rm -f $$TARFILE $$TARFILE.gz $$TARFILE.bz2; \
	DISTDIR=manpages-ru-$(VERSION); \
	rm -f $$DISTDIR; \
	ln -s . $$DISTDIR; \
	tar -c -f $$TARFILE $$DISTDIR/Makefile \
		$$DISTDIR/README \
		$$DISTDIR/CREDITS \
		$$DISTDIR/INSTALL \
		$$DISTDIR/INSTALL.ru \
		$$DISTDIR/NEWS \
		$$DISTDIR/FAQ \
		$$DISTDIR/packaging/ksi-linux/manpages-ru.spec \
		$$DISTDIR/packaging/ruslinux/manpages-ru.spec; \
	tar -r -f $$TARFILE $$DISTDIR/debian/ \
		--exclude '*~' --exclude tmp --exclude CVS; \
	for section in 1 2 3 4 5 6 7 8; do \
	  if [ x"`echo man$$section/*.$$section`" != x\man$$section/\*.$$section ]; then \
	    tar -r -f $$TARFILE $$DISTDIR/man$$section/*.$$section; \
	    if [ -f $$DISTDIR/man$$section/ALIASES ]; then \
	      tar -r -f $$TARFILE $$DISTDIR/man$$section/ALIASES; \
	    fi; \
	  fi; \
	done; \
	bzip2 -c $$TARFILE > $$TARFILE.bz2; \
	gzip $$TARFILE; \
	rm -f $$DISTDIR

publish: html dist
	mkdir -p $$HOME/public_html/manpages-ru/
	mkdir -p $$HOME/public_html/manpages-ru/download/
	cyrrecode k w < index.html > $$HOME/public_html/manpages-ru/index.html
	cyrrecode k w < NEWS > $$HOME/public_html/manpages-ru/NEWS
	cyrrecode k w < FAQ > $$HOME/public_html/manpages-ru/FAQ
	cp download/manpages-ru-$(VERSION).tar.gz $$HOME/public_html/manpages-ru/download/
	cp download/manpages-ru-$(VERSION).tar.bz2 $$HOME/public_html/manpages-ru/download/
	for section in 1 2 3 4 5 6 7 8; do \
	  [ -d ../public_html/manpages-ru/man$$section ] || mkdir ../public_html/manpages-ru/man$$section; \
	  if [ x"`echo man$$section/*.$$section`" != x\man$$section/\*.$$section ]; then \
	    for manpage in man$$section/*.$$section; do \
	      cyrrecode k w < $$manpage.html > ../public_html/manpages-ru/$$manpage.html; \
	    done; \
	  fi; \
	done

rpm:	dist
	cp download/manpages-ru-$(VERSION).tar.gz /usr/src/KSI/SOURCES
	rpm -ba packaging/ksi-linux/manpages-ru.spec

publish-rpm: rpm
	mkdir -p $$HOME/public_html/manpages-ru/download/ksi-linux/
	mv /usr/src/KSI/SRPMS/manpages-ru-$(VERSION)-1.src.rpm \
		$$HOME/public_html/manpages-ru/download/ksi-linux/
	mv /usr/src/KSI/RPMS/noarch/manpages-ru-$(VERSION)-1.noarch.rpm \
		$$HOME/public_html/manpages-ru/download/ksi-linux/
