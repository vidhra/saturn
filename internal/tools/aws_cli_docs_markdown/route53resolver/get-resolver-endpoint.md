# get-resolver-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# get-resolver-endpoint

## Description

Gets information about a specified Resolver endpoint, such as whether itâs an inbound or an outbound Resolver endpoint, and the current status of the endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/GetResolverEndpoint)

## Synopsis

```
get-resolver-endpoint
--resolver-endpoint-id <value>
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

`--resolver-endpoint-id` (string)

The ID of the Resolver endpoint that you want to get information about.

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

**To get information about a Resolver endpoint**

The following `get-resolver-endpoint` example displays details for the outbound specified endpoint. You can use `get-resolver-endpoint` for both inbound and outbound endpoints by specifying the applicable endpoint ID.

```
aws route53resolver get-resolver-endpoint \
    --resolver-endpoint-id rslvr-out-d5e5920e37example
```

Output:

```
{
    "ResolverEndpoint": {
        "Id": "rslvr-out-d5e5920e37example",
        "CreatorRequestId": "2020-01-01-18:47",
        "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-out-d5e5920e37example",
        "Name": "my-outbound-endpoint",
        "SecurityGroupIds": [
            "sg-05cd7b25d6example"
        ],
        "Direction": "OUTBOUND",
        "IpAddressCount": 2,
        "HostVPCId": "vpc-304bexam",
        "Status": "OPERATIONAL",
        "StatusMessage": "This Resolver Endpoint is operational.",
        "CreationTime": "2020-01-01T23:50:50.979Z",
        "ModificationTime": "2020-01-02T23:50:50.979Z"
    }
}
```

For more information, see [Values That You Specify When You Create or Edit Inbound Endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html#resolver-forwarding-inbound-queries-values) in the *Amazon Route 53 Developer Guide*.

## Output

ResolverEndpoint -> (structure)

Information about the Resolver endpoint that you specified in a `GetResolverEndpoint` request.

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