# promote-permission-created-from-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/promote-permission-created-from-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/promote-permission-created-from-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ram](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html#cli-aws-ram) ]

# promote-permission-created-from-policy

## Description

When you attach a resource-based policy to a resource, RAM automatically creates a resource share of `featureSet` =``CREATED_FROM_POLICY`` with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share canât be modified by using RAM.

This operation creates a separate, fully manageable customer managed permission that has the same IAM permissions as the original resource-based policy. You can associate this customer managed permission to any resource shares.

Before you use  PromoteResourceShareCreatedFromPolicy , you should first run this operation to ensure that you have an appropriate customer managed permission that can be associated with the promoted resource share.

### Note

- The original `CREATED_FROM_POLICY` policy isnât deleted, and resource shares using that original policy arenât automatically updated.
- You canât modify a `CREATED_FROM_POLICY` resource share so you canât associate the new customer managed permission by using `ReplacePermsissionAssociations` . However, if you use  PromoteResourceShareCreatedFromPolicy , that operation automatically associates the fully manageable customer managed permission to the newly promoted `STANDARD` resource share.
- After you promote a resource share, if the original `CREATED_FROM_POLICY` managed permission has no other associations to A resource share, then RAM automatically deletes it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/PromotePermissionCreatedFromPolicy)

## Synopsis

```
promote-permission-created-from-policy
--permission-arn <value>
--name <value>
[--client-token <value>]
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

`--permission-arn` (string)

Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the `CREATED_FROM_POLICY` permission that you want to promote. You can get this [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) by calling the  ListResourceSharePermissions operation.

`--name` (string)

Specifies a name for the promoted customer managed permission.

`--client-token` (string)

Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier) .

If you donât provide this value, then Amazon Web Services generates a random one for you.

If you retry the operation with the same `ClientToken` , but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.

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

permission -> (structure)

Information about an RAM permission.

arn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the permission you want information about.

version -> (string)

The version of the permission associated with this resource share.

defaultVersion -> (boolean)

Specifies whether the version of the managed permission used by this resource share is the default version for this managed permission.

name -> (string)

The name of this managed permission.

resourceType -> (string)

The type of resource to which this permission applies. This takes the form of: `service-code` :`resource-code` , and is case-insensitive. For example, an Amazon EC2 Subnet would be represented by the string `ec2:subnet` .

status -> (string)

The current status of the permission.

creationTime -> (timestamp)

The date and time when the permission was created.

lastUpdatedTime -> (timestamp)

The date and time when the permission was last updated.

isResourceTypeDefault -> (boolean)

Specifies whether the managed permission associated with this resource share is the default managed permission for all resources of this resource type.

permissionType -> (string)

The type of managed permission. This can be one of the following values:

- `AWS_MANAGED` â Amazon Web Services created and manages this managed permission. You can associate it with your resource shares, but you canât modify it.
- `CUSTOMER_MANAGED` â You, or another principal in your account created this managed permission. You can associate it with your resource shares and create new versions that have different permissions.

featureSet -> (string)

Indicates what features are available for this resource share. This parameter can have one of the following values:

- **STANDARD** â A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in RAM using the console or APIs. This resource share might have been created by RAM, or it might have been **CREATED_FROM_POLICY** and then promoted.
- **CREATED_FROM_POLICY** â The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so RAM created this customer managed permission automatically on the customerâs behalf based on the attached policy document. This type of resource share is visible only to the Amazon Web Services account that created it. You canât modify it in RAM unless you promote it. For more information, see  PromoteResourceShareCreatedFromPolicy .
- **PROMOTING_TO_STANDARD** â This resource share was originally `CREATED_FROM_POLICY` , but the customer ran the  PromoteResourceShareCreatedFromPolicy and that operation is still in progress. This value changes to `STANDARD` when complete.

tags -> (list)

A list of the tag key value pairs currently attached to the permission.

(structure)

A structure containing a tag. A tag is metadata that you can attach to your resources to help organize and categorize them. You can also use them to help you secure your resources. For more information, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) .

For more information about tags, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference Guide* .

key -> (string)

The key, or name, attached to the tag. Every tag must have a key. Key names are case sensitive.

value -> (string)

The string value attached to the tag. The value can be an empty string. Key values are case sensitive.

clientToken -> (string)

The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.