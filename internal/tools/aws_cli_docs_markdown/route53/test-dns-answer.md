# test-dns-answerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/test-dns-answer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/test-dns-answer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# test-dns-answer

## Description

Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask.

This call only supports querying public hosted zones.

### Note

The `TestDnsAnswer` returns information similar to what you would expect from the answer section of the `dig` command. Therefore, if you query for the name servers of a subdomain that point to the parent name servers, those will not be returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/TestDNSAnswer)

## Synopsis

```
test-dns-answer
--hosted-zone-id <value>
--record-name <value>
--record-type <value>
[--resolver-ip <value>]
[--edns0-client-subnet-ip <value>]
[--edns0-client-subnet-mask <value>]
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

`--hosted-zone-id` (string)

The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.

`--record-name` (string)

The name of the resource record set that you want Amazon Route 53 to simulate a query for.

`--record-type` (string)

The type of the resource record set.

Possible values:

- `SOA`
- `A`
- `TXT`
- `NS`
- `CNAME`
- `MX`
- `NAPTR`
- `PTR`
- `SRV`
- `SPF`
- `AAAA`
- `CAA`
- `DS`
- `TLSA`
- `SSHFP`
- `SVCB`
- `HTTPS`

`--resolver-ip` (string)

If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, `TestDnsAnswer` uses the IP address of a DNS resolver in the Amazon Web Services US East (N. Virginia) Region (`us-east-1` ).

`--edns0-client-subnet-ip` (string)

If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, `192.0.2.44` or `2001:db8:85a3::8a2e:370:7334` .

`--edns0-client-subnet-mask` (string)

If you specify an IP address for `edns0clientsubnetip` , you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify `192.0.2.44` for `edns0clientsubnetip` and `24` for `edns0clientsubnetmask` , the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.

The range of valid values depends on whether `edns0clientsubnetip` is an IPv4 or an IPv6 address:

- **IPv4** : Specify a value between 0 and 32
- **IPv6** : Specify a value between 0 and 128

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

Nameserver -> (string)

The Amazon Route 53 name server used to respond to the request.

RecordName -> (string)

The name of the resource record set that you submitted a request for.

RecordType -> (string)

The type of the resource record set that you submitted a request for.

RecordData -> (list)

A list that contains values that Amazon Route 53 returned for this resource record set.

(string)

A value that Amazon Route 53 returned for this resource record set. A `RecordDataEntry` element is one of the following:

- For non-alias resource record sets, a `RecordDataEntry` element contains one value in the resource record set. If the resource record set contains multiple values, the response includes one `RecordDataEntry` element for each value.
- For multiple resource record sets that have the same name and type, which includes weighted, latency, geolocation, and failover, a `RecordDataEntry` element contains the value from the appropriate resource record set based on the request.
- For alias resource record sets that refer to Amazon Web Services resources other than another resource record set, the `RecordDataEntry` element contains an IP address or a domain name for the Amazon Web Services resource, depending on the type of resource.
- For alias resource record sets that refer to other resource record sets, a `RecordDataEntry` element contains one value from the referenced resource record set. If the referenced resource record set contains multiple values, the response includes one `RecordDataEntry` element for each value.

ResponseCode -> (string)

A code that indicates whether the request is valid or not. The most common response code is `NOERROR` , meaning that the request is valid. If the response is not valid, Amazon Route 53 returns a response code that describes the error. For a list of possible response codes, see [DNS RCODES](http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6) on the IANA website.

Protocol -> (string)

The protocol that Amazon Route 53 used to respond to the request, either `UDP` or `TCP` .