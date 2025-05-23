# get-resources-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-resources-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/get-resources-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# get-resources-summary

## Description

Get counts of Proton resources.

For infrastructure-provisioning resources (environments, services, service instances, pipelines), the action returns staleness counts. A resource is stale when itâs behind the recommended version of the Proton template that it uses and it needs an update to become current.

The action returns staleness counts (counts of resources that are up-to-date, behind a template major version, or behind a template minor version), the total number of resources, and the number of resources that are in a failed state, grouped by resource type. Components, environments, and service templates return less information - see the `components` , `environments` , and `serviceTemplates` field descriptions.

For context, the action also returns the total number of each type of Proton template in the Amazon Web Services account.

For more information, see [Proton dashboard](https://docs.aws.amazon.com/proton/latest/userguide/monitoring-dashboard.html) in the *Proton User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/GetResourcesSummary)

## Synopsis

```
get-resources-summary
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

counts -> (structure)

Summary counts of each Proton resource type.

components -> (structure)

The total number of components in the Amazon Web Services account.

The semantics of the `components` field are different from the semantics of results for other infrastructure-provisioning resources. Thatâs because at this time components donât have associated templates, therefore they donât have the concept of staleness. The `components` object will only contain `total` and `failed` members.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.

environmentTemplates -> (structure)

The total number of environment templates in the Amazon Web Services account. The `environmentTemplates` object will only contain `total` members.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.

environments -> (structure)

The staleness counts for Proton environments in the Amazon Web Services account. The `environments` object will only contain `total` members.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.

pipelines -> (structure)

The staleness counts for Proton pipelines in the Amazon Web Services account.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.

serviceInstances -> (structure)

The staleness counts for Proton service instances in the Amazon Web Services account.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.

serviceTemplates -> (structure)

The total number of service templates in the Amazon Web Services account. The `serviceTemplates` object will only contain `total` members.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.

services -> (structure)

The staleness counts for Proton services in the Amazon Web Services account.

behindMajor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a major template version update.

behindMinor -> (integer)

The number of resources of this type in the Amazon Web Services account that need a minor template version update.

failed -> (integer)

The number of resources of this type in the Amazon Web Services account that failed to deploy.

total -> (integer)

The total number of resources of this type in the Amazon Web Services account.

upToDate -> (integer)

The number of resources of this type in the Amazon Web Services account that are up-to-date with their template.