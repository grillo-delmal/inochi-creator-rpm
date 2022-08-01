%define inochi_creator_ver 0.7.3
%define inochi_creator_semver 0.7.3
%define inochi_creator_dist 0
%define inochi_creator_commit b6d0ab360729a7014cb764c18e7d32445a62dc87
%define inochi_creator_short b6d0ab3

# Project maintained deps
%define bindbc_imgui_semver 0.7.0+build.20.g237a209
%define bindbc_imgui_commit 237a209b0b35ec4766f4263b4d599fac59bd4dc1
%define bindbc_imgui_short 237a209

%define facetrack_d_semver 0.6.2+build.32.g9e1b2b1
%define facetrack_d_commit 9e1b2b1d8f968828c6bfd545287ad60fd48ab97c
%define facetrack_d_short 9e1b2b1

%define fghj_semver 1.0.0
%define fghj_commit 7d8b68001ebef41c78709e8dfa78fbf24e75bffd
%define fghj_short 7d8b680

%define gitver_semver 1.5.0
%define gitver_commit 8616ef003a324fb5067a5e5f9da665898f4fe922
%define gitver_short 8616ef0

%define i18n_d_semver 1.0.1+build.1.ge4a7f0b
%define i18n_d_commit e4a7f0bdee45b02cd5dba622046681a4cde20199
%define i18n_d_short e4a7f0b

%define inmath_semver 1.0.3+build.4.gec62993
%define inmath_commit ec629939647eac2d6e44003adee35fbaddba78e8
%define inmath_short ec62993

%define inochi2d_semver 0.7.2+build.17.g0e32b36
%define inochi2d_commit 0e32b364f07e704641033ef9243a9520825d42d0
%define inochi2d_short 0e32b36

%define psd_d_semver 0.6.2
%define psd_d_commit f12e0ad4bc54381a4a80fd5ec6249cdd91d0e990
%define psd_d_short f12e0ad

%define vmc_d_semver 1.1.1+build.4.gb32fb96
%define vmc_d_commit b32fb96b4ce9a6357b193fb297e44edd8e6112ed
%define vmc_d_short b32fb96

# Indirect deps
%define bindbc_loader_ver 1.0.1
%define bindbc_opengl_ver 1.0.2
%define bindbc_sdl_ver 1.1.3
%define imagefmt_ver 2.1.2
%define mir_algorithm_ver 3.14.11
%define mir_core_ver 1.1.109
%define semver_ver 0.3.4
%define silly_ver 1.1.1
%define tinyfiledialogs_ver 0.10.1

# cimgui
%define cimgui_commit 49bb5ce65f7d5eeab7861d8ffd5aa2a58ca8f08c
%define cimgui_short 49bb5ce
%define imgui_commit dd5b7c6847372016f45d5b5abda687bd5cd19224
%define imgui_short dd5b7c6


%if 0%{inochi_creator_dist} > 0
%define inochi_creator_suffix ^%{inochi_creator_dist}.git%{inochi_creator_short}
%endif

Name:           inochi-creator
Version:        %{inochi_creator_ver}%{?inochi_creator_suffix:}
Release:        %autorelease
Summary:        Tool to create and edit Inochi2D puppets

License:        BSD2 and MIT

URL:            https://github.com/Inochi2D/inochi-creator

#https://github.com/Inochi2D/inochi-creator/archive/{inochi_creator_commit}/{name}-{inochi_creator_short}.tar.gz
Source0:        %{name}-%{version}-norestricted.tar.gz
Source1:        inochi-creator.appdata.xml
Source2:        generate-tarball.sh
Source3:        README.md

# Project maintained deps
Source4:        https://github.com/Inochi2D/bindbc-imgui/archive/%{bindbc_imgui_commit}/bindbc-imgui-%{bindbc_imgui_short}.tar.gz
Source5:        https://github.com/Inochi2D/facetrack-d/archive/%{facetrack_d_commit}/facetrack-d-%{facetrack_d_short}.tar.gz
Source6:        https://github.com/Inochi2D/fghj/archive/%{fghj_commit}/fghj-%{fghj_short}.tar.gz
Source7:        https://github.com/Inochi2D/gitver/archive/%{gitver_commit}/gitver-%{gitver_short}.tar.gz
Source8:        https://github.com/KitsunebiGames/i18n/archive/%{i18n_d_commit}/i18n-%{i18n_d_short}.tar.gz
Source9:        https://github.com/Inochi2D/inmath/archive/%{inmath_commit}/inmath-%{inmath_short}.tar.gz
Source10:       https://github.com/Inochi2D/inochi2d/archive/%{inochi2d_commit}/inochi2d-%{inochi2d_short}.tar.gz
Source11:       https://github.com/Inochi2D/psd-d/archive/%{psd_d_commit}/psd-d-%{psd_d_short}.tar.gz
Source12:       https://github.com/Inochi2D/vmc-d/archive/%{vmc_d_commit}/vmc-%{vmc_d_short}.tar.gz

