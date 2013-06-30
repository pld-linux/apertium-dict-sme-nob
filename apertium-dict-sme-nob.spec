Summary:	Northern Sami-Norwegian Bokmaal and Slovenian language pair for Apertium
Summary(pl.UTF-8):	Para języków północnolapoński-norweski bokmaal dla Apertium
%define	lpair	sme-nob
Name:		apertium-dict-%{lpair}
Version:	0.5.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	6f805e1e4f4d787653da81e82a089fc9
Patch0:		%{name}-cg.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	apertium-lex-tools
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	hfst
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.6
BuildRequires:	vislcg3
Requires:	apertium >= 3.2.0
Requires:	apertium-lex-tools
Requires:	hfst
Requires:	lttoolbox >= 3.2.0
Requires:	vislcg3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Northern Sami and Norwegian Bokmaal, morphological analysis or
part-of-speech tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między północnolapońskim a norweskim bokmaal, a także analizy
morfologicznej lub oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/sme-nob.mode
