# disassociate-resource-shareÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ram](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html#cli-aws-ram) ]

# disassociate-resource-share

## Description

Removes the specified principals or resources from participating in the specified resource share.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/DisassociateResourceShare)

## Synopsis

```
disassociate-resource-share
--resource-share-arn <value>
[--resource-arns <value>]
[--principals <value>]
[--client-token <value>]
[--sources <value>]
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

`--resource-share-arn` (string)

Specifies [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share that you want to remove resources or principals from.

`--resource-arns` (list)

Specifies a list of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for one or more resources that you want to remove from the resource share. After the operation runs, these resources are no longer shared with principals associated with the resource share.

(string)

Syntax:

```
"string" "string" ...
```

`--principals` (list)

Specifies a list of one or more principals that no longer are to have access to the resources in this resource share.

You can include the following values:

- An Amazon Web Services account ID, for example: `123456789012`
- An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in Organizations, for example: `organizations::123456789012:organization/o-exampleorgid`
- An ARN of an organizational unit (OU) in Organizations, for example: `organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123`
- An ARN of an IAM role, for example: `iam::123456789012:role/rolename`
- An ARN of an IAM user, for example: `iam::123456789012user/username`

### Note

Not all resource types can be shared with IAM roles and users. For more information, see [Sharing with IAM roles and users](https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types) in the *Resource Access Manager User Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--client-token` (string)

Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier) .

If you donât provide this value, then Amazon Web Services generates a random one for you.

If you retry the operation with the same `ClientToken` , but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.

`--sources` (list)

Specifies from which source accounts the service principal no longer has access to the resources in this resource share.

(string)

Syntax:

```
"string" "string" ...
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

**To remove a resource from a resource share**

The following `disassociate-resource-share` example removes the specified resource, in this case a VPC subnet, from the specified resource share. Any principals with access to the resource share can no longer perform operations on that resource.

```
aws ram disassociate-resource-share \
    --resource-arns arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE \
    --resource-share-arn arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE
```

Output:

```
{
    "resourceShareAssociations": [
        "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE",
        "associatedEntity": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE",
        "associationType": "RESOURCE",
        "status": "DISASSOCIATING",
        "external": false
    ]
}
```

## Output

resourceShareAssociations -> (list)

An array of objects with information about the updated associations for this resource share.

(structure)

Describes an association between a resource share and either a principal or a resource.

resourceShareArn -> (string)

The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share.

resourceShareName -> (string)

The name of the resource share.

associatedEntity -> (string)

The associated entity. This can be either of the following:

- For a resource association, this is the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource.
- For principal associations, this is one of the following:
- The ID of an Amazon Web Services account
- The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in Organizations
- The ARN of an organizational unit (OU) in Organizations
- The ARN of an IAM role
- The ARN of an IAM user

associationType -> (string)

The type of entity included in this association.

status -> (string)

The current status of the association.

statusMessage -> (string)

A message about the status of the association.

creationTime -> (timestamp)

The date and time when the association was created.

lastUpdatedTime -> (timestamp)

The date and time when the association was last updated.

external -> (boolean)

Indicates whether the principal belongs to the same organization in Organizations as the Amazon Web Services account that owns the resource share.

clientToken -> (string)

The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.