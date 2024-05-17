---
author: ["Joy Doe"]
title: "Com substituir Android per /e/OS en una tauleta antiga"
date: "2023-10-06"
description: "Una guia pas a pas per instal·lar /e/OS en una tauleta antiga amb Android per donar-li una nova vida al teu dispositiu."
summary: "Aprèn com substituir Android per /e/OS en una tauleta antiga, millorant el rendiment i la privacitat del teu dispositiu."
tags: ["Android", "/e/OS", "Tauleta", "Instal·lació"]
categories: ["Tecnologia", "Guies"]
series: ["Mantingues-te sense dades"]
ShowToc: true
TocOpen: true
---

# Com substituir Android per /e/OS en una tauleta antiga

## Per què?

Substituir el sistema operatiu Android estàndard en una tauleta antiga per /e/OS pot donar una nova vida al teu dispositiu. /e/OS és un sistema operatiu de codi obert centrat en la privacitat que elimina moltes de les funcionalitats invasives de la privacitat de l'Android estàndard. Sovint, també funciona de manera més eficient en maquinari antic, oferint una experiència més fluïda.

## Com?

### Pas 1: Comprova la Compatibilitat del Dispositiu

1. Visita la pàgina de dispositius de [/e/OS](https://doc.e.foundation/devices) per veure si la teva tauleta és compatible.
2. Apunta el model exacte de la teva tauleta.

### Pas 2: Fes una còpia de seguretat de les teves dades

1. Connecta la teva tauleta a un ordinador.
2. Transfereix tots els fitxers, fotos i documents importants al teu ordinador o emmagatzematge en línia.
3. Utilitza una aplicació de còpia de seguretat com Titanium Backup per desar dades d'aplicacions si és necessari.

### Pas 3: Desbloqueja el Bootloader

1. Activa les Opcions de desenvolupador:
   - Vés a `Configuració` > `Sobre la tauleta`.
   - Toca set vegades `Número de compilació` per activar les Opcions de desenvolupador.
2. Activa l'Alliberament OEM:
   - Vés a `Configuració` > `Opcions de desenvolupador`.
   - Habilita `Alliberament OEM`.
3. Desbloqueja el Bootloader:
   - Apaga la tauleta.
   - Inicia en el mode Fastboot mantenint premuts els botons `Volum avall` + `Encendre`.
   - Connecta la tauleta al teu ordinador.
   - Obre una finestra d'ordres/terminal i escriu:
     ```sh
     fastboot oem unlock
     ```

### Pas 4: Instal·la una Recuperació Personalitzada

1. Descarrega la imatge TWRP (Team Win Recovery Project) adequada per al teu dispositiu des de la [pàgina web de TWRP](https://twrp.me/Devices/).
2. Inicia la tauleta en el mode Fastboot de nou.
3. Flasheja TWRP:
   ```sh
   fastboot flash recovery ruta/fins/a/twrp.img
   ```
4. Inicia en la recuperació de TWRP:
   - Apaga la tauleta.
   - Mantén premuts els botons `Volum amunt` + `Encendre`.

### Pas 5: Descarrega /e/OS

1. Vés a la [pàgina de descàrregues de /e/OS](https://doc.e.foundation/devices).
2. Descarrega el ROM de /e/OS adequat per al model de la teva tauleta.
3. Transfereix el ROM descarregat a la teva tauleta.

### Pas 6: Instal·la /e/OS

1. Inicia en la recuperació de TWRP.
2. Esborra el sistema actual:
   - Selecciona `Wipe` > `Wipe avançat`.
   - Marca `Cache Dalvik/ART`, `Sistema`, `Dades` i `Cache`.
   - Desliza per esborrar.
3. Instal·la el ROM de /e/OS:
   - Torna al menú principal.
   - Selecciona `Instal·la`.
   - Navega fins al fitxer zip del ROM de /e/OS i selecciona'l.
   - Desliza per confirmar la instal·lació.
4. Reinicia la tauleta:
   - Torna al menú principal.
   - Selecciona `Reinicia` > `Sistema`.

## Què?

### Resultats i Beneficis

- **Privacitat Millorada**: /e/OS està dissenyat amb la privacitat en ment, eliminant moltes funcionalitats de seguiment trobades en l'Android estàndard.
- **Rendiment Millorat**: /e/OS pot ser més eficient, oferint un millor rendiment en maquinari antic.
- **Vida Útil Estesa del Dispositiu**: Instal·lar /e/OS pot allargar la vida útil útil de la teva tauleta antiga, reduint els residus electrònics.
- **Codi Obert**: /e/OS és de codi obert, donant-te més control sobre el teu dispositiu i el seu programari.

Seguint aquests passos, podràs substituir amb èxit Android per /e/OS en la teva tauleta antiga, convertint-la en un dispositiu més privat i eficient. Gaudeix dels avantatges d'una tauleta renovada amb un enfocament en la privacitat i el rendiment!