Name: pamixer
Version: 1.3.1
Release:1%{?dist}
Summary: pamixer is like amixer but for pulseaudio

License: GPLv3
URL: https://github.com/cdemoulins/pamixer

BuildRequires: boost-devel
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
%make_install


%check


%files
/usr/local/bin/pamixer

%changelog
* Mon Apr 10 2017 notkild <notkild@gmail.com> 1.3.1-1
- new package built with tito


