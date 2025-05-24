# create-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# create-rule

## Description

Creates a rule for the specified Amazon Connect instance.

Use the [Rules Function language](https://docs.aws.amazon.com/connect/latest/APIReference/connect-rules-language.html) to code conditions for the rule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateRule)

## Synopsis

```
create-rule
--instance-id <value>
--name <value>
--trigger-event-source <value>
--function <value>
--actions <value>
--publish-status <value>
[--client-token <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--name` (string)

A unique name for the rule.

`--trigger-event-source` (structure)

The event source to trigger the rule.

EventSourceName -> (string)

The name of the event source.

IntegrationAssociationId -> (string)

The identifier for the integration association.

Shorthand Syntax:

```
EventSourceName=string,IntegrationAssociationId=string
```

JSON Syntax:

```
{
  "EventSourceName": "OnPostCallAnalysisAvailable"|"OnRealTimeCallAnalysisAvailable"|"OnRealTimeChatAnalysisAvailable"|"OnPostChatAnalysisAvailable"|"OnZendeskTicketCreate"|"OnZendeskTicketStatusUpdate"|"OnSalesforceCaseCreate"|"OnContactEvaluationSubmit"|"OnMetricDataUpdate"|"OnCaseCreate"|"OnCaseUpdate"|"OnSlaBreach",
  "IntegrationAssociationId": "string"
}
```

`--function` (string)

The conditions of the rule.

`--actions` (list)

A list of actions to be run when the rule is triggered.

(structure)

Information about the action to be performed when a rule is triggered.

ActionType -> (string)

The type of action that creates a rule.

TaskAction -> (structure)

Information about the task action. This field is required if `TriggerEventSource` is one of the following values: `OnZendeskTicketCreate` | `OnZendeskTicketStatusUpdate` | `OnSalesforceCaseCreate`

Name -> (string)

The name. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Amazon Connect Administrators Guide* .

Description -> (string)

The description. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Amazon Connect Administrators Guide* .

ContactFlowId -> (string)

The identifier of the flow.

References -> (map)

Information about the reference when the `referenceType` is `URL` . Otherwise, null. (Supports variable injection in the `Value` field.)

key -> (string)

value -> (structure)

Well-formed data on a contact, used by agents to complete a contact request. You can have up to 4,096 UTF-8 bytes across all references for a contact.

Value -> (string)

A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).

Type -> (string)

The type of the reference. `DATE` must be of type Epoch timestamp.

Status -> (string)

Status of the attachment reference type.

Arn -> (string)

The Amazon Resource Name (ARN) of the reference

StatusReason -> (string)

Relevant details why the reference was not successfully created.

EventBridgeAction -> (structure)

Information about the EventBridge action.

Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` | `OnRealTimeCallAnalysisAvailable` | `OnRealTimeChatAnalysisAvailable` | `OnPostChatAnalysisAvailable` | `OnContactEvaluationSubmit` | `OnMetricDataUpdate`

Name -> (string)

The name.

AssignContactCategoryAction -> (structure)

Information about the contact category action.

Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` | `OnRealTimeCallAnalysisAvailable` | `OnRealTimeChatAnalysisAvailable` | `OnPostChatAnalysisAvailable` | `OnZendeskTicketCreate` | `OnZendeskTicketStatusUpdate` | `OnSalesforceCaseCreate`

SendNotificationAction -> (structure)

