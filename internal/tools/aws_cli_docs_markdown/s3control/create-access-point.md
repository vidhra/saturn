# create-access-pointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html#cli-aws-s3control) ]

# create-access-point

## Description

Creates an access point and associates it to a specified bucket. For more information, see [Managing access to shared datasets in general purpose buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html) or [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the *Amazon S3 User Guide* .

### Note

S3 on Outposts only supports VPC-style access points.

For more information, see [Accessing Amazon S3 on Outposts using virtual private cloud (VPC) only access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html) in the *Amazon S3 User Guide* .

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control` . For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html#API_control_CreateAccessPoint_Examples) section.

The following actions are related to `CreateAccessPoint` :

- [GetAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html)
- [DeleteAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html)
- [ListAccessPoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html)
- [ListAccessPointsForDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForDirectoryBuckets.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/CreateAccessPoint)

## Synopsis

```
create-access-point
--account-id <value>
--name <value>
--bucket <value>
[--vpc-configuration <value>]
[--public-access-block-configuration <value>]
[--bucket-account-id <value>]
[--scope <value>]
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

The Amazon Web Services account ID for the account that owns the specified access point.

`--name` (string)

The name you want to assign to this access point.

For directory buckets, the access point name must consist of a base name that you provide and suffix that includes the `ZoneID` (Amazon Web Services Availability Zone or Local Zone) of your bucket location, followed by `--xa-s3` . For more information, see [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the Amazon S3 User Guide.

`--bucket` (string)

The name of the bucket that you want to associate this access point with.

For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.

For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>` . For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2` , use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports` . The value must be URL encoded.

`--vpc-configuration` (structure)

If you include this field, Amazon S3 restricts access to this access point to requests from the specified virtual private cloud (VPC).

### Note

This is required for creating an access point for Amazon S3 on Outposts buckets.

VpcId -> (string)

If this field is specified, this access point will only allow connections from the specified VPC ID.

Shorthand Syntax:

```
VpcId=string
```

JSON Syntax:

```
{
  "VpcId": "string"
}
```

`--public-access-block-configuration` (structure)

The `PublicAccessBlock` configuration that you want to apply to the access point.

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

Shorthand Syntax:

```
BlockPublicAcls=boolean,IgnorePublicAcls=boolean,BlockPublicPolicy=boolean,RestrictPublicBuckets=boolean
```

JSON Syntax:

```
{
  "BlockPublicAcls": true|false,
  "IgnorePublicAcls": true|false,
  "BlockPublicPolicy": true|false,
  "RestrictPublicBuckets": true|false
}
```

`--bucket-account-id` (string)

The Amazon Web Services account ID associated with the S3 bucket associated with this access point.

For same account access point when your bucket and access point belong to the same account owner, the `BucketAccountId` is not required. For cross-account access point when your bucket and access point are not in the same account, the `BucketAccountId` is required.

`--scope` (structure)

For directory buckets, you can filter access control to specific prefixes, API operations, or a combination of both. For more information, see [Managing access to shared datasets in directory buckets with access points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html) in the Amazon S3 User Guide.

### Note

Scope is not supported for access points for general purpose buckets.

Prefixes -> (list)

You can specify any amount of prefixes, but the total length of characters of all prefixes must be less than 256 bytes in size.

(string)

Permissions -> (list)

You can include one or more API operations as permissions.

(string)

Shorthand Syntax:

```
Prefixes=string,string,Permissions=string,string
```

JSON Syntax:

```
{
  "Prefixes": ["string", ...],
  "Permissions": ["GetObject"|"GetObjectAttributes"|"ListMultipartUploadParts"|"ListBucket"|"ListBucketMultipartUploads"|"PutObject"|"DeleteObject"|"AbortMultipartUpload", ...]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create an access point**

The following `create-access-point` example creates an access point named `finance-ap` for the bucket `business-records` in account 123456789012. Before running this example, replace the access point name, bucket name, and account number with appropriate values for your use case.

```
aws s3control create-access-point \
    --account-id 123456789012 \
    --bucket business-records \
    --name finance-ap
```

This command produces no output.

For more information, see [Creating Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html) in the *Amazon Simple Storage Service Developer Guide*.

## Output

AccessPointArn -> (string)

The ARN of the access point.

### Note

This is only supported by Amazon S3 on Outposts.

Alias -> (string)

The name or alias of the access point.