# update-response-headers-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-response-headers-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-response-headers-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# update-response-headers-policy

## Description

Updates a response headers policy.

When you update a response headers policy, the entire policy is replaced. You cannot update some policy fields independent of others. To update a response headers policy configuration:

- Use `GetResponseHeadersPolicyConfig` to get the current policyâs configuration.
- Modify the fields in the response headers policy configuration that you want to update.
- Call `UpdateResponseHeadersPolicy` , providing the entire response headers policy configuration, including the fields that you modified and those that you didnât.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/UpdateResponseHeadersPolicy)

## Synopsis

```
update-response-headers-policy
--response-headers-policy-config <value>
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

`--response-headers-policy-config` (structure)

A response headers policy configuration.

Comment -> (string)

A comment to describe the response headers policy.

The comment cannot be longer than 128 characters.

Name -> (string)

A name to identify the response headers policy.

The name must be unique for response headers policies in this Amazon Web Services account.

CorsConfig -> (structure)

A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS).

AccessControlAllowOrigins -> (structure)

A list of origins (domain names) that CloudFront can use as the value for the `Access-Control-Allow-Origin` HTTP response header.

For more information about the `Access-Control-Allow-Origin` HTTP response header, see [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

Quantity -> (integer)

The number of origins in the list.

Items -> (list)

The list of origins (domain names). You can specify `*` to allow all origins.

(string)

AccessControlAllowHeaders -> (structure)

A list of HTTP header names that CloudFront includes as values for the `Access-Control-Allow-Headers` HTTP response header.

For more information about the `Access-Control-Allow-Headers` HTTP response header, see [Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) in the MDN Web Docs.

Quantity -> (integer)

The number of HTTP header names in the list.

Items -> (list)

The list of HTTP header names. You can specify `*` to allow all headers.

(string)

AccessControlAllowMethods -> (structure)

A list of HTTP methods that CloudFront includes as values for the `Access-Control-Allow-Methods` HTTP response header.

For more information about the `Access-Control-Allow-Methods` HTTP response header, see [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods) in the MDN Web Docs.

Quantity -> (integer)

The number of HTTP methods in the list.

Items -> (list)

The list of HTTP methods. Valid values are:

- `GET`
- `DELETE`
- `HEAD`
- `OPTIONS`
- `PATCH`
- `POST`
- `PUT`
- `ALL`

`ALL` is a special value that includes all of the listed HTTP methods.

(string)

AccessControlAllowCredentials -> (boolean)

A Boolean that CloudFront uses as the value for the `Access-Control-Allow-Credentials` HTTP response header.

For more information about the `Access-Control-Allow-Credentials` HTTP response header, see [Access-Control-Allow-Credentials](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials) in the MDN Web Docs.

AccessControlExposeHeaders -> (structure)

A list of HTTP headers that CloudFront includes as values for the `Access-Control-Expose-Headers` HTTP response header.

For more information about the `Access-Control-Expose-Headers` HTTP response header, see [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

Quantity -> (integer)

The number of HTTP headers in the list.

Items -> (list)

The list of HTTP headers. You can specify `*` to expose all headers.

(string)

AccessControlMaxAgeSec -> (integer)

A number that CloudFront uses as the value for the `Access-Control-Max-Age` HTTP response header.

For more information about the `Access-Control-Max-Age` HTTP response header, see [Access-Control-Max-Age](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age) in the MDN Web Docs.

OriginOverride -> (boolean)

A Boolean that determines whether CloudFront overrides HTTP response headers received from the origin with the ones specified in this response headers policy.

SecurityHeadersConfig -> (structure)

A configuration for a set of security-related HTTP response headers.

XSSProtection -> (structure)

Determines whether CloudFront includes the `X-XSS-Protection` HTTP response header and the headerâs value.

For more information about the `X-XSS-Protection` HTTP response header, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `X-XSS-Protection` HTTP response header received from the origin with the one specified in this response headers policy.

Protection -> (boolean)

A Boolean that determines the value of the `X-XSS-Protection` HTTP response header. When this setting is `true` , the value of the `X-XSS-Protection` header is `1` . When this setting is `false` , the value of the `X-XSS-Protection` header is `0` .

For more information about these settings, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

ModeBlock -> (boolean)

A Boolean that determines whether CloudFront includes the `mode=block` directive in the `X-XSS-Protection` header.

For more information about this directive, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

ReportUri -> (string)

A reporting URI, which CloudFront uses as the value of the `report` directive in the `X-XSS-Protection` header.

You cannot specify a `ReportUri` when `ModeBlock` is `true` .

For more information about using a reporting URL, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

FrameOptions -> (structure)

Determines whether CloudFront includes the `X-Frame-Options` HTTP response header and the headerâs value.

For more information about the `X-Frame-Options` HTTP response header, see [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `X-Frame-Options` HTTP response header received from the origin with the one specified in this response headers policy.

FrameOption -> (string)

The value of the `X-Frame-Options` HTTP response header. Valid values are `DENY` and `SAMEORIGIN` .

For more information about these values, see [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) in the MDN Web Docs.

ReferrerPolicy -> (structure)

Determines whether CloudFront includes the `Referrer-Policy` HTTP response header and the headerâs value.

For more information about the `Referrer-Policy` HTTP response header, see [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `Referrer-Policy` HTTP response header received from the origin with the one specified in this response headers policy.

ReferrerPolicy -> (string)

The value of the `Referrer-Policy` HTTP response header. Valid values are:

- `no-referrer`
- `no-referrer-when-downgrade`
- `origin`
- `origin-when-cross-origin`
- `same-origin`
- `strict-origin`
- `strict-origin-when-cross-origin`
- `unsafe-url`

For more information about these values, see [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) in the MDN Web Docs.

ContentSecurityPolicy -> (structure)

The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.

For more information about the `Content-Security-Policy` HTTP response header, see [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `Content-Security-Policy` HTTP response header received from the origin with the one specified in this response headers policy.

ContentSecurityPolicy -> (string)

The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.

ContentTypeOptions -> (structure)

Determines whether CloudFront includes the `X-Content-Type-Options` HTTP response header with its value set to `nosniff` .

For more information about the `X-Content-Type-Options` HTTP response header, see [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `X-Content-Type-Options` HTTP response header received from the origin with the one specified in this response headers policy.

StrictTransportSecurity -> (structure)

Determines whether CloudFront includes the `Strict-Transport-Security` HTTP response header and the headerâs value.

For more information about the `Strict-Transport-Security` HTTP response header, see [Security headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html#understanding-response-headers-policies-security) in the *Amazon CloudFront Developer Guide* and [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `Strict-Transport-Security` HTTP response header received from the origin with the one specified in this response headers policy.

IncludeSubdomains -> (boolean)

A Boolean that determines whether CloudFront includes the `includeSubDomains` directive in the `Strict-Transport-Security` HTTP response header.

Preload -> (boolean)

A Boolean that determines whether CloudFront includes the `preload` directive in the `Strict-Transport-Security` HTTP response header.

AccessControlMaxAgeSec -> (integer)

A number that CloudFront uses as the value for the `max-age` directive in the `Strict-Transport-Security` HTTP response header.

ServerTimingHeadersConfig -> (structure)

A configuration for enabling the `Server-Timing` header in HTTP responses sent from CloudFront.

Enabled -> (boolean)

A Boolean that determines whether CloudFront adds the `Server-Timing` header to HTTP responses that it sends in response to requests that match a cache behavior thatâs associated with this response headers policy.

SamplingRate -> (double)

A number 0â100 (inclusive) that specifies the percentage of responses that you want CloudFront to add the `Server-Timing` header to. When you set the sampling rate to 100, CloudFront adds the `Server-Timing` header to the HTTP response for every request that matches the cache behavior that this response headers policy is attached to. When you set it to 50, CloudFront adds the header to 50% of the responses for requests that match the cache behavior. You can set the sampling rate to any number 0â100 with up to four decimal places.

CustomHeadersConfig -> (structure)

A configuration for a set of custom HTTP response headers.

Quantity -> (integer)

The number of HTTP response headers in the list.

Items -> (list)

The list of HTTP response headers and their values.

(structure)

An HTTP response header name and its value. CloudFront includes this header in HTTP responses that it sends for requests that match a cache behavior thatâs associated with this response headers policy.

Header -> (string)

The HTTP response header name.

Value -> (string)

The value for the HTTP response header.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides a response header with the same name received from the origin with the header specified here.

RemoveHeadersConfig -> (structure)

A configuration for a set of HTTP headers to remove from the HTTP response.

Quantity -> (integer)

The number of HTTP header names in the list.

Items -> (list)

The list of HTTP header names.

(structure)

The name of an HTTP header that CloudFront removes from HTTP responses to requests that match the cache behavior that this response headers policy is attached to.

Header -> (string)

The HTTP header name.

JSON Syntax:

```
{
  "Comment": "string",
  "Name": "string",
  "CorsConfig": {
    "AccessControlAllowOrigins": {
      "Quantity": integer,
      "Items": ["string", ...]
    },
    "AccessControlAllowHeaders": {
      "Quantity": integer,
      "Items": ["string", ...]
    },
    "AccessControlAllowMethods": {
      "Quantity": integer,
      "Items": ["GET"|"POST"|"OPTIONS"|"PUT"|"DELETE"|"PATCH"|"HEAD"|"ALL", ...]
    },
    "AccessControlAllowCredentials": true|false,
    "AccessControlExposeHeaders": {
      "Quantity": integer,
      "Items": ["string", ...]
    },
    "AccessControlMaxAgeSec": integer,
    "OriginOverride": true|false
  },
  "SecurityHeadersConfig": {
    "XSSProtection": {
      "Override": true|false,
      "Protection": true|false,
      "ModeBlock": true|false,
      "ReportUri": "string"
    },
    "FrameOptions": {
      "Override": true|false,
      "FrameOption": "DENY"|"SAMEORIGIN"
    },
    "ReferrerPolicy": {
      "Override": true|false,
      "ReferrerPolicy": "no-referrer"|"no-referrer-when-downgrade"|"origin"|"origin-when-cross-origin"|"same-origin"|"strict-origin"|"strict-origin-when-cross-origin"|"unsafe-url"
    },
    "ContentSecurityPolicy": {
      "Override": true|false,
      "ContentSecurityPolicy": "string"
    },
    "ContentTypeOptions": {
      "Override": true|false
    },
    "StrictTransportSecurity": {
      "Override": true|false,
      "IncludeSubdomains": true|false,
      "Preload": true|false,
      "AccessControlMaxAgeSec": integer
    }
  },
  "ServerTimingHeadersConfig": {
    "Enabled": true|false,
    "SamplingRate": double
  },
  "CustomHeadersConfig": {
    "Quantity": integer,
    "Items": [
      {
        "Header": "string",
        "Value": "string",
        "Override": true|false
      }
      ...
    ]
  },
  "RemoveHeadersConfig": {
    "Quantity": integer,
    "Items": [
      {
        "Header": "string"
      }
      ...
    ]
  }
}
```

`--id` (string)

The identifier for the response headers policy that you are updating.

`--if-match` (string)

The version of the response headers policy that you are updating.

The version is returned in the cache policyâs `ETag` field in the response to `GetResponseHeadersPolicyConfig` .

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

ResponseHeadersPolicy -> (structure)

A response headers policy.

Id -> (string)

The identifier for the response headers policy.

LastModifiedTime -> (timestamp)

The date and time when the response headers policy was last modified.

ResponseHeadersPolicyConfig -> (structure)

A response headers policy configuration.

Comment -> (string)

A comment to describe the response headers policy.

The comment cannot be longer than 128 characters.

Name -> (string)

A name to identify the response headers policy.

The name must be unique for response headers policies in this Amazon Web Services account.

CorsConfig -> (structure)

A configuration for a set of HTTP response headers that are used for cross-origin resource sharing (CORS).

AccessControlAllowOrigins -> (structure)

A list of origins (domain names) that CloudFront can use as the value for the `Access-Control-Allow-Origin` HTTP response header.

For more information about the `Access-Control-Allow-Origin` HTTP response header, see [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

Quantity -> (integer)

The number of origins in the list.

Items -> (list)

The list of origins (domain names). You can specify `*` to allow all origins.

(string)

AccessControlAllowHeaders -> (structure)

A list of HTTP header names that CloudFront includes as values for the `Access-Control-Allow-Headers` HTTP response header.

For more information about the `Access-Control-Allow-Headers` HTTP response header, see [Access-Control-Allow-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers) in the MDN Web Docs.

Quantity -> (integer)

The number of HTTP header names in the list.

Items -> (list)

The list of HTTP header names. You can specify `*` to allow all headers.

(string)

AccessControlAllowMethods -> (structure)

A list of HTTP methods that CloudFront includes as values for the `Access-Control-Allow-Methods` HTTP response header.

For more information about the `Access-Control-Allow-Methods` HTTP response header, see [Access-Control-Allow-Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods) in the MDN Web Docs.

Quantity -> (integer)

The number of HTTP methods in the list.

Items -> (list)

The list of HTTP methods. Valid values are:

- `GET`
- `DELETE`
- `HEAD`
- `OPTIONS`
- `PATCH`
- `POST`
- `PUT`
- `ALL`

`ALL` is a special value that includes all of the listed HTTP methods.

(string)

AccessControlAllowCredentials -> (boolean)

A Boolean that CloudFront uses as the value for the `Access-Control-Allow-Credentials` HTTP response header.

For more information about the `Access-Control-Allow-Credentials` HTTP response header, see [Access-Control-Allow-Credentials](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials) in the MDN Web Docs.

AccessControlExposeHeaders -> (structure)

A list of HTTP headers that CloudFront includes as values for the `Access-Control-Expose-Headers` HTTP response header.

For more information about the `Access-Control-Expose-Headers` HTTP response header, see [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

Quantity -> (integer)

The number of HTTP headers in the list.

Items -> (list)

The list of HTTP headers. You can specify `*` to expose all headers.

(string)

AccessControlMaxAgeSec -> (integer)

A number that CloudFront uses as the value for the `Access-Control-Max-Age` HTTP response header.

For more information about the `Access-Control-Max-Age` HTTP response header, see [Access-Control-Max-Age](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age) in the MDN Web Docs.

OriginOverride -> (boolean)

A Boolean that determines whether CloudFront overrides HTTP response headers received from the origin with the ones specified in this response headers policy.

SecurityHeadersConfig -> (structure)

A configuration for a set of security-related HTTP response headers.

XSSProtection -> (structure)

Determines whether CloudFront includes the `X-XSS-Protection` HTTP response header and the headerâs value.

For more information about the `X-XSS-Protection` HTTP response header, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `X-XSS-Protection` HTTP response header received from the origin with the one specified in this response headers policy.

Protection -> (boolean)

A Boolean that determines the value of the `X-XSS-Protection` HTTP response header. When this setting is `true` , the value of the `X-XSS-Protection` header is `1` . When this setting is `false` , the value of the `X-XSS-Protection` header is `0` .

For more information about these settings, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

ModeBlock -> (boolean)

A Boolean that determines whether CloudFront includes the `mode=block` directive in the `X-XSS-Protection` header.

For more information about this directive, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

ReportUri -> (string)

A reporting URI, which CloudFront uses as the value of the `report` directive in the `X-XSS-Protection` header.

You cannot specify a `ReportUri` when `ModeBlock` is `true` .

For more information about using a reporting URL, see [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection) in the MDN Web Docs.

FrameOptions -> (structure)

Determines whether CloudFront includes the `X-Frame-Options` HTTP response header and the headerâs value.

For more information about the `X-Frame-Options` HTTP response header, see [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `X-Frame-Options` HTTP response header received from the origin with the one specified in this response headers policy.

FrameOption -> (string)

The value of the `X-Frame-Options` HTTP response header. Valid values are `DENY` and `SAMEORIGIN` .

For more information about these values, see [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options) in the MDN Web Docs.

ReferrerPolicy -> (structure)

Determines whether CloudFront includes the `Referrer-Policy` HTTP response header and the headerâs value.

For more information about the `Referrer-Policy` HTTP response header, see [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `Referrer-Policy` HTTP response header received from the origin with the one specified in this response headers policy.

ReferrerPolicy -> (string)

The value of the `Referrer-Policy` HTTP response header. Valid values are:

- `no-referrer`
- `no-referrer-when-downgrade`
- `origin`
- `origin-when-cross-origin`
- `same-origin`
- `strict-origin`
- `strict-origin-when-cross-origin`
- `unsafe-url`

For more information about these values, see [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) in the MDN Web Docs.

ContentSecurityPolicy -> (structure)

The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.

For more information about the `Content-Security-Policy` HTTP response header, see [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `Content-Security-Policy` HTTP response header received from the origin with the one specified in this response headers policy.

ContentSecurityPolicy -> (string)

The policy directives and their values that CloudFront includes as values for the `Content-Security-Policy` HTTP response header.

ContentTypeOptions -> (structure)

Determines whether CloudFront includes the `X-Content-Type-Options` HTTP response header with its value set to `nosniff` .

For more information about the `X-Content-Type-Options` HTTP response header, see [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `X-Content-Type-Options` HTTP response header received from the origin with the one specified in this response headers policy.

StrictTransportSecurity -> (structure)

Determines whether CloudFront includes the `Strict-Transport-Security` HTTP response header and the headerâs value.

For more information about the `Strict-Transport-Security` HTTP response header, see [Security headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/understanding-response-headers-policies.html#understanding-response-headers-policies-security) in the *Amazon CloudFront Developer Guide* and [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) in the MDN Web Docs.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides the `Strict-Transport-Security` HTTP response header received from the origin with the one specified in this response headers policy.

IncludeSubdomains -> (boolean)

A Boolean that determines whether CloudFront includes the `includeSubDomains` directive in the `Strict-Transport-Security` HTTP response header.

Preload -> (boolean)

A Boolean that determines whether CloudFront includes the `preload` directive in the `Strict-Transport-Security` HTTP response header.

AccessControlMaxAgeSec -> (integer)

A number that CloudFront uses as the value for the `max-age` directive in the `Strict-Transport-Security` HTTP response header.

ServerTimingHeadersConfig -> (structure)

A configuration for enabling the `Server-Timing` header in HTTP responses sent from CloudFront.

Enabled -> (boolean)

A Boolean that determines whether CloudFront adds the `Server-Timing` header to HTTP responses that it sends in response to requests that match a cache behavior thatâs associated with this response headers policy.

SamplingRate -> (double)

A number 0â100 (inclusive) that specifies the percentage of responses that you want CloudFront to add the `Server-Timing` header to. When you set the sampling rate to 100, CloudFront adds the `Server-Timing` header to the HTTP response for every request that matches the cache behavior that this response headers policy is attached to. When you set it to 50, CloudFront adds the header to 50% of the responses for requests that match the cache behavior. You can set the sampling rate to any number 0â100 with up to four decimal places.

CustomHeadersConfig -> (structure)

A configuration for a set of custom HTTP response headers.

Quantity -> (integer)

The number of HTTP response headers in the list.

Items -> (list)

The list of HTTP response headers and their values.

(structure)

An HTTP response header name and its value. CloudFront includes this header in HTTP responses that it sends for requests that match a cache behavior thatâs associated with this response headers policy.

Header -> (string)

The HTTP response header name.

Value -> (string)

The value for the HTTP response header.

Override -> (boolean)

A Boolean that determines whether CloudFront overrides a response header with the same name received from the origin with the header specified here.

RemoveHeadersConfig -> (structure)

A configuration for a set of HTTP headers to remove from the HTTP response.

Quantity -> (integer)

The number of HTTP header names in the list.

Items -> (list)

The list of HTTP header names.

(structure)

The name of an HTTP header that CloudFront removes from HTTP responses to requests that match the cache behavior that this response headers policy is attached to.

Header -> (string)

The HTTP header name.

ETag -> (string)

The current version of the response headers policy.