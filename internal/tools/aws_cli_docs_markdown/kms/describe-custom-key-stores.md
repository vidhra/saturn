# describe-custom-key-storesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-custom-key-stores.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-custom-key-stores.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# describe-custom-key-stores

## Description

Gets information about [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) in the account and Region.

This operation is part of the [custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) feature in KMS, which combines the convenience and extensive integration of KMS with the isolation and control of a key store that you own and manage.

By default, this operation returns information about all custom key stores in the account and Region. To get only information about a particular custom key store, use either the `CustomKeyStoreName` or `CustomKeyStoreId` parameter (but not both).

To determine whether the custom key store is connected to its CloudHSM cluster or external key store proxy, use the `ConnectionState` element in the response. If an attempt to connect the custom key store failed, the `ConnectionState` value is `FAILED` and the `ConnectionErrorCode` element in the response indicates the cause of the failure. For help interpreting the `ConnectionErrorCode` , see  CustomKeyStoresListEntry .

Custom key stores have a `DISCONNECTED` connection state if the key store has never been connected or you used the  DisconnectCustomKeyStore operation to disconnect it. Otherwise, the connection state is CONNECTED. If your custom key store connection state is `CONNECTED` but you are having trouble using it, verify that the backing store is active and available. For an CloudHSM key store, verify that the associated CloudHSM cluster is active and contains the minimum number of HSMs required for the operation, if any. For an external key store, verify that the external key store proxy and its associated external key manager are reachable and enabled.

For help repairing your CloudHSM key store, see the [Troubleshooting CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) . For help repairing your external key store, see the [Troubleshooting external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/xks-troubleshooting.html) . Both topics are in the *Key Management Service Developer Guide* .

**Cross-account use** : No. You cannot perform this operation on a custom key store in a different Amazon Web Services account.

**Required permissions** : [kms:DescribeCustomKeyStores](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

**Related operations:**

- ConnectCustomKeyStore
- CreateCustomKeyStore
- DeleteCustomKeyStore
- DisconnectCustomKeyStore
- UpdateCustomKeyStore

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeCustomKeyStores)

