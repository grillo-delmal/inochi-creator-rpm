#!/bin/sh

set -e
set -x

TAGVER="$(sed -n 's/%define inochi_creator_ver\s*//p' *.spec)"
DIST="$(sed -n 's/%define inochi_creator_dist\s*//p' *.spec)"
COMMIT="$(sed -n 's/%define inochi_creator_commit\s*//p' *.spec)"
SHORT="$(sed -n 's/%define inochi_creator_short\s*//p' *.spec)"
VERSION=${TAGVER}$([ ${DIST} -gt 0 ] && echo "^${DIST}.git${SHORT}" || echo "")

# Retrieve and set version
curl -L https://github.com/Inochi2D/inochi-creator/archive/${COMMIT}/inochi-creator-${SHORT}.tar.gz --output inochi-creator-${SHORT}.tar.gz
tar -xzf inochi-creator-${SHORT}.tar.gz

pushd inochi-creator-${COMMIT}

# Remove branding assets
rm -rf res/Inochi-Creator.iconset/
find res/ui/ -type f -not -name "grid.png" -delete
rm res/icon.png
rm res/logo.png
rm res/logo_256.png
rm res/shaders/ada.frag
rm res/shaders/ada.vert
cp res/ui/grid.png res/ui/banner.png

popd

tar -czf inochi-creator-$VERSION-norestricted.tar.gz inochi-creator-${COMMIT}
rm -rf inochi-creator-${COMMIT}
rm -rf inochi-creator-${SHORT}.tar.gz