# Indirect deps
Source13:       https://github.com/BindBC/bindbc-loader/archive/refs/tags/v%{bindbc_loader_ver}/bindbc-loader-%{bindbc_loader_ver}.tar.gz
Source14:       https://github.com/BindBC/bindbc-opengl/archive/refs/tags/v%{bindbc_opengl_ver}/bindbc-opengl-%{bindbc_opengl_ver}.tar.gz
Source15:       https://github.com/BindBC/bindbc-sdl/archive/refs/tags/v%{bindbc_sdl_ver}/bindbc-sdl-%{bindbc_sdl_ver}.tar.gz
Source16:       https://github.com/tjhann/imagefmt/archive/refs/tags/v%{imagefmt_ver}/imagefmt-%{imagefmt_ver}.tar.gz
Source17:       https://github.com/libmir/mir-algorithm/archive/refs/tags/v%{mir_algorithm_ver}/mir-algorithm-%{mir_algorithm_ver}.tar.gz
Source18:       https://github.com/libmir/mir-core/archive/refs/tags/v%{mir_core_ver}/mir-core-%{mir_core_ver}.tar.gz
Source19:       https://github.com/dcarp/semver/archive/refs/tags/v%{semver_ver}/semver-%{semver_ver}.tar.gz
Source20:       https://gitlab.com/AntonMeep/silly/-/archive/v%{silly_ver}/silly-v%{silly_ver}.tar.gz
Source21:       https://github.com/dayllenger/tinyfiledialogs-d/archive/refs/tags/v%{tinyfiledialogs_ver}/tinyfiledialogs-d-%{tinyfiledialogs_ver}.tar.gz

# cimgui
Source22:       https://github.com/Inochi2D/cimgui/archive/%{cimgui_commit}/cimgui-%{cimgui_short}.tar.gz
Source23:       https://github.com/Inochi2D/imgui/archive/%{imgui_commit}/imgui-%{imgui_short}.tar.gz

# dlang
BuildRequires:  ldc
BuildRequires:  dub

# cimgui
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  SDL2-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git

Requires:       xprop

%description
Inochi2D is a framework for realtime 2D puppet animation which can be used for VTubing, 
game development and digital animation. 
Inochi Creator is a tool that lets you create and edit Inochi2D puppets.

%prep
%setup -n %{name}-%{inochi_creator_commit}

mkdir deps

# Project maintained deps
tar -xzf %{SOURCE4}
mv bindbc-imgui-%{bindbc_imgui_commit} deps/bindbc-imgui
dub add-local deps/bindbc-imgui/ "%{bindbc_imgui_semver}"

tar -xzf %{SOURCE5}
mv facetrack-d-%{facetrack_d_commit} deps/facetrack-d
dub add-local deps/facetrack-d/ "%{facetrack_d_semver}"

tar -xzf %{SOURCE6}
mv fghj-%{fghj_commit} deps/fghj
dub add-local deps/fghj/ "%{fghj_semver}"

tar -xzf %{SOURCE7}
mv gitver-%{gitver_commit} deps/gitver
dub add-local deps/gitver/ "%{gitver_semver}"

tar -xzf %{SOURCE8}
mv i18n-%{i18n_d_commit} deps/i18n
dub add-local deps/i18n/ "%{i18n_d_semver}"

tar -xzf %{SOURCE9}
mv inmath-%{inmath_commit} deps/inmath
dub add-local deps/inmath/ "%{inmath_semver}"

tar -xzf %{SOURCE10}
mv inochi2d-%{inochi2d_commit} deps/inochi2d
dub add-local deps/inochi2d/ "%{inochi2d_semver}"

tar -xzf %{SOURCE11}
mv psd-d-%{psd_d_commit} deps/psd-d
dub add-local deps/psd-d/ "%{psd_d_semver}"

tar -xzf %{SOURCE12}
mv vmc-d-%{vmc_d_commit} deps/vmc-d
dub add-local deps/vmc-d/ "%{vmc_d_semver}"

# Indirect Deps

tar -xzf %{SOURCE13}
mv bindbc-loader-%{bindbc_loader_ver} deps/bindbc-loader
dub add-local deps/bindbc-loader/ "%{bindbc_loader_ver}"

