# update-cluster-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-cluster-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-cluster-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# update-cluster-version

## Description

Updates an Amazon EKS cluster to the specified Kubernetes version. Your cluster continues to function during the update. The response output includes an update ID that you can use to track the status of your cluster update with the ` `DescribeUpdate` [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeUpdate).html`__ API operation.

Cluster updates are asynchronous, and they should finish within a few minutes. During an update, the cluster status moves to `UPDATING` (this status transition is eventually consistent). When the update is complete (either `Failed` or `Successful` ), the cluster status moves to `Active` .

If your cluster has managed node groups attached to it, all of your node groupsâ Kubernetes versions must match the clusterâs Kubernetes version in order to update the cluster to a new Kubernetes version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateClusterVersion)

## Synopsis

```
update-cluster-version
--name <value>
[--client-request-token <value>]
[--force | --no-force]
--kubernetes-version <value>
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

`--name` (string)

The name of the Amazon EKS cluster to update.

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--force` | `--no-force` (boolean)

Set this value to `true` to override upgrade-blocking readiness checks when updating a cluster.

`--kubernetes-version` (string)

The desired Kubernetes version following a successful update.

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

**To updates an Amazon EKS cluster named `my-eks-cluster` to the specified Kubernetes version**

The following `update-cluster-version` example updates an Amazon EKS cluster to the specified Kubernetes version.

```
aws eks update-cluster-version \
    --name my-eks-cluster \
    --kubernetes-version 1.27
```

Output:

```
{
    "update": {
        "id": "e4091a28-ea14-48fd-a8c7-975aeb469e8a",
        "status": "InProgress",
        "type": "VersionUpdate",
        "params": [
            {
                "type": "Version",
                "value": "1.27"
            },
            {
                "type": "PlatformVersion",
                "value": "eks.16"
            }
        ],
        "createdAt": "2024-04-12T16:56:01.082000-04:00",
        "errors": []
    }
}
```

For more information, see [Updating an Amazon EKS cluster Kubernetes version](https://docs.aws.amazon.com/eks/latest/userguide/update-cluster.html) in the *Amazon EKS User Guide*.

## Output

update -> (structure)

The full description of the specified update

id -> (string)

A UUID that is used to track the update.

status -> (string)

The current status of the update.

type -> (string)

The type of the update.

params -> (list)

A key-value map that contains the parameters associated with the update.

(structure)

An object representing the details of an update request.

type -> (string)

The keys associated with an update request.

value -> (string)

The value of the keys submitted as part of an update request.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

errors -> (list)

Any errors associated with a `Failed` update.

(structure)

An object representing an error when an asynchronous operation fails.

errorCode -> (string)

A brief description of the error.

- **SubnetNotFound** : We couldnât find one of the subnets associated with the cluster.
- **SecurityGroupNotFound** : We couldnât find one of the security groups associated with the cluster.
- **EniLimitReached** : You have reached the elastic network interface limit for your account.
- **IpNotAvailable** : A subnet associated with the cluster doesnât have any available IP addresses.
- **AccessDenied** : You donât have permissions to perform the specified operation.
- **OperationNotPermitted** : The service role associated with the cluster doesnât have the required access permissions for Amazon EKS.
- **VpcIdNotFound** : We couldnât find the VPC associated with the cluster.

errorMessage -> (string)

A more complete description of the error.

resourceIds -> (list)

An optional field that contains the resource IDs associated with the error.

(string)