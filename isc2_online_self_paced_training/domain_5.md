# CISSP - Domain 5: Identity & Access Management

## Access Control Models
- Non-RBAC
    - Users mapped to individual apps
- Limited RBAC
    - Users mapped to app, then to roles
- Hybrid RBAC
    - Users mapped to multi-app roles
- Full RBAC
    - Users mapped to enterprise roles
- Discretionary Access Control (DAC)
- Non-discretionary Access Control (NDAC)
- Mandatory Access Control (MAC)

## Federated Identity Management
- Provides identification, authn, and authz through
    - SAML
        - 3 Roles in SAML
            - User
            - Service Provider
            - SAML Identity Provider
            - Assertion is sent from SAML identity provider to the service provider at time of request from user
    - OAuth

## JIT Access
- Usually implemented through SAML
- Usually used during SSO

## Federal Identity, Credential, and Asset Management (FICAM)
- Related to NIST SP 800-63

## Types of Controls
- Administrative
- Physical
- Technical (Logical)

## Kerberos
- KDC == Key distribution centre
    - Central authority that verifies and issues tickets via 2 services
        - TGS == Ticket granting server
        - AS == Authentication server
    - During authentication requests, grants a ticket granting ticket (TGT) which serves as proof of authentication
    - The TGT is then sent to the TGS to receive a service ticket which can be used to authn to the app

## Identity Stores
- Kerberos

## OpenID Connect & OAuth
- OpenID Connect works for both websites and mobile apps
- OIDC serves as authn layer on top of OAuth which is for author
- ID token from OpenID Connect Provider (OP) contains claims about the subject and the timing (issue time + expiration time)

## Digital Identity Guidelines
- NIST SP 800-63-3
- Identity Assurance Levels
    - IAL1
        - Self-asserted
    - IAL2
        - Attributes verified in person or remotely accepted
    - IAL3
        - In person identity proofing required
        - Attributes verified by credential service provider (CSP) through examining physical documents
- Authenticator Assurance Level (AAL)
    - Refers to authentication process
- Federation Assurance Level (FAL)
    - Refers to strength of assertion in federated environment
