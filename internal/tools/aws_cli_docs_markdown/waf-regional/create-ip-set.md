# create-ip-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-ip-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-ip-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf-regional](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html#cli-aws-waf-regional) ]

# create-ip-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Creates an  IPSet , which you use to specify which web requests that you want to allow or block based on the IP addresses that the requests originate from. For example, if youâre receiving a lot of requests from one or more individual IP addresses or one or more ranges of IP addresses and you want to block the requests, you can create an `IPSet` that contains those IP addresses and then configure AWS WAF to block the requests.

To create and configure an `IPSet` , perform the following steps:

- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateIPSet` request.
- Submit a `CreateIPSet` request.
- Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an  UpdateIPSet request.
- Submit an `UpdateIPSet` request to specify the IP addresses that you want AWS WAF to watch for.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/CreateIPSet)

## Synopsis

```
create-ip-set
--name <value>
--change-token <value>
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

`--name` (string)

A friendly name or description of the  IPSet . You canât change `Name` after you create the `IPSet` .

`--change-token` (string)

The value returned by the most recent call to  GetChangeToken .

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

IPSet -> (structure)

The  IPSet returned in the `CreateIPSet` response.

IPSetId -> (string)

The `IPSetId` for an `IPSet` . You use `IPSetId` to get information about an `IPSet` (see  GetIPSet ), update an `IPSet` (see  UpdateIPSet ), insert an `IPSet` into a `Rule` or delete one from a `Rule` (see  UpdateRule ), and delete an `IPSet` from AWS WAF (see  DeleteIPSet ).

`IPSetId` is returned by  CreateIPSet and by  ListIPSets .

Name -> (string)

A friendly name or description of the  IPSet . You canât change the name of an `IPSet` after you create it.

IPSetDescriptors -> (list)

The IP address type (`IPV4` or `IPV6` ) and the IP address range (in CIDR notation) that web requests originate from. If the `WebACL` is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the IP address type (`IPV4` or `IPV6` ) and the IP address range (in CIDR format) that web requests originate from.

Type -> (string)

Specify `IPV4` or `IPV6` .

Value -> (string)

Specify an IPv4 address by using CIDR notation. For example:

- To configure AWS WAF to allow, block, or count requests that originated from the IP address 192.0.2.44, specify `192.0.2.44/32` .
- To configure AWS WAF to allow, block, or count requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

Specify an IPv6 address by using CIDR notation. For example:

- To configure AWS WAF to allow, block, or count requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- To configure AWS WAF to allow, block, or count requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `CreateIPSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .