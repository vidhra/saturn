# get-metric-data-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-metric-data-v2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-metric-data-v2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# get-metric-data-v2

## Description

Gets metric data from the specified Amazon Connect instance.

`GetMetricDataV2` offers more features than [GetMetricData](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricData.html) , the previous version of this API. It has new metrics, offers filtering at a metric level, and offers the ability to filter and group data by channels, queues, routing profiles, agents, and agent hierarchy levels. It can retrieve historical data for the last 3 months, at varying intervals. It does not support agent queues.

For a description of the historical metrics that are supported by `GetMetricDataV2` and `GetMetricData` , see [Metrics definitions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetMetricDataV2)

## Synopsis

```
get-metric-data-v2
--resource-arn <value>
--start-time <value>
--end-time <value>
[--interval <value>]
--filters <value>
[--groupings <value>]
--metrics <value>
[--next-token <value>]
[--max-results <value>]
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

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the resource. This includes the `instanceId` an Amazon Connect instance.

`--start-time` (timestamp)

The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be before the end time timestamp. The start and end time depends on the `IntervalPeriod` selected. By default the time range between start and end time is 35 days. Historical metrics are available for 3 months.

`--end-time` (timestamp)

The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be later than the start time timestamp. It cannot be later than the current timestamp.

`--interval` (structure)

The interval period and timezone to apply to returned metrics.

- `IntervalPeriod` : An aggregated grouping applied to request metrics. Valid `IntervalPeriod` values are: `FIFTEEN_MIN` | `THIRTY_MIN` | `HOUR` | `DAY` | `WEEK` | `TOTAL` .  For example, if `IntervalPeriod` is selected `THIRTY_MIN` , `StartTime` and `EndTime` differs by 1 day, then Amazon Connect returns 48 results in the response. Each result is aggregated by the THIRTY_MIN period. By default Amazon Connect aggregates results based on the `TOTAL` interval period.  The following list describes restrictions on `StartTime` and `EndTime` based on which `IntervalPeriod` is requested.
- `FIFTEEN_MIN` : The difference between `StartTime` and `EndTime` must be less than 3 days.
- `THIRTY_MIN` : The difference between `StartTime` and `EndTime` must be less than 3 days.
- `HOUR` : The difference between `StartTime` and `EndTime` must be less than 3 days.
- `DAY` : The difference between `StartTime` and `EndTime` must be less than 35 days.
- `WEEK` : The difference between `StartTime` and `EndTime` must be less than 35 days.
- `TOTAL` : The difference between `StartTime` and `EndTime` must be less than 35 days.
- `TimeZone` : The timezone applied to requested metrics.

TimeZone -> (string)

The timezone applied to requested metrics.

IntervalPeriod -> (string)

`IntervalPeriod` : An aggregated grouping applied to request metrics. Valid `IntervalPeriod` values are: `FIFTEEN_MIN` | `THIRTY_MIN` | `HOUR` | `DAY` | `WEEK` | `TOTAL` .

For example, if `IntervalPeriod` is selected `THIRTY_MIN` , `StartTime` and `EndTime` differs by 1 day, then Amazon Connect returns 48 results in the response. Each result is aggregated by the THIRTY_MIN period. By default Amazon Connect aggregates results based on the `TOTAL` interval period.

The following list describes restrictions on `StartTime` and `EndTime` based on what `IntervalPeriod` is requested.

- `FIFTEEN_MIN` : The difference between `StartTime` and `EndTime` must be less than 3 days.
- `THIRTY_MIN` : The difference between `StartTime` and `EndTime` must be less than 3 days.
- `HOUR` : The difference between `StartTime` and `EndTime` must be less than 3 days.
- `DAY` : The difference between `StartTime` and `EndTime` must be less than 35 days.
- `WEEK` : The difference between `StartTime` and `EndTime` must be less than 35 days.
- `TOTAL` : The difference between `StartTime` and `EndTime` must be less than 35 days.

Shorthand Syntax:

```
TimeZone=string,IntervalPeriod=string
```

JSON Syntax:

```
{
  "TimeZone": "string",
  "IntervalPeriod": "FIFTEEN_MIN"|"THIRTY_MIN"|"HOUR"|"DAY"|"WEEK"|"TOTAL"
}
```

`--filters` (list)

The filters to apply to returned metrics. You can filter on the following resources:

- Agents
- Campaigns
- Channels
- Feature
- Queues
- Routing profiles
- Routing step expression
- User hierarchy groups

At least one filter must be passed from queues, routing profiles, agents, or user hierarchy groups.

For metrics for outbound campaigns analytics, you can also use campaigns to satisfy at least one filter requirement.

To filter by phone number, see [Create a historical metrics report](https://docs.aws.amazon.com/connect/latest/adminguide/create-historical-metrics-report.html) in the *Amazon Connect Administrator Guide* .

Note the following limits:

- **Filter keys** : A maximum of 5 filter keys are supported in a single request. Valid filter keys: `AGENT` | `AGENT_HIERARCHY_LEVEL_ONE` | `AGENT_HIERARCHY_LEVEL_TWO` | `AGENT_HIERARCHY_LEVEL_THREE` | `AGENT_HIERARCHY_LEVEL_FOUR` | `AGENT_HIERARCHY_LEVEL_FIVE` | `ANSWERING_MACHINE_DETECTION_STATUS` | `BOT_ID` | `BOT_ALIAS` | `BOT_VERSION` | `BOT_LOCALE` | `BOT_INTENT_NAME` | `CAMPAIGN` | `CAMPAIGN_DELIVERY_EVENT_TYPE` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-metric-data-v2.html#id1)`CASE_TEMPLATE_ARN` | `CASE_STATUS` | `CHANNEL` | `contact/segmentAttributes/connect:Subtype` | `DISCONNECT_REASON` | `EVALUATION_FORM` | `EVALUATION_SECTION` | `EVALUATION_QUESTION` | `EVALUATION_SOURCE` | `FEATURE` | `FLOW_ACTION_ID` | `FLOW_TYPE` | `FLOWS_MODULE_RESOURCE_ID` | `FLOWS_NEXT_RESOURCE_ID` | `FLOWS_NEXT_RESOURCE_QUEUE_ID` | `FLOWS_OUTCOME_TYPE` | `FLOWS_RESOURCE_ID` | `FORM_VERSION` | `INITIATION_METHOD` | `INVOKING_RESOURCE_PUBLISHED_TIMESTAMP` | `INVOKING_RESOURCE_TYPE` | `PARENT_FLOWS_RESOURCE_ID` | `RESOURCE_PUBLISHED_TIMESTAMP` | `ROUTING_PROFILE` | `ROUTING_STEP_EXPRESSION` | `QUEUE` | `Q_CONNECT_ENABLED` |
- **Filter values** : A maximum of 100 filter values are supported in a single request. VOICE, CHAT, and TASK are valid `filterValue` for the CHANNEL filter key. They do not count towards limitation of 100 filter values. For example, a GetMetricDataV2 request can filter by 50 queues, 35 agents, and 15 routing profiles for a total of 100 filter values, along with 3 channel filters.   `contact_lens_conversational_analytics` is a valid filterValue for the `FEATURE` filter key. It is available only to contacts analyzed by Contact Lens conversational analytics.  `connect:Chat` , `connect:SMS` , `connect:Telephony` , and `connect:WebRTC` are valid `filterValue` examples (not exhaustive) for the `contact/segmentAttributes/connect:Subtype filter` key.  `ROUTING_STEP_EXPRESSION` is a valid filter key with a filter value up to 3000 length. This filter is case and order sensitive. JSON string fields must be sorted in ascending order and JSON array order should be kept as is.  `Q_CONNECT_ENABLED` . TRUE and FALSE are the only valid filterValues for the `Q_CONNECT_ENABLED` filter key.
- TRUE includes all contacts that had Amazon Q in Connect enabled as part of the flow.
- FALSE includes all contacts that did not have Amazon Q in Connect enabled as part of the flow

This filter is available only for contact record-driven metrics.

[Campaign](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns_Campaign.html) ARNs are valid `filterValues` for the `CAMPAIGN` filter key.

(structure)

Contains the filter to apply when retrieving metrics with the [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API.

FilterKey -> (string)

The key to use for filtering data. For example, `QUEUE` , `ROUTING_PROFILE, AGENT` , `CHANNEL` , `AGENT_HIERARCHY_LEVEL_ONE` , `AGENT_HIERARCHY_LEVEL_TWO` , `AGENT_HIERARCHY_LEVEL_THREE` , `AGENT_HIERARCHY_LEVEL_FOUR` , `AGENT_HIERARCHY_LEVEL_FIVE` . There must be at least 1 key and a maximum 5 keys.

FilterValues -> (list)

The identifiers to use for filtering data. For example, if you have a filter key of `QUEUE` , you would add queue IDs or ARNs in `FilterValues` .

(string)

Shorthand Syntax:

```
FilterKey=string,FilterValues=string,string ...
```

JSON Syntax:

```
[
  {
    "FilterKey": "string",
    "FilterValues": ["string", ...]
  }
  ...
]
```

`--groupings` (list)

The grouping applied to the metrics that are returned. For example, when results are grouped by queue, the metrics returned are grouped by queue. The values that are returned apply to the metrics for each queue. They are not aggregated for all queues.

If no grouping is specified, a summary of all metrics is returned.

Valid grouping keys: `AGENT` | `AGENT_HIERARCHY_LEVEL_ONE` | `AGENT_HIERARCHY_LEVEL_TWO` | `AGENT_HIERARCHY_LEVEL_THREE` | `AGENT_HIERARCHY_LEVEL_FOUR` | `AGENT_HIERARCHY_LEVEL_FIVE` | `ANSWERING_MACHINE_DETECTION_STATUS` | `BOT_ID` | `BOT_ALIAS` | `BOT_VERSION` | `BOT_LOCALE` | `BOT_INTENT_NAME` | `CAMPAIGN` | `CAMPAIGN_DELIVERY_EVENT_TYPE` | `CASE_TEMPLATE_ARN` | `CASE_STATUS` | `CHANNEL` | `contact/segmentAttributes/connect:Subtype` | `DISCONNECT_REASON` | `EVALUATION_FORM` | `EVALUATION_SECTION` | `EVALUATION_QUESTION` | `EVALUATION_SOURCE` | `FLOWS_RESOURCE_ID` | `FLOWS_MODULE_RESOURCE_ID` | `FLOW_ACTION_ID` | `FLOW_TYPE` | `FLOWS_OUTCOME_TYPE` | `FORM_VERSION` | `INITIATION_METHOD` | `INVOKING_RESOURCE_PUBLISHED_TIMESTAMP` | `INVOKING_RESOURCE_TYPE` | `PARENT_FLOWS_RESOURCE_ID` | `Q_CONNECT_ENABLED` | `QUEUE` | `RESOURCE_PUBLISHED_TIMESTAMP` | `ROUTING_PROFILE` | `ROUTING_STEP_EXPRESSION`

Type: Array of strings

Array Members: Maximum number of 4 items

Required: No

(string)

Syntax:

```
"string" "string" ...
```

`--metrics` (list)

The metrics to retrieve. Specify the name, groupings, and filters for each metric. The following historical metrics are available. For a description of each metric, see [Metrics definition](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html) in the *Amazon Connect Administrator Guide* .

ABANDONMENT_RATE

Unit: Percent

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Abandonment rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#abandonment-rate)

AGENT_ADHERENT_TIME

This metric is available only in Amazon Web Services Regions where [Forecasting, capacity planning, and scheduling](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#optimization_region) is available.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Adherent time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#adherent-time)

AGENT_ANSWER_RATE

Unit: Percent

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Agent answer rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-answer-rate)

AGENT_NON_ADHERENT_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Non-adherent time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-adherent-time)

AGENT_NON_RESPONSE

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Agent non-response](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response)

AGENT_NON_RESPONSE_WITHOUT_CUSTOMER_ABANDONS

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

Data for this metric is available starting from October 1, 2023 0:00:00 GMT.

UI name: [Agent non-response without customer abandons](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response-without-customer-abandons)

AGENT_OCCUPANCY

Unit: Percentage

Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy

UI name: [Occupancy](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#occupancy)

AGENT_SCHEDULE_ADHERENCE

This metric is available only in Amazon Web Services Regions where [Forecasting, capacity planning, and scheduling](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#optimization_region) is available.

Unit: Percent

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Adherence](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#adherence)

AGENT_SCHEDULED_TIME

This metric is available only in Amazon Web Services Regions where [Forecasting, capacity planning, and scheduling](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#optimization_region) is available.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Scheduled time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#scheduled-time)

AVG_ABANDON_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average queue abandon time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time)

AVG_ACTIVE_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Average active time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-active-time)

AVG_AFTER_CONTACT_WORK_TIME

Unit: Seconds

Valid metric filter key: `INITIATION_METHOD`

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average after contact work time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time)

### Note

Feature is a valid filter but not a valid grouping.

AVG_AGENT_CONNECTING_TIME

Unit: Seconds

Valid metric filter key: `INITIATION_METHOD` . For now, this metric only supports the following as `INITIATION_METHOD` : `INBOUND` | `OUTBOUND` | `CALLBACK` | `API`

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Average agent API connecting time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-api-connecting-time)

### Note

The `Negate` key in metric-level filters is not applicable for this metric.

AVG_AGENT_PAUSE_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Average agent pause time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-pause-time)

AVG_BOT_CONVERSATION_TIME

Unit: Seconds

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID

UI name: [Average bot conversation time](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#average-bot-conversation-time)

AVG_BOT_CONVERSATION_TURNS

Unit: Count

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID

UI name: [Average bot conversation turns](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#average-bot-conversation-turns)

AVG_CASE_RELATED_CONTACTS

Unit: Count

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Average contacts per case](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-contacts-per-case)

AVG_CASE_RESOLUTION_TIME

Unit: Seconds

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Average case resolution time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-case-resolution-time)

AVG_CONTACT_DURATION

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average contact duration](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-contact-duration)

### Note

Feature is a valid filter but not a valid grouping.

AVG_CONVERSATION_DURATION

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average conversation duration](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-conversation-duration)

AVG_DIALS_PER_MINUTE

This metric is available only for outbound campaigns that use the agent assisted voice and automated voice delivery modes.

Unit: Count

Valid groupings and filters: Agent, Campaign, Queue, Routing Profile

UI name: [Average dials per minute](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-dials-per-minute)

AVG_EVALUATION_SCORE

Unit: Percent

Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form ID, Evaluation Section ID, Evaluation Question ID, Evaluation Source, Form Version, Queue, Routing Profile

UI name: [Average evaluation score](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-evaluation-score)

AVG_FLOW_TIME

Unit: Seconds

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp

UI name: [Average flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-flow-time)

AVG_GREETING_TIME_AGENT

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average agent greeting time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-greeting-time)

AVG_HANDLE_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, RoutingStepExpression

UI name: [Average handle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-handle-time)

### Note

Feature is a valid filter but not a valid grouping.

AVG_HOLD_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time)

### Note

Feature is a valid filter but not a valid grouping.

AVG_HOLD_TIME_ALL_CONTACTS

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average customer hold time all contacts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time-all-contacts)

AVG_HOLDS

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average holds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-holds)

### Note

Feature is a valid filter but not a valid grouping.

AVG_INTERACTION_AND_HOLD_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average agent interaction and customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-and-customer-hold-time)

AVG_INTERACTION_TIME

Unit: Seconds

Valid metric filter key: `INITIATION_METHOD`

Valid groupings and filters: Queue, Channel, Routing Profile, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average agent interaction time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-time)

### Note

Feature is a valid filter but not a valid grouping.

AVG_INTERRUPTIONS_AGENT

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average agent interruptions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interruptions)

AVG_INTERRUPTION_TIME_AGENT

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average agent interruption time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interruption-time)

AVG_NON_TALK_TIME

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average non-talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-non-talk-time)

AVG_QUEUE_ANSWER_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average queue answer time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-answer-time)

### Note

Feature is a valid filter but not a valid grouping.

AVG_RESOLUTION_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average resolution time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-resolution-time)

AVG_TALK_TIME

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-talk-time)

AVG_TALK_TIME_AGENT

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average agent talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-talk-time)

AVG_TALK_TIME_CUSTOMER

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Average customer talk time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-talk-time)

AVG_WAIT_TIME_AFTER_CUSTOMER_CONNECTION

This metric is available only for outbound campaigns that use the agent assisted voice and automated voice delivery modes.

Unit: Seconds

Valid groupings and filters: Campaign

UI name: [Average wait time after customer connection](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-wait-time-after-customer-connection)

AVG_WEIGHTED_EVALUATION_SCORE

Unit: Percent

Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form Id, Evaluation Section ID, Evaluation Question ID, Evaluation Source, Form Version, Queue, Routing Profile

UI name: [Average weighted evaluation score](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-weighted-evaluation-score)

BOT_CONVERSATIONS_COMPLETED

Unit: Count

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID

UI name: [Bot conversations completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-conversations-completed)

BOT_INTENTS_COMPLETED

Unit: Count

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Bot intent name, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID

UI name: [Bot intents completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-intents-completed)

CAMPAIGN_CONTACTS_ABANDONED_AFTER_X

This metric is available only for outbound campaigns using the agent assisted voice and automated voice delivery modes.

Unit: Count

Valid groupings and filters: Agent, Campaign

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you must enter `GT` (for *Greater than* ).

UI name: [Campaign contacts abandoned after X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-contacts-abandoned-after-x)

CAMPAIGN_CONTACTS_ABANDONED_AFTER_X_RATE

This metric is available only for outbound campaigns using the agent assisted voice and automated voice delivery modes.

Unit: Percent

Valid groupings and filters: Agent, Campaign

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you must enter `GT` (for *Greater than* ).

UI name: [Campaign contacts abandoned after X rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-contacts-abandoned-after-x-rate)

CAMPAIGN_INTERACTIONS

This metric is available only for outbound campaigns using the email delivery mode.

Unit: Count

Valid metric filter key: CAMPAIGN_INTERACTION_EVENT_TYPE

Valid groupings and filters: Campaign

UI name: [Campaign interactions](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-interactions)

CAMPAIGN_SEND_ATTEMPTS

This metric is available only for outbound campaigns.

Unit: Count

Valid groupings and filters: Campaign, Channel, contact/segmentAttributes/connect:Subtype

UI name: [Campaign send attempts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#campaign-send-attempts)

CASES_CREATED

Unit: Count

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Cases created](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-created)

CONTACTS_CREATED

Unit: Count

Valid metric filter key: `INITIATION_METHOD`

Valid groupings and filters: Queue, Channel, Routing Profile, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts created](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-created)

### Note

Feature is a valid filter but not a valid grouping.

CONTACTS_HANDLED

Unit: Count

Valid metric filter key: `INITIATION_METHOD` , `DISCONNECT_REASON`

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, RoutingStepExpression, Q in Connect

UI name: [API contacts handled](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#api-contacts-handled)

### Note

Feature is a valid filter but not a valid grouping.

CONTACTS_HANDLED_BY_CONNECTED_TO_AGENT

Unit: Count

Valid metric filter key: `INITIATION_METHOD`

Valid groupings and filters: Queue, Channel, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts handled (connected to agent timestamp)](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-by-connected-to-agent-timestamp)

CONTACTS_HOLD_ABANDONS

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts hold disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-disconnect)

CONTACTS_ON_HOLD_AGENT_DISCONNECT

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contacts hold agent disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-agent-disconnect)

CONTACTS_ON_HOLD_CUSTOMER_DISCONNECT

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contacts hold customer disconnect](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-customer-disconnect)

CONTACTS_PUT_ON_HOLD

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contacts put on hold](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-put-on-hold)

CONTACTS_TRANSFERRED_OUT_EXTERNAL

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contacts transferred out external](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-external)

CONTACTS_TRANSFERRED_OUT_INTERNAL

Unit: Percent

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contacts transferred out internal](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-internal)

CONTACTS_QUEUED

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts queued](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued)

CONTACTS_QUEUED_BY_ENQUEUE

Unit: Count

Valid groupings and filters: Queue, Channel, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype

UI name: [Contacts queued (enqueue timestamp)](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued-by-enqueue)

CONTACTS_REMOVED_FROM_QUEUE_IN_X

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Q in Connect

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you can use `LT` (for âLess thanâ) or `LTE` (for âLess than equalâ).

UI name: [Contacts removed from queue in X seconds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-removed-from-queue)

CONTACTS_RESOLVED_IN_X

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you can use `LT` (for âLess thanâ) or `LTE` (for âLess than equalâ).

UI name: [Contacts resolved in X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-resolved)

CONTACTS_TRANSFERRED_OUT

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Feature, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts transferred out](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out)

### Note

Feature is a valid filter but not a valid grouping.

CONTACTS_TRANSFERRED_OUT_BY_AGENT

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts transferred out by agent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-by-agent)

CONTACTS_TRANSFERRED_OUT_FROM_QUEUE

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contacts transferred out queue](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue)

CURRENT_CASES

Unit: Count

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Current cases](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#current-cases)

DELIVERY_ATTEMPTS

This metric is available only for outbound campaigns.

Unit: Count

Valid metric filter key: `ANSWERING_MACHINE_DETECTION_STATUS` , `CAMPAIGN_DELIVERY_EVENT_TYPE` , `DISCONNECT_REASON`

Valid groupings and filters: Agent, Answering Machine Detection Status, Campaign, Campaign Delivery EventType, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Queue, Routing Profile

UI name: [Delivery attempts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#delivery-attempts)

### Note

Campaign Delivery EventType filter and grouping are only available for SMS and Email campaign delivery modes. Agent, Queue, Routing Profile, Answering Machine Detection Status and Disconnect Reason are only available for agent assisted voice and automated voice delivery modes.

DELIVERY_ATTEMPT_DISPOSITION_RATE

This metric is available only for outbound campaigns. Dispositions for the agent assisted voice and automated voice delivery modes are only available with answering machine detection enabled.

Unit: Percent

Valid metric filter key: `ANSWERING_MACHINE_DETECTION_STATUS` , `CAMPAIGN_DELIVERY_EVENT_TYPE` , `DISCONNECT_REASON`

Valid groupings and filters: Agent, Answering Machine Detection Status, Campaign, Channel, contact/segmentAttributes/connect:Subtype, Disconnect Reason, Queue, Routing Profile

UI name: [Delivery attempt disposition rate](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#delivery-attempt-disposition-rate)

### Note

Campaign Delivery Event Type filter and grouping are only available for SMS and Email campaign delivery modes. Agent, Queue, Routing Profile, Answering Machine Detection Status and Disconnect Reason are only available for agent assisted voice and automated voice delivery modes.

EVALUATIONS_PERFORMED

Unit: Count

Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form ID, Evaluation Source, Form Version, Queue, Routing Profile

UI name: [Evaluations performed](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#evaluations-performed)

FLOWS_OUTCOME

Unit: Count

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp

UI name: [Flows outcome](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome)

FLOWS_STARTED

Unit: Count

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows resource ID, Initiation method, Resource published timestamp

UI name: [Flows started](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-started)

HUMAN_ANSWERED_CALLS

This metric is available only for outbound campaigns. Dispositions for the agent assisted voice and automated voice delivery modes are only available with answering machine detection enabled.

Unit: Count

Valid groupings and filters: Agent, Campaign

UI name: [Human answered](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#human-answered)

MAX_FLOW_TIME

Unit: Seconds

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp

UI name: [Maximum flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#maximum-flow-time)

MAX_QUEUED_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Maximum queued time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#maximum-queued-time)

MIN_FLOW_TIME

Unit: Seconds

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp

UI name: [Minimum flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#minimum-flow-time)

PERCENT_AUTOMATIC_FAILS

Unit: Percent

Valid groupings and filters: Agent, Agent Hierarchy, Channel, Evaluation Form ID, Evaluation Source, Form Version, Queue, Routing Profile

UI name: [Automatic fails percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#automatic-fails-percent)

PERCENT_BOT_CONVERSATIONS_OUTCOME

Unit: Percent

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID

UI name: [Percent bot conversations outcome](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#percent-bot-conversations-outcome)

PERCENT_BOT_INTENTS_OUTCOME

Unit: Percent

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Bot ID, Bot alias, Bot version, Bot locale, Bot intent name, Flows resource ID, Flows module resource ID, Flow type, Flow action ID, Invoking resource published timestamp, Initiation method, Invoking resource type, Parent flows resource ID

UI name: [Percent bot intents outcome](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#percent-bot-intents-outcome)

PERCENT_CASES_FIRST_CONTACT_RESOLVED

Unit: Percent

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Cases resolved on first contact](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-resolved-on-first-contact)

PERCENT_CONTACTS_STEP_EXPIRED

Unit: Percent

Valid groupings and filters: Queue, RoutingStepExpression

UI name: This metric is available in Real-time Metrics UI but not on the Historical Metrics UI.

PERCENT_CONTACTS_STEP_JOINED

Unit: Percent

Valid groupings and filters: Queue, RoutingStepExpression

UI name: This metric is available in Real-time Metrics UI but not on the Historical Metrics UI.

PERCENT_FLOWS_OUTCOME

Unit: Percent

Valid metric filter key: `FLOWS_OUTCOME_TYPE`

Valid groupings and filters: Channel, contact/segmentAttributes/connect:Subtype, Flow type, Flows module resource ID, Flows next resource ID, Flows next resource queue ID, Flows outcome type, Flows resource ID, Initiation method, Resource published timestamp

UI name: [Flows outcome percentage](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome-percentage) .

### Note

The `FLOWS_OUTCOME_TYPE` is not a valid grouping.

PERCENT_NON_TALK_TIME

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Percentage

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Non-talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-talk-time-percent)

PERCENT_TALK_TIME

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Percentage

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#talk-time-percent)

PERCENT_TALK_TIME_AGENT

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Percentage

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Agent talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-talk-time-percent)

PERCENT_TALK_TIME_CUSTOMER

This metric is available only for contacts analyzed by Contact Lens conversational analytics.

Unit: Percentage

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Customer talk time percent](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#customer-talk-time-percent)

REOPENED_CASE_ACTIONS

Unit: Count

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Cases reopened](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-reopened)

RESOLVED_CASE_ACTIONS

Unit: Count

Required filter key: CASE_TEMPLATE_ARN

Valid groupings and filters: CASE_TEMPLATE_ARN, CASE_STATUS

UI name: [Cases resolved](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#cases-resolved)

SERVICE_LEVEL

You can include up to 20 SERVICE_LEVEL metrics in a request.

Unit: Percent

Valid groupings and filters: Queue, Channel, Routing Profile, Q in Connect

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you can use `LT` (for âLess thanâ) or `LTE` (for âLess than equalâ).

UI name: [Service level X](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#service-level)

STEP_CONTACTS_QUEUED

Unit: Count

Valid groupings and filters: Queue, RoutingStepExpression

UI name: This metric is available in Real-time Metrics UI but not on the Historical Metrics UI.

SUM_AFTER_CONTACT_WORK_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [After contact work time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time)

SUM_CONNECTING_TIME_AGENT

Unit: Seconds

Valid metric filter key: `INITIATION_METHOD` . This metric only supports the following filter keys as `INITIATION_METHOD` : `INBOUND` | `OUTBOUND` | `CALLBACK` | `API`

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Agent API connecting time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-api-connecting-time)

### Note

The `Negate` key in metric-level filters is not applicable for this metric.

CONTACTS_ABANDONED

Unit: Count

Metric filter:

- Valid values: `API` | `Incoming` | `Outbound` | `Transfer` | `Callback` | `Queue_Transfer` | `Disconnect`

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, RoutingStepExpression, Q in Connect

UI name: [Contact abandoned](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned)

SUM_CONTACTS_ABANDONED_IN_X

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you can use `LT` (for âLess thanâ) or `LTE` (for âLess than equalâ).

UI name: [Contacts abandoned in X seconds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned-in-x-seconds)

SUM_CONTACTS_ANSWERED_IN_X

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect

Threshold: For `ThresholdValue` , enter any whole number from 1 to 604800 (inclusive), in seconds. For `Comparison` , you can use `LT` (for âLess thanâ) or `LTE` (for âLess than equalâ).

UI name: [Contacts answered in X seconds](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-answered-in-x-seconds)

SUM_CONTACT_FLOW_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contact flow time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contact-flow-time)

SUM_CONTACT_TIME_AGENT

Unit: Seconds

Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy

UI name: [Agent on contact time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-on-contact-time)

SUM_CONTACTS_DISCONNECTED

Valid metric filter key: `DISCONNECT_REASON`

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Contact disconnected](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contact-disconnected)

SUM_ERROR_STATUS_TIME_AGENT

Unit: Seconds

Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy

UI name: [Error status time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#error-status-time)

SUM_HANDLE_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Contact handle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contact-handle-time)

SUM_HOLD_TIME

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Customer hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#customer-hold-time)

SUM_IDLE_TIME_AGENT

Unit: Seconds

Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy

UI name: [Agent idle time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-idle-time)

SUM_INTERACTION_AND_HOLD_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy, Q in Connect

UI name: [Agent interaction and hold time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-interaction-and-hold-time)

SUM_INTERACTION_TIME

Unit: Seconds

Valid groupings and filters: Queue, Channel, Routing Profile, Agent, Agent Hierarchy

UI name: [Agent interaction time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-interaction-time)

SUM_NON_PRODUCTIVE_TIME_AGENT

Unit: Seconds

Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy

UI name: [Agent non-productive time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-productive-time)

SUM_ONLINE_TIME_AGENT

Unit: Seconds

Valid groupings and filters: Routing Profile, Agent, Agent Hierarchy

UI name: [Online time](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#online-time)

SUM_RETRY_CALLBACK_ATTEMPTS

Unit: Count

Valid groupings and filters: Queue, Channel, Routing Profile, contact/segmentAttributes/connect:Subtype, Q in Connect

UI name: [Callback attempts](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#callback-attempts)

(structure)

Contains information about the metric.

Name -> (string)

The name of the metric.

### Warning

This parameter is required. The following Required = No is incorrect.

Threshold -> (list)

Contains information about the threshold for service level metrics.

(structure)

Contains information about the threshold for service level metrics.

Comparison -> (string)

The type of comparison. Currently, âless thanâ (LT), âless than equalâ (LTE), and âgreater thanâ (GT) comparisons are supported.

ThresholdValue -> (double)

The threshold value to compare.

MetricFilters -> (list)

Contains the filters to be used when returning data.

(structure)

Contains information about the filter used when retrieving metrics. `MetricFiltersV2` can be used on the following metrics: `AVG_AGENT_CONNECTING_TIME` , `CONTACTS_CREATED` , `CONTACTS_HANDLED` , `SUM_CONTACTS_DISCONNECTED` .

MetricFilterKey -> (string)

The key to use for filtering data.

Valid metric filter keys:

- ANSWERING_MACHINE_DETECTION_STATUS
- CASE_STATUS
- DISCONNECT_REASON
- FLOWS_ACTION_IDENTIFIER
- FLOWS_NEXT_ACTION_IDENTIFIER
- FLOWS_OUTCOME_TYPE
- FLOWS_RESOURCE_TYPE
- INITIATION_METHOD

MetricFilterValues -> (list)

The values to use for filtering data. Values for metric-level filters can be either a fixed set of values or a customized list, depending on the use case.

For valid values of metric-level filters `INITIATION_METHOD` , `DISCONNECT_REASON` , and `ANSWERING_MACHINE_DETECTION_STATUS` , see [ContactTraceRecord](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord) in the *Amazon Connect Administrator Guide* .

For valid values of the metric-level filter `FLOWS_OUTCOME_TYPE` , see the description for the [Flow outcome](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome) metric in the *Amazon Connect Administrator Guide* .

For valid values of the metric-level filter `BOT_CONVERSATION_OUTCOME_TYPE` , see the description for the [Bot conversations completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-conversations-completed-metric) in the *Amazon Connect Administrator Guide* .

For valid values of the metric-level filter `BOT_INTENT_OUTCOME_TYPE` , see the description for the [Bot intents completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-intents-completed-metric) metric in the *Amazon Connect Administrator Guide* .

(string)

Negate -> (boolean)

If set to `true` , the API response contains results that filter out the results matched by the metric-level filters condition. By default, `Negate` is set to `false` .

JSON Syntax:

```
[
  {
    "Name": "string",
    "Threshold": [
      {
        "Comparison": "string",
        "ThresholdValue": double
      }
      ...
    ],
    "MetricFilters": [
      {
        "MetricFilterKey": "string",
        "MetricFilterValues": ["string", ...],
        "Negate": true|false
      }
      ...
    ]
  }
  ...
]
```

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

`--max-results` (integer)

The maximum number of results to return per page.

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

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

MetricResults -> (list)

Information about the metrics requested in the API request If no grouping is specified, a summary of metric data is returned.

(structure)

Contains information about the metric results.

Dimensions -> (map)

The dimension for the metrics.

key -> (string)

value -> (string)

MetricInterval -> (structure)

The interval period with the start and end time for the metrics.

Interval -> (string)

The interval period provided in the API request.

StartTime -> (timestamp)

The timestamp, in UNIX Epoch time format. Start time is based on the interval period selected.

EndTime -> (timestamp)

The timestamp, in UNIX Epoch time format. End time is based on the interval period selected. For example, If `IntervalPeriod` is selected `THIRTY_MIN` , `StartTime` and `EndTime` in the API request differs by 1 day, then 48 results are returned in the response. Each result is aggregated by the 30 minutes period, with each `StartTime` and `EndTime` differing by 30 minutes.

Collections -> (list)

The set of metrics.

(structure)

Contains the name, thresholds, and metric filters.

Metric -> (structure)

The metric name, thresholds, and metric filters of the returned metric.

Name -> (string)

The name of the metric.

### Warning

This parameter is required. The following Required = No is incorrect.

Threshold -> (list)

Contains information about the threshold for service level metrics.

(structure)

Contains information about the threshold for service level metrics.

Comparison -> (string)

The type of comparison. Currently, âless thanâ (LT), âless than equalâ (LTE), and âgreater thanâ (GT) comparisons are supported.

ThresholdValue -> (double)

The threshold value to compare.

MetricFilters -> (list)

Contains the filters to be used when returning data.

(structure)

Contains information about the filter used when retrieving metrics. `MetricFiltersV2` can be used on the following metrics: `AVG_AGENT_CONNECTING_TIME` , `CONTACTS_CREATED` , `CONTACTS_HANDLED` , `SUM_CONTACTS_DISCONNECTED` .

MetricFilterKey -> (string)

The key to use for filtering data.

Valid metric filter keys:

- ANSWERING_MACHINE_DETECTION_STATUS
- CASE_STATUS
- DISCONNECT_REASON
- FLOWS_ACTION_IDENTIFIER
- FLOWS_NEXT_ACTION_IDENTIFIER
- FLOWS_OUTCOME_TYPE
- FLOWS_RESOURCE_TYPE
- INITIATION_METHOD

MetricFilterValues -> (list)

The values to use for filtering data. Values for metric-level filters can be either a fixed set of values or a customized list, depending on the use case.

For valid values of metric-level filters `INITIATION_METHOD` , `DISCONNECT_REASON` , and `ANSWERING_MACHINE_DETECTION_STATUS` , see [ContactTraceRecord](https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord) in the *Amazon Connect Administrator Guide* .

For valid values of the metric-level filter `FLOWS_OUTCOME_TYPE` , see the description for the [Flow outcome](https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome) metric in the *Amazon Connect Administrator Guide* .

For valid values of the metric-level filter `BOT_CONVERSATION_OUTCOME_TYPE` , see the description for the [Bot conversations completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-conversations-completed-metric) in the *Amazon Connect Administrator Guide* .

For valid values of the metric-level filter `BOT_INTENT_OUTCOME_TYPE` , see the description for the [Bot intents completed](https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-intents-completed-metric) metric in the *Amazon Connect Administrator Guide* .

(string)

Negate -> (boolean)

If set to `true` , the API response contains results that filter out the results matched by the metric-level filters condition. By default, `Negate` is set to `false` .

Value -> (double)

The corresponding value of the metric returned in the response.