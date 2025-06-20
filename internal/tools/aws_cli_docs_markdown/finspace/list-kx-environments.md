# list-kx-environmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/list-kx-environments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/list-kx-environments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# list-kx-environments

## Description

Returns a list of kdb environments created in an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/ListKxEnvironments)

`list-kx-environments` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `environments`

## Synopsis

```
list-kx-environments
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

## Output

environments -> (list)

A list of environments in an account.

(structure)

The details of a kdb environment.

name -> (string)

The name of the kdb environment.

environmentId -> (string)

A unique identifier for the kdb environment.

awsAccountId -> (string)

The unique identifier of the AWS account in which you create the kdb environment.

status -> (string)

The status of the environment creation.

- CREATE_REQUESTED â Environment creation has been requested.
- CREATING â Environment is in the process of being created.
- FAILED_CREATION â Environment creation has failed.
- CREATED â Environment is successfully created and is currently active.
- DELETE REQUESTED â Environment deletion has been requested.
- DELETING â Environment is in the process of being deleted.
- RETRY_DELETION â Initial environment deletion failed, system is reattempting delete.
- DELETED â Environment has been deleted.
- FAILED_DELETION â Environment deletion has failed.

tgwStatus -> (string)

The status of the network configuration.

dnsStatus -> (string)

The status of DNS configuration.

errorMessage -> (string)

Specifies the error message that appears if a flow fails.

description -> (string)

A description of the kdb environment.

environmentArn -> (string)

The Amazon Resource Name (ARN) of your kdb environment.

kmsKeyId -> (string)

The unique identifier of the KMS key.

dedicatedServiceAccountId -> (string)

A unique identifier for the AWS environment infrastructure account.

transitGatewayConfiguration -> (structure)

Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.

transitGatewayID -> (string)

The identifier of the transit gateway created by the customer to connect outbound traffics from kdb network to your internal network.

routableCIDRSpace -> (string)

The routing CIDR on behalf of kdb environment. It could be any â/26 range in the 100.64.0.0 CIDR space. After providing, it will be added to the customerâs transit gateway routing table so that the traffics could be routed to kdb network.

attachmentNetworkAclConfiguration -> (list)

The rules that define how you manage the outbound traffic from kdb network to your internal network.

(structure)

The network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. The entry is a set of numbered ingress and egress rules that determine whether a packet should be allowed in or out of a subnet associated with the ACL. We process the entries in the ACL according to the rule numbers, in ascending order.

ruleNumber -> (integer)

The rule number for the entry. For example *100* . All the network ACL entries are processed in ascending order by rule number.

protocol -> (string)

The protocol number. A value of *-1* means all the protocols.

ruleAction -> (string)

Indicates whether to allow or deny the traffic that matches the rule.

portRange -> (structure)

The range of ports the rule applies to.

from -> (integer)

The first port in the range.

to -> (integer)

The last port in the range.

icmpTypeCode -> (structure)

Defines the ICMP protocol that consists of the ICMP type and code.

type -> (integer)

The ICMP type. A value of *-1* means all types.

code -> (integer)

The ICMP code. A value of *-1* means all codes for the specified ICMP type.

cidrBlock -> (string)

The IPv4 network range to allow or deny, in CIDR notation. For example, `172.16.0.0/24` . We modify the specified CIDR block to its canonical form. For example, if you specify `100.68.0.18/18` , we modify it to `100.68.0.0/18` .

customDNSConfiguration -> (list)

A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.

(structure)

A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.

customDNSServerName -> (string)

The name of the DNS server.

customDNSServerIP -> (string)

The IP address of the DNS server.

creationTimestamp -> (timestamp)

The timestamp at which the kdb environment was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

updateTimestamp -> (timestamp)

The timestamp at which the kdb environment was modified in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

availabilityZoneIds -> (list)

The identifier of the availability zones where subnets for the environment are created.

(string)

certificateAuthorityArn -> (string)

The Amazon Resource Name (ARN) of the certificate authority:

nextToken -> (string)

A token that indicates where a results page should begin.