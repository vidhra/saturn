# update-custom-key-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-custom-key-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/update-custom-key-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# update-custom-key-store

## Description

Changes the properties of a custom key store. You can use this operation to change the properties of an CloudHSM key store or an external key store.

Use the required `CustomKeyStoreId` parameter to identify the custom key store. Use the remaining optional parameters to change its properties. This operation does not return any property values. To verify the updated property values, use the  DescribeCustomKeyStores operation.

This operation is part of the [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) feature in KMS, which combines the convenience and extensive integration of KMS with the isolation and control of a key store that you own and manage.

### Warning

When updating the properties of an external key store, verify that the updated settings connect your key store, via the external key store proxy, to the same external key manager as the previous settings, or to a backup or snapshot of the external key manager with the same cryptographic keys. If the updated connection settings fail, you can fix them and retry, although an extended delay might disrupt Amazon Web Services services. However, if KMS permanently loses its access to cryptographic keys, ciphertext encrypted under those keys is unrecoverable.

### Note

For external key stores:

Some external key managers provide a simpler method for updating an external key store. For details, see your external key manager documentation.

When updating an external key store in the KMS console, you can upload a JSON-based proxy configuration file with the desired values. You cannot upload the proxy configuration file to the `UpdateCustomKeyStore` operation. However, you can use the file to help you determine the correct values for the `UpdateCustomKeyStore` parameters.

For an CloudHSM key store, you can use this operation to change the custom key store friendly name (`NewCustomKeyStoreName` ), to tell KMS about a change to the `kmsuser` crypto user password (`KeyStorePassword` ), or to associate the custom key store with a different, but related, CloudHSM cluster (`CloudHsmClusterId` ). To update any property of an CloudHSM key store, the `ConnectionState` of the CloudHSM key store must be `DISCONNECTED` .

For an external key store, you can use this operation to change the custom key store friendly name (`NewCustomKeyStoreName` ), or to tell KMS about a change to the external key store proxy authentication credentials (`XksProxyAuthenticationCredential` ), connection method (`XksProxyConnectivity` ), external proxy endpoint (`XksProxyUriEndpoint` ) and path (`XksProxyUriPath` ). For external key stores with an `XksProxyConnectivity` of `VPC_ENDPOINT_SERVICE` , you can also update the Amazon VPC endpoint service name (`XksProxyVpcEndpointServiceName` ). To update most properties of an external key store, the `ConnectionState` of the external key store must be `DISCONNECTED` . However, you can update the `CustomKeyStoreName` , `XksProxyAuthenticationCredential` , and `XksProxyUriPath` of an external key store when it is in the CONNECTED or DISCONNECTED state.

If your update requires a `DISCONNECTED` state, before using `UpdateCustomKeyStore` , use the  DisconnectCustomKeyStore operation to disconnect the custom key store. After the `UpdateCustomKeyStore` operation completes, use the  ConnectCustomKeyStore to reconnect the custom key store. To find the `ConnectionState` of the custom key store, use the  DescribeCustomKeyStores operation.

Before updating the custom key store, verify that the new values allow KMS to connect the custom key store to its backing key store. For example, before you change the `XksProxyUriPath` value, verify that the external key store proxy is reachable at the new path.

If the operation succeeds, it returns a JSON object with no properties.

**Cross-account use** : No. You cannot perform this operation on a custom key store in a different Amazon Web Services account.

**Required permissions** : [kms:UpdateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

**Related operations:**

- ConnectCustomKeyStore
- CreateCustomKeyStore
- DeleteCustomKeyStore
- DescribeCustomKeyStores
- DisconnectCustomKeyStore

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateCustomKeyStore)

## Synopsis

```
update-custom-key-store
--custom-key-store-id <value>
[--new-custom-key-store-name <value>]
[--key-store-password <value>]
[--cloud-hsm-cluster-id <value>]
[--xks-proxy-uri-endpoint <value>]
[--xks-proxy-uri-path <value>]
[--xks-proxy-vpc-endpoint-service-name <value>]
[--xks-proxy-authentication-credential <value>]
[--xks-proxy-connectivity <value>]
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

Identifies the custom key store that you want to update. Enter the ID of the custom key store. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.

`--new-custom-key-store-name` (string)

Changes the friendly name of the custom key store to the value that you specify. The custom key store name must be unique in the Amazon Web Services account.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

To change this value, an CloudHSM key store must be disconnected. An external key store can be connected or disconnected.

`--key-store-password` (string)

Enter the current password of the `kmsuser` crypto user (CU) in the CloudHSM cluster that is associated with the custom key store. This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM` .

