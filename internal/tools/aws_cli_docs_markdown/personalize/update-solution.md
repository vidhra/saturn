# update-solutionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/update-solution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/update-solution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# update-solution

## Description

Updates an Amazon Personalize solution to use a different automatic training configuration. When you update a solution, you can change whether the solution uses automatic training, and you can change the training frequency. For more information about updating a solution, see [Updating a solution](https://docs.aws.amazon.com/personalize/latest/dg/updating-solution.html) .

A solution update can be in one of the following states:

CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED

To get the status of a solution update, call the [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html) API operation and find the status in the `latestSolutionUpdate` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/UpdateSolution)

## Synopsis

```
update-solution
--solution-arn <value>
[--perform-auto-training | --no-perform-auto-training]
[--solution-update-config <value>]
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

`--solution-arn` (string)

The Amazon Resource Name (ARN) of the solution to update.

`--perform-auto-training` | `--no-perform-auto-training` (boolean)

Whether the solution uses automatic training to create new solution versions (trained models). You can change the training frequency by specifying a `schedulingExpression` in the `AutoTrainingConfig` as part of solution configuration.

If you turn on automatic training, the first automatic training starts within one hour after the solution update completes. If you manually create a solution version within the hour, the solution skips the first automatic training. For more information about automatic training, see [Configuring automatic training](https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html) .

After training starts, you can get the solution versionâs Amazon Resource Name (ARN) with the [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html) API operation. To get its status, use the [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html) .

`--solution-update-config` (structure)

The new configuration details of the solution.

autoTrainingConfig -> (structure)

The automatic training configuration to use when `performAutoTraining` is true.

schedulingExpression -> (string)

Specifies how often to automatically train new solution versions. Specify a rate expression in rate(*value* *unit* ) format. For value, specify a number between 1 and 30. For unit, specify `day` or `days` . For example, to automatically create a new solution version every 5 days, specify `rate(5 days)` . The default is every 7 days.

For more information about auto training, see [Creating and configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html) .

eventsConfig -> (structure)

Describes the configuration of an event, which includes a list of event parameters. You can specify up to 10 event parameters. Events are used in solution creation.

eventParametersList -> (list)

A list of event parameters, which includes event types and their event value thresholds and weights.

(structure)

Describes the parameters of events, which are used in solution creation.

eventType -> (string)

The name of the event type to be considered for solution creation.

eventValueThreshold -> (double)

The threshold of the event type. Only events with a value greater or equal to this threshold will be considered for solution creation.

weight -> (double)

The weight of the event type. A higher weight means higher importance of the event type for the created solution.

JSON Syntax:

```
{
  "autoTrainingConfig": {
    "schedulingExpression": "string"
  },
  "eventsConfig": {
    "eventParametersList": [
      {
        "eventType": "string",
        "eventValueThreshold": double,
        "weight": double
      }
      ...
    ]
  }
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

## Output

solutionArn -> (string)

The same solution Amazon Resource Name (ARN) as given in the request.