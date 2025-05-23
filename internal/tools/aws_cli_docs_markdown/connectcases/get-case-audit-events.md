# get-case-audit-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/get-case-audit-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/get-case-audit-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connectcases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/index.html#cli-aws-connectcases) ]

# get-case-audit-events

## Description

Returns the audit history about a specific case if it exists.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connectcases-2022-10-03/GetCaseAuditEvents)

## Synopsis

```
get-case-audit-events
--case-id <value>
--domain-id <value>
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

`--case-id` (string)

A unique identifier of the case.

`--domain-id` (string)

The unique identifier of the Cases domain.

`--max-results` (integer)

The maximum number of audit events to return. The current maximum supported value is 25. This is also the default when no other value is provided.

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

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

auditEvents -> (list)

A list of case audits where each represents a particular edit of the case.

(structure)

Represents the content of a particular audit event.

eventId -> (string)

Unique identifier of a case audit history event.

fields -> (list)

A list of Case Audit History event fields.

(structure)

Fields for audit event.

eventFieldId -> (string)

Unique identifier of field in an Audit History entry.

newValue -> (tagged union structure)

Union of potential field value types.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValue`, `doubleValue`, `emptyValue`, `stringValue`, `userArnValue`.

booleanValue -> (boolean)

Can be either null, or have a Boolean value type. Only one value can be provided.

doubleValue -> (double)

Can be either null, or have a Double value type. Only one value can be provided.

emptyValue -> (structure)

An empty value. You cannot set `EmptyFieldValue` on a field that is required on a case template.

This structure will never have any data members. It signifies an empty value on a case field.

stringValue -> (string)

Can be either null, or have a String value type. Only one value can be provided.

userArnValue -> (string)

Can be either null, or have a String value type formatted as an ARN. Only one value can be provided.

oldValue -> (tagged union structure)

Union of potential field value types.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValue`, `doubleValue`, `emptyValue`, `stringValue`, `userArnValue`.

booleanValue -> (boolean)

Can be either null, or have a Boolean value type. Only one value can be provided.

doubleValue -> (double)

Can be either null, or have a Double value type. Only one value can be provided.

emptyValue -> (structure)

An empty value. You cannot set `EmptyFieldValue` on a field that is required on a case template.

This structure will never have any data members. It signifies an empty value on a case field.

stringValue -> (string)

Can be either null, or have a String value type. Only one value can be provided.

userArnValue -> (string)

Can be either null, or have a String value type formatted as an ARN. Only one value can be provided.

performedBy -> (structure)

Information of the user which performed the audit.

iamPrincipalArn -> (string)

Unique identifier of an IAM role.

user -> (tagged union structure)

Represents the entity that performed the action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `customEntity`, `userArn`.

customEntity -> (string)

Any provided entity.

userArn -> (string)

Represents the Amazon Connect ARN of the user.

performedTime -> (timestamp)

Time at which an Audit History event took place.

relatedItemType -> (string)

The Type of the related item.

type -> (string)

The Type of an audit history event.

nextToken -> (string)

The token for the next set of results. This is null if there are no more results to return.