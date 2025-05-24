# guarddutyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# guardduty

## Description

Amazon GuardDuty is a continuous security monitoring service that analyzes and processes the following foundational data sources - VPC flow logs, Amazon Web Services CloudTrail management event logs, CloudTrail S3 data event logs, EKS audit logs, DNS logs, Amazon EBS volume data, runtime activity belonging to container workloads, such as Amazon EKS, Amazon ECS (including Amazon Web Services Fargate), and Amazon EC2 instances. It uses threat intelligence feeds, such as lists of malicious IPs and domains, and machine learning to identify unexpected, potentially unauthorized, and malicious activity within your Amazon Web Services environment. This can include issues like escalations of privileges, uses of exposed credentials, or communication with malicious IPs, domains, or presence of malware on your Amazon EC2 instances and container workloads. For example, GuardDuty can detect compromised EC2 instances and container workloads serving malware, or mining bitcoin.

GuardDuty also monitors Amazon Web Services account access behavior for signs of compromise, such as unauthorized infrastructure deployments like EC2 instances deployed in a Region that has never been used, or unusual API calls like a password policy change to reduce password strength.

GuardDuty informs you about the status of your Amazon Web Services environment by producing security findings that you can view in the GuardDuty console or through Amazon EventBridge. For more information, see the * [Amazon GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) * .

## Available Commands

- [accept-administrator-invitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/accept-administrator-invitation.html)
- [archive-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/archive-findings.html)
- [create-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html)
- [create-filter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html)
- [create-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-ip-set.html)
- [create-malware-protection-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-malware-protection-plan.html)
- [create-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-members.html)
- [create-publishing-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-publishing-destination.html)
- [create-sample-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-sample-findings.html)
- [create-threat-intel-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-threat-intel-set.html)
- [decline-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/decline-invitations.html)
- [delete-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-detector.html)
- [delete-filter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-filter.html)
- [delete-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-invitations.html)
- [delete-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-ip-set.html)
- [delete-malware-protection-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-malware-protection-plan.html)
- [delete-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-members.html)
- [delete-publishing-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-publishing-destination.html)
- [delete-threat-intel-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-threat-intel-set.html)
- [describe-malware-scans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-malware-scans.html)
- [describe-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-organization-configuration.html)
- [describe-publishing-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/describe-publishing-destination.html)
- [disable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disable-organization-admin-account.html)
- [disassociate-from-administrator-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disassociate-from-administrator-account.html)
- [disassociate-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disassociate-members.html)
- [enable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/enable-organization-admin-account.html)
- [get-administrator-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-administrator-account.html)
- [get-coverage-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-coverage-statistics.html)
- [get-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-detector.html)
- [get-filter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-filter.html)
- [get-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html)
- [get-findings-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings-statistics.html)
- [get-invitations-count](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-invitations-count.html)
- [get-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-ip-set.html)
- [get-malware-protection-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-malware-protection-plan.html)
- [get-malware-scan-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-malware-scan-settings.html)
- [get-member-detectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-member-detectors.html)
- [get-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-members.html)
- [get-organization-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-organization-statistics.html)
- [get-remaining-free-trial-days](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-remaining-free-trial-days.html)
- [get-threat-intel-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-threat-intel-set.html)
- [get-usage-statistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-usage-statistics.html)
- [invite-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/invite-members.html)
- [list-coverage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-coverage.html)
- [list-detectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-detectors.html)
- [list-filters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-filters.html)
- [list-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html)
- [list-invitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-invitations.html)
- [list-ip-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-ip-sets.html)
- [list-malware-protection-plans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-malware-protection-plans.html)
- [list-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-members.html)
- [list-organization-admin-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-organization-admin-accounts.html)
- [list-publishing-destinations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-publishing-destinations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-tags-for-resource.html)
- [list-threat-intel-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-threat-intel-sets.html)
- [start-malware-scan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/start-malware-scan.html)
- [start-monitoring-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/start-monitoring-members.html)
- [stop-monitoring-members](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/stop-monitoring-members.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/tag-resource.html)
- [unarchive-findings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/unarchive-findings.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/untag-resource.html)
- [update-detector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-detector.html)
- [update-filter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-filter.html)
- [update-findings-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-findings-feedback.html)
- [update-ip-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-ip-set.html)
- [update-malware-protection-plan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-malware-protection-plan.html)
- [update-malware-scan-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-malware-scan-settings.html)
- [update-member-detectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-member-detectors.html)
- [update-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-organization-configuration.html)
- [update-publishing-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-publishing-destination.html)
- [update-threat-intel-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-threat-intel-set.html)