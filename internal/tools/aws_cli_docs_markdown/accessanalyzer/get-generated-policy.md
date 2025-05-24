# get-generated-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-generated-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-generated-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [accessanalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html#cli-aws-accessanalyzer) ]

# get-generated-policy

## Description

Retrieves the policy that was generated using `StartPolicyGeneration` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/accessanalyzer-2019-11-01/GetGeneratedPolicy)

## Synopsis

```
get-generated-policy
--job-id <value>
[--include-resource-placeholders | --no-include-resource-placeholders]
[--include-service-level-template | --no-include-service-level-template]
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

`--job-id` (string)

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

`--include-resource-placeholders` | `--no-include-resource-placeholders` (boolean)

The level of detail that you want to generate. You can specify whether to generate policies with placeholders for resource ARNs for actions that support resource level granularity in policies.

For example, in the resource section of a policy, you can receive a placeholder such as `"Resource":"arn:aws:s3:::${BucketName}"` instead of `"*"` .

`--include-service-level-template` | `--no-include-service-level-template` (boolean)

The level of detail that you want to generate. You can specify whether to generate service-level policies.

IAM Access Analyzer uses `iam:servicelastaccessed` to identify services that have been used recently to create this service-level template.

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

**To retrieve the policy that was generated using the `StartPolicyGeneration` API**

The following `get-generated-policy` example retrieves the policy that was generated using the StartPolicyGeneration API in your AWS account.

```
aws accessanalyzer get-generated-policy \
    --job-id c557dc4a-0338-4489-95dd-739014860ff9
```

Output:

```
{
    "generatedPolicyResult": {
        "generatedPolicies": [
            {
                "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"SupportedServiceSid0\",\"Effect\":\"Allow\",\"Action\":[\"access-analyzer:GetAnalyzer\",\"access-analyzer:ListAnalyzers\",\"access-analyzer:ListArchiveRules\",\"access-analyzer:ListFindings\",\"cloudtrail:DescribeTrails\",\"cloudtrail:GetEventDataStore\",\"cloudtrail:GetEventSelectors\",\"cloudtrail:GetInsightSelectors\",\"cloudtrail:GetTrailStatus\",\"cloudtrail:ListChannels\",\"cloudtrail:ListEventDataStores\",\"cloudtrail:ListQueries\",\"cloudtrail:ListTags\",\"cloudtrail:LookupEvents\",\"ec2:DescribeRegions\",\"iam:GetAccountSummary\",\"iam:GetOpenIDConnectProvider\",\"iam:GetRole\",\"iam:ListAccessKeys\",\"iam:ListAccountAliases\",\"iam:ListOpenIDConnectProviders\",\"iam:ListRoles\",\"iam:ListSAMLProviders\",\"kms:ListAliases\",\"s3:GetBucketLocation\",\"s3:ListAllMyBuckets\"],\"Resource\":\"*\"}]}"
            }
        ],
        "properties": {
            "cloudTrailProperties": {
                "endTime": "2024-02-14T22:44:40+00:00",
                "startTime": "2024-02-13T00:30:00+00:00",
                "trailProperties": [
                    {
                        "allRegions": true,
                        "cloudTrailArn": "arn:aws:cloudtrail:us-west-2:111122223333:trail/my-trail",
                        "regions": []
                    }
                ]
            },
            "isComplete": false,
            "principalArn": "arn:aws:iam::111122223333:role/Admin"
        }
    },
    "jobDetails": {
        "completedOn": "2024-02-14T22:47:01+00:00",
        "jobId": "c557dc4a-0338-4489-95dd-739014860ff9",
        "startedOn": "2024-02-14T22:44:41+00:00",
        "status": "SUCCEEDED"
    }
}
```

For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) in the *AWS IAM User Guide*.

## Output

jobDetails -> (structure)

A `GeneratedPolicyDetails` object that contains details about the generated policy.

jobId -> (string)

The `JobId` that is returned by the `StartPolicyGeneration` operation. The `JobId` can be used with `GetGeneratedPolicy` to retrieve the generated policies or used with `CancelPolicyGeneration` to cancel the policy generation request.

status -> (string)

The status of the job request.

startedOn -> (timestamp)

A timestamp of when the job was started.

completedOn -> (timestamp)

A timestamp of when the job was completed.

jobError -> (structure)

The job error for the policy generation request.

code -> (string)

The job error code.

message -> (string)

Specific information about the error. For example, which service quota was exceeded or which resource was not found.

generatedPolicyResult -> (structure)

A `GeneratedPolicyResult` object that contains the generated policies and associated details.

properties -> (structure)

A `GeneratedPolicyProperties` object that contains properties of the generated policy.

isComplete -> (boolean)

This value is set to `true` if the generated policy contains all possible actions for a service that IAM Access Analyzer identified from the CloudTrail trail that you specified, and `false` otherwise.

principalArn -> (string)

The ARN of the IAM entity (user or role) for which you are generating a policy.

cloudTrailProperties -> (structure)

Lists details about the `Trail` used to generated policy.

trailProperties -> (list)

A `TrailProperties` object that contains settings for trail properties.

(structure)

Contains details about the CloudTrail trail being analyzed to generate a policy.

cloudTrailArn -> (string)

Specifies the ARN of the trail. The format of a trail ARN is `arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail` .

regions -> (list)

A list of regions to get CloudTrail data from and analyze to generate a policy.

(string)

allRegions -> (boolean)

Possible values are `true` or `false` . If set to `true` , IAM Access Analyzer retrieves CloudTrail data from all regions to analyze and generate a policy.

startTime -> (timestamp)

The start of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp before this time are not considered to generate a policy.

endTime -> (timestamp)

The end of the time range for which IAM Access Analyzer reviews your CloudTrail events. Events with a timestamp after this time are not considered to generate a policy. If this is not included in the request, the default value is the current time.

generatedPolicies -> (list)

The text to use as the content for the new policy. The policy is created using the [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html) action.

(structure)

Contains the text for the generated policy.

policy -> (string)

The text to use as the content for the new policy. The policy is created using the [CreatePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicy.html) action.