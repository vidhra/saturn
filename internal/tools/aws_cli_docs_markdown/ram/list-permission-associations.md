# list-permission-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-permission-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-permission-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ram](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html#cli-aws-ram) ]

# list-permission-associations

## Description

Lists information about the managed permission and its associations to any resource shares that use this managed permission. This lets you see which resource shares use which versions of the specified managed permission.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListPermissionAssociations)

## Synopsis

```
list-permission-associations
[--permission-arn <value>]
[--permission-version <value>]
[--association-status <value>]
[--resource-type <value>]
[--feature-set <value>]
[--default-version | --no-default-version]
[--next-token <value>]
[--max-results <value>]
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

Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed permission.

`--permission-version` (integer)

Specifies that you want to list only those associations with resource shares that use this version of the managed permission. If you donât provide a value for this parameter, then the operation returns information about associations with resource shares that use any version of the managed permission.

`--association-status` (string)

Specifies that you want to list only those associations with resource shares that match this status.

Possible values:

- `ASSOCIATING`
- `ASSOCIATED`
- `FAILED`
- `DISASSOCIATING`
- `DISASSOCIATED`

`--resource-type` (string)

Specifies that you want to list only those associations with resource shares that include at least one resource of this resource type.

`--feature-set` (string)

Specifies that you want to list only those associations with resource shares that have a `featureSet` with this value.

Possible values:

- `CREATED_FROM_POLICY`
- `PROMOTING_TO_STANDARD`
- `STANDARD`

`--default-version` | `--no-default-version` (boolean)

When `true` , specifies that you want to list only those associations with resource shares that use the default version of the specified managed permission.

When `false` (the default value), lists associations with resource shares that use any version of the specified managed permission.

`--next-token` (string)

Specifies that you want to receive the next page of results. Valid only if you received a `NextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous callâs `NextToken` response to request the next page of results.

`--max-results` (integer)

Specifies the total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the number you specify, the `NextToken` response element is returned with a value (not null). Include the specified value as the `NextToken` request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.

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

permissions -> (list)

A structure with information about this customer managed permission.

(structure)

An object that describes a managed permission associated with a resource share.

arn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the associated managed permission.

permissionVersion -> (string)

The version of the permission currently associated with the resource share.

defaultVersion -> (boolean)

Indicates whether the associated resource share is using the default version of the permission.

resourceType -> (string)

The resource type to which this permission applies.

status -> (string)

The current status of the association between the permission and the resource share. The following are the possible values:

- `ATTACHABLE` â This permission or version can be associated with resource shares.
- `UNATTACHABLE` â This permission or version canât currently be associated with resource shares.
- `DELETING` â This permission or version is in the process of being deleted.
- `DELETED` â This permission or version is deleted.

featureSet -> (string)

Indicates what features are available for this resource share. This parameter can have one of the following values:

- **STANDARD** â A resource share that supports all functionality. These resource shares are visible to all principals you share the resource share with. You can modify these resource shares in RAM using the console or APIs. This resource share might have been created by RAM, or it might have been **CREATED_FROM_POLICY** and then promoted.
- **CREATED_FROM_POLICY** â The customer manually shared a resource by attaching a resource-based policy. That policy did not match any existing managed permissions, so RAM created this customer managed permission automatically on the customerâs behalf based on the attached policy document. This type of resource share is visible only to the Amazon Web Services account that created it. You canât modify it in RAM unless you promote it. For more information, see  PromoteResourceShareCreatedFromPolicy .
- **PROMOTING_TO_STANDARD** â This resource share was originally `CREATED_FROM_POLICY` , but the customer ran the  PromoteResourceShareCreatedFromPolicy and that operation is still in progress. This value changes to `STANDARD` when complete.

lastUpdatedTime -> (timestamp)

The date and time when the association between the permission and the resource share was last updated.

resourceShareArn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a resource share associated with this permission.

nextToken -> (string)

If present, this value indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null` . This indicates that this is the last page of results.