tar -xzf %{SOURCE14}
mv bindbc-opengl-%{bindbc_opengl_ver} deps/bindbc-opengl
dub add-local deps/bindbc-opengl/ "%{bindbc_opengl_ver}"

tar -xzf %{SOURCE15}
mv bindbc-sdl-%{bindbc_sdl_ver} deps/bindbc-sdl
dub add-local deps/bindbc-sdl/ "%{bindbc_sdl_ver}"

tar -xzf %{SOURCE16}
mv imagefmt-%{imagefmt_ver} deps/imagefmt
dub add-local deps/imagefmt/ "%{imagefmt_ver}"

tar -xzf %{SOURCE17}
mv mir-algorithm-%{mir_algorithm_ver} deps/mir-algorithm
dub add-local deps/mir-algorithm/ "%{mir_algorithm_ver}"

tar -xzf %{SOURCE18}
mv mir-core-%{mir_core_ver} deps/mir-core
dub add-local deps/mir-core/ "%{mir_core_ver}"

tar -xzf %{SOURCE19}
mv semver-%{semver_ver} deps/semver
dub add-local deps/semver/ "%{semver_ver}"

tar -xzf %{SOURCE20}
mv silly-v%{silly_ver} deps/silly
dub add-local deps/silly/ "%{silly_ver}"

tar -xzf %{SOURCE21}
mv tinyfiledialogs-d-%{tinyfiledialogs_ver} deps/tinyfiledialogs
dub add-local deps/tinyfiledialogs/ "%{tinyfiledialogs_ver}"

# cimgui

tar -xzf %{SOURCE22}
rm -r deps/bindbc-imgui/deps/cimgui
mv cimgui-%{cimgui_commit} deps/bindbc-imgui/deps/cimgui

tar -xzf %{SOURCE23}
rm -r deps/bindbc-imgui/deps/cimgui/imgui
mv imgui-%{imgui_commit} deps/bindbc-imgui/deps/cimgui/imgui

# FIX: Inochi creator version dependent on git
cat > source/creator/ver.d <<EOF
module creator.ver;

enum INC_VERSION = "%{inochi_creator_semver}";
EOF

# FIX: Inochi2D version dependent on git
cat > deps/inochi2d/source/inochi2d/ver.d <<EOF
module inochi2d.ver;

enum IN_VERSION = "%{inochi2d_semver}";
EOF

# FIX: make bindbc-imgui submodule checking only check cimgui
rm deps/bindbc-imgui/.gitmodules
cat > deps/bindbc-imgui/.gitmodules <<EOF
[submodule "deps/cimgui"]
	path = deps/cimgui
	url = https://github.com/Inochi2D/cimgui.git
EOF
mkdir deps/bindbc-imgui/deps/cimgui/.git


%build
export DFLAGS="%{_d_optflags}"
dub build --config=barebones --skip-registry=all --compiler=ldc2


%install
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -p ./out/inochi-creator ${RPM_BUILD_ROOT}%{_bindir}/inochi-creator

install -d ${RPM_BUILD_ROOT}%{_datadir}/applications/
install -p -m 644 res/inochi-creator.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-creator.desktop
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-creator.desktop

install -d ${RPM_BUILD_ROOT}%{_metainfodir}/
install -p -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-creator.appdata.xml
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-creator.appdata.xml

# Dependency licenses
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/cimgui/
install -p -m 644 ./deps/bindbc-imgui/deps/cimgui/LICENSE \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/cimgui/LICENSE
install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/imgui/
install -p -m 644 ./deps/bindbc-imgui/deps/cimgui/imgui/LICENSE.txt \
    ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/./deps/bindbc-imgui/imgui/LICENSE.txt

install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/deps/
find ./deps/ -mindepth 1 -maxdepth 1 -exec \
    install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/{} ';'

find ./deps/ -mindepth 2 -maxdepth 2 -iname '*LICENSE*' -exec \
    install -p -m 644 "{}" "${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/{}" ';'

install -d ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/res/
find ./res/ -mindepth 1 -maxdepth 1 -iname '*LICENSE*' -exec \
    install -p -m 644 {} ${RPM_BUILD_ROOT}%{_datadir}/licenses/%{name}/{} ';'


%files
%license LICENSE
%{_datadir}/licenses/%{name}/*
%{_bindir}/inochi-creator
%{_metainfodir}/inochi-creator.appdata.xml
%{_datadir}/applications/inochi-creator.desktop


%changelog
%autochangelog