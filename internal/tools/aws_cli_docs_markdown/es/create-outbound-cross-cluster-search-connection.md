# create-outbound-cross-cluster-search-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-outbound-cross-cluster-search-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/create-outbound-cross-cluster-search-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [es](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html#cli-aws-es) ]

# create-outbound-cross-cluster-search-connection

## Description

Creates a new cross-cluster search connection from a source domain to a destination domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/CreateOutboundCrossClusterSearchConnection)

## Synopsis

```
create-outbound-cross-cluster-search-connection
--source-domain-info <value>
--destination-domain-info <value>
--connection-alias <value>
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

`--source-domain-info` (structure)

Specifies the `` DomainInformation`` for the source Elasticsearch domain.

OwnerId -> (string)

DomainName -> (string)

The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

Region -> (string)

Shorthand Syntax:

```
OwnerId=string,DomainName=string,Region=string
```

JSON Syntax:

```
{
  "OwnerId": "string",
  "DomainName": "string",
  "Region": "string"
}
```

`--destination-domain-info` (structure)

Specifies the `` DomainInformation`` for the destination Elasticsearch domain.

OwnerId -> (string)

DomainName -> (string)

The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

Region -> (string)

Shorthand Syntax:

```
OwnerId=string,DomainName=string,Region=string
```

JSON Syntax:

```
{
  "OwnerId": "string",
  "DomainName": "string",
  "Region": "string"
}
```

`--connection-alias` (string)

Specifies the connection alias that will be used by the customer for this connection.

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

SourceDomainInfo -> (structure)

Specifies the `` DomainInformation`` for the source Elasticsearch domain.

OwnerId -> (string)

DomainName -> (string)

The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

Region -> (string)

DestinationDomainInfo -> (structure)

Specifies the `` DomainInformation`` for the destination Elasticsearch domain.

OwnerId -> (string)

DomainName -> (string)

The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

Region -> (string)

ConnectionAlias -> (string)

Specifies the connection alias provided during the create connection request.

ConnectionStatus -> (structure)

Specifies the `` OutboundCrossClusterSearchConnectionStatus`` for the newly created connection.

StatusCode -> (string)

The state code for outbound connection. This can be one of the following:

- VALIDATING: The outbound connection request is being validated.
- VALIDATION_FAILED: Validation failed for the connection request.
- PENDING_ACCEPTANCE: Outbound connection request is validated and is not yet accepted by destination domain owner.
- PROVISIONING: Outbound connection request is in process.
- ACTIVE: Outbound connection is active and ready to use.
- REJECTED: Outbound connection request is rejected by destination domain owner.
- DELETING: Outbound connection deletion is in progress.
- DELETED: Outbound connection is deleted and cannot be used further.

Message -> (string)

Specifies verbose information for the outbound connection status.

CrossClusterSearchConnectionId -> (string)

Unique id for the created outbound connection, which is used for subsequent operations on connection.