# create-continuous-deployment-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-continuous-deployment-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-continuous-deployment-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# create-continuous-deployment-policy

## Description

Creates a continuous deployment policy that distributes traffic for a custom domain name to two different CloudFront distributions.

To use a continuous deployment policy, first use `CopyDistribution` to create a staging distribution, then use `UpdateDistribution` to modify the staging distributionâs configuration.

After you create and update a staging distribution, you can use a continuous deployment policy to incrementally move traffic to the staging distribution. This workflow enables you to test changes to a distributionâs configuration before moving all of your domainâs production traffic to the new configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/CreateContinuousDeploymentPolicy)

## Synopsis

```
create-continuous-deployment-policy
--continuous-deployment-policy-config <value>
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

`--continuous-deployment-policy-config` (structure)

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

JSON Syntax:

```
{
  "StagingDistributionDnsNames": {
    "Quantity": integer,
    "Items": ["string", ...]
  },
  "Enabled": true|false,
  "TrafficConfig": {
    "SingleWeightConfig": {
      "Weight": float,
      "SessionStickinessConfig": {
        "IdleTTL": integer,
        "MaximumTTL": integer
      }
    },
    "SingleHeaderConfig": {
      "Header": "string",
      "Value": "string"
    },
    "Type": "SingleWeight"|"SingleHeader"
  }
}
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

## Output

ContinuousDeploymentPolicy -> (structure)

A continuous deployment policy.

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

Location -> (string)

The location of the continuous deployment policy.

ETag -> (string)

The version identifier for the current version of the continuous deployment policy.