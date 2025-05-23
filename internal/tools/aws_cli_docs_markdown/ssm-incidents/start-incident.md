# start-incidentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/start-incident.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/start-incident.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-incidents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/index.html#cli-aws-ssm-incidents) ]

# start-incident

## Description

Used to start an incident from CloudWatch alarms, EventBridge events, or manually.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-incidents-2018-05-10/StartIncident)

## Synopsis

```
start-incident
[--client-token <value>]
[--impact <value>]
[--related-items <value>]
--response-plan-arn <value>
[--title <value>]
[--trigger-details <value>]
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

`--client-token` (string)

A token ensuring that the operation is called only once with the specified details.

`--impact` (integer)

Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.

**Supported impact codes**

- `1` - Critical
- `2` - High
- `3` - Medium
- `4` - Low
- `5` - No Impact

`--related-items` (list)

Add related items to the incident for other responders to use. Related items are Amazon Web Services resources, external links, or files uploaded to an Amazon S3 bucket.

(structure)

Resources that responders use to triage and mitigate the incident.

generatedId -> (string)

A unique ID for a `RelatedItem` .

### Warning

Donât specify this parameter when you add a `RelatedItem` by using the  UpdateRelatedItems API action.

identifier -> (structure)

Details about the related item.

type -> (string)

The type of related item.

value -> (tagged union structure)

Details about the related item.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `arn`, `metricDefinition`, `pagerDutyIncidentDetail`, `url`.

arn -> (string)

The Amazon Resource Name (ARN) of the related item, if the related item is an Amazon resource.

metricDefinition -> (string)

The metric definition, if the related item is a metric in Amazon CloudWatch.

pagerDutyIncidentDetail -> (structure)

Details about an incident that is associated with a PagerDuty incident.

autoResolve -> (boolean)

Indicates whether to resolve the PagerDuty incident when you resolve the associated Incident Manager incident.

id -> (string)

The ID of the incident associated with the PagerDuty service for the response plan.

secretId -> (string)

The ID of the Amazon Web Services Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.

url -> (string)

The URL, if the related item is a non-Amazon Web Services resource.

title -> (string)

The title of the related item.

JSON Syntax:

```
[
  {
    "generatedId": "string",
    "identifier": {
      "type": "ANALYSIS"|"INCIDENT"|"METRIC"|"PARENT"|"ATTACHMENT"|"OTHER"|"AUTOMATION"|"INVOLVED_RESOURCE"|"TASK",
      "value": {
        "arn": "string",
        "metricDefinition": "string",
        "pagerDutyIncidentDetail": {
          "autoResolve": true|false,
          "id": "string",
          "secretId": "string"
        },
        "url": "string"
      }
    },
    "title": "string"
  }
  ...
]
```

`--response-plan-arn` (string)

The Amazon Resource Name (ARN) of the response plan that pre-defines summary, chat channels, Amazon SNS topics, runbooks, title, and impact of the incident.

`--title` (string)

Provide a title for the incident. Providing a title overwrites the title provided by the response plan.

`--trigger-details` (structure)

Details of what created the incident record in Incident Manager.

rawData -> (string)

Raw data passed from either Amazon EventBridge, Amazon CloudWatch, or Incident Manager when an incident is created.

source -> (string)

Identifies the service that sourced the event. All events sourced from within Amazon Web Services begin with â`aws.` â Customer-generated events can have any value here, as long as it doesnât begin with â`aws.` â We recommend the use of Java package-name style reverse domain-name strings.

timestamp -> (timestamp)

The timestamp for when the incident was detected.

triggerArn -> (string)

The Amazon Resource Name (ARN) of the source that detected the incident.

Shorthand Syntax:

```
rawData=string,source=string,timestamp=timestamp,triggerArn=string
```

JSON Syntax:

```
{
  "rawData": "string",
  "source": "string",
  "timestamp": timestamp,
  "triggerArn": "string"
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To start an incident**

The following `start-incident` example starts an incident using the specified response plan.

```
aws ssm-incidents start-incident \
    --response-plan-arn "arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"
```

Output:

```
{
    "incidentRecordArn": "arn:aws:ssm-incidents::682428703967:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"
}
```

For more information, see [Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html) in the *Incident Manager User Guide*.

## Output

incidentRecordArn -> (string)

The ARN of the newly created incident record.