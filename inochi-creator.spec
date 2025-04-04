%define inochi_creator_ver 0.8.6
%define inochi_creator_semver 0.8.6
%define inochi_creator_dist 0
%define inochi_creator_commit 371e5f4e21117102dbecc82371bfd9a6e2f5df02
%define inochi_creator_short 371e5f4

%if 0%{inochi_creator_dist} > 0
%define inochi_creator_suffix ^%{inochi_creator_dist}.git%{inochi_creator_short}
%endif

Name:           inochi-creator
Version:        %{inochi_creator_ver}%{?inochi_creator_suffix:}
Release:        %autorelease
Summary:        Tool to create and edit Inochi2D puppets

# Bundled lib licenses

# Static dependencies licenses
##   bcaa licenses: BSL-1.0
##   bindbc-loader licenses: BSL-1.0
##   bindbc-sdl licenses: BSL-1.0
##   dcv licenses: BSL-1.0
##   ddbus licenses: MIT
##   dportals licenses: BSD-2-Clause
##   dunit licenses: MIT
##   dxml licenses: BSL-1.0
##   facetrack-d licenses: BSD-2-Clause
##   fghj licenses: BSL-1.0
##   i18n-d licenses: BSD-2-Clause
##   i2d-imgui licenses: BSL-1.0 and MIT
##   i2d-opengl licenses: BSL-1.0
##   imagefmt licenses: BSD-2-Clause
##   inmath licenses: BSD-2-Clause
##   inochi2d licenses: BSD-2-Clause
##   kra-d licenses: BSD-2-Clause
##   mir-algorithm licenses: Apache-2.0
##   mir-core licenses: Apache-2.0
##   mir-linux-kernel licenses: BSL-1.0
##   mir-random licenses: Apache-2.0
##   numem licenses: BSD-2-Clause
##   psd-d licenses: BSD-2-Clause
##   silly licenses: ISC
##   tinyfiledialogs licenses: Zlib
##   vmc-d licenses: BSD-2-Clause
License:        BSD-2-Clause and Apache-2.0 and BSL-1.0 and ISC and MIT and Zlib

URL:            https://github.com/grillo-delmal/inochi-creator-rpm

#https://github.com/Inochi2D/inochi-creator/archive/{inochi_creator_commit}/{name}-{inochi_creator_short}.tar.gz
Source0:        %{name}-%{version}-norestricted.tar.gz
Source1:        config.d
Source2:        icon.png

# Project maintained deps

Patch0:         inochi-creator_0_icon-fix.patch
Patch1:         inochi-creator_1_metadata-fix.patch
Patch2:         inochi-creator_2_f42fix.patch

# dlang
BuildRequires:  ldc
BuildRequires:  dub
BuildRequires:  jq

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  git

BuildRequires:  zdub-dub-settings-hack

BuildRequires:  zdub-bcaa-static
BuildRequires:  zdub-bindbc-loader-static
BuildRequires:  zdub-bindbc-sdl-static
BuildRequires:  zdub-dcv-static
BuildRequires:  zdub-ddbus-static
BuildRequires:  zdub-dportals-static
BuildRequires:  zdub-dunit-static
BuildRequires:  zdub-dxml-static
BuildRequires:  zdub-facetrack-d-static
BuildRequires:  zdub-fghj-static
BuildRequires:  zdub-i18n-d-static
BuildRequires:  zdub-i2d-imgui-static
BuildRequires:  zdub-i2d-opengl-static
BuildRequires:  zdub-imagefmt-static
BuildRequires:  zdub-inmath-static
BuildRequires:  zdub-inochi2d-static
BuildRequires:  zdub-kra-d-static
BuildRequires:  zdub-mir-algorithm-static
BuildRequires:  zdub-mir-core-static
BuildRequires:  zdub-mir-linux-kernel-static
BuildRequires:  zdub-mir-random-static
BuildRequires:  zdub-numem-static
BuildRequires:  zdub-psd-d-static
BuildRequires:  zdub-silly-static
BuildRequires:  zdub-tinyfiledialogs-static
BuildRequires:  zdub-vmc-d-static

#dportals reqs
BuildRequires:       dbus-devel

#i2d-imgui reqs
BuildRequires:       cmake
BuildRequires:       gcc
BuildRequires:       gcc-c++
BuildRequires:       freetype-devel
BuildRequires:       SDL2-devel

Requires:       hicolor-icon-theme

#dportals deps
Requires:       dbus

#i2d-imgui deps
Requires:       libstdc++
Requires:       freetype
Requires:       SDL2


%description
Inochi2D is a framework for realtime 2D puppet animation which can be used for VTubing, 
game development and digital animation. 
Inochi Creator is a tool that lets you create and edit Inochi2D puppets.
This is an unbranded build, unsupported by the official project.


%prep
%setup -n %{name}-%{inochi_creator_commit}

# FIX: Inochi creator version dependent on git
cat > source/creator/ver.d <<EOF
module creator.ver;

enum INC_VERSION = "%{inochi_creator_semver}";
EOF

# FIX: Replace config.d and banner.png
rm source/creator/config.d
cp %{SOURCE1} source/creator/
cp res/ui/grid.png res/ui/banner.png

# FIX: Add fake dependency
mkdir -p deps/vibe-d
cat > deps/vibe-d/dub.sdl <<EOF
name "vibe-d"
subpackage "http"
EOF
dub add-local deps/vibe-d "0.9.5"

%patch -P 0 -p1 -b .inochi-creator-icon-fix
%patch -P 1 -p1 -b .inochi-creator-metadata-fix
%patch -P 2 -p1 -b .inochi-creator-f42-fix
mkdir -p deps

# Project maintained deps

%build
export DFLAGS="%{_d_optflags}"
dub build \
    --cache=local \
    --config=barebones \
    --skip-registry=all \
    --non-interactive \
    --temp-build \
    --compiler=ldc2
mkdir ./out/
cp /tmp/.dub/build/inochi-creator*/barebones*/* ./out/


%install
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -p ./out/inochi-creator ${RPM_BUILD_ROOT}%{_bindir}/inochi-creator

install -d ${RPM_BUILD_ROOT}%{_datadir}/applications/
install -p -m 644 ./build-aux/linux/inochi-creator.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-creator.desktop
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/inochi-creator.desktop

install -d ${RPM_BUILD_ROOT}%{_metainfodir}/
install -p -m 644 ./build-aux/linux/inochi-creator.appdata.xml ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-creator.appdata.xml
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/inochi-creator.appdata.xml

install -d $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/inochi-creator.png

# Dependency licenses
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
%{_datadir}/icons/hicolor/256x256/apps/inochi-creator.png


%changelog
%autochangelog