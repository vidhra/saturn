# create-resolver-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# create-resolver-endpoint

## Description

Creates a Resolver endpoint. There are two types of Resolver endpoints, inbound and outbound:

- An *inbound Resolver endpoint* forwards DNS queries to the DNS service for a VPC from your network.
- An *outbound Resolver endpoint* forwards DNS queries from the DNS service for a VPC to your network.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/CreateResolverEndpoint)

## Synopsis

```
create-resolver-endpoint
--creator-request-id <value>
[--name <value>]
--security-group-ids <value>
--direction <value>
--ip-addresses <value>
[--outpost-arn <value>]
[--preferred-instance-type <value>]
[--tags <value>]
[--resolver-endpoint-type <value>]
[--protocols <value>]
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

`--creator-request-id` (string)

A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.

`--name` (string)

A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.

`--security-group-ids` (list)

The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more inbound rules (for inbound Resolver endpoints) or outbound rules (for outbound Resolver endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that youâre using for DNS queries on your network.

Some security group rules will cause your connection to be tracked. For outbound resolver endpoint, it can potentially impact the maximum queries per second from outbound endpoint to your target name server. For inbound resolver endpoint, it can bring down the overall maximum queries per second per IP address to as low as 1500. To avoid connection tracking caused by security group, see [Untracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connectionsl) .

(string)

Syntax:

```
"string" "string" ...
```

`--direction` (string)

Specify the applicable value:

- `INBOUND` : Resolver forwards DNS queries to the DNS service for a VPC from your network
- `OUTBOUND` : Resolver forwards DNS queries from the DNS service for a VPC to your network

Possible values:

- `INBOUND`
- `OUTBOUND`

`--ip-addresses` (list)

The subnets and IP addresses in your VPC that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). The subnet ID uniquely identifies a VPC.

### Note

Even though the minimum is 1, Route 53 requires that you create at least two.

(structure)

In a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request, the IP address that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). `IpAddressRequest` also includes the ID of the subnet that contains the IP address.

SubnetId -> (string)

The ID of the subnet that contains the IP address.

Ip -> (string)

The IPv4 address that you want to use for DNS queries.

Ipv6 -> (string)

The IPv6 address that you want to use for DNS queries.

Shorthand Syntax:

```
SubnetId=string,Ip=string,Ipv6=string ...
```

JSON Syntax:

```
[
  {
    "SubnetId": "string",
    "Ip": "string",
    "Ipv6": "string"
  }
  ...
]
```

`--outpost-arn` (string)

The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the `PreferredInstanceType` .

`--preferred-instance-type` (string)

The instance type. If you specify this, you must also specify a value for the `OutpostArn` .

`--tags` (list)

A list of the tag keys and values that you want to associate with the endpoint.

(structure)

One tag that you want to add to the specified resource. A tag consists of a `Key` (a name for the tag) and a `Value` .

Key -> (string)

The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of `Key` might be `account-id` .

Value -> (string)

The value for the tag. For example, if `Key` is `account-id` , then `Value` might be the ID of the customer account that youâre creating the resource for.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--resolver-endpoint-type` (string)

For the endpoint type you can choose either IPv4, IPv6, or dual-stack. A dual-stack endpoint means that it will resolve via both IPv4 and IPv6. This endpoint type is applied to all IP addresses.

Possible values:

- `IPV6`
- `IPV4`
- `DUALSTACK`

`--protocols` (list)

The protocols you want to use for the endpoint. DoH-FIPS is applicable for inbound endpoints only.

For an inbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 and DoH-FIPS in combination.
- Do53 alone.
- DoH alone.
- DoH-FIPS alone.
- None, which is treated as Do53.

For an outbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 alone.
- DoH alone.
- None, which is treated as Do53.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  DoH
  Do53
  DoH-FIPS
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

**To create an inbound Resolver endpoint**

The following `create-resolver-endpoint` example creates an inbound Resolver endpoint. You can use the same command to create both inbound and outbound endpoints.

**aws route53resolver create-resolver-endpoint**:
âname my-inbound-endpoint âcreator-request-id 2020-01-01-18:47 âsecurity-group-ids âsg-f62bexamâ âdirection INBOUND âip-addresses SubnetId=subnet-ba47exam,Ip=192.0.2.255 SubnetId=subnet-12d8exam,Ip=192.0.2.254

Output:

