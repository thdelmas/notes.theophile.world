---
author: ["Théophile Delmas"]
title: "La configuració sense fils definitiva per a nòmades digitals: aprofitant el poder dels servidors amb una tauleta Samsung"
date: "2025-01-17"
description: "Descobreix com crear una configuració sense fils potent i portàtil utilitzant una tauleta Samsung i un servidor remot, perfecta per a nòmades digitals."
summary: "Aquest guia proporciona un procés pas a pas perquè els nòmades digitals puguin configurar un lloc de treball sense fils utilitzant una tauleta Samsung, un servidor remot i perifèrics Bluetooth, assegurant productivitat en moviment."
tags: ["Nòmades Digitals", "Treball Remot", "Tecnologia", "Productivitat"]
categories: ["Tecnologia", "Treball Remot"]
ShowToc: true
TocOpen: true
---
# La configuració sense fils definitiva per a nòmades digitals: aprofitant el poder dels servidors amb una tauleta Samsung

En el món digital actual, la capacitat de treballar des de qualsevol lloc és essencial per a molts professionals, especialment per als nòmades digitals. Aquesta guia proporciona un pas a pas detallat per crear una configuració sense fils potent utilitzant una tauleta Samsung per accedir a un servidor remot, millorat amb perifèrics Bluetooth.

## Components Bàsics

