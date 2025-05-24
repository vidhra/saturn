# update-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dsql](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/index.html#cli-aws-dsql) ]

# update-cluster

## Description

The *UpdateCluster* API allows you to modify both single-Region and multi-Region cluster configurations. With the *multiRegionProperties* parameter, you can add or modify witness Region support and manage peer relationships with clusters in other Regions.

### Note

Note that updating multi-region clusters requires additional IAM permissions beyond those needed for standard cluster updates, as detailed in the Permissions section.

**Required permissions**

dsql:UpdateCluster

Permission to update a DSQL cluster.

Resources: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html#id1)arn:aws:dsql:*region* :*account-id* :cluster/*cluster-id* ``

dsql:PutMultiRegionProperties

Permission to configure multi-Region properties for a cluster.

Resources: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html#id3)arn:aws:dsql:*region* :*account-id* :cluster/*cluster-id* ``

dsql:GetCluster

Permission to retrieve cluster information.

Resources: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html#id5)arn:aws:dsql:*region* :*account-id* :cluster/*cluster-id* ``

dsql:AddPeerCluster

Permission to add peer clusters.

Resources:

- Local cluster: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html#id7)arn:aws:dsql:*region* :*account-id* :cluster/*cluster-id* ``
- Each peer cluster: exact ARN of each specified peer cluster

dsql:RemovePeerCluster

Permission to remove peer clusters. The *dsql:RemovePeerCluster* permission uses a wildcard ARN pattern to simplify permission management during updates.

Resources: `arn:aws:dsql:*:*account-id* :cluster/*`

dsql:PutWitnessRegion

Permission to set a witness Region.

Resources: [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/update-cluster.html#id9)arn:aws:dsql:*region* :*account-id* :cluster/*cluster-id* ``

Condition Keys: dsql:WitnessRegion (matching the specified witness Region)

**This permission is checked both in the cluster Region and in the witness Region.**

### Warning

- The witness region specified in `multiRegionProperties.witnessRegion` cannot be the same as the clusterâs Region.
- When updating clusters with peer relationships, permissions are checked for both adding and removing peers.
- The `dsql:RemovePeerCluster` permission uses a wildcard ARN pattern to simplify permission management during updates.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dsql-2018-05-10/UpdateCluster)

## Synopsis

```
update-cluster
--identifier <value>
[--deletion-protection-enabled | --no-deletion-protection-enabled]
[--client-token <value>]
[--multi-region-properties <value>]
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

`--identifier` (string)

The ID of the cluster you want to update.

`--deletion-protection-enabled` | `--no-deletion-protection-enabled` (boolean)

Specifies whether to enable deletion protection in your cluster.

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully. The subsequent retries with the same client token return the result from the original successful request and they have no additional effect.

If you donât specify a client token, the Amazon Web Services SDK automatically generates one.

`--multi-region-properties` (structure)

The new multi-Region cluster configuration settings to be applied during an update operation.

witnessRegion -> (string)

The that serves as the witness region for a multi-Region cluster. The witness region helps maintain cluster consistency and quorum.

clusters -> (list)

The set of linked clusters that form the multi-Region cluster configuration. Each linked cluster represents a database instance in a different Region.

(string)

The Amazon Resource Name of the cluster.

Shorthand Syntax:

```
witnessRegion=string,clusters=string,string
```

JSON Syntax:

```
{
  "witnessRegion": "string",
  "clusters": ["string", ...]
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

identifier -> (string)

The ID of the cluster to update.

arn -> (string)

The ARN of the updated cluster.

status -> (string)

The status of the updated cluster.

creationTime -> (timestamp)

The time of when the cluster was created.