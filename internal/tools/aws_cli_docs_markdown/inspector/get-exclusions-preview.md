# get-exclusions-previewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/get-exclusions-preview.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/get-exclusions-preview.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/index.html#cli-aws-inspector) ]

# get-exclusions-preview

## Description

Retrieves the exclusions preview (a list of ExclusionPreview objects) specified by the preview token. You can obtain the preview token by running the CreateExclusionsPreview API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/GetExclusionsPreview)

## Synopsis

```
get-exclusions-preview
--assessment-template-arn <value>
--preview-token <value>
[--next-token <value>]
[--max-results <value>]
[--locale <value>]
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

`--assessment-template-arn` (string)

The ARN that specifies the assessment template for which the exclusions preview was requested.

`--preview-token` (string)

The unique identifier associated of the exclusions preview.

`--next-token` (string)

You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the GetExclusionsPreviewRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.

`--max-results` (integer)

You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.

`--locale` (string)

The locale into which you want to translate the exclusionâs title, description, and recommendation.

Possible values:

- `EN_US`

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

previewStatus -> (string)

Specifies the status of the request to generate an exclusions preview.

exclusionPreviews -> (list)

Information about the exclusions included in the preview.

(structure)

Contains information about what is excluded from an assessment run given the current state of the assessment template.

title -> (string)

The name of the exclusion preview.

description -> (string)

The description of the exclusion preview.

recommendation -> (string)

The recommendation for the exclusion preview.

scopes -> (list)

The AWS resources for which the exclusion preview pertains.

(structure)

This data type contains key-value pairs that identify various Amazon resources.

key -> (string)

The type of the scope.

value -> (string)

The resource identifier for the specified scope type.

attributes -> (list)

The system-defined attributes for the exclusion preview.

(structure)

This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key -> (string)

The attribute key.

value -> (string)

The value assigned to the attribute key.

nextToken -> (string)

When a response is generated, if there is more data to be listed, this parameters is present in the response and contains the value to use for the nextToken parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.