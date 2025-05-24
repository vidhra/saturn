# update-ip-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-ip-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-ip-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf-regional](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html#cli-aws-waf-regional) ]

# update-ip-set

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Inserts or deletes  IPSetDescriptor objects in an `IPSet` . For each `IPSetDescriptor` object, you specify the following values:

- Whether to insert or delete the object from the array. If you want to change an `IPSetDescriptor` object, you delete the existing object and add a new one.
- The IP address version, `IPv4` or `IPv6` .
- The IP address in CIDR notation, for example, `192.0.2.0/24` (for the range of IP addresses from `192.0.2.0` to `192.0.2.255` ) or `192.0.2.44/32` (for the individual IP address `192.0.2.44` ).

AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

IPv6 addresses can be represented using any of the following formats:

- 1111:0000:0000:0000:0000:0000:0000:0111/128
- 1111:0:0:0:0:0:0:0111/128
- 1111::0111/128
- 1111::111/128

You use an `IPSet` to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if youâre receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an `IPSet` that specifies those IP addresses, and then configure AWS WAF to block the requests.

To create and configure an `IPSet` , perform the following steps:

- Submit a  CreateIPSet request.
- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of an  UpdateIPSet request.
- Submit an `UpdateIPSet` request to specify the IP addresses that you want AWS WAF to watch for.

When you update an `IPSet` , you specify the IP addresses that you want to add and/or the IP addresses that you want to delete. If you want to change an IP address, you delete the existing IP address and add the new one.

You can insert a maximum of 1000 addresses in a single request.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/UpdateIPSet)

## Synopsis

```
update-ip-set
--ip-set-id <value>
--change-token <value>
--updates <value>
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

`--ip-set-id` (string)

The `IPSetId` of the  IPSet that you want to update. `IPSetId` is returned by  CreateIPSet and by  ListIPSets .

`--change-token` (string)

The value returned by the most recent call to  GetChangeToken .

`--updates` (list)

An array of `IPSetUpdate` objects that you want to insert into or delete from an  IPSet . For more information, see the applicable data types:

- IPSetUpdate : Contains `Action` and `IPSetDescriptor`
- IPSetDescriptor : Contains `Type` and `Value`

You can insert a maximum of 1000 addresses in a single request.

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the type of update to perform to an  IPSet with  UpdateIPSet .

Action -> (string)

Specifies whether to insert or delete an IP address with  UpdateIPSet .

IPSetDescriptor -> (structure)

The IP address type (`IPV4` or `IPV6` ) and the IP address range (in CIDR notation) that web requests originate from.

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

Shorthand Syntax:

```
Action=string,IPSetDescriptor={Type=string,Value=string} ...
```

JSON Syntax:

```
[
  {
    "Action": "INSERT"|"DELETE",
    "IPSetDescriptor": {
      "Type": "IPV4"|"IPV6",
      "Value": "string"
    }
  }
  ...
]
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

**To update an IP set**

The following `update-ip-set` command updates an IPSet with an IPv4 address and deletes an IPv6 address. Get the value for `change-token` by running the `get-change-token` command. Because the value for updates includes embedded double-quotes, you must surround the value with single quotes.

```
aws waf update-ip-set \
    --ip-set-id a123fae4-b567-8e90-1234-5ab67ac8ca90 \
    --change-token 12cs345-67cd-890b-1cd2-c3a4567d89f1 \
    --updates 'Action="INSERT",IPSetDescriptor={Type="IPV4",Value="12.34.56.78/16"},Action="DELETE",IPSetDescriptor={Type="IPV6",Value="1111:0000:0000:0000:0000:0000:0000:0111/128"}'
```

Alternatively you can use a JSON file to specify the input. For example:

```
aws waf-regional update-ip-set \
    --ip-set-id a123fae4-b567-8e90-1234-5ab67ac8ca90 \
    --change-token 12cs345-67cd-890b-1cd2-c3a4567d89f1  \
    --updates file://change.json
```

Content of the `change.json`

```
[
    {
        "Action": "INSERT",
        "IPSetDescriptor":
        {
            "Type": "IPV4",
            "Value": "12.34.56.78/16"
        }
    },
    {
        "Action": "DELETE",
        "IPSetDescriptor":
        {
            "Type": "IPV6",
            "Value": "1111:0000:0000:0000:0000:0000:0000:0111/128"
        }
    }
]
```

For more information, see [Working with IP Match Conditions](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-ip-conditions.html) in the *AWS WAF Developer Guide*.

## Output

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `UpdateIPSet` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .