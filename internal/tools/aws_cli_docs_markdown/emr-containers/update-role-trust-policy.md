# update-role-trust-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/update-role-trust-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/update-role-trust-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-containers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html#cli-aws-emr-containers) ]

# update-role-trust-policy

## Description

Updates the trust policy of given IAM role such that it can be used with Amazon EMR on EKS with the given namespace from the given EKS cluster.

**Note:**:
To use the IAM Role with Amazon EMR on EKS, OIDC identity provider also needs to be created for the EKS cluster.
This can be done using `eksctl utils associate-iam-oidc-provider --cluster <cluster_name> --approve` command.
For information about installing or upgrading eksctl, see [Installing or upgrading eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html#installing-eksctl) in the *Amazon EKS User Guide*.

The command would merge the existing trust policy of the role with the below trust policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::<AWS_ACCOUNT_ID>:oidc-provider/<OIDC_PROVIDER>"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringLike": {
                    "<OIDC_PROVIDER>:sub": "system:serviceaccount:<NAMESPACE>:emr-containers-sa-*-*-<AWS_ACCOUNT_ID>-<BASE36_ENCODED_ROLE_NAME>"
                }
            }
        }
    ]
}
```

Here:

```
<AWS_ACCOUNT_ID> = AWS Account ID of the EKS cluster
<OIDC_PROVIDER> = OIDC Identity Provider for the EKS cluster
<NAMESPACE> = Namespace of the EKS cluster
<BASE36_ENCODED_ROLE_NAME> = Base36 encoded form of the IAM Role name
```

You can use the **âdry-run** option to print the merged trust policy document to stdout instead of updating the role trust policy directly.

## Synopsis

```
update-role-trust-policy
--cluster-name <value>
--namespace <value>
--role-name <value>
[--iam-endpoint <value>]
[--dry-run]
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
Specify the name of the Amazon EKS cluster with which the IAM Role would be used.

`--namespace` (string)
Specify the namespace from the Amazon EKS cluster with which the IAM Role would be used.

`--role-name` (string)
Specify the IAM Role name that you want to usewith Amazon EMR on EKS.

`--iam-endpoint` (string)
The IAM endpoint to call for updating the role trust policy. This is optional and should only bespecified when a custom endpoint should be calledfor IAM operations.

`--dry-run` (boolean)
Print the merged trust policy document tostdout instead of updating the role trustpolicy directly.

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

**To update the trust policy of an IAM Role to be used with Amazon EMR on EKS**

This example command updates the trust policy of a role named **example_iam_role** such that it can be used with Amazon EMR on EKS with
**example_namespace** namespace from an EKS cluster named **example_cluster**.

- Command:

```
aws emr-containers update-role-trust-policy \
    --cluster example_cluster \
    --namespace example_namespace \
    --role-name example_iam_role
```
- Output:

```
If the trust policy has already been updated, then the output will be:
Trust policy statement already exists for role example_iam_role. No
changes were made!

If the trust policy has not been updated yet, then the output will be:
Successfully updated trust policy of role example_iam_role.
```