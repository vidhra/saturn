# create-streaming-distributionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-streaming-distribution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-streaming-distribution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# create-streaming-distribution

## Description

This API is deprecated. Amazon CloudFront is deprecating real-time messaging protocol (RTMP) distributions on December 31, 2020. For more information, [read the announcement](http://forums.aws.amazon.com/ann.jspa?annID=7356) on the Amazon CloudFront discussion forum.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/CreateStreamingDistribution)

## Synopsis

```
create-streaming-distribution
--streaming-distribution-config <value>
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

`--streaming-distribution-config` (structure)

The streaming distributionâs configuration information.

CallerReference -> (string)

A unique value (for example, a date-time stamp) that ensures that the request canât be replayed.

If the value of `CallerReference` is new (regardless of the content of the `StreamingDistributionConfig` object), CloudFront creates a new distribution.

If `CallerReference` is a value that you already sent in a previous request to create a distribution, CloudFront returns a `DistributionAlreadyExists` error.

S3Origin -> (structure)

A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName -> (string)

The DNS name of the Amazon S3 origin.

OriginAccessIdentity -> (string)

The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.

If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty `OriginAccessIdentity` element.

To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty `OriginAccessIdentity` element.

To replace the origin access identity, update the distribution configuration and specify the new origin access identity.

For more information, see [Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide* .

Aliases -> (structure)

A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity -> (integer)

The number of CNAME aliases, if any, that you want to associate with this distribution.

Items -> (list)

A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string)

Comment -> (string)

Any comments you want to include about the streaming distribution.

Logging -> (structure)

A complex type that controls whether access logs are written for the streaming distribution.

Enabled -> (boolean)

Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you donât want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify `false` for `Enabled` , and specify `empty Bucket` and `Prefix` elements. If you specify `false` for `Enabled` but you specify values for `Bucket` and `Prefix` , the values are automatically deleted.

Bucket -> (string)

The Amazon S3 bucket to store the access logs in, for example, `amzn-s3-demo-bucket.s3.amazonaws.com` .

Prefix -> (string)

An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, `myprefix/` . If you want to enable logging, but you donât want to specify a prefix, you still must include an empty `Prefix` element in the `Logging` element.

TrustedSigners -> (structure)

A complex type that specifies any Amazon Web Services accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is `false` .

Quantity -> (integer)

The number of Amazon Web Services accounts in the list.

Items -> (list)

A list of Amazon Web Services account identifiers.

(string)

PriceClass -> (string)

A complex type that contains information about price class for this streaming distribution.

Enabled -> (boolean)

Whether the streaming distribution is enabled to accept user requests for content.

Shorthand Syntax:

```
CallerReference=string,S3Origin={DomainName=string,OriginAccessIdentity=string},Aliases={Quantity=integer,Items=[string,string]},Comment=string,Logging={Enabled=boolean,Bucket=string,Prefix=string},TrustedSigners={Enabled=boolean,Quantity=integer,Items=[string,string]},PriceClass=string,Enabled=boolean
```

JSON Syntax:

```
{
  "CallerReference": "string",
  "S3Origin": {
    "DomainName": "string",
    "OriginAccessIdentity": "string"
  },
  "Aliases": {
    "Quantity": integer,
    "Items": ["string", ...]
  },
  "Comment": "string",
  "Logging": {
    "Enabled": true|false,
    "Bucket": "string",
    "Prefix": "string"
  },
  "TrustedSigners": {
    "Enabled": true|false,
    "Quantity": integer,
    "Items": ["string", ...]
  },
  "PriceClass": "PriceClass_100"|"PriceClass_200"|"PriceClass_All"|"None",
  "Enabled": true|false
}
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

## Output

StreamingDistribution -> (structure)

The streaming distributionâs information.

Id -> (string)

The identifier for the RTMP distribution. For example: `EGTXBD79EXAMPLE` .

ARN -> (string)

The ARN (Amazon Resource Name) for the distribution. For example: `arn:aws:cloudfront::123456789012:distribution/EDFDVBD632BHDS5` , where `123456789012` is your Amazon Web Services account ID.

Status -> (string)

The current status of the RTMP distribution. When the status is `Deployed` , the distributionâs information is propagated to all CloudFront edge locations.

LastModifiedTime -> (timestamp)

The date and time that the distribution was last modified.

DomainName -> (string)

The domain name that corresponds to the streaming distribution, for example, `s5c39gqb8ow64r.cloudfront.net` .

ActiveTrustedSigners -> (structure)

A complex type that lists the Amazon Web Services accounts, if any, that you included in the `TrustedSigners` complex type for this distribution. These are the accounts that you want to allow to create signed URLs for private content.

The `Signer` complex type lists the Amazon Web Services account number of the trusted signer or `self` if the signer is the Amazon Web Services account that created the distribution. The `Signer` element also includes the IDs of any active CloudFront key pairs that are associated with the trusted signerâs Amazon Web Services account. If no `KeyPairId` element appears for a `Signer` , that signer canât create signed URLs.

For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

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

StreamingDistributionConfig -> (structure)

The current configuration information for the RTMP distribution.

CallerReference -> (string)

A unique value (for example, a date-time stamp) that ensures that the request canât be replayed.

If the value of `CallerReference` is new (regardless of the content of the `StreamingDistributionConfig` object), CloudFront creates a new distribution.

If `CallerReference` is a value that you already sent in a previous request to create a distribution, CloudFront returns a `DistributionAlreadyExists` error.

S3Origin -> (structure)

A complex type that contains information about the Amazon S3 bucket from which you want CloudFront to get your media files for distribution.

DomainName -> (string)

The DNS name of the Amazon S3 origin.

OriginAccessIdentity -> (string)

The CloudFront origin access identity to associate with the distribution. Use an origin access identity to configure the distribution so that end users can only access objects in an Amazon S3 bucket through CloudFront.

If you want end users to be able to access objects using either the CloudFront URL or the Amazon S3 URL, specify an empty `OriginAccessIdentity` element.

To delete the origin access identity from an existing distribution, update the distribution configuration and include an empty `OriginAccessIdentity` element.

To replace the origin access identity, update the distribution configuration and specify the new origin access identity.

For more information, see [Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide* .

Aliases -> (structure)

A complex type that contains information about CNAMEs (alternate domain names), if any, for this streaming distribution.

Quantity -> (integer)

The number of CNAME aliases, if any, that you want to associate with this distribution.

Items -> (list)

A complex type that contains the CNAME aliases, if any, that you want to associate with this distribution.

(string)

Comment -> (string)

Any comments you want to include about the streaming distribution.

Logging -> (structure)

A complex type that controls whether access logs are written for the streaming distribution.

Enabled -> (boolean)

Specifies whether you want CloudFront to save access logs to an Amazon S3 bucket. If you donât want to enable logging when you create a streaming distribution or if you want to disable logging for an existing streaming distribution, specify `false` for `Enabled` , and specify `empty Bucket` and `Prefix` elements. If you specify `false` for `Enabled` but you specify values for `Bucket` and `Prefix` , the values are automatically deleted.

Bucket -> (string)

The Amazon S3 bucket to store the access logs in, for example, `amzn-s3-demo-bucket.s3.amazonaws.com` .

Prefix -> (string)

An optional string that you want CloudFront to prefix to the access log filenames for this streaming distribution, for example, `myprefix/` . If you want to enable logging, but you donât want to specify a prefix, you still must include an empty `Prefix` element in the `Logging` element.

TrustedSigners -> (structure)

A complex type that specifies any Amazon Web Services accounts that you want to permit to create signed URLs for private content. If you want the distribution to use signed URLs, include this element; if you want the distribution to use public URLs, remove this element. For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is `false` .

Quantity -> (integer)

The number of Amazon Web Services accounts in the list.

Items -> (list)

A list of Amazon Web Services account identifiers.

(string)

PriceClass -> (string)

A complex type that contains information about price class for this streaming distribution.

Enabled -> (boolean)

Whether the streaming distribution is enabled to accept user requests for content.

Location -> (string)

The fully qualified URI of the new streaming distribution resource just created.

ETag -> (string)

The current version of the streaming distribution created.