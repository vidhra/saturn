# update-regex-pattern-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-pattern-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-regex-pattern-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf-regional](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html#cli-aws-waf-regional) ]

# update-regex-pattern-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Inserts or deletes `RegexPatternString` objects in a  RegexPatternSet . For each `RegexPatternString` object, you specify the following values:

- Whether to insert or delete the `RegexPatternString` .
- The regular expression pattern that you want to insert or delete. For more information, see  RegexPatternSet .

For example, you can create a `RegexPatternString` such as `B[a@]dB[o0]t` . AWS WAF will match this `RegexPatternString` to:

- BadBot
- BadB0t
- [B@dBot](mailto:B%40dBot)
- [B@dB0t](mailto:B%40dB0t)

To create and configure a `RegexPatternSet` , perform the following steps:

- Create a `RegexPatternSet.` For more information, see  CreateRegexPatternSet .
- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexPatternSet` request.
- Submit an `UpdateRegexPatternSet` request to specify the regular expression pattern that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateRegexPatternSet)

## Synopsis

```
update-regex-pattern-set
--regex-pattern-set-id <value>
--updates <value>
--change-token <value>
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

`--regex-pattern-set-id` (string)

The `RegexPatternSetId` of the  RegexPatternSet that you want to update. `RegexPatternSetId` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

`--updates` (list)

An array of `RegexPatternSetUpdate` objects that you want to insert into or delete from a  RegexPatternSet .

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

In an  UpdateRegexPatternSet request, `RegexPatternSetUpdate` specifies whether to insert or delete a `RegexPatternString` and includes the settings for the `RegexPatternString` .

Action -> (string)

Specifies whether to insert or delete a `RegexPatternString` .

RegexPatternString -> (string)

Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as `B[a@]dB[o0]t` .

Shorthand Syntax:

```
Action=string,RegexPatternString=string ...
```

JSON Syntax:

```
[
  {
    "Action": "INSERT"|"DELETE",
    "RegexPatternString": "string"
  }
  ...
]
```

`--change-token` (string)

The value returned by the most recent call to  GetChangeToken .

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

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `UpdateRegexPatternSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .