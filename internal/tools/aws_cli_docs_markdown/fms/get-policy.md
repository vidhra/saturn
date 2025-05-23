# get-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/index.html#cli-aws-fms) ]

# get-policy

## Description

Returns information about the specified Firewall Manager policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fms-2018-01-01/GetPolicy)

## Synopsis

```
get-policy
--policy-id <value>
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--policy-id` (string)

The ID of the Firewall Manager policy that you want the details for.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieve a Firewall Manager policy**

The following `get-policy` example retrieves the policy with the specified ID.

```
aws fms get-policy \
    --policy-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "Policy": {
        "PolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "PolicyName": "test",
        "PolicyUpdateToken": "1:p+2RpKR4wPFx7mcrL1UOQQ==",
        "SecurityServicePolicyData": {
            "Type": "SECURITY_GROUPS_COMMON",
            "ManagedServiceData": "{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":true,\"exclusiveResourceSecurityGroupManagement\":false,\"securityGroups\":[{\"id\":\"sg-045c43ccc9724e63e\"}]}"
        },
        "ResourceType": "AWS::EC2::Instance",
        "ResourceTags": [],
        "ExcludeResourceTags": false,
        "RemediationEnabled": false
    },
    "PolicyArn": "arn:aws:fms:us-west-2:123456789012:policy/d1ac59b8-938e-42b3-b2e0-7c620422ddc2"
}
```

