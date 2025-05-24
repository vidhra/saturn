# describe-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/describe-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/describe-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [groundstation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/index.html#cli-aws-groundstation) ]

# describe-contact

## Description

Describes an existing contact.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/DescribeContact)

## Synopsis

```
describe-contact
--contact-id <value>
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

`--contact-id` (string)

UUID of a contact.

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

contactId -> (string)

UUID of a contact.

contactStatus -> (string)

Status of a contact.

dataflowList -> (list)

List describing source and destination details for each dataflow edge.

(structure)

Information about a dataflow edge used in a contact.

destination -> (structure)

Dataflow details for the destination side.

configDetails -> (tagged union structure)

Additional details for a `Config` , if type is dataflow endpoint or antenna demod decode.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `antennaDemodDecodeDetails`, `endpointDetails`, `s3RecordingDetails`.

antennaDemodDecodeDetails -> (structure)

Details for antenna demod decode `Config` in a contact.

outputNode -> (string)

Name of an antenna demod decode output node used in a contact.

endpointDetails -> (structure)

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

s3RecordingDetails -> (structure)

Details for an S3 recording `Config` in a contact.

bucketArn -> (string)

ARN of the bucket used.

keyTemplate -> (string)

Key template used for the S3 Recording Configuration

configId -> (string)

UUID of a `Config` .

configType -> (string)

Type of a `Config` .

dataflowDestinationRegion -> (string)

Region of a dataflow destination.

errorMessage -> (string)

Error message for a dataflow.

source -> (structure)

Dataflow details for the source side.

configDetails -> (tagged union structure)

Additional details for a `Config` , if type is `dataflow-endpoint` or `antenna-downlink-demod-decode`

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `antennaDemodDecodeDetails`, `endpointDetails`, `s3RecordingDetails`.

antennaDemodDecodeDetails -> (structure)

Details for antenna demod decode `Config` in a contact.

outputNode -> (string)

Name of an antenna demod decode output node used in a contact.

endpointDetails -> (structure)

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

s3RecordingDetails -> (structure)

Details for an S3 recording `Config` in a contact.

bucketArn -> (string)

ARN of the bucket used.

keyTemplate -> (string)

Key template used for the S3 Recording Configuration

configId -> (string)

UUID of a `Config` .

configType -> (string)

Type of a `Config` .

dataflowSourceRegion -> (string)

Region of a dataflow source.

endTime -> (timestamp)

End time of a contact in UTC.

errorMessage -> (string)

Error message for a contact.

groundStation -> (string)

Ground station for a contact.

maximumElevation -> (structure)

Maximum elevation angle of a contact.

unit -> (string)

Elevation angle units.

value -> (double)

Elevation angle value.

missionProfileArn -> (string)

ARN of a mission profile.

postPassEndTime -> (timestamp)

Amount of time after a contact ends that youâd like to receive a CloudWatch event indicating the pass has finished.

prePassStartTime -> (timestamp)

Amount of time prior to contact start youâd like to receive a CloudWatch event indicating an upcoming pass.

region -> (string)

Region of a contact.

satelliteArn -> (string)

ARN of a satellite.

startTime -> (timestamp)

Start time of a contact in UTC.

tags -> (map)

Tags assigned to a contact.

key -> (string)

value -> (string)

visibilityEndTime -> (timestamp)

Projected time in UTC your satellite will set below the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html) . This time is based on the satelliteâs current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts.

visibilityStartTime -> (timestamp)

Projected time in UTC your satellite will rise above the [receive mask](https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html) . This time is based on the satelliteâs current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts.