# create-dataflow-endpoint-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-dataflow-endpoint-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-dataflow-endpoint-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [groundstation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/index.html#cli-aws-groundstation) ]

# create-dataflow-endpoint-group

## Description

Creates a `DataflowEndpoint` group containing the specified list of `DataflowEndpoint` objects.

The `name` field in each endpoint is used in your mission profile `DataflowEndpointConfig` to specify which endpoints to use during a contact.

When a contact uses multiple `DataflowEndpointConfig` objects, each `Config` must match a `DataflowEndpoint` in the same group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/CreateDataflowEndpointGroup)

## Synopsis

```
create-dataflow-endpoint-group
[--contact-post-pass-duration-seconds <value>]
[--contact-pre-pass-duration-seconds <value>]
--endpoint-details <value>
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

`--contact-post-pass-duration-seconds` (integer)

Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a `POSTPASS` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the `POSTPASS` state.

`--contact-pre-pass-duration-seconds` (integer)

Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a `PREPASS` state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the `PREPASS` state.

`--endpoint-details` (list)

Endpoint details of each endpoint in the dataflow endpoint group. `All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix <a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AwsGroundStationAgentEndpoint.html"> AWS Ground Station Agent endpoints</a> with <a href="https://docs.aws.amazon.com/ground-station/latest/APIReference/API_DataflowEndpoint.html">Dataflow endpoints</a> in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint groups for each type. </p>`

(structure)

Information about the endpoint details.

awsGroundStationAgentEndpoint -> (structure)

An agent endpoint.

agentStatus -> (string)

The status of AgentEndpoint.

auditResults -> (string)

The results of the audit.

egressAddress -> (structure)

The egress address of AgentEndpoint.

mtu -> (integer)

Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.

socketAddress -> (structure)

A socket address.

name -> (string)

Name of a socket address.

port -> (integer)

Port of a socket address.

ingressAddress -> (structure)

The ingress address of AgentEndpoint.

mtu -> (integer)

Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.

socketAddress -> (structure)

A ranged socket address.

name -> (string)

IPv4 socket address.

portRange -> (structure)

Port range of a socket address.

maximum -> (integer)

A maximum value.

minimum -> (integer)

A minimum value.

name -> (string)

Name string associated with AgentEndpoint. Used as a human-readable identifier for AgentEndpoint.

endpoint -> (structure)

A dataflow endpoint.

address -> (structure)

Socket address of a dataflow endpoint.

name -> (string)

Name of a socket address.

port -> (integer)

Port of a socket address.

mtu -> (integer)

Maximum transmission unit (MTU) size in bytes of a dataflow endpoint.

name -> (string)

Name of a dataflow endpoint.

status -> (string)

Status of a dataflow endpoint.

healthReasons -> (list)

Health reasons for a dataflow endpoint. This field is ignored when calling `CreateDataflowEndpointGroup` .

(string)

healthStatus -> (string)

A dataflow endpoint health status. This field is ignored when calling `CreateDataflowEndpointGroup` .

securityDetails -> (structure)

Endpoint security details including a list of subnets, a list of security groups and a role to connect streams to instances.

roleArn -> (string)

ARN to a role needed for connecting streams to your instances.

securityGroupIds -> (list)

The security groups to attach to the elastic network interfaces.

(string)

subnetIds -> (list)

A list of subnets where AWS Ground Station places elastic network interfaces to send streams to your instances.

(string)

JSON Syntax:

```
[
  {
    "awsGroundStationAgentEndpoint": {
      "agentStatus": "SUCCESS"|"FAILED"|"ACTIVE"|"INACTIVE",
      "auditResults": "HEALTHY"|"UNHEALTHY",
      "egressAddress": {
        "mtu": integer,
        "socketAddress": {
          "name": "string",
          "port": integer
        }
      },
      "ingressAddress": {
        "mtu": integer,
        "socketAddress": {
          "name": "string",
          "portRange": {
            "maximum": integer,
            "minimum": integer
          }
        }
      },
      "name": "string"
    },
    "endpoint": {
      "address": {
        "name": "string",
        "port": integer
      },
      "mtu": integer,
      "name": "string",
      "status": "created"|"creating"|"deleted"|"deleting"|"failed"
    },
    "healthReasons": ["NO_REGISTERED_AGENT"|"INVALID_IP_OWNERSHIP"|"NOT_AUTHORIZED_TO_CREATE_SLR"|"UNVERIFIED_IP_OWNERSHIP"|"INITIALIZING_DATAPLANE"|"DATAPLANE_FAILURE"|"HEALTHY", ...],
    "healthStatus": "HEALTHY"|"UNHEALTHY",
    "securityDetails": {
      "roleArn": "string",
      "securityGroupIds": ["string", ...],
      "subnetIds": ["string", ...]
    }
  }
  ...
]
```

`--tags` (map)

Tags of a dataflow endpoint group.

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

dataflowEndpointGroupId -> (string)

UUID of a dataflow endpoint group.