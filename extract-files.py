#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
    blob_fixup,
)

from extract_utils.fixups_lib import (
    lib_fixups_user_type,
    lib_fixup_remove_arch_suffix,
    lib_fixup_vendorcompat,
    libs_clang_rt_ubsan,
    libs_proto_3_9_1,
)

namespace_imports = [
    'device/xiaomi/sm8450-common',
    'hardware/qcom-caf/sm8450',
	'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/xiaomi/sm8450-common',
]

libs_remove = (
    'libagmclient',
    'libagmmixer',
    'vendor.qti.hardware.pal@1.0-impl',
)

def lib_fixup_remove(lib: str, *args, **kwargs):
    return ''

lib_fixups: lib_fixups_user_type = {
    libs_clang_rt_ubsan: lib_fixup_remove_arch_suffix,
    libs_proto_3_9_1: lib_fixup_vendorcompat,
    libs_remove: lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/etc/camera/zeus_enhance_motiontuning.xml',
        'vendor/etc/camera/zeus_motiontuning.xml'
    ): blob_fixup().regex_replace('xml=version', 'xml version'),
    (
        'vendor/etc/camera/pureShot_parameter.xml',
        'vendor/etc/camera/pureView_parameter.xml'
    ): blob_fixup().regex_replace(r'=([0-9]+)>', r'="\1">'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup().replace_needed(
        'vendor.qti.hardware.display.config-V2-ndk_platform.so',
        'vendor.qti.hardware.display.config-V2-ndk.so',
    ),
    'vendor/lib64/libkaraokepal.so': blob_fixup().replace_needed(
        'audio.primary.taro.so',
        'audio.primary.taro-zeus.so',
    ),
}


module = ExtractUtilsModule(
    'zeus',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

module.add_firmware_proprietary_file()

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()
