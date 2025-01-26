let html = get("https://gstreamer.freedesktop.org/src/gst-plugins-bad/?C=M;O=D");
let v = find(`gst-plugins-bad-([\d.]+)\.tar\.xz`, html, 1);
rpm.version(v);
