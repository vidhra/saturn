# list-finding-aggregationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-finding-aggregations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-finding-aggregations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# list-finding-aggregations

## Description

Lists aggregated finding data for your environment based on specific criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/ListFindingAggregations)

`list-finding-aggregations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `responses`

## Synopsis

```
list-finding-aggregations
[--account-ids <value>]
[--aggregation-request <value>]
--aggregation-type <value>
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

`--account-ids` (list)

The Amazon Web Services account IDs to retrieve finding aggregation data for.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

Shorthand Syntax:

```
comparison=string,value=string ...
```

JSON Syntax:

```
[
  {
    "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
    "value": "string"
  }
  ...
]
```

`--aggregation-request` (tagged union structure)

Details of the aggregation request that is used to filter your aggregation results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `accountAggregation`, `amiAggregation`, `awsEcrContainerAggregation`, `ec2InstanceAggregation`, `findingTypeAggregation`, `imageLayerAggregation`, `lambdaFunctionAggregation`, `lambdaLayerAggregation`, `packageAggregation`, `repositoryAggregation`, `titleAggregation`.

accountAggregation -> (structure)

An object that contains details about an aggregation request based on Amazon Web Services account IDs.

findingType -> (string)

The type of finding.

resourceType -> (string)

The type of resource.

sortBy -> (string)

The value to sort by.

sortOrder -> (string)

The sort order (ascending or descending).

amiAggregation -> (structure)

An object that contains details about an aggregation request based on Amazon Machine Images (AMIs).

amis -> (list)

The IDs of AMIs to aggregate findings for.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

awsEcrContainerAggregation -> (structure)

An object that contains details about an aggregation request based on Amazon ECR container images.

architectures -> (list)

The architecture of the containers.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

imageShas -> (list)

The image SHA values.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

imageTags -> (list)

The image tags.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

inUseCount -> (list)

The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.

(structure)

An object that describes the details of a number filter.

lowerInclusive -> (double)

The lowest number to be included in the filter.

upperInclusive -> (double)

The highest number to be included in the filter.

lastInUseAt -> (list)

The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.

(structure)

Contains details on the time range used to filter findings.

endInclusive -> (timestamp)

A timestamp representing the end of the time period filtered on.

startInclusive -> (timestamp)

A timestamp representing the start of the time period filtered on.

repositories -> (list)

The container repositories.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

resourceIds -> (list)

The container resource IDs.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The value to sort by.

sortOrder -> (string)

The sort order (ascending or descending).

ec2InstanceAggregation -> (structure)

An object that contains details about an aggregation request based on Amazon EC2 instances.

amis -> (list)

The AMI IDs associated with the Amazon EC2 instances to aggregate findings for.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

instanceIds -> (list)

The Amazon EC2 instance IDs to aggregate findings for.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

instanceTags -> (list)

The Amazon EC2 instance tags to aggregate findings for.

(structure)

An object that describes details of a map filter.

comparison -> (string)

The operator to use when comparing values in the filter.

key -> (string)

The tag key used in the filter.

value -> (string)

The tag value used in the filter.

operatingSystems -> (list)

The operating system types to aggregate findings for. Valid values must be uppercase and underscore separated, examples are `ORACLE_LINUX_7` and `ALPINE_LINUX_3_8` .

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

findingTypeAggregation -> (structure)

An object that contains details about an aggregation request based on finding types.

findingType -> (string)

The finding type to aggregate.

resourceType -> (string)

The resource type to aggregate.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

imageLayerAggregation -> (structure)

An object that contains details about an aggregation request based on container image layers.

layerHashes -> (list)

The hashes associated with the layers.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

repositories -> (list)

The repository associated with the container image hosting the layers.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

resourceIds -> (list)

The ID of the container image layer.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

lambdaFunctionAggregation -> (structure)

Returns an object with findings aggregated by Amazon Web Services Lambda function.

functionNames -> (list)

The Amazon Web Services Lambda function names to include in the aggregation results.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

functionTags -> (list)

The tags to include in the aggregation results.

(structure)

An object that describes details of a map filter.

comparison -> (string)

The operator to use when comparing values in the filter.

key -> (string)

The tag key used in the filter.

value -> (string)

The tag value used in the filter.

resourceIds -> (list)

The resource IDs to include in the aggregation results.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

runtimes -> (list)

Returns findings aggregated by Amazon Web Services Lambda function runtime environments.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The finding severity to use for sorting the results.

sortOrder -> (string)

The order to use for sorting the results.

lambdaLayerAggregation -> (structure)

Returns an object with findings aggregated by Amazon Web Services Lambda layer.

functionNames -> (list)

The names of the Amazon Web Services Lambda functions associated with the layers.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

layerArns -> (list)

The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function layer.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

resourceIds -> (list)

The resource IDs for the Amazon Web Services Lambda function layers.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The finding severity to use for sorting the results.

sortOrder -> (string)

The order to use for sorting the results.

