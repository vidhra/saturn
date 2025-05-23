# describe-serverÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-server.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-server.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# describe-server

## Description

Describes a file transfer protocol-enabled server that you specify by passing the `ServerId` parameter.

The response contains a description of a serverâs properties. When you set `EndpointType` to VPC, the response will contain the `EndpointDetails` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeServer)

## Synopsis

```
describe-server
--server-id <value>
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

`--server-id` (string)

A system-assigned unique identifier for a server.

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

Server -> (structure)

An array containing the properties of a server with the `ServerID` you specified.

Arn -> (string)

Specifies the unique Amazon Resource Name (ARN) of the server.

Certificate -> (string)

Specifies the ARN of the Amazon Web ServicesCertificate Manager (ACM) certificate. Required when `Protocols` is set to `FTPS` .

ProtocolDetails -> (structure)

The protocol settings that are configured for your server.

- To indicate passive mode (for FTP and FTPS protocols), use the `PassiveIp` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer.
- To ignore the error that is generated when the client attempts to use the `SETSTAT` command on a file that you are uploading to an Amazon S3 bucket, use the `SetStatOption` parameter. To have the Transfer Family server ignore the `SETSTAT` command and upload files without needing to make any changes to your SFTP client, set the value to `ENABLE_NO_OP` . If you set the `SetStatOption` parameter to `ENABLE_NO_OP` , Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a `SETSTAT` call.
- To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the `TlsSessionResumptionMode` parameter.
- `As2Transports` indicates the transport method for the AS2 messages. Currently, only HTTP is supported.

PassiveIp -> (string)

Indicates passive mode, for FTP and FTPS protocols. Enter a single IPv4 address, such as the public IP address of a firewall, router, or load balancer. For example:

`aws transfer update-server --protocol-details PassiveIp=0.0.0.0`

Replace `0.0.0.0` in the example above with the actual IP address you want to use.

### Note

If you change the `PassiveIp` value, you must stop and then restart your Transfer Family server for the change to take effect. For details on using passive mode (PASV) in a NAT environment, see [Configuring your FTPS server behind a firewall or NAT with Transfer Family](http://aws.amazon.com/blogs/storage/configuring-your-ftps-server-behind-a-firewall-or-nat-with-aws-transfer-family/) .

*Special values*

The `AUTO` and `0.0.0.0` are special values for the `PassiveIp` parameter. The value `PassiveIp=AUTO` is assigned by default to FTP and FTPS type servers. In this case, the server automatically responds with one of the endpoint IPs within the PASV response. `PassiveIp=0.0.0.0` has a more unique application for its usage. For example, if you have a High Availability (HA) Network Load Balancer (NLB) environment, where you have 3 subnets, you can only specify a single IP address using the `PassiveIp` parameter. This reduces the effectiveness of having High Availability. In this case, you can specify `PassiveIp=0.0.0.0` . This tells the client to use the same IP address as the Control connection and utilize all AZs for their connections. Note, however, that not all FTP clients support the `PassiveIp=0.0.0.0` response. FileZilla and WinSCP do support it. If you are using other clients, check to see if your client supports the `PassiveIp=0.0.0.0` response.

TlsSessionResumptionMode -> (string)

A property used with Transfer Family servers that use the FTPS protocol. TLS Session Resumption provides a mechanism to resume or share a negotiated secret key between the control and data connection for an FTPS session. `TlsSessionResumptionMode` determines whether or not the server resumes recent, negotiated sessions through a unique session ID. This property is available during `CreateServer` and `UpdateServer` calls. If a `TlsSessionResumptionMode` value is not specified during `CreateServer` , it is set to `ENFORCED` by default.

- `DISABLED` : the server does not process TLS session resumption client requests and creates a new TLS session for each request.
- `ENABLED` : the server processes and accepts clients that are performing TLS session resumption. The server doesnât reject client data connections that do not perform the TLS session resumption client processing.
- `ENFORCED` : the server processes and accepts clients that are performing TLS session resumption. The server rejects client data connections that do not perform the TLS session resumption client processing. Before you set the value to `ENFORCED` , test your clients.

### Note

Not all FTPS clients perform TLS session resumption. So, if you choose to enforce TLS session resumption, you prevent any connections from FTPS clients that donât perform the protocol negotiation. To determine whether or not you can use the `ENFORCED` value, you need to test your clients.

SetStatOption -> (string)

Use the `SetStatOption` to ignore the error that is generated when the client attempts to use `SETSTAT` on a file you are uploading to an S3 bucket.

Some SFTP file transfer clients can attempt to change the attributes of remote files, including timestamp and permissions, using commands, such as `SETSTAT` when uploading the file. However, these commands are not compatible with object storage systems, such as Amazon S3. Due to this incompatibility, file uploads from these clients can result in errors even when the file is otherwise successfully uploaded.

Set the value to `ENABLE_NO_OP` to have the Transfer Family server ignore the `SETSTAT` command, and upload files without needing to make any changes to your SFTP client. While the `SetStatOption` `ENABLE_NO_OP` setting ignores the error, it does generate a log entry in Amazon CloudWatch Logs, so you can determine when the client is making a `SETSTAT` call.

### Note

If you want to preserve the original timestamp for your file, and modify other file attributes using `SETSTAT` , you can use Amazon EFS as backend storage with Transfer Family.

As2Transports -> (list)

Indicates the transport method for the AS2 messages. Currently, only HTTP is supported.

(string)

Domain -> (string)

Specifies the domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.

EndpointDetails -> (structure)

The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPCâs default security groups are automatically assigned to your endpoint.

AddressAllocationIds -> (list)

A list of address allocation IDs that are required to attach an Elastic IP address to your serverâs endpoint.

An address allocation ID corresponds to the allocation ID of an Elastic IP address. This value can be retrieved from the `allocationId` field from the Amazon EC2 [Address](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html) data type. One way to retrieve this value is by calling the EC2 [DescribeAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html) API.

This parameter is optional. Set this parameter if you want to make your VPC endpoint public-facing. For details, see [Create an internet-facing endpoint for your server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint) .

### Note

This property can only be set as follows:

- `EndpointType` must be set to `VPC`
- The Transfer Family server must be offline.
- You cannot set this parameter for Transfer Family servers that use the FTP protocol.
- The server must already have `SubnetIds` populated (`SubnetIds` and `AddressAllocationIds` cannot be updated simultaneously).
- `AddressAllocationIds` canât contain duplicates, and must be equal in length to `SubnetIds` . For example, if you have three subnet IDs, you must also specify three address allocation IDs.
- Call the `UpdateServer` API to set or change this parameter.

(string)

SubnetIds -> (list)

A list of subnet IDs that are required to host your server endpoint in your VPC.

### Note

This property can only be set when `EndpointType` is set to `VPC` .

(string)

VpcEndpointId -> (string)

The identifier of the VPC endpoint.

### Note

This property can only be set when `EndpointType` is set to `VPC_ENDPOINT` .

For more information, see [https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint).

VpcId -> (string)

The VPC identifier of the VPC in which a serverâs endpoint will be hosted.

### Note

This property can only be set when `EndpointType` is set to `VPC` .

SecurityGroupIds -> (list)

A list of security groups IDs that are available to attach to your serverâs endpoint.

### Note

This property can only be set when `EndpointType` is set to `VPC` .

You can edit the `SecurityGroupIds` property in the [UpdateServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html) API only if you are changing the `EndpointType` from `PUBLIC` or `VPC_ENDPOINT` to `VPC` . To change security groups associated with your serverâs VPC endpoint after creation, use the Amazon EC2 [ModifyVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html) API.

(string)

EndpointType -> (string)

Defines the type of endpoint that your server is connected to. If your server is connected to a VPC endpoint, your server isnât accessible over the public internet.

HostKeyFingerprint -> (string)

Specifies the Base64-encoded SHA256 fingerprint of the serverâs host key. This value is equivalent to the output of the `ssh-keygen -l -f my-new-server-key` command.

IdentityProviderDetails -> (structure)

Specifies information to call a customer-supplied authentication API. This field is not populated when the `IdentityProviderType` of a server is `AWS_DIRECTORY_SERVICE` or `SERVICE_MANAGED` .

Url -> (string)

Provides the location of the service endpoint used to authenticate users.

InvocationRole -> (string)

This parameter is only applicable if your `IdentityProviderType` is `API_GATEWAY` . Provides the type of `InvocationRole` used to authenticate the user account.

DirectoryId -> (string)

The identifier of the Directory Service directory that you want to use as your identity provider.

Function -> (string)

The ARN for a Lambda function to use for the Identity provider.

SftpAuthenticationMethods -> (string)

For SFTP-enabled servers, and for custom identity providers *only* , you can specify whether to authenticate using a password, SSH key pair, or both.

- `PASSWORD` - users must provide their password to connect.
- `PUBLIC_KEY` - users must provide their private key to connect.
- `PUBLIC_KEY_OR_PASSWORD` - users can authenticate with either their password or their key. This is the default value.
- `PUBLIC_KEY_AND_PASSWORD` - users must provide both their private key and their password to connect. The server checks the key first, and then if the key is valid, the system prompts for a password. If the private key provided does not match the public key that is stored, authentication fails.

IdentityProviderType -> (string)

The mode of authentication for a server. The default value is `SERVICE_MANAGED` , which allows you to store and access user credentials within the Transfer Family service.

Use `AWS_DIRECTORY_SERVICE` to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the `IdentityProviderDetails` parameter.

Use the `API_GATEWAY` value to integrate with an identity provider of your choosing. The `API_GATEWAY` setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the `IdentityProviderDetails` parameter.

Use the `AWS_LAMBDA` value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the `Function` parameter for the `IdentityProviderDetails` data type.

LoggingRole -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.

PostAuthenticationLoginBanner -> (string)

Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.

### Note

The SFTP protocol does not support post-authentication display banners.

PreAuthenticationLoginBanner -> (string)

Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:

`This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.`

Protocols -> (list)

Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your serverâs endpoint. The available protocols are:

- `SFTP` (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH
- `FTPS` (File Transfer Protocol Secure): File transfer with TLS encryption
- `FTP` (File Transfer Protocol): Unencrypted file transfer
- `AS2` (Applicability Statement 2): used for transporting structured business-to-business data

### Note

- If you select `FTPS` , you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.
- If `Protocol` includes either `FTP` or `FTPS` , then the `EndpointType` must be `VPC` and the `IdentityProviderType` must be either `AWS_DIRECTORY_SERVICE` , `AWS_LAMBDA` , or `API_GATEWAY` .
- If `Protocol` includes `FTP` , then `AddressAllocationIds` cannot be associated.
- If `Protocol` is set only to `SFTP` , the `EndpointType` can be set to `PUBLIC` and the `IdentityProviderType` can be set any of the supported identity types: `SERVICE_MANAGED` , `AWS_DIRECTORY_SERVICE` , `AWS_LAMBDA` , or `API_GATEWAY` .
- If `Protocol` includes `AS2` , then the `EndpointType` must be `VPC` , and domain must be Amazon S3.

(string)

SecurityPolicyName -> (string)

Specifies the name of the security policy for the server.

ServerId -> (string)

Specifies the unique system-assigned identifier for a server that you instantiate.

State -> (string)

The condition of the server that was described. A value of `ONLINE` indicates that the server can accept jobs and transfer files. A `State` value of `OFFLINE` means that the server cannot perform file transfer operations.

The states of `STARTING` and `STOPPING` indicate that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of `START_FAILED` or `STOP_FAILED` can indicate an error condition.

Tags -> (list)

Specifies the key-value pairs that you can use to search for and group servers that were assigned to the server that was described.

(structure)

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

Contains one or more values that you assigned to the key name you create.

UserCount -> (integer)

Specifies the number of users that are assigned to a server you specified with the `ServerId` .

WorkflowDetails -> (structure)

Specifies the workflow ID for the workflow to assign and the execution role thatâs used for executing the workflow.

In addition to a workflow to execute when a file is uploaded completely, `WorkflowDetails` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.

OnUpload -> (list)

A trigger that starts a workflow: the workflow begins to execute after a file is uploaded.

To remove an associated workflow from a server, you can provide an empty `OnUpload` object, as in the following example.

`aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'`

