---
author: ["Joy Doe"]
title: "How to Replace Android with /e/OS on an Old Tablet"
date: "2023-10-06"
description: "A step-by-step guide to installing /e/OS on an old Android tablet to breathe new life into your device."
summary: "Learn how to replace Android with /e/OS on an old tablet, enhancing your device's performance and privacy."
tags: ["Android", "e/OS", "Tablet", "Installation"]
categories: ["Technology", "Guides"]
ShowToc: true
TocOpen: true
---

# How to Replace Android with /e/OS on an Old Tablet

## Why?

Replacing the stock Android operating system on an old tablet with /e/OS can breathe new life into your device. /e/OS is a privacy-focused, open-source operating system that removes many of the privacy-invading features of standard Android. It also often runs more efficiently on older hardware, providing a smoother experience.

## How?

### Step 1: Check Device Compatibility

1. Visit the [/e/OS devices page](https://doc.e.foundation/devices) to see if your tablet is supported.
2. Note down the exact model of your tablet.

### Step 2: Backup Your Data

1. Connect your tablet to a computer.
2. Transfer all important files, photos, and documents to your computer or cloud storage.
3. Use a backup app like Titanium Backup to save app data if needed.

### Step 3: Unlock the Bootloader

1. Enable Developer Options:
   - Go to `Settings` > `About Tablet`.
   - Tap `Build Number` seven times to enable Developer Options.
2. Enable OEM Unlocking:
   - Go to `Settings` > `Developer Options`.
   - Toggle `OEM Unlocking` to enable it.
3. Unlock the Bootloader:
   - Turn off your tablet.
   - Boot into Fastboot mode by holding the `Volume Down` + `Power` buttons.
   - Connect the tablet to your computer.
   - Open a command prompt/terminal and type:
     ```sh
     fastboot oem unlock
     ```

### Step 4: Install a Custom Recovery

1. Download the appropriate TWRP (Team Win Recovery Project) image for your device from [TWRP's website](https://twrp.me/Devices/).
2. Boot your tablet into Fastboot mode again.
3. Flash TWRP:
   ```sh
   fastboot flash recovery path/to/twrp.img
   ```
4. Boot into TWRP recovery:
   - Turn off your tablet.
   - Hold the `Volume Up` + `Power` buttons.

### Step 5: Download /e/OS

1. Go to the [/e/OS download page](https://doc.e.foundation/devices).
2. Download the appropriate /e/OS ROM for your tablet model.
3. Transfer the downloaded ROM to your tablet.

### Step 6: Install /e/OS

1. Boot into TWRP recovery.
2. Wipe the current system:
   - Select `Wipe` > `Advanced Wipe`.
   - Check `Dalvik/ART Cache`, `System`, `Data`, and `Cache`.
   - Swipe to wipe.
3. Install the /e/OS ROM:
   - Go back to the main menu.
   - Select `Install`.
   - Navigate to the /e/OS ROM zip file and select it.
   - Swipe to confirm the installation.
4. Reboot your tablet:
   - Go back to the main menu.
   - Select `Reboot` > `System`.

## What?

### Outcomes and Benefits

- **Enhanced Privacy**: /e/OS is designed with privacy in mind, removing many tracking features found in standard Android.
- **Improved Performance**: /e/OS can be more efficient, leading to better performance on older hardware.
- **Extended Device Life**: Installing /e/OS can extend the useful life of your old tablet, reducing electronic waste.
- **Open Source**: /e/OS is open-source, giving you more control over your device and its software.

By following these steps, you can successfully replace Android with /e/OS on your old tablet, transforming it into a more private and efficient device. Enjoy the benefits of a refreshed tablet with a focus on privacy and performance!