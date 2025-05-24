# create-fargate-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/create-fargate-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# create-fargate-profile

## Description

Creates an Fargate profile for your Amazon EKS cluster. You must have at least one Fargate profile in a cluster to be able to run pods on Fargate.

The Fargate profile allows an administrator to declare which pods run on Fargate and specify which pods run on which Fargate profile. This declaration is done through the profileâs selectors. Each profile can have up to five selectors that contain a namespace and labels. A namespace is required for every selector. The label field consists of multiple optional key-value pairs. Pods that match the selectors are scheduled on Fargate. If a to-be-scheduled pod matches any of the selectors in the Fargate profile, then that pod is run on Fargate.

When you create a Fargate profile, you must specify a pod execution role to use with the pods that are scheduled with the profile. This role is added to the clusterâs Kubernetes [Role Based Access Control](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (RBAC) for authorization so that the `kubelet` that is running on the Fargate infrastructure can register with your Amazon EKS cluster so that it can appear in your cluster as a node. The pod execution role also provides IAM permissions to the Fargate infrastructure to allow read access to Amazon ECR image repositories. For more information, see [Pod Execution Role](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html) in the *Amazon EKS User Guide* .

Fargate profiles are immutable. However, you can create a new updated profile to replace an existing profile and then delete the original after the updated profile has finished creating.

If any Fargate profiles in a cluster are in the `DELETING` status, you must wait for that Fargate profile to finish deleting before you can create any other profiles in that cluster.

For more information, see [Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html) in the *Amazon EKS User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/CreateFargateProfile)

## Synopsis