### Maquinari Requerit
- **Tauleta Samsung:** Qualsevol sèrie Galaxy Tab S (S7/S8/etc.) que funcioni amb Android 11 o posterior
- **Servidor Remot:** Un ordinador de sobretaula o portàtil amb almenys:
  - 16GB de RAM
  - Processador quad-core
  - 256GB d'emmagatzematge
  - Connexió a Internet estable (mínim 50Mbps d'upload)
- **Perifèrics Bluetooth:**
  - Teclat compatible amb Android
  - Ratolí amb Bluetooth 5.0 o posterior
  - Opcional: Suport portàtil per a tauleta

### Programari Requerit
- **Lloc del servidor:**
  - Windows Pro/Enterprise o distribució de Linux
  - Programari del servidor VNC (TightVNC, RealVNC o UltraVNC)
  - Compte de servei DNS dinàmic (si utilitzes Internet residencial)
- **Lloc de la tauleta:**
  - Aplicació VNC Viewer o Microsoft Remote Desktop
  - Client OpenVPN
  - Eines d'anàlisi de xarxa (opcional)

## Procés de Configuració Detallat

### 1. Preparació del Servidor

#### Per a Sistemes Windows:
1. **Habilitar l'escriptori remot:**
   ```
   Tauler de control → Sistema → Configuració remota → Permetre connexions remotes
   ```
   - Desmarcar "Permetre connexions només des de ordinadors que executen Escriptori Remot amb Autenticació de Nivell de Xarxa"
   - Afegir el teu compte de Microsoft o usuari local a la llista d'usuaris permesos

2. **Configurar el tallafoc de Windows:**
   ```
   Tauler de control → Tallafoc de Windows Defender → Configuració Avançada
   ```
   - Crear noves regles d'entrada per als ports 3389 (RDP) i 5900 (VNC)
   - Habilitar la gestió remota

3. **Instal·lar el servidor VNC:**
   - Descarregar i instal·lar TightVNC Server
   - Durant la instal·lació:
     - Establir contrasenyes primàries i de només visualització
     - Configurar el servei per iniciar-se amb Windows
     - Establir el port per defecte (5900)

#### Per a Sistemes Linux:
1. **Instal·lar el servidor VNC:**
   ```bash
   sudo apt update
   sudo apt install tightvncserver
   ```

2. **Crear un script d'inici VNC:**
   ```bash
   #!/bin/bash
   vncserver :1 -geometry 1920x1080 -depth 24
   ```
   Desa-ho com `~/vnc-startup.sh`
   
3. **Configurar les opcions de visualització:**
   ```bash
   vncserver -kill :1
   mv ~/.vnc/xstartup ~/.vnc/xstartup.bak
   ```
   Crea un nou `~/.vnc/xstartup`:
   ```bash
   #!/bin/bash
   xrdb $HOME/.Xresources
   startxfce4 &
   ```

### 2. Configuració de Xarxa

1. **Configurar DNS dinàmic:**
   - Crear un compte amb un servei com No-IP o DynDNS
   - Instal·lar el client de DNS dinàmic al servidor
   - Configurar el nom de domini (per exemple, myserver.ddns.net)

2. **Configuració del router:**
   - Accedir al panell d'administració del router (normalment 192.168.1.1)
   - Configurar el reencaminament de ports:
     ```
     RDP: Extern 3389 → Intern 3389
     VNC: Extern 5900 → Intern 5900
     ```
   - Habilitar UPnP per a mapeig automàtic de ports
   - Configurar QoS per prioritzar el trànsit d'accés remot

3. **Mesures de seguretat:**
   - Configurar fail2ban per prevenir atacs de força bruta
   - Configurar regles de UFW o del tallafoc de Windows
   - Habilitar el registre de connexions

### 3. Configuració de la Tauleta

1. **Configuració del client VNC:**
   - Instal·lar VNC Viewer des de la Play Store
   - Crear un perfil de connexió:
     ```
     Adreça: your-ddns-domain.net:5900
     Qualitat de la imatge: Automàtic
     Xifrat: Habilitar
     ```

2. **Integració de perifèrics Bluetooth:**
   ```
   Configuració → Dispositius connectats → Emparellar nou dispositiu
   ```
   - Habilitar el mode de descoberta Bluetooth als perifèrics
   - Per al teclat:
     - Provar la disposició del teclat
     - Configurar les opcions del teclat d'Android
     - Configurar accessos ràpids
   - Per al ratolí:
     - Ajustar la velocitat del punter
     - Configurar controls de gestos
     - Establir el comportament del clic dret

3. **Optimització del rendiment:**
   - Habilitar opcions de desenvolupador:
     ```
     Configuració → Quant a la tauleta → Número de compilació (tocar 7 vegades)
     ```
   - Configurar el renderitzat GPU
   - Ajustar les escales d'animació
   - Habilitar forçar 4x MSAA per a una millor claredat del text

## Guia de Solució de Problemes

### Problemes de Connexió
1. **No es pot connectar al servidor:**
   - Verificar que el servidor estigui en funcionament i accessible
   - Comprovar la configuració del reencaminament de ports
   - Provar la connexió localment primer
   - Utilitzar `netstat -an` per verificar els ports d'escolta

2. **Rendiment pobre:**
   - Comprovar l'ample de banda de la xarxa utilitzant speedtest
   - Monitoritzar l'ús de CPU/RAM del servidor
   - Ajustar les opcions de codificació de VNC:
     ```
     Codificació: ZRLE per a un bon equilibri
     Compressió: Nivell 6
     Qualitat: 8 per a un bon equilibri
     ```

3. **Desconnexions de Bluetooth:**
   - Netejar la memòria cau de Bluetooth
   - Actualitzar el firmware de la tauleta
   - Comprovar si hi ha interferències de dispositius USB 3.0
   - Mantenir els perifèrics dins dels 10 metres

## Millors Pràctiques per a l'Operació Diària

1. **Iniciant la teva sessió:**
   - Connectar-se al VPN primer
   - Llançar el client VNC/RDP
   - Verificar l'estat de seguretat de la connexió
   - Comprovar els nivells de bateria dels perifèrics

2. **Durant l'operació:**
   - Monitoritzar la qualitat de la connexió
   - Utilitzar les funcions d'estalvi d'energia de la tauleta
   - Realitzar verificacions de seguretat regulars
   - Mantenir un mètode de connexió de reserva

3. **Acabant la teva sessió:**
   - Procediment de tancament adequat
   - Desconnectar en ordre invers
   - Verificar l'estat del servidor
   - Registrar els detalls de la sessió si és necessari

## Llista de Comprovació de Seguretat

- [ ] Canviar les contrasenyes per defecte
- [ ] Habilitar l'autenticació de dos factors
- [ ] Auditories de seguretat regulars
- [ ] Actualitzar tots els components de programari
- [ ] Monitoritzar els registres d'accés
- [ ] Configurar còpies de seguretat automàtiques
- [ ] Provar el pla de recuperació davant de desastres

Aquesta configuració millorada proporciona una base robusta perquè els nòmades digitals puguin crear un lloc de treball mòbil potent. El manteniment regular i les actualitzacions de seguretat garantiran un funcionament fiable continuat.