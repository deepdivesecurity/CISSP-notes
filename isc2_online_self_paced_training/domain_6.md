# CISSP - Domain 6: Security Assessment & Testing

## Internal Assessments
- 4 steps: 
    - Chartering
        - Executive buy-in
        - Stakeholder management plan to identify stakeholder and communications about assessment
    - Testing
    - Reporting
        - Disclosure of results is a management responsibility
    - Remediating
        - Plan of Action & Milestones (POA&M)
            - Described further in NIST SP 800-37 on Risk Management Framework (RMF)
            - Blueprint for addressing security deficiencies & vulnerabilities

## Compliance & Substantive Tests
- Compliance test: Determine whether a control exists and functions as intended
    - Quicker to perform
- Substantive test: Go further by validating the processes themselves
    - Offers stronger assurances
    - Takes longer

## Log Reviews
- ISO 27001
- NIST SP 800-92
    - Log reviews are a component of log management
- Regulations requiring log review: 
    - Gramm-Leach-Bliley Act (GLBA)
        - Requires financial institutions to protect customer info, log review can be used
    - Sarbanes-Oxley Act (SOX)
        - Regulates accurate financial and accounting practices
    - HIPAA
    - PCI DSS

## Supply Chain Risk Management
- ISO 28000 series

## NIST Risk Management Framework (RMF)
- NIST SP 800-37
- Used for audits & control assessments
- NIST SP 800-53 & NIST SP 800-171 provide further implementation details

## Audit Terminology
- Criteria: Standard used to measure the activity or performance
- Condition: Statement describing audit’s result
- Cause: Explanation of why a problem occurred
- Effect: Highlights differences between and significance of the condition to the criteria

## Plan-Do-Check-Act (PDCA)
- Improvement model following 4 phases: 
    - Plan
    - Do
    - Check
    - Act
        - Identify root cause of error, reevaluate risk, and determine new baseline

## Sig Sigma
- 5 phase approach
    - Define
    - Measure
    - Analyze
    - Improve
    - Control

## Business Continuity (BC) & Disaster Recovery (DR)
- NIST SP 800-34: Contingency Planning Guide for Federal Information Systems
- ISO 27301: Business Continuity Information Systems
- ISO 22301: Business Continuity Management Systems
- Testing
    - Desk check
    - Walk-through
    - Tabletop Exercise
    - Simulation
        - Disaster simulated outside of prod
    - Parallel
        - Disaster simulated while prod activities are ongoing
    - Full Cutover
        - Disaster is invoked affected prod

## Testing
- Acceptance testing
    - Determines if app meets acceptance criteria and can be released
- Regression testing
    - Ensures changes to codebase do not negatively impact existing functionality of app
- Misuse case testing
- Negative tests
    - Provide evidence of app behaviour if unexpected or invalid data
    - Fuzzing
- Positive tests
    - Determines a system works as expected

## Penetration Testing Process
- Chartering
    - Rules of Engagement
- Discovery
- Scanning
    - Fingerprinting
- Exploitation
- Reporting

## Types of Reporting
- Full disclosure
- Responsible disclosure
- Mandatory reporting
- Whistleblowing

## SOC Reports
- SOC 1: Financial
    - SOC 1 Type 1
        - Audits performance of set of controls at a particular point in time
    - SOC 1 Type 2
        - Reports on performance of controls over a specified period of time
- SOC 2: Security
    - Trust Services Criteria Principles
        - Security
        - Availability
        - Confidentiality
        - Processing Integrity
        - Privacy
    - SOC 2 Type 1
        - Verifies design of controls at the time of report
    - SOC 2 Type 2
        - Assesses control effectivity over a specified period of time
- SOC 3: Summary of SOC 2 report
- SOC for Cybersecurity

## Structural Coverage Types
- Statement coverage
- Decision (branch) coverage
- Condition coverage
- Multi-condition coverage
- Loop coverage
- Correspondence between data and field types
- Data flow coverage
- Populating required fields
- Path coverage
- Allowed number of characters
- Allowed data bounds and limits
