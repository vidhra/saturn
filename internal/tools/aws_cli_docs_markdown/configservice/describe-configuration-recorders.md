# describe-configuration-recordersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# describe-configuration-recorders

## Description

Returns details for the configuration recorder you specify.

If a configuration recorder is not specified, this operation returns details for the customer managed configuration recorder configured for the account, if applicable.

### Note

When making a request to this operation, you can only specify one configuration recorder.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeConfigurationRecorders)

## Synopsis

```
describe-configuration-recorders
[--configuration-recorder-names <value>]
[--service-principal <value>]
[--arn <value>]
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

`--configuration-recorder-names` (list)

A list of names of the configuration recorders that you want to specify.

(string)

Syntax:

```
"string" "string" ...
```

`--service-principal` (string)

For service-linked configuration recorders, you can use the service principal of the linked Amazon Web Services service to specify the configuration recorder.

`--arn` (string)

The Amazon Resource Name (ARN) of the configuration recorder that you want to specify.

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

**To get details about the configuration recorder**

The following command returns details about the default configuration recorder:

```
aws configservice describe-configuration-recorders
```

Output:

```
{
    "ConfigurationRecorders": [
        {
            "recordingGroup": {
                "allSupported": true,
                "resourceTypes": [],
                "includeGlobalResourceTypes": true
            },
            "roleARN": "arn:aws:iam::123456789012:role/config-ConfigRole-A1B2C3D4E5F6",
            "name": "default"
        }
    ]
}
```

## Output

ConfigurationRecorders -> (list)

A list that contains the descriptions of the specified configuration recorders.

(structure)

Records configuration changes to the resource types in scope.

For more information about the configuration recorder, see ` **Working with the Configuration Recorder** [https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder](https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder).html`__ in the *Config Developer Guide* .

arn -> (string)

The Amazon Resource Name (ARN) of the specified configuration recorder.

name -> (string)

The name of the configuration recorder.

For customer managed configuration recorders, Config automatically assigns the name of âdefaultâ when creating a configuration recorder if you do not specify a name at creation time.

For service-linked configuration recorders, Config automatically assigns a name that has the prefix â`AWS` â to a new service-linked configuration recorder.

### Note

**Changing the name of a configuration recorder**

To change the name of the customer managed configuration recorder, you must delete it and create a new customer managed configuration recorder with a new name.

You cannot change the name of a service-linked configuration recorder.

roleARN -> (string)

The Amazon Resource Name (ARN) of the IAM role assumed by Config and used by the specified configuration recorder.

### Note

**The server will reject a request without a defined ``roleARN`` for the configuration recorder**

While the API model does not require this field, the server will reject a request without a defined `roleARN` for the configuration recorder.

**Policies and compliance results**

[IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) and [other policies managed in Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html) can impact whether Config has permissions to record configuration changes for your resources. Additionally, rules directly evaluate the configuration of a resource and rules donât take into account these policies when running evaluations. Make sure that the policies in effect align with how you intend to use Config.

**Keep Minimum Permisions When Reusing an IAM role**

If you use an Amazon Web Services service that uses Config, such as Security Hub or Control Tower, and an IAM role has already been created, make sure that the IAM role that you use when setting up Config keeps the same minimum permissions as the pre-existing IAM role. You must do this to ensure that the other Amazon Web Services service continues to run as expected.

For example, if Control Tower has an IAM role that allows Config to read S3 objects, make sure that the same permissions are granted to the IAM role you use when setting up Config. Otherwise, it may interfere with how Control Tower operates.

**The service-linked IAM role for Config must be used for service-linked configuration recorders**

For service-linked configuration recorders, you must use the service-linked IAM role for Config: [AWSServiceRoleForConfig](https://docs.aws.amazon.com/config/latest/developerguide/using-service-linked-roles.html) .

recordingGroup -> (structure)

Specifies which resource types are in scope for the configuration recorder to record.

### Note

**High Number of Config Evaluations**

You might notice increased activity in your account during your initial month recording with Config when compared to subsequent months. During the initial bootstrapping process, Config runs evaluations on all the resources in your account that you have selected for Config to record.

If you are running ephemeral workloads, you may see increased activity from Config as it records configuration changes associated with creating and deleting these temporary resources. An *ephemeral workload* is a temporary use of computing resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances, Amazon EMR jobs, and Auto Scaling.

If you want to avoid the increased activity from running ephemeral workloads, you can set up the configuration recorder to exclude these resource types from being recorded, or run these types of workloads in a separate account with Config turned off to avoid increased configuration recording and rule evaluations.

allSupported -> (boolean)

Specifies whether Config records configuration changes for all supported resource types, excluding the global IAM resource types.

If you set this field to `true` , when Config adds support for a new resource type, Config starts recording resources of that type automatically.

If you set this field to `true` , you cannot enumerate specific resource types to record in the `resourceTypes` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) , or to exclude in the `resourceTypes` field of [ExclusionByResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html) .

### Note

**Region availability**

Check [Resource Coverage by Region Availability](https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html) to see if a resource type is supported in the Amazon Web Services Region where you set up Config.

includeGlobalResourceTypes -> (boolean)

This option is a bundle which only applies to the global IAM resource types: IAM users, groups, roles, and customer managed policies. These global IAM resource types can only be recorded by Config in Regions where Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by Config after February 2022. For a list of those Regions, see [Recording Amazon Web Services Resources | Global Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all) .

### Warning

**Aurora global clusters are recorded in all enabled Regions**

The `AWS::RDS::GlobalCluster` resource type will be recorded in all supported Config Regions where the configuration recorder is enabled, even if `includeGlobalResourceTypes` is set``false`` . The `includeGlobalResourceTypes` option is a bundle which only applies to IAM users, groups, roles, and customer managed policies.

If you do not want to record `AWS::RDS::GlobalCluster` in all enabled Regions, use one of the following recording strategies:

- **Record all current and future resource types with exclusions** (`EXCLUSION_BY_RESOURCE_TYPES` ), or
- **Record specific resource types** (`INCLUSION_BY_RESOURCE_TYPES` ).

For more information, see [Selecting Which Resources are Recorded](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all) in the *Config developer guide* .

### Warning

**includeGlobalResourceTypes and the exclusion recording strategy**

The `includeGlobalResourceTypes` field has no impact on the `EXCLUSION_BY_RESOURCE_TYPES` recording strategy. This means that the global IAM resource types (IAM users, groups, roles, and customer managed policies) will not be automatically added as exclusions for `exclusionByResourceTypes` when `includeGlobalResourceTypes` is set to `false` .

The `includeGlobalResourceTypes` field should only be used to modify the `AllSupported` field, as the default for the `AllSupported` field is to record configuration changes for all supported resource types excluding the global IAM resource types. To include the global IAM resource types when `AllSupported` is set to `true` , make sure to set `includeGlobalResourceTypes` to `true` .

To exclude the global IAM resource types for the `EXCLUSION_BY_RESOURCE_TYPES` recording strategy, you need to manually add them to the `resourceTypes` field of `exclusionByResourceTypes` .

### Note

**Required and optional fields**

Before you set this field to `true` , set the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true` . Optionally, you can set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `ALL_SUPPORTED_RESOURCE_TYPES` .

