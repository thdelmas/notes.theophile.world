---
author: ["Joy Doe"]
title: "Zerrendatu Androida /e/OS-rekin Tablet Zahar batean"
date: "2023-10-06"
description: "Gida pauso-hurrenkera bat zaharreko Android tablet batean /e/OS instalatzen, zure gailuari bizi berri bat emateko."
summary: "Ikasi nola Androida /e/OS-rekin ordezkatu zaharreko tablet batean, gailuaren jarduerak eta pribatutasuna hobetzen."
tags: ["Android", "/e/OS", "Tableta", "Instalazioa"]
categories: ["Teknologia", "Gidaak"]
series: ["Datuak Aske Mantentzeko"]
ShowToc: true
TocOpen: true
---

# Zerrendatu Androida /e/OS-rekin Tablet Zahar batean

## Zergatik?

Zaharreko tablet batean stock Android sistema eragilea /e/OS-rekin ordezkatzeak bizi berri bat sartu dezake zure gailuan. /e/OS pribatutasunari bideratutako, iturburu-ireki sistema eragilea da, standard Android-en pribatutasun-eraso asko kenduz. Gainera, askotan zahar hardwarean eraginkorrago jartzen da, esperientzia lausoa eskaintzen duela.

## Nola?

### 1. Pausu: Egiaztatu Gailuaren Konpatibilitatea

1. Bisitatu [/e/OS gailu orrialdea](https://doc.e.foundation/devices) zure tabletak onartzen duen ikusteko.
2. Ohartu zure tabletaren eredu zehatzaren inguruan.

### 2. Pausu: Segurtasun Kopiatu Zure Datuak

1. Konektatu zure tabletak ordenagailu batera.
2. Transferitu zure datu garrantzitsu guztiak, argazkiak eta agiriak zure ordenagailura edo cloud biltegira.
3. Erabili Titanium Backup aplikazio bat datuak gordetzeko beharrezkoa bada.

### 3. Pausu: Ireki Bootloader-a

1. Gaitu Garatzaile Aukerak:
   - Joan `Ezarpenak` > `Tabletari buruz`.
   - Sakatu `Eraiki Zenbakia` garatzaile aukerak gaitzeko zazpi aldiz.
2. Gaitu OEM Unlocking:
   - Joan `Ezarpenak` > `Garatzaile Aukerak`.
   - Aktibatu `OEM Unlocking` gaitzeko.
3. Ireki Bootloader-a:
   - Itzali zure tabletak.
   - Botatzea Fastboot modura `Bolumen Behera` + `Boton Potentzia` sakatuz.
   - Konektatu tablet ordenagailura.
   - Ireki komando-aurpegia/terminala eta idatzi:
     ```sh
     fastboot oem unlock
     ```

### 4. Pausu: Instalatu Erreserba Pertsonalizatua

1. Deskargatu TWRP (Team Win Recovery Project) irudia zure gailurako egokiena [TWRP-ren webgunean](https://twrp.me/Devices/).
2. Botatu zure tabletak berriro Fastboot modura.
3. Flash TWRP:
   ```sh
   fastboot flash recovery path/to/twrp.img
   ```
4. Bootatu TWRP erreserba:
   - Itzali zure tabletak.
   - Mantendu `Bolumen Goruntz` + `Boton Potentzia`.

### 5. Pausu: Deskargatu /e/OS

1. Joan [/e/OS deskarga orrialdera](https://doc.e.foundation/devices).
2. Deskargatu /e/OS ROM egokiena zure tablet eredurako.
3. Transferitu deskargatutako ROM zure tabletara.

### 6. Pausu: Instalatu /e/OS

1. Bootatu TWRP erreserba.
2. Garbitu oraingo sistema:
   - Hautatu `Garbitu` > `Garapen Garbia`.
   - Egiaztatu `Dalvik/ART Cache`, `Sistema`, `Datuak`, eta `Cache`.
   - Mantendu garbitzeko.
3. Instalatu /e/OS ROM-a:
   - Itzuli atzera menura.
   - Hautatu `Instalatu`.
   - Nabigatu /e/OS ROM zip fitxategira eta hautatu.
   - Mantendu instalazioa berretzeko.
4. Bootatu berri tabletak:
   - Itzuli atzera menura.
   - Hautatu `Berriro Botatzeko` > `Sistema`.

## Zer?

### Emaitzak eta Ondorioak

- **Pribatutasun Hobetua**: /e/OS pribatutasuna kontuan hartuta diseinatua da, standard Android-en jarraipen-eredu asko kenduz.
- **Jarduerak Hobetuta**: /e/OS eraginkorragoa izan daiteke, zahar hardwarean hobekuntza eraginkorragoa eragingarri delako.
- **Gailuaren Bizi Luzatua**: /e/OS instalatzeak zure zahar tabletaren bizi erabilgarria luzatzea lortu dezake, elektronika-ondarea gutxituz.
- **Iturburu Irekia**: /e/OS iturburu-irekia da, gailuaren eta bere softwarearen gainean kontrol gehiago ematen dizuena.

Pausu hauek jarraituz, zure zaharreko tabletan Androida /e/OS-rekin ordezkatzea lortu dezakezu, gailua pribatutasun eta eraginkortasunaren arretaz berrituz. Gozatu tablet freskatua izateko onurak, pribatutasun eta jardueraren arretaz!