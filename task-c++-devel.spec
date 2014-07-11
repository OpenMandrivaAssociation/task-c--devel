
# THIS PACKAGE IS STORED IN SVN
# PLEASE DO NOT UPLOAD WITHOUT
# COMMITTING YOUR CHANGES FIRST

Name: task-c++-devel
Version: %distro_release
Release: 3
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


