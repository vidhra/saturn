# create-replication-subnet-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# create-replication-subnet-group

## Description

Creates a replication subnet group given a list of the subnet IDs in a VPC.

The VPC needs to have at least one subnet in at least two availability zones in the Amazon Web Services Region, otherwise the service will throw a `ReplicationSubnetGroupDoesNotCoverEnoughAZs` exception.

If a replication subnet group exists in your Amazon Web Services account, the CreateReplicationSubnetGroup action returns the following error message: The Replication Subnet Group already exists. In this case, delete the existing replication subnet group. To do so, use the [DeleteReplicationSubnetGroup](https://docs.aws.amazon.com/en_us/dms/latest/APIReference/API_DeleteReplicationSubnetGroup.html) action. Optionally, choose Subnet groups in the DMS console, then choose your subnet group. Next, choose Delete from Actions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/CreateReplicationSubnetGroup)

## Synopsis

```
create-replication-subnet-group
--replication-subnet-group-identifier <value>
--replication-subnet-group-description <value>
--subnet-ids <value>
[--tags <value>]
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

`--replication-subnet-group-identifier` (string)

The name for the replication subnet group. This value is stored as a lowercase string.

Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, or hyphens. Must not be âdefaultâ.

Example: `mySubnetgroup`

`--replication-subnet-group-description` (string)

The description for the subnet group.

`--subnet-ids` (list)

Two or more subnet IDs to be assigned to the subnet group.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

One or more tags to be assigned to the subnet group.

(structure)

A user-defined key-value pair that describes metadata added to an DMS resource and that is used by operations such as the following:

- `AddTagsToResource`
- `ListTagsForResource`
- `RemoveTagsFromResource`

Key -> (string)

A key is the required name of the tag. The string value can be 1-128 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be 1-256 Unicode characters in length and canât be prefixed with âaws:â or âdms:â. The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â (Java regular expressions: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

ResourceArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the resource for which the tag is created.

Shorthand Syntax:

```
Key=string,Value=string,ResourceArn=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "ResourceArn": "string"
  }
  ...
]
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

**To create a subnet group**

The following `create-replication-subnet-group` example creates a group consisting of 3 subnets.

```
aws dms create-replication-subnet-group \
    --replication-subnet-group-identifier my-subnet-group \
    --replication-subnet-group-description "my subnet group" \
    --subnet-ids subnet-da327bf6 subnet-bac383e0 subnet-d7c825e8
```

Output:

```
{
    "ReplicationSubnetGroup": {
        "ReplicationSubnetGroupIdentifier": "my-subnet-group",
        "ReplicationSubnetGroupDescription": "my subnet group",
        "VpcId": "vpc-136a4c6a",
        "SubnetGroupStatus": "Complete",
        "Subnets": [
            {
                "SubnetIdentifier": "subnet-da327bf6",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1a"
                },
                "SubnetStatus": "Active"
            },
            {
                "SubnetIdentifier": "subnet-bac383e0",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1c"
                },
                "SubnetStatus": "Active"
            },
            {
                "SubnetIdentifier": "subnet-d7c825e8",
                "SubnetAvailabilityZone": {
                    "Name": "us-east-1e"
                },
                "SubnetStatus": "Active"
            }
        ]
    }
}
```

For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html) in the *AWS Database Migration Service User Guide*.

## Output

ReplicationSubnetGroup -> (structure)

The replication subnet group that was created.

ReplicationSubnetGroupIdentifier -> (string)

The identifier of the replication instance subnet group.

ReplicationSubnetGroupDescription -> (string)

A description for the replication subnet group.

VpcId -> (string)

The ID of the VPC.

SubnetGroupStatus -> (string)

The status of the subnet group.

Subnets -> (list)

The subnets that are in the subnet group.

(structure)

In response to a request by the `DescribeReplicationSubnetGroups` operation, this object identifies a subnet by its given Availability Zone, subnet identifier, and status.

SubnetIdentifier -> (string)

The subnet identifier.

SubnetAvailabilityZone -> (structure)

The Availability Zone of the subnet.

Name -> (string)

The name of the Availability Zone.

SubnetStatus -> (string)

The status of the subnet.

SupportedNetworkTypes -> (list)

The IP addressing protocol supported by the subnet group. This is used by a replication instance with values such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.

(string)