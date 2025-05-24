# describe-tls-inspection-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-tls-inspection-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-tls-inspection-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [network-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html#cli-aws-network-firewall) ]

# describe-tls-inspection-configuration

## Description

Returns the data objects for the specified TLS inspection configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/network-firewall-2020-11-12/DescribeTLSInspectionConfiguration)

## Synopsis

```
describe-tls-inspection-configuration
[--tls-inspection-configuration-arn <value>]
[--tls-inspection-configuration-name <value>]
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

`--tls-inspection-configuration-arn` (string)

The Amazon Resource Name (ARN) of the TLS inspection configuration.

You must specify the ARN or the name, and you can specify both.

`--tls-inspection-configuration-name` (string)

The descriptive name of the TLS inspection configuration. You canât change the name of a TLS inspection configuration after you create it.

You must specify the ARN or the name, and you can specify both.

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

UpdateToken -> (string)

A token used for optimistic locking. Network Firewall returns a token to your requests that access the TLS inspection configuration. The token marks the state of the TLS inspection configuration resource at the time of the request.

To make changes to the TLS inspection configuration, you provide the token in your request. Network Firewall uses the token to ensure that the TLS inspection configuration hasnât changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException` . If this happens, retrieve the TLS inspection configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.

TLSInspectionConfiguration -> (structure)

The object that defines a TLS inspection configuration. This, along with  TLSInspectionConfigurationResponse , define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling  DescribeTLSInspectionConfiguration .

Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.

To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the *Network Firewall Developer Guide* .

ServerCertificateConfigurations -> (list)

Lists the server certificate configurations that are associated with the TLS configuration.

(structure)

Configures the Certificate Manager certificates and scope that Network Firewall uses to decrypt and re-encrypt traffic using a  TLSInspectionConfiguration . You can configure `ServerCertificates` for inbound SSL/TLS inspection, a `CertificateAuthorityArn` for outbound SSL/TLS inspection, or both. For information about working with certificates for TLS inspection, see [Using SSL/TLS server certficiates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html) in the *Network Firewall Developer Guide* .

### Note

If a server certificate thatâs associated with your  TLSInspectionConfiguration is revoked, deleted, or expired it can result in client-side TLS errors.

ServerCertificates -> (list)

The list of server certificates to use for inbound SSL/TLS inspection.

(structure)

