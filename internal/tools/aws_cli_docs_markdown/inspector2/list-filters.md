# list-filtersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-filters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-filters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# list-filters

## Description

Lists the filters associated with your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/ListFilters)

`list-filters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `filters`

## Synopsis

```
list-filters
[--action <value>]
[--arns <value>]
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

`--action` (string)

The action the filter applies to matched findings.

Possible values:

- `NONE`
- `SUPPRESS`

`--arns` (list)

The Amazon resource number (ARN) of the filter.

(string)

Syntax:

```
"string" "string" ...
```

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

**To list filters associated with the account that you used to activated Amazon Inspector**

The following `list-filters` examples lists filters associated with the account that you used to activated Amazon Inspector.

```
aws inspector2 list-filters
```

Output:

```
{
    "filters": [
        {
            "action": "SUPPRESS",
            "arn": "arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444",
            "createdAt": "2024-05-15T21:11:08.602000+00:00",
            "criteria": {
                "resourceType": [
                    {
                        "comparison": "EQUALS",
                        "value": "AWS_EC2_INSTANCE"
                    },
                ]
            },
            "description": "This suppression rule omits EC2 instance type findings",
            "name": "ExampleSuppressionRuleEC2",
            "ownerId": "o-EXAMPLE222",
            "tags": {},
            "updatedAt": "2024-05-15T21:11:08.602000+00:00"
        },
        {
            "action": "SUPPRESS",
            "arn": "arn:aws:inspector2:us-east-1:813737243517:owner/o-EXAMPLE222/filter/EXAMPLE444444444",
            "createdAt": "2024-05-15T21:28:27.054000+00:00",
            "criteria": {
                "resourceType": [
                    {
                        "comparison": "EQUALS",
                        "value": "AWS_ECR_INSTANCE"
                    }
                ]
            },
            "description": "This suppression rule omits ECR instance type findings",
            "name": "ExampleSuppressionRuleECR",
            "ownerId": "o-EXAMPLE222",
            "tags": {},
            "updatedAt": "2024-05-15T21:28:27.054000+00:00"
        }
    ]
}
```

For more information, see [Filtering Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-filtering.html) in the *Amazon Inspector User Guide*.

## Output

filters -> (list)

Contains details on the filters associated with your account.

(structure)

Details about a filter.

action -> (string)

The action that is to be applied to the findings that match the filter.

arn -> (string)

The Amazon Resource Number (ARN) associated with this filter.

createdAt -> (timestamp)

The date and time this filter was created at.

criteria -> (structure)

Details on the filter criteria associated with this filter.

awsAccountId -> (list)

Details of the Amazon Web Services account IDs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

codeVulnerabilityDetectorName -> (list)

The name of the detector used to identify a code vulnerability in a Lambda function used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

codeVulnerabilityDetectorTags -> (list)

