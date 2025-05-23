# start-engagement-from-opportunity-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/start-engagement-from-opportunity-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/start-engagement-from-opportunity-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [partnercentral-selling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/partnercentral-selling/index.html#cli-aws-partnercentral-selling) ]

# start-engagement-from-opportunity-task

## Description

This action initiates the engagement process from an existing opportunity by accepting the engagement invitation and creating a corresponding opportunity in the partnerâs system. Similar to `StartEngagementByAcceptingInvitationTask` , this action is asynchronous and performs multiple steps before completion.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask)

## Synopsis

```
start-engagement-from-opportunity-task
--aws-submission <value>
--catalog <value>
[--client-token <value>]
--identifier <value>
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

`--aws-submission` (structure)

Indicates the level of AWS involvement in the opportunity. This field helps track AWS participation throughout the engagement, such as providing technical support, deal assistance, and sales support.

InvolvementType -> (string)

Specifies the type of AWS involvement in the opportunity, such as coselling, deal support, or technical consultation. This helps categorize the nature of AWS participation.

Visibility -> (string)

Determines who can view AWS involvement in the opportunity. Typically, this field is set to `Full` for most cases, but it may be restricted based on special program requirements or confidentiality needs.

Shorthand Syntax:

```
InvolvementType=string,Visibility=string
```

JSON Syntax:

```
{
  "InvolvementType": "For Visibility Only"|"Co-Sell",
  "Visibility": "Full"|"Limited"
}
```

`--catalog` (string)

Specifies the catalog in which the engagement is tracked. Acceptable values include `AWS` for production and `Sandbox` for testing environments.

`--client-token` (string)

A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.

`--identifier` (string)

The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.

`--tags` (list)

A map of the key-value pairs of the tag or tags to assign.

(structure)

The key-value pair assigned to a specified resource.

Key -> (string)

The key in the tag.

Value -> (string)

The value in the tag.

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

EngagementId -> (string)

The identifier of the newly created Engagement. Only populated if TaskStatus is COMPLETE.

EngagementInvitationId -> (string)

The identifier of the new Engagement invitation. Only populated if TaskStatus is COMPLETE.

Message -> (string)

If the task fails, this field contains a detailed message describing the failure and possible recovery steps.

OpportunityId -> (string)

Returns the original opportunity identifier passed in the request, which is the unique identifier for the opportunity created in the partnerâs system.

ReasonCode -> (string)

Indicates the reason for task failure using an enumerated code.

ResourceSnapshotJobId -> (string)

The identifier of the resource snapshot job created to add the opportunity resource snapshot to the Engagement. Only populated if TaskStatus is COMPLETE

StartTime -> (timestamp)

The timestamp indicating when the task was initiated. The format follows RFC 3339 section 5.6.

TaskArn -> (string)

The Amazon Resource Name (ARN) of the task, used for tracking and managing the task within AWS.

TaskId -> (string)

The unique identifier of the task, used to track the taskâs progress. This value follows a specific pattern: `^oit-[0-9a-z]{13}$` .

TaskStatus -> (string)

Indicates the current status of the task. Valid values include `IN_PROGRESS` , `COMPLETE` , and `FAILED` .