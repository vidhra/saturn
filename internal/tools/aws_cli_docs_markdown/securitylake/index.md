# securitylakeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# securitylake

## Description

Amazon Security Lake is a fully managed security data lake service. You can use Security Lake to automatically centralize security data from cloud, on-premises, and custom sources into a data lake thatâs stored in your Amazon Web Services account. Amazon Web Services Organizations is an account management service that lets you consolidate multiple Amazon Web Services accounts into an organization that you create and centrally manage. With Organizations, you can create member accounts and invite existing accounts to join your organization. Security Lake helps you analyze security data for a more complete understanding of your security posture across the entire organization. It can also help you improve the protection of your workloads, applications, and data.

The data lake is backed by Amazon Simple Storage Service (Amazon S3) buckets, and you retain ownership over your data.

Amazon Security Lake integrates with CloudTrail, a service that provides a record of actions taken by a user, role, or an Amazon Web Services service. In Security Lake, CloudTrail captures API calls for Security Lake as events. The calls captured include calls from the Security Lake console and code calls to the Security Lake API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Security Lake. If you donât configure a trail, you can still view the most recent events in the CloudTrail console in Event history. Using the information collected by CloudTrail you can determine the request that was made to Security Lake, the IP address from which the request was made, who made the request, when it was made, and additional details. To learn more about Security Lake information in CloudTrail, see the [Amazon Security Lake User Guide](https://docs.aws.amazon.com/security-lake/latest/userguide/securitylake-cloudtrail.html) .

Security Lake automates the collection of security-related log and event data from integrated Amazon Web Services services and third-party services. It also helps you manage the lifecycle of data with customizable retention and replication settings. Security Lake converts ingested data into Apache Parquet format and a standard open-source schema called the Open Cybersecurity Schema Framework (OCSF).

Other Amazon Web Services services and third-party services can subscribe to the data thatâs stored in Security Lake for incident response and security data analytics.

## Available Commands

- [create-aws-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-aws-log-source.html)
- [create-custom-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-custom-log-source.html)
- [create-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html)
- [create-data-lake-exception-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake-exception-subscription.html)
- [create-data-lake-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake-organization-configuration.html)
- [create-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html)
- [create-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber-notification.html)
- [delete-aws-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-aws-log-source.html)
- [delete-custom-log-source](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-custom-log-source.html)
- [delete-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake.html)
- [delete-data-lake-exception-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake-exception-subscription.html)
- [delete-data-lake-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake-organization-configuration.html)
- [delete-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber.html)
- [delete-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber-notification.html)
- [deregister-data-lake-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/deregister-data-lake-delegated-administrator.html)
- [get-data-lake-exception-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-exception-subscription.html)
- [get-data-lake-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-organization-configuration.html)
- [get-data-lake-sources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-sources.html)
- [get-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-subscriber.html)
- [list-data-lake-exceptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lake-exceptions.html)
- [list-data-lakes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lakes.html)
- [list-log-sources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-log-sources.html)
- [list-subscribers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-subscribers.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-tags-for-resource.html)
- [register-data-lake-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/register-data-lake-delegated-administrator.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/untag-resource.html)
- [update-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html)
- [update-data-lake-exception-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake-exception-subscription.html)
- [update-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber.html)
- [update-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber-notification.html)