# get-distributionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# get-distribution

## Description

Get the information about a distribution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/GetDistribution)

## Synopsis

```
get-distribution
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

The distributionâs ID. If the ID is empty, an empty distribution configuration is returned.

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

**To get a CloudFront distribution**

The following `get-distribution` example gets the CloudFront distribution with the ID `EDFDVBD6EXAMPLE`, including its `ETag`. The distribution ID is returned in the [create-distribution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution.html) and [list-distributions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distributions.html) commands.

```
aws cloudfront get-distribution \
    --id EDFDVBD6EXAMPLE
```

Output:

```
{
    "ETag": "E2QWRUHEXAMPLE",
    "Distribution": {
        "Id": "EDFDVBD6EXAMPLE",
        "ARN": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE",
        "Status": "Deployed",
        "LastModifiedTime": "2019-12-04T23:35:41.433Z",
        "InProgressInvalidationBatches": 0,
        "DomainName": "d111111abcdef8.cloudfront.net",
        "ActiveTrustedSigners": {
            "Enabled": false,
            "Quantity": 0
        },
        "DistributionConfig": {
            "CallerReference": "cli-example",
            "Aliases": {
                "Quantity": 0
            },
            "DefaultRootObject": "index.html",
            "Origins": {
                "Quantity": 1,
                "Items": [
                    {
                        "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example",
                        "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com",
                        "OriginPath": "",
                        "CustomHeaders": {
                            "Quantity": 0
                        },
                        "S3OriginConfig": {
                            "OriginAccessIdentity": ""
                        }
                    }
                ]
            },
            "OriginGroups": {
                "Quantity": 0
            },
            "DefaultCacheBehavior": {
                "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example",
                "ForwardedValues": {
                    "QueryString": false,
                    "Cookies": {
                        "Forward": "none"
                    },
                    "Headers": {
                        "Quantity": 0
                    },
                    "QueryStringCacheKeys": {
                        "Quantity": 0
                    }
                },
                "TrustedSigners": {
                    "Enabled": false,
                    "Quantity": 0
                },
                "ViewerProtocolPolicy": "allow-all",
                "MinTTL": 0,
                "AllowedMethods": {
                    "Quantity": 2,
                    "Items": [
                        "HEAD",
                        "GET"
                    ],
                    "CachedMethods": {
                        "Quantity": 2,
                        "Items": [
                            "HEAD",
                            "GET"
                        ]
                    }
                },
                "SmoothStreaming": false,
                "DefaultTTL": 86400,
                "MaxTTL": 31536000,
                "Compress": false,
                "LambdaFunctionAssociations": {
                    "Quantity": 0
                },
                "FieldLevelEncryptionId": ""
            },
            "CacheBehaviors": {
                "Quantity": 0
            },
            "CustomErrorResponses": {
                "Quantity": 0
            },
            "Comment": "",
            "Logging": {
                "Enabled": false,
                "IncludeCookies": false,
                "Bucket": "",
                "Prefix": ""
            },
            "PriceClass": "PriceClass_All",
            "Enabled": true,
            "ViewerCertificate": {
                "CloudFrontDefaultCertificate": true,
                "MinimumProtocolVersion": "TLSv1",
                "CertificateSource": "cloudfront"
            },
            "Restrictions": {
                "GeoRestriction": {
                    "RestrictionType": "none",
                    "Quantity": 0
                }
            },
            "WebACLId": "",
            "HttpVersion": "http2",
            "IsIPV6Enabled": true
        }
    }
}
```

## Output

Distribution -> (structure)

The distributionâs information.

Id -> (string)

The distributionâs identifier. For example: `E1U5RQF7T870K0` .

ARN -> (string)

The distributionâs Amazon Resource Name (ARN).

Status -> (string)

The distributionâs status. When the status is `Deployed` , the distributionâs information is fully propagated to all CloudFront edge locations.

LastModifiedTime -> (timestamp)

The date and time when the distribution was last modified.

InProgressInvalidationBatches -> (integer)

The number of invalidation batches currently in progress.

DomainName -> (string)

The distributionâs CloudFront domain name. For example: `d111111abcdef8.cloudfront.net` .

ActiveTrustedSigners -> (structure)

### Warning

We recommend using `TrustedKeyGroups` instead of `TrustedSigners` .

This field contains a list of Amazon Web Services account IDs and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs or signed cookies.

Enabled -> (boolean)

This field is `true` if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is `false` .

Quantity -> (integer)

The number of Amazon Web Services accounts in the list.

Items -> (list)

A list of Amazon Web Services accounts and the identifiers of active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs and signed cookies.

(structure)

A list of Amazon Web Services accounts and the active CloudFront key pairs in each account that CloudFront can use to verify the signatures of signed URLs and signed cookies.

AwsAccountNumber -> (string)

An Amazon Web Services account number that contains active CloudFront key pairs that CloudFront can use to verify the signatures of signed URLs and signed cookies. If the Amazon Web Services account that owns the key pairs is the same account that owns the CloudFront distribution, the value of this field is `self` .

KeyPairIds -> (structure)

A list of CloudFront key pair identifiers.

Quantity -> (integer)

The number of key pair identifiers in the list.

Items -> (list)

A list of CloudFront key pair identifiers.

(string)

ActiveTrustedKeyGroups -> (structure)

This field contains a list of key groups and the public keys in each key group that CloudFront can use to verify the signatures of signed URLs or signed cookies.

Enabled -> (boolean)

This field is `true` if any of the key groups have public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not, this field is `false` .

Quantity -> (integer)

The number of key groups in the list.

Items -> (list)

A list of key groups, including the identifiers of the public keys in each key group that CloudFront can use to verify the signatures of signed URLs and signed cookies.

(structure)

A list of identifiers for the public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies.

KeyGroupId -> (string)

The identifier of the key group that contains the public keys.

KeyPairIds -> (structure)

A list of CloudFront key pair identifiers.

Quantity -> (integer)

The number of key pair identifiers in the list.

Items -> (list)

A list of CloudFront key pair identifiers.

(string)

DistributionConfig -> (structure)

The distributionâs configuration.

CallerReference -> (string)

A unique value (for example, a date-time stamp) that ensures that the request canât be replayed.

If the value of `CallerReference` is new (regardless of the content of the `DistributionConfig` object), CloudFront creates a new distribution.

If `CallerReference` is a value that you already sent in a previous request to create a distribution, CloudFront returns a `DistributionAlreadyExists` error.

Aliases -> (structure)

A complex type that contains information about CNAMEs (alternate domain names), if any, for this distribution.

Quantity -> (integer)

The number of CNAME aliases, if any, that you want to associate with this distribution.

Items -> (list)

A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string)

DefaultRootObject -> (string)

When a viewer requests the root URL for your distribution, the default root object is the object that you want CloudFront to request from your origin. For example, if your root URL is `https://www.example.com` , you can specify CloudFront to return the `index.html` file as the default root object. You can specify a default root object so that viewers see a specific file or object, instead of another object in your distribution (for example, `https://www.example.com/product-description.html` ). A default root object avoids exposing the contents of your distribution.

You can specify the object name or a path to the object name (for example, `index.html` or `exampleFolderName/index.html` ). Your string canât begin with a forward slash (`/` ). Only specify the object name or the path to the object.

