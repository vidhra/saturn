# update-size-constraint-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-size-constraint-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf-regional](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html#cli-aws-waf-regional) ]

# update-size-constraint-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Inserts or deletes  SizeConstraint objects (filters) in a  SizeConstraintSet . For each `SizeConstraint` object, you specify the following values:

- Whether to insert or delete the object from the array. If you want to change a `SizeConstraintSetUpdate` object, you delete the existing object and add a new one.
- The part of a web request that you want AWS WAF to evaluate, such as the length of a query string or the length of the `User-Agent` header.
- Whether to perform any transformations on the request, such as converting it to lowercase, before checking its length. Note that transformations of the request body are not supported because the AWS resource forwards only the first `8192` bytes of your request to AWS WAF. You can only specify a single type of TextTransformation.
- A `ComparisonOperator` used for evaluating the selected part of the request against the specified `Size` , such as equals, greater than, less than, and so on.
- The length, in bytes, that you want AWS WAF to watch for in selected part of the request. The length is computed after applying the transformation.

For example, you can add a `SizeConstraintSetUpdate` object that matches web requests in which the length of the `User-Agent` header is greater than 100 bytes. You can then configure AWS WAF to block those requests.

To create and configure a `SizeConstraintSet` , perform the following steps:

- Create a `SizeConstraintSet.` For more information, see  CreateSizeConstraintSet .
- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an `UpdateSizeConstraintSet` request.
- Submit an `UpdateSizeConstraintSet` request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateSizeConstraintSet)

## Synopsis

```
update-size-constraint-set
--size-constraint-set-id <value>
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

`--size-constraint-set-id` (string)

The `SizeConstraintSetId` of the  SizeConstraintSet that you want to update. `SizeConstraintSetId` is returned by  CreateSizeConstraintSet and by  ListSizeConstraintSets .

`--change-token` (string)

The value returned by the most recent call to  GetChangeToken .

`--updates` (list)

An array of `SizeConstraintSetUpdate` objects that you want to insert into or delete from a  SizeConstraintSet . For more information, see the applicable data types:

- SizeConstraintSetUpdate : Contains `Action` and `SizeConstraint`
- SizeConstraint : Contains `FieldToMatch` , `TextTransformation` , `ComparisonOperator` , and `Size`
- FieldToMatch : Contains `Data` and `Type`

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the part of a web request that you want to inspect the size of and indicates whether you want to add the specification to a  SizeConstraintSet or delete it from a `SizeConstraintSet` .

Action -> (string)

Specify `INSERT` to add a  SizeConstraintSetUpdate to a  SizeConstraintSet . Use `DELETE` to remove a `SizeConstraintSetUpdate` from a `SizeConstraintSet` .

SizeConstraint -> (structure)

Specifies a constraint on the size of a part of the web request. AWS WAF uses the `Size` , `ComparisonOperator` , and `FieldToMatch` to build an expression in the form of â`Size` `ComparisonOperator` size in bytes of `FieldToMatch` â. If that expression is true, the `SizeConstraint` is considered to match.

FieldToMatch -> (structure)

Specifies where in a web request to look for the size constraint.

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

Note that if you choose `BODY` for the value of `Type` , you must choose `NONE` for `TextTransformation` because CloudFront forwards only the first 8192 bytes for inspection.

**NONE**

Specify `NONE` if you donât want to perform any text transformations.

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

ComparisonOperator -> (string)

The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided `Size` and `FieldToMatch` to build an expression in the form of â`Size` `ComparisonOperator` size in bytes of `FieldToMatch` â. If that expression is true, the `SizeConstraint` is considered to match.

**EQ** : Used to test if the `Size` is equal to the size of the `FieldToMatch`

**NE** : Used to test if the `Size` is not equal to the size of the `FieldToMatch`

**LE** : Used to test if the `Size` is less than or equal to the size of the `FieldToMatch`

**LT** : Used to test if the `Size` is strictly less than the size of the `FieldToMatch`

**GE** : Used to test if the `Size` is greater than or equal to the size of the `FieldToMatch`

**GT** : Used to test if the `Size` is strictly greater than the size of the `FieldToMatch`

Size -> (long)

The size in bytes that you want AWS WAF to compare against the size of the specified `FieldToMatch` . AWS WAF uses this in combination with `ComparisonOperator` and `FieldToMatch` to build an expression in the form of â`Size` `ComparisonOperator` size in bytes of `FieldToMatch` â. If that expression is true, the `SizeConstraint` is considered to match.

Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).

If you specify `URI` for the value of `Type` , the / in the URI counts as one character. For example, the URI `/logo.jpg` is nine characters long.

Shorthand Syntax:

```
Action=string,SizeConstraint={FieldToMatch={Type=string,Data=string},TextTransformation=string,ComparisonOperator=string,Size=long} ...
```

JSON Syntax:

```
[
  {
    "Action": "INSERT"|"DELETE",
    "SizeConstraint": {
      "FieldToMatch": {
        "Type": "URI"|"QUERY_STRING"|"HEADER"|"METHOD"|"BODY"|"SINGLE_QUERY_ARG"|"ALL_QUERY_ARGS",
        "Data": "string"
      },
      "TextTransformation": "NONE"|"COMPRESS_WHITE_SPACE"|"HTML_ENTITY_DECODE"|"LOWERCASE"|"CMD_LINE"|"URL_DECODE",
      "ComparisonOperator": "EQ"|"NE"|"LE"|"LT"|"GE"|"GT",
      "Size": long
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

**To update a size constraint set**

The following `update-size-constraint-set` command  deletes a SizeConstraint` object (filters) in a size constraint set. Because the `updates` value contains embedded double quotes, you must surround the entire value with single quotes.

```
aws waf-regional update-size-constraint-set \
    --size-constraint-set-id a123fae4-b567-8e90-1234-5ab67ac8ca90 \
    --change-token 12cs345-67cd-890b-1cd2-c3a4567d89f1 \
    --updates 'Action="DELETE",SizeConstraint={FieldToMatch={Type="QUERY_STRING"},TextTransformation="NONE",ComparisonOperator="GT",Size=0}'
```

For more information, see [Working with Size Constraint Conditions](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-size-conditions.html) in the *AWS WAF Developer Guide*.

## Output

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `UpdateSizeConstraintSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .