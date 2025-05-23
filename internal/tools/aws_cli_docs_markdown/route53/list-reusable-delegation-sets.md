# list-reusable-delegation-setsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-reusable-delegation-sets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-reusable-delegation-sets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-reusable-delegation-sets

## Description

Retrieves a list of the reusable delegation sets that are associated with the current Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListReusableDelegationSets)

## Synopsis

```
list-reusable-delegation-sets
[--marker <value>]
[--max-items <value>]
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

`--marker` (string)

If the value of `IsTruncated` in the previous response was `true` , you have more reusable delegation sets. To get another group, submit another `ListReusableDelegationSets` request.

For the value of `marker` , specify the value of `NextMarker` from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.

If the value of `IsTruncated` in the previous response was `false` , there are no more reusable delegation sets to get.

`--max-items` (string)

The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.

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

DelegationSets -> (list)

A complex type that contains one `DelegationSet` element for each reusable delegation set that was created by the current Amazon Web Services account.

(structure)

A complex type that lists the name servers in a delegation set, as well as the `CallerReference` and the `ID` for the delegation set.

Id -> (string)

The ID that Amazon Route 53 assigns to a reusable delegation set.

CallerReference -> (string)

The value that you specified for `CallerReference` when you created the reusable delegation set.

NameServers -> (list)

A complex type that contains a list of the authoritative name servers for a hosted zone or for a reusable delegation set.

(string)

Marker -> (string)

For the second and subsequent calls to `ListReusableDelegationSets` , `Marker` is the value that you specified for the `marker` parameter in the request that produced the current response.

IsTruncated -> (boolean)

A flag that indicates whether there are more reusable delegation sets to be listed.

NextMarker -> (string)

If `IsTruncated` is `true` , the value of `NextMarker` identifies the next reusable delegation set that Amazon Route 53 will return if you submit another `ListReusableDelegationSets` request and specify the value of `NextMarker` in the `marker` parameter.

MaxItems -> (string)

The value that you specified for the `maxitems` parameter in the call to `ListReusableDelegationSets` that produced the current response.