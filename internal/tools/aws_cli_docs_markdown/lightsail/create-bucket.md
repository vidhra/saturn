# create-bucketÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-bucket.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-bucket.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-bucket

## Description

Creates an Amazon Lightsail bucket.

A bucket is a cloud storage resource available in the Lightsail object storage service. Use buckets to store objects such as data and its descriptive metadata. For more information about buckets, see [Buckets in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/buckets-in-amazon-lightsail) in the *Amazon Lightsail Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateBucket)

## Synopsis

```
create-bucket
--bucket-name <value>
--bundle-id <value>
[--tags <value>]
[--enable-object-versioning | --no-enable-object-versioning]
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

`--bucket-name` (string)

The name for the bucket.

For more information about bucket names, see [Bucket naming rules in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/bucket-naming-rules-in-amazon-lightsail) in the *Amazon Lightsail Developer Guide* .

`--bundle-id` (string)

The ID of the bundle to use for the bucket.

A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.

Use the [GetBucketBundles](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html) action to get a list of bundle IDs that you can specify.

Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to change the bundle after the bucket is created.

`--tags` (list)

The tag keys and optional values to add to the bucket during creation.

Use the [TagResource](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_TagResource.html) action to tag the bucket after itâs created.

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

`--enable-object-versioning` | `--no-enable-object-versioning` (boolean)

A Boolean value that indicates whether to enable versioning of objects in the bucket.

For more information about versioning, see [Enabling and suspending object versioning in a bucket in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-bucket-object-versioning) in the *Amazon Lightsail Developer Guide* .

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

bucket -> (structure)

An object that describes the bucket that is created.

resourceType -> (string)

The Lightsail resource type of the bucket.

accessRules -> (structure)

An object that describes the access rules of the bucket.

getObject -> (string)

Specifies the anonymous access to all objects in a bucket.

The following options can be specified:

- `public` - Sets all objects in the bucket to public (read-only), making them readable by anyone in the world. If the `getObject` value is set to `public` , then all objects in the bucket default to public regardless of the `allowPublicOverrides` value.
- `private` - Sets all objects in the bucket to private, making them readable only by you or anyone you give access to. If the `getObject` value is set to `private` , and the `allowPublicOverrides` value is set to `true` , then all objects in the bucket default to private unless they are configured with a `public-read` ACL. Individual objects with a `public-read` ACL are readable by anyone in the world.

allowPublicOverrides -> (boolean)

A Boolean value that indicates whether the access control list (ACL) permissions that are applied to individual objects override the `getObject` option that is currently specified.

When this is true, you can use the [PutObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) Amazon S3 API action to set individual objects to public (read-only) using the `public-read` ACL, or to private using the `private` ACL.

arn -> (string)

The Amazon Resource Name (ARN) of the bucket.

bundleId -> (string)

The ID of the bundle currently applied to the bucket.

A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.

Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to change the bundle of a bucket.

createdAt -> (timestamp)

The timestamp when the distribution was created.

url -> (string)

The URL of the bucket.

location -> (structure)

An object that describes the location of the bucket, such as the Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

name -> (string)

The name of the bucket.

supportCode -> (string)

The support code for a bucket. Include this code in your email to support when you have questions about a Lightsail bucket. This code enables our support team to look up your Lightsail information more easily.

tags -> (list)

The tag keys and optional values for the bucket. For more information, see [Tags in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags) in the *Amazon Lightsail Developer Guide* .

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

objectVersioning -> (string)

Indicates whether object versioning is enabled for the bucket.

The following options can be configured:

- `Enabled` - Object versioning is enabled.
- `Suspended` - Object versioning was previously enabled but is currently suspended. Existing object versions are retained.
- `NeverEnabled` - Object versioning has never been enabled.

ableToUpdateBundle -> (boolean)

Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle.

You can update a bucketâs bundle only one time within a monthly Amazon Web Services billing cycle.

Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to change a bucketâs bundle.

readonlyAccessAccounts -> (list)

An array of strings that specify the Amazon Web Services account IDs that have read-only access to the bucket.

(string)

resourcesReceivingAccess -> (list)

An array of objects that describe Lightsail instances that have access to the bucket.

Use the [SetResourceAccessForBucket](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html) action to update the instances that have access to a bucket.

(structure)

Describes an Amazon Lightsail instance that has access to a Lightsail bucket.

name -> (string)

The name of the Lightsail instance.

resourceType -> (string)

The Lightsail resource type (for example, `Instance` ).

state -> (structure)

An object that describes the state of the bucket.

code -> (string)

The state code of the bucket.

The following codes are possible:

- `OK` - The bucket is in a running state.
- `Unknown` - Creation of the bucket might have timed-out. You might want to delete the bucket and create a new one.

message -> (string)

A message that describes the state of the bucket.

accessLogConfig -> (structure)

An object that describes the access log configuration for the bucket.

enabled -> (boolean)

A Boolean value that indicates whether bucket access logging is enabled for the bucket.

destination -> (string)

The name of the bucket where the access logs are saved. The destination can be a Lightsail bucket in the same account, and in the same Amazon Web Services Region as the source bucket.

### Note

This parameter is required when enabling the access log for a bucket, and should be omitted when disabling the access log.

prefix -> (string)

The optional object prefix for the bucket access log.

The prefix is an optional addition to the object key that organizes your access log files in the destination bucket. For example, if you specify a `logs/` prefix, then each log object will begin with the `logs/` prefix in its key (for example, `logs/2021-11-01-21-32-16-E568B2907131C0C0` ).

### Note

This parameter can be optionally specified when enabling the access log for a bucket, and should be omitted when disabling the access log.

operations -> (list)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(structure)

Describes the API operation.

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