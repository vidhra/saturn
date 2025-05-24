# get-sbom-exportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/get-sbom-export.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/get-sbom-export.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# get-sbom-export

## Description

Gets details of a software bill of materials (SBOM) report.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/GetSbomExport)

## Synopsis

```
get-sbom-export
--report-id <value>
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

`--report-id` (string)

The report ID of the SBOM export to get details for.

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

errorCode -> (string)

An error code.

errorMessage -> (string)

An error message.

filterCriteria -> (structure)

Contains details about the resource filter criteria used for the software bill of materials (SBOM) report.

accountId -> (list)

The account IDs used as resource filter criteria.

(structure)

A resource string filter for a software bill of materials report.

comparison -> (string)

The filterâs comparison.

value -> (string)

The filterâs value.

ec2InstanceTags -> (list)

The EC2 instance tags used as resource filter criteria.

(structure)

A resource map filter for a software bill of material report.

comparison -> (string)

The filterâs comparison.

key -> (string)

The filterâs key.

value -> (string)

The filterâs value.

ecrImageTags -> (list)

The ECR image tags used as resource filter criteria.

(structure)

A resource string filter for a software bill of materials report.

comparison -> (string)

The filterâs comparison.

value -> (string)

The filterâs value.

ecrRepositoryName -> (list)

The ECR repository names used as resource filter criteria.

(structure)

A resource string filter for a software bill of materials report.

comparison -> (string)

The filterâs comparison.

value -> (string)

The filterâs value.

lambdaFunctionName -> (list)

The Amazon Web Services Lambda function name used as resource filter criteria.

(structure)

A resource string filter for a software bill of materials report.

comparison -> (string)

The filterâs comparison.

value -> (string)

The filterâs value.

lambdaFunctionTags -> (list)

The Amazon Web Services Lambda function tags used as resource filter criteria.

(structure)

A resource map filter for a software bill of material report.

comparison -> (string)

The filterâs comparison.

key -> (string)

The filterâs key.

value -> (string)

The filterâs value.

resourceId -> (list)

The resource IDs used as resource filter criteria.

(structure)

A resource string filter for a software bill of materials report.

comparison -> (string)

The filterâs comparison.

value -> (string)

The filterâs value.

resourceType -> (list)

The resource types used as resource filter criteria.

(structure)

A resource string filter for a software bill of materials report.

comparison -> (string)

The filterâs comparison.

value -> (string)

The filterâs value.

format -> (string)

The format of the software bill of materials (SBOM) report.

reportId -> (string)

The report ID of the software bill of materials (SBOM) report.

s3Destination -> (structure)

Contains details of the Amazon S3 bucket and KMS key used to export findings

bucketName -> (string)

The name of the Amazon S3 bucket to export findings to.

keyPrefix -> (string)

The prefix that the findings will be written under.

kmsKeyArn -> (string)

The ARN of the KMS key used to encrypt data when exporting findings.

status -> (string)

The status of the software bill of materials (SBOM) report.