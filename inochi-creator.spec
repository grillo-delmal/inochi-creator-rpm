%define inochi_creator_ver 0.7.4.1
%define inochi_creator_semver 0.7.4.1
%define inochi_creator_dist 0
%define inochi_creator_commit f1bfc20122d1f912f400d0838c529e220718bfb2
%define inochi_creator_short f1bfc20

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