# replace-permission-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/replace-permission-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/replace-permission-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ram](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html#cli-aws-ram) ]

# replace-permission-associations

## Description

Updates all resource shares that use a managed permission to a different managed permission. This operation always applies the default version of the target managed permission. You can optionally specify that the update applies to only resource shares that currently use a specified version. This enables you to update to the latest version, without changing the which managed permission is used.

You can use this operation to update all of your resource shares to use the current default version of the permission by specifying the same value for the `fromPermissionArn` and `toPermissionArn` parameters.

You can use the optional `fromPermissionVersion` parameter to update only those resources that use a specified version of the managed permission to the new managed permission.

### Warning

To successfully perform this operation, you must have permission to update the resource-based policy on all affected resource types.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ReplacePermissionAssociations)

## Synopsis

```
replace-permission-associations
--from-permission-arn <value>
[--from-permission-version <value>]
--to-permission-arn <value>
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

`--from-permission-arn` (string)

Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed permission that you want to replace.

`--from-permission-version` (integer)

Specifies that you want to updated the permissions for only those resource shares that use the specified version of the managed permission.

`--to-permission-arn` (string)

Specifies the ARN of the managed permission that you want to associate with resource shares in place of the one specified by `fromPerssionArn` and `fromPermissionVersion` .

The operation always associates the version that is currently the default for the specified managed permission.

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

replacePermissionAssociationsWork -> (structure)

Specifies a data structure that you can use to track the asynchronous tasks that RAM performs to complete this operation. You can use the  ListReplacePermissionAssociationsWork operation and pass the `id` value returned in this structure.

id -> (string)

The unique identifier for the background task associated with one  ReplacePermissionAssociations request.

fromPermissionArn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed permission that this background task is replacing.

fromPermissionVersion -> (string)

The version of the managed permission that this background task is replacing.

toPermissionArn -> (string)

The ARN of the managed permission that this background task is associating with the resource shares in place of the managed permission and version specified in `fromPermissionArn` and `fromPermissionVersion` .

toPermissionVersion -> (string)

The version of the managed permission that this background task is associating with the resource shares. This is always the version that is currently the default for this managed permission.

status -> (string)

Specifies the current status of the background tasks for the specified ID. The output is one of the following strings:

- `IN_PROGRESS`
- `COMPLETED`
- `FAILED`

statusMessage -> (string)

Specifies the reason for a `FAILED` status. This field is present only when there `status` is `FAILED` .

creationTime -> (timestamp)

The date and time when this asynchronous background task was created.

lastUpdatedTime -> (timestamp)

The date and time when the status of this background task was last updated.

clientToken -> (string)

The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.