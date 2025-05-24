# update-addonÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-addon.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/update-addon.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# update-addon

## Description

Updates an Amazon EKS add-on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/UpdateAddon)

## Synopsis

```
update-addon
--cluster-name <value>
--addon-name <value>
[--addon-version <value>]
[--service-account-role-arn <value>]
[--resolve-conflicts <value>]
[--client-request-token <value>]
[--configuration-values <value>]
[--pod-identity-associations <value>]
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

`--addon-version` (string)

The version of the add-on. The version must match one of the versions returned by ` `DescribeAddonVersions` [https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeAddonVersions).html`__ .

`--service-account-role-arn` (string)

The Amazon Resource Name (ARN) of an existing IAM role to bind to the add-onâs service account. The role must be assigned the IAM permissions required by the add-on. If you donât specify an existing IAM role, then the add-on uses the permissions assigned to the node IAM role. For more information, see [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) in the *Amazon EKS User Guide* .

### Note

To specify an existing IAM role, you must have an IAM OpenID Connect (OIDC) provider created for your cluster. For more information, see [Enabling IAM roles for service accounts on your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html) in the *Amazon EKS User Guide* .

`--resolve-conflicts` (string)

How to resolve field value conflicts for an Amazon EKS add-on if youâve changed a value from the Amazon EKS default value. Conflicts are handled based on the option you choose:

- **None** â Amazon EKS doesnât change the value. The update might fail.
- **Overwrite** â Amazon EKS overwrites the changed value back to the Amazon EKS default value.
- **Preserve** â Amazon EKS preserves the value. If you choose this option, we recommend that you test any field and value changes on a non-production cluster before updating the add-on on your production cluster.

Possible values:

- `OVERWRITE`
- `NONE`
- `PRESERVE`

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--configuration-values` (string)

The set of configuration values for the add-on thatâs created. The values that you provide are validated against the schema returned by `DescribeAddonConfiguration` .

`--pod-identity-associations` (list)

An array of Pod Identity Assocations to be updated. Each EKS Pod Identity association maps a Kubernetes service account to an IAM Role. If this value is left blank, no change. If an empty array is provided, existing Pod Identity Assocations owned by the Addon are deleted.

