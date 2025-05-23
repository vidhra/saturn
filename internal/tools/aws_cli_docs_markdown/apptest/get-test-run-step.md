# get-test-run-stepÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/get-test-run-step.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/get-test-run-step.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apptest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/index.html#cli-aws-apptest) ]

# get-test-run-step

## Description

Gets a test run step.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apptest-2022-12-06/GetTestRunStep)

## Synopsis

```
get-test-run-step
--test-run-id <value>
--step-name <value>
[--test-case-id <value>]
[--test-suite-id <value>]
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

`--test-run-id` (string)

The test run ID of the test run step.

`--step-name` (string)

The step name of the test run step.

`--test-case-id` (string)

The test case ID of a test run step.

`--test-suite-id` (string)

The test suite ID of a test run step.

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

stepName -> (string)

The step name of the test run step.

testRunId -> (string)

The test run ID of the test run step.

testCaseId -> (string)

The test case ID of the test run step.

testCaseVersion -> (integer)

The test case version of the test run step.

testSuiteId -> (string)

The test suite ID of the test run step.

testSuiteVersion -> (integer)

The test suite version of the test run step.

beforeStep -> (boolean)

The before steps of the test run step.

afterStep -> (boolean)

The after steps of the test run step.

status -> (string)

The status of the test run step.

statusReason -> (string)

The status reason of the test run step.

runStartTime -> (timestamp)

The run start time of the test run step.

runEndTime -> (timestamp)

The run end time of the test run step.

stepRunSummary -> (tagged union structure)

The step run summary of the test run step.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `mainframeAction`, `compareAction`, `resourceAction`.

mainframeAction -> (tagged union structure)

The mainframe action of the step run summary.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `batch`, `tn3270`.

batch -> (structure)

The batch of the mainframe action summary.

stepInput -> (structure)

The step input of the batch summary.

resource -> (tagged union structure)

The resource of the batch step input.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `m2ManagedApplication`, `m2NonManagedApplication`.

m2ManagedApplication -> (structure)

The AWS Mainframe Modernization managed application in the mainframe resource summary.

applicationId -> (string)

The application ID of the AWS Mainframe Modernization managed application summary.

runtime -> (string)

The runtime of the AWS Mainframe Modernization managed application summary.

listenerPort -> (integer)

The listener port of the AWS Mainframe Modernization managed application summary.

m2NonManagedApplication -> (structure)

The AWS Mainframe Modernization non-managed application in the mainframe resource summary.

vpcEndpointServiceName -> (string)

The VPC endpoint service name of the AWS Mainframe Modernization non-managed application summary.

listenerPort -> (integer)

The listener port of the AWS Mainframe Modernization non-managed application summary.

runtime -> (string)

The runtime of the AWS Mainframe Modernization non-managed application summary.

webAppName -> (string)

The web application name of the AWS Mainframe Modernization non-managed application summary.

batchJobName -> (string)

The batch job name of the batch step input.

batchJobParameters -> (map)

The batch job parameters of the batch step input.

key -> (string)

value -> (string)

exportDataSetNames -> (list)

The export data set names of the batch step input.

(string)

properties -> (structure)

The properties of the batch step input.

dmsTaskArn -> (string)

The DMS task ARN of the mainframe action properties.

stepOutput -> (structure)

The step output of the batch summary.

dataSetExportLocation -> (string)

The data set export location of the batch step output.

dmsOutputLocation -> (string)

The Database Migration Service (DMS) output location of the batch step output.

dataSetDetails -> (list)

The data set details of the batch step output.

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

tn3270 -> (structure)

The tn3270 port of the mainframe action summary.

stepInput -> (structure)

The step input of the TN3270 summary.

resource -> (tagged union structure)

The resource of the TN3270 step input.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `m2ManagedApplication`, `m2NonManagedApplication`.

m2ManagedApplication -> (structure)

The AWS Mainframe Modernization managed application in the mainframe resource summary.

applicationId -> (string)

The application ID of the AWS Mainframe Modernization managed application summary.

runtime -> (string)

The runtime of the AWS Mainframe Modernization managed application summary.

listenerPort -> (integer)

The listener port of the AWS Mainframe Modernization managed application summary.

m2NonManagedApplication -> (structure)

The AWS Mainframe Modernization non-managed application in the mainframe resource summary.

vpcEndpointServiceName -> (string)

The VPC endpoint service name of the AWS Mainframe Modernization non-managed application summary.

listenerPort -> (integer)

The listener port of the AWS Mainframe Modernization non-managed application summary.

runtime -> (string)

The runtime of the AWS Mainframe Modernization non-managed application summary.

webAppName -> (string)

The web application name of the AWS Mainframe Modernization non-managed application summary.

script -> (structure)

The script of the TN3270 step input.

scriptLocation -> (string)

The script location of the script summary.

type -> (string)

The type of the script summary.

exportDataSetNames -> (list)

The export data set names of the TN3270 step input.

(string)

properties -> (structure)

The properties of the TN3270 step input.

dmsTaskArn -> (string)

The DMS task ARN of the mainframe action properties.

stepOutput -> (structure)

The step output of the TN3270 summary.

dataSetExportLocation -> (string)

The data set export location of the TN3270 step output.

dmsOutputLocation -> (string)

The output location of the TN3270 step output.

dataSetDetails -> (list)

The data set details of the TN3270 step output.

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

scriptOutputLocation -> (string)

The script output location of the TN3270 step output.

compareAction -> (structure)

The compare action of the step run summary.

type -> (tagged union structure)

The type of the compare action summary.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fileType`.

