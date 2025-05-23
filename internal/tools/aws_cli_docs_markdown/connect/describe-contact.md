# describe-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# describe-contact

## Description

This API is in preview release for Amazon Connect and is subject to change.

Describes the specified contact.

### Warning

- `SystemEndpoint` is not populated for contacts with initiation method of MONITOR, QUEUE_TRANSFER, or CALLBACK
- Contact information remains available in Amazon Connect for 24 months from the `InitiationTimestamp` , and then it is deleted. Only contact information that is available in Amazon Connect is returned by this API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/DescribeContact)

## Synopsis

```
describe-contact
--instance-id <value>
--contact-id <value>
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

`--contact-id` (string)

The identifier of the contact.

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

Contact -> (structure)

Information about the contact.

Arn -> (string)

The Amazon Resource Name (ARN) for the contact.

Id -> (string)

The identifier for the contact.

InitialContactId -> (string)

If this contact is related to other contacts, this is the ID of the initial contact.

PreviousContactId -> (string)

If this contact is not the first contact, this is the ID of the previous contact.

ContactAssociationId -> (string)

This is the root contactId which is used as a unique identifier for all subsequent contacts in a contact tree.

InitiationMethod -> (string)

Indicates how the contact was initiated.

Name -> (string)

The name of the contact.

Description -> (string)

The description of the contact.

Channel -> (string)

How the contact reached your contact center.

QueueInfo -> (structure)

If this contact was queued, this contains information about the queue.

Id -> (string)

The unique identifier for the queue.

EnqueueTimestamp -> (timestamp)

The timestamp when the contact was added to the queue.

AgentInfo -> (structure)

Information about the agent who accepted the contact.

Id -> (string)

The identifier of the agent who accepted the contact.

ConnectedToAgentTimestamp -> (timestamp)

The timestamp when the contact was connected to the agent.

AgentPauseDurationInSeconds -> (integer)

Agent pause duration for a contact in seconds.

HierarchyGroups -> (structure)

The agent hierarchy groups for the agent.

Level1 -> (structure)

The group at level one of the agent hierarchy.

Arn -> (string)

The Amazon Resource Name (ARN) of the group.

Level2 -> (structure)

The group at level two of the agent hierarchy.

Arn -> (string)

The Amazon Resource Name (ARN) of the group.

Level3 -> (structure)

The group at level three of the agent hierarchy.

Arn -> (string)

The Amazon Resource Name (ARN) of the group.

Level4 -> (structure)

The group at level four of the agent hierarchy.

Arn -> (string)

The Amazon Resource Name (ARN) of the group.

Level5 -> (structure)

The group at level five of the agent hierarchy.

Arn -> (string)

The Amazon Resource Name (ARN) of the group.

DeviceInfo -> (structure)

Information regarding Agentâs device.

PlatformName -> (string)

Name of the platform that the participant used for the call.

PlatformVersion -> (string)

Version of the platform that the participant used for the call.

OperatingSystem -> (string)

Operating system that the participant used for the call.

Capabilities -> (structure)

The configuration for the allowed video and screen sharing capabilities for participants present over the call. For more information, see [Set up in-app, web, video calling, and screen sharing capabilities](https://docs.aws.amazon.com/connect/latest/adminguide/inapp-calling.html) in the *Amazon Connect Administrator Guide* .

Video -> (string)

The configuration having the video and screen sharing capabilities for participants over the call.

ScreenShare -> (string)

The screen sharing capability that is enabled for the participant. `SEND` indicates the participant can share their screen.

AfterContactWorkDuration -> (integer)

The difference in time, in whole seconds, between `AfterContactWorkStartTimestamp` and `AfterContactWorkEndTimestamp` .

AfterContactWorkStartTimestamp -> (timestamp)

The date and time when the agent started doing After Contact Work for the contact, in UTC time.

AfterContactWorkEndTimestamp -> (timestamp)

The date and time when the agent ended After Contact Work for the contact, in UTC time. In cases when agent finishes doing `AfterContactWork` for chat contacts and switches their activity status to offline or equivalent without clearing the contact in CCP, discrepancies may be noticed for `AfterContactWorkEndTimestamp` .

AgentInitiatedHoldDuration -> (integer)

The total hold duration in seconds initiated by the agent.

StateTransitions -> (list)

List of `StateTransition` for a supervisor.

(structure)

Information about the state transition of a supervisor.

State -> (string)

The state of the transition.

StateStartTimestamp -> (timestamp)

The date and time when the state started in UTC time.

StateEndTimestamp -> (timestamp)

The date and time when the state ended in UTC time.

InitiationTimestamp -> (timestamp)

The date and time this contact was initiated, in UTC time. For `INBOUND` , this is when the contact arrived. For `OUTBOUND` , this is when the agent began dialing. For `CALLBACK` , this is when the callback contact was created. For `TRANSFER` and `QUEUE_TRANSFER` , this is when the transfer was initiated. For `API` , this is when the request arrived. For `EXTERNAL_OUTBOUND` , this is when the agent started dialing the external participant. For `MONITOR` , this is when the supervisor started listening to a contact.

DisconnectTimestamp -> (timestamp)

The date and time that the customer endpoint disconnected from the current contact, in UTC time. In transfer scenarios, the DisconnectTimestamp of the previous contact indicates the date and time when that contact ended.

LastUpdateTimestamp -> (timestamp)

The timestamp when contact was last updated.

LastPausedTimestamp -> (timestamp)

The timestamp when the contact was last paused.

LastResumedTimestamp -> (timestamp)

The timestamp when the contact was last resumed.

TotalPauseCount -> (integer)

Total pause count for a contact.

TotalPauseDurationInSeconds -> (integer)

Total pause duration for a contact in seconds.

ScheduledTimestamp -> (timestamp)

The timestamp, in Unix epoch time format, at which to start running the inbound flow.

RelatedContactId -> (string)

The contactId that is [related](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html#relatedcontactid) to this contact.

WisdomInfo -> (structure)

Information about Amazon Connect Wisdom.

SessionArn -> (string)

The Amazon Resource Name (ARN) of the Wisdom session.

CustomerId -> (string)

The customerâs identification number. For example, the `CustomerId` may be a customer number from your CRM. You can create a Lambda function to pull the unique customer ID of the caller from your CRM system. If you enable Amazon Connect Voice ID capability, this attribute is populated with the `CustomerSpeakerId` of the caller.

CustomerEndpoint -> (structure)

The customer or external third party participant endpoint.

Type -> (string)

Type of endpoint.

Address -> (string)

Address of the endpoint.

DisplayName -> (string)

Display name of the endpoint.

SystemEndpoint -> (structure)

The system endpoint. For `INBOUND` , this is the phone number or email address that the customer dialed. For `OUTBOUND` and `EXTERNAL_OUTBOUND` , this is the outbound caller ID number assigned to the outbound queue that is used to dial the customer. For callback, this shows up as Softphone for calls handled by agents with softphone.

Type -> (string)

Type of endpoint.

Address -> (string)

Address of the endpoint.

DisplayName -> (string)

Display name of the endpoint.

QueueTimeAdjustmentSeconds -> (integer)

An integer that represents the queue time adjust to be applied to the contact, in seconds (longer / larger queue time are routed preferentially). Cannot be specified if the QueuePriority is specified. Must be statically defined and a valid integer value.

QueuePriority -> (long)

An integer that represents the queue priority to be applied to the contact (lower priorities are routed preferentially). Cannot be specified if the QueueTimeAdjustmentSeconds is specified. Must be statically defined, must be larger than zero, and a valid integer value. Default Value is 5.

Tags -> (map)

Tags associated with the contact. This contains both Amazon Web Services generated and user-defined tags.

key -> (string)

value -> (string)

ConnectedToSystemTimestamp -> (timestamp)

The timestamp when customer endpoint connected to Amazon Connect.

RoutingCriteria -> (structure)

Latest routing criteria on the contact.

Steps -> (list)

List of routing steps. When Amazon Connect does not find an available agent meeting the requirements in a step for a given step duration, the routing criteria will move on to the next step sequentially until a join is completed with an agent. When all steps are exhausted, the contact will be offered to any agent in the queue.

(structure)

Step signifies the criteria to be used for routing to an agent

Expiry -> (structure)

An object to specify the expiration of a routing step.

DurationInSeconds -> (integer)

The number of seconds to wait before expiring the routing step.

ExpiryTimestamp -> (timestamp)

The timestamp indicating when the routing step expires.

Expression -> (structure)

A tagged union to specify expression for a routing step.

AttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

AndExpression -> (list)

List of routing expressions which will be AND-ed together.

(structure)

A tagged union to specify expression for a routing step.

AttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

AndExpression -> (list)

List of routing expressions which will be AND-ed together.

( â¦ recursive â¦ )

OrExpression -> (list)

List of routing expressions which will be OR-ed together.

( â¦ recursive â¦ )

NotAttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

OrExpression -> (list)

List of routing expressions which will be OR-ed together.

(structure)

A tagged union to specify expression for a routing step.

AttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

AndExpression -> (list)

List of routing expressions which will be AND-ed together.

( â¦ recursive â¦ )

OrExpression -> (list)

List of routing expressions which will be OR-ed together.

( â¦ recursive â¦ )

NotAttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

NotAttributeCondition -> (structure)

An object to specify the predefined attribute condition.

Name -> (string)

The name of predefined attribute.

Value -> (string)

The value of predefined attribute.

ProficiencyLevel -> (float)

The proficiency level of the condition.

Range -> (structure)

An Object to define the minimum and maximum proficiency levels.

MinProficiencyLevel -> (float)

The minimum proficiency level of the range.

MaxProficiencyLevel -> (float)

The maximum proficiency level of the range.

MatchCriteria -> (structure)

An object to define `AgentsCriteria` .

AgentsCriteria -> (structure)

An object to define agentIds.

AgentIds -> (list)

An object to specify a list of agents, by user ID.

(string)

ComparisonOperator -> (string)

The operator of the condition.

Status -> (string)

Represents status of the Routing step.

ActivationTimestamp -> (timestamp)

The timestamp indicating when the routing criteria is set to active. A routing criteria is activated when contact is transferred to a queue. ActivationTimestamp will be set on routing criteria for contacts in agent queue even though Routing criteria is never activated for contacts in agent queue.

Index -> (integer)

Information about the index of the routing criteria.

Customer -> (structure)

Information about the Customer on the contact.

DeviceInfo -> (structure)

Information regarding Customerâs device.

PlatformName -> (string)

Name of the platform that the participant used for the call.

PlatformVersion -> (string)

Version of the platform that the participant used for the call.

OperatingSystem -> (string)

Operating system that the participant used for the call.

Capabilities -> (structure)

The configuration for the allowed video and screen sharing capabilities for participants present over the call. For more information, see [Set up in-app, web, video calling, and screen sharing capabilities](https://docs.aws.amazon.com/connect/latest/adminguide/inapp-calling.html) in the *Amazon Connect Administrator Guide* .

Video -> (string)

The configuration having the video and screen sharing capabilities for participants over the call.

ScreenShare -> (string)

The screen sharing capability that is enabled for the participant. `SEND` indicates the participant can share their screen.

Campaign -> (structure)

Information associated with a campaign.

CampaignId -> (string)

A unique identifier for a campaign.

AnsweringMachineDetectionStatus -> (string)

Indicates how an [outbound campaign](https://docs.aws.amazon.com/connect/latest/adminguide/how-to-create-campaigns.html) call is actually disposed if the contact is connected to Amazon Connect.

CustomerVoiceActivity -> (structure)

Information about customerâs voice activity.

GreetingStartTimestamp -> (timestamp)

Timestamp that measures the beginning of the customer greeting from an outbound voice call.

GreetingEndTimestamp -> (timestamp)

Timestamp that measures the end of the customer greeting from an outbound voice call.

QualityMetrics -> (structure)

Information about the quality of the participantâs media connection.

Agent -> (structure)

Information about the quality of Agent media connection.

Audio -> (structure)

Information about the audio quality of the Agent

QualityScore -> (float)

Number measuring the estimated quality of the media connection.

PotentialQualityIssues -> (list)

List of potential issues causing degradation of quality on a media connection. If the service did not detect any potential quality issues the list is empty.

Valid values: `HighPacketLoss` | `HighRoundTripTime` | `HighJitterBuffer`

(string)

Customer -> (structure)

Information about the quality of Customer media connection.

Audio -> (structure)

Information about the audio quality of the Customer

QualityScore -> (float)

Number measuring the estimated quality of the media connection.

PotentialQualityIssues -> (list)

List of potential issues causing degradation of quality on a media connection. If the service did not detect any potential quality issues the list is empty.

Valid values: `HighPacketLoss` | `HighRoundTripTime` | `HighJitterBuffer`

(string)

DisconnectDetails -> (structure)

Information about the call disconnect experience.

PotentialDisconnectIssue -> (string)

Indicates the potential disconnection issues for a call. This field is not populated if the service does not detect potential issues.

AdditionalEmailRecipients -> (structure)

List of additional email addresses for an email contact.

ToList -> (list)

List of additional TO email recipients for an email contact.

(structure)

Information about the email recipient

Address -> (string)

Address of the email recipient.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

DisplayName -> (string)

Display name of the email recipient.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

CcList -> (list)

List of additional CC email recipients for an email contact.

(structure)

Information about the email recipient

Address -> (string)

Address of the email recipient.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

DisplayName -> (string)

Display name of the email recipient.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

SegmentAttributes -> (map)

A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Amazon Connect attributes and can be accessed in flows. Attribute keys can include only alphanumeric, -, and _ characters. This field can be used to show channel subtype. For example, `connect:Guide` or `connect:SMS` .

key -> (string)

value -> (structure)

A value for a segment attribute. This is structured as a map where the key is `valueString` and the value is a string.

ValueString -> (string)

The value of a segment attribute.

ValueMap -> (map)

The value of a segment attribute.

key -> (string)

value -> (structure)

A value for a segment attribute. This is structured as a map where the key is `valueString` and the value is a string.

ValueString -> (string)

The value of a segment attribute.

ValueMap -> (map)

The value of a segment attribute.

key -> (string)

( â¦ recursive â¦ )

ValueInteger -> (integer)

The value of a segment attribute.

ValueInteger -> (integer)

The value of a segment attribute.

Recordings -> (list)

If recording was enabled, this is information about the recordings.

(structure)

Information about a voice recording, chat transcript, or screen recording.

StorageType -> (string)

Where the recording/transcript is stored.

Location -> (string)

The location, in Amazon S3, for the recording/transcript.

MediaStreamType -> (string)

Information about the media stream used during the conversation.

ParticipantType -> (string)

Information about the conversation participant, whether they are an agent or contact. The participant types are as follows:

- All
- Manager
- Agent
- Customer
- Thirdparty
- Supervisor

FragmentStartNumber -> (string)

The number that identifies the Kinesis Video Streams fragment where the customer audio stream started.

FragmentStopNumber -> (string)

The number that identifies the Kinesis Video Streams fragment where the customer audio stream stopped.

StartTimestamp -> (timestamp)

When the conversation of the last leg of the recording started in UTC time.

StopTimestamp -> (timestamp)

When the conversation of the last leg of recording stopped in UTC time.

Status -> (string)

The status of the recording/transcript.

DeletionReason -> (string)

If the recording/transcript was deleted, this is the reason entered for the deletion.

DisconnectReason -> (string)

The disconnect reason for the contact.

ContactEvaluations -> (map)

Information about the contact evaluations where the key is the FormId, which is a unique identifier for the form.

key -> (string)

value -> (structure)

Information about the contact evaluations where the key is the FormId, which is a unique identifier for the form.

FormId -> (string)

The `FormId` of the contact evaluation.

EvaluationArn -> (string)

The Amazon Resource Name for the evaluation form. It is always present.

Status -> (string)

The status of the evaluation.

StartTimestamp -> (timestamp)

The date and time when the evaluation was started, in UTC time.

EndTimestamp -> (timestamp)

The date and time when the evaluation was submitted, in UTC time.

DeleteTimestamp -> (timestamp)

The date and time when the evaluation was deleted, in UTC time.

ExportLocation -> (string)

The path where evaluation was exported.

ContactDetails -> (structure)

A map of string key/value pairs that contain user-defined attributes which are lightly typed within the contact. This object is used only for task contacts.

Name -> (string)

The name of the contact details.

Description -> (string)

Teh description of the contact details.

Attributes -> (map)

The attributes of the contact.

key -> (string)

value -> (string)