# list-testsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-tests.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-tests.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# list-tests

## Description

Gets information about tests in a given test suite.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/ListTests)

`list-tests` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `tests`

## Synopsis

```
list-tests
--arn <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--max-items <value>]
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

`--arn` (string)

The test suiteâs Amazon Resource Name (ARN).

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

tests -> (list)

Information about the tests.

(structure)

Represents a condition that is evaluated.

arn -> (string)

The testâs ARN.

name -> (string)

The testâs name.

type -> (string)

The testâs type.

Must be one of the following values:

- BUILTIN_FUZZ
- APPIUM_JAVA_JUNIT
- APPIUM_JAVA_TESTNG
- APPIUM_PYTHON
- APPIUM_NODE
- APPIUM_RUBY
- APPIUM_WEB_JAVA_JUNIT
- APPIUM_WEB_JAVA_TESTNG
- APPIUM_WEB_PYTHON
- APPIUM_WEB_NODE
- APPIUM_WEB_RUBY
- INSTRUMENTATION
- XCTEST
- XCTEST_UI

created -> (timestamp)

When the test was created.

status -> (string)

The testâs status.

Allowed values include:

- PENDING
- PENDING_CONCURRENCY
- PENDING_DEVICE
- PROCESSING
- SCHEDULING
- PREPARING
- RUNNING
- COMPLETED
- STOPPING

result -> (string)

The testâs result.

Allowed values include:

- PENDING
- PASSED
- WARNED
- FAILED
- SKIPPED
- ERRORED
- STOPPED

started -> (timestamp)

The testâs start time.

stopped -> (timestamp)

The testâs stop time.

counters -> (structure)

The testâs result counters.

total -> (integer)

The total number of entities.

passed -> (integer)

The number of passed entities.

failed -> (integer)

The number of failed entities.

warned -> (integer)

The number of warned entities.

errored -> (integer)

The number of errored entities.

stopped -> (integer)

The number of stopped entities.

skipped -> (integer)

The number of skipped entities.

message -> (string)

A message about the testâs result.

deviceMinutes -> (structure)

Represents the total (metered or unmetered) minutes used by the test.

total -> (double)

When specified, represents the total minutes used by the resource to run tests.

metered -> (double)

When specified, represents only the sum of metered minutes used by the resource to run tests.

unmetered -> (double)

When specified, represents only the sum of unmetered minutes used by the resource to run tests.

nextToken -> (string)

If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.