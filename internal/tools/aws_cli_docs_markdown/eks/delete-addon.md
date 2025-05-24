# delete-addonÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-addon.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/delete-addon.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# delete-addon

## Description

Deletes an Amazon EKS add-on.

When you remove an add-on, itâs deleted from the cluster. You can always manually start an add-on on the cluster using the Kubernetes API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DeleteAddon)

## Synopsis

```
delete-addon
--cluster-name <value>
--addon-name <value>
[--preserve | --no-preserve]
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

`--cluster-name` (string)

The name of your cluster.

`--addon-name` (string)

The name of the add-on. The name must match one of the names returned by ` `ListAddons` [https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons](https://docs.aws.amazon.com/eks/latest/APIReference/API_ListAddons).html`__ .

`--preserve` | `--no-preserve` (boolean)

Specifying this option preserves the add-on software on your cluster but Amazon EKS stops managing any settings for the add-on. If an IAM account is associated with the add-on, it isnât removed.

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

**Example 1. To deletes an Amazon EKS add-on but preserve the add-on software on the EKS Cluster**

The following `delete-addon` example command deletes an Amazon EKS add-on but preserve the add-on software on the EKS Cluster.

```
aws eks delete-addon \
    --cluster-name my-eks-cluster \
    --addon-name my-eks-addon \
    --preserve
```

Output:

```
{
    "addon": {
        "addonName": "my-eks-addon",
        "clusterName": "my-eks-cluster",
        "status": "DELETING",
        "addonVersion": "v1.9.3-eksbuild.7",
        "health": {
            "issues": []
        },
        "addonArn": "arn:aws:eks:us-east-2:111122223333:addon/my-eks-cluster/my-eks-addon/a8c71ed3-944e-898b-9167-c763856af4b8",
        "createdAt": "2024-03-14T11:49:09.009000-04:00",
        "modifiedAt": "2024-03-14T12:03:49.776000-04:00",
        "tags": {}
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Deleting an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#removing-an-add-on) in the *Amazon EKS*.

**Example 2. To deletes an Amazon EKS add-on and also delete the add-on software from the EKS Cluster**

The following `delete-addon` example command deletes an Amazon EKS add-on and also delete the add-on software from the EKS Cluster.

```
aws eks delete-addon \
    --cluster-name my-eks-cluster \
    --addon-name my-eks-addon
```

Output:

```
{
    "addon": {
        "addonName": "my-eks-addon",
        "clusterName": "my-eks-cluster",
        "status": "DELETING",
        "addonVersion": "v1.15.1-eksbuild.1",
        "health": {
            "issues": []
        },
        "addonArn": "arn:aws:eks:us-east-2:111122223333:addon/my-eks-cluster/my-eks-addon/bac71ed1-ec43-3bb6-88ea-f243cdb58954",
        "createdAt": "2024-03-14T11:45:31.983000-04:00",
        "modifiedAt": "2024-03-14T11:58:40.136000-04:00",
        "serviceAccountRoleArn": "arn:aws:iam::111122223333:role/role-name",
        "tags": {}
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Deleting an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#removing-an-add-on) in the *Amazon EKS*.

## Output

addon -> (structure)

An Amazon EKS add-on. For more information, see [Amazon EKS add-ons](https://docs.aws.amazon.com/eks/latest/userguide/eks-add-ons.html) in the *Amazon EKS User Guide* .

addonName -> (string)

The name of the add-on.

clusterName -> (string)

The name of your cluster.

status -> (string)

The status of the add-on.

addonVersion -> (string)

The version of the add-on.

health -> (structure)

An object that represents the health of the add-on.

issues -> (list)

An object representing the health issues for an add-on.

(structure)

An issue related to an add-on.

code -> (string)

A code that describes the type of issue.

message -> (string)

A message that provides details about the issue and what might cause it.

resourceIds -> (list)

The resource IDs of the issue.

(string)

addonArn -> (string)

The Amazon Resource Name (ARN) of the add-on.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

modifiedAt -> (timestamp)

The Unix epoch timestamp for the last modification to the object.

serviceAccountRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role thatâs bound to the Kubernetes `ServiceAccount` object that the add-on uses.

tags -> (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

publisher -> (string)

The publisher of the add-on.

owner -> (string)

The owner of the add-on.

marketplaceInformation -> (structure)

Information about an Amazon EKS add-on from the Amazon Web Services Marketplace.

productId -> (string)

The product ID from the Amazon Web Services Marketplace.

productUrl -> (string)

The product URL from the Amazon Web Services Marketplace.

configurationValues -> (string)

The configuration values that you provided.

podIdentityAssociations -> (list)

An array of Pod Identity Assocations owned by the Addon. Each EKS Pod Identity association maps a role to a service account in a namespace in the cluster.

For more information, see [Attach an IAM Role to an Amazon EKS add-on using Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide* .

(string)