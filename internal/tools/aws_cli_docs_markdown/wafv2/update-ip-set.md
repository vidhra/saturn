# update-ip-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-ip-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-ip-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# update-ip-set

## Description

Updates the specified  IPSet .

### Note

This operation completely replaces the mutable specifications that you already have for the IP set with the ones that you provide to this call.

To modify an IP set, do the following:

- Retrieve it by calling  GetIPSet
- Update its settings as needed
- Provide the complete IP set specification to this call

**Temporary inconsistencies during updates**

When you create or change a web ACL or other WAF resources, the changes take a small amount of time to propagate to all areas where the resources are stored. The propagation time can be from a few seconds to a number of minutes.

The following are examples of the temporary inconsistencies that you might notice during change propagation:

- After you create a web ACL, if you try to associate it with a resource, you might get an exception indicating that the web ACL is unavailable.
- After you add a rule group to a web ACL, the new rule group rules might be in effect in one area where the web ACL is used and not in another.
- After you change a rule action setting, you might see the old action in some places and the new action in others.
- After you add an IP address to an IP set that is in use in a blocking rule, the new address might be blocked in one area while still allowed in another.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/UpdateIPSet)

## Synopsis

```
update-ip-set
--name <value>
--scope <value>
--id <value>
[--description <value>]
--addresses <value>
--lock-token <value>
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

The name of the IP set. You cannot change the name of an `IPSet` after you create it.

`--scope` (string)

Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use `CLOUDFRONT` .

To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

- CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1` .
- API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

- `CLOUDFRONT`
- `REGIONAL`

`--id` (string)

A unique identifier for the set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

`--description` (string)

A description of the IP set that helps with identification.

`--addresses` (list)

Contains an array of strings that specifies zero or more IP addresses or blocks of IP addresses that you want WAF to inspect for in incoming requests. All addresses must be specified using Classless Inter-Domain Routing (CIDR) notation. WAF supports all IPv4 and IPv6 CIDR ranges except for `/0` .

Example address strings:

- For requests that originated from the IP address 192.0.2.44, specify `192.0.2.44/32` .
- For requests that originated from IP addresses from 192.0.2.0 to 192.0.2.255, specify `192.0.2.0/24` .
- For requests that originated from the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify `1111:0000:0000:0000:0000:0000:0000:0111/128` .
- For requests that originated from IP addresses 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify `1111:0000:0000:0000:0000:0000:0000:0000/64` .

For more information about CIDR notation, see the Wikipedia entry [Classless Inter-Domain Routing](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) .

Example JSON `Addresses` specifications:

- Empty array: `"Addresses": []`
- Array with one address: `"Addresses": ["192.0.2.44/32"]`
- Array with three addresses: `"Addresses": ["192.0.2.44/32", "192.0.2.0/24", "192.0.0.0/16"]`
- INVALID specification: `"Addresses": [""]` INVALID

(string)

Syntax:

```
"string" "string" ...
```

`--lock-token` (string)

A token used for optimistic locking. WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete` . WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException` . If this happens, perform another `get` , and use the new token returned by that operation.

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

**To modify the settings for an existing IP set**

The following `update-ip-set` updates the settings for the specified IP set. This call requires an ID, which you can obtain from the call, `list-ip-sets`, and a lock token which you can obtain from the calls, `list-ip-sets` and `get-ip-set`. This call also returns a lock token that you can use for a subsequent update.

```
aws wafv2 update-ip-set \
    --name testip \
    --scope REGIONAL \
    --id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --addresses 198.51.100.0/16 \
    --lock-token 447e55ac-2396-4c6d-b9f9-86b67c17f8b5
```

Output:

```
{
    "NextLockToken": "0674c84b-0304-47fe-8728-c6bff46af8fc"
}
```

For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

NextLockToken -> (string)

A token used for optimistic locking. WAF returns this token to your `update` requests. You use `NextLockToken` in the same manner as you use `LockToken` .