```
create-fargate-profile
--fargate-profile-name <value>
--cluster-name <value>
--pod-execution-role-arn <value>
[--subnets <value>]
[--selectors <value>]
[--client-request-token <value>]
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

`--fargate-profile-name` (string)

The name of the Fargate profile.

`--cluster-name` (string)

The name of your cluster.

`--pod-execution-role-arn` (string)

The Amazon Resource Name (ARN) of the `Pod` execution role to use for a `Pod` that matches the selectors in the Fargate profile. The `Pod` execution role allows Fargate infrastructure to register with your cluster as a node, and it provides read access to Amazon ECR image repositories. For more information, see ` `Pod` execution role <[https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html)>`__ in the *Amazon EKS User Guide* .

`--subnets` (list)

The IDs of subnets to launch a `Pod` into. A `Pod` running on Fargate isnât assigned a public IP address, so only private subnets (with no direct route to an Internet Gateway) are accepted for this parameter.

(string)

Syntax:

```
"string" "string" ...
```

`--selectors` (list)

The selectors to match for a `Pod` to use this Fargate profile. Each selector must have an associated Kubernetes `namespace` . Optionally, you can also specify `labels` for a `namespace` . You may specify up to five selectors in a Fargate profile.

(structure)

An object representing an Fargate profile selector.

namespace -> (string)

The Kubernetes `namespace` that the selector should match.

labels -> (map)

The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.

key -> (string)

value -> (string)

Shorthand Syntax:

```
namespace=string,labels={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "namespace": "string",
    "labels": {"string": "string"
      ...}
  }
  ...
]
```

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--tags` (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**Example 1: Create EKS Fargate Profile for a selector with a namespace**

The following `create-fargate-profile` example creates an EKS Fargate Profile for a selector with a namespace.

```
aws eks create-fargate-profile \
    --cluster-name my-eks-cluster \
    --pod-execution-role-arn arn:aws:iam::111122223333:role/role-name \
    --fargate-profile-name my-fargate-profile \
    --selectors '[{"namespace": "default"}]'
```

Output:

```
{
    "fargateProfile": {
        "fargateProfileName": "my-fargate-profile",
        "fargateProfileArn": "arn:aws:eks:us-east-2:111122223333:fargateprofile/my-eks-cluster/my-fargate-profile/a2c72bca-318e-abe8-8ed1-27c6d4892e9e",
        "clusterName": "my-eks-cluster",
        "createdAt": "2024-03-19T12:38:47.368000-04:00",
        "podExecutionRoleArn": "arn:aws:iam::111122223333:role/role-name",
        "subnets": [
            "subnet-09d912bb63ef21b9a",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-0e2907431c9988b72"
        ],
        "selectors": [
            {
                "namespace": "default"
            }
        ],
        "status": "CREATING",
        "tags": {}
    }
}
```

For more information, see [AWS Fargate profile - Creating a Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html#create-fargate-profile) in the *Amazon EKS User Guide*.

**Example 2: Create EKS Fargate Profile for a selector with a namespace and labels**

The following `create-fargate-profile` example creates an EKS Fargate Profile for a selector with a namespace and labels.

```
aws eks create-fargate-profile \
    --cluster-name my-eks-cluster \
    --pod-execution-role-arn arn:aws:iam::111122223333:role/role-name \
    --fargate-profile-name my-fargate-profile \
    --selectors '[{"namespace": "default", "labels": {"labelname1": "labelvalue1"}}]'
```

Output:

```
{
    "fargateProfile": {
        "fargateProfileName": "my-fargate-profile",
        "fargateProfileArn": "arn:aws:eks:us-east-2:111122223333:fargateprofile/my-eks-cluster/my-fargate-profile/88c72bc7-e8a4-fa34-44e4-2f1397224bb3",
        "clusterName": "my-eks-cluster",
        "createdAt": "2024-03-19T12:33:48.125000-04:00",
        "podExecutionRoleArn": "arn:aws:iam::111122223333:role/role-name",
        "subnets": [
            "subnet-09d912bb63ef21b9a",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-0e2907431c9988b72"
        ],
        "selectors": [
            {
                "namespace": "default",
                "labels": {
                    "labelname1": "labelvalue1"
                }
            }
        ],
        "status": "CREATING",
        "tags": {}
    }
}
```

For more information, see [AWS Fargate profile - Creating a Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html#create-fargate-profile) in the *Amazon EKS User Guide*.

**Example 3: Create EKS Fargate Profile for a selector with a namespace and labels, along with IDs of subnets to launch a Pod into.**

The following `create-fargate-profile` example create EKS Fargate Profile for a selector with a namespace and labels, along with IDs of subnets to launch a Pod into.

```
aws eks create-fargate-profile \
    --cluster-name my-eks-cluster \
    --pod-execution-role-arn arn:aws:iam::111122223333:role/role-name \
    --fargate-profile-name my-fargate-profile \
    --selectors '[{"namespace": "default", "labels": {"labelname1": "labelvalue1"}}]' \
    --subnets '["subnet-09d912bb63ef21b9a", "subnet-04ad87f71c6e5ab4d", "subnet-0e2907431c9988b72"]'
```

Output:

```
{
    "fargateProfile": {
        "fargateProfileName": "my-fargate-profile",
        "fargateProfileArn": "arn:aws:eks:us-east-2:111122223333:fargateprofile/my-eks-cluster/my-fargate-profile/e8c72bc8-e87b-5eb6-57cb-ed4fe57577e3",
        "clusterName": "my-eks-cluster",
        "createdAt": "2024-03-19T12:35:58.640000-04:00",
        "podExecutionRoleArn": "arn:aws:iam::111122223333:role/role-name",
        "subnets": [
            "subnet-09d912bb63ef21b9a",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-0e2907431c9988b72"
        ],
        "selectors": [
            {
                "namespace": "default",
                "labels": {
                    "labelname1": "labelvalue1"
                }
            }
        ],
        "status": "CREATING",
        "tags": {}
    }
}
```

For more information, see [AWS Fargate profile - Creating a Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html#create-fargate-profile) in the *Amazon EKS User Guide*.

**Example 4: Create EKS Fargate Profile for a selector with multiple namespace and labels, along with IDs of subnets to launch a Pod into**

The following `create-fargate-profile` example creates an EKS Fargate Profile for a selector with multiple namespace and labels, along with IDs of subnets to launch a Pod into.

```
aws eks create-fargate-profile \
    --cluster-name my-eks-cluster \
    --pod-execution-role-arn arn:aws:iam::111122223333:role/role-name \
    --fargate-profile-name my-fargate-profile \
    --selectors '[{"namespace": "default1", "labels": {"labelname1": "labelvalue1", "labelname2": "labelvalue2"}}, {"namespace": "default2", "labels": {"labelname1": "labelvalue1", "labelname2": "labelvalue2"}}]' \
    --subnets '["subnet-09d912bb63ef21b9a", "subnet-04ad87f71c6e5ab4d", "subnet-0e2907431c9988b72"]' \
    --tags '{"eks-fargate-profile-key-1": "value-1" , "eks-fargate-profile-key-2": "value-2"}'
```

Output:

```
{
    "fargateProfile": {
        "fargateProfileName": "my-fargate-profile",
        "fargateProfileArn": "arn:aws:eks:us-east-2:111122223333:fargateprofile/my-eks-cluster/my-fargate-profile/4cc72bbf-b766-8ee6-8d29-e62748feb3cd",
        "clusterName": "my-eks-cluster",
        "createdAt": "2024-03-19T12:15:55.271000-04:00",
        "podExecutionRoleArn": "arn:aws:iam::111122223333:role/role-name",
        "subnets": [
            "subnet-09d912bb63ef21b9a",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-0e2907431c9988b72"
        ],
        "selectors": [
            {
                "namespace": "default1",
                "labels": {
                    "labelname2": "labelvalue2",
                    "labelname1": "labelvalue1"
                }
            },
            {
                "namespace": "default2",
                "labels": {
                    "labelname2": "labelvalue2",
                    "labelname1": "labelvalue1"
                }
            }
        ],
        "status": "CREATING",
        "tags": {
            "eks-fargate-profile-key-2": "value-2",
            "eks-fargate-profile-key-1": "value-1"
        }
    }
}
```

For more information, see [AWS Fargate profile - Creating a Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html#create-fargate-profile) in the *Amazon EKS User Guide*.

**Example 5: Create EKS Fargate Profile with a wildcard selector for namespaces and labels, along with IDs of subnets to launch a Pod into**

The following `create-fargate-profile` example creates an EKS Fargate Profile for a selector with multiple namespace and labels, along with IDs of subnets to launch a Pod into.

```
aws eks create-fargate-profile \
    --cluster-name my-eks-cluster \
    --pod-execution-role-arn arn:aws:iam::111122223333:role/role-name \
    --fargate-profile-name my-fargate-profile \
    --selectors '[{"namespace": "prod*", "labels": {"labelname*?": "*value1"}}, {"namespace": "*dev*", "labels": {"labelname*?": "*value*"}}]' \
    --subnets '["subnet-09d912bb63ef21b9a", "subnet-04ad87f71c6e5ab4d", "subnet-0e2907431c9988b72"]' \
    --tags '{"eks-fargate-profile-key-1": "value-1" , "eks-fargate-profile-key-2": "value-2"}'
```

Output:

```
{
    "fargateProfile": {
        "fargateProfileName": "my-fargate-profile",
        "fargateProfileArn": "arn:aws:eks:us-east-2:111122223333:fargateprofile/my-eks-cluster/my-fargate-profile/e8c72bd6-5966-0bfe-b77b-1802893e5a6f",
        "clusterName": "my-eks-cluster",
        "createdAt": "2024-03-19T13:05:20.550000-04:00",
        "podExecutionRoleArn": "arn:aws:iam::111122223333:role/role-name",
        "subnets": [
            "subnet-09d912bb63ef21b9a",
            "subnet-04ad87f71c6e5ab4d",
            "subnet-0e2907431c9988b72"
        ],
        "selectors": [
            {
                "namespace": "prod*",
                "labels": {
                    "labelname*?": "*value1"
                }
            },
            {
                "namespace": "*dev*",
                "labels": {
                    "labelname*?": "*value*"
                }
            }
        ],
        "status": "CREATING",
        "tags": {
            "eks-fargate-profile-key-2": "value-2",
            "eks-fargate-profile-key-1": "value-1"
        }
    }
}
```

For more information, see [AWS Fargate profile - Creating a Fargate profile](https://docs.aws.amazon.com/eks/latest/userguide/fargate-profile.html#create-fargate-profile) in the *Amazon EKS User Guide*.

## Output

fargateProfile -> (structure)

The full description of your new Fargate profile.

fargateProfileName -> (string)

The name of the Fargate profile.

fargateProfileArn -> (string)

The full Amazon Resource Name (ARN) of the Fargate profile.

clusterName -> (string)

The name of your cluster.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

podExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the `Pod` execution role to use for any `Pod` that matches the selectors in the Fargate profile. For more information, see ` `Pod` execution role <[https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html](https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html)>`__ in the *Amazon EKS User Guide* .

subnets -> (list)

The IDs of subnets to launch a `Pod` into.

(string)

selectors -> (list)

The selectors to match for a `Pod` to use this Fargate profile.

(structure)

An object representing an Fargate profile selector.

namespace -> (string)

The Kubernetes `namespace` that the selector should match.

labels -> (map)

The Kubernetes labels that the selector should match. A pod must contain all of the labels that are specified in the selector for it to be considered a match.

key -> (string)

value -> (string)

status -> (string)

The current status of the Fargate profile.

tags -> (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

health -> (structure)

The health status of the Fargate profile. If there are issues with your Fargate profileâs health, they are listed here.

issues -> (list)

Any issues that are associated with the Fargate profile.

(structure)

An issue that is associated with the Fargate profile.

code -> (string)

A brief description of the error.

message -> (string)

The error message associated with the issue.

resourceIds -> (list)

The Amazon Web Services resources that are affected by this issue.

(string)