This parameter tells KMS the current password of the `kmsuser` crypto user (CU). It does not set or change the password of any users in the CloudHSM cluster.

To change this value, the CloudHSM key store must be disconnected.

`--cloud-hsm-cluster-id` (string)

Associates the custom key store with a related CloudHSM cluster. This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM` .

Enter the cluster ID of the cluster that you used to create the custom key store or a cluster that shares a backup history and has the same cluster certificate as the original cluster. You cannot use this parameter to associate a custom key store with an unrelated cluster. In addition, the replacement cluster must [fulfill the requirements](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) for a cluster associated with a custom key store. To view the cluster certificate of a cluster, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation.

To change this value, the CloudHSM key store must be disconnected.

`--xks-proxy-uri-endpoint` (string)

Changes the URI endpoint that KMS uses to connect to your external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

For external key stores with an `XksProxyConnectivity` value of `PUBLIC_ENDPOINT` , the protocol must be HTTPS.

For external key stores with an `XksProxyConnectivity` value of `VPC_ENDPOINT_SERVICE` , specify `https://` followed by the private DNS name associated with the VPC endpoint service. Each external key store must use a different private DNS name.

The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the Amazon Web Services account and Region.

To change this value, the external key store must be disconnected.

`--xks-proxy-uri-path` (string)

Changes the base path to the proxy APIs for this external key store. To find this value, see the documentation for your external key manager and external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

The value must start with `/` and must end with `/kms/xks/v1` , where `v1` represents the version of the KMS external key store proxy API. You can include an optional prefix between the required elements such as `/*example* /kms/xks/v1` .

The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the Amazon Web Services account and Region.

You can change this value when the external key store is connected or disconnected.

`--xks-proxy-vpc-endpoint-service-name` (string)

Changes the name that KMS uses to identify the Amazon VPC endpoint service for your external key store proxy (XKS proxy). This parameter is valid when the `CustomKeyStoreType` is `EXTERNAL_KEY_STORE` and the `XksProxyConnectivity` is `VPC_ENDPOINT_SERVICE` .

To change this value, the external key store must be disconnected.

`--xks-proxy-authentication-credential` (structure)

Changes the credentials that KMS uses to sign requests to the external key store proxy (XKS proxy). This parameter is valid only for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

You must specify both the `AccessKeyId` and `SecretAccessKey` value in the authentication credential, even if you are only updating one value.

This parameter doesnât establish or change your authentication credentials on the proxy. It just tells KMS the credential that you established with your external key store proxy. For example, if you rotate the credential on your external key store proxy, you can use this parameter to update the credential in KMS.

You can change this value when the external key store is connected or disconnected.

AccessKeyId -> (string)

A unique identifier for the raw secret access key.

RawSecretAccessKey -> (string)

A secret string of 43-64 characters. Valid characters are a-z, A-Z, 0-9, /, +, and =.

Shorthand Syntax:

```
AccessKeyId=string,RawSecretAccessKey=string
```

JSON Syntax:

```
{
  "AccessKeyId": "string",
  "RawSecretAccessKey": "string"
}
```

`--xks-proxy-connectivity` (string)

Changes the connectivity setting for the external key store. To indicate that the external key store proxy uses a Amazon VPC endpoint service to communicate with KMS, specify `VPC_ENDPOINT_SERVICE` . Otherwise, specify `PUBLIC_ENDPOINT` .

If you change the `XksProxyConnectivity` to `VPC_ENDPOINT_SERVICE` , you must also change the `XksProxyUriEndpoint` and add an `XksProxyVpcEndpointServiceName` value.

If you change the `XksProxyConnectivity` to `PUBLIC_ENDPOINT` , you must also change the `XksProxyUriEndpoint` and specify a null or empty string for the `XksProxyVpcEndpointServiceName` value.

To change this value, the external key store must be disconnected.

Possible values:

- `PUBLIC_ENDPOINT`
- `VPC_ENDPOINT_SERVICE`

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

**Example 1: To edit the friendly name of a custom key store**

The following `update-custom-key-store` example changes the name of the custom key store. This example works for an AWS CloudHSM key store or an external key store.

Use the `custom-key-store-id` to identify the key store. Use the `new-custom-key-store-name` parameter to specify the new friendly name.

To update the friendly name of an AWS CloudHSM key store, you must first disconnect the key store, such as by using the `disconnect-custom-key-store` command. You can update the friendly name of an external key store while it is connected or disconnected. To find the connection state of your custom key store, use the `describe-custom-key-store` command.

```
aws kms update-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0 \
    --new-custom-key-store-name ExampleKeyStore
```

