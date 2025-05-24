# create-regex-pattern-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-pattern-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-regex-pattern-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/index.html#cli-aws-waf) ]

# create-regex-pattern-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Creates a `RegexPatternSet` . You then use  UpdateRegexPatternSet to specify the regular expression (regex) pattern that you want AWS WAF to search for, such as `B[a@]dB[o0]t` . You can then configure AWS WAF to reject those requests.

To create and configure a `RegexPatternSet` , perform the following steps:

- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRegexPatternSet` request.
- Submit a `CreateRegexPatternSet` request.
- Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexPatternSet` request.
- Submit an  UpdateRegexPatternSet request to specify the string that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/CreateRegexPatternSet)

## Synopsis

```
create-regex-pattern-set
--name <value>
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

`--name` (string)

A friendly name or description of the  RegexPatternSet . You canât change `Name` after you create a `RegexPatternSet` .

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

RegexPatternSet -> (structure)

A  RegexPatternSet that contains no objects.

RegexPatternSetId -> (string)

The identifier for the `RegexPatternSet` . You use `RegexPatternSetId` to get information about a `RegexPatternSet` , update a `RegexPatternSet` , remove a `RegexPatternSet` from a `RegexMatchSet` , and delete a `RegexPatternSet` from AWS WAF.

`RegexMatchSetId` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

Name -> (string)

A friendly name or description of the  RegexPatternSet . You canât change `Name` after you create a `RegexPatternSet` .

RegexPatternStrings -> (list)

Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as `B[a@]dB[o0]t` .

(string)

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `CreateRegexPatternSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .