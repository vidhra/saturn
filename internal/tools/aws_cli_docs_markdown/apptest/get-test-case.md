# get-test-caseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/get-test-case.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/get-test-case.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apptest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/index.html#cli-aws-apptest) ]

# get-test-case

## Description

Gets a test case.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apptest-2022-12-06/GetTestCase)

## Synopsis

```
get-test-case
--test-case-id <value>
[--test-case-version <value>]
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

`--test-case-id` (string)

The request test ID of the test case.

`--test-case-version` (integer)

The test case version of the test case.

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

testCaseId -> (string)

The response test ID of the test case.

testCaseArn -> (string)

The Amazon Resource Name (ARN) of the test case.

name -> (string)

The name of the test case.

description -> (string)

The description of the test case.

latestVersion -> (structure)

The latest version of the test case.

version -> (integer)

The version of the test case latest version.

status -> (string)

The status of the test case latest version.

statusReason -> (string)

The status reason of the test case latest version.

testCaseVersion -> (integer)

The case version of the test case.

status -> (string)

The status of the test case.

statusReason -> (string)

The status reason of the test case.

creationTime -> (timestamp)

The creation time of the test case.

lastUpdateTime -> (timestamp)

The last update time of the test case.

steps -> (list)

The steps of the test case.

(structure)

Defines a step.

name -> (string)

The name of the step.

description -> (string)

The description of the step.

action -> (tagged union structure)

The action of the step.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceAction`, `mainframeAction`, `compareAction`.

resourceAction -> (tagged union structure)

The resource action of the step action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `m2ManagedApplicationAction`, `m2NonManagedApplicationAction`, `cloudFormationAction`.

m2ManagedApplicationAction -> (structure)

The AWS Mainframe Modernization managed application action of the resource action.

resource -> (string)

The resource of the AWS Mainframe Modernization managed application action.

actionType -> (string)

The action type of the AWS Mainframe Modernization managed application action.

properties -> (structure)

The properties of the AWS Mainframe Modernization managed application action.

forceStop -> (boolean)

Force stops the AWS Mainframe Modernization managed action properties.

importDataSetLocation -> (string)

The import data set location of the AWS Mainframe Modernization managed action properties.

m2NonManagedApplicationAction -> (structure)

The AWS Mainframe Modernization non-managed application action of the resource action.

resource -> (string)

The resource of the AWS Mainframe Modernization non-managed application action.

actionType -> (string)

The action type of the AWS Mainframe Modernization non-managed application action.

cloudFormationAction -> (structure)

The CloudFormation action of the resource action.

resource -> (string)

The resource of the CloudFormation action.

actionType -> (string)

The action type of the CloudFormation action.

mainframeAction -> (structure)

The mainframe action of the step action.

resource -> (string)

The resource of the mainframe action.

actionType -> (tagged union structure)

The action type of the mainframe action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `batch`, `tn3270`.

batch -> (structure)

The batch of the mainframe action type.

batchJobName -> (string)

The job name of the batch.

batchJobParameters -> (map)

The batch job parameters of the batch.

key -> (string)

value -> (string)

exportDataSetNames -> (list)

The export data set names of the batch.

(string)

tn3270 -> (structure)

The tn3270 port of the mainframe action type.

script -> (structure)

The script of the TN3270 protocol.

scriptLocation -> (string)

The script location of the scripts.

type -> (string)

The type of the scripts.

exportDataSetNames -> (list)

The data set names of the TN3270 protocol.

(string)

properties -> (structure)

The properties of the mainframe action.

dmsTaskArn -> (string)

The DMS task ARN of the mainframe action properties.

compareAction -> (structure)

The compare action of the step action.

input -> (tagged union structure)

The input of the compare action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`.

file -> (structure)

The file in the input.

sourceLocation -> (string)

The source location of the input file.

targetLocation -> (string)

The target location of the input file.

fileMetadata -> (tagged union structure)

The file metadata of the input file.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dataSets`, `databaseCDC`.

dataSets -> (list)

The data sets of the file metadata.

(structure)

Defines a data set.

type -> (string)

The type of the data set.

name -> (string)

The name of the data set.

ccsid -> (string)

The CCSID of the data set.

format -> (string)

The format of the data set.

length -> (integer)

The length of the data set.

databaseCDC -> (structure)

The database CDC of the file metadata.

sourceMetadata -> (structure)

The source metadata of the database CDC.

type -> (string)

The type of the source database metadata.

captureTool -> (string)

The capture tool of the source database metadata.

targetMetadata -> (structure)

The target metadata of the database CDC.

type -> (string)

The type of the target database metadata.

captureTool -> (string)

The capture tool of the target database metadata.

output -> (tagged union structure)

The output of the compare action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `file`.

file -> (structure)

The file of the output.

fileLocation -> (string)

The file location of the output file.

tags -> (map)

The tags of the test case.

key -> (string)

value -> (string)