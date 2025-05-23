# get-suite-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-suite-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/get-suite-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotdeviceadvisor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/index.html#cli-aws-iotdeviceadvisor) ]

# get-suite-run

## Description

Gets information about a Device Advisor test suite run.

Requires permission to access the [GetSuiteRun](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotdeviceadvisor-2020-09-18/GetSuiteRun)

## Synopsis

```
get-suite-run
--suite-definition-id <value>
--suite-run-id <value>
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

`--suite-definition-id` (string)

Suite definition ID for the test suite run.

`--suite-run-id` (string)

Suite run ID for the test suite run.

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

**To get the information about an IoT Device Advisor test suite run status**

The following `get-suite-run` example gets the information about a device advisor test suite run status with the specified suite definition ID and suite run ID.

```
aws iotdeviceadvisor get-suite-run \
    --suite-definition-id qqcsmtyyjabl \
    --suite-run-id nzlfyhaa18oa
```

Output:

```
{
    "suiteDefinitionId": "qqcsmtyyjabl",
    "suiteDefinitionVersion": "v1",
    "suiteRunId": "nzlfyhaa18oa",
    "suiteRunArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suiterun/qqcsmtyyjabl/nzlfyhaa18oa",
    "suiteRunConfiguration": {
        "primaryDevice": {
            "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyIotThing",
            "certificateArn": "arn:aws:iot:us-east-1:123456789012:cert/certFile"
        },
        "parallelRun": false
    },
    "testResult": {
        "groups": [
            {
                "groupId": "uta5d9j1kvwc",
                "groupName": "Test group 1",
                "tests": [
                    {
                        "testCaseRunId": "2ve2twrqyr0s",
                        "testCaseDefinitionId": "awr8pq5vc9yp",
                        "testCaseDefinitionName": "MQTT Connect",
                        "status": "PASS",
                        "startTime": "2022-11-12T00:01:53.693000-05:00",
                        "endTime": "2022-11-12T00:02:15.443000-05:00",
                        "logUrl": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logEventViewer:group=/aws/iot/deviceadvisor/qqcsmtyyjabl;stream=nzlfyhaa18oa_2ve2twrqyr0s",
                        "warnings": "null",
                        "failure": "null"
                    }
                ]
            }
        ]
    },
    "startTime": "2022-11-12T00:01:52.673000-05:00",
    "endTime": "2022-11-12T00:02:16.496000-05:00",
    "status": "PASS",
    "tags": {}
}
```

For more information, see [Get a test suite run](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-describe-suite) in the *AWS IoT Core Developer Guide*.

## Output

suiteDefinitionId -> (string)

Suite definition ID for the test suite run.

suiteDefinitionVersion -> (string)

Suite definition version for the test suite run.

suiteRunId -> (string)

Suite run ID for the test suite run.

suiteRunArn -> (string)

The ARN of the suite run.

suiteRunConfiguration -> (structure)

Suite run configuration for the test suite run.

primaryDevice -> (structure)

Sets the primary device for the test suite run. This requires a thing ARN or a certificate ARN.

thingArn -> (string)

Lists deviceâs thing ARN.

certificateArn -> (string)

Lists deviceâs certificate ARN.

deviceRoleArn -> (string)

Lists deviceâs role ARN.

selectedTestList -> (list)

Sets test case list.

(string)

parallelRun -> (boolean)

TRUE if multiple test suites run in parallel.

testResult -> (structure)

Test results for the test suite run.

groups -> (list)

Show each group of test results.

(structure)

Show Group Result.

groupId -> (string)

Group result ID.

groupName -> (string)

Group Result Name.

tests -> (list)

Tests under Group Result.

(structure)

Provides the test case run.

testCaseRunId -> (string)

Provides the test case run ID.

testCaseDefinitionId -> (string)

Provides the test case run definition ID.

testCaseDefinitionName -> (string)

Provides the test case run definition name.

status -> (string)

Provides the test case run status. Status is one of the following:

- `PASS` : Test passed.
- `FAIL` : Test failed.
- `PENDING` : Test has not started running but is scheduled.
- `RUNNING` : Test is running.
- `STOPPING` : Test is performing cleanup steps. You will see this status only if you stop a suite run.
- `STOPPED` Test is stopped. You will see this status only if you stop a suite run.
- `PASS_WITH_WARNINGS` : Test passed with warnings.
- `ERORR` : Test faced an error when running due to an internal issue.

startTime -> (timestamp)

Provides test case run start time.

endTime -> (timestamp)

Provides test case run end time.

logUrl -> (string)

Provides test case run log URL.

warnings -> (string)

Provides test case run warnings.

failure -> (string)

Provides test case run failure result.

testScenarios -> (list)

Provides the test scenarios for the test case run.

(structure)

Provides test case scenario.

testCaseScenarioId -> (string)

Provides test case scenario ID.

testCaseScenarioType -> (string)

Provides test case scenario type. Type is one of the following:

- Advanced
- Basic

status -> (string)

Provides the test case scenario status. Status is one of the following:

- `PASS` : Test passed.
- `FAIL` : Test failed.
- `PENDING` : Test has not started running but is scheduled.
- `RUNNING` : Test is running.
- `STOPPING` : Test is performing cleanup steps. You will see this status only if you stop a suite run.
- `STOPPED` Test is stopped. You will see this status only if you stop a suite run.
- `PASS_WITH_WARNINGS` : Test passed with warnings.
- `ERORR` : Test faced an error when running due to an internal issue.

failure -> (string)

Provides test case scenario failure result.

systemMessage -> (string)

Provides test case scenario system messages if any.

startTime -> (timestamp)

Date (in Unix epoch time) when the test suite run started.

endTime -> (timestamp)

Date (in Unix epoch time) when the test suite run ended.

status -> (string)

Status for the test suite run.

errorReason -> (string)

Error reason for any test suite run failure.

tags -> (map)

The tags attached to the suite run.

key -> (string)

value -> (string)