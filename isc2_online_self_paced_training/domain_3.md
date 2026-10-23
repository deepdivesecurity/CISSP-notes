# CISSP - Domain 3: Security Architecture & Engineering

## Key Management
- Kerchkhoff’s Principle - Everything must remain secure even if it’s public knowledge - only small secret remains private
- Key escrow: Storing keys with a trusted 3rd-party

## Fail Securely
- Fail open: Preserves availability of systems
- Fail closed: Preserves security of systems
- Clipping level: Locking accounts after a set number of failed attempts

## Encryption
FIPS 197 - Approved AES for use

## Certificate Authority
- 3rd-party who verifies identities of entities
    - Registration Authority performs this function
- Signs a certificate which it issues with its own private key
- Certificate includes the entity information + their public key
- Parties can then use the CA’s public key to verify validity of the certificate
- Validation authority validates that a certificate is still valid or revoked

## Number of Encryption Keys Necessary
- Calculate number of symmetrical keys needed: 
    - N(N-1)/2 where N is the number of users
- Calculate number of asymmetrical keys needed: 
    - N*2

## Kerberos
- KDC: Key Distribution Center
    - Issues session keys and authentication tickets to users & services
- Susceptible to brute force attacks due to encryption processes being mapped to passwords

## Hypervisors
- Type 1: Run directly on the hardware (more secure)
- Type 2: Run on host OS (less secure)

## Fog computing
- Hierarchal

## Attacks
- Side channel == Physical
- Fault analysis == Looks for error messages
- Probing == Watch cryptographic module
- Algebraic

## High Performance Computing (HPC)
- Do NOT use IDS or IPS; use proper architecture, logging, & monitoring instead

## Industrial Control Systems (ICS)
- Supervisory control & data acquisition (SCADA)
    - Interconnected geographically distributed processes
- Distributed control systems (DCS)
    - Confined to a local area
- Programmable logic controllers (PLC)
    - Specialized code device that can react in realtime

## Crime Prevention Through Environmental Design (CPTED)

## Handling Fires

### Fire Prevention
- Very early smoke detection apparatus (VESDA)
    - Aspirating sensors - uses air quality monitoring

### Fire Suppression
- Wet pipe
    - Water exists in pipes
    - Sprinkler head activates by heat
- Dry pipe
    - Pressurized gas in pipes
    - Sprinkler heads operate independently
- Pre-action
    - Fire sensors initiate charging of water pipes
    - Sprinkler heads operate independently
- Deluge
    - Similar to pre-action, but all sprinklers activate simultaneously
- Aqueous Firefighting Foam (AFFF)
- Non-conductive, nontoxic liquid suppressants
    - Novec 1230
- Gas systems
    - FM-200
    - Halon
        - Not commonly used
    - CO2
    - Aragonite
    - Inergen

## Security Models
### Brewer & Nash
- Users should not access confidential info of both a client and one or more of its competitors

### Biba
- Integrity focused
- Prevents users from modifying data at higher integrity levels or reading from lower ones
- Simple security property
    - Subject cannot read an object of lower integrity (no read down)
- Star property (* Property)
    - Subject cannot write an object of higher integrity (no write up)
- Invocation property
    - Subject with lower integrity level cannot request access to a higher integrity level object

### Clark-Wilson
- Improves on Biba
    - Transaction-level integrity
    - Separation of duties
- Establishes subject-program-object structure so subjects don’t have direct access to the object

### Bell-LaPadera
- Confidentiality focused
- Uses labels to keep track of clearances and classifications
- Simple security property
    - Subjects cannot read an object of higher security level (No read up)
- Star property (* Property)
    - Subjects can only write an object of the same or higher security level (No write down)
- Strong star
    - Subjects can only write to objects of the same level

### Graham-Denning
- 8 Basic rules
    - Create objects
    - Delete objects
    - Provision read access rights
    - Provision delete access rights
    - Provision transfer access rights
    - Provision grant access rights
    - Create subjects
    - Delete subjects

## Hashes
- Hash of Variable Length (HAVAL)
    - 3-5 rounds
    - 1024bit input blocks

### Cloud Computing
- ISO 17789 adds NaaS in addition to NIST pillars
