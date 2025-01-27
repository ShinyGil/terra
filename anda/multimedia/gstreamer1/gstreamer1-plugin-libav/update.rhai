let release = labels.branch.to_upper();
let ver = get(`https://bodhi.fedoraproject.org/updates/?search=
gstreamer1-plugin-libav&status=stable&releases=F41&rows_per_page=1&page=1`).json().updates[0].title;
rpm.version(find(`
gstreamer1-plugin-libav-([\d.]+)`, ver, 1));
