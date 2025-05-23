# update-cache-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cache-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cache-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# update-cache-policy

## Description

Updates a cache policy configuration.

When you update a cache policy configuration, all the fields are updated with the values provided in the request. You cannot update some fields independent of others. To update a cache policy configuration:

- Use `GetCachePolicyConfig` to get the current configuration.
- Locally modify the fields in the cache policy configuration that you want to update.
- Call `UpdateCachePolicy` by providing the entire cache policy configuration, including the fields that you modified and those that you didnât.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/UpdateCachePolicy)

## Synopsis

```
update-cache-policy
--cache-policy-config <value>
--id <value>
[--if-match <value>]
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

`--cache-policy-config` (structure)

A cache policy configuration.

Comment -> (string)

A comment to describe the cache policy. The comment cannot be longer than 128 characters.

Name -> (string)

A unique name to identify the cache policy.

DefaultTTL -> (long)

The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value as the objectâs time to live (TTL) only when the origin does *not* send `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

The default value for this field is 86400 seconds (one day). If the value of `MinTTL` is more than 86400 seconds, then the default value for this field is the same as the value of `MinTTL` .

MaxTTL -> (long)

The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value only when the origin sends `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

The default value for this field is 31536000 seconds (one year). If the value of `MinTTL` or `DefaultTTL` is more than 31536000 seconds, then the default value for this field is the same as the value of `DefaultTTL` .

MinTTL -> (long)

The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

ParametersInCacheKeyAndForwardedToOrigin -> (structure)

The HTTP headers, cookies, and URL query strings to include in the cache key. The values included in the cache key are also included in requests that CloudFront sends to the origin.

EnableAcceptEncodingGzip -> (boolean)

A flag that can affect whether the `Accept-Encoding` HTTP header is included in the cache key and included in requests that CloudFront sends to the origin.

This field is related to the `EnableAcceptEncodingBrotli` field. If one or both of these fields is `true` *and* the viewer request includes the `Accept-Encoding` header, then CloudFront does the following:

- Normalizes the value of the viewerâs `Accept-Encoding` header
- Includes the normalized header in the cache key
- Includes the normalized header in the request to the origin, if a request is necessary

For more information, see [Compression support](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-policy-compressed-objects) in the *Amazon CloudFront Developer Guide* .

If you set this value to `true` , and this cache behavior also has an origin request policy attached, do not include the `Accept-Encoding` header in the origin request policy. CloudFront always includes the `Accept-Encoding` header in origin requests when the value of this field is `true` , so including this header in an origin request policy has no effect.

If both of these fields are `false` , then CloudFront treats the `Accept-Encoding` header the same as any other HTTP header in the viewer request. By default, itâs not included in the cache key and itâs not included in origin requests. In this case, you can manually add `Accept-Encoding` to the headers whitelist like any other HTTP header.

EnableAcceptEncodingBrotli -> (boolean)

A flag that can affect whether the `Accept-Encoding` HTTP header is included in the cache key and included in requests that CloudFront sends to the origin.

This field is related to the `EnableAcceptEncodingGzip` field. If one or both of these fields is `true` *and* the viewer request includes the `Accept-Encoding` header, then CloudFront does the following:

- Normalizes the value of the viewerâs `Accept-Encoding` header
- Includes the normalized header in the cache key
- Includes the normalized header in the request to the origin, if a request is necessary

For more information, see [Compression support](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-policy-compressed-objects) in the *Amazon CloudFront Developer Guide* .

If you set this value to `true` , and this cache behavior also has an origin request policy attached, do not include the `Accept-Encoding` header in the origin request policy. CloudFront always includes the `Accept-Encoding` header in origin requests when the value of this field is `true` , so including this header in an origin request policy has no effect.

If both of these fields are `false` , then CloudFront treats the `Accept-Encoding` header the same as any other HTTP header in the viewer request. By default, itâs not included in the cache key and itâs not included in origin requests. In this case, you can manually add `Accept-Encoding` to the headers whitelist like any other HTTP header.

HeadersConfig -> (structure)

An object that determines whether any HTTP headers (and if so, which headers) are included in the cache key and in requests that CloudFront sends to the origin.

HeaderBehavior -> (string)

Determines whether any HTTP headers are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:

- `none` â No HTTP headers are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none` , any headers that are listed in an `OriginRequestPolicy` *are* included in origin requests.
- `whitelist` â Only the HTTP headers that are listed in the `Headers` type are included in the cache key and in requests that CloudFront sends to the origin.

Headers -> (structure)

Contains a list of HTTP header names.

Quantity -> (integer)

The number of header names in the `Items` list.

Items -> (list)

A list of HTTP header names.

(string)

CookiesConfig -> (structure)

An object that determines whether any cookies in viewer requests (and if so, which cookies) are included in the cache key and in requests that CloudFront sends to the origin.

