# revision 33289
# category Package
# catalog-ctan /macros/latex/contrib/grundgesetze
# catalog-date 2014-04-08 11:20:21 +0200
# catalog-license gpl2
# catalog-version 1.01
Name:		texlive-grundgesetze
Version:	1.02
Release:	1
Summary:	Typeset Frege's Grundgesetze der Arithmetik
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/grundgesetze
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grundgesetze.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grundgesetze.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grundgesetze.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines maths mode commands for typesetting Gottlob
Frege's concept-script in the style of his "Grundgesetze der
Arithmetik" (Basic Laws of Arithmetic).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/grundgesetze/grundgesetze.sty
%doc %{_texmfdistdir}/doc/latex/grundgesetze/README
%doc %{_texmfdistdir}/doc/latex/grundgesetze/grundgesetze.pdf
#- source
%doc %{_texmfdistdir}/source/latex/grundgesetze/grundgesetze.dtx
%doc %{_texmfdistdir}/source/latex/grundgesetze/grundgesetze.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
