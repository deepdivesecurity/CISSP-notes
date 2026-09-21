# Data Security Controls Notes

## Developing Security Baselines
- Baseline security standard elements:
    - Administered by named individual
    - Protected against unauthz access
    - Doesn't jeopardize other systems or data
    - Remains under positive control
    - Complies with data security requirements
- Baselines are generic on purpose They may include specific requirements for handling different categories of info
- Specific security standards for:
    - OS
    - Mobile devices
    - Network infra components
    - Appliances
- System configuration managers automate policy deployment

## Leveraging Industry Standards
- Sources of Security Standards
    - Vendors (e.g. Microsoft Security Compliance Toolkit)
    - Government agencies (e.g. NIST)
    - Independent orgs (e.g. CIS)

## Customizing Security Standards
- Orgs should document the rationale for any deviations from the 3rd-party standard they use/modify

## Cloud Storage Security
- Apply the same security controls in the cloud that you would in your own DC
- Cloud storage security:
    - Encryption
    - Access control
- Encryption keys must be protected for cloud storage.
    - This could involve using a CMEK with a cloud-based HSM to protect the key, even from the CSP

## Information Classification
- Data classification policy: Assigns info into categories, known as classifications, which determine storage, handling, and access requirements
- Assign classifications based on:
    1. Sensitivity of info
    2. Criticality of info
- Labeling requirement: Ensures users can recognize and handle sensitive info appropriately
    - Can be applied to info as well as assets

## Digital Rights Management
- Information rights management (IRM) attempt to achieve 3 objectives:
    1. Enforcing data rights to keep information out of unauthz hands
    2. Provisioning access to employees, partners, or other authz users
    3. Implementing access control models that enforce access control models appropriately across systems
- Digital rights management (DRM): Provides the owners of IP with the technical means to prevent the unauthz use of their content through the use of encryption technology
- Business applications of DRM include:
    - Protect trade secrets and other IP
    - Limit redistribution of info
    - Revoke access after expiration date to data

## Data Loss Prevention
- DLP: Technology that searches systems and monitors networks for sensitive info that is unsecured and provide the ability to remove the info, block the transmission, or encrypt the stored data
- Types of DLP:
    - Host-based DLP: Uses software agents installed on a single system
    - Network-based DLP: Scans network transmissions for sensitive information
- DLP solutions can:
    - Pattern match: Recognize known patterns of sensitive info (e.g. social security numbers)
    - Watermarking: Identifies sensitive information using electronic tags