The detector type tag associated with the vulnerability used to filter findings. Detector tags group related vulnerabilities by common themes or tactics. For a list of available tags by programming language, see [Java tags](https://docs.aws.amazon.com/codeguru/detector-library/java/tags/) , or [Python tags](https://docs.aws.amazon.com/codeguru/detector-library/python/tags/) .

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

codeVulnerabilityFilePath -> (list)

The file path to the file in a Lambda function that contains a code vulnerability used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

componentId -> (list)

Details of the component IDs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

componentType -> (list)

Details of the component types used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ec2InstanceImageId -> (list)

Details of the Amazon EC2 instance image IDs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ec2InstanceSubnetId -> (list)

Details of the Amazon EC2 instance subnet IDs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ec2InstanceVpcId -> (list)

Details of the Amazon EC2 instance VPC IDs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ecrImageArchitecture -> (list)

Details of the Amazon ECR image architecture types used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ecrImageHash -> (list)

Details of the Amazon ECR image hashes used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ecrImageInUseCount -> (list)

Filter criteria indicating when details for an Amazon ECR image include when an Amazon ECR image is in use.

(structure)

An object that describes the details of a number filter.

lowerInclusive -> (double)

The lowest number to be included in the filter.

upperInclusive -> (double)

The highest number to be included in the filter.

ecrImageLastInUseAt -> (list)

Filter criteria indicating when an Amazon ECR image was last used in an Amazon ECS cluster task or Amazon EKS cluster pod.

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

ecrImagePushedAt -> (list)

Details on the Amazon ECR image push date and time used to filter findings.

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

ecrImageRegistry -> (list)

Details on the Amazon ECR registry used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ecrImageRepositoryName -> (list)

Details on the name of the Amazon ECR repository used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

ecrImageTags -> (list)

The tags attached to the Amazon ECR container image.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

epssScore -> (list)

The EPSS score used to filter findings.

(structure)

An object that describes the details of a number filter.

lowerInclusive -> (double)

The lowest number to be included in the filter.

upperInclusive -> (double)

The highest number to be included in the filter.

exploitAvailable -> (list)

Filters the list of Amazon Web Services Lambda findings by the availability of exploits.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

findingArn -> (list)

Details on the finding ARNs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

findingStatus -> (list)

Details on the finding status types used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

findingType -> (list)

Details on the finding types used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

firstObservedAt -> (list)

Details on the date and time a finding was first seen used to filter findings.

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

fixAvailable -> (list)

Details on whether a fix is available through a version update. This value can be `YES` , `NO` , or `PARTIAL` . A `PARTIAL` fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

inspectorScore -> (list)

The Amazon Inspector score to filter on.

(structure)

An object that describes the details of a number filter.

lowerInclusive -> (double)

The lowest number to be included in the filter.

upperInclusive -> (double)

The highest number to be included in the filter.

lambdaFunctionExecutionRoleArn -> (list)

Filters the list of Amazon Web Services Lambda functions by execution role.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

lambdaFunctionLastModifiedAt -> (list)

Filters the list of Amazon Web Services Lambda functions by the date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html)

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

lambdaFunctionLayers -> (list)

Filters the list of Amazon Web Services Lambda functions by the functionâs [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) . A Lambda function can have up to five layers.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

lambdaFunctionName -> (list)

Filters the list of Amazon Web Services Lambda functions by the name of the function.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

lambdaFunctionRuntime -> (list)

Filters the list of Amazon Web Services Lambda functions by the runtime environment for the Lambda function.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

lastObservedAt -> (list)

Details on the date and time a finding was last seen used to filter findings.

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

networkProtocol -> (list)

Details on network protocol used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

portRange -> (list)

Details on the port ranges used to filter findings.

(structure)

An object that describes the details of a port range filter.

beginInclusive -> (integer)

The port number the port range begins at.

endInclusive -> (integer)

The port number the port range ends at.

relatedVulnerabilities -> (list)

Details on the related vulnerabilities used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

resourceId -> (list)

Details on the resource IDs used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

resourceTags -> (list)

Details on the resource tags used to filter findings.

(structure)

An object that describes details of a map filter.

comparison -> (string)

The operator to use when comparing values in the filter.

key -> (string)

The tag key used in the filter.

value -> (string)

The tag value used in the filter.

resourceType -> (list)

Details on the resource types used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

severity -> (list)

Details on the severity used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

title -> (list)

Details on the finding title used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

updatedAt -> (list)

Details on the date and time a finding was last updated at used to filter findings.

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

vendorSeverity -> (list)

Details on the vendor severity used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

vulnerabilityId -> (list)

Details on the vulnerability ID used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

vulnerabilitySource -> (list)

Details on the vulnerability type used to filter findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

vulnerablePackages -> (list)

Details on the vulnerable packages used to filter findings.

(structure)

Contains information on the details of a package filter.

architecture -> (structure)

An object that contains details on the package architecture type to filter on.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

epoch -> (structure)

An object that contains details on the package epoch to filter on.

lowerInclusive -> (double)

The lowest number to be included in the filter.

upperInclusive -> (double)

The highest number to be included in the filter.

filePath -> (structure)

An object that contains details on the package file path to filter on.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

name -> (structure)

An object that contains details on the name of the package to filter on.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

release -> (structure)

An object that contains details on the package release to filter on.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sourceLambdaLayerArn -> (structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sourceLayerHash -> (structure)

An object that contains details on the source layer hash to filter on.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

version -> (structure)

The package version to filter on.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

description -> (string)

A description of the filter.

name -> (string)

The name of the filter.

ownerId -> (string)

The Amazon Web Services account ID of the account that created the filter.

reason -> (string)

The reason for the filter.

tags -> (map)

The tags attached to the filter.

key -> (string)

value -> (string)

updatedAt -> (timestamp)

The date and time the filter was last updated at.

nextToken -> (string)

A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.