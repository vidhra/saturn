# group-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/group-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/group-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resource-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/index.html#cli-aws-resource-groups) ]

# group-resources

## Description

Adds the specified resources to the specified group.

### Warning

You can only use this operation with the following groups:

- `AWS::EC2::HostManagement`
- `AWS::EC2::CapacityReservationPool`
- `AWS::ResourceGroups::ApplicationGroup`

Other resource group types and resource types are not currently supported by this operation.

**Minimum permissions**

To run this command, you must have the following permissions:

- `resource-groups:GroupResources`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resource-groups-2017-11-27/GroupResources)

## Synopsis

```
group-resources
--group <value>
--resource-arns <value>
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

`--group` (string)

The name or the Amazon resource name (ARN) of the resource group to add resources to.

`--resource-arns` (list)

The list of Amazon resource names (ARNs) of the resources to be added to the group.

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

## Output

Succeeded -> (list)

A list of Amazon resource names (ARNs) of the resources that this operation successfully added to the group.

(string)

Failed -> (list)

A list of Amazon resource names (ARNs) of any resources that this operation failed to add to the group.

(structure)

A resource that failed to be added to or removed from a group.

ResourceArn -> (string)

The Amazon resource name (ARN) of the resource that failed to be added or removed.

ErrorMessage -> (string)

The error message text associated with the failure.

ErrorCode -> (string)

The error code associated with the failure.

Pending -> (list)

A list of Amazon resource names (ARNs) of any resources that this operation is still in the process adding to the group. These pending additions continue asynchronously. You can check the status of pending additions by using the ``  ListGroupResources `` operation, and checking the `Resources` array in the response and the `Status` field of each object in that array.

(structure)

A structure that identifies a resource that is currently pending addition to the group as a member. Adding a resource to a resource group happens asynchronously as a background task and this one isnât completed yet.

ResourceArn -> (string)

The Amazon resource name (ARN) of the resource thatâs in a pending state.