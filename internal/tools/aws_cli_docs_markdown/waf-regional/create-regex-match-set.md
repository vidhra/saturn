# create-regex-match-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-regex-match-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-regex-match-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf-regional](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html#cli-aws-waf-regional) ]

# create-regex-match-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Creates a  RegexMatchSet . You then use  UpdateRegexMatchSet to identify the part of a web request that you want AWS WAF to inspect, such as the values of the `User-Agent` header or the query string. For example, you can create a `RegexMatchSet` that contains a `RegexMatchTuple` that looks for any requests with `User-Agent` headers that match a `RegexPatternSet` with pattern `B[a@]dB[o0]t` . You can then configure AWS WAF to reject those requests.

To create and configure a `RegexMatchSet` , perform the following steps:

- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRegexMatchSet` request.
- Submit a `CreateRegexMatchSet` request.
- Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an `UpdateRegexMatchSet` request.
- Submit an  UpdateRegexMatchSet request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value, using a `RegexPatternSet` , that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateRegexMatchSet)

## Synopsis

```
create-regex-match-set
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

A friendly name or description of the  RegexMatchSet . You canât change `Name` after you create a `RegexMatchSet` .

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

RegexMatchSet -> (structure)

A  RegexMatchSet that contains no `RegexMatchTuple` objects.

RegexMatchSetId -> (string)

The `RegexMatchSetId` for a `RegexMatchSet` . You use `RegexMatchSetId` to get information about a `RegexMatchSet` (see  GetRegexMatchSet ), update a `RegexMatchSet` (see  UpdateRegexMatchSet ), insert a `RegexMatchSet` into a `Rule` or delete one from a `Rule` (see  UpdateRule ), and delete a `RegexMatchSet` from AWS WAF (see  DeleteRegexMatchSet ).

`RegexMatchSetId` is returned by  CreateRegexMatchSet and by  ListRegexMatchSets .

Name -> (string)

A friendly name or description of the  RegexMatchSet . You canât change `Name` after you create a `RegexMatchSet` .

RegexMatchTuples -> (list)

Contains an array of  RegexMatchTuple objects. Each `RegexMatchTuple` object contains:

- The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header.
- The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
- Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The regular expression pattern that you want AWS WAF to search for in web requests, the location in requests that you want AWS WAF to search, and other settings. Each `RegexMatchTuple` object contains:

- The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the `User-Agent` header.
- The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see  RegexPatternSet .
- Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.

FieldToMatch -> (structure)

Specifies where in a web request to look for the `RegexPatternSet` .

Type -> (string)

The part of the web request that you want AWS WAF to search for a specified string. Parts of a request that you can search include the following:

- `HEADER` : A specified request header, for example, the value of the `User-Agent` or `Referer` header. If you choose `HEADER` for the type, specify the name of the header in `Data` .
- `METHOD` : The HTTP method, which indicated the type of operation that the request is asking the origin to perform. Amazon CloudFront supports the following methods: `DELETE` , `GET` , `HEAD` , `OPTIONS` , `PATCH` , `POST` , and `PUT` .
- `QUERY_STRING` : A query string, which is the part of a URL that appears after a `?` character, if any.
- `URI` : The part of a web request that identifies a resource, for example, `/images/daily-ad.jpg` .
- `BODY` : The part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. The request body immediately follows the request headers. Note that only the first `8192` bytes of the request body are forwarded to AWS WAF for inspection. To allow or block requests based on the length of the body, you can create a size constraint set. For more information, see  CreateSizeConstraintSet .
- `SINGLE_QUERY_ARG` : The parameter in the query string that you will inspect, such as *UserName* or *SalesRegion* . The maximum length for `SINGLE_QUERY_ARG` is 30 characters.
- `ALL_QUERY_ARGS` : Similar to `SINGLE_QUERY_ARG` , but rather than inspecting a single parameter, AWS WAF will inspect all parameters within the query for the value or regex pattern that you specify in `TargetString` .

Data -> (string)

When the value of `Type` is `HEADER` , enter the name of the header that you want AWS WAF to search, for example, `User-Agent` or `Referer` . The name of the header is not case sensitive.

When the value of `Type` is `SINGLE_QUERY_ARG` , enter the name of the parameter that you want AWS WAF to search, for example, `UserName` or `SalesRegion` . The parameter name is not case sensitive.

If the value of `Type` is any other value, omit `Data` .

TextTransformation -> (string)

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on `RegexPatternSet` before inspecting a request for a match.

You can only specify a single type of TextTransformation.

**CMD_LINE**

When youâre concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

- Delete the following characters: â â ^
- Delete spaces before the following characters: / (
- Replace the following characters with a space: , ;
- Replace multiple spaces with one space
- Convert uppercase letters (A-Z) to lowercase (a-z)

**COMPRESS_WHITE_SPACE**

Use this option to replace the following characters with a space character (decimal 32):

- f, formfeed, decimal 12
- t, tab, decimal 9
- n, newline, decimal 10
- r, carriage return, decimal 13
- v, vertical tab, decimal 11
- non-breaking space, decimal 160

`COMPRESS_WHITE_SPACE` also replaces multiple spaces with one space.

**HTML_ENTITY_DECODE**

Use this option to replace HTML-encoded characters with unencoded characters. `HTML_ENTITY_DECODE` performs the following operations:

- Replaces `(ampersand)quot;` with `"`
- Replaces `(ampersand)nbsp;` with a non-breaking space, decimal 160
- Replaces `(ampersand)lt;` with a âless thanâ symbol
- Replaces `(ampersand)gt;` with `>`
- Replaces characters that are represented in hexadecimal format, `(ampersand)#xhhhh;` , with the corresponding characters
- Replaces characters that are represented in decimal format, `(ampersand)#nnnn;` , with the corresponding characters

**LOWERCASE**

Use this option to convert uppercase letters (A-Z) to lowercase (a-z).

**URL_DECODE**

Use this option to decode a URL-encoded value.

**NONE**

Specify `NONE` if you donât want to perform any text transformations.

RegexPatternSetId -> (string)

The `RegexPatternSetId` for a `RegexPatternSet` . You use `RegexPatternSetId` to get information about a `RegexPatternSet` (see  GetRegexPatternSet ), update a `RegexPatternSet` (see  UpdateRegexPatternSet ), insert a `RegexPatternSet` into a `RegexMatchSet` or delete one from a `RegexMatchSet` (see  UpdateRegexMatchSet ), and delete an `RegexPatternSet` from AWS WAF (see  DeleteRegexPatternSet ).

`RegexPatternSetId` is returned by  CreateRegexPatternSet and by  ListRegexPatternSets .

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `CreateRegexMatchSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .