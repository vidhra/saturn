# create-custom-key-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-custom-key-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-custom-key-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# create-custom-key-store

## Description

Creates a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) backed by a key store that you own and manage. When you use a KMS key in a custom key store for a cryptographic operation, the cryptographic operation is actually performed in your key store using your keys. KMS supports [CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) backed by an [CloudHSM cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html) and [external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) backed by an external key store proxy and external key manager outside of Amazon Web Services.

This operation is part of the [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) feature in KMS, which combines the convenience and extensive integration of KMS with the isolation and control of a key store that you own and manage.

Before you create the custom key store, the required elements must be in place and operational. We recommend that you use the test tools that KMS provides to verify the configuration your external key store proxy. For details about the required elements and verification tests, see [Assemble the prerequisites (for CloudHSM key stores)](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore) or [Assemble the prerequisites (for external key stores)](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keystore.html#xks-requirements) in the *Key Management Service Developer Guide* .

To create a custom key store, use the following parameters.

- To create an CloudHSM key store, specify the `CustomKeyStoreName` , `CloudHsmClusterId` , `KeyStorePassword` , and `TrustAnchorCertificate` . The `CustomKeyStoreType` parameter is optional for CloudHSM key stores. If you include it, set it to the default value, `AWS_CLOUDHSM` . For help with failures, see [Troubleshooting an CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the *Key Management Service Developer Guide* .
- To create an external key store, specify the `CustomKeyStoreName` and a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` . Also, specify values for `XksProxyConnectivity` , `XksProxyAuthenticationCredential` , `XksProxyUriEndpoint` , and `XksProxyUriPath` . If your `XksProxyConnectivity` value is `VPC_ENDPOINT_SERVICE` , specify the `XksProxyVpcEndpointServiceName` parameter. For help with failures, see [Troubleshooting an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html) in the *Key Management Service Developer Guide* .

### Note

For external key stores:

Some external key managers provide a simpler method for creating an external key store. For details, see your external key manager documentation.

When creating an external key store in the KMS console, you can upload a JSON-based proxy configuration file with the desired values. You cannot use a proxy configuration with the `CreateCustomKeyStore` operation. However, you can use the values in the file to help you determine the correct values for the `CreateCustomKeyStore` parameters.

When the operation completes successfully, it returns the ID of the new custom key store. Before you can use your new custom key store, you need to use the  ConnectCustomKeyStore operation to connect a new CloudHSM key store to its CloudHSM cluster, or to connect a new external key store to the external key store proxy for your external key manager. Even if you are not going to use your custom key store immediately, you might want to connect it to verify that all settings are correct and then disconnect it until you are ready to use it.

For help with failures, see [Troubleshooting a custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : No. You cannot perform this operation on a custom key store in a different Amazon Web Services account.

**Required permissions** : [kms:CreateCustomKeyStore](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy).

**Related operations:**

- ConnectCustomKeyStore
- DeleteCustomKeyStore
- DescribeCustomKeyStores
- DisconnectCustomKeyStore
- UpdateCustomKeyStore

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateCustomKeyStore)

## Synopsis

```
create-custom-key-store
--custom-key-store-name <value>
[--cloud-hsm-cluster-id <value>]
[--trust-anchor-certificate <value>]
[--key-store-password <value>]
[--custom-key-store-type <value>]
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

`--custom-key-store-name` (string)

Specifies a friendly name for the custom key store. The name must be unique in your Amazon Web Services account and Region. This parameter is required for all custom key stores.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

`--cloud-hsm-cluster-id` (string)

Identifies the CloudHSM cluster for an CloudHSM key store. This parameter is required for custom key stores with `CustomKeyStoreType` of `AWS_CLOUDHSM` .

Enter the cluster ID of any active CloudHSM cluster that is not already associated with a custom key store. To find the cluster ID, use the [DescribeClusters](https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html) operation.

`--trust-anchor-certificate` (string)

Specifies the certificate for an CloudHSM key store. This parameter is required for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM` .

Enter the content of the trust anchor certificate for the CloudHSM cluster. This is the content of the `customerCA.crt` file that you created when you [initialized the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html) .

`--key-store-password` (string)

Specifies the `kmsuser` password for an CloudHSM key store. This parameter is required for custom key stores with a `CustomKeyStoreType` of `AWS_CLOUDHSM` .

Enter the password of the ` `kmsuser` crypto user (CU) account <[https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser)>`__ in the specified CloudHSM cluster. KMS logs into the cluster as this user to manage key material on your behalf.

The password must be a string of 7 to 32 characters. Its value is case sensitive.

This parameter tells KMS the `kmsuser` account password; it does not change the password in the CloudHSM cluster.

`--custom-key-store-type` (string)

Specifies the type of custom key store. The default value is `AWS_CLOUDHSM` .

For a custom key store backed by an CloudHSM cluster, omit the parameter or enter `AWS_CLOUDHSM` . For a custom key store backed by an external key manager outside of Amazon Web Services, enter `EXTERNAL_KEY_STORE` . You cannot change this property after the key store is created.

Possible values:

- `AWS_CLOUDHSM`
- `EXTERNAL_KEY_STORE`

`--xks-proxy-uri-endpoint` (string)

Specifies the endpoint that KMS uses to send requests to the external key store proxy (XKS proxy). This parameter is required for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

The protocol must be HTTPS. KMS communicates on port 443. Do not specify the port in the `XksProxyUriEndpoint` value.

For external key stores with `XksProxyConnectivity` value of `VPC_ENDPOINT_SERVICE` , specify `https://` followed by the private DNS name of the VPC endpoint service.

For external key stores with `PUBLIC_ENDPOINT` connectivity, this endpoint must be reachable before you create the custom key store. KMS connects to the external key store proxy while creating the custom key store. For external key stores with `VPC_ENDPOINT_SERVICE` connectivity, KMS connects when you call the  ConnectCustomKeyStore operation.

The value of this parameter must begin with `https://` . The remainder can contain upper and lower case letters (A-Z and a-z), numbers (0-9), dots (`.` ), and hyphens (`-` ). Additional slashes (`/` and `\` ) are not permitted.

**Uniqueness requirements:**

- The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the Amazon Web Services account and Region.
- An external key store with `PUBLIC_ENDPOINT` connectivity cannot use the same `XksProxyUriEndpoint` value as an external key store with `VPC_ENDPOINT_SERVICE` connectivity in this Amazon Web Services Region.
- Each external key store with `VPC_ENDPOINT_SERVICE` connectivity must have its own private DNS name. The `XksProxyUriEndpoint` value for external key stores with `VPC_ENDPOINT_SERVICE` connectivity (private DNS name) must be unique in the Amazon Web Services account and Region.

`--xks-proxy-uri-path` (string)

Specifies the base path to the proxy APIs for this external key store. To find this value, see the documentation for your external key store proxy. This parameter is required for all custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

The value must start with `/` and must end with `/kms/xks/v1` where `v1` represents the version of the KMS external key store proxy API. This path can include an optional prefix between the required elements such as `/*prefix* /kms/xks/v1` .

**Uniqueness requirements:**

- The combined `XksProxyUriEndpoint` and `XksProxyUriPath` values must be unique in the Amazon Web Services account and Region.

`--xks-proxy-vpc-endpoint-service-name` (string)

Specifies the name of the Amazon VPC endpoint service for interface endpoints that is used to communicate with your external key store proxy (XKS proxy). This parameter is required when the value of `CustomKeyStoreType` is `EXTERNAL_KEY_STORE` and the value of `XksProxyConnectivity` is `VPC_ENDPOINT_SERVICE` .

The Amazon VPC endpoint service must [fulfill all requirements](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keystore.html#xks-requirements) for use with an external key store.

**Uniqueness requirements:**

- External key stores with `VPC_ENDPOINT_SERVICE` connectivity can share an Amazon VPC, but each external key store must have its own VPC endpoint service and private DNS name.

`--xks-proxy-authentication-credential` (structure)

Specifies an authentication credential for the external key store proxy (XKS proxy). This parameter is required for all custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

The `XksProxyAuthenticationCredential` has two required elements: `RawSecretAccessKey` , a secret key, and `AccessKeyId` , a unique identifier for the `RawSecretAccessKey` . For character requirements, see [XksProxyAuthenticationCredentialType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/APIReference/API_XksProxyAuthenticationCredentialType.html) .

KMS uses this authentication credential to sign requests to the external key store proxy on your behalf. This credential is unrelated to Identity and Access Management (IAM) and Amazon Web Services credentials.

This parameter doesnât set or change the authentication credentials on the XKS proxy. It just tells KMS the credential that you established on your external key store proxy. If you rotate your proxy authentication credential, use the  UpdateCustomKeyStore operation to provide the new credential to KMS.

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

Indicates how KMS communicates with the external key store proxy. This parameter is required for custom key stores with a `CustomKeyStoreType` of `EXTERNAL_KEY_STORE` .

If the external key store proxy uses a public endpoint, specify `PUBLIC_ENDPOINT` . If the external key store proxy uses a Amazon VPC endpoint service for communication with KMS, specify `VPC_ENDPOINT_SERVICE` . For help making this choice, see [Choosing a connectivity option](https://docs.aws.amazon.com/kms/latest/developerguide/plan-xks-keystore.html#choose-xks-connectivity) in the *Key Management Service Developer Guide* .

An Amazon VPC endpoint service keeps your communication with KMS in a private address space entirely within Amazon Web Services, but it requires more configuration, including establishing a Amazon VPC with multiple subnets, a VPC endpoint service, a network load balancer, and a verified private DNS name. A public endpoint is simpler to set up, but it might be slower and might not fulfill your security requirements. You might consider testing with a public endpoint, and then establishing a VPC endpoint service for production tasks. Note that this choice does not determine the location of the external key store proxy. Even if you choose a VPC endpoint service, the proxy can be hosted within the VPC or outside of Amazon Web Services such as in your corporate data center.

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

**Example 1: To create an AWS CloudHSM key store**

The following `create-custom-key-store` example creates an AWS CloudHSM key store backed by an AWS CloudHSM cluster using the required parameters. You can also add the `custom-key-store-type``parameter with the default value: ``AWS_CLOUDHSM`.

To specify the file input for the `trust-anchor-certificate` command in the AWS CLI, the `file://` prefix is required.

```
aws kms create-custom-key-store \
    --custom-key-store-name ExampleCloudHSMKeyStore \
    --cloud-hsm-cluster-id cluster-1a23b4cdefg \
    --key-store-password kmsPswd \
    --trust-anchor-certificate file://customerCA.crt
```

Output:

```
{
    "CustomKeyStoreId": cks-1234567890abcdef0
}
```

For more information, see [Creating an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 2: To create an external key store with public endpoint connectivity**

The following `create-custom-key-store` example creates an external key store (XKS) that communicates with AWS KMS over the internet.

In this example, the `XksProxyUriPath` uses an optional prefix of `example-prefix`.

NOTE: If you use AWS CLI version 1.0, run the following command before specifying a parameter with an HTTP or HTTPS value, such as the XksProxyUriEndpoint parameter.

```
aws configure set cli_follow_urlparam false
```

Otherwise, AWS CLI version 1.0 replaces the parameter value with the content found at that URI address.

```
aws kms create-custom-key-store \
    --custom-key-store-name ExamplePublicEndpointXKS \
    --custom-key-store-type EXTERNAL_KEY_STORE \
    --xks-proxy-connectivity PUBLIC_ENDPOINT \
    --xks-proxy-uri-endpoint "https://myproxy.xks.example.com" \
    --xks-proxy-uri-path "/example-prefix/kms/xks/v1" \
    --xks-proxy-authentication-credential "AccessKeyId=ABCDE12345670EXAMPLE, RawSecretAccessKey=DXjSUawnel2fr6SKC7G25CNxTyWKE5PF9XX6H/u9pSo="
```

Output:

```
{
    "CustomKeyStoreId": cks-2234567890abcdef0
}
```

For more information, see [Creating an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystorecreate-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 3: To create an external key store with VPC endpoint service connectivity**

The following `create-custom-key-store` example creates an external key store (XKS) that uses an Amazon VPC endpoint service to communicate with AWS KMS.

NOTE: If you use AWS CLI version 1.0, run the following command before specifying a parameter with an HTTP or HTTPS value, such as the XksProxyUriEndpoint parameter.

```
aws configure set cli_follow_urlparam false
```

Otherwise, AWS CLI version 1.0 replaces the parameter value with the content found at that URI address.

```
aws kms create-custom-key-store \
    --custom-key-store-name ExampleVPCEndpointXKS \
    --custom-key-store-type EXTERNAL_KEY_STORE \
    --xks-proxy-connectivity VPC_ENDPOINT_SERVICE \
    --xks-proxy-uri-endpoint "https://myproxy-private.xks.example.com" \
    --xks-proxy-uri-path "/kms/xks/v1" \
    --xks-proxy-vpc-endpoint-service-name "com.amazonaws.vpce.us-east-1.vpce-svc-example1" \
    --xks-proxy-authentication-credential "AccessKeyId=ABCDE12345670EXAMPLE, RawSecretAccessKey=DXjSUawnel2fr6SKC7G25CNxTyWKE5PF9XX6H/u9pSo="
```

Output:

```
{
    "CustomKeyStoreId": cks-3234567890abcdef0
}
```

For more information, see [Creating an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-keystorecreate-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

## Output

CustomKeyStoreId -> (string)

A unique identifier for the new custom key store.