### Note

`OnUpload` can contain a maximum of one `WorkflowDetail` object.

(structure)

Specifies the workflow ID for the workflow to assign and the execution role thatâs used for executing the workflow.

In addition to a workflow to execute when a file is uploaded completely, `WorkflowDetails` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.

WorkflowId -> (string)

A unique identifier for the workflow.

ExecutionRole -> (string)

Includes the necessary permissions for S3, EFS, and Lambda operations that Transfer can assume, so that all workflow steps can operate on the required resources

OnPartialUpload -> (list)

A trigger that starts a workflow if a file is only partially uploaded. You can attach a workflow to a server that executes whenever there is a partial upload.

A *partial upload* occurs when a file is open when the session disconnects.

### Note

`OnPartialUpload` can contain a maximum of one `WorkflowDetail` object.

(structure)

Specifies the workflow ID for the workflow to assign and the execution role thatâs used for executing the workflow.

In addition to a workflow to execute when a file is uploaded completely, `WorkflowDetails` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.

WorkflowId -> (string)

A unique identifier for the workflow.

ExecutionRole -> (string)

Includes the necessary permissions for S3, EFS, and Lambda operations that Transfer can assume, so that all workflow steps can operate on the required resources

StructuredLogDestinations -> (list)

Specifies the log groups to which your server logs are sent.

To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:

`arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*`

For example, `arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*`

If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an `update-server` call. For example:

`update-server --server-id s-1234567890abcdef0 --structured-log-destinations`

(string)

S3StorageOptions -> (structure)

Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default.

By default, home directory mappings have a `TYPE` of `DIRECTORY` . If you enable this option, you would then need to explicitly set the `HomeDirectoryMapEntry` `Type` to `FILE` if you want a mapping to have a file target.

DirectoryListingOptimization -> (string)

Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default.

By default, home directory mappings have a `TYPE` of `DIRECTORY` . If you enable this option, you would then need to explicitly set the `HomeDirectoryMapEntry` `Type` to `FILE` if you want a mapping to have a file target.

As2ServiceManagedEgressIpAddresses -> (list)

The list of egress IP addresses of this server. These IP addresses are only relevant for servers that use the AS2 protocol. They are used for sending asynchronous MDNs.

These IP addresses are assigned automatically when you create an AS2 server. Additionally, if you update an existing server and add the AS2 protocol, static IP addresses are assigned as well.

(string)