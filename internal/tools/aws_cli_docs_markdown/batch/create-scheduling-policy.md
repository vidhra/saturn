# create-scheduling-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-scheduling-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-scheduling-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# create-scheduling-policy

## Description

Creates an Batch scheduling policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/CreateSchedulingPolicy)

## Synopsis

```
create-scheduling-policy
--name <value>
[--fairshare-policy <value>]
[--tags <value>]
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

The name of the fair-share scheduling policy. It can be up to 128 letters long. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (_).

`--fairshare-policy` (structure)

The fair-share scheduling policy details.

shareDecaySeconds -> (integer)

The amount of time (in seconds) to use to calculate a fair-share percentage for each share identifier in use. A value of zero (0) indicates the default minimum time window (600 seconds). The maximum supported value is 604800 (1 week).

The decay allows for more recently run jobs to have more weight than jobs that ran earlier. Consider adjusting this number if you have jobs that (on average) run longer than ten minutes, or a large difference in job count or job run times between share identifiers, and the allocation of resources doesnât meet your needs.

computeReservation -> (integer)

A value used to reserve some of the available maximum vCPU for share identifiers that arenât already used.

The reserved ratio is [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-scheduling-policy.html#id1)(*computeReservation* /100)^*ActiveFairShares* `` where `` *ActiveFairShares* `` is the number of active share identifiers.

For example, a `computeReservation` value of 50 indicates that Batch reserves 50% of the maximum available vCPU if thereâs only one share identifier. It reserves 25% if there are two share identifiers. It reserves 12.5% if there are three share identifiers. A `computeReservation` value of 25 indicates that Batch should reserve 25% of the maximum available vCPU if thereâs only one share identifier, 6.25% if there are two fair share identifiers, and 1.56% if there are three share identifiers.

The minimum value is 0 and the maximum value is 99.

shareDistribution -> (list)

An array of `SharedIdentifier` objects that contain the weights for the share identifiers for the fair-share policy. Share identifiers that arenât included have a default weight of `1.0` .

(structure)

Specifies the weights for the share identifiers for the fair-share policy. Share identifiers that arenât included have a default weight of `1.0` .

shareIdentifier -> (string)

A share identifier or share identifier prefix. If the string ends with an asterisk (*), this entry specifies the weight factor to use for share identifiers that start with that prefix. The list of share identifiers in a fair-share policy canât overlap. For example, you canât have one that specifies a `shareIdentifier` of `UserA*` and another that specifies a `shareIdentifier` of `UserA-1` .

There can be no more than 500 share identifiers active in a job queue.

The string is limited to 255 alphanumeric characters, and can be followed by an asterisk (*).

weightFactor -> (float)

The weight factor for the share identifier. The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1.

The smallest supported value is 0.0001, and the largest supported value is 999.9999.

Shorthand Syntax:

```
shareDecaySeconds=integer,computeReservation=integer,shareDistribution=[{shareIdentifier=string,weightFactor=float},{shareIdentifier=string,weightFactor=float}]
```

JSON Syntax:

```
{
  "shareDecaySeconds": integer,
  "computeReservation": integer,
  "shareDistribution": [
    {
      "shareIdentifier": "string",
      "weightFactor": float
    }
    ...
  ]
}
```

`--tags` (map)

The tags that you apply to the scheduling policy to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in *Amazon Web Services General Reference* .

These tags can be updated or removed using the [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html) API operations.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

name -> (string)

The name of the scheduling policy.

arn -> (string)

The Amazon Resource Name (ARN) of the scheduling policy. The format is `aws:*Partition* :batch:*Region* :*Account* :scheduling-policy/*Name* `` . For example, ``aws:aws:batch:us-west-2:123456789012:scheduling-policy/MySchedulingPolicy` .