Summary:		Ozon multimedia codecs
Name:			ozon-multimedia-codecs
Version:		21
Release:		1%{?dist}

License:		GPL-3
Group:			System Environment/Base

URL:			http://ozonos.github.io

Requires:		gstreamer1-libav
Requires:		gstreamer1-plugins-bad-free
Requires:		gstreamer1-plugins-bad-freeworld
Requires:		gstreamer1-plugins-base
Requires:		gstreamer1-plugins-good
Requires:		gstreamer1-plugins-ugly
Requires:		gstreamer-ffmpeg
Requires:		gstreamer-plugins-bad
Requires:		gstreamer-plugins-bad-free
Requires:		gstreamer-plugins-bad-nonfree
Requires:		gstreamer-plugins-base
Requires:		gstreamer-plugins-espeak
Requires:		gstreamer-plugins-fc
Requires:		gstreamer-plugins-good
Requires:		gstreamer-plugins-ugly
Requires:		gstreamer-rtsp
Requires:		amrnb
Requires:		amrwb
Requires:		faac
Requires:		faad2
Requires:		flac
Requires:		lame
Requires:		libdca
Requires:		libmad
Requires:		libmatroska
Requires:		x264
Requires:		xvidcore

BuildArch:		noarch

%description
The multimedia codecs for Ozon desktop.

%files

%changelog
* Tue Feb 17 2015 Satyajit Sahoo <satya164@fedoraproject.org> - 0.0-1
- Initial package for Fedora

