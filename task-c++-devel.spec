
# THIS PACKAGE IS STORED IN SVN
# PLEASE DO NOT UPLOAD WITHOUT
# COMMITTING YOUR CHANGES FIRST

Name: task-c++-devel
Version: 2013.1
Release: 1
License: GPL
Summary: Metapackage for C++ development
Summary(pt_BR): Metapacote para desenvolvimento em C++
Group: Development/C++
Requires: task-c-devel
Requires: gcc-c++
BuildArch: noarch

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a complete environment for development of programs in the C++
programming language.

It itself includes no software, only dependencies on software.

%description -l pt_BR
Este pacote é um metapacote, ou seja, o seu único propósito é conter
dependências para um completo ambiente de desenvolvimento de programas em C++.

Este pacote não inclui nenhum programa, apenas dependências para outros
programas.

%files
%defattr(0644,root,root,0755)





%changelog
* Tue Apr 19 2011 Antoine Ginies <aginies@mandriva.com> 2011.0-1mdv2011.0
+ Revision: 655947
- bumpo to 2011 release

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.0-4mdv2011.0
+ Revision: 607975
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2009.0-3mdv2010.1
+ Revision: 524163
- rebuilt for 2010.1

* Tue Sep 01 2009 Christophe Fergeau <cfergeau@mandriva.com> 2009.0-2mdv2010.0
+ Revision: 423749
- rebuild

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-1mdv2009.0
+ Revision: 282560
- bump version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2008-3mdv2009.0
+ Revision: 242853
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 2008-1mdv2008.0
+ Revision: 69901
- fix wrong prereq


* Fri Aug 04 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-08-04 14:59:57 (51796)
- updated version to 2007

* Fri Aug 04 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-08-04 14:58:16 (51791)
- import task-c++-devel-2006-1mdk

* Fri Jul 29 2005 Andreas Hasenack <andreas@mandriva.com> 2006-1mdk
- packaged for Mandriva

