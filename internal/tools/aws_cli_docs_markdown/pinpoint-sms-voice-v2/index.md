# pinpoint-sms-voice-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# pinpoint-sms-voice-v2

## Description

Welcome to the *AWS End User Messaging SMS and Voice, version 2 API Reference* . This guide provides information about AWS End User Messaging SMS and Voice, version 2 API resources, including supported HTTP methods, parameters, and schemas.

Amazon Pinpoint is an Amazon Web Services service that you can use to engage with your recipients across multiple messaging channels. The AWS End User Messaging SMS and Voice, version 2 API provides programmatic access to options that are unique to the SMS and voice channels. AWS End User Messaging SMS and Voice, version 2 resources such as phone numbers, sender IDs, and opt-out lists can be used by the Amazon Pinpoint API.

If youâre new to AWS End User Messaging SMS and Voice, itâs also helpful to review the [AWS End User Messaging SMS User Guide](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html) . The *AWS End User Messaging SMS User Guide* provides tutorials, code samples, and procedures that demonstrate how to use AWS End User Messaging SMS and Voice features programmatically and how to integrate functionality into mobile apps and other types of applications. The guide also provides key information, such as AWS End User Messaging SMS and Voice integration with other Amazon Web Services services, and the quotas that apply to use of the service.

**Regional availability**

The *AWS End User Messaging SMS and Voice version 2 API Reference* is available in several Amazon Web Services Regions and it provides an endpoint for each of these Regions. For a list of all the Regions and endpoints where the API is currently available, see [Amazon Web Services Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#pinpoint_region) and [Amazon Pinpoint endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html) in the Amazon Web Services General Reference. To learn more about Amazon Web Services Regions, see [Managing Amazon Web Services Regions](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html) in the Amazon Web Services General Reference.

In each Region, Amazon Web Services maintains multiple Availability Zones. These Availability Zones are physically isolated from each other, but are united by private, low-latency, high-throughput, and highly redundant network connections. These Availability Zones enable us to provide very high levels of availability and redundancy, while also minimizing latency. To learn more about the number of Availability Zones that are available in each Region, see [Amazon Web Services Global Infrastructure.](https://aws.amazon.com/about-aws/global-infrastructure/)

## Available Commands

- [associate-origination-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/associate-origination-identity.html)
- [associate-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/associate-protect-configuration.html)
- [create-configuration-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-configuration-set.html)
- [create-event-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-event-destination.html)
- [create-opt-out-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-opt-out-list.html)
- [create-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-pool.html)
- [create-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-protect-configuration.html)
- [create-registration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-registration.html)
- [create-registration-association](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-registration-association.html)
- [create-registration-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-registration-attachment.html)
- [create-registration-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-registration-version.html)
- [create-verified-destination-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-verified-destination-number.html)
- [delete-account-default-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-account-default-protect-configuration.html)
- [delete-configuration-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-configuration-set.html)
- [delete-default-message-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-default-message-type.html)
- [delete-default-sender-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-default-sender-id.html)
- [delete-event-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-event-destination.html)
- [delete-keyword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-keyword.html)
- [delete-media-message-spend-limit-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-media-message-spend-limit-override.html)
- [delete-opt-out-list](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-opt-out-list.html)
- [delete-opted-out-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-opted-out-number.html)
- [delete-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-pool.html)
- [delete-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-protect-configuration.html)
- [delete-protect-configuration-rule-set-number-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-protect-configuration-rule-set-number-override.html)
- [delete-registration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-registration.html)
- [delete-registration-attachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-registration-attachment.html)
- [delete-registration-field-value](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-registration-field-value.html)
- [delete-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-resource-policy.html)
- [delete-text-message-spend-limit-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-text-message-spend-limit-override.html)
- [delete-verified-destination-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-verified-destination-number.html)
- [delete-voice-message-spend-limit-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/delete-voice-message-spend-limit-override.html)
- [describe-account-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-account-attributes.html)
- [describe-account-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-account-limits.html)
- [describe-configuration-sets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-configuration-sets.html)
- [describe-keywords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-keywords.html)
- [describe-opt-out-lists](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-opt-out-lists.html)
- [describe-opted-out-numbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-opted-out-numbers.html)
- [describe-phone-numbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.html)
- [describe-pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-pools.html)
- [describe-protect-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-protect-configurations.html)
- [describe-registration-attachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-attachments.html)
- [describe-registration-field-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-field-definitions.html)
- [describe-registration-field-values](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-field-values.html)
- [describe-registration-section-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-section-definitions.html)
- [describe-registration-type-definitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-type-definitions.html)
- [describe-registration-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registration-versions.html)
- [describe-registrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-registrations.html)
- [describe-sender-ids](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.html)
- [describe-spend-limits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-spend-limits.html)
- [describe-verified-destination-numbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-verified-destination-numbers.html)
- [disassociate-origination-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/disassociate-origination-identity.html)
- [disassociate-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/disassociate-protect-configuration.html)
- [discard-registration-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/discard-registration-version.html)
- [get-protect-configuration-country-rule-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/get-protect-configuration-country-rule-set.html)
- [get-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/get-resource-policy.html)
- [list-pool-origination-identities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/list-pool-origination-identities.html)
- [list-protect-configuration-rule-set-number-overrides](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/list-protect-configuration-rule-set-number-overrides.html)
- [list-registration-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/list-registration-associations.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/list-tags-for-resource.html)
- [put-keyword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/put-keyword.html)
- [put-message-feedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/put-message-feedback.html)
- [put-opted-out-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/put-opted-out-number.html)
- [put-protect-configuration-rule-set-number-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/put-protect-configuration-rule-set-number-override.html)
- [put-registration-field-value](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/put-registration-field-value.html)
- [put-resource-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/put-resource-policy.html)
- [release-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/release-phone-number.html)
- [release-sender-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/release-sender-id.html)
- [request-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/request-phone-number.html)
- [request-sender-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/request-sender-id.html)
- [send-destination-number-verification-code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/send-destination-number-verification-code.html)
- [send-media-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/send-media-message.html)
- [send-text-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/send-text-message.html)
- [send-voice-message](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/send-voice-message.html)
- [set-account-default-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-account-default-protect-configuration.html)
- [set-default-message-feedback-enabled](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-default-message-feedback-enabled.html)
- [set-default-message-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-default-message-type.html)
- [set-default-sender-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-default-sender-id.html)
- [set-media-message-spend-limit-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-media-message-spend-limit-override.html)
- [set-text-message-spend-limit-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-text-message-spend-limit-override.html)
- [set-voice-message-spend-limit-override](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/set-voice-message-spend-limit-override.html)
- [submit-registration-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/submit-registration-version.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/untag-resource.html)
- [update-event-destination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-event-destination.html)
- [update-phone-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-phone-number.html)
- [update-pool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-pool.html)
- [update-protect-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-protect-configuration.html)
- [update-protect-configuration-country-rule-set](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-protect-configuration-country-rule-set.html)
- [update-sender-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/update-sender-id.html)
- [verify-destination-number](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/verify-destination-number.html)