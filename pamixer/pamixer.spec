Name: pamixer
Version: 1.3.1
Release:3
Summary: pamixer is like amixer but for pulseaudio

License: GPLv3
URL: https://github.com/cdemoulins/pamixer

BuildRequires: boost-devel
BuildRequires: git
BuildRequires: glibc-common
BuildRequires: pulseaudio-libs-devel
Requires: boost-program-options
Requires: pulseaudio
Requires: pulseaudio-libs

%description


%prep
rm -rf pamixer
git clone https://github.com/cdemoulins/pamixer --branch %{version}

%build
cd pamixer
%make_build


%install
cd pamixer
mkdir -p %{buildroot}/usr/bin
/usr/bin/make install PREFIX=%{buildroot}/usr


%check


%files
%{_bindir}/pamixer

%changelog
* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.3.1-3
- 

* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.3.1-2
-

* Mon Apr 10 2017 notkild <notkild@gmail.com>
-

* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.3.1-1
- new package built with tito


