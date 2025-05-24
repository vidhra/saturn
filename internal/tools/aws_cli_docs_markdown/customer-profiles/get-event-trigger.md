# get-event-triggerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-event-trigger.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-event-trigger.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# get-event-trigger

## Description

Get a specific Event Trigger from the domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/GetEventTrigger)

## Synopsis

```
get-event-trigger
--domain-name <value>
--event-trigger-name <value>
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

`--domain-name` (string)

The unique name of the domain.

`--event-trigger-name` (string)

The unique name of the event trigger.

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

EventTriggerName -> (string)

The unique name of the event trigger.

ObjectTypeName -> (string)

The unique name of the object type.

Description -> (string)

The description of the event trigger.

EventTriggerConditions -> (list)

A list of conditions that determine when an event should trigger the destination.

(structure)

Specifies the circumstances under which the event should trigger the destination.

EventTriggerDimensions -> (list)

A list of dimensions to be evaluated for the event.

(structure)

A specific event dimension to be assessed.

ObjectAttributes -> (list)

A list of object attributes to be evaluated.

(structure)

The criteria that a specific object attribute must meet to trigger the destination.

Source -> (string)

An attribute contained within a source object.

FieldName -> (string)

A field defined within an object type.

ComparisonOperator -> (string)

The operator used to compare an attribute against a list of values.

Values -> (list)

A list of attribute values used for comparison.

(string)

LogicalOperator -> (string)

The operator used to combine multiple dimensions.

SegmentFilter -> (string)

The destination is triggered only for profiles that meet the criteria of a segment definition.

EventTriggerLimits -> (structure)

Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.

EventExpiration -> (long)

In milliseconds. Specifies that an event will only trigger the destination if it is processed within a certain latency period.

Periods -> (list)

A list of time periods during which the limits apply.

(structure)

Defines a limit and the time period during which it is enforced.

Unit -> (string)

The unit of time.

Value -> (integer)

The amount of time of the specified unit.

MaxInvocationsPerProfile -> (integer)

The maximum allowed number of destination invocations per profile.

Unlimited -> (boolean)

If set to true, there is no limit on the number of destination invocations per profile. The default is false.

CreatedAt -> (timestamp)

The timestamp of when the event trigger was created.

LastUpdatedAt -> (timestamp)

The timestamp of when the event trigger was most recently updated.

Tags -> (map)

An array of key-value pairs to apply to this resource.

key -> (string)

value -> (string)