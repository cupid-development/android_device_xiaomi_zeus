#
# Copyright (C) 2022-2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from xiaomi sm8450-common
$(call inherit-product, device/xiaomi/sm8450-common/common.mk)

# Inherit from the proprietary version
$(call inherit-product, vendor/xiaomi/zeus/zeus-vendor.mk)

# Overlay
PRODUCT_PACKAGES += \
    ApertureResZeus \
    FrameworksResZeus \
    LineageResZeus \
    NfcResZeus \
    SettingsProviderResZeus \
    SettingsResZeus \
    SystemUIResZeus \
    WifiResZeus

# Powershare
PRODUCT_PACKAGES += \
    vendor.lineage.powershare@1.0-service.default

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)
