# update-access-entryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-access-entry.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-access-entry.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# update-access-entry

## Description

Updates an access entry.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateAccessEntry)

## Synopsis

```
update-access-entry
--cluster-name <value>
--principal-arn <value>
[--kubernetes-groups <value>]
[--client-request-token <value>]
[--username <value>]
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

`--principal-arn` (string)

The ARN of the IAM principal for the `AccessEntry` .

`--kubernetes-groups` (list)

The value for `name` that youâve specified for `kind: Group` as a `subject` in a Kubernetes `RoleBinding` or `ClusterRoleBinding` object. Amazon EKS doesnât confirm that the value for `name` exists in any bindings on your cluster. You can specify one or more names.

Kubernetes authorizes the `principalArn` of the access entry to access any cluster objects that youâve specified in a Kubernetes `Role` or `ClusterRole` object that is also specified in a bindingâs `roleRef` . For more information about creating Kubernetes `RoleBinding` , `ClusterRoleBinding` , `Role` , or `ClusterRole` objects, see [Using RBAC Authorization in the Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) .

If you want Amazon EKS to authorize the `principalArn` (instead of, or in addition to Kubernetes authorizing the `principalArn` ), you can associate one or more access policies to the access entry using `AssociateAccessPolicy` . If you associate any access policies, the `principalARN` has all permissions assigned in the associated access policies and all permissions in any Kubernetes `Role` or `ClusterRole` objects that the group names are bound to.

(string)

Syntax:

```
"string" "string" ...
```

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--username` (string)

The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see [Creating access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries) in the *Amazon EKS User Guide* .

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

accessEntry -> (structure)

The ARN of the IAM principal for the `AccessEntry` .

clusterName -> (string)

The name of your cluster.

principalArn -> (string)

The ARN of the IAM principal for the access entry. If you ever delete the IAM principal with this ARN, the access entry isnât automatically deleted. We recommend that you delete the access entry with an ARN for an IAM principal that you delete. If you donât delete the access entry and ever recreate the IAM principal, even if it has the same ARN, the access entry wonât work. This is because even though the ARN is the same for the recreated IAM principal, the `roleID` or `userID` (you can see this with the Security Token Service `GetCallerIdentity` API) is different for the recreated IAM principal than it was for the original IAM principal. Even though you donât see the IAM principalâs `roleID` or `userID` for an access entry, Amazon EKS stores it with the access entry.

kubernetesGroups -> (list)

A `name` that youâve specified in a Kubernetes `RoleBinding` or `ClusterRoleBinding` object so that Kubernetes authorizes the `principalARN` access to cluster objects.

(string)

accessEntryArn -> (string)

The ARN of the access entry.

createdAt -> (timestamp)

The Unix epoch timestamp at object creation.

modifiedAt -> (timestamp)

The Unix epoch timestamp for the last modification to the object.

tags -> (map)

Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags donât propagate to any other cluster or Amazon Web Services resources.

key -> (string)

One part of a key-value pair that make up a tag. A `key` is a general label that acts like a category for more specific tag values.

value -> (string)

The optional part of a key-value pair that make up a tag. A `value` acts as a descriptor within a tag category (key).

username -> (string)

The `name` of a user that can authenticate to your cluster.

type -> (string)

The type of the access entry.