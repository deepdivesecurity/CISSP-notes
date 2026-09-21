# Change & Configuration Management Notes

## Change Management
- Change management: Ensures that an org follows a standard process for requesting, reviewing, approving, and implementing changes to information systems
- Standard tool used for change management:
    - Request for Change (RFC) which includes:
        - Description of change
        - Expected impact
        - Risk assessment
        - Rollback plan
        - Identity of those involved
        - Proposed schedule
        - Affected configuration items
    - RFC must be approved by relevant authority (e.g. manager or CAB)
- Routine changes may be pre-approved to allow for immediate action

## Configuration & Asset Management
- Configuration Management: Tracks specific device settings
- Baselines: A snapshot of a system or app at a given point in time which can be used to assess if a system or app has changed outside of a given time
- Versioning and version control: Assigns numbers to each version (e.g. Version 1.0.10)
    - First number represents major version of the software
    - Second number represents the major update
    - Third number represents minor updates
- Standardize device configurations like:
    - Naming conventions
    - IP address schemes

## Physical Asset Management
- Asset management should follow a lifecycle approach
    1. User requests a new hardware device
    2. Receiving clerk who accepts hardware delivery updates the inventory and assigns the hardware to an IT staff member. During receiving process, someone should affix a permanent hardware asset tag to the device
    3. After configuring device to meet requriements, the IT staff member assigns it to the user and delivers it to them
    4. Device is either repurposed or discarded of in a secure way

## Supply Chain Risk & Mitigations
- End of Sale: Product will no longer be offered for purchase, but the vendor will support existing customers
- End of Support: The vendor will reduce or eliminate support for existing users of the product
- End of Life: The vendor will no longer provide any support or updates for the product
- Monitor vendor announcements for end of sale, end of support, and end of life products
- Vendors may not disclose the use of embedded systems in their products
- Watch for risks with shared responsibility (e.g. CSP data storage) whereby they may not be able to support you or your data in the future. Consider keeping secondary backups off of that vendor to mitigate the risk
- Types of providers for supply chain risks:
    - Hardware providers
    - Software providers (inc. client-based, agentless)
    - Managed service providers (MSP)
- Product tampering: Unauthz alteration of products
- Counterfeit products: Made without authz
- Implants: Unauthz hardware or software embedded in legitimate product
- How to address supply chain risks:
    - Silicon root of trust: Embeds security directly into the silicon. Ensures hardware boots with trusted firmware and software to reduce risk of unauthz modification
    - Physically unclonable functions: Unique unclonable digital fingerprints derived from physical variations inherent in each silicon chip
    - Software bill of materials (SBOM): Enhances transparency in software components. Detailed inventory of all software components used in a product
