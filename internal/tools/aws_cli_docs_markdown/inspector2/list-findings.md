# list-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# list-findings

## Description

Lists findings for your environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/ListFindings)

`list-findings` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `findings`

## Synopsis

```
list-findings
[--filter-criteria <value>]
[--sort-criteria <value>]
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

`--filter-criteria` (structure)

Details on the filters to apply to your finding results.

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

JSON Syntax:

```
{
  "awsAccountId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "codeVulnerabilityDetectorName": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "codeVulnerabilityDetectorTags": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "codeVulnerabilityFilePath": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "componentId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "componentType": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ec2InstanceImageId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ec2InstanceSubnetId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ec2InstanceVpcId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrImageArchitecture": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrImageHash": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrImageInUseCount": [
    {
      "lowerInclusive": double,
      "upperInclusive": double
    }
    ...
  ],
  "ecrImageLastInUseAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "ecrImagePushedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "ecrImageRegistry": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrImageRepositoryName": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrImageTags": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "epssScore": [
    {
      "lowerInclusive": double,
      "upperInclusive": double
    }
    ...
  ],
  "exploitAvailable": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "findingArn": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "findingStatus": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "findingType": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "firstObservedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "fixAvailable": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "inspectorScore": [
    {
      "lowerInclusive": double,
      "upperInclusive": double
    }
    ...
  ],
  "lambdaFunctionExecutionRoleArn": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionLastModifiedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "lambdaFunctionLayers": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionName": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionRuntime": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lastObservedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "networkProtocol": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "portRange": [
    {
      "beginInclusive": integer,
      "endInclusive": integer
    }
    ...
  ],
  "relatedVulnerabilities": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "resourceId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "resourceTags": [
    {
      "comparison": "EQUALS",
      "key": "string",
      "value": "string"
    }
    ...
  ],
  "resourceType": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "severity": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "title": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "updatedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "vendorSeverity": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "vulnerabilityId": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "vulnerabilitySource": [
    {
      "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "vulnerablePackages": [
    {
      "architecture": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      },
      "epoch": {
        "lowerInclusive": double,
        "upperInclusive": double
      },
      "filePath": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      },
      "name": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      },
      "release": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      },
      "sourceLambdaLayerArn": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      },
      "sourceLayerHash": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      },
      "version": {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
    }
    ...
  ]
}
```

`--sort-criteria` (structure)

Details on the sort criteria to apply to your finding results.

field -> (string)

The finding detail field by which results are sorted.

sortOrder -> (string)

The order by which findings are sorted.

Shorthand Syntax:

```
field=string,sortOrder=string
```

JSON Syntax:

```
{
  "field": "AWS_ACCOUNT_ID"|"FINDING_TYPE"|"SEVERITY"|"FIRST_OBSERVED_AT"|"LAST_OBSERVED_AT"|"FINDING_STATUS"|"RESOURCE_TYPE"|"ECR_IMAGE_PUSHED_AT"|"ECR_IMAGE_REPOSITORY_NAME"|"ECR_IMAGE_REGISTRY"|"NETWORK_PROTOCOL"|"COMPONENT_TYPE"|"VULNERABILITY_ID"|"VULNERABILITY_SOURCE"|"INSPECTOR_SCORE"|"VENDOR_SEVERITY"|"EPSS_SCORE",
  "sortOrder": "ASC"|"DESC"
}
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

## Output

findings -> (list)

Contains details on the findings in your environment.

(structure)

Details about an Amazon Inspector finding.

awsAccountId -> (string)

The Amazon Web Services account ID associated with the finding.

codeVulnerabilityDetails -> (structure)

Details about the code vulnerability identified in a Lambda function used to filter findings.

cwes -> (list)

The Common Weakness Enumeration (CWE) item associated with the detected vulnerability.

(string)

detectorId -> (string)