CookieBehavior -> (string)

Determines whether any cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:

- `none` â No cookies in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none` , any cookies that are listed in an `OriginRequestPolicy` *are* included in origin requests.
- `whitelist` â Only the cookies in viewer requests that are listed in the `CookieNames` type are included in the cache key and in requests that CloudFront sends to the origin.
- `allExcept` â All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * for those that are listed in the `CookieNames` type, which are not included.
- `all` â All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.

Cookies -> (structure)

Contains a list of cookie names.

Quantity -> (integer)

The number of cookie names in the `Items` list.

Items -> (list)

A list of cookie names.

(string)

QueryStringsConfig -> (structure)

An object that determines whether any URL query strings in viewer requests (and if so, which query strings) are included in the cache key and in requests that CloudFront sends to the origin.

QueryStringBehavior -> (string)

Determines whether any URL query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:

- `none` â No query strings in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none` , any query strings that are listed in an `OriginRequestPolicy` *are* included in origin requests.
- `whitelist` â Only the query strings in viewer requests that are listed in the `QueryStringNames` type are included in the cache key and in requests that CloudFront sends to the origin.
- `allExcept` â All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * those that are listed in the `QueryStringNames` type, which are not included.
- `all` â All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.

QueryStrings -> (structure)

Contains the specific query strings in viewer requests that either * **are** * or * **are not** * included in the cache key and in requests that CloudFront sends to the origin. The behavior depends on whether the `QueryStringBehavior` field in the `CachePolicyQueryStringsConfig` type is set to `whitelist` (the listed query strings * **are** * included) or `allExcept` (the listed query strings * **are not** * included, but all other query strings are).

Quantity -> (integer)

The number of query string names in the `Items` list.

Items -> (list)

A list of query string names.

(string)

JSON Syntax:

```
{
  "Comment": "string",
  "Name": "string",
  "DefaultTTL": long,
  "MaxTTL": long,
  "MinTTL": long,
  "ParametersInCacheKeyAndForwardedToOrigin": {
    "EnableAcceptEncodingGzip": true|false,
    "EnableAcceptEncodingBrotli": true|false,
    "HeadersConfig": {
      "HeaderBehavior": "none"|"whitelist",
      "Headers": {
        "Quantity": integer,
        "Items": ["string", ...]
      }
    },
    "CookiesConfig": {
      "CookieBehavior": "none"|"whitelist"|"allExcept"|"all",
      "Cookies": {
        "Quantity": integer,
        "Items": ["string", ...]
      }
    },
    "QueryStringsConfig": {
      "QueryStringBehavior": "none"|"whitelist"|"allExcept"|"all",
      "QueryStrings": {
        "Quantity": integer,
        "Items": ["string", ...]
      }
    }
  }
}
```

`--id` (string)

The unique identifier for the cache policy that you are updating. The identifier is returned in a cache behaviorâs `CachePolicyId` field in the response to `GetDistributionConfig` .

`--if-match` (string)

The version of the cache policy that you are updating. The version is returned in the cache policyâs `ETag` field in the response to `GetCachePolicyConfig` .

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

CachePolicy -> (structure)

A cache policy.

Id -> (string)

The unique identifier for the cache policy.

LastModifiedTime -> (timestamp)

The date and time when the cache policy was last modified.

CachePolicyConfig -> (structure)

The cache policy configuration.

Comment -> (string)

A comment to describe the cache policy. The comment cannot be longer than 128 characters.

Name -> (string)

A unique name to identify the cache policy.

DefaultTTL -> (long)