This command does not return any data. To verify that the command worked, use a `describe-custom-key-stores` command.

For more information about updating an AWS CloudHSM key store, see [Editing AWS CloudHSM key store settings](https://docs.aws.amazon.com/kms/latest/developerguide/update-keystore.html) in the *AWS Key Management Service Developer Guide*.

For more information about updating an external key store, see [Editing external key store properties](https://docs.aws.amazon.com/kms/latest/developerguide/update-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 2: To edit the kmsuser password of an AWS CloudHSM key store**

The following `update-custom-key-store` example updates the value of the `kmsuser` password to the current password for the `kmsuser` in the CloudHSM cluster associated with the specified key store. This command doesnât change the `kmsuser` password it the cluster. It just tells AWS KMS the current password. If KMS doesnât have the current `kmsuser` password, it cannot connect to the AWS CloudHSM key store.

**NOTE:** Before updating an AWS CloudHSM key store, you must disconnect it. Use the `disconnect-custom-key-store` command. After the command completes, you can reconnect the AWS CloudHSM key store. Use the `connect-custom-key-store` command.

```
aws kms update-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0 \
    --key-store-password ExamplePassword
```

This command does not return any output. To verify that the change was effective, use a `describe-custom-key-stores` command.

For more information about updating an AWS CloudHSM key store, see [Editing AWS CloudHSM key store settings](https://docs.aws.amazon.com/kms/latest/developerguide/update-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 3: To edit the AWS CloudHSM cluster of an AWS CloudHSM key store**

The following example changes the AWS CloudHSM cluster that is associated with an AWS CloudHSM key store to a related cluster, such as a different backup of the same cluster.

**NOTE:** Before updating an AWS CloudHSM key store, you must disconnect it. Use the `disconnect-custom-key-store` command. After the command completes, you can reconnect the AWS CloudHSM key store. Use the `connect-custom-key-store` command.

```
aws kms update-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0 \
    --cloud-hsm-cluster-id cluster-1a23b4cdefg
```

This command does not return any output. To verify that the change was effective, use a `describe-custom-key-stores` command.

For more information about updating an AWS CloudHSM key store, see [Editing AWS CloudHSM key store settings](https://docs.aws.amazon.com/kms/latest/developerguide/update-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 4: To edit the proxy authentication credential of an external key store**

The following example updates the proxy authentication credential for your external key store. You must specify both the `raw-secret-access-key` and the `access-key-id`, even if you are changing only one of the values. You can use this feature to fix an invalid credential or to change the credential when the external key store proxy rotates it.

Establish the proxy authentication credential for AWS KMS on your external key store. Then use this command to provide the credential to AWS KMS. AWS KMS uses this credential to sign its requests to your external key store proxy.

You can update the proxy authentication credential while the external key store is connected or disconnected. To find the connection state of your custom key store, use the `describe-custom-key-store` command.

```
aws kms update-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0 \
    --xks-proxy-authentication-credential "AccessKeyId=ABCDE12345670EXAMPLE, RawSecretAccessKey=DXjSUawnel2fr6SKC7G25CNxTyWKE5PF9XX6H/u9pSo="
```

This command does not return any output. To verify that the change was effective, use a `describe-custom-key-stores` command.

For more information about updating an external key store, see [Editing external key store properties](https://docs.aws.amazon.com/kms/latest/developerguide/update-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 5: To edit the proxy connectivity of an external key store**

The following example changes the external key store proxy connectivity option from public endpoint connectivity to VPC endpoint service connectivity. In addition to changing the `xks-proxy-connectivity` value, you must change the `xks-proxy-uri-endpoint` value to reflect the private DNS name associated with the VPC endpoint service. You must also add an `xks-proxy-vpc-endpoint-service-name` value.

**NOTE:** Before updating the proxy connectivity of an external store, you must disconnect it. Use the `disconnect-custom-key-store` command. After the command completes, you can reconnect the external key store by using the `connect-custom-key-store` command.

```
aws kms update-custom-key-store \
    --custom-key-store-id cks-1234567890abcdef0 \
    --xks-proxy-connectivity VPC_ENDPOINT_SERVICE \
    --xks-proxy-uri-endpoint "https://myproxy-private.xks.example.com" \
    --xks-proxy-vpc-endpoint-service-name "com.amazonaws.vpce.us-east-1.vpce-svc-example"
```

This command does not return any output. To verify that the change was effective, use a `describe-custom-key-stores` command.

For more information about updating an external key store, see [Editing external key store properties](https://docs.aws.amazon.com/kms/latest/developerguide/update-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

## Output

None