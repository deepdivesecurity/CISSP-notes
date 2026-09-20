# Risk Management Notes

## Risk Analysis, Assessment, & Scope
- Determine scope of risk assessment before starting
- Threat: External force jeopardizing security
- *EXAM*: Threat vectors are specific methods that threats use to exploit a vulnerability
- Vulnerability: Weaknesses in security controls
- Risks occur when there is a vulnerability with a corresponding threat which exists in the environment
- Likelihood: Probability that a risk will occur
- Impact: Amount of expected damage
- Types of risk assessments: 
    - One-time 
    - Ad hoc
    - Recurring
    - Continuous
- Qualitative risk analysis: Uses subjective ratings to evaluate risk likelihood and impact
- Quantitative risk analysis: Uses objective numeric ratings to evaluate risk likelihood and impact

## Risk Treatment
- Risk Management Strategies
    - Risk avoidance: Change org business practice to avoid risk
    - Risk transference: Shift the impact of a risk to another org
    - Risk mitigation: Reduce likelihood or impact of risk
    - Risk acceptance: Accept the risk without taking further action
        - Risk acceptance may require exemption or exception to policies or standards
- Risk profile: The full set of risks facing an org
- Risk appetites
    - Expansionary: Risk appetites involve a willingness to take on higher levels of risk
    - Neutral: Risk appetites take a balanced approach to risk
    - Conservative: Risk appetites focus on maintaining stability and protecting assets
- Risk threshold: Level at which the risk becomes unacceptable

## Security Control Selection & Implementation
- Defense in depth: Multiple controls for one objective
- Types of controls: 
    - Preventative controls: Stops a security issue from occurring in the first place
    - Detection controls: Identifies that a potential security issue has taken place
    - Corrective controls: Remediates security issues that have already occurred
    - Technical controls: Use technology to achieve security control objectives
    - Operational controls: Human-driven processes to manage technology in a secure manner
    - Management controls: Improve security of a risk management process itself
    - **EXAM**: Technical controls are carried out by technology; operational controls are carried out by people
- False positive error: Occurs when a control triggers when it shouldn't
- False negative error: Occurs when a control fails to trigger when it should have

## Continuous Monitoring, Measurement, & Tuning
- 6 steps of continuous monitoring program as defined by NIST: 
    1. Define a continuous monitoring strategy based upon risk tolerance that maintains clear visibility into assets, vulnerabilities, threats, and business impact
    2. Establish a monitoring program by outlining metrics & monitoring & assessment frequencies
    3. Implement the program by collecting the metrics, performing the assessments, & building reports in an automated was as much as possible
    4. Analyze & report findings from the collected data
    5. Respond to those findings by mitigating, avoiding, transferring, or accepting the risk
    6. Review & update the monitoring program, adjusting the strategy, and maturing measurement capabilities
- SIEMs assist with security data analytics and correlation
- Types of analysis: 
    - Anomaly/Heuristic analysis: Detects outlier data points
    - Trend analysis: Detects changes over time
    - Behavioral analysis: Detects unusual user activity
    - Availability analysis: Provides uptime information
- Continuous tuning: Maintains effective controls

## Risk Management Frameworks
- NIST SP 800-37: Risk management framework
    - NIST Risk Management Framework Steps
        1. Categorize information system
        2. Select security controls
        3. Implement security controls
        4. Assess security controls
        5. Authorize information system
        6. Monitor security controls

## Risk Visibility & Reporting
- Risk register: Tracks risk information
    - Centralized document
    - Used on org-wide basis, or project/domain basis
    - May be referred to as risk logs
    - Risk register contents:
        - Description
        - Category
        - Risk owner
        - Probability and impact
        - Risk rating
        - Risk management actions
    - Risk register information sources:
        - Risk assessment results
        - Audit findings
        - Team member output
        - Threat intelligence
- Types of reporting: 
    - Internal reporting: Updates to management on status and effectiveness of risk management activities
    - External reporting: Meets requirements for providing information to regulators, investors, customers, and partners
