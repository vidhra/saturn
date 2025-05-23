# describe-stepÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-step.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# describe-step

## Description

Provides more detail about the cluster step.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeStep)

## Synopsis

```
describe-step
--cluster-id <value>
--step-id <value>
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

`--cluster-id` (string)

The identifier of the cluster with steps to describe.

`--step-id` (string)

The identifier of the step to describe.

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

The following command describes a step with the step ID `s-3LZC0QUT43AM` in a cluster with the cluster ID `j-3SD91U2E1L2QX`:

```
aws emr describe-step --cluster-id j-3SD91U2E1L2QX --step-id s-3LZC0QUT43AM
```

Output:

```
{
    "Step": {
        "Status": {
            "Timeline": {
                "EndDateTime": 1433200470.481,
                "CreationDateTime": 1433199926.597,
                "StartDateTime": 1433200404.959
            },
            "State": "COMPLETED",
            "StateChangeReason": {}
        },
        "Config": {
            "Args": [
                "s3://us-west-2.elasticmapreduce/libs/hive/hive-script",
                "--base-path",
                "s3://us-west-2.elasticmapreduce/libs/hive/",
                "--install-hive",
                "--hive-versions",
                "0.13.1"
            ],
            "Jar": "s3://us-west-2.elasticmapreduce/libs/script-runner/script-runner.jar",
            "Properties": {}
        },
        "Id": "s-3LZC0QUT43AM",
        "ActionOnFailure": "TERMINATE_CLUSTER",
        "Name": "Setup hive"
    }
}
```

## Output

Step -> (structure)

The step details for the requested step identifier.

Id -> (string)

The identifier of the cluster step.

Name -> (string)

The name of the cluster step.

Config -> (structure)

The Hadoop job configuration of the cluster step.

Jar -> (string)

The path to the JAR file that runs during the step.

Properties -> (map)

The list of Java properties that are set when the step runs. You can use these properties to pass key-value pairs to your main function.

key -> (string)

value -> (string)

MainClass -> (string)

The name of the main class in the specified Java file. If not specified, the JAR file should specify a main class in its manifest file.

Args -> (list)

The list of command line arguments to pass to the JAR fileâs main function for execution.

(string)

ActionOnFailure -> (string)

The action to take when the cluster step fails. Possible values are `TERMINATE_CLUSTER` , `CANCEL_AND_WAIT` , and `CONTINUE` . `TERMINATE_JOB_FLOW` is provided for backward compatibility. We recommend using `TERMINATE_CLUSTER` instead.

If a clusterâs `StepConcurrencyLevel` is greater than `1` , do not use `AddJobFlowSteps` to submit a step with this parameter set to `CANCEL_AND_WAIT` or `TERMINATE_CLUSTER` . The step is not submitted and the action fails with a message that the `ActionOnFailure` setting is not valid.

If you change a clusterâs `StepConcurrencyLevel` to be greater than 1 while a step is running, the `ActionOnFailure` parameter may not behave as you expect. In this case, for a step that fails with this parameter set to `CANCEL_AND_WAIT` , pending steps and the running step are not canceled; for a step that fails with this parameter set to `TERMINATE_CLUSTER` , the cluster does not terminate.

Status -> (structure)

The current execution status details of the cluster step.

State -> (string)

The execution state of the cluster step.

StateChangeReason -> (structure)

The reason for the step execution status change.

Code -> (string)

The programmable code for the state change reason. Note: Currently, the service provides no code for the state change.

Message -> (string)

The descriptive message for the state change reason.

FailureDetails -> (structure)

The details for the step failure including reason, message, and log file path where the root cause was identified.

Reason -> (string)

The reason for the step failure. In the case where the service cannot successfully determine the root cause of the failure, it returns âUnknown Errorâ as a reason.

Message -> (string)

The descriptive message including the error the Amazon EMR service has identified as the cause of step failure. This is text from an error log that describes the root cause of the failure.

LogFile -> (string)

The path to the log file where the step failure root cause was originally recorded.

Timeline -> (structure)

The timeline of the cluster step status over time.

CreationDateTime -> (timestamp)

The date and time when the cluster step was created.

StartDateTime -> (timestamp)

The date and time when the cluster step execution started.

EndDateTime -> (timestamp)

The date and time when the cluster step execution completed or failed.

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the runtime role for a step on the cluster. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: `arn:partition:service:region:account:resource` .

For example, `arn:aws:IAM::1234567890:role/ReadOnly` is a correctly formatted runtime role ARN.