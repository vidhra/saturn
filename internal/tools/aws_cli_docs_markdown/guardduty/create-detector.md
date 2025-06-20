# create-detectorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# create-detector

## Description

Creates a single GuardDuty detector. A detector is a resource that represents the GuardDuty service. To start using GuardDuty, you must create a detector in each Region where you enable the service. You can have only one detector per account per Region. All data sources are enabled in a new detector by default.

- When you donât specify any `features` , with an exception to `RUNTIME_MONITORING` , all the optional features are enabled by default.
- When you specify some of the `features` , any feature that is not specified in the API call gets enabled by default, with an exception to `RUNTIME_MONITORING` .

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING` ) and Runtime Monitoring (`RUNTIME_MONITORING` ) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) .

There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/CreateDetector)

## Synopsis

```
create-detector
--enable | --no-enable
[--client-token <value>]
[--finding-publishing-frequency <value>]
[--data-sources <value>]
[--tags <value>]
[--features <value>]
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

`--enable` | `--no-enable` (boolean)

A Boolean value that specifies whether the detector is to be enabled.

`--client-token` (string)

The idempotency token for the create request.

`--finding-publishing-frequency` (string)

A value that specifies how frequently updated findings are exported.

Possible values:

- `FIFTEEN_MINUTES`
- `ONE_HOUR`
- `SIX_HOURS`

`--data-sources` (structure)

Describes which data sources will be enabled for the detector.

There might be regional differences because some data sources might not be available in all the Amazon Web Services Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html) .

S3Logs -> (structure)

Describes whether S3 data event logs are enabled as a data source.

Enable -> (boolean)

The status of S3 data event logs as a data source.

Kubernetes -> (structure)

Describes whether any Kubernetes logs are enabled as data sources.

AuditLogs -> (structure)

The status of Kubernetes audit logs as a data source.

Enable -> (boolean)

The status of Kubernetes audit logs as a data source.

MalwareProtection -> (structure)

Describes whether Malware Protection is enabled as a data source.

ScanEc2InstanceWithFindings -> (structure)

Describes the configuration of Malware Protection for EC2 instances with findings.

EbsVolumes -> (boolean)

Describes the configuration for scanning EBS volumes as data source.

Shorthand Syntax:

```
S3Logs={Enable=boolean},Kubernetes={AuditLogs={Enable=boolean}},MalwareProtection={ScanEc2InstanceWithFindings={EbsVolumes=boolean}}
```

JSON Syntax:

```
{
  "S3Logs": {
    "Enable": true|false
  },
  "Kubernetes": {
    "AuditLogs": {
      "Enable": true|false
    }
  },
  "MalwareProtection": {
    "ScanEc2InstanceWithFindings": {
      "EbsVolumes": true|false
    }
  }
}
```

`--tags` (map)

The tags to be added to a new detector resource.

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

`--features` (list)

A list of features that will be configured for the detector.

(structure)

Contains information about a GuardDuty feature.

Specifying both EKS Runtime Monitoring (`EKS_RUNTIME_MONITORING` ) and Runtime Monitoring (`RUNTIME_MONITORING` ) will cause an error. You can add only one of these two features because Runtime Monitoring already includes the threat detection for Amazon EKS resources. For more information, see [Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) .

Name -> (string)

The name of the feature.

Status -> (string)

The status of the feature.

AdditionalConfiguration -> (list)

Additional configuration for a resource.

(structure)

Information about the additional configuration for a feature in your GuardDuty account.

Name -> (string)

Name of the additional configuration.

Status -> (string)

Status of the additional configuration.

Shorthand Syntax:

```
Name=string,Status=string,AdditionalConfiguration=[{Name=string,Status=string},{Name=string,Status=string}] ...
```

JSON Syntax:

```
[
  {
    "Name": "S3_DATA_EVENTS"|"EKS_AUDIT_LOGS"|"EBS_MALWARE_PROTECTION"|"RDS_LOGIN_EVENTS"|"EKS_RUNTIME_MONITORING"|"LAMBDA_NETWORK_LOGS"|"RUNTIME_MONITORING",
    "Status": "ENABLED"|"DISABLED",
    "AdditionalConfiguration": [
      {
        "Name": "EKS_ADDON_MANAGEMENT"|"ECS_FARGATE_AGENT_MANAGEMENT"|"EC2_AGENT_MANAGEMENT",
        "Status": "ENABLED"|"DISABLED"
      }
      ...
    ]
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To enable GuardDuty in the current region**

This example shows how to create a new detector, which enables GuardDuty, in the current region.:

```
aws guardduty create-detector \
    --enable
```

Output:

```
{
    "DetectorId": "b6b992d6d2f48e64bc59180bfexample"
}
```

For more information, see [Enable Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html#guardduty_enable-gd) in the *GuardDuty User Guide*.

## Output

DetectorId -> (string)

The unique ID of the created detector.

UnprocessedDataSources -> (structure)

Specifies the data sources that couldnât be enabled when GuardDuty was enabled for the first time.

MalwareProtection -> (structure)

An object that contains information on the status of all Malware Protection data sources.

ScanEc2InstanceWithFindings -> (structure)

Describes the configuration of Malware Protection for EC2 instances with findings.

EbsVolumes -> (structure)

Describes the configuration of scanning EBS volumes as a data source.

Status -> (string)

Describes whether scanning EBS volumes is enabled as a data source.

Reason -> (string)

Specifies the reason why scanning EBS volumes (Malware Protection) was not enabled as a data source.

ServiceRole -> (string)

The GuardDuty Malware Protection service role.