Any Certificate Manager (ACM) Secure Sockets Layer/Transport Layer Security (SSL/TLS) server certificate thatâs associated with a  ServerCertificateConfiguration . Used in a  TLSInspectionConfiguration for inspection of inbound traffic to your firewall. You must request or import a SSL/TLS certificate into ACM for each domain Network Firewall needs to decrypt and inspect. Network Firewall uses the SSL/TLS certificates to decrypt specified inbound SSL/TLS traffic going to your firewall. For information about working with certificates in Certificate Manager, see [Request a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) or [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *Certificate Manager User Guide* .

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the Certificate Manager SSL/TLS server certificate thatâs used for inbound SSL/TLS inspection.

Scopes -> (list)

A list of scopes.

(structure)

Settings that define the Secure Sockets Layer/Transport Layer Security (SSL/TLS) traffic that Network Firewall should decrypt for inspection by the stateful rule engine.

Sources -> (list)

The source IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any source address.

(structure)

A single IP address specification. This is used in the  MatchAttributes source and destination specifications.

AddressDefinition -> (string)

Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

Examples:

- To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

Destinations -> (list)

The destination IP addresses and address ranges to decrypt for inspection, in CIDR notation. If not specified, this matches with any destination address.

(structure)

A single IP address specification. This is used in the  MatchAttributes source and destination specifications.

AddressDefinition -> (string)

Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6.

Examples:

- To configure Network Firewall to inspect for the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

SourcePorts -> (list)

The source ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any source port.

You can specify individual ports, for example `1994` , and you can specify port ranges, such as `1990:1994` .

(structure)

A single port range specification. This is used for source and destination port ranges in the stateless rule  MatchAttributes , `SourcePorts` , and `DestinationPorts` settings.

FromPort -> (integer)

The lower limit of the port range. This must be less than or equal to the `ToPort` specification.

ToPort -> (integer)

The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.

DestinationPorts -> (list)

The destination ports to decrypt for inspection, in Transmission Control Protocol (TCP) format. If not specified, this matches with any destination port.

You can specify individual ports, for example `1994` , and you can specify port ranges, such as `1990:1994` .

(structure)

A single port range specification. This is used for source and destination port ranges in the stateless rule  MatchAttributes , `SourcePorts` , and `DestinationPorts` settings.

FromPort -> (integer)

The lower limit of the port range. This must be less than or equal to the `ToPort` specification.

ToPort -> (integer)

The upper limit of the port range. This must be greater than or equal to the `FromPort` specification.

Protocols -> (list)

The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.

Network Firewall currently supports only TCP.

(integer)

CertificateAuthorityArn -> (string)

The Amazon Resource Name (ARN) of the imported certificate authority (CA) certificate within Certificate Manager (ACM) to use for outbound SSL/TLS inspection.

The following limitations apply:

- You can use CA certificates that you imported into ACM, but you canât generate CA certificates with ACM.
- You canât use certificates issued by Private Certificate Authority.

For more information about configuring certificates for outbound inspection, see [Using SSL/TLS certificates with certificates with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-certificate-requirements.html) in the *Network Firewall Developer Guide* .

For information about working with certificates in ACM, see [Importing certificates](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *Certificate Manager User Guide* .

CheckCertificateRevocationStatus -> (structure)

When enabled, Network Firewall checks if the server certificate presented by the server in the SSL/TLS connection has a revoked or unkown status. If the certificate has an unknown or revoked status, you must specify the actions that Network Firewall takes on outbound traffic. To check the certificate revocation status, you must also specify a `CertificateAuthorityArn` in  ServerCertificateConfiguration .

RevokedStatusAction -> (string)

Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has a revoked status.

- **PASS** - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
- **DROP** - Network Firewall closes the connection and drops subsequent packets for that connection.
- **REJECT** - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. `REJECT` is available only for TCP traffic.

UnknownStatusAction -> (string)

Configures how Network Firewall processes traffic when it determines that the certificate presented by the server in the SSL/TLS connection has an unknown status, or a status that cannot be determined for any other reason, including when the service is unable to connect to the OCSP and CRL endpoints for the certificate.

- **PASS** - Allow the connection to continue, and pass subsequent packets to the stateful engine for inspection.
- **DROP** - Network Firewall closes the connection and drops subsequent packets for that connection.
- **REJECT** - Network Firewall sends a TCP reject packet back to your client. The service closes the connection and drops subsequent packets for that connection. `REJECT` is available only for TCP traffic.

TLSInspectionConfigurationResponse -> (structure)

The high-level properties of a TLS inspection configuration. This, along with the  TLSInspectionConfiguration , define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling  DescribeTLSInspectionConfiguration .

TLSInspectionConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the TLS inspection configuration.

TLSInspectionConfigurationName -> (string)

The descriptive name of the TLS inspection configuration. You canât change the name of a TLS inspection configuration after you create it.

TLSInspectionConfigurationId -> (string)

A unique identifier for the TLS inspection configuration. This ID is returned in the responses to create and list commands. You provide it to operations such as update and delete.

TLSInspectionConfigurationStatus -> (string)

Detailed information about the current status of a  TLSInspectionConfiguration . You can retrieve this for a TLS inspection configuration by calling  DescribeTLSInspectionConfiguration and providing the TLS inspection configuration name and ARN.

Description -> (string)

A description of the TLS inspection configuration.

Tags -> (list)

The key:value pairs to associate with the resource.

(structure)

A key:value pair associated with an Amazon Web Services resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as âenvironmentâ) and the tag value represents a specific value within that category (such as âtest,â âdevelopment,â or âproductionâ). You can add up to 50 tags to each Amazon Web Services resource.

Key -> (string)

The part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as âcustomer.â Tag keys are case-sensitive.

Value -> (string)

The part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as âcompanyAâ or âcompanyB.â Tag values are case-sensitive.

LastModifiedTime -> (timestamp)

The last time that the TLS inspection configuration was changed.

NumberOfAssociations -> (integer)

The number of firewall policies that use this TLS inspection configuration.

EncryptionConfiguration -> (structure)

A complex type that contains the Amazon Web Services KMS encryption configuration settings for your TLS inspection configuration.

KeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless youâre using a key thatâs managed by another account. If youâre using a key managed by another account, then specify the key ARN. For more information, see [Key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *Amazon Web Services KMS Developer Guide* .

Type -> (string)

The type of Amazon Web Services KMS key to use for encryption of your Network Firewall resources.

Certificates -> (list)

A list of the certificates associated with the TLS inspection configuration.

(structure)

Contains metadata about an Certificate Manager certificate.

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate.

CertificateSerial -> (string)

The serial number of the certificate.

Status -> (string)

The status of the certificate.

StatusMessage -> (string)

Contains details about the certificate status, including information about certificate errors.

CertificateAuthority -> (structure)

Contains metadata about an Certificate Manager certificate.

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate.

CertificateSerial -> (string)

The serial number of the certificate.

Status -> (string)

The status of the certificate.

StatusMessage -> (string)

Contains details about the certificate status, including information about certificate errors.