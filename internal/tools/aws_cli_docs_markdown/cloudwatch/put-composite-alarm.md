# put-composite-alarmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudwatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html#cli-aws-cloudwatch) ]

# put-composite-alarm

## Description

Creates or updates a *composite alarm* . When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.

The alarms specified in a composite alarmâs rule expression can include metric alarms and other composite alarms. The rule expression of a composite alarm can include as many as 100 underlying alarms. Any single alarm can be included in the rule expressions of as many as 150 composite alarms.

Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.

Composite alarms can take the following actions:

- Notify Amazon SNS topics.
- Invoke Lambda functions.
- Create OpsItems in Systems Manager Ops Center.
- Create incidents in Systems Manager Incident Manager.

### Note

It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you canât delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.

To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the `AlarmRule` of one of the alarms to `false` .

Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path.

When this operation creates an alarm, the alarm state is immediately set to `INSUFFICIENT_DATA` . The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in `INSUFFICIENT_DATA` state.

When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.

To use this operation, you must be signed on with the `cloudwatch:PutCompositeAlarm` permission that is scoped to `*` . You canât create a composite alarms if your `cloudwatch:PutCompositeAlarm` permission has a narrower scope.

If you are an IAM user, you must have `iam:CreateServiceLinkedRole` to create a composite alarm that has Systems Manager OpsItem actions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/monitoring-2010-08-01/PutCompositeAlarm)

## Synopsis

```
put-composite-alarm
[--actions-enabled | --no-actions-enabled]
[--alarm-actions <value>]
[--alarm-description <value>]
--alarm-name <value>
--alarm-rule <value>
[--insufficient-data-actions <value>]
[--ok-actions <value>]
[--tags <value>]
[--actions-suppressor <value>]
[--actions-suppressor-wait-period <value>]
[--actions-suppressor-extension-period <value>]
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

`--actions-enabled` | `--no-actions-enabled` (boolean)

Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is `TRUE` .

`--alarm-actions` (list)

The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

Valid Values: ]

**Amazon SNS actions:**

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id1)arn:aws:sns:*region* :*account-id* :*sns-topic-name* ``

**Lambda actions:**

- Invoke the latest version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id3)arn:aws:lambda:*region* :*account-id* :function:*function-name* ``
- Invoke a specific version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id5)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*version-number* ``
- Invoke a function by using an alias Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id7)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*alias-name* ``

**Systems Manager actions:**

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id9)arn:aws:ssm:*region* :*account-id* :opsitem:*severity* ``

**Start a Amazon Q Developer operational investigation**

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id11)arn:aws:aiops:*region* :*account-id* :investigation-group:*investigation-group-id* ``

(string)

Syntax:

```
"string" "string" ...
```

`--alarm-description` (string)

The description for the composite alarm.

`--alarm-name` (string)

The name for the composite alarm. This name must be unique within the Region.

`--alarm-rule` (string)

An expression that specifies which other alarms are to be evaluated to determine this composite alarmâs state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.

You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.

Functions can include the following:

- `ALARM("*alarm-name* or *alarm-ARN* ")` is TRUE if the named alarm is in ALARM state.
- `OK("*alarm-name* or *alarm-ARN* ")` is TRUE if the named alarm is in OK state.
- `INSUFFICIENT_DATA("*alarm-name* or *alarm-ARN* ")` is TRUE if the named alarm is in INSUFFICIENT_DATA state.
- `TRUE` always evaluates to TRUE.
- `FALSE` always evaluates to FALSE.

TRUE and FALSE are useful for testing a complex `AlarmRule` structure, and for testing your alarm actions.

Alarm names specified in `AlarmRule` can be surrounded with double-quotes (â), but do not have to be.

The following are some examples of `AlarmRule` :

- `ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh)` specifies that the composite alarm goes into ALARM state only if both CPUUtilizationTooHigh and DiskReadOpsTooHigh alarms are in ALARM state.
- `ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress)` specifies that the alarm goes to ALARM state if CPUUtilizationTooHigh is in ALARM state and DeploymentInProgress is not in ALARM state. This example reduces alarm noise during a known deployment window.
- `(ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh)` goes into ALARM state if CPUUtilizationTooHigh OR DiskReadOpsTooHigh is in ALARM state, and if NetworkOutTooHigh is in OK state. This provides another example of using a composite alarm to prevent noise. This rule ensures that you are not notified with an alarm action on high CPU or disk usage if a known network problem is also occurring.

The `AlarmRule` can specify as many as 100 âchildrenâ alarms. The `AlarmRule` expression can have as many as 500 elements. Elements are child alarms, TRUE or FALSE statements, and parentheses.

`--insufficient-data-actions` (list)

The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

Valid Values: ]

**Amazon SNS actions:**

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id13)arn:aws:sns:*region* :*account-id* :*sns-topic-name* ``

**Lambda actions:**

- Invoke the latest version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id15)arn:aws:lambda:*region* :*account-id* :function:*function-name* ``
- Invoke a specific version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id17)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*version-number* ``
- Invoke a function by using an alias Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id19)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*alias-name* ``

(string)

Syntax:

```
"string" "string" ...
```

`--ok-actions` (list)

The actions to execute when this alarm transitions to an `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

Valid Values: ]

**Amazon SNS actions:**

[``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id21)arn:aws:sns:*region* :*account-id* :*sns-topic-name* ``

**Lambda actions:**

- Invoke the latest version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id23)arn:aws:lambda:*region* :*account-id* :function:*function-name* ``
- Invoke a specific version of a Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id25)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*version-number* ``
- Invoke a function by using an alias Lambda function: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-composite-alarm.html#id27)arn:aws:lambda:*region* :*account-id* :function:*function-name* :*alias-name* ``

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm. To be able to associate tags with the alarm when you create the alarm, you must have the `cloudwatch:TagResource` permission.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html) .

(structure)

A key-value pair associated with a CloudWatch resource.

Key -> (string)

A string that you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.

Value -> (string)

The value for the specified tag key.

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

`--actions-suppressor` (string)

Actions will be suppressed if the suppressor alarm is in the `ALARM` state. `ActionsSuppressor` can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm.

`--actions-suppressor-wait-period` (integer)

The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the `ALARM` state. After this time, the composite alarm performs its actions.

### Warning

`WaitPeriod` is required only when `ActionsSuppressor` is specified.

`--actions-suppressor-extension-period` (integer)

The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the `ALARM` state. After this time, the composite alarm performs its actions.

### Warning

`ExtensionPeriod` is required only when `ActionsSuppressor` is specified.

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

**To create a composite cloudwatch alarm**

The following `put-composite-alarm` example creates a composite alarm named `ProdAlarm`  in the specified account.

```
aws cloudwatch put-composite-alarm \
    --alarm-name ProdAlarm \
    --alarm-rule "ALARM(CPUUtilizationTooHigh) AND ALARM(MemUsageTooHigh)" \
    --alarm-actions arn:aws:sns:us-east-1:123456789012:demo \
    --actions-enabled
```

This command produces no output.

For more information, see [Create a composite alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm_How_To.html) in the *Amazon CloudWatch User Guide*.

## Output

None