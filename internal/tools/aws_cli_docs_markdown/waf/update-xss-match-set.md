# update-xss-match-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-xss-match-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-xss-match-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/index.html#cli-aws-waf) ]

# update-xss-match-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Inserts or deletes  XssMatchTuple objects (filters) in an  XssMatchSet . For each `XssMatchTuple` object, you specify the following values:

- `Action` : Whether to insert the object into or delete the object from the array. To change an `XssMatchTuple` , you delete the existing object and add a new one.
- `FieldToMatch` : The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.
- `TextTransformation` : Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks. You can only specify a single type of TextTransformation.

You use `XssMatchSet` objects to specify which CloudFront requests that you want to allow, block, or count. For example, if youâre receiving requests that contain cross-site scripting attacks in the request body and you want to block the requests, you can create an `XssMatchSet` with the applicable settings, and then configure AWS WAF to block the requests.

To create and configure an `XssMatchSet` , perform the following steps:

- Submit a  CreateXssMatchSet request.
- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an  UpdateIPSet request.
- Submit an `UpdateXssMatchSet` request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/UpdateXssMatchSet)

## Synopsis

```
update-xss-match-set
--xss-match-set-id <value>
--change-token <value>
--updates <value>
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

`--xss-match-set-id` (string)

The `XssMatchSetId` of the `XssMatchSet` that you want to update. `XssMatchSetId` is returned by  CreateXssMatchSet and by  ListXssMatchSets .

`--change-token` (string)

The value returned by the most recent call to  GetChangeToken .

`--updates` (list)

An array of `XssMatchSetUpdate` objects that you want to insert into or delete from an  XssMatchSet . For more information, see the applicable data types:

- XssMatchSetUpdate : Contains `Action` and `XssMatchTuple`
- XssMatchTuple : Contains `FieldToMatch` and `TextTransformation`
- FieldToMatch : Contains `Data` and `Type`

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the part of a web request that you want to inspect for cross-site scripting attacks and indicates whether you want to add the specification to an  XssMatchSet or delete it from an `XssMatchSet` .

Action -> (string)

Specify `INSERT` to add an  XssMatchSetUpdate to an  XssMatchSet . Use `DELETE` to remove an `XssMatchSetUpdate` from an `XssMatchSet` .

XssMatchTuple -> (structure)

Specifies the part of a web request that you want AWS WAF to inspect for cross-site scripting attacks and, if you want AWS WAF to inspect a header, the name of the header.

FieldToMatch -> (structure)

Specifies where in a web request to look for cross-site scripting attacks.

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

Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on `FieldToMatch` before inspecting it for a match.

You can only specify a single type of TextTransformation.

**CMD_LINE**

When youâre concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:

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

Shorthand Syntax:

```
Action=string,XssMatchTuple={FieldToMatch={Type=string,Data=string},TextTransformation=string} ...
```

JSON Syntax:

```
[
  {
    "Action": "INSERT"|"DELETE",
    "XssMatchTuple": {
      "FieldToMatch": {
        "Type": "URI"|"QUERY_STRING"|"HEADER"|"METHOD"|"BODY"|"SINGLE_QUERY_ARG"|"ALL_QUERY_ARGS",
        "Data": "string"
      },
      "TextTransformation": "NONE"|"COMPRESS_WHITE_SPACE"|"HTML_ENTITY_DECODE"|"LOWERCASE"|"CMD_LINE"|"URL_DECODE"
    }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update an XSSMatchSet**

The following `update-xss-match-set` command  deletes an XssMatchTuple object (filters) in an XssMatchSet:

```
aws waf update-xss-match-set --xss-match-set-id a123fae4-b567-8e90-1234-5ab67ac8ca90 --change-token 12cs345-67cd-890b-1cd2-c3a4567d89f1 --updates Action="DELETE",XssMatchTuple={FieldToMatch={Type="QUERY_STRING"},TextTransformation="URL_DECODE"}
```

For more information, see [Working with Cross-site Scripting Match Conditions](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-xss-conditions.html) in the *AWS WAF* developer guide.

## Output

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `UpdateXssMatchSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .