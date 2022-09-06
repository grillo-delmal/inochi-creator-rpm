# Inochi Creator RPM

This repository contains the files necesary to generate a RPM package of a barebones version of Inochi Creator. 
It also includes a script to download the upstream package and strip it from the non redistributable files.

Packages generated using this files and scripts are not supported by the upstream Inochi2D project.

If you want to use this software on Fedora, you can use the COPR version from the following link

https://copr.fedorainfracloud.org/coprs/grillo-delmal/inochi2d/

## Building

If you want to build the RPM locally on Fedora you need the following tools

```git curl rpmdevtools fedpkg```

### Prepare the sources

First you need to download the sources, 

```sh
./generate-tarball.sh
spectool -g inochi-creator.spec
```

(this is basically what the `prepare.sh` script does)

### Build

```sh
fedpkg --release f36 --name inochi-creator mockbuild
```

## About the icon

The included icon is Copyright (c) 2022 [Grillo del Mal](https://twitter.com/grillo_delmal), [Anasu](https://twitter.com/ooanasuoo).

It is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). 

![license](https://i.creativecommons.org/l/by-sa/4.0/88x31.png "Creative Commons Attribution-ShareAlike 4.0 International License")