# update-hub-contentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-hub-content.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-hub-content.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-hub-content

## Description

Updates SageMaker hub content (either a `Model` or `Notebook` resource).

You can update the metadata that describes the resource. In addition to the required request fields, specify at least one of the following fields to update:

- `HubContentDescription`
- `HubContentDisplayName`
- `HubContentMarkdown`
- `HubContentSearchKeywords`
- `SupportStatus`

For more information about hubs, see [Private curated hubs for foundation model access control in JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html) .

### Note

If you want to update a `ModelReference` resource in your hub, use the `UpdateHubContentResource` API instead.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateHubContent)

## Synopsis

```
update-hub-content
--hub-name <value>
--hub-content-name <value>
--hub-content-type <value>
--hub-content-version <value>
[--hub-content-display-name <value>]
[--hub-content-description <value>]
[--hub-content-markdown <value>]
[--hub-content-search-keywords <value>]
[--support-status <value>]
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

`--hub-name` (string)

The name of the SageMaker hub that contains the hub content you want to update. You can optionally use the hub ARN instead.

`--hub-content-name` (string)

The name of the hub content resource that you want to update.

`--hub-content-type` (string)

The content type of the resource that you want to update. Only specify a `Model` or `Notebook` resource for this API. To update a `ModelReference` , use the `UpdateHubContentReference` API instead.

Possible values:

- `Model`
- `Notebook`
- `ModelReference`

`--hub-content-version` (string)

The hub content version that you want to update. For example, if you have two versions of a resource in your hub, you can update the second version.

`--hub-content-display-name` (string)

The display name of the hub content.

`--hub-content-description` (string)

The description of the hub content.

`--hub-content-markdown` (string)

A string that provides a description of the hub content. This string can include links, tables, and standard markdown formatting.

`--hub-content-search-keywords` (list)

The searchable keywords of the hub content.

(string)

Syntax:

```
"string" "string" ...
```

`--support-status` (string)

Indicates the current status of the hub content resource.

Possible values:

- `Supported`
- `Deprecated`
- `Restricted`

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

HubArn -> (string)

The ARN of the private model hub that contains the updated hub content.

HubContentArn -> (string)

The ARN of the hub content resource that was updated.