For more information, see [Working with AWS Firewall Manager Policies](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-policies.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

Policy -> (structure)

Information about the specified Firewall Manager policy.

PolicyId -> (string)

The ID of the Firewall Manager policy.

PolicyName -> (string)

The name of the Firewall Manager policy.

PolicyUpdateToken -> (string)

A unique identifier for each update to the policy. When issuing a `PutPolicy` request, the `PolicyUpdateToken` in the request must match the `PolicyUpdateToken` of the current policy version. To get the `PolicyUpdateToken` of the current policy version, use a `GetPolicy` request.

SecurityServicePolicyData -> (structure)

Details about the security service that is being used to protect the resources.

Type -> (string)

The service that the policy is using to protect the resources. This specifies the type of policy that is created, either an WAF policy, a Shield Advanced policy, or a security group policy. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting Amazon Web Services Support.

ManagedServiceData -> (string)

Details about the service that are specific to the service type, in JSON format.

- Example: `DNS_FIREWALL` `"{\"type\":\"DNS_FIREWALL\",\"preProcessRuleGroups\":[{\"ruleGroupId\":\"rslvr-frg-1\",\"priority\":10}],\"postProcessRuleGroups\":[{\"ruleGroupId\":\"rslvr-frg-2\",\"priority\":9911}]}"`

### Note

Valid values for `preProcessRuleGroups` are between 1 and 99. Valid values for `postProcessRuleGroups` are between 9901 and 10000.

- Example: `IMPORT_NETWORK_FIREWALL` `"{\"type\":\"IMPORT_NETWORK_FIREWALL\",\"awsNetworkFirewallConfig\":{\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-west-2:000000000000:stateless-rulegroup\/rg1\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:drop\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:pass\"],\"networkFirewallStatelessCustomActions\":[],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-west-2:aws-managed:stateful-rulegroup\/ThreatSignaturesEmergingEventsStrictOrder\",\"priority\":8}],\"networkFirewallStatefulEngineOptions\":{\"ruleOrder\":\"STRICT_ORDER\"},\"networkFirewallStatefulDefaultActions\":[\"aws:drop_strict\"]}}"` `"{\"type\":\"DNS_FIREWALL\",\"preProcessRuleGroups\":[{\"ruleGroupId\":\"rslvr-frg-1\",\"priority\":10}],\"postProcessRuleGroups\":[{\"ruleGroupId\":\"rslvr-frg-2\",\"priority\":9911}]}"`

### Note

Valid values for `preProcessRuleGroups` are between 1 and 99. Valid values for `postProcessRuleGroups` are between 9901 and 10000.

- Example: `NETWORK_FIREWALL` - Centralized deployment model  `"{\"type\":\"NETWORK_FIREWALL\",\"awsNetworkFirewallConfig\":{\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":true}},\"firewallDeploymentModel\":{\"centralizedFirewallDeploymentModel\":{\"centralizedFirewallOrchestrationConfig\":{\"inspectionVpcIds\":[{\"resourceId\":\"vpc-1234\",\"accountId\":\"123456789011\"}],\"firewallCreationConfig\":{\"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneId\":null,\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]}]}},\"allowedIPV4CidrList\":[]}}}}"`   To use the centralized deployment model, you must set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `CENTRALIZED` .
- Example: `NETWORK_FIREWALL` - Distributed deployment model with automatic Availability Zone configuration  `"{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":[\"10.0.0.0/28\",\"192.168.0.0/28\"],\"routeManagementAction\":\"OFF\"},\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":true}}"`   With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `NULL` .
- Example: `NETWORK_FIREWALL` - Distributed deployment model with automatic Availability Zone configuration and route management  `"{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":[\"10.0.0.0/28\",\"192.168.0.0/28\"],\"routeManagementAction\":\"MONITOR\",\"routeManagementTargetTypes\":[\"InternetGateway\"]},\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\": \"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":true}}"`   To use the distributed deployment model, you must set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `NULL` .
- Example: `NETWORK_FIREWALL` - Distributed deployment model with custom Availability Zone configuration  `"{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"fragmentcustomactionname\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\", \"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}},{\"actionName\":\"fragmentcustomactionname\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"fragmentmetricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"firewallCreationConfig\":{ \"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]},{\"availabilityZoneName\":\"us-east-1b\",\"allowedIPV4CidrList\":[ \"10.0.0.0/28\"]}]} },\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":null,\"routeManagementAction\":\"OFF\",\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":boolean}}"`   With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring `firewallCreationConfig` . To configure the Availability Zones in `firewallCreationConfig` , specify either the `availabilityZoneName` or `availabilityZoneId` parameter, not both parameters.  To use the distributed deployment model, you must set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `NULL` .
- Example: `NETWORK_FIREWALL` - Distributed deployment model with custom Availability Zone configuration and route management  `"{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"fragmentcustomactionname\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}},{\"actionName\":\"fragmentcustomactionname\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"fragmentmetricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"firewallCreationConfig\":{\"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]},{\"availabilityZoneName\":\"us-east-1b\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]}]}},\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":null,\"routeManagementAction\":\"MONITOR\",\"routeManagementTargetTypes\":[\"InternetGateway\"],\"routeManagementConfig\":{\"allowCrossAZTrafficIfNoEndpoint\":true}},\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":boolean}}"`   To use the distributed deployment model, you must set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `NULL` .
- Example: `SECURITY_GROUPS_COMMON` `"{\"type\":\"SECURITY_GROUPS_COMMON\",\"securityGroups\":[{\"id\":\"sg-03b1f67d69ed00197\"}],\"revertManualSecurityGroupChanges\":true,\"exclusiveResourceSecurityGroupManagement\":true,\"applyToAllEC2InstanceENIs\":false,\"includeSharedVPC\":true,\"enableSecurityGroupReferencesDistribution\":true}"`
- Example: `SECURITY_GROUPS_COMMON` - Security group tag distribution   `""{\"type\":\"SECURITY_GROUPS_COMMON\",\"securityGroups\":[{\"id\":\"sg-000e55995d61a06bd\"}],\"revertManualSecurityGroupChanges\":true,\"exclusiveResourceSecurityGroupManagement\":false,\"applyToAllEC2InstanceENIs\":false,\"includeSharedVPC\":false,\"enableTagDistribution\":true}""`   Firewall Manager automatically distributes tags from the primary group to the security groups created by this policy. To use security group tag distribution, you must also set `revertManualSecurityGroupChanges` to `true` , otherwise Firewall Manager wonât be able to create the policy. When you enable `revertManualSecurityGroupChanges` , Firewall Manager identifies and reports when the security groups created by this policy become non-compliant.  Firewall Manager wonât distribute system tags added by Amazon Web Services services into the replica security groups. System tags begin with the `aws:` prefix.
- Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns   `"{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":false,\"exclusiveResourceSecurityGroupManagement\":false, \"applyToAllEC2InstanceENIs\":false,\"includeSharedVPC\":true,\"securityGroups\":[{\"id\":\" sg-000e55995d61a06bd\"}]}"`
- Example: `SECURITY_GROUPS_CONTENT_AUDIT` `"{\"type\":\"SECURITY_GROUPS_CONTENT_AUDIT\",\"preManagedOptions\":[{\"denyProtocolAllValue\":true},{\"auditSgDirection\":{\"type\":\"ALL\"}}],\"securityGroups\":[{\"id\":\"sg-049b2393a25468971\"}],\"securityGroupAction\":{\"type\":\"ALLOW\"}}"`   The security group action for content audit can be `ALLOW` or `DENY` . For `ALLOW` , all in-scope security group rules must be within the allowed range of the policyâs security group rules. For `DENY` , all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.
- Example: `SECURITY_GROUPS_USAGE_AUDIT` `"{\"type\":\"SECURITY_GROUPS_USAGE_AUDIT\",\"deleteUnusedSecurityGroups\":true,\"coalesceRedundantSecurityGroups\":true,\"optionalDelayForUnusedInMinutes\":60}"`
- Example: `SHIELD_ADVANCED` with web ACL management  `"{\"type\":\"SHIELD_ADVANCED\",\"optimizeUnassociatedWebACL\":true}"`   If you set `optimizeUnassociatedWebACL` to `true` , Firewall Manager creates web ACLs in accounts within the policy scope if the web ACLs will be used by at least one resource. Firewall Manager creates web ACLs in the accounts within policy scope only if the web ACLs will be used by at least one resource. If at any time an account comes into policy scope, Firewall Manager automatically creates a web ACL in the account if at least one resource will use the web ACL. Upon enablement, Firewall Manager performs a one-time cleanup of unused web ACLs in your account. The cleanup process can take several hours. If a resource leaves policy scope after Firewall Manager creates a web ACL, Firewall Manager doesnât disassociate the resource from the web ACL. If you want Firewall Manager to clean up the web ACL, you must first manually disassociate the resources from the web ACL, and then enable the manage unused web ACLs option in your policy. If you set `optimizeUnassociatedWebACL` to `false` , and Firewall Manager automatically creates an empty web ACL in each account thatâs within policy scope.
- Specification for `SHIELD_ADVANCED` for Amazon CloudFront distributions   `"{\"type\":\"SHIELD_ADVANCED\",\"automaticResponseConfiguration\": {\"automaticResponseStatus\":\"ENABLED|IGNORED|DISABLED\", \"automaticResponseAction\":\"BLOCK|COUNT\"}, \"overrideCustomerWebaclClassic\":true|false, \"optimizeUnassociatedWebACL\":true|false}"`   For example: `"{\"type\":\"SHIELD_ADVANCED\",\"automaticResponseConfiguration\": {\"automaticResponseStatus\":\"ENABLED\", \"automaticResponseAction\":\"COUNT\"}}"`   The default value for `automaticResponseStatus` is `IGNORED` . The value for `automaticResponseAction` is only required when `automaticResponseStatus` is set to `ENABLED` . The default value for `overrideCustomerWebaclClassic` is `false` . For other resource types that you can protect with a Shield Advanced policy, this `ManagedServiceData` configuration is an empty string.
- Example: `THIRD_PARTY_FIREWALL`   Replace `THIRD_PARTY_FIREWALL_NAME` with the name of the third-party firewall.  `"{ "type":"THIRD_PARTY_FIREWALL", "thirdPartyFirewall":"THIRD_PARTY_FIREWALL_NAME", "thirdPartyFirewallConfig":{ "thirdPartyFirewallPolicyList":["global-1"] }, "firewallDeploymentModel":{ "distributedFirewallDeploymentModel":{ "distributedFirewallOrchestrationConfig":{ "firewallCreationConfig":{ "endpointLocation":{ "availabilityZoneConfigList":[ { "availabilityZoneName":"${AvailabilityZone}" } ] } }, "allowedIPV4CidrList":[ ] } } } }"`
- Example: `WAFV2` - Account takeover prevention, Bot Control managed rule groups, optimize unassociated web ACL, and rule action override   `"{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupArn\":null,\"overrideAction\":{\"type\":\"NONE\"},\"managedRuleGroupIdentifier\":{\"versionEnabled\":null,\"version\":null,\"vendorName\":\"AWS\",\"managedRuleGroupName\":\"AWSManagedRulesATPRuleSet\",\"managedRuleGroupConfigs\":[{\"awsmanagedRulesATPRuleSet\":{\"loginPath\":\"/loginpath\",\"requestInspection\":{\"payloadType\":\"FORM_ENCODED|JSON\",\"usernameField\":{\"identifier\":\"/form/username\"},\"passwordField\":{\"identifier\":\"/form/password\"}}}}]},\"ruleGroupType\":\"ManagedRuleGroup\",\"excludeRules\":[],\"sampledRequestsEnabled\":true},{\"ruleGroupArn\":null,\"overrideAction\":{\"type\":\"NONE\"},\"managedRuleGroupIdentifier\":{\"versionEnabled\":null,\"version\":null,\"vendorName\":\"AWS\",\"managedRuleGroupName\":\"AWSManagedRulesBotControlRuleSet\",\"managedRuleGroupConfigs\":[{\"awsmanagedRulesBotControlRuleSet\":{\"inspectionLevel\":\"TARGETED|COMMON\"}}]},\"ruleGroupType\":\"ManagedRuleGroup\",\"excludeRules\":[],\"sampledRequestsEnabled\":true,\"ruleActionOverrides\":[{\"name\":\"Rule1\",\"actionToUse\":{\"allow|block|count|captcha|challenge\":{}}},{\"name\":\"Rule2\",\"actionToUse\":{\"allow|block|count|captcha|challenge\":{}}}]}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"ALLOW\"},\"customRequestHandling\":null,\"customResponse\":null,\"overrideCustomerWebACLAssociation\":false,\"loggingConfiguration\":null,\"sampledRequestsEnabledForDefaultActions\":true,\"optimizeUnassociatedWebACL\":true}"`
- Bot Control - For information about `AWSManagedRulesBotControlRuleSet` managed rule groups, see [AWSManagedRulesBotControlRuleSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesBotControlRuleSet.html) in the *WAF API Reference* .
- Fraud Control account takeover prevention (ATP) - For information about the properties available for `AWSManagedRulesATPRuleSet` managed rule groups, see [AWSManagedRulesATPRuleSet](https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesATPRuleSet.html) in the *WAF API Reference* .
- Optimize unassociated web ACL - If you set `optimizeUnassociatedWebACL` to `true` , Firewall Manager creates web ACLs in accounts within the policy scope if the web ACLs will be used by at least one resource. Firewall Manager creates web ACLs in the accounts within policy scope only if the web ACLs will be used by at least one resource. If at any time an account comes into policy scope, Firewall Manager automatically creates a web ACL in the account if at least one resource will use the web ACL. Upon enablement, Firewall Manager performs a one-time cleanup of unused web ACLs in your account. The cleanup process can take several hours. If a resource leaves policy scope after Firewall Manager creates a web ACL, Firewall Manager disassociates the resource from the web ACL, but wonât clean up the unused web ACL. Firewall Manager only cleans up unused web ACLs when you first enable management of unused web ACLs in a policy. If you set `optimizeUnassociatedWebACL` to `false` Firewall Manager doesnât manage unused web ACLs, and Firewall Manager automatically creates an empty web ACL in each account thatâs within policy scope.
- Rule action overrides - Firewall Manager supports rule action overrides only for managed rule groups. To configure a `RuleActionOverrides` add the `Name` of the rule to override, and `ActionToUse` , which is the new action to use for the rule. For information about using rule action override, see [RuleActionOverride](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleActionOverride.html) in the *WAF API Reference* .
- Example: `WAFV2` - `CAPTCHA` and `Challenge` configs   `"{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupArn\":null,\"overrideAction\":{\"type\":\"NONE\"},\"managedRuleGroupIdentifier\":{\"versionEnabled\":null,\"version\":null,\"vendorName\":\"AWS\",\"managedRuleGroupName\":\"AWSManagedRulesAdminProtectionRuleSet\"},\"ruleGroupType\":\"ManagedRuleGroup\",\"excludeRules\":[],\"sampledRequestsEnabled\":true}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"ALLOW\"},\"customRequestHandling\":null,\"customResponse\":null,\"overrideCustomerWebACLAssociation\":false,\"loggingConfiguration\":null,\"sampledRequestsEnabledForDefaultActions\":true,\"captchaConfig\":{\"immunityTimeProperty\":{\"immunityTime\":500}},\"challengeConfig\":{\"immunityTimeProperty\":{\"immunityTime\":800}},\"tokenDomains\":[\"google.com\",\"amazon.com\"],\"associationConfig\":{\"requestBody\":{\"CLOUDFRONT\":{\"defaultSizeInspectionLimit\":\"KB_16\"}}}}"`
- `CAPTCHA` and `Challenge` configs - If you update the policyâs values for `associationConfig` , `captchaConfig` , `challengeConfig` , or `tokenDomains` , Firewall Manager will overwrite your local web ACLs to contain the new value(s). However, if you donât update the policyâs `associationConfig` , `captchaConfig` , `challengeConfig` , or `tokenDomains` values, the values in your local web ACLs will remain unchanged. For information about association configs, see [AssociationConfig](https://docs.aws.amazon.com/waf/latest/APIReference/API_AssociationConfig.html) . For information about CAPTCHA and Challenge configs, see [CaptchaConfig](https://docs.aws.amazon.com/waf/latest/APIReference/API_CaptchaConfig.html) and [ChallengeConfig](https://docs.aws.amazon.com/waf/latest/APIReference/API_ChallengeConfig.html) in the *WAF API Reference* .
- `defaultSizeInspectionLimit` - Specifies the maximum size of the web request body component that an associated Amazon CloudFront distribution should send to WAF for inspection. For more information, see [DefaultSizeInspectionLimit](https://docs.aws.amazon.com/waf/latest/APIReference/API_RequestBodyAssociatedResourceTypeConfig.html#WAF-Type-RequestBodyAssociatedResourceTypeConfig-DefaultSizeInspectionLimit) in the *WAF API Reference* .
- Example: `WAFV2` - Firewall Manager support for WAF managed rule group versioning   `"{\"preProcessRuleGroups\":[{\"ruleGroupType\":\"ManagedRuleGroup\",\"overrideAction\":{\"type\":\"NONE\"},\"sampledRequestsEnabled\":true,\"managedRuleGroupIdentifier\":{\"managedRuleGroupName\":\"AWSManagedRulesAdminProtectionRuleSet\",\"vendorName\":\"AWS\",\"managedRuleGroupConfigs\":null}}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"ALLOW\"},\"customRequestHandling\":null,\"tokenDomains\":null,\"customResponse\":null,\"type\":\"WAFV2\",\"overrideCustomerWebACLAssociation\":false,\"sampledRequestsEnabledForDefaultActions\":true,\"optimizeUnassociatedWebACL\":true,\"webACLSource\":\"RETROFIT_EXISTING\"}"`   To use a specific version of a WAF managed rule group in your Firewall Manager policy, you must set `versionEnabled` to `true` , and set `version` to the version youâd like to use. If you donât set `versionEnabled` to `true` , or if you omit `versionEnabled` , then Firewall Manager uses the default version of the WAF managed rule group.
- Example: `WAFV2` - Logging configurations   `"{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupArn\":null, \"overrideAction\":{\"type\":\"NONE\"},\"managedRuleGroupIdentifier\": {\"versionEnabled\":null,\"version\":null,\"vendorName\":\"AWS\", \"managedRuleGroupName\":\"AWSManagedRulesAdminProtectionRuleSet\"} ,\"ruleGroupType\":\"ManagedRuleGroup\",\"excludeRules\":[], \"sampledRequestsEnabled\":true}],\"postProcessRuleGroups\":[], \"defaultAction\":{\"type\":\"ALLOW\"},\"customRequestHandling\" :null,\"customResponse\":null,\"overrideCustomerWebACLAssociation\" :false,\"loggingConfiguration\":{\"logDestinationConfigs\": [\"arn:aws:s3:::aws-waf-logs-example-bucket\"] ,\"redactedFields\":[],\"loggingFilterConfigs\":{\"defaultBehavior\":\"KEEP\", \"filters\":[{\"behavior\":\"KEEP\",\"requirement\":\"MEETS_ALL\", \"conditions\":[{\"actionCondition\":\"CAPTCHA\"},{\"actionCondition\": \"CHALLENGE\"}, {\"actionCondition\":\"EXCLUDED_AS_COUNT\"}]}]}},\"sampledRequestsEnabledForDefaultActions\":true}"`   Firewall Manager supports Amazon Kinesis Data Firehose and Amazon S3 as the `logDestinationConfigs` in your `loggingConfiguration` . For information about WAF logging configurations, see [LoggingConfiguration](https://docs.aws.amazon.com/waf/latest/APIReference/API_LoggingConfiguration.html) in the *WAF API Reference*   In the `loggingConfiguration` , you can specify one `logDestinationConfigs` . Optionally provide as many as 20 `redactedFields` . The `RedactedFieldType` must be one of `URI` , `QUERY_STRING` , `HEADER` , or `METHOD` .
- Example: `WAF Classic` `"{\"ruleGroups\":[{\"id\":\"78cb36c0-1b5e-4d7d-82b2-cf48d3ad9659\",\"overrideAction\":{\"type\":\"NONE\"}}],\"overrideCustomerWebACLAssociation\":true,\"defaultAction\":{\"type\":\"ALLOW\"},\"type\":\"WAF\"}"`

PolicyOption -> (structure)

Contains the settings to configure a network ACL policy, a Network Firewall firewall policy deployment model, or a third-party firewall policy.

NetworkFirewallPolicy -> (structure)

Defines the deployment model to use for the firewall policy.

FirewallDeploymentModel -> (string)

Defines the deployment model to use for the firewall policy. To use a distributed model, set [PolicyOption](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PolicyOption.html) to `NULL` .

ThirdPartyFirewallPolicy -> (structure)

Defines the policy options for a third-party firewall policy.

FirewallDeploymentModel -> (string)

Defines the deployment model to use for the third-party firewall policy.

NetworkAclCommonPolicy -> (structure)

Defines a Firewall Manager network ACL policy.

NetworkAclEntrySet -> (structure)

The definition of the first and last rules for the network ACL policy.

FirstEntries -> (list)

The rules that you want to run first in the Firewall Manager managed network ACLs.

### Note

Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.

You must specify at least one first entry or one last entry in any network ACL policy.

(structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

ForceRemediateForFirstEntries -> (boolean)

Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.

If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation) in the *Firewall Manager Developer Guide* .

LastEntries -> (list)

The rules that you want to run last in the Firewall Manager managed network ACLs.

### Note

Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates.

You must specify at least one first entry or one last entry in any network ACL policy.

(structure)

Describes a rule in a network ACL.

Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order.

When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.

IcmpTypeCode -> (structure)

ICMP protocol: The ICMP type and code.

Code -> (integer)

ICMP code.

Type -> (integer)

ICMP type.

Protocol -> (string)

The protocol number. A value of â-1â means all protocols.

PortRange -> (structure)

TCP or UDP protocols: The range of ports the rule applies to.

From -> (integer)

The beginning port number of the range.

To -> (integer)

The ending port number of the range.

CidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation.

Ipv6CidrBlock -> (string)

The IPv6 network range to allow or deny, in CIDR notation.

RuleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

Egress -> (boolean)

Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If itâs not an egress rule, then itâs an ingress, or inbound, rule.

ForceRemediateForLastEntries -> (boolean)

Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries.

If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation) in the *Firewall Manager Developer Guide* .

ResourceType -> (string)

The type of resource protected by or in scope of the policy. This is in the format shown in the [Amazon Web Services Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) . To apply this policy to multiple resource types, specify a resource type of `ResourceTypeList` and then specify the resource types in a `ResourceTypeList` .

The following are valid resource types for each Firewall Manager policy type:

- Amazon Web Services WAF Classic - `AWS::ApiGateway::Stage` , `AWS::CloudFront::Distribution` , and `AWS::ElasticLoadBalancingV2::LoadBalancer` .
- WAF - `AWS::ApiGateway::Stage` , `AWS::ElasticLoadBalancingV2::LoadBalancer` , and `AWS::CloudFront::Distribution` .
- Shield Advanced - `AWS::ElasticLoadBalancingV2::LoadBalancer` , `AWS::ElasticLoadBalancing::LoadBalancer` , `AWS::EC2::EIP` , and `AWS::CloudFront::Distribution` .
- Network ACL - `AWS::EC2::Subnet` .
- Security group usage audit - `AWS::EC2::SecurityGroup` .
- Security group content audit - `AWS::EC2::SecurityGroup` , `AWS::EC2::NetworkInterface` , and `AWS::EC2::Instance` .
- DNS Firewall, Network Firewall, and third-party firewall - `AWS::EC2::VPC` .

ResourceTypeList -> (list)

An array of `ResourceType` objects. Use this only to specify multiple resource types. To specify a single resource type, use `ResourceType` .

(string)

ResourceTags -> (list)

An array of `ResourceTag` objects.

(structure)

The resource tags that Firewall Manager uses to determine if a particular resource should be included or excluded from the Firewall Manager policy. Tags enable you to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value. If you add more than one tag to a policy, you can specify whether to combine them using the logical AND operator or the logical OR operator. For more information, see [Working with Tag Editor](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/tag-editor.html) .

Every resource tag must have a string value, either a non-empty string or an empty string. If you donât provide a value for a resource tag, Firewall Manager saves the value as an empty string: ââ. When Firewall Manager compares tags, it only matches two tags if they have the same key and the same value. A tag with an empty string value only matches with tags that also have an empty string value.

Key -> (string)

The resource tag key.

Value -> (string)

The resource tag value. To specify an empty string value, either donât provide this or specify it as ââ.

ExcludeResourceTags -> (boolean)

If set to `True` , resources with the tags that are specified in the `ResourceTag` array are not in scope of the policy. If set to `False` , and the `ResourceTag` array is not null, only resources with the specified tags are in scope of the policy.

RemediationEnabled -> (boolean)

Indicates if the policy should be automatically applied to new resources.

DeleteUnusedFMManagedResources -> (boolean)

Indicates whether Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.

By default, Firewall Manager doesnât remove protections or delete Firewall Manager managed resources.

This option is not available for Shield Advanced or WAF Classic policies.

IncludeMap -> (map)

Specifies the Amazon Web Services account IDs and Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

You can specify inclusions or exclusions, but not both. If you specify an `IncludeMap` , Firewall Manager applies the policy to all accounts specified by the `IncludeMap` , and does not evaluate any `ExcludeMap` specifications. If you do not specify an `IncludeMap` , then Firewall Manager applies the policy to all accounts except for those specified by the `ExcludeMap` .

You can specify account IDs, OUs, or a combination:

- Specify account IDs by setting the key to `ACCOUNT` . For example, the following is a valid map: `{âACCOUNTâ : [âaccountID1â, âaccountID2â]}` .
- Specify OUs by setting the key to `ORG_UNIT` . For example, the following is a valid map: `{âORG_UNITâ : [âouid111â, âouid112â]}` .
- Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{âACCOUNTâ : [âaccountID1â, âaccountID2â], âORG_UNITâ : [âouid111â, âouid112â]}` .

key -> (string)

value -> (list)

(string)

ExcludeMap -> (map)

Specifies the Amazon Web Services account IDs and Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.

You can specify inclusions or exclusions, but not both. If you specify an `IncludeMap` , Firewall Manager applies the policy to all accounts specified by the `IncludeMap` , and does not evaluate any `ExcludeMap` specifications. If you do not specify an `IncludeMap` , then Firewall Manager applies the policy to all accounts except for those specified by the `ExcludeMap` .

You can specify account IDs, OUs, or a combination:

- Specify account IDs by setting the key to `ACCOUNT` . For example, the following is a valid map: `{âACCOUNTâ : [âaccountID1â, âaccountID2â]}` .
- Specify OUs by setting the key to `ORG_UNIT` . For example, the following is a valid map: `{âORG_UNITâ : [âouid111â, âouid112â]}` .
- Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{âACCOUNTâ : [âaccountID1â, âaccountID2â], âORG_UNITâ : [âouid111â, âouid112â]}` .

key -> (string)

value -> (list)

(string)

ResourceSetIds -> (list)

The unique identifiers of the resource sets used by the policy.

(string)

PolicyDescription -> (string)

Your description of the Firewall Manager policy.

PolicyStatus -> (string)

Indicates whether the policy is in or out of an adminâs policy or Region scope.

- `ACTIVE` - The administrator can manage and delete the policy.
- `OUT_OF_ADMIN_SCOPE` - The administrator can view the policy, but they canât edit or delete the policy. Existing policy protections stay in place. Any new resources that come into scope of the policy wonât be protected.

ResourceTagLogicalOperator -> (string)

Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag.

Default: `AND`

PolicyArn -> (string)

The Amazon Resource Name (ARN) of the specified policy.