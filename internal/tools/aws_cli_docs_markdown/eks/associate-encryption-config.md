# associate-encryption-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/associate-encryption-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/associate-encryption-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# associate-encryption-config

## Description

Associates an encryption configuration to an existing cluster.

Use this API to enable encryption on existing clusters that donât already have encryption enabled. This allows you to implement a defense-in-depth security strategy without migrating applications to new Amazon EKS clusters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/AssociateEncryptionConfig)

## Synopsis

```
associate-encryption-config
--cluster-name <value>
--encryption-config <value>
[--client-request-token <value>]
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

`--encryption-config` (list)

The configuration you are using for encryption.

(structure)

The encryption configuration for the cluster.

resources -> (list)

Specifies the resources to be encrypted. The only supported value is `secrets` .

(string)

provider -> (structure)

Key Management Service (KMS) key. Either the ARN or the alias can be used.

keyArn -> (string)

Amazon Resource Name (ARN) or alias of the KMS key. The KMS key must be symmetric and created in the same Amazon Web Services Region as the cluster. If the KMS key was created in a different account, the [IAM principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) must have access to the KMS key. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the *Key Management Service Developer Guide* .

Shorthand Syntax:

```
resources=string,string,provider={keyArn=string} ...
```

JSON Syntax:

```
[
  {
    "resources": ["string", ...],
    "provider": {
      "keyArn": "string"
    }
  }
  ...
]
```

`--client-request-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

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

**To associates an encryption configuration to an existing cluster**

The following `associate-encryption-config` example enableâs encryption on an existing EKS clusters that do not already have encryption enabled.

```
aws eks associate-encryption-config \
    --cluster-name my-eks-cluster \
    --encryption-config '[{"resources":["secrets"],"provider":{"keyArn":"arn:aws:kms:region-code:account:key/key"}}]'
```

Output:

```
{
    "update": {
        "id": "3141b835-8103-423a-8e68-12c2521ffa4d",
        "status": "InProgress",
        "type": "AssociateEncryptionConfig",
        "params": [
            {
                "type": "EncryptionConfig",
                "value": "[{\"resources\":[\"secrets\"],\"provider\":{\"keyArn\":\"arn:aws:kms:region-code:account:key/key\"}}]"
            }
        ],
        "createdAt": "2024-03-14T11:01:26.297000-04:00",
        "errors": []
    }
}
```

For more information, see [Enabling secret encryption on an existing cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-kms.html) in the *Amazon EKS User Guide*.

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