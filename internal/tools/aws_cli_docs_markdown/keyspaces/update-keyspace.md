# update-keyspaceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/update-keyspace.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/update-keyspace.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [keyspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/index.html#cli-aws-keyspaces) ]

# update-keyspace

## Description

Adds a new Amazon Web Services Region to the keyspace. You can add a new Region to a keyspace that is either a single or a multi-Region keyspace. Amazon Keyspaces is going to replicate all tables in the keyspace to the new Region. To successfully replicate all tables to the new Region, they must use client-side timestamps for conflict resolution. To enable client-side timestamps, specify `clientSideTimestamps.status = enabled` when invoking the API. For more information about client-side timestamps, see [Client-side timestamps in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps.html) in the *Amazon Keyspaces Developer Guide* .

To add a Region to a keyspace using the `UpdateKeyspace` API, the IAM principal needs permissions for the following IAM actions:

- `cassandra:Alter`
- `cassandra:AlterMultiRegionResource`
- `cassandra:Create`
- `cassandra:CreateMultiRegionResource`
- `cassandra:Select`
- `cassandra:SelectMultiRegionResource`
- `cassandra:Modify`
- `cassandra:ModifyMultiRegionResource`

If the keyspace contains a table that is configured in provisioned mode with auto scaling enabled, the following additional IAM actions need to be allowed.

- `application-autoscaling:RegisterScalableTarget`
- `application-autoscaling:DeregisterScalableTarget`
- `application-autoscaling:DescribeScalableTargets`
- `application-autoscaling:PutScalingPolicy`
- `application-autoscaling:DescribeScalingPolicies`

To use the `UpdateKeyspace` API, the IAM principal also needs permissions to create a service-linked role with the following elements:

- `iam:CreateServiceLinkedRole` - The **action** the principal can perform.
- `arn:aws:iam::*:role/aws-service-role/replication.cassandra.amazonaws.com/AWSServiceRoleForKeyspacesReplication` - The **resource** that the action can be performed on.
- `iam:AWSServiceName: replication.cassandra.amazonaws.com` - The only Amazon Web Services service that this role can be attached to is Amazon Keyspaces.

For more information, see [Configure the IAM permissions required to add an Amazon Web Services Region to a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_replication_permissions_addReplica.html) in the *Amazon Keyspaces Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/keyspaces-2022-02-10/UpdateKeyspace)

## Synopsis

```
update-keyspace
--keyspace-name <value>
--replication-specification <value>
[--client-side-timestamps <value>]
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

`--keyspace-name` (string)

The name of the keyspace.

`--replication-specification` (structure)

The replication specification of the keyspace includes:

- `regionList` - the Amazon Web Services Regions where the keyspace is replicated in.
- `replicationStrategy` - the required value is `SINGLE_REGION` or `MULTI_REGION` .

replicationStrategy -> (string)

The `replicationStrategy` of a keyspace, the required value is `SINGLE_REGION` or `MULTI_REGION` .

regionList -> (list)

The `regionList` contains the Amazon Web Services Regions where the keyspace is replicated in.

(string)

Shorthand Syntax:

```
replicationStrategy=string,regionList=string,string
```

JSON Syntax:

```
{
  "replicationStrategy": "SINGLE_REGION"|"MULTI_REGION",
  "regionList": ["string", ...]
}
```

`--client-side-timestamps` (structure)

The client-side timestamp setting of the table.

For more information, see [How it works: Amazon Keyspaces client-side timestamps](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps-how-it-works.html) in the *Amazon Keyspaces Developer Guide* .

status -> (string)

Shows how to enable client-side timestamps settings for the specified table.

Shorthand Syntax:

```
status=string
```

JSON Syntax:

```
{
  "status": "ENABLED"
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

## Output

resourceArn -> (string)

The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).