The ID for the Amazon CodeGuru detector associated with the finding. For more information on detectors see [Amazon CodeGuru Detector Library](https://docs.aws.amazon.com/codeguru/detector-library) .

detectorName -> (string)

The name of the detector used to identify the code vulnerability. For more information on detectors see [CodeGuru Detector Library](https://docs.aws.amazon.com/codeguru/detector-library) .

detectorTags -> (list)

The detector tag associated with the vulnerability. Detector tags group related vulnerabilities by common themes or tactics. For a list of available tags by programming language, see [Java tags](https://docs.aws.amazon.com/codeguru/detector-library/java/tags/) , or [Python tags](https://docs.aws.amazon.com/codeguru/detector-library/python/tags/) .

(string)

filePath -> (structure)

Contains information on where the code vulnerability is located in your code.

endLine -> (integer)

The line number of the last line of code that a vulnerability was found in.

fileName -> (string)

The name of the file the code vulnerability was found in.

filePath -> (string)

The file path to the code that a vulnerability was found in.

startLine -> (integer)

The line number of the first line of code that a vulnerability was found in.

referenceUrls -> (list)

A URL containing supporting documentation about the code vulnerability detected.

(string)

ruleId -> (string)

The identifier for a rule that was used to detect the code vulnerability.

sourceLambdaLayerArn -> (string)

The Amazon Resource Name (ARN) of the Lambda layer that the code vulnerability was detected in.

description -> (string)

The description of the finding.

epss -> (structure)

The findingâs EPSS score.

score -> (double)

The EPSS score.

exploitAvailable -> (string)

If a finding discovered in your environment has an exploit available.

exploitabilityDetails -> (structure)

The details of an exploit available for a finding discovered in your environment.

lastKnownExploitAt -> (timestamp)

The date and time of the last exploit associated with a finding discovered in your environment.

findingArn -> (string)

The Amazon Resource Number (ARN) of the finding.

firstObservedAt -> (timestamp)

The date and time that the finding was first observed.

fixAvailable -> (string)

Details on whether a fix is available through a version update. This value can be `YES` , `NO` , or `PARTIAL` . A `PARTIAL` fix means that some, but not all, of the packages identified in the finding have fixes available through updated versions.

inspectorScore -> (double)

The Amazon Inspector score given to the finding.

inspectorScoreDetails -> (structure)

An object that contains details of the Amazon Inspector score.

adjustedCvss -> (structure)

An object that contains details about the CVSS score given to a finding.

adjustments -> (list)

An object that contains details about adjustment Amazon Inspector made to the CVSS score.

(structure)

Details on adjustments Amazon Inspector made to the CVSS score for a finding.

metric -> (string)

The metric used to adjust the CVSS score.

reason -> (string)

The reason the CVSS score has been adjustment.

cvssSource -> (string)

The source of the CVSS data.

score -> (double)

The CVSS score.

scoreSource -> (string)

The source for the CVSS score.

scoringVector -> (string)

The vector for the CVSS score.

version -> (string)

The CVSS version used in scoring.

lastObservedAt -> (timestamp)

The date and time the finding was last observed. This timestamp for this field remains unchanged until a finding is updated.

networkReachabilityDetails -> (structure)

An object that contains the details of a network reachability finding.

networkPath -> (structure)

An object that contains details about a network path associated with a finding.

steps -> (list)

The details on the steps in the network path.

(structure)

Details about the step associated with a finding.

componentArn -> (string)

The component ARN. The ARN can be null and is not displayed in the Amazon Web Services console.

componentId -> (string)

The component ID.

componentType -> (string)

The component type.

openPortRange -> (structure)

An object that contains details about the open port range associated with a finding.

begin -> (integer)

The beginning port in a port range.

end -> (integer)

The ending port in a port range.

protocol -> (string)

The protocol associated with a finding.

packageVulnerabilityDetails -> (structure)

An object that contains the details of a package vulnerability finding.

cvss -> (list)

An object that contains details about the CVSS score of a finding.

(structure)

The CVSS score for a finding.

baseScore -> (double)

The base CVSS score used for the finding.

scoringVector -> (string)

The vector string of the CVSS score.

source -> (string)

The source of the CVSS score.

version -> (string)

The version of CVSS used for the score.

referenceUrls -> (list)

One or more URLs that contain details about this vulnerability type.

(string)

relatedVulnerabilities -> (list)

One or more vulnerabilities related to the one identified in this finding.

(string)

source -> (string)

The source of the vulnerability information.

sourceUrl -> (string)

A URL to the source of the vulnerability information.

vendorCreatedAt -> (timestamp)

The date and time that this vulnerability was first added to the vendorâs database.

vendorSeverity -> (string)

The severity the vendor has given to this vulnerability type.

vendorUpdatedAt -> (timestamp)

The date and time the vendor last updated this vulnerability in their database.

vulnerabilityId -> (string)

The ID given to this vulnerability.

vulnerablePackages -> (list)

The packages impacted by this vulnerability.

(structure)

Information on the vulnerable package identified by a finding.

arch -> (string)

The architecture of the vulnerable package.

epoch -> (integer)

The epoch of the vulnerable package.

filePath -> (string)

The file path of the vulnerable package.

fixedInVersion -> (string)

The version of the package that contains the vulnerability fix.

name -> (string)

The name of the vulnerable package.

packageManager -> (string)

The package manager of the vulnerable package.

release -> (string)

The release of the vulnerable package.

remediation -> (string)

The code to run in your environment to update packages with a fix available.

sourceLambdaLayerArn -> (string)

The Amazon Resource Number (ARN) of the Amazon Web Services Lambda function affected by a finding.

sourceLayerHash -> (string)

The source layer hash of the vulnerable package.

version -> (string)

The version of the vulnerable package.

remediation -> (structure)

An object that contains the details about how to remediate a finding.

recommendation -> (structure)

An object that contains information about the recommended course of action to remediate the finding.

Url -> (string)

The URL address to the CVE remediation recommendations.

text -> (string)

The recommended course of action to remediate the finding.

resources -> (list)

Contains information on the resources involved in a finding. The `resource` value determines the valid values for `type` in your request. For more information, see [Finding types](https://docs.aws.amazon.com/inspector/latest/user/findings-types.html) in the Amazon Inspector user guide.

(structure)

Details about the resource involved in a finding.

details -> (structure)

An object that contains details about the resource involved in a finding.

awsEc2Instance -> (structure)

An object that contains details about the Amazon EC2 instance involved in the finding.

iamInstanceProfileArn -> (string)

The IAM instance profile ARN of the Amazon EC2 instance.

imageId -> (string)

The image ID of the Amazon EC2 instance.

ipV4Addresses -> (list)

The IPv4 addresses of the Amazon EC2 instance.

(string)

ipV6Addresses -> (list)

The IPv6 addresses of the Amazon EC2 instance.

(string)

keyName -> (string)

The name of the key pair used to launch the Amazon EC2 instance.

launchedAt -> (timestamp)

The date and time the Amazon EC2 instance was launched at.

platform -> (string)

The platform of the Amazon EC2 instance.

subnetId -> (string)

The subnet ID of the Amazon EC2 instance.

type -> (string)

The type of the Amazon EC2 instance.

vpcId -> (string)

The VPC ID of the Amazon EC2 instance.

awsEcrContainerImage -> (structure)

An object that contains details about the Amazon ECR container image involved in the finding.

architecture -> (string)

The architecture of the Amazon ECR container image.

author -> (string)

The image author of the Amazon ECR container image.

imageHash -> (string)

The image hash of the Amazon ECR container image.

imageTags -> (list)

The image tags attached to the Amazon ECR container image.

(string)

inUseCount -> (long)

The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.

lastInUseAt -> (timestamp)

The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.

platform -> (string)

The platform of the Amazon ECR container image.

pushedAt -> (timestamp)

The date and time the Amazon ECR container image was pushed.

registry -> (string)

The registry for the Amazon ECR container image.

repositoryName -> (string)

The name of the repository the Amazon ECR container image resides in.

awsLambdaFunction -> (structure)

A summary of the information about an Amazon Web Services Lambda function affected by a finding.

architectures -> (list)

The instruction set architecture that the Amazon Web Services Lambda function supports. Architecture is a string array with one of the valid values. The default architecture value is `x86_64` .

(string)

codeSha256 -> (string)

The SHA256 hash of the Amazon Web Services Lambda functionâs deployment package.

executionRoleArn -> (string)

The Amazon Web Services Lambda functionâs execution role.

functionName -> (string)

The name of the Amazon Web Services Lambda function.

lastModifiedAt -> (timestamp)

The date and time that a user last updated the configuration, in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html)

layers -> (list)

The Amazon Web Services Lambda functionâs [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) . A Lambda function can have up to five layers.

(string)

packageType -> (string)

The type of deployment package. Set to `Image` for container image and set `Zip` for .zip file archive.

runtime -> (string)

The runtime environment for the Amazon Web Services Lambda function.

version -> (string)

The version of the Amazon Web Services Lambda function.

vpcConfig -> (structure)

The Amazon Web Services Lambda functionâs networking configuration.

securityGroupIds -> (list)

The VPC security groups and subnets that are attached to an Amazon Web Services Lambda function. For more information, see [VPC Settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) .

(string)

subnetIds -> (list)

A list of VPC subnet IDs.

(string)

vpcId -> (string)

The ID of the VPC.

id -> (string)

The ID of the resource.

partition -> (string)

The partition of the resource.

region -> (string)

The Amazon Web Services Region the impacted resource is located in.

tags -> (map)

The tags attached to the resource.

key -> (string)

value -> (string)

type -> (string)

The type of resource.

severity -> (string)

The severity of the finding. `UNTRIAGED` applies to `PACKAGE_VULNERABILITY` type findings that the vendor has not assigned a severity yet. For more information, see [Severity levels for findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html) in the Amazon Inspector user guide.

status -> (string)

The status of the finding.

title -> (string)

The title of the finding.

type -> (string)

The type of the finding. The `type` value determines the valid values for `resource` in your request. For more information, see [Finding types](https://docs.aws.amazon.com/inspector/latest/user/findings-types.html) in the Amazon Inspector user guide.

updatedAt -> (timestamp)

The date and time the finding was last updated at.

nextToken -> (string)

A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.