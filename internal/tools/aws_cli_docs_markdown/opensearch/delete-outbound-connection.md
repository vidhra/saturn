# delete-outbound-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/delete-outbound-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/delete-outbound-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# delete-outbound-connection

## Description

Allows the source Amazon OpenSearch Service domain owner to delete an existing outbound cross-cluster search connection. For more information, see [Cross-cluster search for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/cross-cluster-search.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/DeleteOutboundConnection)

## Synopsis

```
delete-outbound-connection
--connection-id <value>
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

`--connection-id` (string)

The ID of the outbound connection you want to permanently delete.

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

Connection -> (structure)

The deleted inbound connection.

LocalDomainInfo -> (structure)

Information about the source (local) domain.

AWSDomainInformation -> (structure)

Information about an Amazon OpenSearch Service domain.

OwnerId -> (string)

The Amazon Web Services account ID of the domain owner.

DomainName -> (string)

Name of the domain.

Region -> (string)

The Amazon Web Services Region in which the domain is located.

RemoteDomainInfo -> (structure)

Information about the destination (remote) domain.

AWSDomainInformation -> (structure)

Information about an Amazon OpenSearch Service domain.

OwnerId -> (string)

The Amazon Web Services account ID of the domain owner.

DomainName -> (string)

Name of the domain.

Region -> (string)

The Amazon Web Services Region in which the domain is located.

ConnectionId -> (string)

Unique identifier of the connection.

ConnectionAlias -> (string)

Name of the connection.

ConnectionStatus -> (structure)

Status of the connection.

StatusCode -> (string)

The status code for the outbound connection. Can be one of the following:

- **VALIDATING** - The outbound connection request is being validated.
- **VALIDATION_FAILED** - Validation failed for the connection request.
- **PENDING_ACCEPTANCE** : Outbound connection request is validated and is not yet accepted by the remote domain owner.
- **APPROVED** - Outbound connection has been approved by the remote domain owner for getting provisioned.
- **PROVISIONING** - Outbound connection request is in process.
- **ACTIVE** - Outbound connection is active and ready to use.
- **REJECTING** - Outbound connection rejection by remote domain owner is in progress.
- **REJECTED** - Outbound connection request is rejected by remote domain owner.
- **DELETING** - Outbound connection deletion is in progress.
- **DELETED** - Outbound connection is deleted and can no longer be used.

Message -> (string)

Verbose information for the outbound connection.

ConnectionMode -> (string)

The connection mode.

ConnectionProperties -> (structure)

Properties for the outbound connection.

Endpoint -> (string)

### Warning

The Endpoint attribute cannot be modified.

The endpoint of the remote domain. Applicable for VPC_ENDPOINT connection mode.

CrossClusterSearch -> (structure)

The connection properties for cross cluster search.

SkipUnavailable -> (string)

The status of the `SkipUnavailable` setting for the outbound connection. This feature allows you to specify some clusters as optional and ensure that your cross-cluster queries return partial results despite failures on one or more remote clusters.