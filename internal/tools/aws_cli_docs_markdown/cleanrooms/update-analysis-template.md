# update-analysis-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/update-analysis-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/update-analysis-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# update-analysis-template

## Description

Updates the analysis template metadata.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/UpdateAnalysisTemplate)

## Synopsis

```
update-analysis-template
--membership-identifier <value>
--analysis-template-identifier <value>
[--description <value>]
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

`--membership-identifier` (string)

The identifier for a membership resource.

`--analysis-template-identifier` (string)

The identifier for the analysis template resource.

`--description` (string)

A new description for the analysis template.

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

analysisTemplate -> (structure)

The analysis template.

id -> (string)

The identifier for the analysis template.

arn -> (string)

The Amazon Resource Name (ARN) of the analysis template.

collaborationId -> (string)

The unique ID for the associated collaboration of the analysis template.

collaborationArn -> (string)

The unique ARN for the analysis templateâs associated collaboration.

membershipId -> (string)

The identifier of a member who created the analysis template.

membershipArn -> (string)

The Amazon Resource Name (ARN) of the member who created the analysis template.

description -> (string)

The description of the analysis template.

name -> (string)

The name of the analysis template.

createTime -> (timestamp)

The time that the analysis template was created.

updateTime -> (timestamp)

The time that the analysis template was last updated.

schema -> (structure)

The entire schema object.

referencedTables -> (list)

The tables referenced in the analysis schema.

(string)

format -> (string)

The format of the analysis template.

source -> (tagged union structure)

The source of the analysis template.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `artifacts`.

text -> (string)

The query text.

artifacts -> (structure)

The artifacts of the analysis source.

entryPoint -> (structure)

The entry point for the analysis template artifacts.

location -> (structure)

The artifact location.

bucket -> (string)

The bucket name.

key -> (string)

The object key.

additionalArtifacts -> (list)

Additional artifacts for the analysis template.

(structure)

The analysis template artifact.

location -> (structure)

The artifact location.

bucket -> (string)

The bucket name.

key -> (string)

The object key.

roleArn -> (string)

The role ARN for the analysis template artifacts.

sourceMetadata -> (tagged union structure)

The source metadata for the analysis template.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `artifacts`.

artifacts -> (structure)

The artifacts of the analysis source metadata.

entryPointHash -> (structure)

The hash of the entry point for the analysis template artifact metadata.

sha256 -> (string)

The SHA-256 hash value.

additionalArtifactHashes -> (list)

Additional artifact hashes for the analysis template.

(structure)

Hash

sha256 -> (string)

The SHA-256 hash value.

analysisParameters -> (list)

The parameters of the analysis template.

(structure)

Optional. The member who can query can provide this placeholder for a literal data value in an analysis template.

name -> (string)

The name of the parameter. The name must use only alphanumeric, underscore (_), or hyphen (-) characters but cannot start or end with a hyphen.

type -> (string)

The type of parameter.

defaultValue -> (string)

Optional. The default value that is applied in the analysis template. The member who can query can override this value in the query editor.

validations -> (list)

Information about the validations performed on the analysis template.

(structure)

The status details of the analysis template validation. Clean Rooms Differential Privacy uses a general-purpose query structure to support complex SQL queries and validates whether an analysis template fits that general-purpose query structure. Validation is performed when analysis templates are created and fetched. Because analysis templates are immutable by design, we recommend that you create analysis templates after you associate the configured tables with their analysis rule to your collaboration.

For more information, see [https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-custom.html#custom-diff-privacy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/analysis-rules-custom.html#custom-diff-privacy) .

type -> (string)

The type of validation that was performed.

status -> (string)

The status of the validation.

reasons -> (list)

The reasons for the validation results.

(structure)

The reasons for the validation results.

message -> (string)

The validation message.