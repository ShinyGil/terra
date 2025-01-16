%global commit 0019b5d8af9d558aa7888218dfeeafef6104277a
%global commit_date 20241121
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gstreamer1-plugin-icamerasrc
Summary:        GStreamer 1.0 Intel IPU6 camera plugin
Version:        %{commit_date}.%{shortcommit}
Release:        1%{?dist}
License:        LGPL-2.1-only
Source0:        https://github.com/intel/icamerasrc/archive/%{commit}/icamerasrc-%{shortcommit}.tar.gz
Patch0:         %{name}-videoformat.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  ipu6-camera-hal-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(gstreamer-va-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gstreamer-controller-1.0) >= 1.0.0
ExclusiveArch:  x86_64

%description
This package provides the GStreamer plugin for the Intel IPU6 MIPI camera.

%package devel
Summary:        GStreamer plugin development files for Intel IPU6 camera
Requires:       gstreamer1-devel
Requires:       ipu6-camera-bins-devel
Requires:       ipu6-camera-hal-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for the GStreamer IPU6 camera plugin.

%prep
%autosetup -p1 -n icamerasrc-%{commit}
autoreconf -vif

%build
export CHROME_SLIM_CAMHAL=ON
export STRIP_VIRTUAL_CHANNEL_CAMHAL=ON
%configure --enable-gstdrmformat --with-haladaptor
%make_build

%install
%make_install

%files
%license LICENSE
%{_libdir}/gstreamer-1.0/*
%{_libdir}/libgsticamerainterface-1.0.so.1
%{_libdir}/libgsticamerainterface-1.0.so.1.0.0

%files devel
%{_libdir}/libgsticamerainterface-1.0.so
%{_includedir}/gstreamer-1.0/gst/*
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
