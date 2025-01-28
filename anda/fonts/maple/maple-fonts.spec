%define debug_package %nil
%define _ttfontsdir %{_datadir}/fonts/maple
%define  upstream_version %(echo "$( tr '~' '-' <<< "%{version}" )")

Name:           maple-fonts
Version:        7.0~beta36
Release:        1%?dist
Summary:        Open source monospace & nerd font with round corner and ligatures
License:        OFL-1.1
URL:            https://github.com/subframe7536/Maple-font
Source0:        %{url}/releases/download/v%{upstream_version}/MapleMono-NF-CN.zip
Source1:        %{url}/releases/download/v%{upstream_version}/MapleMono-TTF.zip
Source2:        %{url}/releases/download/v%{upstream_version}/MapleMono-NF.zip
Source3:        https://raw.githubusercontent.com/subframe7536/maple-font/refs/heads/variable/README.md
BuildArch:      noarch

%description
%{summary}. The CN version contains the glyphs of simplified and traditional Chinese, and Japanese, which are not as normal as most CN fonts. The CJK glyphs' spacing is much looser for better metric alignment.

%prep
%setup -q -c
%setup -T -D -a1 -a2

%build

%install
install -d %{buildroot}%{_ttfontsdir}
install -d %{buildroot}%{_docdir}/%{name}
# by default install command uses 755 umask
install -m 644 *.ttf %{buildroot}%{_ttfontsdir}
install -m 644 %{SOURCE3} %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE.txt
%{_docdir}/%{name}/README.md
%dir %{_ttfontsdir}
%{_ttfontsdir}/MapleMono*.ttf

%changelog
* Tue Dec 26 2023 madoka773 <valigarmanda55@gmail.com> - 6.4
- Initial package
