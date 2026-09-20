# Threat Modeling Notes

## Threat Intelligence
- Evaluating a threat intelligence source: 
    - Timeliness: How prompty is threat intelligence delivered?
    - Accuracy: Is the data correct?
    - Reliability: Is the provider consistent?

## Managing Threat Indicators
- Cyber Observable eXpression (CyxOX): Schema to classify different threats
- Structured Threat Information eXpression (STIX): Language to represent CyBox threat information
- Trusted Automated eXchange of Intelligence Information (TAXII): Exchange for STIX threat information
- OpenIOC: Mandiant threat framework

## Intelligence Sharing
- ISACs: Information sharing and analysis centers

## Threat Research
- Reputational threat research: Identifies potentially malicious actors based upon their use of IP address, email address, domains, etc. that were previously used in attacks
- Behavioral threat research: Identifies potentially malicious actors based upon the similarity of their behaviors to past attackers

## Identifying Threats
Identifying threats with a structured approach:
- Asset focus: Use the asset inventory as the basis for the analysis
- Threat focus: Identify how specific threats may affect each information system
- Service focus: Identify the impact of various threats on a specific service

## Automating Threat Intelligence
Data enrichment tasks:
- Source address reconnaissance
- Trigger vuln scan
- Retrieve related log records

## Threat Hunting
- Assumption of compromise
- Begin with hypothesis