If you donât want to specify a default root object when you create a distribution, include an empty `DefaultRootObject` element.

To delete the default root object from an existing distribution, update the distribution configuration and include an empty `DefaultRootObject` element.

To replace the default root object, update the distribution configuration and specify the new object.

For more information about the default root object, see [Specify a default root object](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html) in the *Amazon CloudFront Developer Guide* .

Origins -> (structure)

A complex type that contains information about origins for this distribution.

Quantity -> (integer)

The number of origins for this distribution.

Items -> (list)

A list of origins.

(structure)

An origin.

An origin is the location where content is stored, and from which CloudFront gets content to serve to viewers. To specify an origin:

- Use `S3OriginConfig` to specify an Amazon S3 bucket that is not configured with static website hosting.
- Use `VpcOriginConfig` to specify a VPC origin.
- Use `CustomOriginConfig` to specify all other kinds of origins, including:
- An Amazon S3 bucket that is configured with static website hosting
- An Elastic Load Balancing load balancer
- An Elemental MediaPackage endpoint
- An Elemental MediaStore container
- Any other HTTP server, running on an Amazon EC2 instance or any other kind of host

For the current maximum number of origins that you can specify per distribution, see [General Quotas on Web Distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html#limits-web-distributions) in the *Amazon CloudFront Developer Guide* (quotas were formerly referred to as limits).

Id -> (string)

A unique identifier for the origin. This value must be unique within the distribution.

Use this value to specify the `TargetOriginId` in a `CacheBehavior` or `DefaultCacheBehavior` .

DomainName -> (string)

The domain name for the origin.

For more information, see [Origin Domain Name](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesDomainName) in the *Amazon CloudFront Developer Guide* .

OriginPath -> (string)

An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

For more information, see [Origin Path](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginPath) in the *Amazon CloudFront Developer Guide* .

CustomHeaders -> (structure)

A list of HTTP header names and values that CloudFront adds to the requests that it sends to the origin.

For more information, see [Adding Custom Headers to Origin Requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of custom headers, if any, for this distribution.

Items -> (list)

**Optional** : A list that contains one `OriginCustomHeader` element for each custom header that you want CloudFront to forward to the origin. If Quantity is `0` , omit `Items` .

(structure)

A complex type that contains `HeaderName` and `HeaderValue` elements, if any, for this distribution.

HeaderName -> (string)

The name of a header that you want CloudFront to send to your origin. For more information, see [Adding Custom Headers to Origin Requests](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/forward-custom-headers.html) in the *Amazon CloudFront Developer Guide* .

HeaderValue -> (string)

The value for the header that you specified in the `HeaderName` field.

S3OriginConfig -> (structure)

Use this type to specify an origin that is an Amazon S3 bucket that is not configured with static website hosting. To specify any other type of origin, including an Amazon S3 bucket that is configured with static website hosting, use the `CustomOriginConfig` type instead.

OriginAccessIdentity -> (string)

### Note

If youâre using origin access control (OAC) instead of origin access identity, specify an empty `OriginAccessIdentity` element. For more information, see [Restricting access to an Amazon Web Services](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html) in the *Amazon CloudFront Developer Guide* .

The CloudFront origin access identity to associate with the origin. Use an origin access identity to configure the origin so that viewers can *only* access objects in an Amazon S3 bucket through CloudFront. The format of the value is:

`origin-access-identity/cloudfront/ID-of-origin-access-identity`

The `` *ID-of-origin-access-identity* `` is the value that CloudFront returned in the `ID` element when you created the origin access identity.

If you want viewers to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty `OriginAccessIdentity` element.

To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty `OriginAccessIdentity` element.

To replace the origin access identity, update the distribution configuration and specify the new origin access identity.

For more information about the origin access identity, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

CustomOriginConfig -> (structure)

Use this type to specify an origin that is not an Amazon S3 bucket, with one exception. If the Amazon S3 bucket is configured with static website hosting, use this type. If the Amazon S3 bucket is not configured with static website hosting, use the `S3OriginConfig` type instead.

HTTPPort -> (integer)

The HTTP port that CloudFront uses to connect to the origin. Specify the HTTP port that the origin listens on.

HTTPSPort -> (integer)

The HTTPS port that CloudFront uses to connect to the origin. Specify the HTTPS port that the origin listens on.

OriginProtocolPolicy -> (string)

Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Valid values are:

- `http-only` â CloudFront always uses HTTP to connect to the origin.
- `match-viewer` â CloudFront connects to the origin using the same protocol that the viewer used to connect to CloudFront.
- `https-only` â CloudFront always uses HTTPS to connect to the origin.

OriginSslProtocols -> (structure)

Specifies the minimum SSL/TLS protocol that CloudFront uses when connecting to your origin over HTTPS. Valid values include `SSLv3` , `TLSv1` , `TLSv1.1` , and `TLSv1.2` .

For more information, see [Minimum Origin SSL Protocol](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginSSLProtocols) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of SSL/TLS protocols that you want to allow CloudFront to use when establishing an HTTPS connection with this origin.

Items -> (list)

A list that contains allowed SSL/TLS protocols for this distribution.

(string)

OriginReadTimeout -> (integer)

Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout* . The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you donât specify otherwise) is 30 seconds.

For more information, see [Response timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide* .

OriginKeepaliveTimeout -> (integer)

Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you donât specify otherwise) is 5 seconds.

For more information, see [Keep-alive timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginKeepaliveTimeout) in the *Amazon CloudFront Developer Guide* .

VpcOriginConfig -> (structure)

The VPC origin configuration.

VpcOriginId -> (string)

The VPC origin ID.

OriginReadTimeout -> (integer)

Specifies how long, in seconds, CloudFront waits for a response from the origin. This is also known as the *origin response timeout* . The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you donât specify otherwise) is 30 seconds.

For more information, see [Response timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginResponseTimeout) in the *Amazon CloudFront Developer Guide* .

OriginKeepaliveTimeout -> (integer)

Specifies how long, in seconds, CloudFront persists its connection to the origin. The minimum timeout is 1 second, the maximum is 60 seconds, and the default (if you donât specify otherwise) is 5 seconds.

For more information, see [Keep-alive timeout (custom origins only)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginKeepaliveTimeout) in the *Amazon CloudFront Developer Guide* .

ConnectionAttempts -> (integer)

The number of times that CloudFront attempts to connect to the origin. The minimum number is 1, the maximum is 3, and the default (if you donât specify otherwise) is 3.

For a custom origin (including an Amazon S3 bucket thatâs configured with static website hosting), this value also specifies the number of times that CloudFront attempts to get a response from the origin, in the case of an [Origin Response Timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginResponseTimeout) .

