# disconnect-custom-key-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disconnect-custom-key-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/disconnect-custom-key-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# disconnect-custom-key-store

## Description

Disconnects the [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) from its backing key store. This operation disconnects an CloudHSM key store from its associated CloudHSM cluster or disconnects an external key store from the external key store proxy that communicates with your external key manager.

This operation is part of the [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) feature in KMS, which combines the convenience and extensive integration of KMS with the isolation and control of a key store that you own and manage.

While a custom key store is disconnected, you can manage the custom key store and its KMS keys, but you cannot create or use its KMS keys. You can reconnect the custom key store at any time.

### Note

While a custom key store is disconnected, all attempts to create KMS keys in the custom key store or to use existing KMS keys in [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) will fail. This action can prevent users from storing and accessing sensitive data.

When you disconnect a custom key store, its `ConnectionState` changes to `Disconnected` . To find the connection state of a custom key store, use the  DescribeCustomKeyStores operation. To reconnect a custom key store, use the  ConnectCustomKeyStore operation.

If the operation succeeds, it returns a JSON object with no properties.

**Cross-account use** : No. You cannot perform this operation on a custom key store in a different Amazon Web Services account.

**Required permissions** : [kms:DisconnectCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

**Related operations:**

- ConnectCustomKeyStore
- CreateCustomKeyStore
- DeleteCustomKeyStore
- DescribeCustomKeyStores
- UpdateCustomKeyStore

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisconnectCustomKeyStore)

## Synopsis

```
disconnect-custom-key-store
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

Enter the ID of the custom key store you want to disconnect. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.

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

**To disconnect a custom key store**

The following `disconnect-custom-key-store` example disconnects a custom key store from its AWS CloudHSM cluster. You might disconnect a key store to troubleshoot a problem, to update its settings, or to prevent KMS keys in the keystore from being used in cryptographic operations.

This command is the same for all custom key stores, including AWS CloudHSM key stores and external key stores.

Before running this command, replace the example custom key store ID with a valid one.

```
$ aws kms disconnect-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0
```

This command produces no output.  verify that the command was effective, use the `describe-custom-key-stores` command.

For more information about disconnecting an AWS CloudHSM key store, see [Connecting and disconnecting an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/disconnect-keystore.html) in the *AWS Key Management Service Developer Guide*.

For more information about disconnecting an external key store, see [Connecting and disconnecting an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/xks-connect-disconnect.html) in the *AWS Key Management Service Developer Guide*.

## Output

None