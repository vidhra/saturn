# connect-custom-key-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/connect-custom-key-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/connect-custom-key-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# connect-custom-key-store

## Description

Connects or reconnects a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) to its backing key store. For an CloudHSM key store, `ConnectCustomKeyStore` connects the key store to its associated CloudHSM cluster. For an external key store, `ConnectCustomKeyStore` connects the key store to the external key store proxy that communicates with your external key manager.

The custom key store must be connected before you can create KMS keys in the key store or use the KMS keys it contains. You can disconnect and reconnect a custom key store at any time.

The connection process for a custom key store can take an extended amount of time to complete. This operation starts the connection process, but it does not wait for it to complete. When it succeeds, this operation quickly returns an HTTP 200 response and a JSON object with no properties. However, this response does not indicate that the custom key store is connected. To get the connection state of the custom key store, use the  DescribeCustomKeyStores operation.

This operation is part of the [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) feature in KMS, which combines the convenience and extensive integration of KMS with the isolation and control of a key store that you own and manage.

The `ConnectCustomKeyStore` operation might fail for various reasons. To find the reason, use the  DescribeCustomKeyStores operation and see the `ConnectionErrorCode` in the response. For help interpreting the `ConnectionErrorCode` , see  CustomKeyStoresListEntry .

To fix the failure, use the  DisconnectCustomKeyStore operation to disconnect the custom key store, correct the error, use the  UpdateCustomKeyStore operation if necessary, and then use `ConnectCustomKeyStore` again.

**CloudHSM key store**

During the connection process for an CloudHSM key store, KMS finds the CloudHSM cluster that is associated with the custom key store, creates the connection infrastructure, connects to the cluster, logs into the CloudHSM client as the `kmsuser` CU, and rotates its password.

To connect an CloudHSM key store, its associated CloudHSM cluster must have at least one active HSM. To get the number of active HSMs in a cluster, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation. To add HSMs to the cluster, use the [CreateHsm](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html) operation. Also, the ` `kmsuser` crypto user <[https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser)>`__ (CU) must not be logged into the cluster. This prevents KMS from using this account to log in.

If you are having trouble connecting or disconnecting a CloudHSM key store, see [Troubleshooting an CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the *Key Management Service Developer Guide* .

**External key store**

When you connect an external key store that uses public endpoint connectivity, KMS tests its ability to communicate with your external key manager by sending a request via the external key store proxy.

When you connect to an external key store that uses VPC endpoint service connectivity, KMS establishes the networking elements that it needs to communicate with your external key manager via the external key store proxy. This includes creating an interface endpoint to the VPC endpoint service and a private hosted zone for traffic between KMS and the VPC endpoint service.

To connect an external key store, KMS must be able to connect to the external key store proxy, the external key store proxy must be able to communicate with your external key manager, and the external key manager must be available for cryptographic operations.

If you are having trouble connecting or disconnecting an external key store, see [Troubleshooting an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : No. You cannot perform this operation on a custom key store in a different Amazon Web Services account.

**Required permissions** : [kms:ConnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

**Related operations**

- CreateCustomKeyStore
- DeleteCustomKeyStore
- DescribeCustomKeyStores
- DisconnectCustomKeyStore
- UpdateCustomKeyStore

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ConnectCustomKeyStore)

## Synopsis

```
connect-custom-key-store
--custom-key-store-id <value>
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

`--custom-key-store-id` (string)

Enter the key store ID of the custom key store that you want to connect. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.

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

**To connect a custom key store**

The following `connect-custom-key-store` example reconnects the specified custom key store. You can use a command like this one to connect a custom key store for the first time or to reconnect a key store that was disconnected.

You can use this command to connect an AWS CloudHSM key store or an external key store.

```
aws kms connect-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0
```

This command does not return any output. To verify that the command was effective, use the `describe-custom-key-stores` command.

For information about connecting an AWS CloudHSM key store, see [Connecting and disconnecting an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/disconnect-keystore.html) in the *AWS Key Management Service Developer Guide*.

For information about connecting an external key store, see [Connecting and disconnecting an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/xks-connect-disconnect.html) in the *AWS Key Management Service Developer Guide*.

## Output

None