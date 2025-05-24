# create-voice-connectorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-voice/create-voice-connector.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-voice/create-voice-connector.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-voice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-voice/index.html#cli-aws-chime-sdk-voice) ]

# create-voice-connector

## Description

Creates an Amazon Chime SDK Voice Connector. For more information about Voice Connectors, see [Managing Amazon Chime SDK Voice Connector groups](https://docs.aws.amazon.com/chime-sdk/latest/ag/voice-connector-groups.html) in the *Amazon Chime SDK Administrator Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-voice-2022-08-03/CreateVoiceConnector)

## Synopsis

```
create-voice-connector
--name <value>
[--aws-region <value>]
--require-encryption | --no-require-encryption
[--tags <value>]
[--integration-type <value>]
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

`--name` (string)

The name of the Voice Connector.

`--aws-region` (string)

The AWS Region in which the Amazon Chime SDK Voice Connector is created. Default value: `us-east-1` .

Possible values:

- `us-east-1`
- `us-west-2`
- `ca-central-1`
- `eu-central-1`
- `eu-west-1`
- `eu-west-2`
- `ap-northeast-2`
- `ap-northeast-1`
- `ap-southeast-1`
- `ap-southeast-2`

`--require-encryption` | `--no-require-encryption` (boolean)

Enables or disables encryption for the Voice Connector.

`--tags` (list)

The tags assigned to the Voice Connector.

(structure)

Describes a tag applied to a resource.

Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--integration-type` (string)

The connectors for use with Amazon Connect.

The following options are available:

- `CONNECT_CALL_TRANSFER_CONNECTOR` - Enables enterprises to integrate Amazon Connect with other voice systems to directly transfer voice calls and metadata without using the public telephone network. They can use Amazon Connect telephony and Interactive Voice Response (IVR) with their existing voice systems to modernize the IVR experience of their existing contact center and their enterprise and branch voice systems. Additionally, enterprises migrating their contact center to Amazon Connect can start with Connect telephony and IVR for immediate modernization ahead of agent migration.
- `CONNECT_ANALYTICS_CONNECTOR` - Enables enterprises to integrate Amazon Connect with other voice systems for real-time and post-call analytics. They can use Amazon Connect Contact Lens with their existing voice systems to provides call recordings, conversational analytics (including contact transcript, sensitive data redaction, content categorization, theme detection, sentiment analysis, real-time alerts, and post-contact summary), and agent performance evaluations (including evaluation forms, automated evaluation, supervisor review) with a rich user experience to display, search and filter customer interactions, and programmatic access to data streams and the data lake. Additionally, enterprises migrating their contact center to Amazon Connect can start with Contact Lens analytics and performance insights ahead of agent migration.

Possible values:

- `CONNECT_CALL_TRANSFER_CONNECTOR`
- `CONNECT_ANALYTICS_CONNECTOR`

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

VoiceConnector -> (structure)

The details of the Voice Connector.

VoiceConnectorId -> (string)

The Voice Connectorâs ID.

AwsRegion -> (string)

The AWS Region in which the Voice Connector is created. Default: us-east-1.

Name -> (string)

The Voice Connectorâs name.

OutboundHostName -> (string)

The outbound host name for the Voice Connector.

RequireEncryption -> (boolean)

Enables or disables encryption for the Voice Connector.

CreatedTimestamp -> (timestamp)

The Voice Connectorâs creation timestamp, in ISO 8601 format.

UpdatedTimestamp -> (timestamp)

The Voice Connectorâs updated timestamp, in ISO 8601 format.

VoiceConnectorArn -> (string)

The ARN of the Voice Connector.

IntegrationType -> (string)

The connectors for use with Amazon Connect.