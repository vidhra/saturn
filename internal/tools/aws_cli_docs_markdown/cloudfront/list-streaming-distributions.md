# list-streaming-distributionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-streaming-distributions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-streaming-distributions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# list-streaming-distributions

## Description

List streaming distributions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/ListStreamingDistributions)

`list-streaming-distributions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `StreamingDistributionList.Items`

## Synopsis

```
list-streaming-distributions
[--max-items <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--max-items` (string)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (string)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

StreamingDistributionList -> (structure)

The `StreamingDistributionList` type.

Marker -> (string)

The value you provided for the `Marker` request parameter.

NextMarker -> (string)

If `IsTruncated` is `true` , this element is present and contains the value you can use for the `Marker` request parameter to continue listing your RTMP distributions where they left off.

MaxItems -> (integer)

The value you provided for the `MaxItems` request parameter.

IsTruncated -> (boolean)

A flag that indicates whether more streaming distributions remain to be listed. If your results were truncated, you can make a follow-up pagination request using the `Marker` request parameter to retrieve more distributions in the list.

Quantity -> (integer)

The number of streaming distributions that were created by the current Amazon Web Services account.

Items -> (list)

A complex type that contains one `StreamingDistributionSummary` element for each distribution that was created by the current Amazon Web Services account.

(structure)

A summary of the information for a CloudFront streaming distribution.

Id -> (string)

The identifier for the distribution, for example, `EDFDVBD632BHDS5` .

ARN -> (string)

The ARN (Amazon Resource Name) for the streaming distribution. For example: `arn:aws:cloudfront::123456789012:streaming-distribution/EDFDVBD632BHDS5` , where `123456789012` is your Amazon Web Services account ID.

Status -> (string)

Indicates the current status of the distribution. When the status is `Deployed` , the distributionâs information is fully propagated throughout the Amazon CloudFront system.

LastModifiedTime -> (timestamp)

The date and time the distribution was last modified.

DomainName -> (string)

The domain name corresponding to the distribution, for example, `d111111abcdef8.cloudfront.net` .

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

TrustedSigners -> (structure)

A complex type that specifies the Amazon Web Services accounts, if any, that you want to allow to create signed URLs for private content. If you want to require signed URLs in requests for objects in the target origin that match the `PathPattern` for this cache behavior, specify `true` for `Enabled` , and specify the applicable values for `Quantity` and `Items` .If you donât want to require signed URLs in requests for objects that match `PathPattern` , specify `false` for `Enabled` and `0` for `Quantity` . Omit `Items` . To add, change, or remove one or more trusted signers, change `Enabled` to `true` (if itâs currently `false` ), change `Quantity` as applicable, and specify all of the trusted signers that you want to include in the updated distribution.

For more information, see [Serving Private Content through CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide* .

Enabled -> (boolean)

This field is `true` if any of the Amazon Web Services accounts in the list are configured as trusted signers. If not, this field is `false` .

Quantity -> (integer)

The number of Amazon Web Services accounts in the list.

Items -> (list)

A list of Amazon Web Services account identifiers.

(string)

Comment -> (string)

The comment originally specified when this distribution was created.

PriceClass -> (string)

A complex type that contains information about price class for this streaming distribution.

Enabled -> (boolean)

Whether the distribution is enabled to accept end user requests for content.