# create-response-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-response-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-response-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-incidents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/index.html#cli-aws-ssm-incidents) ]

# create-response-plan

## Description

Creates a response plan that automates the initial response to incidents. A response plan engages contacts, starts chat channel collaboration, and initiates runbooks at the beginning of an incident.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-incidents-2018-05-10/CreateResponsePlan)

## Synopsis

```
create-response-plan
[--actions <value>]
[--chat-channel <value>]
[--client-token <value>]
[--display-name <value>]
[--engagements <value>]
--incident-template <value>
[--integrations <value>]
--name <value>
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

`--actions` (list)

The actions that the response plan starts at the beginning of an incident.

(tagged union structure)

The action that starts at the beginning of an incident. The response plan defines the action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ssmAutomation`.

ssmAutomation -> (structure)

The Systems Manager automation document to start as the runbook at the beginning of the incident.

documentName -> (string)

The automation documentâs name.

documentVersion -> (string)

The automation documentâs version to use when running.

dynamicParameters -> (map)

The key-value pair to resolve dynamic parameter values when processing a Systems Manager Automation runbook.

key -> (string)

value -> (tagged union structure)

The dynamic SSM parameter value.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `variable`.

variable -> (string)

Variable dynamic parameters. A parameter value is determined when an incident is created.

parameters -> (map)

The key-value pair parameters to use when running the automation document.

key -> (string)

value -> (list)

(string)

roleArn -> (string)

The Amazon Resource Name (ARN) of the role that the automation document will assume when running commands.

targetAccount -> (string)

The account that the automation document will be run in. This can be in either the management account or an application account.

Shorthand Syntax:

```
ssmAutomation={documentName=string,documentVersion=string,dynamicParameters={KeyName1={variable=string},KeyName2={variable=string}},parameters={KeyName1=[string,string],KeyName2=[string,string]},roleArn=string,targetAccount=string} ...
```

JSON Syntax:

```
[
  {
    "ssmAutomation": {
      "documentName": "string",
      "documentVersion": "string",
      "dynamicParameters": {"string": {
            "variable": "INCIDENT_RECORD_ARN"|"INVOLVED_RESOURCES"
          }
        ...},
      "parameters": {"string": ["string", ...]
        ...},
      "roleArn": "string",
      "targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT"|"IMPACTED_ACCOUNT"
    }
  }
  ...
]
```

`--chat-channel` (tagged union structure)

The Chatbot chat channel used for collaboration during an incident.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `chatbotSns`, `empty`.

chatbotSns -> (list)

The Amazon SNS targets that Chatbot uses to notify the chat channel of updates to an incident. You can also make updates to the incident through the chat channel by using the Amazon SNS topics.

(string)

empty -> (structure)

Used to remove the chat channel from an incident record or response plan.

Shorthand Syntax:

```
chatbotSns=string,string,empty={}
```

JSON Syntax:

```
{
  "chatbotSns": ["string", ...],
  "empty": {

  }
}
```

`--client-token` (string)

A token ensuring that the operation is called only once with the specified details.

`--display-name` (string)

The long format of the response plan name. This field can contain spaces.

`--engagements` (list)

The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.

(string)

Syntax:

```
"string" "string" ...
```

`--incident-template` (structure)

Details used to create an incident when using this response plan.

dedupeString -> (string)

The string Incident Manager uses to prevent the same root cause from creating multiple incidents in the same account.

A deduplication string is a term or phrase the system uses to check for duplicate incidents. If you specify a deduplication string, Incident Manager searches for open incidents that contain the same string in the `dedupeString` field when it creates the incident. If a duplicate is detected, Incident Manager deduplicates the newer incident into the existing incident.

### Note

By default, Incident Manager automatically deduplicates multiple incidents created by the same Amazon CloudWatch alarm or Amazon EventBridge event. You donât have to enter your own deduplication string to prevent duplication for these resource types.

impact -> (integer)

The impact of the incident on your customers and applications.

**Supported impact codes**

- `1` - Critical
- `2` - High
- `3` - Medium
- `4` - Low
- `5` - No Impact

incidentTags -> (map)

Tags to assign to the template. When the `StartIncident` API action is called, Incident Manager assigns the tags specified in the template to the incident.

key -> (string)

value -> (string)

notificationTargets -> (list)

The Amazon SNS targets that are notified when updates are made to an incident.

(tagged union structure)

The SNS targets that are notified when updates are made to an incident.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `snsTopicArn`.

snsTopicArn -> (string)

The Amazon Resource Name (ARN) of the SNS topic.

summary -> (string)

The summary of the incident. The summary is a brief synopsis of what occurred, whatâs currently happening, and context.

title -> (string)

The title of the incident.

Shorthand Syntax:

```
dedupeString=string,impact=integer,incidentTags={KeyName1=string,KeyName2=string},notificationTargets=[{snsTopicArn=string},{snsTopicArn=string}],summary=string,title=string
```

JSON Syntax:

```
{
  "dedupeString": "string",
  "impact": integer,
  "incidentTags": {"string": "string"
    ...},
  "notificationTargets": [
    {
      "snsTopicArn": "string"
    }
    ...
  ],
  "summary": "string",
  "title": "string"
}
```

`--integrations` (list)

Information about third-party services integrated into the response plan.

(tagged union structure)

Information about third-party services integrated into a response plan.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `pagerDutyConfiguration`.

pagerDutyConfiguration -> (structure)

Information about the PagerDuty service where the response plan creates an incident.

name -> (string)

The name of the PagerDuty configuration.

pagerDutyIncidentConfiguration -> (structure)

Details about the PagerDuty service associated with the configuration.

serviceId -> (string)

The ID of the PagerDuty service that the response plan associates with an incident when it launches.

secretId -> (string)

The ID of the Amazon Web Services Secrets Manager secret that stores your PagerDuty key, either a General Access REST API Key or User Token REST API Key, and other user credentials.

Shorthand Syntax:

```
pagerDutyConfiguration={name=string,pagerDutyIncidentConfiguration={serviceId=string},secretId=string} ...
```

JSON Syntax:

```
[
  {
    "pagerDutyConfiguration": {
      "name": "string",
      "pagerDutyIncidentConfiguration": {
        "serviceId": "string"
      },
      "secretId": "string"
    }
  }
  ...
]
```

`--name` (string)

The short format name of the response plan. Canât include spaces.

`--tags` (map)

A list of tags that you are adding to the response plan.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To create a response plan**

The following `create-response-plan` example creates a response plan with the specified details.

```
aws ssm-incidents create-response-plan \
    --chat-channel '{"chatbotSns": ["arn:aws:sns:us-east-1:111122223333:Standard_User"]}' \
    --display-name "Example response plan" \
    --incident-template '{"impact": 5, "title": "example-incident"}' \
    --name "example-response" \
    --actions '[{"ssmAutomation": {"documentName": "AWSIncidents-CriticalIncidentRunbookTemplate", "documentVersion": "$DEFAULT", "roleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm-incidents.amazonaws.com/AWSServiceRoleForIncidentManager", "targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT"}}]' \
    --engagements '["arn:aws:ssm-contacts:us-east-1:111122223333:contact/example"]'
```

Output:

```
{
    "arn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response"
}
```

For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html) in the *Incident Manager User Guide*.

## Output

arn -> (string)

The Amazon Resource Name (ARN) of the response plan.