Name: light
Version: 1.0
Release: 4
Summary: Light is a program to control backlight controllers under GNU/Linux, it is the successor of lightscript, which was a bash script with the same purpose, and tries to maintain the same functionality.

License: GPLv3
URL: https://github.com/haikarainen/light

BuildRequires: git
BuildRequires: help2man
BuildRequires: sed

%description


%prep
rm -rf light
git clone https://github.com/haikarainen/light --branch v%{version}
cd light
sed '/chown/d' Makefile > Makefile.tmp
sed '/chmod/d' Makefile.tmp > Makefile


%build
cd light
make all


%install
cd light
%make_install


%check


%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.0-4
- 

* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.0-3
-

* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.0-2
-

* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.0-1
- new package built with tito


