
# THIS PACKAGE IS STORED IN SVN
# PLEASE DO NOT UPLOAD WITHOUT
# COMMITTING YOUR CHANGES FIRST

Name: task-c++-devel
Version: 2011.0
Release: %mkrel 1
License: GPL
Summary: Metapackage for C++ development
Summary(pt_BR): Metapacote para desenvolvimento em C++
Group: Development/C++
Requires: task-c-devel
Requires: gcc-c++
Requires: libstdc++-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for a complete environment for development of programs in the C++
programming language.

It itself includes no software, only dependencies on software.

%description -l pt_BR
Este pacote � um metapacote, ou seja, o seu �nico prop�sito � conter
depend�ncias para um completo ambiente de desenvolvimento de programas em C++.

Este pacote n�o inclui nenhum programa, apenas depend�ncias para outros
programas.

%files
%defattr(0644,root,root,0755)



