# modify-instance-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# modify-instance-groups

## Description

ModifyInstanceGroups modifies the number of nodes and configuration settings of an instance group. The input parameters include the new target instance count for the group and the instance group ID. The call will either succeed or fail atomically.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ModifyInstanceGroups)

## Synopsis

```
modify-instance-groups
[--cluster-id <value>]
[--instance-groups <value>]
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

`--cluster-id` (string)

The ID of the cluster to which the instance group belongs.

`--instance-groups` (list)

Instance groups to change.

(structure)

Modify the size or configurations of an instance group.

InstanceGroupId -> (string)

Unique ID of the instance group to modify.

InstanceCount -> (integer)

Target size for the instance group.

EC2InstanceIdsToTerminate -> (list)

The Amazon EC2 InstanceIds to terminate. After you terminate the instances, the instance group will not return to its original requested size.

(string)

ShrinkPolicy -> (structure)

Policy for customizing shrink operations.

DecommissionTimeout -> (integer)

The desired timeout for decommissioning an instance. Overrides the default YARN decommissioning timeout.

InstanceResizePolicy -> (structure)

Custom policy for requesting termination protection or termination of specific instances when shrinking an instance group.

InstancesToTerminate -> (list)

Specific list of instances to be terminated when shrinking an instance group.

(string)

InstancesToProtect -> (list)

Specific list of instances to be protected when shrinking an instance group.

(string)

InstanceTerminationTimeout -> (integer)

Decommissioning timeout override for the specific list of instances to be terminated.

ReconfigurationType -> (string)

Type of reconfiguration requested. Valid values are MERGE and OVERWRITE.

Configurations -> (list)

A list of new or modified configurations to apply for an instance group.

(structure)

### Note

Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) .

Classification -> (string)

The classification within a configuration.

Configurations -> (list)

A list of additional configurations to apply within a configuration object.

(structure)

### Note

Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) .

Classification -> (string)

The classification within a configuration.

Properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

Properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

JSON Syntax:

```
[
  {
    "InstanceGroupId": "string",
    "InstanceCount": integer,
    "EC2InstanceIdsToTerminate": ["string", ...],
    "ShrinkPolicy": {
      "DecommissionTimeout": integer,
      "InstanceResizePolicy": {
        "InstancesToTerminate": ["string", ...],
        "InstancesToProtect": ["string", ...],
        "InstanceTerminationTimeout": integer
      }
    },
    "ReconfigurationType": "OVERWRITE"|"MERGE",
    "Configurations": [
      {
        "Classification": "string",
        "Configurations": [
          {
            "Classification": "string",
            "Configurations": ,
            "Properties": {"string": "string"
              ...}
          }
          ...
        ],
        "Properties": {"string": "string"
          ...}
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

## Output

None