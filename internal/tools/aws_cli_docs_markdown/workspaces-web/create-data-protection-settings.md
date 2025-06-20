# create-data-protection-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/create-data-protection-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/create-data-protection-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces-web](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces-web/index.html#cli-aws-workspaces-web) ]

# create-data-protection-settings

## Description

Creates a data protection settings resource that can be associated with a web portal.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-web-2020-07-08/CreateDataProtectionSettings)

## Synopsis

```
create-data-protection-settings
[--additional-encryption-context <value>]
[--client-token <value>]
[--customer-managed-key <value>]
[--description <value>]
[--display-name <value>]
[--inline-redaction-configuration <value>]
[--tags <value>]
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

`--additional-encryption-context` (map)

Additional encryption context of the data protection settings.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request.

If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.

`--customer-managed-key` (string)

The custom managed key of the data protection settings.

`--description` (string)

The description of the data protection settings.

`--display-name` (string)

The display name of the data protection settings.

`--inline-redaction-configuration` (structure)

The inline redaction configuration of the data protection settings that will be applied to all sessions.

globalConfidenceLevel -> (integer)

The global confidence level for the inline redaction configuration. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern + unformatted pattern without keyword. This is applied to patterns that do not have a pattern-level confidence level. Defaults to confidence level 2.

globalEnforcedUrls -> (list)

The global enforced URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level enforced URL list.

(string)

globalExemptUrls -> (list)

The global exempt URL configuration for the inline redaction configuration. This is applied to patterns that do not have a pattern-level exempt URL list.

(string)

inlineRedactionPatterns -> (list)

The inline redaction patterns to be enabled for the inline redaction configuration.

(structure)

The set of patterns that determine the data types redacted in session.

builtInPatternId -> (string)

The built-in pattern from the list of preconfigured patterns. Either a customPattern or builtInPatternId is required.

confidenceLevel -> (integer)

The confidence level for inline redaction pattern. This indicates the certainty of data type matches in the redaction process. Confidence level 3 means high confidence, and requires a formatted text pattern match in order for content to be redacted. Confidence level 2 means medium confidence, and redaction considers both formatted and unformatted text, and adds keyword associate to the logic. Confidence level 1 means low confidence, and redaction is enforced for both formatted pattern + unformatted pattern without keyword. This overrides the global confidence level.

customPattern -> (structure)

>The configuration for a custom pattern. Either a customPattern or builtInPatternId is required.

keywordRegex -> (string)

The keyword regex for the customer pattern. After there is a match to the pattern regex, the keyword regex is used to search within the proximity of the match. If there is a keyword match, then the match is confirmed. If no keyword regex is provided, the pattern regex match will automatically be confirmed. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example, â/ab+c/giâ

patternDescription -> (string)

The pattern description for the customer pattern.

patternName -> (string)

The pattern name for the custom pattern.

patternRegex -> (string)

The pattern regex for the customer pattern. The format must follow JavaScript regex format. The pattern must be enclosed between slashes, and can have flags behind the second slash. For example: â/ab+c/giâ.

enforcedUrls -> (list)

The enforced URL configuration for the inline redaction pattern. This will override the global enforced URL configuration.

(string)

exemptUrls -> (list)

The exempt URL configuration for the inline redaction pattern. This will override the global exempt URL configuration for the inline redaction pattern.

(string)

redactionPlaceHolder -> (structure)

The redaction placeholder that will replace the redacted text in session for the inline redaction pattern.

redactionPlaceHolderText -> (string)

The redaction placeholder text that will replace the redacted text in session for the custom text redaction placeholder type.

redactionPlaceHolderType -> (string)

The redaction placeholder type that will replace the redacted text in session.

JSON Syntax:

```
{
  "globalConfidenceLevel": integer,
  "globalEnforcedUrls": ["string", ...],
  "globalExemptUrls": ["string", ...],
  "inlineRedactionPatterns": [
    {
      "builtInPatternId": "string",
      "confidenceLevel": integer,
      "customPattern": {
        "keywordRegex": "string",
        "patternDescription": "string",
        "patternName": "string",
        "patternRegex": "string"
      },
      "enforcedUrls": ["string", ...],
      "exemptUrls": ["string", ...],
      "redactionPlaceHolder": {
        "redactionPlaceHolderText": "string",
        "redactionPlaceHolderType": "CustomText"
      }
    }
    ...
  ]
}
```

`--tags` (list)

The tags to add to the data protection settings resource. A tag is a key-value pair.

(structure)

The tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

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

dataProtectionSettingsArn -> (string)

The ARN of the data protection settings resource.