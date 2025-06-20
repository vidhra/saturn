# update-quick-responseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/update-quick-response.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/update-quick-response.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# update-quick-response

## Description

Updates an existing Amazon Q in Connect quick response.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/UpdateQuickResponse)

## Synopsis

```
update-quick-response
--knowledge-base-id <value>
--quick-response-id <value>
[--name <value>]
[--content <value>]
[--content-type <value>]
[--grouping-configuration <value>]
[--remove-grouping-configuration | --no-remove-grouping-configuration]
[--description <value>]
[--remove-description | --no-remove-description]
[--shortcut-key <value>]
[--remove-shortcut-key | --no-remove-shortcut-key]
[--is-active | --no-is-active]
[--channels <value>]
[--language <value>]
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

`--knowledge-base-id` (string)

The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.

`--quick-response-id` (string)

The identifier of the quick response.

`--name` (string)

The name of the quick response.

`--content` (tagged union structure)

The updated content of the quick response.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the quick response.

Shorthand Syntax:

```
content=string
```

JSON Syntax:

```
{
  "content": "string"
}
```

`--content-type` (string)

The media type of the quick response content.

- Use `application/x.quickresponse;format=plain` for quick response written in plain text.
- Use `application/x.quickresponse;format=markdown` for quick response written in richtext.

`--grouping-configuration` (structure)

The updated grouping configuration of the quick response.

criteria -> (string)

The criteria used for grouping Amazon Q in Connect users.

The following is the list of supported criteria values.

- `RoutingProfileArn` : Grouping the users by their [Amazon Connect routing profile ARN](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) . User should have [SearchRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) permissions when setting criteria to this value.

values -> (list)

The list of values that define different groups of Amazon Q in Connect users.

- When setting `criteria` to `RoutingProfileArn` , you need to provide a list of ARNs of [Amazon Connect routing profiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) as values of this parameter.

(string)

Shorthand Syntax:

```
criteria=string,values=string,string
```

JSON Syntax:

```
{
  "criteria": "string",
  "values": ["string", ...]
}
```

`--remove-grouping-configuration` | `--no-remove-grouping-configuration` (boolean)

Whether to remove the grouping configuration of the quick response.

`--description` (string)

The updated description of the quick response.

`--remove-description` | `--no-remove-description` (boolean)

Whether to remove the description from the quick response.

`--shortcut-key` (string)

The shortcut key of the quick response. The value should be unique across the knowledge base.

`--remove-shortcut-key` | `--no-remove-shortcut-key` (boolean)

Whether to remove the shortcut key of the quick response.

`--is-active` | `--no-is-active` (boolean)

Whether the quick response is active.

`--channels` (list)

The Amazon Connect contact channels this quick response applies to. The supported contact channel types include `Chat` .

(string)

Syntax:

```
"string" "string" ...
```

`--language` (string)

The language code value for the language in which the quick response is written. The supported language codes include `de_DE` , `en_US` , `es_ES` , `fr_FR` , `id_ID` , `it_IT` , `ja_JP` , `ko_KR` , `pt_BR` , `zh_CN` , `zh_TW`

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

quickResponse -> (structure)

The quick response.

quickResponseArn -> (string)

The Amazon Resource Name (ARN) of the quick response.

quickResponseId -> (string)

The identifier of the quick response.

knowledgeBaseArn -> (string)

The Amazon Resource Name (ARN) of the knowledge base.

knowledgeBaseId -> (string)

The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.

name -> (string)

The name of the quick response.

contentType -> (string)

The media type of the quick response content.

- Use `application/x.quickresponse;format=plain` for quick response written in plain text.
- Use `application/x.quickresponse;format=markdown` for quick response written in richtext.

status -> (string)

The status of the quick response data.

createdTime -> (timestamp)

The timestamp when the quick response was created.

lastModifiedTime -> (timestamp)

The timestamp when the quick response data was last modified.

contents -> (structure)

The contents of the quick response.

plainText -> (tagged union structure)

The container quick response content.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the quick response.

markdown -> (tagged union structure)

The container quick response content.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the quick response.

description -> (string)

The description of the quick response.

groupingConfiguration -> (structure)

The configuration information of the user groups that the quick response is accessible to.

criteria -> (string)

The criteria used for grouping Amazon Q in Connect users.

The following is the list of supported criteria values.

- `RoutingProfileArn` : Grouping the users by their [Amazon Connect routing profile ARN](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) . User should have [SearchRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) permissions when setting criteria to this value.

values -> (list)

The list of values that define different groups of Amazon Q in Connect users.

- When setting `criteria` to `RoutingProfileArn` , you need to provide a list of ARNs of [Amazon Connect routing profiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) as values of this parameter.

(string)

shortcutKey -> (string)

The shortcut key of the quick response. The value should be unique across the knowledge base.

lastModifiedBy -> (string)

The Amazon Resource Name (ARN) of the user who last updated the quick response data.

isActive -> (boolean)

Whether the quick response is active.

channels -> (list)

The Amazon Connect contact channels this quick response applies to. The supported contact channel types include `Chat` .

(string)

language -> (string)

The language code value for the language in which the quick response is written. The supported language codes include `de_DE` , `en_US` , `es_ES` , `fr_FR` , `id_ID` , `it_IT` , `ja_JP` , `ko_KR` , `pt_BR` , `zh_CN` , `zh_TW`

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)