For more information, see [Origin Connection Attempts](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#origin-connection-attempts) in the *Amazon CloudFront Developer Guide* .

ConnectionTimeout -> (integer)

The number of seconds that CloudFront waits when trying to establish a connection to the origin. The minimum timeout is 1 second, the maximum is 10 seconds, and the default (if you donât specify otherwise) is 10 seconds.

For more information, see [Origin Connection Timeout](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#origin-connection-timeout) in the *Amazon CloudFront Developer Guide* .

OriginShield -> (structure)

CloudFront Origin Shield. Using Origin Shield can help reduce the load on your origin.

For more information, see [Using Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

A flag that specifies whether Origin Shield is enabled.

When itâs enabled, CloudFront routes all requests through Origin Shield, which can help protect your origin. When itâs disabled, CloudFront might send requests directly to your origin from multiple edge locations or regional edge caches.

OriginShieldRegion -> (string)

The Amazon Web Services Region for Origin Shield.

Specify the Amazon Web Services Region that has the lowest latency to your origin. To specify a region, use the region code, not the region name. For example, specify the US East (Ohio) region as `us-east-2` .

When you enable CloudFront Origin Shield, you must specify the Amazon Web Services Region for Origin Shield. For the list of Amazon Web Services Regions that you can specify, and for help choosing the best Region for your origin, see [Choosing the Amazon Web Services Region for Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html#choose-origin-shield-region) in the *Amazon CloudFront Developer Guide* .

OriginAccessControlId -> (string)

The unique identifier of an origin access control for this origin.

For more information, see [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide* .

OriginGroups -> (structure)

A complex type that contains information about origin groups for this distribution.

Quantity -> (integer)

The number of origin groups.

Items -> (list)

The items (origin groups) in a distribution.

(structure)

An origin group includes two origins (a primary origin and a secondary origin to failover to) and a failover criteria that you specify. You create an origin group to support origin failover in CloudFront. When you create or update a distribution, you can specify the origin group instead of a single origin, and CloudFront will failover from the primary origin to the secondary origin under the failover conditions that youâve chosen.

Optionally, you can choose selection criteria for your origin group to specify how your origins are selected when your distribution routes viewer requests.

Id -> (string)

The origin groupâs ID.

FailoverCriteria -> (structure)

A complex type that contains information about the failover criteria for an origin group.

StatusCodes -> (structure)

The status codes that, when returned from the primary origin, will trigger CloudFront to failover to the second origin.

Quantity -> (integer)

The number of status codes.

Items -> (list)

The items (status codes) for an origin group.

(integer)

Members -> (structure)

A complex type that contains information about the origins in an origin group.

Quantity -> (integer)

The number of origins in an origin group.

Items -> (list)

Items (origins) in an origin group.

(structure)

An origin in an origin group.

OriginId -> (string)

The ID for an origin in an origin group.

SelectionCriteria -> (string)

The selection criteria for the origin group. For more information, see [Create an origin group](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html#concept_origin_groups.creating) in the *Amazon CloudFront Developer Guide* .

DefaultCacheBehavior -> (structure)

A complex type that describes the default cache behavior if you donât specify a `CacheBehavior` element or if files donât match any of the values of `PathPattern` in `CacheBehavior` elements. You must create exactly one default cache behavior.

TargetOriginId -> (string)

The value of `ID` for the origin that you want CloudFront to route requests to when they use the default cache behavior.

TrustedSigners -> (structure)

### Warning

We recommend using `TrustedKeyGroups` instead of `TrustedSigners` .

A list of Amazon Web Services account IDs whose public keys CloudFront can use to validate signed URLs or signed cookies.

When a cache behavior contains trusted signers, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with the private key of a CloudFront key pair in a trusted signerâs Amazon Web Services account. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is `false` .

Quantity -> (integer)

The number of Amazon Web Services accounts in the list.

Items -> (list)

A list of Amazon Web Services account identifiers.

(string)

TrustedKeyGroups -> (structure)

A list of key groups that CloudFront can use to validate signed URLs or signed cookies.

When a cache behavior contains trusted key groups, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the key groups in the list have public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not, this field is `false` .

Quantity -> (integer)

The number of key groups in the list.

Items -> (list)

A list of key groups identifiers.

(string)

ViewerProtocolPolicy -> (string)

The protocol that viewers can use to access the files in the origin specified by `TargetOriginId` when a request matches the path pattern in `PathPattern` . You can specify the following options:

- `allow-all` : Viewers can use HTTP or HTTPS.
- `redirect-to-https` : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
- `https-only` : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see [Requiring HTTPS Between Viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in the *Amazon CloudFront Developer Guide* .

### Note

The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objectsâ cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see [Managing Cache Expiration](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

AllowedMethods -> (structure)

A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

- CloudFront forwards only `GET` and `HEAD` requests.
- CloudFront forwards only `GET` , `HEAD` , and `OPTIONS` requests.
- CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST` , and `DELETE` requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users canât perform operations that you donât want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity -> (integer)

The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for `GET` and `HEAD` requests), 3 (for `GET` , `HEAD` , and `OPTIONS` requests) and 7 (for `GET, HEAD, OPTIONS, PUT, PATCH, POST` , and `DELETE` requests).

Items -> (list)

A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string)

CachedMethods -> (structure)

A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

- CloudFront caches responses to `GET` and `HEAD` requests.
- CloudFront caches responses to `GET` , `HEAD` , and `OPTIONS` requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity -> (integer)

The number of HTTP methods for which you want CloudFront to cache responses. Valid values are `2` (for caching responses to `GET` and `HEAD` requests) and `3` (for caching responses to `GET` , `HEAD` , and `OPTIONS` requests).

Items -> (list)

A complex type that contains the HTTP methods that you want CloudFront to cache responses to. Valid values for `CachedMethods` include `GET` , `HEAD` , and `OPTIONS` , depending on which caching option you choose. For more information, see the preceding section.

(string)

SmoothStreaming -> (boolean)

Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify `true` ; if not, specify `false` . If you specify `true` for `SmoothStreaming` , you can still distribute other content using this cache behavior if the content matches the value of `PathPattern` .

Compress -> (boolean)

Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify `true` ; if not, specify `false` . For more information, see [Serving Compressed Files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html) in the *Amazon CloudFront Developer Guide* .

LambdaFunctionAssociations -> (structure)

A complex type that contains zero or more [Lambda@Edge](mailto:Lambda%40Edge) function associations for a cache behavior.

Quantity -> (integer)

The number of [Lambda@Edge](mailto:Lambda%40Edge) function associations for this cache behavior.

Items -> (list)

**Optional** : A complex type that contains `LambdaFunctionAssociation` items for this cache behavior. If `Quantity` is `0` , you can omit `Items` .

(structure)

A complex type that contains a [Lambda@Edge](mailto:Lambda%40Edge) function association.

LambdaFunctionARN -> (string)

The ARN of the [Lambda@Edge](mailto:Lambda%40Edge) function. You must specify the ARN of a function version; you canât specify an alias or $LATEST.

EventType -> (string)

Specifies the event type that triggers a [Lambda@Edge](mailto:Lambda%40Edge) function invocation. You can specify the following values:

- `viewer-request` : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
- `origin-request` : The function executes only when CloudFront sends a request to your origin. When the requested object is in the edge cache, the function doesnât execute.
- `origin-response` : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesnât execute.
- `viewer-response` : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesnât execute.

IncludeBody -> (boolean)

A flag that allows a [Lambda@Edge](mailto:Lambda%40Edge) function to have read access to the body content. For more information, see [Accessing the Request Body by Choosing the Include Body Option](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.html) in the Amazon CloudFront Developer Guide.

FunctionAssociations -> (structure)

A list of CloudFront functions that are associated with this cache behavior. Your functions must be published to the `LIVE` stage to associate them with a cache behavior.

Quantity -> (integer)

The number of CloudFront functions in the list.

Items -> (list)

The CloudFront functions that are associated with a cache behavior in a CloudFront distribution. Your functions must be published to the `LIVE` stage to associate them with a cache behavior.

(structure)

A CloudFront function that is associated with a cache behavior in a CloudFront distribution.

FunctionARN -> (string)

The Amazon Resource Name (ARN) of the function.

EventType -> (string)

The event type of the function, either `viewer-request` or `viewer-response` . You cannot use origin-facing event types (`origin-request` and `origin-response` ) with a CloudFront function.

FieldLevelEncryptionId -> (string)

The value of `ID` for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for the default cache behavior.

RealtimeLogConfigArn -> (string)

The Amazon Resource Name (ARN) of the real-time log configuration that is attached to this cache behavior. For more information, see [Real-time logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html) in the *Amazon CloudFront Developer Guide* .

CachePolicyId -> (string)

The unique identifier of the cache policy that is attached to the default cache behavior. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

A `DefaultCacheBehavior` must include either a `CachePolicyId` or `ForwardedValues` . We recommend that you use a `CachePolicyId` .

OriginRequestPolicyId -> (string)

The unique identifier of the origin request policy that is attached to the default cache behavior. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) or [Using the managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html) in the *Amazon CloudFront Developer Guide* .

ResponseHeadersPolicyId -> (string)

The identifier for a response headers policy.

GrpcConfig -> (structure)

The gRPC configuration for your cache behavior.

Enabled -> (boolean)

Enables your CloudFront distribution to receive gRPC requests and to proxy them directly to your origins.

ForwardedValues -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field. For more information, see [Working with policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) in the *Amazon CloudFront Developer Guide* .

If you want to include values in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

If you want to send values to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) or [Using the managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html) in the *Amazon CloudFront Developer Guide* .

A `DefaultCacheBehavior` must include either a `CachePolicyId` or `ForwardedValues` . We recommend that you use a `CachePolicyId` .

A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString -> (boolean)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include query strings in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send query strings to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of `QueryString` and on the values that you specify for `QueryStringCacheKeys` , if any:

If you specify true for `QueryString` and you donât specify any values for `QueryStringCacheKeys` , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.

If you specify true for `QueryString` and you specify one or more values for `QueryStringCacheKeys` , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.

If you specify false for `QueryString` , CloudFront doesnât forward any query string parameters to the origin, and doesnât cache based on query string parameters.

For more information, see [Configuring CloudFront to Cache Based on Query String Parameters](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html) in the *Amazon CloudFront Developer Guide* .

Cookies -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see [How CloudFront Forwards, Caches, and Logs Cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html) in the *Amazon CloudFront Developer Guide* .

Forward -> (string)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send cookies to the origin but not include them in the cache key, use origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the `WhitelistedNames` complex type.

Amazon S3 doesnât process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the `Forward` element.

WhitelistedNames -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

Required if you specify `whitelist` for the value of `Forward` . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.

If you specify `all` or `none` for the value of `Forward` , omit `WhitelistedNames` . If you change the value of `Forward` from `whitelist` to `all` or `none` and you donât delete the `WhitelistedNames` element and its child elements, CloudFront deletes them automatically.

For the current limit on the number of cookie names that you can whitelist for each cache behavior, see [CloudFront Limits](https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront) in the *Amazon Web Services General Reference* .

Quantity -> (integer)

The number of cookie names in the `Items` list.

Items -> (list)

A list of cookie names.

(string)

Headers -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include headers in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send headers to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

A complex type that specifies the `Headers` , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.

For more information, see [Caching Content Based on Request Headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of header names in the `Items` list.

Items -> (list)

A list of HTTP header names.

(string)

QueryStringCacheKeys -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include query strings in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send query strings to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity -> (integer)

The number of `whitelisted` query string parameters for a cache behavior.

Items -> (list)

A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If `Quantity` is 0, you can omit `Items` .

(string)

MinTTL -> (long)

This field is deprecated. We recommend that you use the `MinTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

You must specify `0` for `MinTTL` if you configure CloudFront to forward all headers to your origin (under `Headers` , if you specify `1` for `Quantity` and `*` for `Name` ).

DefaultTTL -> (long)

This field is deprecated. We recommend that you use the `DefaultTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

MaxTTL -> (long)

This field is deprecated. We recommend that you use the `MaxTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

CacheBehaviors -> (structure)

A complex type that contains zero or more `CacheBehavior` elements.

Quantity -> (integer)

The number of cache behaviors for this distribution.

Items -> (list)

Optional: A complex type that contains cache behaviors for this distribution. If `Quantity` is `0` , you can omit `Items` .

(structure)

A complex type that describes how CloudFront processes requests.

You must create at least as many cache behaviors (including the default cache behavior) as you have origins if you want CloudFront to serve objects from all of the origins. Each cache behavior specifies the one origin from which you want CloudFront to get objects. If you have two origins and only the default cache behavior, the default cache behavior will cause CloudFront to get objects from one of the origins, but the other origin is never used.

For the current quota (formerly known as limit) on the number of cache behaviors that you can add to a distribution, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) in the *Amazon CloudFront Developer Guide* .

If you donât want to specify any cache behaviors, include only an empty `CacheBehaviors` element. Donât specify an empty individual `CacheBehavior` element, because this is invalid. For more information, see [CacheBehaviors](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CacheBehaviors.html) .

To delete all cache behaviors in an existing distribution, update the distribution configuration and include only an empty `CacheBehaviors` element.

To add, change, or remove one or more cache behaviors, update the distribution configuration and specify all of the cache behaviors that you want to include in the updated distribution.

For more information about cache behaviors, see [Cache Behavior Settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior) in the *Amazon CloudFront Developer Guide* .

PathPattern -> (string)

The pattern (for example, `images/*.jpg` ) that specifies which requests to apply the behavior to. When CloudFront receives a viewer request, the requested path is compared with path patterns in the order in which cache behaviors are listed in the distribution.

### Note

You can optionally include a slash (`/` ) at the beginning of the path pattern. For example, `/images/*.jpg` . CloudFront behavior is the same with or without the leading `/` .

The path pattern for the default cache behavior is `*` and cannot be changed. If the request for an object does not match the path pattern for any cache behaviors, CloudFront applies the behavior in the default cache behavior.

For more information, see [Path Pattern](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern) in the *Amazon CloudFront Developer Guide* .

TargetOriginId -> (string)

The value of `ID` for the origin that you want CloudFront to route requests to when they match this cache behavior.

TrustedSigners -> (structure)

### Warning

We recommend using `TrustedKeyGroups` instead of `TrustedSigners` .

A list of Amazon Web Services account IDs whose public keys CloudFront can use to validate signed URLs or signed cookies.

When a cache behavior contains trusted signers, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with the private key of a CloudFront key pair in the trusted signerâs Amazon Web Services account. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is `false` .

Quantity -> (integer)

The number of Amazon Web Services accounts in the list.

Items -> (list)

A list of Amazon Web Services account identifiers.

(string)

TrustedKeyGroups -> (structure)

A list of key groups that CloudFront can use to validate signed URLs or signed cookies.

When a cache behavior contains trusted key groups, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the key groups in the list have public keys that CloudFront can use to verify the signatures of signed URLs and signed cookies. If not, this field is `false` .

Quantity -> (integer)

The number of key groups in the list.

Items -> (list)

A list of key groups identifiers.

(string)

ViewerProtocolPolicy -> (string)

The protocol that viewers can use to access the files in the origin specified by `TargetOriginId` when a request matches the path pattern in `PathPattern` . You can specify the following options:

- `allow-all` : Viewers can use HTTP or HTTPS.
- `redirect-to-https` : If a viewer submits an HTTP request, CloudFront returns an HTTP status code of 301 (Moved Permanently) to the viewer along with the HTTPS URL. The viewer then resubmits the request using the new URL.
- `https-only` : If a viewer sends an HTTP request, CloudFront returns an HTTP status code of 403 (Forbidden).

For more information about requiring the HTTPS protocol, see [Requiring HTTPS Between Viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in the *Amazon CloudFront Developer Guide* .

### Note

The only way to guarantee that viewers retrieve an object that was fetched from the origin using HTTPS is never to use any other protocol to fetch the object. If you have recently changed from HTTP to HTTPS, we recommend that you clear your objectsâ cache because cached objects are protocol agnostic. That means that an edge location will return an object from the cache regardless of whether the current request protocol matches the protocol used previously. For more information, see [Managing Cache Expiration](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

AllowedMethods -> (structure)

A complex type that controls which HTTP methods CloudFront processes and forwards to your Amazon S3 bucket or your custom origin. There are three choices:

- CloudFront forwards only `GET` and `HEAD` requests.
- CloudFront forwards only `GET` , `HEAD` , and `OPTIONS` requests.
- CloudFront forwards `GET, HEAD, OPTIONS, PUT, PATCH, POST` , and `DELETE` requests.

If you pick the third choice, you may need to restrict access to your Amazon S3 bucket or to your custom origin so users canât perform operations that you donât want them to. For example, you might not want users to have permissions to delete objects from your origin.

Quantity -> (integer)

The number of HTTP methods that you want CloudFront to forward to your origin. Valid values are 2 (for `GET` and `HEAD` requests), 3 (for `GET` , `HEAD` , and `OPTIONS` requests) and 7 (for `GET, HEAD, OPTIONS, PUT, PATCH, POST` , and `DELETE` requests).

Items -> (list)

A complex type that contains the HTTP methods that you want CloudFront to process and forward to your origin.

(string)

CachedMethods -> (structure)

A complex type that controls whether CloudFront caches the response to requests using the specified HTTP methods. There are two choices:

- CloudFront caches responses to `GET` and `HEAD` requests.
- CloudFront caches responses to `GET` , `HEAD` , and `OPTIONS` requests.

If you pick the second choice for your Amazon S3 Origin, you may need to forward Access-Control-Request-Method, Access-Control-Request-Headers, and Origin headers for the responses to be cached correctly.

Quantity -> (integer)

The number of HTTP methods for which you want CloudFront to cache responses. Valid values are `2` (for caching responses to `GET` and `HEAD` requests) and `3` (for caching responses to `GET` , `HEAD` , and `OPTIONS` requests).

Items -> (list)

A complex type that contains the HTTP methods that you want CloudFront to cache responses to. Valid values for `CachedMethods` include `GET` , `HEAD` , and `OPTIONS` , depending on which caching option you choose. For more information, see the preceding section.

(string)

SmoothStreaming -> (boolean)

Indicates whether you want to distribute media files in the Microsoft Smooth Streaming format using the origin that is associated with this cache behavior. If so, specify `true` ; if not, specify `false` . If you specify `true` for `SmoothStreaming` , you can still distribute other content using this cache behavior if the content matches the value of `PathPattern` .

Compress -> (boolean)

Whether you want CloudFront to automatically compress certain files for this cache behavior. If so, specify true; if not, specify false. For more information, see [Serving Compressed Files](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html) in the *Amazon CloudFront Developer Guide* .

LambdaFunctionAssociations -> (structure)

A complex type that contains zero or more [Lambda@Edge](mailto:Lambda%40Edge) function associations for a cache behavior.

Quantity -> (integer)

The number of [Lambda@Edge](mailto:Lambda%40Edge) function associations for this cache behavior.

Items -> (list)

**Optional** : A complex type that contains `LambdaFunctionAssociation` items for this cache behavior. If `Quantity` is `0` , you can omit `Items` .

(structure)

A complex type that contains a [Lambda@Edge](mailto:Lambda%40Edge) function association.

LambdaFunctionARN -> (string)

The ARN of the [Lambda@Edge](mailto:Lambda%40Edge) function. You must specify the ARN of a function version; you canât specify an alias or $LATEST.

EventType -> (string)

Specifies the event type that triggers a [Lambda@Edge](mailto:Lambda%40Edge) function invocation. You can specify the following values:

- `viewer-request` : The function executes when CloudFront receives a request from a viewer and before it checks to see whether the requested object is in the edge cache.
- `origin-request` : The function executes only when CloudFront sends a request to your origin. When the requested object is in the edge cache, the function doesnât execute.
- `origin-response` : The function executes after CloudFront receives a response from the origin and before it caches the object in the response. When the requested object is in the edge cache, the function doesnât execute.
- `viewer-response` : The function executes before CloudFront returns the requested object to the viewer. The function executes regardless of whether the object was already in the edge cache. If the origin returns an HTTP status code other than HTTP 200 (OK), the function doesnât execute.

IncludeBody -> (boolean)

A flag that allows a [Lambda@Edge](mailto:Lambda%40Edge) function to have read access to the body content. For more information, see [Accessing the Request Body by Choosing the Include Body Option](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-include-body-access.html) in the Amazon CloudFront Developer Guide.

FunctionAssociations -> (structure)

A list of CloudFront functions that are associated with this cache behavior. CloudFront functions must be published to the `LIVE` stage to associate them with a cache behavior.

Quantity -> (integer)

The number of CloudFront functions in the list.

Items -> (list)

The CloudFront functions that are associated with a cache behavior in a CloudFront distribution. Your functions must be published to the `LIVE` stage to associate them with a cache behavior.

(structure)

A CloudFront function that is associated with a cache behavior in a CloudFront distribution.

FunctionARN -> (string)

The Amazon Resource Name (ARN) of the function.

EventType -> (string)

The event type of the function, either `viewer-request` or `viewer-response` . You cannot use origin-facing event types (`origin-request` and `origin-response` ) with a CloudFront function.

FieldLevelEncryptionId -> (string)

The value of `ID` for the field-level encryption configuration that you want CloudFront to use for encrypting specific fields of data for this cache behavior.

RealtimeLogConfigArn -> (string)

The Amazon Resource Name (ARN) of the real-time log configuration that is attached to this cache behavior. For more information, see [Real-time logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/real-time-logs.html) in the *Amazon CloudFront Developer Guide* .

CachePolicyId -> (string)

The unique identifier of the cache policy that is attached to this cache behavior. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

A `CacheBehavior` must include either a `CachePolicyId` or `ForwardedValues` . We recommend that you use a `CachePolicyId` .

OriginRequestPolicyId -> (string)

The unique identifier of the origin request policy that is attached to this cache behavior. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) or [Using the managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html) in the *Amazon CloudFront Developer Guide* .

ResponseHeadersPolicyId -> (string)

The identifier for a response headers policy.

GrpcConfig -> (structure)

The gRPC configuration for your cache behavior.

Enabled -> (boolean)

Enables your CloudFront distribution to receive gRPC requests and to proxy them directly to your origins.

ForwardedValues -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field. For more information, see [Working with policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/working-with-policies.html) in the *Amazon CloudFront Developer Guide* .

If you want to include values in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

If you want to send values to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) or [Using the managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html) in the *Amazon CloudFront Developer Guide* .

A `CacheBehavior` must include either a `CachePolicyId` or `ForwardedValues` . We recommend that you use a `CachePolicyId` .

A complex type that specifies how CloudFront handles query strings, cookies, and HTTP headers.

QueryString -> (boolean)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include query strings in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send query strings to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

Indicates whether you want CloudFront to forward query strings to the origin that is associated with this cache behavior and cache based on the query string parameters. CloudFront behavior depends on the value of `QueryString` and on the values that you specify for `QueryStringCacheKeys` , if any:

If you specify true for `QueryString` and you donât specify any values for `QueryStringCacheKeys` , CloudFront forwards all query string parameters to the origin and caches based on all query string parameters. Depending on how many query string parameters and values you have, this can adversely affect performance because CloudFront must forward more requests to the origin.

If you specify true for `QueryString` and you specify one or more values for `QueryStringCacheKeys` , CloudFront forwards all query string parameters to the origin, but it only caches based on the query string parameters that you specify.

If you specify false for `QueryString` , CloudFront doesnât forward any query string parameters to the origin, and doesnât cache based on query string parameters.

For more information, see [Configuring CloudFront to Cache Based on Query String Parameters](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html) in the *Amazon CloudFront Developer Guide* .

Cookies -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

A complex type that specifies whether you want CloudFront to forward cookies to the origin and, if so, which ones. For more information about forwarding cookies to the origin, see [How CloudFront Forwards, Caches, and Logs Cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Cookies.html) in the *Amazon CloudFront Developer Guide* .

Forward -> (string)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send cookies to the origin but not include them in the cache key, use origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

Specifies which cookies to forward to the origin for this cache behavior: all, none, or the list of cookies specified in the `WhitelistedNames` complex type.

Amazon S3 doesnât process cookies. When the cache behavior is forwarding requests to an Amazon S3 origin, specify none for the `Forward` element.

WhitelistedNames -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include cookies in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send cookies to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

Required if you specify `whitelist` for the value of `Forward` . A complex type that specifies how many different cookies you want CloudFront to forward to the origin for this cache behavior and, if you want to forward selected cookies, the names of those cookies.

If you specify `all` or `none` for the value of `Forward` , omit `WhitelistedNames` . If you change the value of `Forward` from `whitelist` to `all` or `none` and you donât delete the `WhitelistedNames` element and its child elements, CloudFront deletes them automatically.

For the current limit on the number of cookie names that you can whitelist for each cache behavior, see [CloudFront Limits](https://docs.aws.amazon.com/general/latest/gr/xrefaws_service_limits.html#limits_cloudfront) in the *Amazon Web Services General Reference* .

Quantity -> (integer)

The number of cookie names in the `Items` list.

Items -> (list)

A list of cookie names.

(string)

Headers -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include headers in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send headers to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

A complex type that specifies the `Headers` , if any, that you want CloudFront to forward to the origin for this cache behavior (whitelisted headers). For the headers that you specify, CloudFront also caches separate versions of a specified object that is based on the header values in viewer requests.

For more information, see [Caching Content Based on Request Headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/header-caching.html) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of header names in the `Items` list.

Items -> (list)

A list of HTTP header names.

(string)

QueryStringCacheKeys -> (structure)

This field is deprecated. We recommend that you use a cache policy or an origin request policy instead of this field.

If you want to include query strings in the cache key, use a cache policy. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) in the *Amazon CloudFront Developer Guide* .

If you want to send query strings to the origin but not include them in the cache key, use an origin request policy. For more information, see [Creating origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-origin-requests.html#origin-request-create-origin-request-policy) in the *Amazon CloudFront Developer Guide* .

A complex type that contains information about the query string parameters that you want CloudFront to use for caching for this cache behavior.

Quantity -> (integer)

The number of `whitelisted` query string parameters for a cache behavior.

Items -> (list)

A list that contains the query string parameters that you want CloudFront to use as a basis for caching for a cache behavior. If `Quantity` is 0, you can omit `Items` .

(string)

MinTTL -> (long)

This field is deprecated. We recommend that you use the `MinTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

The minimum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

You must specify `0` for `MinTTL` if you configure CloudFront to forward all headers to your origin (under `Headers` , if you specify `1` for `Quantity` and `*` for `Name` ).

DefaultTTL -> (long)

This field is deprecated. We recommend that you use the `DefaultTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

The default amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin does not add HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

MaxTTL -> (long)

This field is deprecated. We recommend that you use the `MaxTTL` field in a cache policy instead of this field. For more information, see [Creating cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/controlling-the-cache-key.html#cache-key-create-cache-policy) or [Using the managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) in the *Amazon CloudFront Developer Guide* .

The maximum amount of time that you want objects to stay in CloudFront caches before CloudFront forwards another request to your origin to determine whether the object has been updated. The value that you specify applies only when your origin adds HTTP headers such as `Cache-Control max-age` , `Cache-Control s-maxage` , and `Expires` to objects. For more information, see [Managing How Long Content Stays in an Edge Cache (Expiration)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) in the *Amazon CloudFront Developer Guide* .

CustomErrorResponses -> (structure)

A complex type that controls the following:

- Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
- How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see [Customizing Error Responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html) in the *Amazon CloudFront Developer Guide* .

Quantity -> (integer)

The number of HTTP status codes for which you want to specify a custom error page and/or a caching duration. If `Quantity` is `0` , you can omit `Items` .

Items -> (list)

A complex type that contains a `CustomErrorResponse` element for each HTTP status code for which you want to specify a custom error page and/or a caching duration.

(structure)

A complex type that controls:

- Whether CloudFront replaces HTTP status codes in the 4xx and 5xx range with custom error messages before returning the response to the viewer.
- How long CloudFront caches HTTP status codes in the 4xx and 5xx range.

For more information about custom error pages, see [Customizing Error Responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html) in the *Amazon CloudFront Developer Guide* .

ErrorCode -> (integer)

The HTTP status code for which you want to specify a custom error page and/or a caching duration.

ResponsePagePath -> (string)

The path to the custom error page that you want CloudFront to return to a viewer when your origin returns the HTTP status code specified by `ErrorCode` , for example, `/4xx-errors/403-forbidden.html` . If you want to store your objects and your custom error pages in different locations, your distribution must include a cache behavior for which the following is true:

- The value of `PathPattern` matches the path to your custom error messages. For example, suppose you saved custom error pages for 4xx errors in an Amazon S3 bucket in a directory named `/4xx-errors` . Your distribution must include a cache behavior for which the path pattern routes requests for your custom error pages to that location, for example, `/4xx-errors/*` .
- The value of `TargetOriginId` specifies the value of the `ID` element for the origin that contains your custom error pages.

If you specify a value for `ResponsePagePath` , you must also specify a value for `ResponseCode` .

We recommend that you store custom error pages in an Amazon S3 bucket. If you store custom error pages on an HTTP server and the server starts to return 5xx errors, CloudFront canât get the files that you want to return to viewers because the origin server is unavailable.

ResponseCode -> (string)

The HTTP status code that you want CloudFront to return to the viewer along with the custom error page. There are a variety of reasons that you might want CloudFront to return a status code different from the status code that your origin returned to CloudFront, for example:

- Some Internet devices (some firewalls and corporate proxies, for example) intercept HTTP 4xx and 5xx and prevent the response from being returned to the viewer. If you substitute `200` , the response typically wonât be intercepted.
- If you donât care about distinguishing among different client errors or server errors, you can specify `400` or `500` as the `ResponseCode` for all 4xx or 5xx errors.
- You might want to return a `200` status code (OK) and static website so your customers donât know that your website is down.

If you specify a value for `ResponseCode` , you must also specify a value for `ResponsePagePath` .

ErrorCachingMinTTL -> (long)

The minimum amount of time, in seconds, that you want CloudFront to cache the HTTP status code specified in `ErrorCode` . When this time period has elapsed, CloudFront queries your origin to see whether the problem that caused the error has been resolved and the requested object is now available.

For more information, see [Customizing Error Responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html) in the *Amazon CloudFront Developer Guide* .

Comment -> (string)

A comment to describe the distribution. The comment cannot be longer than 128 characters.

Logging -> (structure)

A complex type that controls whether access logs are written for the distribution.

For more information about logging, see [Access Logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you donât want to enable logging when you create a distribution or if you want to disable logging for an existing distribution, specify `false` for `Enabled` , and specify empty `Bucket` and `Prefix` elements. If you specify `false` for `Enabled` but you specify values for `Bucket` and `prefix` , the values are automatically deleted.

IncludeCookies -> (boolean)

Specifies whether you want CloudFront to include cookies in access logs, specify `true` for `IncludeCookies` . If you choose to include cookies in logs, CloudFront logs all cookies regardless of how you configure the cache behaviors for this distribution. If you donât want to include cookies when you create a distribution or if you want to disable include cookies for an existing distribution, specify `false` for `IncludeCookies` .

Bucket -> (string)

The Amazon S3 bucket to store the access logs in, for example, `amzn-s3-demo-bucket.s3.amazonaws.com` .

Prefix -> (string)

An optional string that you want CloudFront to prefix to the access log `filenames` for this distribution, for example, `myprefix/` . If you want to enable logging, but you donât want to specify a prefix, you still must include an empty `Prefix` element in the `Logging` element.

PriceClass -> (string)

The price class that corresponds with the maximum price that you want to pay for CloudFront service. If you specify `PriceClass_All` , CloudFront responds to requests for your objects from all CloudFront edge locations.

If you specify a price class other than `PriceClass_All` , CloudFront serves your objects from the CloudFront edge location that has the lowest latency among the edge locations in your price class. Viewers who are in or near regions that are excluded from your specified price class may encounter slower performance.

For more information about price classes, see [Choosing the Price Class for a CloudFront Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html) in the *Amazon CloudFront Developer Guide* . For information about CloudFront pricing, including how price classes (such as Price Class 100) map to CloudFront regions, see [Amazon CloudFront Pricing](http://aws.amazon.com/cloudfront/pricing/) .

Enabled -> (boolean)

From this field, you can enable or disable the selected distribution.

ViewerCertificate -> (structure)

A complex type that determines the distributionâs SSL/TLS configuration for communicating with viewers.

CloudFrontDefaultCertificate -> (boolean)

If the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net` , set this field to `true` .

If the distribution uses `Aliases` (alternate domain names or CNAMEs), set this field to `false` and specify values for the following fields:

- `ACMCertificateArn` or `IAMCertificateId` (specify a value for one, not both)
- `MinimumProtocolVersion`
- `SSLSupportMethod`

IAMCertificateId -> (string)

If the distribution uses `Aliases` (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in [Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html) , provide the ID of the IAM certificate.

If you specify an IAM certificate ID, you must also specify values for `MinimumProtocolVersion` and `SSLSupportMethod` .

ACMCertificateArn -> (string)

If the distribution uses `Aliases` (alternate domain names or CNAMEs) and the SSL/TLS certificate is stored in [Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) , provide the Amazon Resource Name (ARN) of the ACM certificate. CloudFront only supports ACM certificates in the US East (N. Virginia) Region (`us-east-1` ).

If you specify an ACM certificate ARN, you must also specify values for `MinimumProtocolVersion` and `SSLSupportMethod` .

SSLSupportMethod -> (string)

If the distribution uses `Aliases` (alternate domain names or CNAMEs), specify which viewers the distribution accepts HTTPS connections from.

- `sni-only` â The distribution accepts HTTPS connections from only viewers that support [server name indication (SNI)](https://en.wikipedia.org/wiki/Server_Name_Indication) . This is recommended. Most browsers and clients support SNI.
- `vip` â The distribution accepts HTTPS connections from all viewers including those that donât support SNI. This is not recommended, and results in additional monthly charges from CloudFront.
- `static-ip` - Do not specify this value unless your distribution has been enabled for this feature by the CloudFront team. If you have a use case that requires static IP addresses for a distribution, contact CloudFront through the [Amazon Web ServicesSupport Center](https://console.aws.amazon.com/support/home) .

If the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net` , donât set a value for this field.

MinimumProtocolVersion -> (string)

If the distribution uses `Aliases` (alternate domain names or CNAMEs), specify the security policy that you want CloudFront to use for HTTPS connections with viewers. The security policy determines two settings:

- The minimum SSL/TLS protocol that CloudFront can use to communicate with viewers.
- The ciphers that CloudFront can use to encrypt the content that it returns to viewers.

For more information, see [Security Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValues-security-policy) and [Supported Protocols and Ciphers Between Viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html#secure-connections-supported-ciphers) in the *Amazon CloudFront Developer Guide* .

### Note

On the CloudFront console, this setting is called **Security Policy** .

When youâre using SNI only (you set `SSLSupportMethod` to `sni-only` ), you must specify `TLSv1` or higher.

If the distribution uses the CloudFront domain name such as `d111111abcdef8.cloudfront.net` (you set `CloudFrontDefaultCertificate` to `true` ), CloudFront automatically sets the security policy to `TLSv1` regardless of the value that you set here.

Certificate -> (string)

This field is deprecated. Use one of the following fields instead:

- `ACMCertificateArn`
- `IAMCertificateId`
- `CloudFrontDefaultCertificate`

CertificateSource -> (string)

This field is deprecated. Use one of the following fields instead:

- `ACMCertificateArn`
- `IAMCertificateId`
- `CloudFrontDefaultCertificate`

Restrictions -> (structure)

A complex type that identifies ways in which you want to restrict distribution of your content.

GeoRestriction -> (structure)

A complex type that controls the countries in which your content is distributed. CloudFront determines the location of your users using `MaxMind` GeoIP databases.

RestrictionType -> (string)

The method that you want to use to restrict distribution of your content by country:

- `none` : No geo restriction is enabled, meaning access to content is not restricted by client geo location.
- `blacklist` : The `Location` elements specify the countries in which you donât want CloudFront to distribute your content.
- `whitelist` : The `Location` elements specify the countries in which you want CloudFront to distribute your content.

Quantity -> (integer)

When geo restriction is `enabled` , this is the number of countries in your `whitelist` or `blacklist` . Otherwise, when it is not enabled, `Quantity` is `0` , and you can omit `Items` .

Items -> (list)

A complex type that contains a `Location` element for each country in which you want CloudFront either to distribute your content (`whitelist` ) or not distribute your content (`blacklist` ).

The `Location` element is a two-letter, uppercase country code for a country that you want to include in your `blacklist` or `whitelist` . Include one `Location` element for each country.

CloudFront and `MaxMind` both use `ISO 3166` country codes. For the current list of countries and the corresponding codes, see `ISO 3166-1-alpha-2` code on the *International Organization for Standardization* website. You can also refer to the country list on the CloudFront console, which includes both country names and codes.

(string)

WebACLId -> (string)

A unique identifier that specifies the WAF web ACL, if any, to associate with this distribution. To specify a web ACL created using the latest version of WAF, use the ACL ARN, for example `arn:aws:wafv2:us-east-1:123456789012:global/webacl/ExampleWebACL/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` . To specify a web ACL created using WAF Classic, use the ACL ID, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` .

WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to CloudFront, and lets you control access to your content. Based on conditions that you specify, such as the IP addresses that requests originate from or the values of query strings, CloudFront responds to requests either with the requested content or with an HTTP 403 status code (Forbidden). You can also configure CloudFront to return a custom error page when a request is blocked. For more information about WAF, see the [WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) .

HttpVersion -> (string)

(Optional) Specify the HTTP version(s) that you want viewers to use to communicate with CloudFront. The default value for new web distributions is `http2` . Viewers that donât support HTTP/2 automatically use an earlier HTTP version.

For viewers and CloudFront to use HTTP/2, viewers must support TLSv1.2 or later, and must support Server Name Indication (SNI).

For viewers and CloudFront to use HTTP/3, viewers must support TLSv1.3 and Server Name Indication (SNI). CloudFront supports HTTP/3 connection migration to allow the viewer to switch networks without losing connection. For more information about connection migration, see [Connection Migration](https://www.rfc-editor.org/rfc/rfc9000.html#name-connection-migration) at RFC 9000. For more information about supported TLSv1.3 ciphers, see [Supported protocols and ciphers between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html) .

IsIPV6Enabled -> (boolean)

If you want CloudFront to respond to IPv6 DNS requests with an IPv6 address for your distribution, specify `true` . If you specify `false` , CloudFront responds to IPv6 DNS requests with the DNS response code `NOERROR` and with no IP addresses. This allows viewers to submit a second request, for an IPv4 address for your distribution.

In general, you should enable IPv6 if you have users on IPv6 networks who want to access your content. However, if youâre using signed URLs or signed cookies to restrict access to your content, and if youâre using a custom policy that includes the `IpAddress` parameter to restrict the IP addresses that can access your content, donât enable IPv6. If you want to restrict access to some content by IP address and not restrict access to other content (or restrict access but not by IP address), you can create two distributions. For more information, see [Creating a Signed URL Using a Custom Policy](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-creating-signed-url-custom-policy.html) in the *Amazon CloudFront Developer Guide* .

If youâre using an Route 53 Amazon Web Services Integration alias resource record set to route traffic to your CloudFront distribution, you need to create a second alias resource record set when both of the following are true:

- You enable IPv6 for the distribution
- Youâre using alternate domain names in the URLs for your objects

For more information, see [Routing Traffic to an Amazon CloudFront Web Distribution by Using Your Domain Name](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html) in the *Route 53 Amazon Web Services Integration Developer Guide* .

If you created a CNAME resource record set, either with Route 53 Amazon Web Services Integration or with another DNS service, you donât need to make any changes. A CNAME record will route traffic to your distribution regardless of the IP address format of the viewer request.

ContinuousDeploymentPolicyId -> (string)

The identifier of a continuous deployment policy. For more information, see `CreateContinuousDeploymentPolicy` .

Staging -> (boolean)

A Boolean that indicates whether this is a staging distribution. When this value is `true` , this is a staging distribution. When this value is `false` , this is not a staging distribution.

AnycastIpListId -> (string)

ID of the Anycast static IP list that is associated with the distribution.

TenantConfig -> (structure)

A distribution tenant configuration.

ParameterDefinitions -> (list)

The parameters that you specify for a distribution tenant.

(structure)

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

Name -> (string)

The name of the parameter.

Definition -> (structure)

The value that you assigned to the parameter.

StringSchema -> (structure)

An object that contains information about the string schema.

Comment -> (string)

A comment to describe the parameter.

DefaultValue -> (string)

The default value of the parameter.

Required -> (boolean)

Whether the defined parameter is required.

ConnectionMode -> (string)

The connection mode to filter distributions by.

AliasICPRecordals -> (list)

Amazon Web Services services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that theyâve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions.

For more information about ICP recordals, see [Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with Amazon Web Services services in China* .

(structure)

Amazon Web Services services in China customers must file for an Internet Content Provider (ICP) recordal if they want to serve content publicly on an alternate domain name, also known as a CNAME, that theyâve added to CloudFront. AliasICPRecordal provides the ICP recordal status for CNAMEs associated with distributions. The status is returned in the CloudFront response; you canât configure it yourself.

For more information about ICP recordals, see [Signup, Accounts, and Credentials](https://docs.amazonaws.cn/en_us/aws/latest/userguide/accounts-and-credentials.html) in *Getting Started with Amazon Web Services services in China* .

CNAME -> (string)

A domain name associated with a distribution.

ICPRecordalStatus -> (string)

The Internet Content Provider (ICP) recordal status for a CNAME. The ICPRecordalStatus is set to APPROVED for all CNAMEs (aliases) in Amazon Web Services Regions outside of China.

The status values returned are the following:

- **APPROVED** indicates that the associated CNAME has a valid ICP recordal number. Multiple CNAMEs can be associated with a distribution, and CNAMEs can correspond to different ICP recordals. To be marked as APPROVED, that is, valid to use with the China Regions, a CNAME must have one ICP recordal number associated with it.
- **SUSPENDED** indicates that the associated CNAME does not have a valid ICP recordal number.
- **PENDING** indicates that CloudFront canât determine the ICP recordal status of the CNAME associated with the distribution because there was an error in trying to determine the status. You can try again to see if the error is resolved in which case CloudFront returns an APPROVED or SUSPENDED status.

ETag -> (string)

The current version of the distributionâs information. For example: `E2QWRUHAPOMQZL` .