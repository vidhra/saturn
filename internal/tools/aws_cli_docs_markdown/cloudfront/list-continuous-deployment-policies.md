# list-continuous-deployment-policiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-continuous-deployment-policies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-continuous-deployment-policies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# list-continuous-deployment-policies

## Description

Gets a list of the continuous deployment policies in your Amazon Web Services account.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/ListContinuousDeploymentPolicies)

## Synopsis

```
list-continuous-deployment-policies
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

Use this field when paginating results to indicate where to begin in your list of continuous deployment policies. The response includes policies in the list that occur after the marker. To get the next page of the list, set this fieldâs value to the value of `NextMarker` from the current pageâs response.

`--max-items` (string)

The maximum number of continuous deployment policies that you want returned in the response.

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

ContinuousDeploymentPolicyList -> (structure)

A list of continuous deployment policies.

NextMarker -> (string)

Indicates the next page of continuous deployment policies. To get the next page of the list, use this value in the `Marker` field of your request.

MaxItems -> (integer)

The maximum number of continuous deployment policies that were specified in your request.

Quantity -> (integer)

The total number of continuous deployment policies in your Amazon Web Services account, regardless of the `MaxItems` value.

Items -> (list)

A list of continuous deployment policy items.

(structure)

A summary of the information about your continuous deployment policies.

ContinuousDeploymentPolicy -> (structure)

The continuous deployment policy.

Id -> (string)

The identifier of the continuous deployment policy.

LastModifiedTime -> (timestamp)

The date and time the continuous deployment policy was last modified.

ContinuousDeploymentPolicyConfig -> (structure)

Contains the configuration for a continuous deployment policy.

StagingDistributionDnsNames -> (structure)

The CloudFront domain name of the staging distribution. For example: `d111111abcdef8.cloudfront.net` .

Quantity -> (integer)

The number of CloudFront domain names in your staging distribution.

Items -> (list)

The CloudFront domain name of the staging distribution.

(string)

Enabled -> (boolean)

A Boolean that indicates whether this continuous deployment policy is enabled (in effect). When this value is `true` , this policy is enabled and in effect. When this value is `false` , this policy is not enabled and has no effect.

TrafficConfig -> (structure)

Contains the parameters for routing production traffic from your primary to staging distributions.

SingleWeightConfig -> (structure)

Contains the percentage of traffic to send to the staging distribution.

Weight -> (float)

The percentage of traffic to send to a staging distribution, expressed as a decimal number between 0 and 0.15. For example, a value of 0.10 means 10% of traffic is sent to the staging distribution.

SessionStickinessConfig -> (structure)

Session stickiness provides the ability to define multiple requests from a single viewer as a single session. This prevents the potentially inconsistent experience of sending some of a given userâs requests to your staging distribution, while others are sent to your primary distribution. Define the session duration using TTL values.

IdleTTL -> (integer)

The amount of time after which you want sessions to cease if no requests are received. Allowed values are 300â3600 seconds (5â60 minutes).

The value must be less than or equal to `MaximumTTL` .

MaximumTTL -> (integer)

The maximum amount of time to consider requests from the viewer as being part of the same session. Allowed values are 300â3600 seconds (5â60 minutes).

The value must be greater than or equal to `IdleTTL` .

SingleHeaderConfig -> (structure)

Determines which HTTP requests are sent to the staging distribution.

Header -> (string)

The request header name that you want CloudFront to send to your staging distribution. The header must contain the prefix `aws-cf-cd-` .

Value -> (string)

The request header value.

Type -> (string)

The type of traffic configuration.