### Note

**Overriding fields**

If you set this field to `false` but list global IAM resource types in the `resourceTypes` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) , Config will still record configuration changes for those specified resource types *regardless* of if you set the `includeGlobalResourceTypes` field to false.

If you do not want to record configuration changes to the global IAM resource types (IAM users, groups, roles, and customer managed policies), make sure to not list them in the `resourceTypes` field in addition to setting the `includeGlobalResourceTypes` field to false.

resourceTypes -> (list)

A comma-separated list that specifies which resource types Config records.

For a list of valid `resourceTypes` values, see the **Resource Type Value** column in [Supported Amazon Web Services resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources) in the *Config developer guide* .

### Note

**Required and optional fields**

Optionally, you can set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `INCLUSION_BY_RESOURCE_TYPES` .

To record all configuration changes, set the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true` , and either omit this field or donât specify any resource types in this field. If you set the `allSupported` field to `false` and specify values for `resourceTypes` , when Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group.

### Note

**Region availability**

Before specifying a resource type for Config to track, check [Resource Coverage by Region Availability](https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html) to see if the resource type is supported in the Amazon Web Services Region where you set up Config. If a resource type is supported by Config in at least one Region, you can enable the recording of that resource type in all Regions supported by Config, even if the specified resource type is not supported in the Amazon Web Services Region where you set up Config.

(string)

exclusionByResourceTypes -> (structure)

An object that specifies how Config excludes resource types from being recorded by the configuration recorder.

### Note

**Required fields**

To use this option, you must set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `EXCLUSION_BY_RESOURCE_TYPES` .

resourceTypes -> (list)

A comma-separated list of resource types to exclude from recording by the configuration recorder.

(string)

recordingStrategy -> (structure)

An object that specifies the recording strategy for the configuration recorder.

- If you set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `ALL_SUPPORTED_RESOURCE_TYPES` , Config records configuration changes for all supported resource types, excluding the global IAM resource types. You also must set the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true` . When Config adds support for a new resource type, Config automatically starts recording resources of that type.
- If you set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `INCLUSION_BY_RESOURCE_TYPES` , Config records configuration changes for only the resource types you specify in the `resourceTypes` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) .
- If you set the `useOnly` field of [RecordingStrategy](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html) to `EXCLUSION_BY_RESOURCE_TYPES` , Config records configuration changes for all supported resource types except the resource types that you specify to exclude from being recorded in the `resourceTypes` field of [ExclusionByResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html) .

### Note

**Required and optional fields**

