# update-organization-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-organization-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-organization-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# update-organization-configuration

## Description

Configures the delegated administrator account with the provided values. You must provide a value for either `autoEnableOrganizationMembers` or `autoEnable` , but not both.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING` ) and Runtime Monitoring (`RUNTIME_MONITORING` ) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) .

There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/UpdateOrganizationConfiguration)

## Synopsis

```
update-organization-configuration
--detector-id <value>
[--auto-enable | --no-auto-enable]
[--data-sources <value>]
[--features <value>]
[--auto-enable-organization-members <value>]
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

`--detector-id` (string)

The ID of the detector that configures the delegated administrator.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--auto-enable` | `--no-auto-enable` (boolean)

Represents whether to automatically enable member accounts in the organization. This applies to only new member accounts, not the existing member accounts. When a new account joins the organization, the chosen features will be enabled for them by default.

Even though this is still supported, we recommend using `AutoEnableOrganizationMembers` to achieve the similar results. You must provide a value for either `autoEnableOrganizationMembers` or `autoEnable` .

`--data-sources` (structure)

Describes which data sources will be updated.

S3Logs -> (structure)

Describes whether S3 data event logs are enabled for new members of the organization.

AutoEnable -> (boolean)

A value that contains information on whether S3 data event logs will be enabled automatically as a data source for the organization.

Kubernetes -> (structure)

Describes the configuration of Kubernetes data sources for new members of the organization.

AuditLogs -> (structure)

Whether Kubernetes audit logs data source should be auto-enabled for new members joining the organization.

AutoEnable -> (boolean)

A value that contains information on whether Kubernetes audit logs should be enabled automatically as a data source for the organization.

MalwareProtection -> (structure)

Describes the configuration of Malware Protection for new members of the organization.

ScanEc2InstanceWithFindings -> (structure)

Whether Malware Protection for EC2 instances with findings should be auto-enabled for new members joining the organization.

EbsVolumes -> (structure)

Whether scanning EBS volumes should be auto-enabled for new members joining the organization.

AutoEnable -> (boolean)

Whether scanning EBS volumes should be auto-enabled for new members joining the organization.

JSON Syntax:

```
{
  "S3Logs": {
    "AutoEnable": true|false
  },
  "Kubernetes": {
    "AuditLogs": {
      "AutoEnable": true|false
    }
  },
  "MalwareProtection": {
    "ScanEc2InstanceWithFindings": {
      "EbsVolumes": {
        "AutoEnable": true|false
      }
    }
  }
}
```

`--features` (list)

A list of features that will be configured for the organization.

(structure)

A list of features which will be configured for the organization.

Name -> (string)

The name of the feature that will be configured for the organization.

AutoEnable -> (string)

Describes the status of the feature that is configured for the member accounts within the organization. One of the following values is the status for the entire organization:

- `NEW` : Indicates that when a new account joins the organization, they will have the feature enabled automatically.
- `ALL` : Indicates that all accounts in the organization have the feature enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty. It may take up to 24 hours to update the configuration for all the member accounts.
- `NONE` : Indicates that the feature will not be automatically enabled for any account in the organization. The administrator must manage the feature for each account individually.

AdditionalConfiguration -> (list)

The additional information that will be configured for the organization.

(structure)

A list of additional configurations which will be configured for the organization.

Additional configuration applies to only GuardDuty Runtime Monitoring protection plan.

Name -> (string)

The name of the additional configuration that will be configured for the organization. These values are applicable to only Runtime Monitoring protection plan.

AutoEnable -> (string)

The status of the additional configuration that will be configured for the organization. Use one of the following values to configure the feature status for the entire organization:

- `NEW` : Indicates that when a new account joins the organization, they will have the additional configuration enabled automatically.
- `ALL` : Indicates that all accounts in the organization have the additional configuration enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty. It may take up to 24 hours to update the configuration for all the member accounts.
- `NONE` : Indicates that the additional configuration will not be automatically enabled for any account in the organization. The administrator must manage the additional configuration for each account individually.

Shorthand Syntax:

```
Name=string,AutoEnable=string,AdditionalConfiguration=[{Name=string,AutoEnable=string},{Name=string,AutoEnable=string}] ...
```

JSON Syntax:

```
[
  {
    "Name": "S3_DATA_EVENTS"|"EKS_AUDIT_LOGS"|"EBS_MALWARE_PROTECTION"|"RDS_LOGIN_EVENTS"|"EKS_RUNTIME_MONITORING"|"LAMBDA_NETWORK_LOGS"|"RUNTIME_MONITORING",
    "AutoEnable": "NEW"|"NONE"|"ALL",
    "AdditionalConfiguration": [
      {
        "Name": "EKS_ADDON_MANAGEMENT"|"ECS_FARGATE_AGENT_MANAGEMENT"|"EC2_AGENT_MANAGEMENT",
        "AutoEnable": "NEW"|"NONE"|"ALL"
      }
      ...
    ]
  }
  ...
]
```

`--auto-enable-organization-members` (string)

Indicates the auto-enablement configuration of GuardDuty for the member accounts in the organization. You must provide a value for either `autoEnableOrganizationMembers` or `autoEnable` .

Use one of the following configuration values for `autoEnableOrganizationMembers` :

- `NEW` : Indicates that when a new account joins the organization, they will have GuardDuty enabled automatically.
- `ALL` : Indicates that all accounts in the organization have GuardDuty enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty. It may take up to 24 hours to update the configuration for all the member accounts.
- `NONE` : Indicates that GuardDuty will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually. When you update the auto-enable setting from `ALL` or `NEW` to `NONE` , this action doesnât disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.

Possible values:

- `NEW`
- `ALL`
- `NONE`

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

None