The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value as the objectâs time to live (TTL) only when the origin does *not* send `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

The default value for this field is 86400 seconds (one day). If the value of `MinTTL` is more than 86400 seconds, then the default value for this field is the same as the value of `MinTTL` .

MaxTTL -> (long)

The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. CloudFront uses this value only when the origin sends `Cache-Control` or `Expires` headers with the object. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

The default value for this field is 31536000 seconds (one year). If the value of `MinTTL` or `DefaultTTL` is more than 31536000 seconds, then the default value for this field is the same as the value of `DefaultTTL` .

MinTTL -> (long)

The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

ParametersInCacheKeyAndForwardedToOrigin -> (structure)

The HTTP headers, cookies, and URL query strings to include in the cache key. The values included in the cache key are also included in requests that CloudFront sends to the origin.

EnableAcceptEncodingGzip -> (boolean)

A flag that can affect whether the `Accept-Encoding` HTTP header is included in the cache key and included in requests that CloudFront sends to the origin.

This field is related to the `EnableAcceptEncodingBrotli` field. If one or both of these fields is `true` *and* the viewer request includes the `Accept-Encoding` header, then CloudFront does the following:

- Normalizes the value of the viewerâs `Accept-Encoding` header
- Includes the normalized header in the cache key
- Includes the normalized header in the request to the origin, if a request is necessary

For more information, see [Compression support](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-policy-compressed-objects) in the *Amazon CloudFront Developer Guide* .

If you set this value to `true` , and this cache behavior also has an origin request policy attached, do not include the `Accept-Encoding` header in the origin request policy. CloudFront always includes the `Accept-Encoding` header in origin requests when the value of this field is `true` , so including this header in an origin request policy has no effect.

If both of these fields are `false` , then CloudFront treats the `Accept-Encoding` header the same as any other HTTP header in the viewer request. By default, itâs not included in the cache key and itâs not included in origin requests. In this case, you can manually add `Accept-Encoding` to the headers whitelist like any other HTTP header.

EnableAcceptEncodingBrotli -> (boolean)

A flag that can affect whether the `Accept-Encoding` HTTP header is included in the cache key and included in requests that CloudFront sends to the origin.

This field is related to the `EnableAcceptEncodingGzip` field. If one or both of these fields is `true` *and* the viewer request includes the `Accept-Encoding` header, then CloudFront does the following:

- Normalizes the value of the viewerâs `Accept-Encoding` header
- Includes the normalized header in the cache key
- Includes the normalized header in the request to the origin, if a request is necessary

For more information, see [Compression support](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-policy-compressed-objects) in the *Amazon CloudFront Developer Guide* .

If you set this value to `true` , and this cache behavior also has an origin request policy attached, do not include the `Accept-Encoding` header in the origin request policy. CloudFront always includes the `Accept-Encoding` header in origin requests when the value of this field is `true` , so including this header in an origin request policy has no effect.

If both of these fields are `false` , then CloudFront treats the `Accept-Encoding` header the same as any other HTTP header in the viewer request. By default, itâs not included in the cache key and itâs not included in origin requests. In this case, you can manually add `Accept-Encoding` to the headers whitelist like any other HTTP header.

HeadersConfig -> (structure)

An object that determines whether any HTTP headers (and if so, which headers) are included in the cache key and in requests that CloudFront sends to the origin.

HeaderBehavior -> (string)

Determines whether any HTTP headers are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:

- `none` â No HTTP headers are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none` , any headers that are listed in an `OriginRequestPolicy` *are* included in origin requests.
- `whitelist` â Only the HTTP headers that are listed in the `Headers` type are included in the cache key and in requests that CloudFront sends to the origin.

Headers -> (structure)

Contains a list of HTTP header names.

Quantity -> (integer)

The number of header names in the `Items` list.

Items -> (list)

A list of HTTP header names.

(string)

CookiesConfig -> (structure)

An object that determines whether any cookies in viewer requests (and if so, which cookies) are included in the cache key and in requests that CloudFront sends to the origin.

CookieBehavior -> (string)

Determines whether any cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:

- `none` â No cookies in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none` , any cookies that are listed in an `OriginRequestPolicy` *are* included in origin requests.
- `whitelist` â Only the cookies in viewer requests that are listed in the `CookieNames` type are included in the cache key and in requests that CloudFront sends to the origin.
- `allExcept` â All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * for those that are listed in the `CookieNames` type, which are not included.
- `all` â All cookies in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.

Cookies -> (structure)

Contains a list of cookie names.

Quantity -> (integer)

The number of cookie names in the `Items` list.

Items -> (list)

A list of cookie names.

(string)

QueryStringsConfig -> (structure)

An object that determines whether any URL query strings in viewer requests (and if so, which query strings) are included in the cache key and in requests that CloudFront sends to the origin.

QueryStringBehavior -> (string)

Determines whether any URL query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin. Valid values are:

- `none` â No query strings in viewer requests are included in the cache key or in requests that CloudFront sends to the origin. Even when this field is set to `none` , any query strings that are listed in an `OriginRequestPolicy` *are* included in origin requests.
- `whitelist` â Only the query strings in viewer requests that are listed in the `QueryStringNames` type are included in the cache key and in requests that CloudFront sends to the origin.
- `allExcept` â All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin, * **except** * those that are listed in the `QueryStringNames` type, which are not included.
- `all` â All query strings in viewer requests are included in the cache key and in requests that CloudFront sends to the origin.

QueryStrings -> (structure)

Contains the specific query strings in viewer requests that either * **are** * or * **are not** * included in the cache key and in requests that CloudFront sends to the origin. The behavior depends on whether the `QueryStringBehavior` field in the `CachePolicyQueryStringsConfig` type is set to `whitelist` (the listed query strings * **are** * included) or `allExcept` (the listed query strings * **are not** * included, but all other query strings are).

Quantity -> (integer)

The number of query string names in the `Items` list.

Items -> (list)

A list of query string names.

(string)

ETag -> (string)

The current version of the cache policy.