```
{
    "ResolverEndpoint": {
        "Id": "rslvr-in-f9ab8a03f1example",
        "CreatorRequestId": "2020-01-01-18:47",
        "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-f9ab8a03f1example",
        "Name": "my-inbound-endpoint",
        "SecurityGroupIds": [
            "sg-f62bexam"
        ],
        "Direction": "INBOUND",
        "IpAddressCount": 2,
        "HostVPCId": "vpc-304examp",
        "Status": "CREATING",
        "StatusMessage": "[Trace id: 1-5dc1ff84-f3477826e4a190025example] Creating the Resolver Endpoint",
        "CreationTime": "2020-01-01T23:02:29.583Z",
        "ModificationTime": "2020-01-01T23:02:29.583Z"
    }
}
```

**To create an outbound Resolver endpoint**

The following `create-resolver-endpoint` example creates an outbound resolver endpoint using the values in the JSON-formatted document `create-outbound-resolver-endpoint.json`.

```
aws route53resolver create-resolver-endpoint \
    --cli-input-json file://c:\temp\create-outbound-resolver-endpoint.json
```

Contents of `create-outbound-resolver-endpoint.json`:

```
{
   "CreatorRequestId": "2020-01-01-18:47",
   "Direction": "OUTBOUND",
   "IpAddresses": [
      {
         "Ip": "192.0.2.255",
         "SubnetId": "subnet-ba47exam"
      },
      {
         "Ip": "192.0.2.254",
         "SubnetId": "subnet-12d8exam"
      }
   ],
   "Name": "my-outbound-endpoint",
   "SecurityGroupIds": [ "sg-05cd7b25d6example" ],
   "Tags": [
      {
         "Key": "my-key-name",
         "Value": "my-key-value"
      }
   ]
}
```

For more information, see [Resolving DNS Queries Between VPCs and Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) in the *Amazon Route 53 Developer Guide*.

## Output

ResolverEndpoint -> (structure)

Information about the `CreateResolverEndpoint` request, including the status of the request.

Id -> (string)

The ID of the Resolver endpoint.

CreatorRequestId -> (string)

A unique string that identifies the request that created the Resolver endpoint. The `CreatorRequestId` allows failed requests to be retried without the risk of running the operation twice.

Arn -> (string)

The ARN (Amazon Resource Name) for the Resolver endpoint.

Name -> (string)

The name that you assigned to the Resolver endpoint when you submitted a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request.

SecurityGroupIds -> (list)

The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that youâre using for DNS queries on your network.

(string)

Direction -> (string)

Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:

- `INBOUND` : allows DNS queries to your VPC from your network
- `OUTBOUND` : allows DNS queries from your VPC to your network

IpAddressCount -> (integer)

The number of IP addresses that the Resolver endpoint can use for DNS queries.

HostVPCId -> (string)

The ID of the VPC that you want to create the Resolver endpoint in.

Status -> (string)

A code that specifies the current status of the Resolver endpoint. Valid values include the following:

- `CREATING` : Resolver is creating and configuring one or more Amazon VPC network interfaces for this endpoint.
- `OPERATIONAL` : The Amazon VPC network interfaces for this endpoint are correctly configured and able to pass inbound or outbound DNS queries between your network and Resolver.
- `UPDATING` : Resolver is associating or disassociating one or more network interfaces with this endpoint.
- `AUTO_RECOVERING` : Resolver is trying to recover one or more of the network interfaces that are associated with this endpoint. During the recovery process, the endpoint functions with limited capacity because of the limit on the number of DNS queries per IP address (per network interface). For the current limit, see [Limits on Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-resolver) .
- `ACTION_NEEDED` : This endpoint is unhealthy, and Resolver canât automatically recover it. To resolve the problem, we recommend that you check each IP address that you associated with the endpoint. For each IP address that isnât available, add another IP address and then delete the IP address that isnât available. (An endpoint must always include at least two IP addresses.) A status of `ACTION_NEEDED` can have a variety of causes. Here are two common causes:
- One or more of the network interfaces that are associated with the endpoint were deleted using Amazon VPC.
- The network interface couldnât be created for some reason thatâs outside the control of Resolver.
- `DELETING` : Resolver is deleting this endpoint and the associated network interfaces.

StatusMessage -> (string)

A detailed description of the status of the Resolver endpoint.

CreationTime -> (string)

The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime -> (string)

The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).

OutpostArn -> (string)

The ARN (Amazon Resource Name) for the Outpost.

PreferredInstanceType -> (string)

The Amazon EC2 instance type.

ResolverEndpointType -> (string)

The Resolver endpoint IP address type.

Protocols -> (list)

Protocols used for the endpoint. DoH-FIPS is applicable for inbound endpoints only.

For an inbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 and DoH-FIPS in combination.
- Do53 alone.
- DoH alone.
- DoH-FIPS alone.
- None, which is treated as Do53.

For an outbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 alone.
- DoH alone.
- None, which is treated as Do53.

(string)