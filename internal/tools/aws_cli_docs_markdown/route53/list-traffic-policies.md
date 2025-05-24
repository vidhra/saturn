# list-traffic-policiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/index.html#cli-aws-route53) ]

# list-traffic-policies

## Description

Gets information about the latest version for every traffic policy that is associated with the current Amazon Web Services account. Policies are listed in the order that they were created in.

For information about how of deleting a traffic policy affects the response from `ListTrafficPolicies` , see [DeleteTrafficPolicy](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/ListTrafficPolicies)

## Synopsis

```
list-traffic-policies
[--traffic-policy-id-marker <value>]
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

`--traffic-policy-id-marker` (string)

(Conditional) For your first request to `ListTrafficPolicies` , donât include the `TrafficPolicyIdMarker` parameter.

If you have more traffic policies than the value of `MaxItems` , `ListTrafficPolicies` returns only the first `MaxItems` traffic policies. To get the next group of policies, submit another request to `ListTrafficPolicies` . For the value of `TrafficPolicyIdMarker` , specify the value of `TrafficPolicyIdMarker` that was returned in the previous response.

`--max-items` (string)

(Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than `MaxItems` traffic policies, the value of `IsTruncated` in the response is `true` , and the value of `TrafficPolicyIdMarker` is the ID of the first traffic policy that Route 53 will return if you submit another request.

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

TrafficPolicySummaries -> (list)

A list that contains one `TrafficPolicySummary` element for each traffic policy that was created by the current Amazon Web Services account.

(structure)

A complex type that contains information about the latest version of one traffic policy that is associated with the current Amazon Web Services account.

Id -> (string)

The ID that Amazon Route 53 assigned to the traffic policy when you created it.

Name -> (string)

The name that you specified for the traffic policy when you created it.

Type -> (string)

The DNS type of the resource record sets that Amazon Route 53 creates when you use a traffic policy to create a traffic policy instance.

LatestVersion -> (integer)

The version number of the latest version of the traffic policy.

TrafficPolicyCount -> (integer)

The number of traffic policies that are associated with the current Amazon Web Services account.

IsTruncated -> (boolean)

A flag that indicates whether there are more traffic policies to be listed. If the response was truncated, you can get the next group of traffic policies by submitting another `ListTrafficPolicies` request and specifying the value of `TrafficPolicyIdMarker` in the `TrafficPolicyIdMarker` request parameter.

TrafficPolicyIdMarker -> (string)

If the value of `IsTruncated` is `true` , `TrafficPolicyIdMarker` is the ID of the first traffic policy in the next group of `MaxItems` traffic policies.

MaxItems -> (string)

The value that you specified for the `MaxItems` parameter in the `ListTrafficPolicies` request that produced the current response.