# describe-inbound-cross-cluster-search-connectionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-inbound-cross-cluster-search-connections.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-inbound-cross-cluster-search-connections.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [es](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html#cli-aws-es) ]

# describe-inbound-cross-cluster-search-connections

## Description

Lists all the inbound cross-cluster search connections for a destination domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeInboundCrossClusterSearchConnections)

## Synopsis

```
describe-inbound-cross-cluster-search-connections
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--filters` (list)

A list of filters used to match properties for inbound cross-cluster search connection. Available `` Filter`` names for this operation are:

- cross-cluster-search-connection-id
- source-domain-info.domain-name
- source-domain-info.owner-id
- source-domain-info.region
- destination-domain-info.domain-name

(structure)

A filter used to limit results when describing inbound or outbound cross-cluster search connections. Multiple values can be specified per filter. A cross-cluster search connection must match at least one of the specified values for it to be returned from an operation.

Name -> (string)

Specifies the name of the filter.

Values -> (list)

Contains one or more values for the filter.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

Set this value to limit the number of results returned. If not specified, defaults to 100.

`--next-token` (string)

NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.

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

CrossClusterSearchConnections -> (list)

Consists of list of `` InboundCrossClusterSearchConnection`` matching the specified filter criteria.

(structure)

Specifies details of an inbound connection.

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

CrossClusterSearchConnectionId -> (string)

Specifies the connection id for the inbound cross-cluster search connection.

ConnectionStatus -> (structure)

Specifies the `` InboundCrossClusterSearchConnectionStatus`` for the outbound connection.

StatusCode -> (string)

The state code for inbound connection. This can be one of the following:

- PENDING_ACCEPTANCE: Inbound connection is not yet accepted by destination domain owner.
- APPROVED: Inbound connection is pending acceptance by destination domain owner.
- REJECTING: Inbound connection rejection is in process.
- REJECTED: Inbound connection is rejected.
- DELETING: Inbound connection deletion is in progress.
- DELETED: Inbound connection is deleted and cannot be used further.

Message -> (string)

Specifies verbose information for the inbound connection status.

NextToken -> (string)

If more results are available and NextToken is present, make the next request to the same API with the received NextToken to paginate the remaining results.