packageAggregation -> (structure)

An object that contains details about an aggregation request based on operating system package type.

packageNames -> (list)

The names of packages to aggregate findings on.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

repositoryAggregation -> (structure)

An object that contains details about an aggregation request based on Amazon ECR repositories.

repositories -> (list)

The names of repositories to aggregate findings on.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

titleAggregation -> (structure)

An object that contains details about an aggregation request based on finding title.

findingType -> (string)

The type of finding to aggregate on.

resourceType -> (string)

The resource type to aggregate on.

sortBy -> (string)

The value to sort results by.

sortOrder -> (string)

The order to sort results by.

titles -> (list)

The finding titles to aggregate on.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

vulnerabilityIds -> (list)

The vulnerability IDs of the findings.

(structure)

An object that describes the details of a string filter.

comparison -> (string)

The operator to use when comparing values in the filter.

value -> (string)

The value to filter on.

JSON Syntax:

```
{
  "accountAggregation": {
    "findingType": "NETWORK_REACHABILITY"|"PACKAGE_VULNERABILITY"|"CODE_VULNERABILITY",
    "resourceType": "AWS_EC2_INSTANCE"|"AWS_ECR_CONTAINER_IMAGE"|"AWS_LAMBDA_FUNCTION",
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "amiAggregation": {
    "amis": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL"|"AFFECTED_INSTANCES",
    "sortOrder": "ASC"|"DESC"
  },
  "awsEcrContainerAggregation": {
    "architectures": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "imageShas": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "imageTags": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "inUseCount": [
      {
        "lowerInclusive": double,
        "upperInclusive": double
      }
      ...
    ],
    "lastInUseAt": [
      {
        "endInclusive": timestamp,
        "startInclusive": timestamp
      }
      ...
    ],
    "repositories": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "resourceIds": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "ec2InstanceAggregation": {
    "amis": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "instanceIds": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "instanceTags": [
      {
        "comparison": "EQUALS",
        "key": "string",
        "value": "string"
      }
      ...
    ],
    "operatingSystems": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "NETWORK_FINDINGS"|"CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "findingTypeAggregation": {
    "findingType": "NETWORK_REACHABILITY"|"PACKAGE_VULNERABILITY"|"CODE_VULNERABILITY",
    "resourceType": "AWS_EC2_INSTANCE"|"AWS_ECR_CONTAINER_IMAGE"|"AWS_LAMBDA_FUNCTION",
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "imageLayerAggregation": {
    "layerHashes": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "repositories": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "resourceIds": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "lambdaFunctionAggregation": {
    "functionNames": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "functionTags": [
      {
        "comparison": "EQUALS",
        "key": "string",
        "value": "string"
      }
      ...
    ],
    "resourceIds": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "runtimes": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "lambdaLayerAggregation": {
    "functionNames": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "layerArns": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "resourceIds": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "packageAggregation": {
    "packageNames": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC"
  },
  "repositoryAggregation": {
    "repositories": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "sortBy": "CRITICAL"|"HIGH"|"ALL"|"AFFECTED_IMAGES",
    "sortOrder": "ASC"|"DESC"
  },
  "titleAggregation": {
    "findingType": "NETWORK_REACHABILITY"|"PACKAGE_VULNERABILITY"|"CODE_VULNERABILITY",
    "resourceType": "AWS_EC2_INSTANCE"|"AWS_ECR_CONTAINER_IMAGE"|"AWS_LAMBDA_FUNCTION",
    "sortBy": "CRITICAL"|"HIGH"|"ALL",
    "sortOrder": "ASC"|"DESC",
    "titles": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ],
    "vulnerabilityIds": [
      {
        "comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS",
        "value": "string"
      }
      ...
    ]
  }
}
```

`--aggregation-type` (string)

The type of the aggregation request.

Possible values:

- `FINDING_TYPE`
- `PACKAGE`
- `TITLE`
- `REPOSITORY`
- `AMI`
- `AWS_EC2_INSTANCE`
- `AWS_ECR_CONTAINER`
- `IMAGE_LAYER`
- `ACCOUNT`
- `AWS_LAMBDA_FUNCTION`
- `LAMBDA_LAYER`

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

aggregationType -> (string)

The type of aggregation to perform.

nextToken -> (string)

A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.

responses -> (list)

Objects that contain the results of an aggregation operation.

(tagged union structure)

A structure that contains details about the results of an aggregation type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `accountAggregation`, `amiAggregation`, `awsEcrContainerAggregation`, `ec2InstanceAggregation`, `findingTypeAggregation`, `imageLayerAggregation`, `lambdaFunctionAggregation`, `lambdaLayerAggregation`, `packageAggregation`, `repositoryAggregation`, `titleAggregation`.

accountAggregation -> (structure)

An object that contains details about an aggregation response based on Amazon Web Services account IDs.

accountId -> (string)

The Amazon Web Services account ID.

exploitAvailableCount -> (long)

