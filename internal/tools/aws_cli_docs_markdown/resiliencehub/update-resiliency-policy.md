# update-resiliency-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/update-resiliency-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/update-resiliency-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# update-resiliency-policy

## Description

Updates a resiliency policy.

### Note

Resilience Hub allows you to provide a value of zero for `rtoInSecs` and `rpoInSecs` of your resiliency policy. But, while assessing your application, the lowest possible assessment result is near zero. Hence, if you provide value zero for `rtoInSecs` and `rpoInSecs` , the estimated workload RTO and estimated workload RPO result will be near zero and the **Compliance status** for your application will be set to **Policy breached** .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/UpdateResiliencyPolicy)

## Synopsis

```
update-resiliency-policy
[--data-location-constraint <value>]
[--policy <value>]
--policy-arn <value>
[--policy-description <value>]
[--policy-name <value>]
[--tier <value>]
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

`--data-location-constraint` (string)

Specifies a high-level geographical location constraint for where your resilience policy data can be stored.

Possible values:

- `AnyLocation`
- `SameContinent`
- `SameCountry`

`--policy` (map)

Resiliency policy to be created, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.

key -> (string)

value -> (structure)

Defines a failure policy.

rpoInSecs -> (integer)

Recovery Point Objective (RPO) in seconds.

rtoInSecs -> (integer)

Recovery Time Objective (RTO) in seconds.

Shorthand Syntax:

```
KeyName1=rpoInSecs=integer,rtoInSecs=integer,KeyName2=rpoInSecs=integer,rtoInSecs=integer

Where valid key names are:
  Software
  Hardware
  AZ
  Region
```

JSON Syntax:

```
{"Software"|"Hardware"|"AZ"|"Region": {
      "rpoInSecs": integer,
      "rtoInSecs": integer
    }
  ...}
```

`--policy-arn` (string)

Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :resiliency-policy/`policy-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

`--policy-description` (string)

Description of the resiliency policy.

`--policy-name` (string)

Name of the resiliency policy.

`--tier` (string)

The tier for this resiliency policy, ranging from the highest severity (`MissionCritical` ) to lowest (`NonCritical` ).

Possible values:

- `MissionCritical`
- `Critical`
- `Important`
- `CoreServices`
- `NonCritical`
- `NotApplicable`

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

policy -> (structure)

The resiliency policy that was updated, including the recovery time objective (RTO) and recovery point objective (RPO) in seconds.

creationTime -> (timestamp)

Date and time when the resiliency policy was created.

dataLocationConstraint -> (string)

Specifies a high-level geographical location constraint for where your resilience policy data can be stored.

estimatedCostTier -> (string)

Specifies the estimated cost tier of the resiliency policy.

policy -> (map)

The resiliency policy.

key -> (string)

value -> (structure)

Defines a failure policy.

rpoInSecs -> (integer)

Recovery Point Objective (RPO) in seconds.

rtoInSecs -> (integer)

Recovery Time Objective (RTO) in seconds.

policyArn -> (string)

Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :resiliency-policy/`policy-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

policyDescription -> (string)

Description of the resiliency policy.

policyName -> (string)

The name of the policy

tags -> (map)

Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.

key -> (string)

value -> (string)

tier -> (string)

The tier for this resiliency policy, ranging from the highest severity (`MissionCritical` ) to lowest (`NonCritical` ).