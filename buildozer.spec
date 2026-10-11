[app]
title = AGS
package.name = ags
package.domain = org.fanasina
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
