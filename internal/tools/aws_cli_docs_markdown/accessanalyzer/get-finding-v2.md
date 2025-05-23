# get-finding-v2Â¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding-v2.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding-v2.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [accessanalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html#cli-aws-accessanalyzer) ]

# get-finding-v2

## Description

Retrieves information about the specified finding. GetFinding and GetFindingV2 both use `access-analyzer:GetFinding` in the `Action` element of an IAM policy statement. You must have permission to perform the `access-analyzer:GetFinding` action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/accessanalyzer-2019-11-01/GetFindingV2)

`get-finding-v2` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `findingDetails`

## Synopsis

```
get-finding-v2
--analyzer-arn <value>
--id <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--analyzer-arn` (string)

The [ARN of the analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources) that generated the finding.

`--id` (string)

The ID of the finding to retrieve.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To retrieve information about the specified finding**

The following `get-finding-v2` example etrieves information about the specified finding in your AWS account.

```
aws accessanalyzer get-finding-v2 \
    --analyzer-arn arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-organization \
    --id 0910eedb-381e-4e95-adda-0d25c19e6e90
```

Output:

```
{
    "findingDetails": [
        {
            "externalAccessDetails": {
                "action": [
                    "sts:AssumeRoleWithWebIdentity"
                ],
                "condition": {
                    "cognito-identity.amazonaws.com:aud": "us-west-2:EXAMPLE0-0000-0000-0000-000000000000"
                },
                "isPublic": false,
                "principal": {
                    "Federated": "cognito-identity.amazonaws.com"
                }
            }
        }
    ],
    "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolAuth_Role",
    "status": "ACTIVE",
    "error": null,
    "createdAt": "2021-02-26T21:17:50.905000+00:00",
    "resourceType": "AWS::IAM::Role",
    "findingType": "ExternalAccess",
    "resourceOwnerAccount": "111122223333",
    "analyzedAt": "2024-02-16T18:17:47.888000+00:00",
    "id": "0910eedb-381e-4e95-adda-0d25c19e6e90",
    "updatedAt": "2021-02-26T21:17:50.905000+00:00"
}
```

For more information, see [Reviewing findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html) in the *AWS IAM User Guide*.

## Output

analyzedAt -> (timestamp)

The time at which the resource-based policy or IAM entity that generated the finding was analyzed.

createdAt -> (timestamp)

The time at which the finding was created.

error -> (string)

An error.

id -> (string)

The ID of the finding to retrieve.

nextToken -> (string)

A token used for pagination of results returned.

resource -> (string)

The resource that generated the finding.

resourceType -> (string)

The type of the resource identified in the finding.

resourceOwnerAccount -> (string)

Tye Amazon Web Services account ID that owns the resource.

status -> (string)

The status of the finding.

updatedAt -> (timestamp)

The time at which the finding was updated.

findingDetails -> (list)

A localized message that explains the finding and provides guidance on how to address it.

(tagged union structure)

Contains information about an external access or unused access finding. Only one parameter can be used in a `FindingDetails` object.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `externalAccessDetails`, `unusedPermissionDetails`, `unusedIamUserAccessKeyDetails`, `unusedIamRoleDetails`, `unusedIamUserPasswordDetails`.

externalAccessDetails -> (structure)

The details for an external access analyzer finding.

action -> (list)

The action in the analyzed policy statement that an external principal has permission to use.

(string)

condition -> (map)

The condition in the analyzed policy statement that resulted in an external access finding.

key -> (string)

value -> (string)

isPublic -> (boolean)

Specifies whether the external access finding is public.

principal -> (map)

The external principal that has access to a resource within the zone of trust.

key -> (string)

value -> (string)

sources -> (list)

The sources of the external access finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

(structure)

The source of the finding. This indicates how the access that generated the finding is granted. It is populated for Amazon S3 bucket findings.

type -> (string)

Indicates the type of access that generated the finding.

detail -> (structure)

Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.

accessPointArn -> (string)

The ARN of the access point that generated the finding. The ARN format depends on whether the ARN represents an access point or a multi-region access point.

accessPointAccount -> (string)

The account of the cross-account access point that generated the finding.

resourceControlPolicyRestriction -> (string)

The type of restriction applied to the finding by the resource owner with an Organizations resource control policy (RCP).

unusedPermissionDetails -> (structure)

The details for an unused access analyzer finding with an unused permission finding type.

actions -> (list)

A list of unused actions for which the unused access finding was generated.

(structure)

Contains information about an unused access finding for an action. IAM Access Analyzer charges for unused access analysis based on the number of IAM roles and users analyzed per month. For more details on pricing, see [IAM Access Analyzer pricing](https://aws.amazon.com/iam/access-analyzer/pricing) .

action -> (string)

The action for which the unused access finding was generated.

lastAccessed -> (timestamp)

The time at which the action was last accessed.

serviceNamespace -> (string)

The namespace of the Amazon Web Services service that contains the unused actions.

lastAccessed -> (timestamp)

The time at which the permission was last accessed.

unusedIamUserAccessKeyDetails -> (structure)

The details for an unused access analyzer finding with an unused IAM user access key finding type.

accessKeyId -> (string)

The ID of the access key for which the unused access finding was generated.

lastAccessed -> (timestamp)

The time at which the access key was last accessed.

unusedIamRoleDetails -> (structure)

The details for an unused access analyzer finding with an unused IAM role finding type.

lastAccessed -> (timestamp)

The time at which the role was last accessed.

unusedIamUserPasswordDetails -> (structure)

The details for an unused access analyzer finding with an unused IAM user password finding type.

lastAccessed -> (timestamp)

The time at which the password was last accessed.

findingType -> (string)

The type of the finding. For external access analyzers, the type is `ExternalAccess` . For unused access analyzers, the type can be `UnusedIAMRole` , `UnusedIAMUserAccessKey` , `UnusedIAMUserPassword` , or `UnusedPermission` .