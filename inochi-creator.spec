%define inochi_creator_ver 0.7.4.1
%define inochi_creator_semver 0.7.4.1
%define inochi_creator_dist 0
%define inochi_creator_commit f1bfc20122d1f912f400d0838c529e220718bfb2
%define inochi_creator_short f1bfc20

# Project maintained deps
%define bindbc_imgui_semver 0.7.0+build.22.gb3d6e32
%define bindbc_imgui_commit b3d6e32cb0ce7c607a8e249a11c4a5a4ed0a19e8
%define bindbc_imgui_short b3d6e32

%define facetrack_d_semver 0.6.2+build.57.g3dc8ed7
%define facetrack_d_commit 3dc8ed78ca987ba69b79cba393f281796de62acf
%define facetrack_d_short 3dc8ed7

%define fghj_semver 1.0.1
%define fghj_commit 2df8f8af58421da760190e3f8ddf1dcee546c796
%define fghj_short 2df8f8a

%define i18n_d_semver 1.0.1+build.2.g75c57ea
%define i18n_d_commit 75c57ea0889d459b73765d932aec02f9b3e71b80
%define i18n_d_short 75c57ea

%define inmath_semver 1.0.3+build.4.gec62993
%define inmath_commit ec629939647eac2d6e44003adee35fbaddba78e8
%define inmath_short ec62993

%define inochi2d_semver 0.7.2+build.62.g08fe198
%define inochi2d_commit 08fe19825b0db01c0a7831711722e5c9660d74ad
%define inochi2d_short 08fe198

%define psd_d_semver 0.6.2
%define psd_d_commit f12e0ad4bc54381a4a80fd5ec6249cdd91d0e990
%define psd_d_short f12e0ad

%define vmc_d_semver 1.1.2
%define vmc_d_commit b32fb96b4ce9a6357b193fb297e44edd8e6112ed
%define vmc_d_short b32fb96

# Indirect deps
%define bindbc_loader_ver 1.0.1
%define bindbc_opengl_ver 1.0.2
%define bindbc_sdl_ver 1.1.3
%define ddbus_ver 3.0.0-beta.2
%define dunit_ver 1.0.16
%define imagefmt_ver 2.1.2
%define mir_algorithm_ver 3.16.5
%define mir_core_ver 1.3.9
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

License:        BSD-2-Clause and MIT

URL:            https://github.com/grillo-delmal/inochi-creator-rpm

#https://github.com/Inochi2D/inochi-creator/archive/{inochi_creator_commit}/{name}-{inochi_creator_short}.tar.gz
Source0:        %{name}-%{version}-norestricted.tar.gz
Source1:        inochi-creator.appdata.xml
Source2:        icon.png
Source3:        config.d
Source4:        banner.png
Source5:        generate-tarball.sh
Source6:        README.md

Patch0:         inochi-creator_0.7.3_icon-fix.patch
Patch1:         inochi-creator_0.7.3_no-gitver.patch


# dlang
BuildRequires:  ldc
BuildRequires:  dub

# cimgui
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  SDL2-devel
BuildRequires:  dbus-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git

BuildRequires:  zdub-inochi2d-static
BuildRequires:  zdub-dportals-static
BuildRequires:  zdub-tinyfiledialogs-static
BuildRequires:  zdub-facetrack-d-static
BuildRequires:  zdub-bindbc-sdl-static
BuildRequires:  zdub-bindbc-imgui-static
BuildRequires:  zdub-i18n-d-static
BuildRequires:  zdub-inmath-static
BuildRequires:  zdub-psd-d-static

BuildRequires:  setgittag

Requires:       hicolor-icon-theme


%description
Inochi2D is a framework for realtime 2D puppet animation which can be used for VTubing, 
game development and digital animation. 
Inochi Creator is a tool that lets you create and edit Inochi2D puppets.
This is an unbranded build, unsupported by the official project.

%prep
%setup -n %{name}-%{inochi_creator_commit}

%patch0 -p1 -b .icon-fix
%patch1 -p1 -b .no-gitver-a

# FIX: Inochi creator version dependent on git
cat > source/creator/ver.d <<EOF
module creator.ver;

enum INC_VERSION = "%{inochi_creator_semver}";
EOF

# FIX: Replace config.d and banner.png
rm source/creator/config.d
cp %{SOURCE3} source/creator/
cp %{SOURCE4} res/ui/banner.png

#HACK because dub can't actually deal with installed libraries
mkdir -p /builddir/.dub/
cp -r /usr/include/zdub /builddir/.dub/packages

pushd deps; pushd bindbc-imgui

enum INC_VERSION = "%{inochi_creator_semver}";
EOF

# FIX: Replace config.d and banner.png
rm source/creator/config.d
cp %{SOURCE3} source/creator/
cp %{SOURCE4} res/ui/banner.png


%build
export DFLAGS="%{_d_optflags}"
dub build \
    --cache=local \
    --config=barebones \
    --skip-registry=all \
    --compiler=ldc2


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

install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/inochi-creator.png


%files
%license LICENSE
%{_bindir}/inochi-creator
%{_metainfodir}/inochi-creator.appdata.xml
%{_datadir}/applications/inochi-creator.desktop
%{_datadir}/icons/hicolor/256x256/apps/inochi-creator.png


%changelog
%autochangelog