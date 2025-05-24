# get-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/get-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/get-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-sap](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/index.html#cli-aws-ssm-sap) ]

# get-component

## Description

Gets the component of an application registered with AWS Systems Manager for SAP.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-sap-2018-05-10/GetComponent)

## Synopsis

```
get-component
--application-id <value>
--component-id <value>
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

`--application-id` (string)

The ID of the application.

`--component-id` (string)

The ID of the component.

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

Component -> (structure)

The component of an application registered with AWS Systems Manager for SAP.

ComponentId -> (string)

The ID of the component.

Sid -> (string)

The SAP System Identifier of the application component.

SystemNumber -> (string)

The SAP system number of the application component.

ParentComponent -> (string)

The parent component of a highly available environment. For example, in a highly available SAP on AWS workload, the parent component consists of the entire setup, including the child components.

ChildComponents -> (list)

The child components of a highly available environment. For example, in a highly available SAP on AWS workload, the child component consists of the primary and secondar instances.

(string)

ApplicationId -> (string)

The ID of the application.

ComponentType -> (string)

The type of the component.

Status -> (string)

The status of the component.

- ACTIVATED - this status has been deprecated.
- STARTING - the component is in the process of being started.
- STOPPED - the component is not running.
- STOPPING - the component is in the process of being stopped.
- RUNNING - the component is running.
- RUNNING_WITH_ERROR - one or more child component(s) of the parent component is not running. Call ` `GetComponent` [https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetComponent](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetComponent).html`__ to review the status of each child component.
- UNDEFINED - AWS Systems Manager for SAP cannot provide the component status based on the discovered information. Verify your SAP application.

SapHostname -> (string)

The hostname of the component.

SapFeature -> (string)

The SAP feature of the component.

SapKernelVersion -> (string)

The kernel version of the component.

HdbVersion -> (string)

The SAP HANA version of the component.

Resilience -> (structure)

Details of the SAP HANA system replication for the component.

HsrTier -> (string)

The tier of the component.

HsrReplicationMode -> (string)

The replication mode of the component.

HsrOperationMode -> (string)

The operation mode of the component.

ClusterStatus -> (string)

The cluster status of the component.

EnqueueReplication -> (boolean)

Indicates if or not enqueue replication is enabled for the ASCS component.

AssociatedHost -> (structure)

The associated host of the component.

Hostname -> (string)

The name of the host.

Ec2InstanceId -> (string)

The ID of the Amazon EC2 instance.

IpAddresses -> (list)

The IP addresses of the associated host.

(structure)

Provides information of the IP address.

IpAddress -> (string)

The IP address.

Primary -> (boolean)

The primary IP address.

AllocationType -> (string)

The type of allocation for the IP address.

OsVersion -> (string)

The version of the operating system.

Databases -> (list)

The SAP HANA databases of the component.

(string)

Hosts -> (list)

The hosts of the component.

(structure)

Describes the properties of the Dedicated Host.

HostName -> (string)

The name of the Dedicated Host.

HostIp -> (string)

The IP address of the Dedicated Host.

EC2InstanceId -> (string)

The ID of Amazon EC2 instance.

InstanceId -> (string)

The instance ID of the instance on the Dedicated Host.

HostRole -> (string)

The role of the Dedicated Host.

OsVersion -> (string)

The version of the operating system.

PrimaryHost -> (string)

The primary host of the component.

DatabaseConnection -> (structure)

The connection specifications for the database of the component.

DatabaseConnectionMethod -> (string)

The method of connection.

DatabaseArn -> (string)

The Amazon Resource Name of the connected SAP HANA database.

ConnectionIp -> (string)

The IP address for connection.

LastUpdated -> (timestamp)

The time at which the component was last updated.

Arn -> (string)

The Amazon Resource Name (ARN) of the component.

Tags -> (map)

The tags of a component.

key -> (string)

value -> (string)