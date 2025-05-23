# network-firewallÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# network-firewall

## Description

This is the API Reference for Network Firewall. This guide is for developers who need detailed information about the Network Firewall API actions, data types, and errors.

The REST API requires you to handle connection details, such as calculating signatures, handling request retries, and error handling. For general information about using the Amazon Web Services REST APIs, see [Amazon Web Services APIs](https://docs.aws.amazon.com/general/latest/gr/aws-apis.html) .

To view the complete list of Amazon Web Services Regions where Network Firewall is available, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/network-firewall.html) in the *Amazon Web Services General Reference* .

To access Network Firewall using the IPv4 REST API endpoint: `https://network-firewall.<region>.amazonaws.com`

To access Network Firewall using the Dualstack (IPv4 and IPv6) REST API endpoint: `https://network-firewall.<region>.aws.api`

Alternatively, you can use one of the Amazon Web Services SDKs to access an API thatâs tailored to the programming language or platform that youâre using. For more information, see [Amazon Web Services SDKs](http://aws.amazon.com/tools/#SDKs) .

For descriptions of Network Firewall features, including and step-by-step instructions on how to use them through the Network Firewall console, see the [Network Firewall Developer Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/) .

Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for Amazon Virtual Private Cloud (Amazon VPC). With Network Firewall, you can filter traffic at the perimeter of your VPC. This includes filtering traffic going to and coming from an internet gateway, NAT gateway, or over VPN or Direct Connect. Network Firewall uses rules that are compatible with Suricata, a free, open source network analysis and threat detection engine. Network Firewall supports Suricata version 7.0.3. For information about Suricata, see the [Suricata website](https://suricata.io/) and the [Suricata User Guide](https://suricata.readthedocs.io/en/suricata-7.0.3/) .

You can use Network Firewall to monitor and protect your VPC traffic in a number of ways. The following are just a few examples:

- Allow domains or IP addresses for known Amazon Web Services service endpoints, such as Amazon S3, and block all other forms of traffic.
- Use custom lists of known bad domains to limit the types of domain names that your applications can access.
- Perform deep packet inspection on traffic entering or leaving your VPC.
- Use stateful protocol detection to filter protocols like HTTPS, regardless of the port used.

To enable Network Firewall for your VPCs, you perform steps in both Amazon VPC and in Network Firewall. For information about using Amazon VPC, see [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/) .

To start using Network Firewall, do the following:

- (Optional) If you donât already have a VPC that you want to protect, create it in Amazon VPC.
- In Amazon VPC, in each Availability Zone where you want to have a firewall endpoint, create a subnet for the sole use of Network Firewall.
- In Network Firewall, create stateless and stateful rule groups, to define the components of the network traffic filtering behavior that you want your firewall to have.
- In Network Firewall, create a firewall policy that uses your rule groups and specifies additional default traffic filtering behavior.
- In Network Firewall, create a firewall and specify your new firewall policy and VPC subnets. Network Firewall creates a firewall endpoint in each subnet that you specify, with the behavior thatâs defined in the firewall policy.
- In Amazon VPC, use ingress routing enhancements to route traffic through the new firewall endpoints.

## Available Commands

- [associate-firewall-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-firewall-policy.html)
- [associate-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/associate-subnets.html)
- [create-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall.html)
- [create-firewall-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall-policy.html)
- [create-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-rule-group.html)
- [create-tls-inspection-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-tls-inspection-configuration.html)
- [delete-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall.html)
- [delete-firewall-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall-policy.html)
- [delete-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-resource-policy.html)
- [delete-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-rule-group.html)
- [delete-tls-inspection-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-tls-inspection-configuration.html)
- [describe-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall.html)
- [describe-firewall-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall-policy.html)
- [describe-flow-operation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-flow-operation.html)
- [describe-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-logging-configuration.html)
- [describe-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-resource-policy.html)
- [describe-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group.html)
- [describe-rule-group-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-rule-group-metadata.html)
- [describe-tls-inspection-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-tls-inspection-configuration.html)
- [disassociate-subnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/disassociate-subnets.html)
- [get-analysis-report-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/get-analysis-report-results.html)
- [list-analysis-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-analysis-reports.html)
- [list-firewall-policies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewall-policies.html)
- [list-firewalls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewalls.html)
- [list-flow-operation-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-flow-operation-results.html)
- [list-flow-operations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-flow-operations.html)
- [list-rule-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-rule-groups.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-tags-for-resource.html)
- [list-tls-inspection-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-tls-inspection-configurations.html)
- [put-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/put-resource-policy.html)
- [start-analysis-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/start-analysis-report.html)
- [start-flow-capture](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/start-flow-capture.html)
- [start-flow-flush](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/start-flow-flush.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/untag-resource.html)
- [update-firewall-analysis-settings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-analysis-settings.html)
- [update-firewall-delete-protection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-delete-protection.html)
- [update-firewall-description](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-description.html)
- [update-firewall-encryption-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-encryption-configuration.html)
- [update-firewall-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html)
- [update-firewall-policy-change-protection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy-change-protection.html)
- [update-logging-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-logging-configuration.html)
- [update-rule-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-rule-group.html)
- [update-subnet-change-protection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-subnet-change-protection.html)
- [update-tls-inspection-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-tls-inspection-configuration.html)