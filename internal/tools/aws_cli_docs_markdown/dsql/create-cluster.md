# create-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/create-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/create-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dsql](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dsql/index.html#cli-aws-dsql) ]

# create-cluster

## Description

The CreateCluster API allows you to create both single-region clusters and multi-Region clusters. With the addition of the *multiRegionProperties* parameter, you can create a cluster with witness Region support and establish peer relationships with clusters in other Regions during creation.

### Note

Creating multi-Region clusters requires additional IAM permissions beyond those needed for single-Region clusters, as detailed in the **Required permissions** section below.

**Required permissions**

dsql:CreateCluster

Required to create a cluster.

Resources: `arn:aws:dsql:region:account-id:cluster/*`

dsql:TagResource

Permission to add tags to a resource.

Resources: `arn:aws:dsql:region:account-id:cluster/*`

dsql:PutMultiRegionProperties

Permission to configure multi-region properties for a cluster.

Resources: `arn:aws:dsql:region:account-id:cluster/*`

dsql:AddPeerCluster

When specifying `multiRegionProperties.clusters` , permission to add peer clusters.

Resources:

- Local cluster: `arn:aws:dsql:region:account-id:cluster/*`
- Each peer cluster: exact ARN of each specified peer cluster

dsql:PutWitnessRegion

When specifying `multiRegionProperties.witnessRegion` , permission to set a witness Region. This permission is checked both in the cluster Region and in the witness Region.

Resources: `arn:aws:dsql:region:account-id:cluster/*`

Condition Keys: `dsql:WitnessRegion` (matching the specified witness region)

### Warning

- The witness Region specified in `multiRegionProperties.witnessRegion` cannot be the same as the clusterâs Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dsql-2018-05-10/CreateCluster)

## Synopsis

```
create-cluster
[--deletion-protection-enabled | --no-deletion-protection-enabled]
[--tags <value>]
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

`--deletion-protection-enabled` | `--no-deletion-protection-enabled` (boolean)

If enabled, you canât delete your cluster. You must first disable this property before you can delete your cluster.

`--tags` (map)

A map of key and value pairs to use to tag your cluster.

key -> (string)

Unique tag key, maximum 128 Unicode characters in UTF-8.

value -> (string)

Tag value, maximum 256 Unicode characters in UTF-8.

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries with the same client token return the result from the original successful request and they have no additional effect.

If you donât specify a client token, the Amazon Web Services SDK automatically generates one.

`--multi-region-properties` (structure)

The configuration settings when creating a multi-Region cluster, including the witness region and linked cluster properties.

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

The ID of the created cluster.

arn -> (string)

The ARN of the created cluster.

status -> (string)

The status of the created cluster.

creationTime -> (timestamp)

The time of when created the cluster.

multiRegionProperties -> (structure)

The multi-Region cluster configuration details that were set during cluster creation

witnessRegion -> (string)

The that serves as the witness region for a multi-Region cluster. The witness region helps maintain cluster consistency and quorum.

clusters -> (list)

The set of linked clusters that form the multi-Region cluster configuration. Each linked cluster represents a database instance in a different Region.

(string)

The Amazon Resource Name of the cluster.

deletionProtectionEnabled -> (boolean)

Whether deletion protection is enabled on this cluster.