The `recordingStrategy` field is optional when you set the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true` .

The `recordingStrategy` field is optional when you list resource types in the `resourceTypes` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) .

The `recordingStrategy` field is required if you list resource types to exclude from recording in the `resourceTypes` field of [ExclusionByResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html) .

### Note

**Overriding fields**

If you choose `EXCLUSION_BY_RESOURCE_TYPES` for the recording strategy, the `exclusionByResourceTypes` field will override other properties in the request.

For example, even if you set `includeGlobalResourceTypes` to false, global IAM resource types will still be automatically recorded in this option unless those resource types are specifically listed as exclusions in the `resourceTypes` field of `exclusionByResourceTypes` .

### Note

**Global resources types and the resource exclusion recording strategy**

By default, if you choose the `EXCLUSION_BY_RESOURCE_TYPES` recording strategy, when Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, Config starts recording resources of that type automatically.

Unless specifically listed as exclusions, `AWS::RDS::GlobalCluster` will be recorded automatically in all supported Config Regions were the configuration recorder is enabled.

IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by Config after February 2022. For a list of those Regions, see [Recording Amazon Web Services Resources | Global Resources](https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all) .

useOnly -> (string)

The recording strategy for the configuration recorder.

- If you set this option to `ALL_SUPPORTED_RESOURCE_TYPES` , Config records configuration changes for all supported resource types, excluding the global IAM resource types. You also must set the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true` . When Config adds support for a new resource type, Config automatically starts recording resources of that type. For a list of supported resource types, see [Supported Resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources) in the *Config developer guide* .
- If you set this option to `INCLUSION_BY_RESOURCE_TYPES` , Config records configuration changes for only the resource types that you specify in the `resourceTypes` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) .
- If you set this option to `EXCLUSION_BY_RESOURCE_TYPES` , Config records configuration changes for all supported resource types, except the resource types that you specify to exclude from being recorded in the `resourceTypes` field of [ExclusionByResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html) .

### Note

**Required and optional fields**

The `recordingStrategy` field is optional when you set the `allSupported` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) to `true` .

The `recordingStrategy` field is optional when you list resource types in the `resourceTypes` field of [RecordingGroup](https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html) .

The `recordingStrategy` field is required if you list resource types to exclude from recording in the `resourceTypes` field of [ExclusionByResourceTypes](https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html) .

### Note

**Overriding fields**

If you choose `EXCLUSION_BY_RESOURCE_TYPES` for the recording strategy, the `exclusionByResourceTypes` field will override other properties in the request.

For example, even if you set `includeGlobalResourceTypes` to false, global IAM resource types will still be automatically recorded in this option unless those resource types are specifically listed as exclusions in the `resourceTypes` field of `exclusionByResourceTypes` .

### Note

**Global resource types and the exclusion recording strategy**

By default, if you choose the `EXCLUSION_BY_RESOURCE_TYPES` recording strategy, when Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, Config starts recording resources of that type automatically.

Unless specifically listed as exclusions, `AWS::RDS::GlobalCluster` will be recorded automatically in all supported Config Regions were the configuration recorder is enabled.

IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions:

- Asia Pacific (Hyderabad)
- Asia Pacific (Melbourne)
- Canada West (Calgary)
- Europe (Spain)
- Europe (Zurich)
- Israel (Tel Aviv)
- Middle East (UAE)

recordingMode -> (structure)

Specifies the default recording frequency for the configuration recorder. Config supports *Continuous recording* and *Daily recording* .

- Continuous recording allows you to record configuration changes continuously whenever a change occurs.
- Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if itâs different from the previous CI recorded.

### Note

**Some resource types require continuous recording**

Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

You can also override the recording frequency for specific resource types.

recordingFrequency -> (string)

The default recording frequency that Config uses to record configuration changes.

### Warning

Daily recording cannot be specified for the following resource types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`

For the **allSupported** (`ALL_SUPPORTED_RESOURCE_TYPES` ) recording strategy, these resource types will be set to Continuous recording.

recordingModeOverrides -> (list)

An array of `recordingModeOverride` objects for you to specify your overrides for the recording mode. The `recordingModeOverride` object in the `recordingModeOverrides` array consists of three fields: a `description` , the new `recordingFrequency` , and an array of `resourceTypes` to override.

(structure)

An object for you to specify your overrides for the recording mode.

description -> (string)

A description that you provide for the override.

resourceTypes -> (list)

A comma-separated list that specifies which resource types Config includes in the override.

### Warning

Daily recording cannot be specified for the following resource types:

- `AWS::Config::ResourceCompliance`
- `AWS::Config::ConformancePackCompliance`
- `AWS::Config::ConfigurationRecorder`

(string)

recordingFrequency -> (string)

The recording frequency that will be applied to all the resource types specified in the override.

- Continuous recording allows you to record configuration changes continuously whenever a change occurs.
- Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if itâs different from the previous CI recorded.

### Note

Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

recordingScope -> (string)

Specifies whether the [ConfigurationItems](https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html) in scope for the specified configuration recorder are recorded for free (`INTERNAL` ) or if it impacts the costs to your bill (`PAID` ).

servicePrincipal -> (string)

For service-linked configuration recorders, specifies the linked Amazon Web Services service for the configuration recorder.