Information about the send notification action.

Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` | `OnRealTimeCallAnalysisAvailable` | `OnRealTimeChatAnalysisAvailable` | `OnPostChatAnalysisAvailable` | `OnContactEvaluationSubmit` | `OnMetricDataUpdate`

DeliveryMethod -> (string)

Notification delivery method.

Subject -> (string)

The subject of the email if the delivery method is `EMAIL` . Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Amazon Connect Administrators Guide* .

Content -> (string)

Notification content. Supports variable injection. For more information, see [JSONPath reference](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html) in the *Amazon Connect Administrators Guide* .

ContentType -> (string)

Content type format.

Recipient -> (structure)

Notification recipient.

UserTags -> (map)

The tags used to organize, track, or control access for this resource. For example, { âTagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }. Amazon Connect users with the specified tags will be notified.

key -> (string)

value -> (string)

UserIds -> (list)

A list of user IDs. Supports variable injection of `$.ContactLens.ContactEvaluation.Agent.AgentId` for `OnContactEvaluationSubmit` event source.

(string)

CreateCaseAction -> (structure)

Information about the create case action.

Supported only for `TriggerEventSource` values: `OnPostCallAnalysisAvailable` | `OnPostChatAnalysisAvailable` .

Fields -> (list)

An array of objects with `Field ID` and `Value` data.

(structure)

Object for case field values.

Id -> (string)

Unique identifier of a field.

Value -> (structure)

Union of potential field value types.

BooleanValue -> (boolean)

A Boolean number value type.

DoubleValue -> (double)

A Double number value type.

EmptyValue -> (structure)

An empty value.

StringValue -> (string)

String value type.

TemplateId -> (string)

A unique identifier of a template.

UpdateCaseAction -> (structure)

Information about the update case action.

Supported only for `TriggerEventSource` values: `OnCaseCreate` | `OnCaseUpdate` .

Fields -> (list)

An array of objects with `Field ID` and Value data.

(structure)

Object for case field values.

Id -> (string)

Unique identifier of a field.

Value -> (structure)

Union of potential field value types.

BooleanValue -> (boolean)

A Boolean number value type.

DoubleValue -> (double)

A Double number value type.

EmptyValue -> (structure)

An empty value.

StringValue -> (string)

String value type.

AssignSlaAction -> (structure)

Information about the assign SLA action.

SlaAssignmentType -> (string)

Type of SLA assignment.

CaseSlaConfiguration -> (structure)

The SLA configuration for Case SLA Assignment.

Name -> (string)

Name of an SLA.

Type -> (string)

Type of SLA for Case SlaAssignmentType.

FieldId -> (string)

Unique identifier of a Case field.

TargetFieldValues -> (list)

Represents a list of target field values for the fieldId specified in CaseSlaConfiguration. The SLA is considered met if any one of these target field values matches the actual field value.

(structure)

Object to store union of Field values.

BooleanValue -> (boolean)

A Boolean number value type.

DoubleValue -> (double)

A Double number value type.

EmptyValue -> (structure)

An empty value.

StringValue -> (string)

String value type.

TargetSlaMinutes -> (long)

Target duration in minutes within which an SLA should be completed.

EndAssociatedTasksAction -> (structure)

Information about the end associated tasks action.

Supported only for `TriggerEventSource` values: `OnCaseUpdate` .

SubmitAutoEvaluationAction -> (structure)

Information about the submit automated evaluation action.

EvaluationFormId -> (string)

The identifier of the auto-evaluation enabled form.

JSON Syntax:

```
[
  {
    "ActionType": "CREATE_TASK"|"ASSIGN_CONTACT_CATEGORY"|"GENERATE_EVENTBRIDGE_EVENT"|"SEND_NOTIFICATION"|"CREATE_CASE"|"UPDATE_CASE"|"ASSIGN_SLA"|"END_ASSOCIATED_TASKS"|"SUBMIT_AUTO_EVALUATION",
    "TaskAction": {
      "Name": "string",
      "Description": "string",
      "ContactFlowId": "string",
      "References": {"string": {
            "Value": "string",
            "Type": "URL"|"ATTACHMENT"|"CONTACT_ANALYSIS"|"NUMBER"|"STRING"|"DATE"|"EMAIL"|"EMAIL_MESSAGE",
            "Status": "AVAILABLE"|"DELETED"|"APPROVED"|"REJECTED"|"PROCESSING"|"FAILED",
            "Arn": "string",
            "StatusReason": "string"
          }
        ...}
    },
    "EventBridgeAction": {
      "Name": "string"
    },
    "AssignContactCategoryAction": {

    },
    "SendNotificationAction": {
      "DeliveryMethod": "EMAIL",
      "Subject": "string",
      "Content": "string",
      "ContentType": "PLAIN_TEXT",
      "Recipient": {
        "UserTags": {"string": "string"
          ...},
        "UserIds": ["string", ...]
      }
    },
    "CreateCaseAction": {
      "Fields": [
        {
          "Id": "string",
          "Value": {
            "BooleanValue": true|false,
            "DoubleValue": double,
            "EmptyValue": {

            },
            "StringValue": "string"
          }
        }
        ...
      ],
      "TemplateId": "string"
    },
    "UpdateCaseAction": {
      "Fields": [
        {
          "Id": "string",
          "Value": {
            "BooleanValue": true|false,
            "DoubleValue": double,
            "EmptyValue": {

            },
            "StringValue": "string"
          }
        }
        ...
      ]
    },
    "AssignSlaAction": {
      "SlaAssignmentType": "CASES",
      "CaseSlaConfiguration": {
        "Name": "string",
        "Type": "CaseField",
        "FieldId": "string",
        "TargetFieldValues": [
          {
            "BooleanValue": true|false,
            "DoubleValue": double,
            "EmptyValue": {

            },
            "StringValue": "string"
          }
          ...
        ],
        "TargetSlaMinutes": long
      }
    },
    "EndAssociatedTasksAction": {

    },
    "SubmitAutoEvaluationAction": {
      "EvaluationFormId": "string"
    }
  }
  ...
]
```

`--publish-status` (string)

The publish status of the rule.

Possible values:

- `DRAFT`
- `PUBLISHED`

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

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

RuleArn -> (string)

The Amazon Resource Name (ARN) of the rule.

RuleId -> (string)

A unique identifier for the rule.