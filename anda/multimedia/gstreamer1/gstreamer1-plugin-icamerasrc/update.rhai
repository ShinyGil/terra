let url = `https://api.github.com/repos/intel/icamerasrc/commits/icamerasrc_slim_api`;
let json = get(url).json();
let c = json.sha;
let d = json.commit.author.date;
date.truncate(10);
rpm.global("commit", v);
rpm.global("fulldate", d);