For more information, see [Attach an IAM Role to an Amazon EKS add-on using Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide* .

(structure)

A type of Pod Identity Association owned by an Amazon EKS Add-on.

Each EKS Pod Identity Association maps a role to a service account in a namespace in the cluster.

For more information, see [Attach an IAM Role to an Amazon EKS add-on using Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/add-ons-iam.html) in the *Amazon EKS User Guide* .

serviceAccount -> (string)

The name of a Kubernetes Service Account.

roleArn -> (string)

The ARN of an IAM Role.

Shorthand Syntax:

```
serviceAccount=string,roleArn=string ...
```

JSON Syntax:

```
[
  {
    "serviceAccount": "string",
    "roleArn": "string"
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

**Example 1. To update an Amazon EKS add-on with service account role ARN**

The following `update-addon` example command updates an Amazon EKS add-on with service account role ARN.

```
aws eks update-addon \
    --cluster-name my-eks-cluster \
    --addon-name vpc-cni \
    --service-account-role-arn arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm
```

Output:

```
{
    "update": {
        "id": "c00d2de2-c2e4-3d30-929e-46b8edec2ce4",
        "status": "InProgress",
        "type": "AddonUpdate",
        "params": [
            {
                "type": "ServiceAccountRoleArn",
                "value": "arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm"
            }
        ],
        "updatedAt": "2024-04-12T16:04:55.614000-04:00",
        "errors": []
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Updating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#updating-an-add-on) in the *Amazon EKS User Guide*.

**Example 2. To update an Amazon EKS add-on with specific add-on version**

The following `update-addon` example command updates an Amazon EKS add-on with specific add-on version.

```
aws eks update-addon \
    --cluster-name my-eks-cluster \
    --addon-name vpc-cni \
    --service-account-role-arn arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm \
    --addon-version v1.16.4-eksbuild.2
```

Output:

```
{
    "update": {
        "id": "f58dc0b0-2b18-34bd-bc6a-e4abc0011f36",
        "status": "InProgress",
        "type": "AddonUpdate",
        "params": [
            {
                "type": "AddonVersion",
                "value": "v1.16.4-eksbuild.2"
            },
            {
                "type": "ServiceAccountRoleArn",
                "value": "arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm"
            }
        ],
        "createdAt": "2024-04-12T16:07:16.550000-04:00",
        "errors": []
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Updating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#updating-an-add-on) in the *Amazon EKS User Guide*.

**Example 3. To update an Amazon EKS add-on with custom configuration values and resolve conflicts details**

The following `update-addon` example command updates an Amazon EKS add-on with custom configuration values and resolve conflicts details.

```
aws eks update-addon \
    --cluster-name my-eks-cluster \
    --addon-name vpc-cni \
    --service-account-role-arn arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm \
    --addon-version v1.16.4-eksbuild.2 \
    --configuration-values '{"resources": {"limits":{"cpu":"100m"}, "requests":{"cpu":"50m"}}}' \
    --resolve-conflicts PRESERVE
```

Output:

```
{
    "update": {
        "id": "cd9f2173-a8d8-3004-a90f-032f14326520",
        "status": "InProgress",
        "type": "AddonUpdate",
        "params": [
            {
                "type": "AddonVersion",
                "value": "v1.16.4-eksbuild.2"
            },
            {
                "type": "ServiceAccountRoleArn",
                "value": "arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm"
            },
            {
                "type": "ResolveConflicts",
                "value": "PRESERVE"
            },
            {
                "type": "ConfigurationValues",
                "value": "{\"resources\": {\"limits\":{\"cpu\":\"100m\"}, \"requests\":{\"cpu\":\"50m\"}}}"
            }
        ],
        "createdAt": "2024-04-12T16:16:27.363000-04:00",
        "errors": []
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Updating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#updating-an-add-on) in the *Amazon EKS User Guide*.

**Example 4. To update an Amazon EKS add-on with custom JSON configuration values file**

The following `update-addon` example command updates an Amazon EKS add-on with custom JSON configuration values and resolve conflicts details.

```
aws eks update-addon \
    --cluster-name my-eks-cluster \
    --addon-name vpc-cni \
    --service-account-role-arn arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm \
    --addon-version v1.17.1-eksbuild.1 \
    --configuration-values 'file://configuration-values.json' \
    --resolve-conflicts PRESERVE
```

Contents of `configuration-values.json`:

```
{
    "resources": {
        "limits": {
            "cpu": "100m"
        },
        "requests": {
            "cpu": "50m"
        }
    },
    "env": {
        "AWS_VPC_K8S_CNI_LOGLEVEL": "ERROR"
    }
}
```

Output:

```
{
    "update": {
        "id": "6881a437-174f-346b-9a63-6e91763507cc",
        "status": "InProgress",
        "type": "AddonUpdate",
        "params": [
            {
                "type": "AddonVersion",
                "value": "v1.17.1-eksbuild.1"
            },
            {
                "type": "ServiceAccountRoleArn",
                "value": "arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm"
            },
            {
                "type": "ResolveConflicts",
                "value": "PRESERVE"
            },
            {
                "type": "ConfigurationValues",
                "value": "{\n    \"resources\": {\n        \"limits\": {\n            \"cpu\": \"100m\"\n        },\n        \"requests\": {\n            \"cpu\": \"50m\"\n        }\n    },\n    \"env\": {\n        \"AWS_VPC_K8S_CNI_LOGLEVEL\": \"ERROR\"\n    }\n}"
            }
        ],
        "createdAt": "2024-04-12T16:22:55.519000-04:00",
        "errors": []
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Updating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#updating-an-add-on) in the *Amazon EKS User Guide*.

**Example 5. To update an Amazon EKS add-on with custom YAML configuration values file**

The following `update-addon` example command updates an Amazon EKS add-on with custom YAML configuration values and resolve conflicts details.

```
aws eks update-addon \
    --cluster-name my-eks-cluster \
    --addon-name vpc-cni \
    --service-account-role-arn arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm \
    --addon-version v1.18.0-eksbuild.1 \
    --configuration-values 'file://configuration-values.yaml' \
    --resolve-conflicts PRESERVE
```

Contents of `configuration-values.yaml`:

```
resources:
    limits:
        cpu: '100m'
    requests:
        cpu: '50m'
env:
    AWS_VPC_K8S_CNI_LOGLEVEL: 'DEBUG'
```

Output:

```
{
    "update": {
        "id": "a067a4c9-69d0-3769-ace9-d235c5b16701",
        "status": "InProgress",
        "type": "AddonUpdate",
        "params": [
            {
                "type": "AddonVersion",
                "value": "v1.18.0-eksbuild.1"
            },
            {
                "type": "ServiceAccountRoleArn",
                "value": "arn:aws:iam::111122223333:role/eksctl-my-eks-cluster-addon-vpc-cni-Role1-YfakrqOC1UTm"
            },
            {
                "type": "ResolveConflicts",
                "value": "PRESERVE"
            },
            {
                "type": "ConfigurationValues",
                "value": "resources:\n    limits:\n        cpu: '100m'\n    requests:\n        cpu: '50m'\nenv:\n    AWS_VPC_K8S_CNI_LOGLEVEL: 'DEBUG'"
            }
        ],
        "createdAt": "2024-04-12T16:25:07.212000-04:00",
        "errors": []
    }
}
```

For more information, see [Managing Amazon EKS add-ons - Updating an add-on](https://docs.aws.amazon.com/eks/latest/userguide/managing-add-ons.html#updating-an-add-on) in the *Amazon EKS User Guide*.

## Output

update -> (structure)

An object representing an asynchronous update.

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