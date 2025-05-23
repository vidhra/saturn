# get-data-automation-projectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-data-automation/get-data-automation-project.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-data-automation/get-data-automation-project.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-data-automation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-data-automation/index.html#cli-aws-bedrock-data-automation) ]

# get-data-automation-project

## Description

Gets an existing Amazon Bedrock Data Automation Project

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-data-automation-2023-07-26/GetDataAutomationProject)

## Synopsis

```
get-data-automation-project
--project-arn <value>
[--project-stage <value>]
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

`--project-arn` (string)

ARN generated at the server side when a DataAutomationProject is created

`--project-stage` (string)

Optional field to delete a specific DataAutomationProject stage

Possible values:

- `DEVELOPMENT`
- `LIVE`

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

project -> (structure)

Contains the information of a DataAutomationProject.

projectArn -> (string)

ARN of a DataAutomationProject

creationTime -> (timestamp)

Time Stamp

lastModifiedTime -> (timestamp)

Time Stamp

projectName -> (string)

Name of the DataAutomationProject

projectStage -> (string)

Stage of the Project

projectDescription -> (string)

Description of the DataAutomationProject

standardOutputConfiguration -> (structure)

Standard output configuration

document -> (structure)

Standard Output Configuration of Document

extraction -> (structure)

Standard Extraction Configuration of Document

granularity -> (structure)

Granularity of Document Extraction

types -> (list)

List of Document Extraction Granularity Type

(string)

boundingBox -> (structure)

Bounding Box Configuration of Document Extraction

state -> (string)

State

generativeField -> (structure)

Standard Generative Field Configuration of Document

state -> (string)

State

outputFormat -> (structure)

Output Format of Document

textFormat -> (structure)

Text Format of Document Output

types -> (list)

List of Document Output Text Format Type

(string)

additionalFileFormat -> (structure)

Additional File Format of Document Output

state -> (string)

State

image -> (structure)

Standard Output Configuration of Image

extraction -> (structure)

Standard Extraction Configuration of Image

category -> (structure)

Category of Image Extraction

state -> (string)

State

types -> (list)

List of Image Extraction Category

(string)

boundingBox -> (structure)

Bounding Box Configuration of Image Extraction

state -> (string)

State

generativeField -> (structure)

Standard Generative Field Configuration of Image

state -> (string)

State

types -> (list)

List of Image Standard Generative Field Type

(string)

video -> (structure)

Standard Output Configuration of Video

extraction -> (structure)

Standard Extraction Configuration of Video

category -> (structure)

Category of Video Extraction

state -> (string)

State

types -> (list)

List of Video Extraction Category Type

(string)

boundingBox -> (structure)

Bounding Box Configuration of Video Extraction

state -> (string)

State

generativeField -> (structure)

Standard Generative Field Configuration of Video

state -> (string)

State

types -> (list)

List of Video Standard Generative Field Type

(string)

audio -> (structure)

Standard Output Configuration of Audio

extraction -> (structure)

Standard Extraction Configuration of Audio

category -> (structure)

Category of Audio Extraction

state -> (string)

State

types -> (list)

List of Audio Extraction Category Type

(string)

generativeField -> (structure)

Standard Generative Field Configuration of Audio

state -> (string)

State

types -> (list)

List of Audio Standard Generative Field Type

(string)

customOutputConfiguration -> (structure)

Custom output configuration

blueprints -> (list)

List of Blueprint Item

(structure)

Blueprint Item

blueprintArn -> (string)

ARN of a Blueprint

blueprintVersion -> (string)

Blueprint Version

blueprintStage -> (string)

Stage of the Blueprint

overrideConfiguration -> (structure)

Override configuration

document -> (structure)

Override Configuration of Document

splitter -> (structure)

Configuration of Splitter

state -> (string)

State

modalityProcessing -> (structure)

Configuration to enable/disable processing of modality

state -> (string)

State

image -> (structure)

Override Configuration of Image

modalityProcessing -> (structure)

Configuration to enable/disable processing of modality

state -> (string)

State

video -> (structure)

Override Configuration of Video

modalityProcessing -> (structure)

Configuration to enable/disable processing of modality

state -> (string)

State

audio -> (structure)

Override Configuration of Audio

modalityProcessing -> (structure)

Configuration to enable/disable processing of modality

state -> (string)

State

modalityRouting -> (structure)

Configuration for routing file type to desired modality

jpeg -> (string)

Desired Modality types

png -> (string)

Desired Modality types

mp4 -> (string)

Desired Modality types

mov -> (string)

Desired Modality types

status -> (string)

Status of Data Automation Project

kmsKeyId -> (string)

KMS Key Identifier

kmsEncryptionContext -> (map)

KMS Encryption Context

key -> (string)

Encryption context key.

value -> (string)

Encryption context value.