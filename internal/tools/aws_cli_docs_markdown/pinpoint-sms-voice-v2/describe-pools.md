# describe-poolsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-pools.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/describe-pools.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-sms-voice-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html#cli-aws-pinpoint-sms-voice-v2) ]

# describe-pools

## Description

Retrieves the specified pools or all pools associated with your Amazon Web Services account.

If you specify pool IDs, the output includes information for only the specified pools. If you specify filters, the output includes information for only those pools that meet the filter criteria. If you donât specify pool IDs or filters, the output includes information for all pools.

If you specify a pool ID that isnât valid, an error is returned.

A pool is a collection of phone numbers and SenderIds. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-v2-2022-03-31/DescribePools)

`describe-pools` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Pools`

## Synopsis

```
describe-pools
[--pool-ids <value>]
[--filters <value>]
[--owner <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--pool-ids` (list)

The unique identifier of pools to find. This is an array of strings that can be either the PoolId or PoolArn.

### Warning

If you are using a shared AWS End User Messaging SMS and Voice resource then you must use the full Amazon Resource Name(ARN).

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

An array of PoolFilter objects to filter the results.

(structure)

The information for a pool that meets a specified criteria.

Name -> (string)

The name of the attribute to filter on.

Values -> (list)

An array values to filter for.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "status"|"message-type"|"two-way-enabled"|"self-managed-opt-outs-enabled"|"opt-out-list-name"|"shared-routes-enabled"|"deletion-protection-enabled"|"two-way-channel-arn",
    "Values": ["string", ...]
  }
  ...
]
```

`--owner` (string)

Use `SELF` to filter the list of Pools to ones your account owns or use `SHARED` to filter on Pools shared with your account. The `Owner` and `PoolIds` parameters canât be used at the same time.

Possible values:

- `SELF`
- `SHARED`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

Pools -> (list)

An array of PoolInformation objects that contain the details for the requested pools.

(structure)

The information for a pool in an Amazon Web Services account.

PoolArn -> (string)

The Amazon Resource Name (ARN) for the pool.

PoolId -> (string)

The unique identifier for the pool.

Status -> (string)

The current status of the pool.

MessageType -> (string)

The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that arenât critical or time-sensitive.

TwoWayEnabled -> (boolean)

When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.

TwoWayChannelArn -> (string)

The Amazon Resource Name (ARN) of the two way channel.

TwoWayChannelRole -> (string)

An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.

SelfManagedOptOutsEnabled -> (boolean)

When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS and Voice automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true youâre responsible for responding to HELP and STOP requests. Youâre also responsible for tracking and honoring opt-out requests. For more information see [Self-managed opt-outs](https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out)

OptOutListName -> (string)

The name of the OptOutList associated with the pool.

SharedRoutesEnabled -> (boolean)

Allows you to enable shared routes on your pool.

By default, this is set to `False` . If you set this value to `True` , your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders arenât allowed to use shared routes and must use a dedicated phone number or short code.

DeletionProtectionEnabled -> (boolean)

When set to true the pool canât be deleted.

CreatedTimestamp -> (timestamp)

The time when the pool was created, in [UNIX epoch time](https://www.epochconverter.com/) format.

NextToken -> (string)

The token to be used for the next set of paginated results. If this field is empty then there are no more results.