The number of findings that have an exploit available.

fixAvailableCount -> (long)

Details about the number of fixes.

severityCounts -> (structure)

The number of findings by severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

amiAggregation -> (structure)

An object that contains details about an aggregation response based on Amazon Machine Images (AMIs).

accountId -> (string)

The Amazon Web Services account ID for the AMI.

affectedInstances -> (long)

The IDs of Amazon EC2 instances using this AMI.

ami -> (string)

The ID of the AMI that findings were aggregated for.

severityCounts -> (structure)

An object that contains the count of matched findings per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

awsEcrContainerAggregation -> (structure)

An object that contains details about an aggregation response based on Amazon ECR container images.

accountId -> (string)

The Amazon Web Services account ID of the account that owns the container.

architecture -> (string)

The architecture of the container.

imageSha -> (string)

The SHA value of the container image.

imageTags -> (list)

The container image stags.

(string)

inUseCount -> (long)

The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.

lastInUseAt -> (timestamp)

The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.

repository -> (string)

The container repository.

resourceId -> (string)

The resource ID of the container.

severityCounts -> (structure)

The number of finding by severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

ec2InstanceAggregation -> (structure)

An object that contains details about an aggregation response based on Amazon EC2 instances.

accountId -> (string)

The Amazon Web Services account for the Amazon EC2 instance.

ami -> (string)

The Amazon Machine Image (AMI) of the Amazon EC2 instance.

instanceId -> (string)

The Amazon EC2 instance ID.

instanceTags -> (map)

The tags attached to the instance.

key -> (string)

value -> (string)

networkFindings -> (long)

The number of network findings for the Amazon EC2 instance.

operatingSystem -> (string)

The operating system of the Amazon EC2 instance.

severityCounts -> (structure)

An object that contains the count of matched findings per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

findingTypeAggregation -> (structure)

An object that contains details about an aggregation response based on finding types.

accountId -> (string)

The ID of the Amazon Web Services account associated with the findings.

exploitAvailableCount -> (long)

The number of findings that have an exploit available.

fixAvailableCount -> (long)

Details about the number of fixes.

severityCounts -> (structure)

The value to sort results by.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

imageLayerAggregation -> (structure)

An object that contains details about an aggregation response based on container image layers.

accountId -> (string)

The ID of the Amazon Web Services account that owns the container image hosting the layer image.

layerHash -> (string)

The layer hash.

repository -> (string)

The repository the layer resides in.

resourceId -> (string)

The resource ID of the container image layer.

severityCounts -> (structure)

An object that represents the count of matched findings per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

lambdaFunctionAggregation -> (structure)

An aggregation of findings by Amazon Web Services Lambda function.

accountId -> (string)

The ID of the Amazon Web Services account that owns the Amazon Web Services Lambda function.

functionName -> (string)

The Amazon Web Services Lambda function names included in the aggregation results.

lambdaTags -> (map)

The tags included in the aggregation results.

key -> (string)

value -> (string)

lastModifiedAt -> (timestamp)

The date that the Amazon Web Services Lambda function included in the aggregation results was last changed.

resourceId -> (string)

The resource IDs included in the aggregation results.

runtime -> (string)

The runtimes included in the aggregation results.

severityCounts -> (structure)

An object that contains the counts of aggregated finding per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

lambdaLayerAggregation -> (structure)

An aggregation of findings by Amazon Web Services Lambda layer.

accountId -> (string)

The account ID of the Amazon Web Services Lambda function layer.

functionName -> (string)

The names of the Amazon Web Services Lambda functions associated with the layers.

layerArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function layer.

resourceId -> (string)

The Resource ID of the Amazon Web Services Lambda function layer.

severityCounts -> (structure)

An object that contains the counts of aggregated finding per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

packageAggregation -> (structure)

An object that contains details about an aggregation response based on operating system package type.

accountId -> (string)

The ID of the Amazon Web Services account associated with the findings.

packageName -> (string)

The name of the operating system package.

severityCounts -> (structure)

An object that contains the count of matched findings per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

repositoryAggregation -> (structure)

An object that contains details about an aggregation response based on Amazon ECR repositories.

accountId -> (string)

The ID of the Amazon Web Services account associated with the findings.

affectedImages -> (long)

The number of container images impacted by the findings.

repository -> (string)

The name of the repository associated with the findings.

severityCounts -> (structure)

An object that represent the count of matched findings per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

titleAggregation -> (structure)

An object that contains details about an aggregation response based on finding title.

accountId -> (string)

The ID of the Amazon Web Services account associated with the findings.

severityCounts -> (structure)

An object that represent the count of matched findings per severity.

all -> (long)

The total count of findings from all severities.

critical -> (long)

The total count of critical severity findings.

high -> (long)

The total count of high severity findings.

medium -> (long)

The total count of medium severity findings.

title -> (string)

The title that the findings were aggregated on.

vulnerabilityId -> (string)

The vulnerability ID of the finding.