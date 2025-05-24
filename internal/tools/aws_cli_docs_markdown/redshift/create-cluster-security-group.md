# create-cluster-security-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# create-cluster-security-group

## Description

Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.

For information about managing security groups, go to [Amazon Redshift Cluster Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateClusterSecurityGroup)

## Synopsis

```
create-cluster-security-group
--cluster-security-group-name <value>
--description <value>
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

`--cluster-security-group-name` (string)

The name for the security group. Amazon Redshift stores the value as a lowercase string.

Constraints:

- Must contain no more than 255 alphanumeric characters or hyphens.
- Must not be âDefaultâ.
- Must be unique for all security groups that are created by your Amazon Web Services account.

Example: `examplesecuritygroup`

`--description` (string)

A description for the security group.

`--tags` (list)

A list of tag instances.

(structure)

A tag consisting of a name/value pair for a resource.

Key -> (string)

The key, or name, for the resource tag.

Value -> (string)

The value for the resource tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

### Creating a Cluster Security Group

This example creates a new cluster security group. By default, the output is in JSON format.

Command:

```
aws redshift create-cluster-security-group --cluster-security-group-name mysecuritygroup --description "This is my cluster security group"
```

Result:

```
{
   "create_cluster_security_group_response": {
      "create_cluster_security_group_result": {
         "cluster_security_group": {
            "description": "This is my cluster security group",
            "owner_id": "300454760768",
            "cluster_security_group_name": "mysecuritygroup",
            "ec2_security_groups": \[],
            "ip_ranges": \[]
         }
      },
      "response_metadata": {
         "request_id": "5df486a0-343a-11e2-b0d8-d15d0ef48549"
      }
   }
}
```

You can also obtain the same information in text format using the `--output text` option.

Command:

```
aws redshift create-cluster-security-group --cluster-security-group-name mysecuritygroup --description "This is my cluster security group" --output text
```

Result:

```
This is my cluster security group   300454760768    mysecuritygroup
a0c0bfab-343a-11e2-95d2-c3dc9fe8ab57
```

## Output

ClusterSecurityGroup -> (structure)

Describes a security group.

ClusterSecurityGroupName -> (string)

The name of the cluster security group to which the operation was applied.

Description -> (string)

A description of the security group.

EC2SecurityGroups -> (list)

A list of EC2 security groups that are permitted to access clusters associated with this cluster security group.

(structure)

Describes an Amazon EC2 security group.

Status -> (string)

The status of the EC2 security group.

EC2SecurityGroupName -> (string)

The name of the EC2 Security Group.

EC2SecurityGroupOwnerId -> (string)

The Amazon Web Services account ID of the owner of the EC2 security group specified in the `EC2SecurityGroupName` field.

Tags -> (list)

The list of tags for the EC2 security group.

(structure)

A tag consisting of a name/value pair for a resource.

Key -> (string)

The key, or name, for the resource tag.

Value -> (string)

The value for the resource tag.

IPRanges -> (list)

A list of IP ranges (CIDR blocks) that are permitted to access clusters associated with this cluster security group.

(structure)

Describes an IP range used in a security group.

Status -> (string)

The status of the IP range, for example, âauthorizedâ.

CIDRIP -> (string)

The IP range in Classless Inter-Domain Routing (CIDR) notation.

Tags -> (list)

The list of tags for the IP range.

(structure)

A tag consisting of a name/value pair for a resource.

Key -> (string)

The key, or name, for the resource tag.

Value -> (string)

The value for the resource tag.

Tags -> (list)

The list of tags for the cluster security group.

(structure)

A tag consisting of a name/value pair for a resource.

Key -> (string)

The key, or name, for the resource tag.

Value -> (string)

The value for the resource tag.