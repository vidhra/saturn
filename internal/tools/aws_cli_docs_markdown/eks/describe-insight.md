# describe-insightÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-insight.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-insight.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [eks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/index.html#cli-aws-eks) ]

# describe-insight

## Description

Returns details about an insight that you specify using its ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eks-2017-11-01/DescribeInsight)

## Synopsis

```
describe-insight
--cluster-name <value>
--id <value>
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

`--cluster-name` (string)

The name of the cluster to describe the insight for.

`--id` (string)

The identity of the insight to describe.

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

insight -> (structure)

The full description of the insight.

id -> (string)

The ID of the insight.

name -> (string)

The name of the insight.

category -> (string)

The category of the insight.

kubernetesVersion -> (string)

The Kubernetes minor version associated with an insight if applicable.

lastRefreshTime -> (timestamp)

The time Amazon EKS last successfully completed a refresh of this insight check on the cluster.

lastTransitionTime -> (timestamp)

The time the status of the insight last changed.

description -> (string)

The description of the insight which includes alert criteria, remediation recommendation, and additional resources (contains Markdown).

insightStatus -> (structure)

An object containing more detail on the status of the insight resource.

status -> (string)

The status of the resource.

reason -> (string)

Explanation on the reasoning for the status of the resource.

recommendation -> (string)

A summary of how to remediate the finding of this insight if applicable.

additionalInfo -> (map)

Links to sources that provide additional context on the insight.

key -> (string)

value -> (string)

resources -> (list)

The details about each resource listed in the insight check result.

(structure)

Returns information about the resource being evaluated.

insightStatus -> (structure)

An object containing more detail on the status of the insight resource.

status -> (string)

The status of the resource.

reason -> (string)

Explanation on the reasoning for the status of the resource.

kubernetesResourceUri -> (string)

The Kubernetes resource URI if applicable.

arn -> (string)

The Amazon Resource Name (ARN) if applicable.

categorySpecificSummary -> (structure)

Summary information that relates to the category of the insight. Currently only returned with certain insights having category `UPGRADE_READINESS` .

deprecationDetails -> (list)

The summary information about deprecated resource usage for an insight check in the `UPGRADE_READINESS` category.

(structure)

The summary information about deprecated resource usage for an insight check in the `UPGRADE_READINESS` category.

usage -> (string)

The deprecated version of the resource.

replacedWith -> (string)

The newer version of the resource to migrate to if applicable.

stopServingVersion -> (string)

The version of the software where the deprecated resource version will stop being served.

startServingReplacementVersion -> (string)

The version of the software where the newer resource version became available to migrate to if applicable.

clientStats -> (list)

Details about Kubernetes clients using the deprecated resources.

(structure)

Details about clients using the deprecated resources.

userAgent -> (string)

The user agent of the Kubernetes client using the deprecated resource.

numberOfRequestsLast30Days -> (integer)

The number of requests from the Kubernetes client seen over the last 30 days.

lastRequestTime -> (timestamp)

The timestamp of the last request seen from the Kubernetes client.

addonCompatibilityDetails -> (list)

A list of `AddonCompatibilityDetail` objects for Amazon EKS add-ons.

(structure)

The summary information about the Amazon EKS add-on compatibility for the next Kubernetes version for an insight check in the `UPGRADE_READINESS` category.

name -> (string)

The name of the Amazon EKS add-on.

compatibleVersions -> (list)

The list of compatible Amazon EKS add-on versions for the next Kubernetes version.

(string)