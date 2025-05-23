# create-distributionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-distribution

## Description

Creates an Amazon Lightsail content delivery network (CDN) distribution.

A distribution is a globally distributed network of caching servers that improve the performance of your website or web application hosted on a Lightsail instance. For more information, see [Content delivery networks in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-content-delivery-network-distributions) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateDistribution)

## Synopsis

```
create-distribution
--distribution-name <value>
--origin <value>
--default-cache-behavior <value>
[--cache-behavior-settings <value>]
[--cache-behaviors <value>]
--bundle-id <value>
[--ip-address-type <value>]
[--tags <value>]
[--certificate-name <value>]
[--viewer-minimum-tls-protocol-version <value>]
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

`--distribution-name` (string)

The name for the distribution.

`--origin` (structure)

An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.

The distribution pulls, caches, and serves content from the origin.

name -> (string)

The name of the origin resource.

regionName -> (string)

The AWS Region name of the origin resource.

protocolPolicy -> (string)

The protocol that your Amazon Lightsail distribution uses when establishing a connection with your origin to pull content.

responseTimeout -> (integer)

The amount of time, in seconds, that the distribution waits for a response after forwarding a request to the origin. The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you donât specify otherwise) is 30 seconds.

Shorthand Syntax:

```
name=string,regionName=string,protocolPolicy=string,responseTimeout=integer
```

JSON Syntax:

```
{
  "name": "string",
  "regionName": "us-east-1"|"us-east-2"|"us-west-1"|"us-west-2"|"eu-west-1"|"eu-west-2"|"eu-west-3"|"eu-central-1"|"ca-central-1"|"ap-south-1"|"ap-southeast-1"|"ap-southeast-2"|"ap-northeast-1"|"ap-northeast-2"|"eu-north-1",
  "protocolPolicy": "http-only"|"https-only",
  "responseTimeout": integer
}
```

`--default-cache-behavior` (structure)

An object that describes the default cache behavior for the distribution.

behavior -> (string)

The cache behavior of the distribution.

The following cache behaviors can be specified:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id1)`cache` ** - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesnât change depending on who views it, or for websites that donât use cookies, headers, or query strings to personalize content.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id3)`dont-cache` ** - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serve only the content that is specified in the distributionâs `CacheBehaviorPerPath` parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.

Shorthand Syntax:

```
behavior=string
```

JSON Syntax:

```
{
  "behavior": "dont-cache"|"cache"
}
```

`--cache-behavior-settings` (structure)

An object that describes the cache behavior settings for the distribution.

defaultTTL -> (long)

The default amount of time that objects stay in the distributionâs cache before the distribution forwards another request to the origin to determine whether the content has been updated.

### Note

The value specified applies only when the origin does not add HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects.

minimumTTL -> (long)

The minimum amount of time that objects stay in the distributionâs cache before the distribution forwards another request to the origin to determine whether the object has been updated.

A value of `0` must be specified for `minimumTTL` if the distribution is configured to forward all headers to the origin.

maximumTTL -> (long)

The maximum amount of time that objects stay in the distributionâs cache before the distribution forwards another request to the origin to determine whether the object has been updated.

The value specified applies only when the origin adds HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects.

allowedHTTPMethods -> (string)

The HTTP methods that are processed and forwarded to the distributionâs origin.

You can specify the following options:

- `GET,HEAD` - The distribution forwards the `GET` and `HEAD` methods.
- `GET,HEAD,OPTIONS` - The distribution forwards the `GET` , `HEAD` , and `OPTIONS` methods.
- `GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE` - The distribution forwards the `GET` , `HEAD` , `OPTIONS` , `PUT` , `PATCH` , `POST` , and `DELETE` methods.

If you specify the third option, you might need to restrict access to your distributionâs origin so users canât perform operations that you donât want them to. For example, you might not want users to have permission to delete objects from your origin.

cachedHTTPMethods -> (string)

The HTTP method responses that are cached by your distribution.

You can specify the following options:

- `GET,HEAD` - The distribution caches responses to the `GET` and `HEAD` methods.
- `GET,HEAD,OPTIONS` - The distribution caches responses to the `GET` , `HEAD` , and `OPTIONS` methods.

forwardedCookies -> (structure)

An object that describes the cookies that are forwarded to the origin. Your content is cached based on the cookies that are forwarded.

option -> (string)

Specifies which cookies to forward to the distributionâs origin for a cache behavior: `all` , `none` , or `allow-list` to forward only the cookies specified in the `cookiesAllowList` parameter.

cookiesAllowList -> (list)

The specific cookies to forward to your distributionâs origin.

(string)

forwardedHeaders -> (structure)

An object that describes the headers that are forwarded to the origin. Your content is cached based on the headers that are forwarded.

option -> (string)

The headers that you want your distribution to forward to your origin and base caching on.

You can configure your distribution to do one of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id5)`all` ** - Forward all headers to your origin.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id7)`none` ** - Forward only the default headers.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id9)`allow-list` ** - Forward only the headers you specify using the `headersAllowList` parameter.

headersAllowList -> (list)

The specific headers to forward to your distributionâs origin.

(string)

forwardedQueryStrings -> (structure)

An object that describes the query strings that are forwarded to the origin. Your content is cached based on the query strings that are forwarded.

option -> (boolean)

Indicates whether the distribution forwards and caches based on query strings.

queryStringsAllowList -> (list)

The specific query strings that the distribution forwards to the origin.

Your distribution will cache content based on the specified query strings.

If the `option` parameter is true, then your distribution forwards all query strings, regardless of what you specify using the `queryStringsAllowList` parameter.

(string)

Shorthand Syntax:

```
defaultTTL=long,minimumTTL=long,maximumTTL=long,allowedHTTPMethods=string,cachedHTTPMethods=string,forwardedCookies={option=string,cookiesAllowList=[string,string]},forwardedHeaders={option=string,headersAllowList=[string,string]},forwardedQueryStrings={option=boolean,queryStringsAllowList=[string,string]}
```

JSON Syntax:

```
{
  "defaultTTL": long,
  "minimumTTL": long,
  "maximumTTL": long,
  "allowedHTTPMethods": "string",
  "cachedHTTPMethods": "string",
  "forwardedCookies": {
    "option": "none"|"allow-list"|"all",
    "cookiesAllowList": ["string", ...]
  },
  "forwardedHeaders": {
    "option": "none"|"allow-list"|"all",
    "headersAllowList": ["Accept"|"Accept-Charset"|"Accept-Datetime"|"Accept-Encoding"|"Accept-Language"|"Authorization"|"CloudFront-Forwarded-Proto"|"CloudFront-Is-Desktop-Viewer"|"CloudFront-Is-Mobile-Viewer"|"CloudFront-Is-SmartTV-Viewer"|"CloudFront-Is-Tablet-Viewer"|"CloudFront-Viewer-Country"|"Host"|"Origin"|"Referer", ...]
  },
  "forwardedQueryStrings": {
    "option": true|false,
    "queryStringsAllowList": ["string", ...]
  }
}
```

`--cache-behaviors` (list)

An array of objects that describe the per-path cache behavior for the distribution.

(structure)

Describes the per-path cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

A per-path cache behavior is used to override, or add an exception to, the default cache behavior of a distribution. For example, if the `cacheBehavior` is set to `cache` , then a per-path cache behavior can be used to specify a directory, file, or file type that your distribution will cache. Alternately, if the distributionâs `cacheBehavior` is `dont-cache` , then a per-path cache behavior can be used to specify a directory, file, or file type that your distribution will not cache.

path -> (string)

The path to a directory or file to cached, or not cache. Use an asterisk symbol to specify wildcard directories (`path/to/assets/*` ), and file types (`*.html, *jpg, *js` ). Directories and file paths are case-sensitive.

Examples:

- Specify the following to cache all files in the document root of an Apache web server running on a Lightsail instance.  `var/www/html/`
- Specify the following file to cache only the index page in the document root of an Apache web server.  `var/www/html/index.html`
- Specify the following to cache only the .html files in the document root of an Apache web server.  `var/www/html/*.html`
- Specify the following to cache only the .jpg, .png, and .gif files in the images sub-directory of the document root of an Apache web server.  `var/www/html/images/*.jpg` `var/www/html/images/*.png` `var/www/html/images/*.gif`   Specify the following to cache all files in the images sub-directory of the document root of an Apache web server.  `var/www/html/images/`

behavior -> (string)

The cache behavior for the specified path.

You can specify one of the following per-path cache behaviors:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id11)`cache` ** - This behavior caches the specified path.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id13)`dont-cache` ** - This behavior doesnât cache the specified path.

Shorthand Syntax:

```
path=string,behavior=string ...
```

JSON Syntax:

```
[
  {
    "path": "string",
    "behavior": "dont-cache"|"cache"
  }
  ...
]
```

`--bundle-id` (string)

The bundle ID to use for the distribution.

A distribution bundle describes the specifications of your distribution, such as the monthly cost and monthly network transfer quota.

Use the `GetDistributionBundles` action to get a list of distribution bundle IDs that you can specify.

`--ip-address-type` (string)

The IP address type for the distribution.

The possible values are `ipv4` for IPv4 only, and `dualstack` for IPv4 and IPv6.

The default value is `dualstack` .

Possible values:

- `dualstack`
- `ipv4`
- `ipv6`

`--tags` (list)

The tag keys and optional values to add to the distribution during create.

Use the `TagResource` action to tag a resource after itâs created.

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--certificate-name` (string)

The name of the SSL/TLS certificate that you want to attach to the distribution.

Use the [GetCertificates](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html) action to get a list of certificate names that you can specify.

`--viewer-minimum-tls-protocol-version` (string)

The minimum TLS protocol version for the SSL/TLS certificate.

Possible values:

- `TLSv1.1_2016`
- `TLSv1.2_2018`
- `TLSv1.2_2019`
- `TLSv1.2_2021`

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

distribution -> (structure)

An object that describes the distribution created.

name -> (string)

The name of the distribution.

arn -> (string)

The Amazon Resource Name (ARN) of the distribution.

supportCode -> (string)

The support code. Include this code in your email to support when you have questions about your Lightsail distribution. This code enables our support team to look up your Lightsail information more easily.

createdAt -> (timestamp)

The timestamp when the distribution was created.

location -> (structure)

An object that describes the location of the distribution, such as the Amazon Web Services Region and Availability Zone.

### Note

Lightsail distributions are global resources that can reference an origin in any Amazon Web Services Region, and distribute its content globally. However, all distributions are located in the `us-east-1` Region.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The Lightsail resource type (`Distribution` ).

alternativeDomainNames -> (list)

The alternate domain names of the distribution.

(string)

status -> (string)

The status of the distribution.

isEnabled -> (boolean)

Indicates whether the distribution is enabled.

domainName -> (string)

The domain name of the distribution.

bundleId -> (string)

The ID of the bundle currently applied to the distribution.

certificateName -> (string)

The name of the SSL/TLS certificate attached to the distribution, if any.

origin -> (structure)

An object that describes the origin resource of the distribution, such as a Lightsail instance, bucket, or load balancer.

The distribution pulls, caches, and serves content from the origin.

name -> (string)

The name of the origin resource.

resourceType -> (string)

The resource type of the origin resource (*Instance* ).

regionName -> (string)

The AWS Region name of the origin resource.

protocolPolicy -> (string)

The protocol that your Amazon Lightsail distribution uses when establishing a connection with your origin to pull content.

responseTimeout -> (integer)

The amount of time, in seconds, that the distribution waits for a response after forwarding a request to the origin. The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you donât specify otherwise) is 30 seconds.

originPublicDNS -> (string)

The public DNS of the origin.

defaultCacheBehavior -> (structure)

An object that describes the default cache behavior of the distribution.

behavior -> (string)

The cache behavior of the distribution.

The following cache behaviors can be specified:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id15)`cache` ** - This option is best for static sites. When specified, your distribution caches and serves your entire website as static content. This behavior is ideal for websites with static content that doesnât change depending on who views it, or for websites that donât use cookies, headers, or query strings to personalize content.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id17)`dont-cache` ** - This option is best for sites that serve a mix of static and dynamic content. When specified, your distribution caches and serve only the content that is specified in the distributionâs `CacheBehaviorPerPath` parameter. This behavior is ideal for websites or web applications that use cookies, headers, and query strings to personalize content for individual users.

cacheBehaviorSettings -> (structure)

An object that describes the cache behavior settings of the distribution.

defaultTTL -> (long)

The default amount of time that objects stay in the distributionâs cache before the distribution forwards another request to the origin to determine whether the content has been updated.

### Note

The value specified applies only when the origin does not add HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects.

minimumTTL -> (long)

The minimum amount of time that objects stay in the distributionâs cache before the distribution forwards another request to the origin to determine whether the object has been updated.

A value of `0` must be specified for `minimumTTL` if the distribution is configured to forward all headers to the origin.

maximumTTL -> (long)

The maximum amount of time that objects stay in the distributionâs cache before the distribution forwards another request to the origin to determine whether the object has been updated.

The value specified applies only when the origin adds HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects.

allowedHTTPMethods -> (string)

The HTTP methods that are processed and forwarded to the distributionâs origin.

You can specify the following options:

- `GET,HEAD` - The distribution forwards the `GET` and `HEAD` methods.
- `GET,HEAD,OPTIONS` - The distribution forwards the `GET` , `HEAD` , and `OPTIONS` methods.
- `GET,HEAD,OPTIONS,PUT,PATCH,POST,DELETE` - The distribution forwards the `GET` , `HEAD` , `OPTIONS` , `PUT` , `PATCH` , `POST` , and `DELETE` methods.

If you specify the third option, you might need to restrict access to your distributionâs origin so users canât perform operations that you donât want them to. For example, you might not want users to have permission to delete objects from your origin.

cachedHTTPMethods -> (string)

The HTTP method responses that are cached by your distribution.

You can specify the following options:

- `GET,HEAD` - The distribution caches responses to the `GET` and `HEAD` methods.
- `GET,HEAD,OPTIONS` - The distribution caches responses to the `GET` , `HEAD` , and `OPTIONS` methods.

forwardedCookies -> (structure)

An object that describes the cookies that are forwarded to the origin. Your content is cached based on the cookies that are forwarded.

option -> (string)

Specifies which cookies to forward to the distributionâs origin for a cache behavior: `all` , `none` , or `allow-list` to forward only the cookies specified in the `cookiesAllowList` parameter.

cookiesAllowList -> (list)

The specific cookies to forward to your distributionâs origin.

(string)

forwardedHeaders -> (structure)

An object that describes the headers that are forwarded to the origin. Your content is cached based on the headers that are forwarded.

option -> (string)

The headers that you want your distribution to forward to your origin and base caching on.

You can configure your distribution to do one of the following:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id19)`all` ** - Forward all headers to your origin.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id21)`none` ** - Forward only the default headers.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id23)`allow-list` ** - Forward only the headers you specify using the `headersAllowList` parameter.

headersAllowList -> (list)

The specific headers to forward to your distributionâs origin.

(string)

forwardedQueryStrings -> (structure)

An object that describes the query strings that are forwarded to the origin. Your content is cached based on the query strings that are forwarded.

option -> (boolean)

Indicates whether the distribution forwards and caches based on query strings.

queryStringsAllowList -> (list)

The specific query strings that the distribution forwards to the origin.

Your distribution will cache content based on the specified query strings.

If the `option` parameter is true, then your distribution forwards all query strings, regardless of what you specify using the `queryStringsAllowList` parameter.

(string)

cacheBehaviors -> (list)

An array of objects that describe the per-path cache behavior of the distribution.

(structure)

Describes the per-path cache behavior of an Amazon Lightsail content delivery network (CDN) distribution.

A per-path cache behavior is used to override, or add an exception to, the default cache behavior of a distribution. For example, if the `cacheBehavior` is set to `cache` , then a per-path cache behavior can be used to specify a directory, file, or file type that your distribution will cache. Alternately, if the distributionâs `cacheBehavior` is `dont-cache` , then a per-path cache behavior can be used to specify a directory, file, or file type that your distribution will not cache.

path -> (string)

The path to a directory or file to cached, or not cache. Use an asterisk symbol to specify wildcard directories (`path/to/assets/*` ), and file types (`*.html, *jpg, *js` ). Directories and file paths are case-sensitive.

Examples:

- Specify the following to cache all files in the document root of an Apache web server running on a Lightsail instance.  `var/www/html/`
- Specify the following file to cache only the index page in the document root of an Apache web server.  `var/www/html/index.html`
- Specify the following to cache only the .html files in the document root of an Apache web server.  `var/www/html/*.html`
- Specify the following to cache only the .jpg, .png, and .gif files in the images sub-directory of the document root of an Apache web server.  `var/www/html/images/*.jpg` `var/www/html/images/*.png` `var/www/html/images/*.gif`   Specify the following to cache all files in the images sub-directory of the document root of an Apache web server.  `var/www/html/images/`

behavior -> (string)

The cache behavior for the specified path.

You can specify one of the following per-path cache behaviors:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id25)`cache` ** - This behavior caches the specified path.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-distribution.html#id27)`dont-cache` ** - This behavior doesnât cache the specified path.

ableToUpdateBundle -> (boolean)

Indicates whether the bundle that is currently applied to your distribution, specified using the `distributionName` parameter, can be changed to another bundle.

Use the `UpdateDistributionBundle` action to change your distributionâs bundle.

ipAddressType -> (string)

The IP address type of the distribution.

The possible values are `ipv4` for IPv4 only, and `dualstack` for IPv4 and IPv6.

tags -> (list)

The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

viewerMinimumTlsProtocolVersion -> (string)

The minimum TLS protocol version that the distribution can use to communicate with viewers.

operation -> (structure)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

id -> (string)

The ID of the operation.

resourceName -> (string)

The resource name.

resourceType -> (string)

The resource type.

createdAt -> (timestamp)

The timestamp when the operation was initialized (`1479816991.349` ).

location -> (structure)

The Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

isTerminal -> (boolean)

A Boolean value indicating whether the operation is terminal.

operationDetails -> (string)

Details about the operation (`Debian-1GB-Ohio-1` ).

operationType -> (string)

The type of operation.

status -> (string)

The status of the operation.

statusChangedAt -> (timestamp)

The timestamp when the status was changed (`1479816991.349` ).

errorCode -> (string)

The error code.

errorDetails -> (string)

The error details.