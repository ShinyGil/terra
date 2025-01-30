%global debug_package %{nil}
%global git_name HeroicGamesLauncher
%define _build_id_links none

Name:          heroic-games-launcher
Version:       2.15.2
Release:       1%{?dist}
Summary:       A games launcher for GOG, Amazon, and Epic Games
License:       GPL-3.0-only AND MIT AND BSD-3-Clause
URL:           https://heroicgameslauncher.com
Source0:       https://github.com/Heroic-Games-Launcher/%{git_name}/archive/refs/tags/v%{version}.tar.gz
### Makes it actually sign the package, though will say it was skipped first.
Patch0:        afterPack.diff
BuildRequires: bsdtar
BuildRequires: libxcrypt-compat
### Electron builder builds some things with GCC(++) and Make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: nodejs
BuildRequires: pnpm
BuildRequires: python3
Requires:      alsa-lib
Requires:      gtk3
Requires:      hicolor-icon-theme
Requires:      nss
Requires:      python3
Requires:      which
Recommends:    gamemode
Recommends:    mangohud
Packager:      ShinyGil <rockgrub@disroot.org>

%description
Heroic is a Free and Open Source Epic, GOG, and Amazon Prime Games launcher for Linux, Windows, and macOS.

%prep
%autosetup -n %{git_name}-%{version} -p1

%build
pnpm install
pnpm run download-helper-binaries
### RPM doesn't work and it needs a package format to generate icons, AppImage isn't a good option for packaging because it will try to self update
pnpm dist:linux pacman

%install
mkdir -p %{buildroot}%{_datadir}/heroic
mv dist/linux-unpacked/* %{buildroot}%{_datadir}/heroic
mkdir -p %{buildroot}%{_bindir}
ln -sf %{_datadir}/heroic/heroic %{buildroot}%{_bindir}/%{name}
install -Dm644 public/icon.png %{buildroot}%{_datadir}/pixmaps/heroic.png
install -Dm644 dist/.icon-set/icon_16x16.png %{buildroot}%{_iconsdir}/hicolor/16x16/heroic.png
install -Dm644 dist/.icon-set/icon_32x32.png %{buildroot}%{_iconsdir}/hicolor/32x32/heroic.png
install -Dm644 dist/.icon-set/icon_48x48.png %{buildroot}%{_iconsdir}/hicolor/48x48/heroic.png
install -Dm644 dist/.icon-set/icon_64x64.png %{buildroot}%{_iconsdir}/hicolor/64x64/heroic.png
install -Dm644 dist/.icon-set/icon_128x128.png %{buildroot}%{_iconsdir}/hicolor/128x128/heroic.png
install -Dm644 dist/.icon-set/icon_256x256.png %{buildroot}%{_iconsdir}/hicolor/256x256/heroic.png
install -Dm644 dist/.icon-set/icon_512x512.png %{buildroot}%{_iconsdir}/hicolor/512x512/heroic.png
install -Dm644 dist/.icon-set/icon_1024.png %{buildroot}%{_iconsdir}/hicolor/1024x1024/heroic.png
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/heroic.desktop << EOF
[Desktop Entry]
Name=Heroic Games Launcher
Exec=%{_datadir}/heroic/heroic %U
Terminal=false
Type=Application
Icon=heroic
StartupWMClass=Heroic
Comment[de]=Ein Open source Spielelauncher for GOG, Amazon und Epic Games
Comment=Open source GOG, Amazon, and Epic Games launcher
MimeType=x-scheme-handler/heroic;
Categories=Game;
EOF

%files
%doc     README.md
%doc     CODE_OF_CONDUCT.md
%license COPYING
%_datadir/heroic
%_datadir/pixmaps/heroic.png
%_bindir/heroic-games-launcher
%_datadir/applications/heroic.desktop
%_iconsdir/hicolor/16x16/heroic.png
%_iconsdir/hicolor/32x32/heroic.png
%_iconsdir/hicolor/48x48/heroic.png
%_iconsdir/hicolor/64x64/heroic.png
%_iconsdir/hicolor/128x128/heroic.png
%_iconsdir/hicolor/256x256/heroic.png
%_iconsdir/hicolor/512x512/heroic.png
%_iconsdir/hicolor/1024x1024/heroic.png

%changelog
* Thu Jan 30 2025 ShinyGil <rockgrub@disroot.org>
- Initial package

