Name: polybar
Version: 3.0.6
Release:        1%{?dist}
Summary: A fast and easy-to-use tool for creating status bars.

License: MIT
URL: https://github.com/jaagr/polybar

BuildRequires: git clang cmake cairo-devel git jsoncpp-devel libxcb-devel python2 xcb-proto xcb-util-image-devel xcb-util-wm-devel xcb-util-xrm-devel wireless-tools-devel libmpdclient-devel libcurl-devel alsa-lib-devel
Requires: cairo libxcb python2 xcb-proto xcb-util-image xcb-util-wm xcb-util-xrm jsoncpp

%description
A fast and easy-to-use tool for creating status bars.

%prep
rm -rf polybar
git clone https://github.com/jaagr/polybar --recursive --branch %{version}

%build
cd polybar
mkdir build
cd build
cmake .. -DCMAKE_C_COMPILER="clang" -DCMAKE_CXX_COMPILER="clang++" -DENABLE_ALSA:BOOL="ON" -DENABLE_I3:BOOL="ON" -DENABLE_MPD:BOOL="ON" -DENABLE_NETWORK:BOOL="ON" -DENABLE_CURL:BOOL="ON"
make

%install
cd polybar/build
%make_install

%files

%changelog
* Mon Apr 10 2017 notkild <notkild@gmail.com> 3.0.6-1
- new package built with tito


