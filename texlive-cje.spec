Name:		texlive-cje
Version:	46721
Release:	2
Summary:	LaTeX document class for CJE articles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cje
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cje.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cje.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cje article class allows authors to format their papers to
Canadian Journal of Economics style with minimum effort. The
class includes options for two other formats: "review" (double
spaced, for use at the submission stage) and "proof" (used by
the typesetters to prepare the proof authors will receive for
approval).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cje
%{_texmfdistdir}/bibtex/bst/cje
%doc %{_texmfdistdir}/doc/latex/cje

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
