# pinpoint-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# pinpoint-email

## Description

Welcome to the *Amazon Pinpoint Email API Reference* . This guide provides information about the Amazon Pinpoint Email API (version 1.0), including supported operations, data types, parameters, and schemas.

[Amazon Pinpoint](https://aws.amazon.com/pinpoint) is an AWS service that you can use to engage with your customers across multiple messaging channels. You can use Amazon Pinpoint to send email, SMS text messages, voice messages, and push notifications. The Amazon Pinpoint Email API provides programmatic access to options that are unique to the email channel and supplement the options provided by the Amazon Pinpoint API.

If youâre new to Amazon Pinpoint, you might find it helpful to also review the [Amazon Pinpoint Developer Guide](https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html) . The *Amazon Pinpoint Developer Guide* provides tutorials, code samples, and procedures that demonstrate how to use Amazon Pinpoint features programmatically and how to integrate Amazon Pinpoint functionality into mobile apps and other types of applications. The guide also provides information about key topics such as Amazon Pinpoint integration with other AWS services and the limits that apply to using the service.

The Amazon Pinpoint Email API is available in several AWS Regions and it provides an endpoint for each of these Regions. For a list of all the Regions and endpoints where the API is currently available, see [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#pinpoint_region) in the *Amazon Web Services General Reference* . To learn more about AWS Regions, see [Managing AWS Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the *Amazon Web Services General Reference* .

In each Region, AWS maintains multiple Availability Zones. These Availability Zones are physically isolated from each other, but are united by private, low-latency, high-throughput, and highly redundant network connections. These Availability Zones enable us to provide very high levels of availability and redundancy, while also minimizing latency. To learn more about the number of Availability Zones that are available in each Region, see [AWS Global Infrastructure](http://aws.amazon.com/about-aws/global-infrastructure/) .

## Available Commands

- [create-configuration-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-configuration-set.html)
- [create-configuration-set-event-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-configuration-set-event-destination.html)
- [create-dedicated-ip-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-dedicated-ip-pool.html)
- [create-deliverability-test-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-deliverability-test-report.html)
- [create-email-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-email-identity.html)
- [delete-configuration-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-configuration-set.html)
- [delete-configuration-set-event-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-configuration-set-event-destination.html)
- [delete-dedicated-ip-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-dedicated-ip-pool.html)
- [delete-email-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-email-identity.html)
- [get-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-account.html)
- [get-blacklist-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-blacklist-reports.html)
- [get-configuration-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-configuration-set.html)
- [get-configuration-set-event-destinations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-configuration-set-event-destinations.html)
- [get-dedicated-ip](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-dedicated-ip.html)
- [get-dedicated-ips](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-dedicated-ips.html)
- [get-deliverability-dashboard-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-deliverability-dashboard-options.html)
- [get-deliverability-test-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-deliverability-test-report.html)
- [get-domain-deliverability-campaign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-domain-deliverability-campaign.html)
- [get-domain-statistics-report](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-domain-statistics-report.html)
- [get-email-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-email-identity.html)
- [list-configuration-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-configuration-sets.html)
- [list-dedicated-ip-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-dedicated-ip-pools.html)
- [list-deliverability-test-reports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-deliverability-test-reports.html)
- [list-domain-deliverability-campaigns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-domain-deliverability-campaigns.html)
- [list-email-identities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-email-identities.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-tags-for-resource.html)
- [put-account-dedicated-ip-warmup-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-account-dedicated-ip-warmup-attributes.html)
- [put-account-sending-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-account-sending-attributes.html)
- [put-configuration-set-delivery-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-configuration-set-delivery-options.html)
- [put-configuration-set-reputation-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-configuration-set-reputation-options.html)
- [put-configuration-set-sending-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-configuration-set-sending-options.html)
- [put-configuration-set-tracking-options](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-configuration-set-tracking-options.html)
- [put-dedicated-ip-in-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-dedicated-ip-in-pool.html)
- [put-dedicated-ip-warmup-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-dedicated-ip-warmup-attributes.html)
- [put-deliverability-dashboard-option](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-deliverability-dashboard-option.html)
- [put-email-identity-dkim-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-email-identity-dkim-attributes.html)
- [put-email-identity-feedback-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-email-identity-feedback-attributes.html)
- [put-email-identity-mail-from-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/put-email-identity-mail-from-attributes.html)
- [send-email](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/send-email.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/untag-resource.html)
- [update-configuration-set-event-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/update-configuration-set-event-destination.html)