fileType -> (tagged union structure)

The file type of the file.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `datasets`, `databaseCDC`.

datasets -> (structure)

The data sets in the compare file type.

stepInput -> (structure)

The step input of the compare data sets summary.

sourceLocation -> (string)

The source location of the compare data sets step input location.

targetLocation -> (string)

The target location of the compare data sets step input location.

sourceDataSets -> (list)

The source data sets of the compare data sets step input location.

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

targetDataSets -> (list)

The target data sets of the compare data sets step input location.

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

stepOutput -> (structure)

The step output of the compare data sets summary.

comparisonOutputLocation -> (string)

The comparison output location of the compare data sets step output.

comparisonStatus -> (string)

The comparison status of the compare data sets step output.

databaseCDC -> (structure)

The database CDC of the compare file type.

stepInput -> (structure)

The step input of the compare database CDC summary.

sourceLocation -> (string)

The source location of the compare database CDC step input.

targetLocation -> (string)

The target location of the compare database CDC step input.

outputLocation -> (string)

The output location of the compare database CDC step input.

sourceMetadata -> (structure)

The source metadata of the compare database CDC step input.

type -> (string)

The type of the source database metadata.

captureTool -> (string)

The capture tool of the source database metadata.

targetMetadata -> (structure)

The target metadata location of the compare database CDC step input.

type -> (string)

The type of the target database metadata.

captureTool -> (string)

The capture tool of the target database metadata.

stepOutput -> (structure)

The step output of the compare database CDC summary.

comparisonOutputLocation -> (string)

The comparison output of the compare database CDC step output.

comparisonStatus -> (string)

The comparison status of the compare database CDC step output.

resourceAction -> (tagged union structure)

The resource action of the step run summary.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cloudFormation`, `m2ManagedApplication`, `m2NonManagedApplication`.

cloudFormation -> (tagged union structure)

The CloudFormation template of the resource action summary.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `createCloudformation`, `deleteCloudformation`.

createCloudformation -> (structure)

Creates the CloudFormation summary of the step.

stepInput -> (structure)

The step input of the CloudFormation summary.

templateLocation -> (string)

The template location of the CloudFormation step input.

parameters -> (map)

The CloudFormation properties of the CloudFormation step input.

key -> (string)

value -> (string)

stepOutput -> (structure)

The step output of the CloudFormation summary.

stackId -> (string)

The stack ID of the CloudFormation step output.

exports -> (map)

The exports of the CloudFormation step output.

key -> (string)

value -> (string)

deleteCloudformation -> (structure)

Deletes the CloudFormation summary of the CloudFormation step summary.

stepInput -> (structure)

The step input of the deleted CloudFormation summary.

stackId -> (string)

The stack ID of the deleted CloudFormation step input.

stepOutput -> (structure)

The step output of the deleted CloudFormation summary.

m2ManagedApplication -> (structure)

The AWS Mainframe Modernization managed application of the resource action summary.

stepInput -> (structure)

The step input of the AWS Mainframe Modernization managed application step summary.

applicationId -> (string)

The application ID of the AWS Mainframe Modernization managed application step input.

runtime -> (string)

The runtime of the AWS Mainframe Modernization managed application step input.

vpcEndpointServiceName -> (string)

The VPC endpoint service name of the AWS Mainframe Modernization managed application step input.

listenerPort -> (integer)

The listener port of the AWS Mainframe Modernization managed application step input.

actionType -> (string)

The action type of the AWS Mainframe Modernization managed application step input.

properties -> (structure)

The properties of the AWS Mainframe Modernization managed application step input.

forceStop -> (boolean)

Force stops the AWS Mainframe Modernization managed action properties.

importDataSetLocation -> (string)

The import data set location of the AWS Mainframe Modernization managed action properties.

stepOutput -> (structure)

The step output of the AWS Mainframe Modernization managed application step summary.

importDataSetSummary -> (map)

The import data set summary of the AWS Mainframe Modernization managed application step output.

key -> (string)

value -> (string)

m2NonManagedApplication -> (structure)

The AWS Mainframe Modernization non-managed application of the resource action summary.

stepInput -> (structure)

The step input of the AWS Mainframe Modernization non-managed application step summary.

vpcEndpointServiceName -> (string)

The VPC endpoint service name of the AWS Mainframe Modernization non-managed application step input.

listenerPort -> (integer)

The listener port of the AWS Mainframe Modernization non-managed application step input.

runtime -> (string)

The runtime of the AWS Mainframe Modernization non-managed application step input.

webAppName -> (string)

The web app name of the AWS Mainframe Modernization non-managed application step input.

actionType -> (string)

The action type of the AWS Mainframe Modernization non-managed application step input.

stepOutput -> (structure)

The step output of the AWS Mainframe Modernization non-managed application step summary.