# get-incident-recordÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-incident-record.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-incident-record.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-incidents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/index.html#cli-aws-ssm-incidents) ]

# get-incident-record

## Description

Returns the details for the specified incident record.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-incidents-2018-05-10/GetIncidentRecord)

## Synopsis

```
get-incident-record
--arn <value>
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

`--arn` (string)

The Amazon Resource Name (ARN) of the incident record.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get an incident record**

The following `get-incident-record` example gets details about the specified incident record.

```
aws ssm-incidents get-incident-record \
    --arn "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"
```

Output:

```
{
    "incidentRecord": {
        "arn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308",
        "automationExecutions": [],
        "creationTime": "2021-05-21T18:16:57.579000+00:00",
        "dedupeString": "c4bcc812-85e7-938d-2b78-17181176ee1a",
        "impact": 5,
        "incidentRecordSource": {
            "createdBy": "arn:aws:iam::111122223333:user/draliatp",
            "invokedBy": "arn:aws:iam::111122223333:user/draliatp",
            "source": "aws.ssm-incidents.custom"
        },
        "lastModifiedBy": "arn:aws:iam::111122223333:user/draliatp",
        "lastModifiedTime": "2021-05-21T18:16:59.149000+00:00",
        "notificationTargets": [],
        "status": "OPEN",
        "title": "Example-Incident"
    }
}
```

For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html) in the *Incident Manager User Guide*.

## Output

incidentRecord -> (structure)

Details the structure of the incident record.

arn -> (string)

The Amazon Resource Name (ARN) of the incident record.

automationExecutions -> (list)

The runbook, or automation document, thatâs run at the beginning of the incident.

(tagged union structure)

The Systems Manager automation document process to start as the runbook at the beginning of the incident.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ssmExecutionArn`.

ssmExecutionArn -> (string)

The Amazon Resource Name (ARN) of the automation process.

chatChannel -> (tagged union structure)

The chat channel used for collaboration during an incident.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `chatbotSns`, `empty`.

chatbotSns -> (list)

The Amazon SNS targets that Chatbot uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel by using the Amazon SNS topics.

(string)

empty -> (structure)

Used to remove the chat channel from an incident record or response plan.

creationTime -> (timestamp)

The timestamp for when Incident Manager created the incident record.

dedupeString -> (string)

The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.

impact -> (integer)

The impact of the incident on customers and applications.

**Supported impact codes**

- `1` - Critical
- `2` - High
- `3` - Medium
- `4` - Low
- `5` - No Impact

incidentRecordSource -> (structure)

Details about the action that started the incident.

createdBy -> (string)

The principal that started the incident.

invokedBy -> (string)

The service principal that assumed the role specified in `createdBy` . If no service principal assumed the role this will be left blank.

resourceArn -> (string)

The resource that caused the incident to be created.

source -> (string)

The service that started the incident. This can be manually created from Incident Manager, automatically created using an Amazon CloudWatch alarm, or Amazon EventBridge event.

lastModifiedBy -> (string)

Who modified the incident most recently.

lastModifiedTime -> (timestamp)

The timestamp for when the incident was most recently modified.

notificationTargets -> (list)

The Amazon SNS targets that are notified when updates are made to an incident.

(tagged union structure)

The SNS targets that are notified when updates are made to an incident.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `snsTopicArn`.

snsTopicArn -> (string)

The Amazon Resource Name (ARN) of the SNS topic.

resolvedTime -> (timestamp)

The timestamp for when the incident was resolved. This appears as a timeline event.

status -> (string)

The current status of the incident.

summary -> (string)

The summary of the incident. The summary is a brief synopsis of what occurred, whatâs currently happening, and context of the incident.

title -> (string)

The title of the incident.