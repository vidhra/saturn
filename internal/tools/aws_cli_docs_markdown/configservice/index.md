# configserviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# configservice

## Description

Config provides a way to keep track of the configurations of all the Amazon Web Services resources associated with your Amazon Web Services account. You can use Config to get the current and historical configurations of each Amazon Web Services resource and also to get information about the relationship between the resources. An Amazon Web Services resource can be an Amazon Compute Cloud (Amazon EC2) instance, an Elastic Block Store (EBS) volume, an elastic network Interface (ENI), or a security group. For a complete list of resources currently supported by Config, see [Supported Amazon Web Services resources](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources) .

You can access and manage Config through the Amazon Web Services Management Console, the Amazon Web Services Command Line Interface (Amazon Web Services CLI), the Config API, or the Amazon Web Services SDKs for Config. This reference guide contains documentation for the Config API and the Amazon Web Services CLI commands that you can use to manage Config. The Config API uses the Signature Version 4 protocol for signing requests. For more information about how to sign a request with this protocol, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) . For detailed information about Config features and their associated actions or commands, as well as how to work with Amazon Web Services Management Console, see [What Is Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) in the *Config Developer Guide* .

## Available Commands

- [associate-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/associate-resource-types.html)
- [batch-get-aggregate-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/batch-get-aggregate-resource-config.html)
- [batch-get-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/batch-get-resource-config.html)
- [delete-aggregation-authorization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-aggregation-authorization.html)
- [delete-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-config-rule.html)
- [delete-configuration-aggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-configuration-aggregator.html)
- [delete-configuration-recorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-configuration-recorder.html)
- [delete-conformance-pack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-conformance-pack.html)
- [delete-delivery-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-delivery-channel.html)
- [delete-evaluation-results](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-evaluation-results.html)
- [delete-organization-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-organization-config-rule.html)
- [delete-organization-conformance-pack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-organization-conformance-pack.html)
- [delete-pending-aggregation-request](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-pending-aggregation-request.html)
- [delete-remediation-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-remediation-configuration.html)
- [delete-remediation-exceptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-remediation-exceptions.html)
- [delete-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-resource-config.html)
- [delete-retention-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-retention-configuration.html)
- [delete-service-linked-configuration-recorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-service-linked-configuration-recorder.html)
- [delete-stored-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-stored-query.html)
- [deliver-config-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/deliver-config-snapshot.html)
- [describe-aggregate-compliance-by-config-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-aggregate-compliance-by-config-rules.html)
- [describe-aggregate-compliance-by-conformance-packs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-aggregate-compliance-by-conformance-packs.html)
- [describe-aggregation-authorizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-aggregation-authorizations.html)
- [describe-compliance-by-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-config-rule.html)
- [describe-compliance-by-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-resource.html)
- [describe-config-rule-evaluation-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rule-evaluation-status.html)
- [describe-config-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html)
- [describe-configuration-aggregator-sources-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-aggregator-sources-status.html)
- [describe-configuration-aggregators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-aggregators.html)
- [describe-configuration-recorder-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorder-status.html)
- [describe-configuration-recorders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html)
- [describe-conformance-pack-compliance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-conformance-pack-compliance.html)
- [describe-conformance-pack-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-conformance-pack-status.html)
- [describe-conformance-packs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-conformance-packs.html)
- [describe-delivery-channel-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channel-status.html)
- [describe-delivery-channels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html)
- [describe-organization-config-rule-statuses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-config-rule-statuses.html)
- [describe-organization-config-rules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-config-rules.html)
- [describe-organization-conformance-pack-statuses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-conformance-pack-statuses.html)
- [describe-organization-conformance-packs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-organization-conformance-packs.html)
- [describe-pending-aggregation-requests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-pending-aggregation-requests.html)
- [describe-remediation-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-configurations.html)
- [describe-remediation-exceptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-exceptions.html)
- [describe-remediation-execution-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-execution-status.html)
- [describe-retention-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-retention-configurations.html)
- [disassociate-resource-types](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/disassociate-resource-types.html)
- [get-aggregate-compliance-details-by-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-compliance-details-by-config-rule.html)
- [get-aggregate-config-rule-compliance-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-config-rule-compliance-summary.html)
- [get-aggregate-conformance-pack-compliance-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-conformance-pack-compliance-summary.html)
- [get-aggregate-discovered-resource-counts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-discovered-resource-counts.html)
- [get-aggregate-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-resource-config.html)
- [get-compliance-details-by-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-config-rule.html)
- [get-compliance-details-by-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-resource.html)
- [get-compliance-summary-by-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-config-rule.html)
- [get-compliance-summary-by-resource-type](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-resource-type.html)
- [get-conformance-pack-compliance-details](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-conformance-pack-compliance-details.html)
- [get-conformance-pack-compliance-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-conformance-pack-compliance-summary.html)
- [get-custom-rule-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-custom-rule-policy.html)
- [get-discovered-resource-counts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-discovered-resource-counts.html)
- [get-organization-config-rule-detailed-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-organization-config-rule-detailed-status.html)
- [get-organization-conformance-pack-detailed-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-organization-conformance-pack-detailed-status.html)
- [get-organization-custom-rule-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-organization-custom-rule-policy.html)
- [get-resource-config-history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-config-history.html)
- [get-resource-evaluation-summary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-evaluation-summary.html)
- [get-status](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-status.html)
- [get-stored-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-stored-query.html)
- [list-aggregate-discovered-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-aggregate-discovered-resources.html)
- [list-configuration-recorders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-configuration-recorders.html)
- [list-conformance-pack-compliance-scores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-conformance-pack-compliance-scores.html)
- [list-discovered-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-discovered-resources.html)
- [list-resource-evaluations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-resource-evaluations.html)
- [list-stored-queries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-stored-queries.html)
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-tags-for-resource.html)
- [put-aggregation-authorization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-aggregation-authorization.html)
- [put-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-config-rule.html)
- [put-configuration-aggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-aggregator.html)
- [put-configuration-recorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-recorder.html)
- [put-conformance-pack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-conformance-pack.html)
- [put-delivery-channel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-delivery-channel.html)
- [put-evaluations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-evaluations.html)
- [put-external-evaluation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-external-evaluation.html)
- [put-organization-config-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-organization-config-rule.html)
- [put-organization-conformance-pack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-organization-conformance-pack.html)
- [put-remediation-configurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-remediation-configurations.html)
- [put-remediation-exceptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-remediation-exceptions.html)
- [put-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-resource-config.html)
- [put-retention-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-retention-configuration.html)
- [put-service-linked-configuration-recorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-service-linked-configuration-recorder.html)
- [put-stored-query](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-stored-query.html)
- [select-aggregate-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/select-aggregate-resource-config.html)
- [select-resource-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/select-resource-config.html)
- [start-config-rules-evaluation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-config-rules-evaluation.html)
- [start-configuration-recorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-configuration-recorder.html)
- [start-remediation-execution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-remediation-execution.html)
- [start-resource-evaluation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-resource-evaluation.html)
- [stop-configuration-recorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/stop-configuration-recorder.html)
- [subscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/subscribe.html)
- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/tag-resource.html)
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/untag-resource.html)