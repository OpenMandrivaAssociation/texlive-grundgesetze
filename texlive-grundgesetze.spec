%global tl_name grundgesetze
%global tl_revision 58997

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	Typeset Freges Grundgesetze der Arithmetik
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/grundgesetze
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grundgesetze.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grundgesetze.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grundgesetze.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines maths mode commands for typesetting Gottlob Frege's
concept-script in the style of his "Grundgesetze der Arithmetik" (Basic
Laws of Arithmetic).

