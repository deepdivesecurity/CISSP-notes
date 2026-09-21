# Data Security Notes

## Understanding Data Security
- Types of Data
    - Data at Rest: Data stored for later use on storage media
    - Data in Transit: Data being sent over a network between 2 systems
    - Data in Use: Data being actively used in a system's memory
- Data security controls: 
    - Policies and procedures
    - Encryption
    - Access controls
- Big Data: Use of datasets much larger than those handled by conventional data processing and analytic techniques

## Data Security Policies
- Data security policy criteria: 
    - Foundational authority for data security efforts
    - Clear expectations for data security responsibilities
    - Guidance for requesting access to info
    - Process for granting policy exceptions
- Data classification: Describes security levels
- Data storage policies should cover: 
    - Appropriate storage locations
    - Access control requirements
    - Encryption requirements
- Data transmission policies should cover: 
    - Appropriate data transmissions (What data)
    - Encryption requirements
    - Acceptable transmission mechanisms
- Data lifecycle policy: Describes end of life for data
- Data retention policy: How long to keep data
- Data disposal policy: Techniques for destroying data
- Physical destruction of data may use device shredders and degaussers

## Data Security Roles
- Data owner/controller: Business leaders with overall responsibility for data. They set policies and guidelines for data sets
- Data steward: Handle the day-to-day data governance activities. Delegated the responsibility from the data owner/data controller
- Data custodian: Stores and processes information and are often IT staff members
- Data user: Users who work with data in their jobs on daily basis (e.g. analyst)
- Data subjects: Referred to in collected data
- Data processors: 3rd party orgs or individuals who handle data on behalf of an org
- **EXAM**: GDPR uses the term data controller rather than data owner
- **EXAM**: System owner and data owner/controller are 2 difference concepts - the system owner is usually not the data owner/controller

## Limiting Data Collection
- Need to obtain new consent prior to collecting any new information
- Minimize information collected and delete unneeded information quickly
- Monitor third parties and verify their privacy practices

## Data Lifecycle
- Data lifecycle:
    1. Create: Org creates new data or collects data from sources
    2. Store: Data is moved to storage repo or storage system
    3. Use: Data is viewed or processed
    4. Share: Data is shared with employees, customers, and partners
    5. Archive: Data is moved from active storage to long-term storage repo
    6. Destroy: Data is securely destroyed
- Data sanitization techniques:
    1. Clearing: Overwrites sensitive info to frustrate casual analysis
    2. Purging: Uses more advanced techniques to frustrate lab analysis (e.g crypto functions to obscure data on disk; degaussing)
    3. Destroying: Completely obliterates the media through shredding, pulverization, melting, or burning
- NIST has a flowchart for selecting the appropriate sanitization technique
- Handling paper
    - Shredding
    - Pulping
    - Burning
- 3rd-party services for data destruction exist
- Stages of data lifecycle do not always follow the same order of the lifecycle