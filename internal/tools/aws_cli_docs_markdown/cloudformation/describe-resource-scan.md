# describe-resource-scanÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-resource-scan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-resource-scan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-resource-scan

## Description

Describes details of a resource scan.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeResourceScan)

## Synopsis

```
describe-resource-scan
--resource-scan-id <value>
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

`--resource-scan-id` (string)

The Amazon Resource Name (ARN) of the resource scan.

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

ResourceScanId -> (string)

The Amazon Resource Name (ARN) of the resource scan. The format is `arn:${Partition}:cloudformation:${Region}:${Account}:resourceScan/${Id}` . An example is [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-resource-scan.html#id1)arn:aws:cloudformation:*us-east-1* :*123456789012* :resourceScan/*f5b490f7-7ed4-428a-aa06-31ff25db0772* `` .

Status -> (string)

Status of the resource scan.

IN_PROGRESS

The resource scan is still in progress.

COMPLETE

The resource scan is complete.

EXPIRED

The resource scan has expired.

FAILED

The resource scan has failed.

StatusReason -> (string)

The reason for the resource scan status, providing more information if a failure happened.

StartTime -> (timestamp)

The time that the resource scan was started.

EndTime -> (timestamp)

The time that the resource scan was finished.

PercentageCompleted -> (double)

The percentage of the resource scan that has been completed.

ResourceTypes -> (list)

The list of resource types for the specified scan. Resource types are only available for scans with a `Status` set to `COMPLETE` or `FAILED` .

(string)

ResourcesScanned -> (integer)

The number of resources that were listed. This is only available for scans with a `Status` set to `COMPLETE` , `EXPIRED` , or `FAILED` .

ResourcesRead -> (integer)

The number of resources that were read. This is only available for scans with a `Status` set to `COMPLETE` , `EXPIRED` , or `FAILED` .

### Note

This field may be 0 if the resource scan failed with a `ResourceScanLimitExceededException` .

ScanFilters -> (list)

The scan filters that were used.

(structure)

A filter that is used to specify which resource types to scan.

Types -> (list)

An array of strings where each string represents an Amazon Web Services resource type you want to scan. Each string defines the resource type using the format `AWS::ServiceName::ResourceType` , for example, `AWS::DynamoDB::Table` . For the full list of supported resource types, see the [Resource type support](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) table in the *CloudFormation User Guide* .

To scan all resource types within a service, you can use a wildcard, represented by an asterisk (`*` ). You can place a asterisk at only the end of the string, for example, `AWS::S3::*` .

(string)