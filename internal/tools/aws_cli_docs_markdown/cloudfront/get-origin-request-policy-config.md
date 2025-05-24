# get-origin-request-policy-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-origin-request-policy-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-origin-request-policy-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# get-origin-request-policy-config

## Description

Gets an origin request policy configuration.

To get an origin request policy configuration, you must provide the policyâs identifier. If the origin request policy is attached to a distributionâs cache behavior, you can get the policyâs identifier using `ListDistributions` or `GetDistribution` . If the origin request policy is not attached to a cache behavior, you can get the identifier using `ListOriginRequestPolicies` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/GetOriginRequestPolicyConfig)

## Synopsis

```
get-origin-request-policy-config
--id <value>
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

`--id` (string)

The unique identifier for the origin request policy. If the origin request policy is attached to a distributionâs cache behavior, you can get the policyâs identifier using `ListDistributions` or `GetDistribution` . If the origin request policy is not attached to a cache behavior, you can get the identifier using `ListOriginRequestPolicies` .

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

OriginRequestPolicyConfig -> (structure)

The origin request policy configuration.

Comment -> (string)

A comment to describe the origin request policy. The comment cannot be longer than 128 characters.

Name -> (string)

A unique name to identify the origin request policy.

HeadersConfig -> (structure)

The HTTP headers to include in origin requests. These can include headers from viewer requests and additional headers added by CloudFront.

HeaderBehavior -> (string)

Determines whether any HTTP headers are included in requests that CloudFront sends to the origin. Valid values are:

- `none` â No HTTP headers in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to `none` , any headers that are listed in a `CachePolicy` *are* included in origin requests.
- `whitelist` â Only the HTTP headers that are listed in the `Headers` type are included in requests that CloudFront sends to the origin.
- `allViewer` â All HTTP headers in viewer requests are included in requests that CloudFront sends to the origin.
- `allViewerAndWhitelistCloudFront` â All HTTP headers in viewer requests and the additional CloudFront headers that are listed in the `Headers` type are included in requests that CloudFront sends to the origin. The additional headers are added by CloudFront.
- `allExcept` â All HTTP headers in viewer requests are included in requests that CloudFront sends to the origin, * **except** * for those listed in the `Headers` type, which are not included.

Headers -> (structure)

Contains a list of HTTP header names.

Quantity -> (integer)

The number of header names in the `Items` list.

Items -> (list)

A list of HTTP header names.

(string)

CookiesConfig -> (structure)

The cookies from viewer requests to include in origin requests.

CookieBehavior -> (string)

Determines whether cookies in viewer requests are included in requests that CloudFront sends to the origin. Valid values are:

- `none` â No cookies in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to `none` , any cookies that are listed in a `CachePolicy` *are* included in origin requests.
- `whitelist` â Only the cookies in viewer requests that are listed in the `CookieNames` type are included in requests that CloudFront sends to the origin.
- `all` â All cookies in viewer requests are included in requests that CloudFront sends to the origin.
- `allExcept` â All cookies in viewer requests are included in requests that CloudFront sends to the origin, * **except** * for those listed in the `CookieNames` type, which are not included.

Cookies -> (structure)

Contains a list of cookie names.

Quantity -> (integer)

The number of cookie names in the `Items` list.

Items -> (list)

A list of cookie names.

(string)

QueryStringsConfig -> (structure)

The URL query strings from viewer requests to include in origin requests.

QueryStringBehavior -> (string)

Determines whether any URL query strings in viewer requests are included in requests that CloudFront sends to the origin. Valid values are:

- `none` â No query strings in viewer requests are included in requests that CloudFront sends to the origin. Even when this field is set to `none` , any query strings that are listed in a `CachePolicy` *are* included in origin requests.
- `whitelist` â Only the query strings in viewer requests that are listed in the `QueryStringNames` type are included in requests that CloudFront sends to the origin.
- `all` â All query strings in viewer requests are included in requests that CloudFront sends to the origin.
- `allExcept` â All query strings in viewer requests are included in requests that CloudFront sends to the origin, * **except** * for those listed in the `QueryStringNames` type, which are not included.

QueryStrings -> (structure)

Contains the specific query strings in viewer requests that either * **are** * or * **are not** * included in requests that CloudFront sends to the origin. The behavior depends on whether the `QueryStringBehavior` field in the `OriginRequestPolicyQueryStringsConfig` type is set to `whitelist` (the listed query strings * **are** * included) or `allExcept` (the listed query strings * **are not** * included, but all other query strings are).

Quantity -> (integer)

The number of query string names in the `Items` list.

Items -> (list)

A list of query string names.

(string)

ETag -> (string)

The current version of the origin request policy.