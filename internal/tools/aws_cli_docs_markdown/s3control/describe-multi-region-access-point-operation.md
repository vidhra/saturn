# describe-multi-region-access-point-operationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-multi-region-access-point-operation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-multi-region-access-point-operation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html#cli-aws-s3control) ]

# describe-multi-region-access-point-operation

## Description

### Note

This operation is not supported by directory buckets.

Retrieves the status of an asynchronous request to manage a Multi-Region Access Point. For more information about managing Multi-Region Access Points and how asynchronous requests work, see [Using Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MrapOperations.html) in the *Amazon S3 User Guide* .

The following actions are related to `GetMultiRegionAccessPoint` :

- [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html)
- [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html)
- [GetMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html)
- [ListMultiRegionAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation)

## Synopsis

```
describe-multi-region-access-point-operation
--account-id <value>
--request-token-arn <value>
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

`--account-id` (string)

The Amazon Web Services account ID for the owner of the Multi-Region Access Point.

`--request-token-arn` (string)

The request token associated with the request you want to know about. This request token is returned as part of the response when you make an asynchronous request. You provide this token to query about the status of the asynchronous action.

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

AsyncOperation -> (structure)

A container element containing the details of the asynchronous operation.

CreationTime -> (timestamp)

The time that the request was sent to the service.

Operation -> (string)

The specific operation for the asynchronous request.

RequestTokenARN -> (string)

The request token associated with the request.

RequestParameters -> (structure)

The parameters associated with the request.

CreateMultiRegionAccessPointRequest -> (structure)

A container of the parameters for a [CreateMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html) request.

Name -> (string)

The name of the Multi-Region Access Point associated with this request.

PublicAccessBlock -> (structure)

The `PublicAccessBlock` configuration that you want to apply to this Amazon S3 account. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see [The Meaning of âPublicâ](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status) in the *Amazon S3 User Guide* .

This data type is not supported for Amazon S3 on Outposts.

BlockPublicAcls -> (boolean)

Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to `TRUE` causes the following behavior:

- `PutBucketAcl` and `PutObjectAcl` calls fail if the specified ACL is public.
- PUT Object calls fail if the request includes a public ACL.
- PUT Bucket calls fail if the request includes a public ACL.

Enabling this setting doesnât affect existing policies or ACLs.

This property is not supported for Amazon S3 on Outposts.

IgnorePublicAcls -> (boolean)

Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to `TRUE` causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain.

Enabling this setting doesnât affect the persistence of any existing ACLs and doesnât prevent new public ACLs from being set.

This property is not supported for Amazon S3 on Outposts.

BlockPublicPolicy -> (boolean)

Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to `TRUE` causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access.

Enabling this setting doesnât affect existing bucket policies.

This property is not supported for Amazon S3 on Outposts.

RestrictPublicBuckets -> (boolean)

Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to `TRUE` restricts access to buckets with public policies to only Amazon Web Services service principals and authorized users within this account.

Enabling this setting doesnât affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked.

This property is not supported for Amazon S3 on Outposts.

Regions -> (list)

The buckets in different Regions that are associated with the Multi-Region Access Point.

(structure)

A Region that supports a Multi-Region Access Point as well as the associated bucket for the Region.

Bucket -> (string)

The name of the associated bucket for the Region.

BucketAccountId -> (string)

The Amazon Web Services account ID that owns the Amazon S3 bucket thatâs associated with this Multi-Region Access Point.

DeleteMultiRegionAccessPointRequest -> (structure)

A container of the parameters for a [DeleteMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html) request.

Name -> (string)

The name of the Multi-Region Access Point associated with this request.

PutMultiRegionAccessPointPolicyRequest -> (structure)

A container of the parameters for a [PutMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPoint.html) request.

Name -> (string)

The name of the Multi-Region Access Point associated with the request.

Policy -> (string)

The policy details for the `PutMultiRegionAccessPoint` request.

RequestStatus -> (string)

The current status of the request.

ResponseDetails -> (structure)

The details of the response.

MultiRegionAccessPointDetails -> (structure)

The details for the Multi-Region Access Point.

Regions -> (list)

A collection of status information for the different Regions that a Multi-Region Access Point supports.

(structure)

Status information for a single Multi-Region Access Point Region.

Name -> (string)

The name of the Region in the Multi-Region Access Point.

RequestStatus -> (string)

The current status of the Multi-Region Access Point in this Region.

ErrorDetails -> (structure)

Error details for an asynchronous request.

Code -> (string)

A string that uniquely identifies the error condition.

Message -> (string)

A generic description of the error condition in English.

Resource -> (string)

The identifier of the resource associated with the error.

RequestId -> (string)

The ID of the request associated with the error.