# CISSP - Domain 4: Communication & Network Security

## OSI Model
- Application
- Presentation
- Session
- Transport: TCP, UDP
- Network: Router
- Data link
- Physical: Physical devices

## TCP/IP Model
- Application layer (Application + Presentation + Session)
- Host-to-Host transport layer (Network + transport)
- Internet layer (Data link + network)
- Network interface layer (physical + data link)

## VoIP
- Session Initiation Protocol (SIP)
    - Enables any SIP compatible device to communicate with any other SIP system

## Zero Trust
- NIST SP 800-207

## Network Function Virtualization (NFV)
- Meant to decouple functions like firewall management, IDS, NAT, away from hardware and into software
- CapEx to OpEx
- Service consumption agility
- Reduction in wait time

## 802.1X NAC
- Port-based network access control (PNAC)
- Provides authn for devices connecting to both LAN or WLAN
- Authenticator == Switch or access point
- Can perform device scanning for current security settings & enforcement

## Digital Subscriber Line (DSL)
- Asymmetric DSL (ADSL)
    - Downstream > upstream
- Rate-adaptive DSL (RADSL)
    - Upstream tuned automatically
- Symmetric DSL (SDSL)
    - Downstream == Upstream rates
- Very high bit rate DSL (VDSL)
    - Higher transmission rates than other DSLs

## Cellular Networks
- Code-Division Multiple Access (CDMA)
    - Uses network-based allow list to verify subscribers
    - All calls are assigned a unique code
    - Call data is encoded and calls are transmitted immediately
- Global System for Mobiles (GSM)
    - Each call assigned specific channel and time slot

## Proxies
- Circuit-Level proxy
    - Does not inspect data that it forwards
    - Can forward any traffic to any TCP or UDP port
- Application-Level proxy
    - Create processing overhead, but can inspect data for attacks

## Tunneling
- Point-to-Point Tunnelling Protocol (PPTP)
    - Uses generic routing encapsulation (GRE)
    - Based on point-to-point protocol (PPP)
    - Offers authn through:
        - password authentication protocol (PAP)
        - challenge-handshake authentication protocol (CHAP)
        - extensible authentication protocol (EAP)
- Layer 2 Tunnelling Protocol (L2TP)
    - Does not provide encryption - relies on IPSec to provide it
    - Based on PPP, so offers the same authn above
        - IPSec can also provide authn
- VPN using TLS
    - Relies on PKI
    - Easier to deploy than IPSec

## Kill Chain Operational Phases
1. Reconnaissance
2. Weaponization
    1. Select access technique
3. Delivery
4. Exploitation
5. Installation
    1. Install backdoors
6. Command and Control
7. Actions on Objective
    1. Exfiltration, etc.

## Cabling
- Twisted pair
    - Unshielded twisted pair (UTP)
    - Shielded twisted pair (STP)
- Coax
- Fiber
    - Single mode
        - Longest transmission distances
    - Multimode
        - Mid distance
    - Plastic optical fibre (POF)
        - Shortest distance
