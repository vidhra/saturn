# list-coverageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/index.html#cli-aws-inspector2) ]

# list-coverage

## Description

Lists coverage details for your environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector2-2020-06-08/ListCoverage)

`list-coverage` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `coveredResources`

## Synopsis

```
list-coverage
[--filter-criteria <value>]
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

An object that contains details on the filters to apply to the coverage data for your environment.

accountId -> (list)

An array of Amazon Web Services account IDs to return coverage statistics for.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

ec2InstanceTags -> (list)

The Amazon EC2 instance tags to filter on.

(structure)

Contains details of a coverage map filter.

comparison -> (string)

The operator to compare coverage on.

key -> (string)

The tag key associated with the coverage map filter.

value -> (string)

The tag value associated with the coverage map filter.

ecrImageInUseCount -> (list)

The number of Amazon ECR images in use.

(structure)

The coverage number to be used in the filter.

lowerInclusive -> (long)

The lower inclusive for the coverage number.

upperInclusive -> (long)

The upper inclusive for the coverage number.>

ecrImageLastInUseAt -> (list)

The Amazon ECR image that was last in use.

(structure)

Contains details of a coverage date filter.

endInclusive -> (timestamp)

A timestamp representing the end of the time period to filter results by.

startInclusive -> (timestamp)

A timestamp representing the start of the time period to filter results by.

ecrImageTags -> (list)

The Amazon ECR image tags to filter on.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

ecrRepositoryName -> (list)

The Amazon ECR repository name to filter on.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

imagePulledAt -> (list)

The date an image was last pulled at.

(structure)

Contains details of a coverage date filter.

endInclusive -> (timestamp)

A timestamp representing the end of the time period to filter results by.

startInclusive -> (timestamp)

A timestamp representing the start of the time period to filter results by.

lambdaFunctionName -> (list)

Returns coverage statistics for Amazon Web Services Lambda functions filtered by function names.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

lambdaFunctionRuntime -> (list)

Returns coverage statistics for Amazon Web Services Lambda functions filtered by runtime.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

lambdaFunctionTags -> (list)

Returns coverage statistics for Amazon Web Services Lambda functions filtered by tag.

(structure)

Contains details of a coverage map filter.

comparison -> (string)

The operator to compare coverage on.

key -> (string)

The tag key associated with the coverage map filter.

value -> (string)

The tag value associated with the coverage map filter.

lastScannedAt -> (list)

Filters Amazon Web Services resources based on whether Amazon Inspector has checked them for vulnerabilities within the specified time range.

(structure)

Contains details of a coverage date filter.

endInclusive -> (timestamp)

A timestamp representing the end of the time period to filter results by.

startInclusive -> (timestamp)

A timestamp representing the start of the time period to filter results by.

resourceId -> (list)

An array of Amazon Web Services resource IDs to return coverage statistics for.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

resourceType -> (list)

An array of Amazon Web Services resource types to return coverage statistics for. The values can be `AWS_EC2_INSTANCE` , `AWS_LAMBDA_FUNCTION` , `AWS_ECR_CONTAINER_IMAGE` , `AWS_ECR_REPOSITORY` or `AWS_ACCOUNT` .

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanMode -> (list)

The filter to search for Amazon EC2 instance coverage by scan mode. Valid values are `EC2_SSM_AGENT_BASED` and `EC2_AGENTLESS` .

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanStatusCode -> (list)

The scan status code to filter on. Valid values are: `ValidationException` , `InternalServerException` , `ResourceNotFoundException` , `BadRequestException` , and `ThrottlingException` .

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanStatusReason -> (list)

The scan status reason to filter on.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

scanType -> (list)

An array of Amazon Inspector scan types to return coverage statistics for.

(structure)

Contains details of a coverage string filter.

comparison -> (string)

The operator to compare strings on.

value -> (string)

The value to compare strings on.

Shorthand Syntax:

```
accountId=[{comparison=string,value=string},{comparison=string,value=string}],ec2InstanceTags=[{comparison=string,key=string,value=string},{comparison=string,key=string,value=string}],ecrImageInUseCount=[{lowerInclusive=long,upperInclusive=long},{lowerInclusive=long,upperInclusive=long}],ecrImageLastInUseAt=[{endInclusive=timestamp,startInclusive=timestamp},{endInclusive=timestamp,startInclusive=timestamp}],ecrImageTags=[{comparison=string,value=string},{comparison=string,value=string}],ecrRepositoryName=[{comparison=string,value=string},{comparison=string,value=string}],imagePulledAt=[{endInclusive=timestamp,startInclusive=timestamp},{endInclusive=timestamp,startInclusive=timestamp}],lambdaFunctionName=[{comparison=string,value=string},{comparison=string,value=string}],lambdaFunctionRuntime=[{comparison=string,value=string},{comparison=string,value=string}],lambdaFunctionTags=[{comparison=string,key=string,value=string},{comparison=string,key=string,value=string}],lastScannedAt=[{endInclusive=timestamp,startInclusive=timestamp},{endInclusive=timestamp,startInclusive=timestamp}],resourceId=[{comparison=string,value=string},{comparison=string,value=string}],resourceType=[{comparison=string,value=string},{comparison=string,value=string}],scanMode=[{comparison=string,value=string},{comparison=string,value=string}],scanStatusCode=[{comparison=string,value=string},{comparison=string,value=string}],scanStatusReason=[{comparison=string,value=string},{comparison=string,value=string}],scanType=[{comparison=string,value=string},{comparison=string,value=string}]
```

JSON Syntax:

```
{
  "accountId": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ec2InstanceTags": [
    {
      "comparison": "EQUALS",
      "key": "string",
      "value": "string"
    }
    ...
  ],
  "ecrImageInUseCount": [
    {
      "lowerInclusive": long,
      "upperInclusive": long
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
  "ecrImageTags": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "ecrRepositoryName": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "imagePulledAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "lambdaFunctionName": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionRuntime": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "lambdaFunctionTags": [
    {
      "comparison": "EQUALS",
      "key": "string",
      "value": "string"
    }
    ...
  ],
  "lastScannedAt": [
    {
      "endInclusive": timestamp,
      "startInclusive": timestamp
    }
    ...
  ],
  "resourceId": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "resourceType": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanMode": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanStatusCode": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanStatusReason": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ],
  "scanType": [
    {
      "comparison": "EQUALS"|"NOT_EQUALS",
      "value": "string"
    }
    ...
  ]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To list coverage details about your environment**

The following `list-coverage` example lists your environmentâs coverage details.

```
aws inspector2 list-coverage
```

Output:

```
{
    "coveredResources": [
        {
            "accountId": "123456789012",
            "lastScannedAt": "2024-05-20T16:23:20-07:00",
            "resourceId": "i-EXAMPLE55555555555",
            "resourceMetadata": {
                "ec2": {
                    "amiId": "ami-EXAMPLE6666666666",
                    "platform": "LINUX"
                }
            },
            "resourceType": "AWS_EC2_INSTANCE",
            "scanStatus": {
                "reason": "SUCCESSFUL",
                "statusCode": "ACTIVE"
            },
            "scanType": "PACKAGE"
        }
    ]
}
```

**Example 2: To list coverage details about the Lambda function resource type**

The following `list-coverage` example lists your Lamda function resource type details.

```
aws inspector2 list-coverage
    --filter-criteria '{"resourceType":[{"comparison":"EQUALS","value":"AWS_LAMBDA_FUNCTION"}]}'
```

Output:

```
{
    "coveredResources": [
        {
            "accountId": "123456789012",
            "resourceId": "arn:aws:lambda:us-west-2:123456789012:function:Eval-container-scan-results:$LATEST",
            "resourceMetadata": {
                "lambdaFunction": {
                    "functionName": "Eval-container-scan-results",
                    "functionTags": {},
                    "layers": [],
                    "runtime": "PYTHON_3_7"
                }
            },
            "resourceType": "AWS_LAMBDA_FUNCTION",
            "scanStatus": {
                "reason": "SUCCESSFUL",
                "statusCode": "ACTIVE"
            },
            "scanType": "CODE"
        }
    ]
}
```

## Output

coveredResources -> (list)

An object that contains details on the covered resources in your environment.

(structure)

An object that contains details about a resource covered by Amazon Inspector.

accountId -> (string)

The Amazon Web Services account ID of the covered resource.

lastScannedAt -> (timestamp)

The date and time the resource was last checked for vulnerabilities.

resourceId -> (string)

The ID of the covered resource.

resourceMetadata -> (structure)

An object that contains details about the metadata.

ec2 -> (structure)

An object that contains metadata details for an Amazon EC2 instance.

amiId -> (string)

The ID of the Amazon Machine Image (AMI) used to launch the instance.

platform -> (string)

The platform of the instance.

tags -> (map)

The tags attached to the instance.

key -> (string)

value -> (string)

ecrImage -> (structure)

An object that contains details about the container metadata for an Amazon ECR image.

imagePulledAt -> (timestamp)

The date an image was last pulled at.

inUseCount -> (long)

The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.

lastInUseAt -> (timestamp)

The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.

tags -> (list)

Tags associated with the Amazon ECR image metadata.

(string)

ecrRepository -> (structure)

An object that contains details about the repository an Amazon ECR image resides in.

name -> (string)

The name of the Amazon ECR repository.

scanFrequency -> (string)

The frequency of scans.

lambdaFunction -> (structure)

An object that contains metadata details for an Amazon Web Services Lambda function.

functionName -> (string)

The name of a function.

functionTags -> (map)

The resource tags on an Amazon Web Services Lambda function.

key -> (string)

value -> (string)

layers -> (list)

The layers for an Amazon Web Services Lambda function. A Lambda function can have up to five layers.

(string)

runtime -> (string)

An Amazon Web Services Lambda functionâs runtime.

resourceType -> (string)

The type of the covered resource.

scanMode -> (string)

The scan method that is applied to the instance.

scanStatus -> (structure)

The status of the scan covering the resource.

reason -> (string)

The scan status. Possible return values and descriptions are:

`PENDING_INITIAL_SCAN` - This resource has been identified for scanning, results will be available soon.

`ACCESS_DENIED` - Resource access policy restricting Amazon Inspector access. Please update the IAM policy.

`INTERNAL_ERROR` - Amazon Inspector has encountered an internal error for this resource. Amazon Inspector service will automatically resolve the issue and resume the scanning. No action required from the user.

`UNMANAGED_EC2_INSTANCE` - The EC2 instance is not managed by SSM, please use the following SSM automation to remediate the issue: [https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshoot-managed-instance.html) . Once the instance becomes managed by SSM, Inspector will automatically begin scanning this instance.

`UNSUPPORTED_OS` - Amazon Inspector does not support this OS, architecture, or image manifest type at this time. To see a complete list of supported operating systems see: [`https\://docs.aws.amazon.com/inspector/latest/user/supported.html < https://docs.aws.amazon.com/inspector/latest/user/supported.html>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage.html#id1) .

`SCAN_ELIGIBILITY_EXPIRED` - The configured scan duration has lapsed for this image.

`RESOURCE_TERMINATED` - This resource has been terminated. The findings and coverage associated with this resource are in the process of being cleaned up.

`SUCCESSFUL` - The scan was successful.

`NO_RESOURCES_FOUND` - Reserved for future use.

`IMAGE_SIZE_EXCEEDED` - Reserved for future use.

`SCAN_FREQUENCY_MANUAL` - This image will not be covered by Amazon Inspector due to the repository scan frequency configuration.

`SCAN_FREQUENCY_SCAN_ON_PUSH` - This image will be scanned one time and will not new findings because of the scan frequency configuration.

`EC2_INSTANCE_STOPPED` - This EC2 instance is in a stopped state, therefore, Amazon Inspector will pause scanning. The existing findings will continue to exist until the instance is terminated. Once the instance is re-started, Inspector will automatically start scanning the instance again. Please note that you will not be charged for this instance while itâs in a stopped state.

`PENDING_DISABLE` - This resource is pending cleanup during disablement. The customer will not be billed while a resource is in the pending disable status.

`NO INVENTORY` - Amazon Inspector couldnât find software application inventory to scan for vulnerabilities. This might be caused due to required Amazon Inspector associations being deleted or failing to run on your resource. Please verify the status of `InspectorInventoryCollection-do-not-delete` association in the SSM console for the resource. Additionally, you can verify the instanceâs inventory in the SSM Fleet Manager console.

`STALE_INVENTORY` - Amazon Inspector wasnât able to collect an updated software application inventory in the last 7 days. Please confirm the required Amazon Inspector associations still exist and you can still see an updated inventory in the SSM console.

`EXCLUDED_BY_TAG` - This resource was not scanned because it has been excluded by a tag.

`UNSUPPORTED_RUNTIME` - The function was not scanned because it has an unsupported runtime. To see a complete list of supported runtimes see: [`https\://docs.aws.amazon.com/inspector/latest/user/supported.html < https://docs.aws.amazon.com/inspector/latest/user/supported.html>`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage.html#id1) .

`UNSUPPORTED_MEDIA_TYPE` - The ECR image has an unsupported media type.

`UNSUPPORTED_CONFIG_FILE` - Reserved for future use.

`DEEP_INSPECTION_PACKAGE_COLLECTION_LIMIT_EXCEEDED` - The instance has exceeded the 5000 package limit for Amazon Inspector Deep inspection. To resume Deep inspection for this instance you can try to adjust the custom paths associated with the account.

`DEEP_INSPECTION_DAILY_SSM_INVENTORY_LIMIT_EXCEEDED` - The SSM agent couldnât send inventory to Amazon Inspector because the SSM quota for Inventory data collected per instance per day has already been reached for this instance.

`DEEP_INSPECTION_COLLECTION_TIME_LIMIT_EXCEEDED` - Amazon Inspector failed to extract the package inventory because the package collection time exceeding the maximum threshold of 15 minutes.

`DEEP_INSPECTION_NO_INVENTORY` The Amazon Inspector plugin hasnât yet been able to collect an inventory of packages for this instance. This is usually the result of a pending scan, however, if this status persists after 6 hours, use SSM to ensure that the required Amazon Inspector associations exist and are running for the instance.

statusCode -> (string)

The status code of the scan.

scanType -> (string)

The Amazon Inspector scan type covering the resource.

nextToken -> (string)

A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the `NextToken` value returned from the previous request to continue listing results after the first page.