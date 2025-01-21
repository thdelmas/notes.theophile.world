---
author: ["Théophile Delmas"]
title: "Askatu zure Samsung Tabletaren Indarra: Urruneko Zerbitzari Sarbidea Ubuntu-n"
date: "2025-01-21"
description: "Digital nomadentzako urratsez urrats gida bat, Samsung tablet bat erabiliz Ubuntu-n exekutatzen den urruneko zerbitzari batera sarbidea lortzeko lanpostu wireless bat ezartzeko."
summary: "Ikasi nola bihurtu zure Samsung tablet bat urruneko lanpostu indartsu bat, Ubuntu zerbitzari batera konektatuz. Gida honek hardware beharrak, software ezarpena eta errendimendu eta segurtasun optimoarentzako praktika onenak aztertzen ditu."
tags: ["Samsung Tablet", "Ubuntu", "Urruneko Sarbidea", "Digital Nomad"]
categories: ["Teknologia", "Gidak"]
ShowToc: true
TocOpen: true
---

## Sarrera

Gaur egungo azkar joan den digital munduan, digital nomadek edozein lekutatik lan egiteko malgutasuna behar dute. Gida honek urratsez urrats tutorial bat eskaintzen du, Samsung tablet bat erabiliz Ubuntu-n exekutatzen den urruneko zerbitzari batera sarbidea lortzeko lanpostu wireless indartsu bat ezartzeko.

## Osagai Oinarrizkoak

### Beharrezko Hardwarea
- **Samsung Tablet:** Galaxy Tab S seriea, Android 11 edo berriro
- **Urruneko Zerbitzaria:** Mahaiko ordenagailu edo laptop bat, honako hauen ezaugarriak dituena:
  - 16GB RAM
  - Lau nukleoko prozesadorea
  - 256GB biltegiratze
  - Interneta konexio egonkorra (gutxienez 50Mbps igotze)

### Beharrezko Softwarea
- **Zerbitzari aldean:**
  - Ubuntu sistema eragilea
  - VNC zerbitzari softwarea (adibidez, TightVNC)
  - Dinamiko DNS zerbitzu kontua (etxeko internet erabiltzen bada)

- **Tablet aldean:**
  - VNC Viewer aplikazioa
  - OpenVPN bezeroa

## Ezarpen Prozesua

### Zerbitzari Prestaketa

#### Ubuntu Sistementzat:

1. **Instalatu VNC Zerbitzaria:**
   ```bash
   sudo apt update
   sudo apt install tightvncserver
   ```

2. **Sortu VNC Hasierako Script-a:**
   ```bash
   nano ~/vnc-startup.sh
   ```
   Gehitu hurrengo lerroak:
   ```bash
   #!/bin/bash
   vncserver :1 -geometry 1920x1080 -depth 24
   ```
   Egin script-a exekutagarria:
   ```bash
   chmod +x ~/vnc-startup.sh
   ```

3. **Ezarri Iragazki Ezarpenak:**
   ```bash
   vncserver -kill :1
   mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
   ```
   Sortu berri bat `~/.vnc/xstartup` fitxategi:
   ```bash
   nano ~/.vnc/xstartup
   ```
   Gehitu hurrengo edukia:
   ```bash
   #!/bin/bash
   xrdb $HOME/.Xresources
   startxfce4 &
   ```

### Sarea Konfiguratzea

1. **Dinamiko DNS Ezarri:**
   - Kontu bat sortu No-IP edo DynDNS bezalako zerbitzu batekin.
   - Instalatu dinamikoko DNS bezeroa zerbitzarian.
   - Konfiguratu domeinu izena (adibidez, myserver.ddns.net).

2. **Router Konfigurazioa:**
   - Sar zaitez router administrazio panelera (normalean 192.168.1.1).
   - Ezarri portu aurreratzeak:
     ```
     VNC: Kanpokoa 5900 → Barnekoa 5900
     ```

3. **Segurtasun Neurriak:**
   - Ezarri `fail2ban` indarrezko erasoak saihesteko.
   - Konfiguratu `ufw` (Sinple Firewall) arauak.
   - Aktibatu konexio logak.

### Tablet Konfigurazioa

1. **VNC Bezeroaren Ezarpena:**
   - Instalatu VNC Viewer aplikazioa Play Store-tik.
   - Sortu konexio profila:
     ```
     Helbidea: zure-ddns-domeinua.net:5900
     Irudi Kalitatea: Automatikoki
     Enkriptazioa: Aktibatu
     ```

2. **Errendimendu Optimizazioa:**
   - Aktibatu Garatzaile Aukerak:
     ```
     Ezarpenak → Tabletari buruz → Build zenbakia (bost aldiz ukitu)
     ```
   - Konfiguratu GPU irudikapena.
   - Egokitu animazio eskalak.
   - Aktibatu "Force 4x MSAA" testuaren argitasun hobea lortzeko.

## Eguneroko Eragiketa Praktika Onenak

1. **Zure Saioa Hastea:**
   - Konektatu lehenik VPN-ra.
   - Abiarazi VNC bezeroa.
   - Berretsi konexio segurtasun egoera.

2. **Eragiketan:**
   - Monitorizatu konexio kalitatea.
   - Erabili tabletaren energia aurrezteko ezaugarriak.
   - Egin segurtasun kontrolak maiz.

3. **Zure Saioa Amaitzea:**
   - Jarri martxan itzultze prozedura egokia.
   - Deskonectatu alderantzizko ordenan.
   - Berretsi zerbitzariaren egoera.

## Segurtasun Zerrenda

- [ ] Aldatu lehenetsitako pasahitzak.
- [ ] Aktibatu bi faktoreko autentifikazioa.
- [ ] Egin segurtasun azterketa maiz.
- [ ] Eguneratu software osagai guztiak.
- [ ] Monitorizatu sarbide logak.
- [ ] Konfiguratu automatikoko backup-ak.
- [ ] Proba egin hondamendien berreskurapen plana.

Ezarpen honek digital nomadentzako lanpostu mugikor indartsu bat eskaintzen du. Mantentze maiz eta segurtasun eguneratzeek funtzionamendu fidagarria bermatuko dute.