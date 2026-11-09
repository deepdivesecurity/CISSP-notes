# Kerberos

## Ticket Granting Ticket (TGT)
- Authentication server issues the TGT

## Ticket Granting Service (TGS)
- Receives TGT, validates it, & issues a service ticket to allow for accessing the resource

## Attacks
### Silver Ticket
- Target: TGS
- Doesn't touch KDC
- Provides service-level access

### Golden Ticket
- Target: TGT
- Forged TGT presented to KDC
- Provides full access