`describe-custom-key-stores` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CustomKeyStores`

## Synopsis

```
describe-custom-key-stores
[--custom-key-store-id <value>]
[--custom-key-store-name <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

Gets only information about the specified custom key store. Enter the key store ID.

By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the `CustomKeyStoreId` or `CustomKeyStoreName` parameter, but not both.

`--custom-key-store-name` (string)

Gets only information about the specified custom key store. Enter the friendly name of the custom key store.

By default, this operation gets information about all custom key stores in the account and Region. To limit the output to a particular custom key store, provide either the `CustomKeyStoreId` or `CustomKeyStoreName` parameter, but not both.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**Example 1: To get details about an AWS CloudHSM key store**

The following `describe-custom-key-store` example displays details about the specified AWS CloudHSM key store. The command is the same for all types of custom key stores, but the output differs with the key store type and, for an external key store, its connectivity option.

By default, this command displays information about all custom key stores in the account and Region. To display information about a particular custom key store, use the `custom-key-store-name` or `custom-key-store-id` parameter.

```
aws kms describe-custom-key-stores \
    --custom-key-store-name ExampleCloudHSMKeyStore
```

The output of this command includes useful details about the AWS CloudHSM key store including its connection state (`ConnectionState`). If the connection state is `FAILED`, the output includes a `ConnectionErrorCode` field that describes the problem.

Output:

```
{
    "CustomKeyStores": [
        {
            "CloudHsmClusterId": "cluster-1a23b4cdefg",
            "ConnectionState": "CONNECTED",
            "CreationDate": "2022-04-05T14:04:55-07:00",
            "CustomKeyStoreId": "cks-1234567890abcdef0",
            "CustomKeyStoreName": "ExampleExternalKeyStore",
            "TrustAnchorCertificate": "<certificate appears here>"
        }
    ]
}
```

For more information, see [Viewing an AWS CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/view-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 2: To get details about an external key store with public endpoint connectivity**

The following `describe-custom-key-store` example displays details about the specified external key store. The command is the same for all types of custom key stores, but the output differs with the key store type and, for an external key store, its connectivity option.

By default, this command displays information about all custom key stores in the account and Region. To display information about a particular custom key store, use the `custom-key-store-name` or `custom-key-store-id` parameter.

```
aws kms describe-custom-key-stores \
    --custom-key-store-id cks-9876543210fedcba9
```

The output of this command includes useful details about the external key store including its connection state (`ConnectionState`). If the connection state is `FAILED`, the output includes a `ConnectionErrorCode` field that describes the problem.

Output:

```
{
    "CustomKeyStores": [
        {
            "CustomKeyStoreId": "cks-9876543210fedcba9",
            "CustomKeyStoreName": "ExampleXKS",
            "ConnectionState": "CONNECTED",
            "CreationDate": "2022-12-02T07:48:55-07:00",
            "CustomKeyStoreType": "EXTERNAL_KEY_STORE",
            "XksProxyConfiguration": {
                "AccessKeyId": "ABCDE12345670EXAMPLE",
                "Connectivity": "PUBLIC_ENDPOINT",
                "UriEndpoint": "https://myproxy.xks.example.com",
                "UriPath": "/example-prefix/kms/xks/v1"
            }
        }
    ]
}
```

For more information, see [Viewing an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/view-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

**Example 3: To get details about an external key store with VPC endpoint service connectivity**

The following `describe-custom-key-store` example displays details about the specified external key store. The command is the same for all types of custom key stores, but the output differs with the key store type and, for an external key store, its connectivity option.

By default, this command displays information about all custom key stores in the account and Region. To display information about a particular custom key store, use the `custom-key-store-name` or `custom-key-store-id` parameter.

```
aws kms describe-custom-key-stores \
    --custom-key-store-id cks-2234567890abcdef0
```

The output of this command includes useful details about the external key store including its connection state (`ConnectionState`). If the connection state is `FAILED`, the output includes a `ConnectionErrorCode` field that describes the problem.

Output:

```
{
    "CustomKeyStores": [
        {
            "CustomKeyStoreId": "cks-3234567890abcdef0",
            "CustomKeyStoreName": "ExampleVPCExternalKeyStore",
            "ConnectionState": "CONNECTED",
            "CreationDate": "2022-12-22T07:48:55-07:00",
            "CustomKeyStoreType": "EXTERNAL_KEY_STORE",
            "XksProxyConfiguration": {
                "AccessKeyId": "ABCDE12345670EXAMPLE",
                "Connectivity": "VPC_ENDPOINT_SERVICE",
                "UriEndpoint": "https://myproxy-private.xks.example.com",
                "UriPath": "/kms/xks/v1",
                "VpcEndpointServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-example1"
            }
        }
    ]
}
```

For more information, see [Viewing an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/view-xks-keystore.html) in the *AWS Key Management Service Developer Guide*.

## Output

CustomKeyStores -> (list)

Contains metadata about each custom key store.

(structure)

Contains information about each custom key store in the custom key store list.

CustomKeyStoreId -> (string)

A unique identifier for the custom key store.

CustomKeyStoreName -> (string)

The user-specified friendly name for the custom key store.

CloudHsmClusterId -> (string)

A unique identifier for the CloudHSM cluster that is associated with an CloudHSM key store. This field appears only when the `CustomKeyStoreType` is `AWS_CLOUDHSM` .

TrustAnchorCertificate -> (string)

The trust anchor certificate of the CloudHSM cluster associated with an CloudHSM key store. When you [initialize the cluster](https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr) , you create this certificate and save it in the `customerCA.crt` file.

This field appears only when the `CustomKeyStoreType` is `AWS_CLOUDHSM` .

ConnectionState -> (string)

Indicates whether the custom key store is connected to its backing key store. For an CloudHSM key store, the `ConnectionState` indicates whether it is connected to its CloudHSM cluster. For an external key store, the `ConnectionState` indicates whether it is connected to the external key store proxy that communicates with your external key manager.

You can create and use KMS keys in your custom key stores only when its `ConnectionState` is `CONNECTED` .

The `ConnectionState` value is `DISCONNECTED` only if the key store has never been connected or you use the  DisconnectCustomKeyStore operation to disconnect it. If the value is `CONNECTED` but you are having trouble using the custom key store, make sure that the backing key store is reachable and active. For an CloudHSM key store, verify that its associated CloudHSM cluster is active and contains at least one active HSM. For an external key store, verify that the external key store proxy and external key manager are connected and enabled.

A value of `FAILED` indicates that an attempt to connect was unsuccessful. The `ConnectionErrorCode` field in the response indicates the cause of the failure. For help resolving a connection failure, see [Troubleshooting a custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html) in the *Key Management Service Developer Guide* .

ConnectionErrorCode -> (string)

Describes the connection error. This field appears in the response only when the `ConnectionState` is `FAILED` .

Many failures can be resolved by updating the properties of the custom key store. To update a custom key store, disconnect it ( DisconnectCustomKeyStore ), correct the errors ( UpdateCustomKeyStore ), and try to connect again ( ConnectCustomKeyStore ). For additional help resolving these errors, see [How to Fix a Connection Failure](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-failed) in *Key Management Service Developer Guide* .

**All custom key stores:**

- `INTERNAL_ERROR` â KMS could not complete the request due to an internal error. Retry the request. For `ConnectCustomKeyStore` requests, disconnect the custom key store before trying to connect again.
- `NETWORK_ERRORS` â Network errors are preventing KMS from connecting the custom key store to its backing key store.

**CloudHSM key stores:**

- `CLUSTER_NOT_FOUND` â KMS cannot find the CloudHSM cluster with the specified cluster ID.
- `INSUFFICIENT_CLOUDHSM_HSMS` â The associated CloudHSM cluster does not contain any active HSMs. To connect a custom key store to its CloudHSM cluster, the cluster must contain at least one active HSM.
- `INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET` â At least one private subnet associated with the CloudHSM cluster doesnât have any available IP addresses. A CloudHSM key store connection requires one free IP address in each of the associated private subnets, although two are preferable. For details, see [How to Fix a Connection Failure](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-failed) in the *Key Management Service Developer Guide* .
- `INVALID_CREDENTIALS` â The `KeyStorePassword` for the custom key store doesnât match the current password of the `kmsuser` crypto user in the CloudHSM cluster. Before you can connect your custom key store to its CloudHSM cluster, you must change the `kmsuser` account password and update the `KeyStorePassword` value for the custom key store.
- `SUBNET_NOT_FOUND` â A subnet in the CloudHSM cluster configuration was deleted. If KMS cannot find all of the subnets in the cluster configuration, attempts to connect the custom key store to the CloudHSM cluster fail. To fix this error, create a cluster from a recent backup and associate it with your custom key store. (This process creates a new cluster configuration with a VPC and private subnets.) For details, see [How to Fix a Connection Failure](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-failed) in the *Key Management Service Developer Guide* .
- `USER_LOCKED_OUT` â The `kmsuser` CU account is locked out of the associated CloudHSM cluster due to too many failed password attempts. Before you can connect your custom key store to its CloudHSM cluster, you must change the `kmsuser` account password and update the key store password value for the custom key store.
- `USER_LOGGED_IN` â The `kmsuser` CU account is logged into the associated CloudHSM cluster. This prevents KMS from rotating the `kmsuser` account password and logging into the cluster. Before you can connect your custom key store to its CloudHSM cluster, you must log the `kmsuser` CU out of the cluster. If you changed the `kmsuser` password to log into the cluster, you must also and update the key store password value for the custom key store. For help, see [How to Log Out and Reconnect](https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#login-kmsuser-2) in the *Key Management Service Developer Guide* .
- `USER_NOT_FOUND` â KMS cannot find a `kmsuser` CU account in the associated CloudHSM cluster. Before you can connect your custom key store to its CloudHSM cluster, you must create a `kmsuser` CU account in the cluster, and then update the key store password value for the custom key store.

**External key stores:**

- `INVALID_CREDENTIALS` â One or both of the `XksProxyAuthenticationCredential` values is not valid on the specified external key store proxy.
- `XKS_PROXY_ACCESS_DENIED` â KMS requests are denied access to the external key store proxy. If the external key store proxy has authorization rules, verify that they permit KMS to communicate with the proxy on your behalf.
- `XKS_PROXY_INVALID_CONFIGURATION` â A configuration error is preventing the external key store from connecting to its proxy. Verify the value of the `XksProxyUriPath` .
- `XKS_PROXY_INVALID_RESPONSE` â KMS cannot interpret the response from the external key store proxy. If you see this connection error code repeatedly, notify your external key store proxy vendor.
- `XKS_PROXY_INVALID_TLS_CONFIGURATION` â KMS cannot connect to the external key store proxy because the TLS configuration is invalid. Verify that the XKS proxy supports TLS 1.2 or 1.3. Also, verify that the TLS certificate is not expired, and that it matches the hostname in the `XksProxyUriEndpoint` value, and that it is signed by a certificate authority included in the [Trusted Certificate Authorities](https://github.com/aws/aws-kms-xksproxy-api-spec/blob/main/TrustedCertificateAuthorities) list.
- `XKS_PROXY_NOT_REACHABLE` â KMS canât communicate with your external key store proxy. Verify that the `XksProxyUriEndpoint` and `XksProxyUriPath` are correct. Use the tools for your external key store proxy to verify that the proxy is active and available on its network. Also, verify that your external key manager instances are operating properly. Connection attempts fail with this connection error code if the proxy reports that all external key manager instances are unavailable.
- `XKS_PROXY_TIMED_OUT` â KMS can connect to the external key store proxy, but the proxy does not respond to KMS in the time allotted. If you see this connection error code repeatedly, notify your external key store proxy vendor.
- `XKS_VPC_ENDPOINT_SERVICE_INVALID_CONFIGURATION` â The Amazon VPC endpoint service configuration doesnât conform to the requirements for an KMS external key store.
- The VPC endpoint service must be an endpoint service for interface endpoints in the callerâs Amazon Web Services account.
- It must have a network load balancer (NLB) connected to at least two subnets, each in a different Availability Zone.
- The `Allow principals` list must include the KMS service principal for the Region, `cks.kms.<region>.amazonaws.com` , such as `cks.kms.us-east-1.amazonaws.com` .
- It must *not* require [acceptance](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html) of connection requests.
- It must have a private DNS name. The private DNS name for an external key store with `VPC_ENDPOINT_SERVICE` connectivity must be unique in its Amazon Web Services Region.
- The domain of the private DNS name must have a [verification status](https://docs.aws.amazon.com/vpc/latest/privatelink/verify-domains.html) of `verified` .
- The [TLS certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html) specifies the private DNS hostname at which the endpoint is reachable.
- `XKS_VPC_ENDPOINT_SERVICE_NOT_FOUND` â KMS canât find the VPC endpoint service that it uses to communicate with the external key store proxy. Verify that the `XksProxyVpcEndpointServiceName` is correct and the KMS service principal has service consumer permissions on the Amazon VPC endpoint service.

CreationDate -> (timestamp)

The date and time when the custom key store was created.

CustomKeyStoreType -> (string)

Indicates the type of the custom key store. `AWS_CLOUDHSM` indicates a custom key store backed by an CloudHSM cluster. `EXTERNAL_KEY_STORE` indicates a custom key store backed by an external key store proxy and external key manager outside of Amazon Web Services.

XksProxyConfiguration -> (structure)

Configuration settings for the external key store proxy (XKS proxy). The external key store proxy translates KMS requests into a format that your external key manager can understand. The proxy configuration includes connection information that KMS requires.

This field appears only when the `CustomKeyStoreType` is `EXTERNAL_KEY_STORE` .

Connectivity -> (string)

Indicates whether the external key store proxy uses a public endpoint or an Amazon VPC endpoint service to communicate with KMS.

AccessKeyId -> (string)

The part of the external key store [proxy authentication credential](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateCustomKeyStore.html#KMS-CreateCustomKeyStore-request-XksProxyAuthenticationCredential) that uniquely identifies the secret access key.

UriEndpoint -> (string)

The URI endpoint for the external key store proxy.

If the external key store proxy has a public endpoint, it is displayed here.

If the external key store proxy uses an Amazon VPC endpoint service name, this field displays the private DNS name associated with the VPC endpoint service.

UriPath -> (string)

The path to the external key store proxy APIs.

VpcEndpointServiceName -> (string)

The Amazon VPC endpoint service used to communicate with the external key store proxy. This field appears only when the external key store proxy uses an Amazon VPC endpoint service to communicate with KMS.

NextMarker -> (string)

When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.

Truncated -> (boolean)

A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.