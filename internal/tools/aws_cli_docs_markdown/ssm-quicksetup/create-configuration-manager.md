# create-configuration-managerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-quicksetup/create-configuration-manager.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-quicksetup/create-configuration-manager.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-quicksetup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-quicksetup/index.html#cli-aws-ssm-quicksetup) ]

# create-configuration-manager

## Description

Creates a Quick Setup configuration manager resource. This object is a collection of desired state configurations for multiple configuration definitions and summaries describing the deployments of those definitions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-quicksetup-2018-05-10/CreateConfigurationManager)

## Synopsis

```
create-configuration-manager
--configuration-definitions <value>
[--description <value>]
[--name <value>]
[--tags <value>]
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

`--configuration-definitions` (list)

The definition of the Quick Setup configuration that the configuration manager deploys.

(structure)

Defines the preferences and options for a configuration definition.

LocalDeploymentAdministrationRoleArn -> (string)

The ARN of the IAM role used to administrate local configuration deployments.

LocalDeploymentExecutionRoleName -> (string)

The name of the IAM role used to deploy local configurations.

Parameters -> (map)

The parameters for the configuration definition type. Parameters for configuration definitions vary based the configuration type. The following tables outline the parameters for each configuration type.

OpsCenter (Type: Amazon Web ServicesQuickSetupType-SSMOpsCenter)

- `DelegatedAccountId`

- Description: (Required) The ID of the delegated administrator account.
- `TargetOrganizationalUnits`

- Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Resource Scheduler (Type: Amazon Web ServicesQuickSetupType-Scheduler)
- `TargetTagKey`

- Description: (Required) The tag key assigned to the instances you want to target.
- `TargetTagValue`

- Description: (Required) The value of the tag key assigned to the instances you want to target.
- `ICalendarString`

- Description: (Required) An iCalendar formatted string containing the schedule you want Change Manager to use.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Default Host Management Configuration (Type: Amazon Web ServicesQuickSetupType-DHMC)
- `UpdateSSMAgent`

- Description: (Optional) A boolean value that determines whether the SSM Agent is updated on the target instances every 2 weeks. The default value is â`true` â.
- `TargetOrganizationalUnits`

- Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Resource Explorer (Type: Amazon Web ServicesQuickSetupType-ResourceExplorer)
- `SelectedAggregatorRegion`

- Description: (Required) The Amazon Web Services Region where you want to create the aggregator index.
- `ReplaceExistingAggregator`

- Description: (Required) A boolean value that determines whether to demote an existing aggregator if it is in a Region that differs from the value you specify for the `SelectedAggregatorRegion` .
- `TargetOrganizationalUnits`

- Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Change Manager (Type: Amazon Web ServicesQuickSetupType-SSMChangeMgr)
- `DelegatedAccountId`

- Description: (Required) The ID of the delegated administrator account.
- `JobFunction`

- Description: (Required) The name for the Change Manager job function.
- `PermissionType`

- Description: (Optional) Specifies whether you want to use default administrator permissions for the job function role, or provide a custom IAM policy. The valid values are `CustomPermissions` and `AdminPermissions` . The default value for the parameter is `CustomerPermissions` .
- `CustomPermissions`

- Description: (Optional) A JSON string containing the IAM policy you want your job function to use. You must provide a value for this parameter if you specify `CustomPermissions` for the `PermissionType` parameter.
- `TargetOrganizationalUnits`

- Description: (Required) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

DevOps Guru (Type: Amazon Web ServicesQuickSetupType-DevOpsGuru)
- `AnalyseAllResources`

- Description: (Optional) A boolean value that determines whether DevOps Guru analyzes all CloudFormation stacks in the account. The default value is â`false` â.
- `EnableSnsNotifications`

- Description: (Optional) A boolean value that determines whether DevOps Guru sends notifications when an insight is created. The default value is â`true` â.
- `EnableSsmOpsItems`

- Description: (Optional) A boolean value that determines whether DevOps Guru creates an OpsCenter OpsItem when an insight is created. The default value is â`true` â.
- `EnableDriftRemediation`

- Description: (Optional) A boolean value that determines whether a drift remediation schedule is used. The default value is â`false` â.
- `RemediationSchedule`

- Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are `rate(30 days)` , `rate(14 days)` , `rate(1 days)` , and `none` . The default value is â`none` â.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Conformance Packs (Type: Amazon Web ServicesQuickSetupType-CFGCPacks)
- `DelegatedAccountId`

- Description: (Optional) The ID of the delegated administrator account. This parameter is required for Organization deployments.
- `RemediationSchedule`

- Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are `rate(30 days)` , `rate(14 days)` , `rate(2 days)` , and `none` . The default value is â`none` â.
- `CPackNames`

- Description: (Required) A comma separated list of Config conformance packs.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) The ID of the root of your Organization. This configuration type doesnât currently support choosing specific OUs. The configuration will be deployed to all the OUs in the Organization.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Config Recording (Type: Amazon Web ServicesQuickSetupType-CFGRecording)
- `RecordAllResources`

- Description: (Optional) A boolean value that determines whether all supported resources are recorded. The default value is â`true` â.
- `ResourceTypesToRecord`

- Description: (Optional) A comma separated list of resource types you want to record.
- `RecordGlobalResourceTypes`

- Description: (Optional) A boolean value that determines whether global resources are recorded with all resource configurations. The default value is â`false` â.
- `GlobalResourceTypesRegion`

- Description: (Optional) Determines the Amazon Web Services Region where global resources are recorded.
- `UseCustomBucket`

- Description: (Optional) A boolean value that determines whether a custom Amazon S3 bucket is used for delivery. The default value is â`false` â.
- `DeliveryBucketName`

- Description: (Optional) The name of the Amazon S3 bucket you want Config to deliver configuration snapshots and configuration history files to.
- `DeliveryBucketPrefix`

- Description: (Optional) The key prefix you want to use in the custom Amazon S3 bucket.
- `NotificationOptions`

- Description: (Optional) Determines the notification configuration for the recorder. The valid values are `NoStreaming` , `UseExistingTopic` , and `CreateTopic` . The default value is `NoStreaming` .
- `CustomDeliveryTopicAccountId`

- Description: (Optional) The ID of the Amazon Web Services account where the Amazon SNS topic you want to use for notifications resides. You must specify a value for this parameter if you use the `UseExistingTopic` notification option.
- `CustomDeliveryTopicName`

- Description: (Optional) The name of the Amazon SNS topic you want to use for notifications. You must specify a value for this parameter if you use the `UseExistingTopic` notification option.
- `RemediationSchedule`

- Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are `rate(30 days)` , `rate(7 days)` , `rate(1 days)` , and `none` . The default value is â`none` â.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) The ID of the root of your Organization. This configuration type doesnât currently support choosing specific OUs. The configuration will be deployed to all the OUs in the Organization.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Host Management (Type: Amazon Web ServicesQuickSetupType-SSMHostMgmt)
- `UpdateSSMAgent`

- Description: (Optional) A boolean value that determines whether the SSM Agent is updated on the target instances every 2 weeks. The default value is â`true` â.
- `UpdateEc2LaunchAgent`

- Description: (Optional) A boolean value that determines whether the EC2 Launch agent is updated on the target instances every month. The default value is â`false` â.
- `CollectInventory`

- Description: (Optional) A boolean value that determines whether the EC2 Launch agent is updated on the target instances every month. The default value is â`true` â.
- `ScanInstances`

- Description: (Optional) A boolean value that determines whether the target instances are scanned daily for available patches. The default value is â`true` â.
- `InstallCloudWatchAgent`

- Description: (Optional) A boolean value that determines whether the Amazon CloudWatch agent is installed on the target instances. The default value is â`false` â.
- `UpdateCloudWatchAgent`

- Description: (Optional) A boolean value that determines whether the Amazon CloudWatch agent is updated on the target instances every month. The default value is â`false` â.
- `IsPolicyAttachAllowed`

- Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is â`false` â.
- `TargetType`

- Description: (Optional) Determines how instances are targeted for local account deployments. Donât specify a value for this parameter if youâre deploying to OUs. The valid values are `*` , `InstanceIds` , `ResourceGroups` , and `Tags` . Use `*` to target all instances in the account.
- `TargetInstances`

- Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify `InstanceIds` for the `TargetType` parameter.
- `TargetTagKey`

- Description: (Optional) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify `Tags` for the `TargetType` parameter.
- `TargetTagValue`

- Description: (Optional) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify `Tags` for the `TargetType` parameter.
- `ResourceGroupName`

- Description: (Optional) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify `ResourceGroups` for the `TargetType` parameter.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Distributor (Type: Amazon Web ServicesQuickSetupType-Distributor)
- `PackagesToInstall`

- Description: (Required) A comma separated list of packages you want to install on the target instances. The valid values are `AWSEFSTools` , `AWSCWAgent` , and `AWSEC2LaunchAgent` .
- `RemediationSchedule`

- Description: (Optional) A rate expression that defines the schedule for drift remediation. The valid values are `rate(30 days)` , `rate(14 days)` , `rate(2 days)` , and `none` . The default value is â`rate(30 days)` â.
- `IsPolicyAttachAllowed`

- Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is â`false` â.
- `TargetType`

- Description: (Optional) Determines how instances are targeted for local account deployments. Donât specify a value for this parameter if youâre deploying to OUs. The valid values are `*` , `InstanceIds` , `ResourceGroups` , and `Tags` . Use `*` to target all instances in the account.
- `TargetInstances`

- Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify `InstanceIds` for the `TargetType` parameter.
- `TargetTagKey`

- Description: (Required) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify `Tags` for the `TargetType` parameter.
- `TargetTagValue`

- Description: (Required) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify `Tags` for the `TargetType` parameter.
- `ResourceGroupName`

- Description: (Required) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify `ResourceGroups` for the `TargetType` parameter.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

Patch Policy (Type: Amazon Web ServicesQuickSetupType-PatchPolicy)
- `PatchPolicyName`

- Description: (Required) A name for the patch policy. The value you provide is applied to target Amazon EC2 instances as a tag.
- `SelectedPatchBaselines`

- Description: (Required) An array of JSON objects containing the information for the patch baselines to include in your patch policy.
- `PatchBaselineUseDefault`

- Description: (Optional) A boolean value that determines whether the selected patch baselines are all Amazon Web Services provided.
- `ConfigurationOptionsPatchOperation`

- Description: (Optional) Determines whether target instances scan for available patches, or scan and install available patches. The valid values are `Scan` and `ScanAndInstall` . The default value for the parameter is `Scan` .
- `ConfigurationOptionsScanValue`

- Description: (Optional) A cron expression that is used as the schedule for when instances scan for available patches.
- `ConfigurationOptionsInstallValue`

- Description: (Optional) A cron expression that is used as the schedule for when instances install available patches.
- `ConfigurationOptionsScanNextInterval`

- Description: (Optional) A boolean value that determines whether instances should scan for available patches at the next cron interval. The default value is â`false` â.
- `ConfigurationOptionsInstallNextInterval`

- Description: (Optional) A boolean value that determines whether instances should scan for available patches at the next cron interval. The default value is â`false` â.
- `RebootOption`

- Description: (Optional) Determines whether instances are rebooted after patches are installed. Valid values are `RebootIfNeeded` and `NoReboot` .
- `IsPolicyAttachAllowed`

- Description: (Optional) A boolean value that determines whether Quick Setup attaches policies to instances profiles already associated with the target instances. The default value is â`false` â.
- `OutputLogEnableS3`

- Description: (Optional) A boolean value that determines whether command output logs are sent to Amazon S3.
- `OutputS3Location`

- Description: (Optional) A JSON string containing information about the Amazon S3 bucket where you want to store the output details of the request.
- `OutputS3BucketRegion`
- Description: (Optional) The Amazon Web Services Region where the Amazon S3 bucket you want Config to deliver command output to is located.
- `OutputS3BucketName`
- Description: (Optional) The name of the Amazon S3 bucket you want Config to deliver command output to.
- `OutputS3KeyPrefix`
- Description: (Optional) The key prefix you want to use in the custom Amazon S3 bucket.
- `TargetType`

- Description: (Optional) Determines how instances are targeted for local account deployments. Donât specify a value for this parameter if youâre deploying to OUs. The valid values are `*` , `InstanceIds` , `ResourceGroups` , and `Tags` . Use `*` to target all instances in the account.
- `TargetInstances`

- Description: (Optional) A comma separated list of instance IDs. You must provide a value for this parameter if you specify `InstanceIds` for the `TargetType` parameter.
- `TargetTagKey`

- Description: (Required) The tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify `Tags` for the `TargetType` parameter.
- `TargetTagValue`

- Description: (Required) The value of the tag key assigned to the instances you want to target. You must provide a value for this parameter if you specify `Tags` for the `TargetType` parameter.
- `ResourceGroupName`

- Description: (Required) The name of the resource group associated with the instances you want to target. You must provide a value for this parameter if you specify `ResourceGroups` for the `TargetType` parameter.
- `TargetAccounts`

- Description: (Optional) The ID of the Amazon Web Services account initiating the configuration deployment. You only need to provide a value for this parameter if you want to deploy the configuration locally. A value must be provided for either `TargetAccounts` or `TargetOrganizationalUnits` .
- `TargetOrganizationalUnits`

- Description: (Optional) A comma separated list of organizational units (OUs) you want to deploy the configuration to.
- `TargetRegions`

- Description: (Required) A comma separated list of Amazon Web Services Regions you want to deploy the configuration to.

key -> (string)

value -> (string)

Type -> (string)

The type of the Quick Setup configuration.

TypeVersion -> (string)

The version of the Quick Setup type to use.

Shorthand Syntax:

```
LocalDeploymentAdministrationRoleArn=string,LocalDeploymentExecutionRoleName=string,Parameters={KeyName1=string,KeyName2=string},Type=string,TypeVersion=string ...
```

JSON Syntax:

```
[
  {
    "LocalDeploymentAdministrationRoleArn": "string",
    "LocalDeploymentExecutionRoleName": "string",
    "Parameters": {"string": "string"
      ...},
    "Type": "string",
    "TypeVersion": "string"
  }
  ...
]
```

`--description` (string)

A description of the configuration manager.

`--name` (string)

A name for the configuration manager.

`--tags` (map)

Key-value pairs of metadata to assign to the configuration manager.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

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

## Output

ManagerArn -> (string)

The ARN for the newly created configuration manager.