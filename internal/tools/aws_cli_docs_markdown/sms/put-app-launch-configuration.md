# put-app-launch-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/put-app-launch-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/put-app-launch-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/index.html#cli-aws-sms) ]

# put-app-launch-configuration

## Description

Creates or updates the launch configuration for the specified application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sms-2016-10-24/PutAppLaunchConfiguration)

## Synopsis

```
put-app-launch-configuration
[--app-id <value>]
[--role-name <value>]
[--auto-launch | --no-auto-launch]
[--server-group-launch-configurations <value>]
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

`--app-id` (string)

The ID of the application.

`--role-name` (string)

The name of service role in the customerâs account that CloudFormation uses to launch the application.

`--auto-launch` | `--no-auto-launch` (boolean)

Indicates whether the application is configured to launch automatically after replication is complete.

`--server-group-launch-configurations` (list)

Information about the launch configurations for server groups in the application.

(structure)

Launch configuration for a server group.

serverGroupId -> (string)

The ID of the server group with which the launch configuration is associated.

launchOrder -> (integer)

The launch order of servers in the server group.

serverLaunchConfigurations -> (list)

The launch configuration for servers in the server group.

(structure)

Launch configuration for a server.

server -> (structure)

The ID of the server with which the launch configuration is associated.

serverId -> (string)

The ID of the server.

serverType -> (string)

The type of server.

vmServer -> (structure)

Information about the VM server.

vmServerAddress -> (structure)

The VM server location.

vmManagerId -> (string)

The ID of the VM manager.

vmId -> (string)

The ID of the VM.

vmName -> (string)

The name of the VM.

vmManagerName -> (string)

The name of the VM manager.

vmManagerType -> (string)

The type of VM management product.

vmPath -> (string)

The VM folder path in the vCenter Server virtual machine inventory tree.

replicationJobId -> (string)

The ID of the replication job.

replicationJobTerminated -> (boolean)

Indicates whether the replication job is deleted or failed.

logicalId -> (string)

The logical ID of the server in the CloudFormation template.

vpc -> (string)

The ID of the VPC into which the server should be launched.

subnet -> (string)

The ID of the subnet the server should be launched into.

securityGroup -> (string)

The ID of the security group that applies to the launched server.

ec2KeyName -> (string)

The name of the Amazon EC2 SSH key to be used for connecting to the launched server.

userData -> (structure)

Location of the user-data script to be executed when launching the server.

s3Location -> (structure)

Amazon S3 location of the user-data script.

bucket -> (string)

The Amazon S3 bucket name.

key -> (string)

The Amazon S3 bucket key.

instanceType -> (string)

The instance type to use when launching the server.

associatePublicIpAddress -> (boolean)

Indicates whether a publicly accessible IP address is created when launching the server.

iamInstanceProfileName -> (string)

The name of the IAM instance profile.

configureScript -> (structure)

Location of an Amazon S3 object.

bucket -> (string)

The Amazon S3 bucket name.

key -> (string)

The Amazon S3 bucket key.

configureScriptType -> (string)

The type of configuration script.

JSON Syntax:

```
[
  {
    "serverGroupId": "string",
    "launchOrder": integer,
    "serverLaunchConfigurations": [
      {
        "server": {
          "serverId": "string",
          "serverType": "VIRTUAL_MACHINE",
          "vmServer": {
            "vmServerAddress": {
              "vmManagerId": "string",
              "vmId": "string"
            },
            "vmName": "string",
            "vmManagerName": "string",
            "vmManagerType": "VSPHERE"|"SCVMM"|"HYPERV-MANAGER",
            "vmPath": "string"
          },
          "replicationJobId": "string",
          "replicationJobTerminated": true|false
        },
        "logicalId": "string",
        "vpc": "string",
        "subnet": "string",
        "securityGroup": "string",
        "ec2KeyName": "string",
        "userData": {
          "s3Location": {
            "bucket": "string",
            "key": "string"
          }
        },
        "instanceType": "string",
        "associatePublicIpAddress": true|false,
        "iamInstanceProfileName": "string",
        "configureScript": {
          "bucket": "string",
          "key": "string"
        },
        "configureScriptType": "SHELL_SCRIPT"|"POWERSHELL_SCRIPT"
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