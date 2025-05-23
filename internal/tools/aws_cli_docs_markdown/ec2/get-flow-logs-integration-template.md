# get-flow-logs-integration-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-flow-logs-integration-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-flow-logs-integration-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# get-flow-logs-integration-template

## Description

Generates a CloudFormation template that streamlines and automates the integration of VPC flow logs with Amazon Athena. This make it easier for you to query and gain insights from VPC flow logs data. Based on the information that you provide, we configure resources in the template to do the following:

- Create a table in Athena that maps fields to a custom log format
- Create a Lambda function that updates the table with new partitions on a daily, weekly, or monthly basis
- Create a table partitioned between two timestamps in the past
- Create a set of named queries in Athena that you can use to get started quickly

### Note

`GetFlowLogsIntegrationTemplate` does not support integration between Amazon Web Services Transit Gateway Flow Logs and Amazon Athena.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetFlowLogsIntegrationTemplate)

## Synopsis

```
get-flow-logs-integration-template
[--dry-run | --no-dry-run]
--flow-log-id <value>
--config-delivery-s3-destination-arn <value>
--integrate-services <value>
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--flow-log-id` (string)

The ID of the flow log.

`--config-delivery-s3-destination-arn` (string)

To store the CloudFormation template in Amazon S3, specify the location in Amazon S3.

`--integrate-services` (structure)

Information about the service integration.

AthenaIntegrations -> (list)

Information about the integration with Amazon Athena.

(structure)

Describes integration options for Amazon Athena.

IntegrationResultS3DestinationArn -> (string)

The location in Amazon S3 to store the generated CloudFormation template.

PartitionLoadFrequency -> (string)

The schedule for adding new partitions to the table.

PartitionStartDate -> (timestamp)

The start date for the partition.

PartitionEndDate -> (timestamp)

The end date for the partition.

Shorthand Syntax:

```
AthenaIntegrations=[{IntegrationResultS3DestinationArn=string,PartitionLoadFrequency=string,PartitionStartDate=timestamp,PartitionEndDate=timestamp},{IntegrationResultS3DestinationArn=string,PartitionLoadFrequency=string,PartitionStartDate=timestamp,PartitionEndDate=timestamp}]
```

JSON Syntax:

```
{
  "AthenaIntegrations": [
    {
      "IntegrationResultS3DestinationArn": "string",
      "PartitionLoadFrequency": "none"|"daily"|"weekly"|"monthly",
      "PartitionStartDate": timestamp,
      "PartitionEndDate": timestamp
    }
    ...
  ]
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a CloudFormation template to automate the integration of VPC flow logs with Amazon Athena**

The following `get-flow-logs-integration-template` examples create a CloudFormation template to automate the integration of VPC flow logs with Amazon Athena.

Linux:

```
aws ec2 get-flow-logs-integration-template \
    --flow-log-id fl-1234567890abcdef0 \
    --config-delivery-s3-destination-arn arn:aws:s3:::amzn-s3-demo-bucket \
    --integrate-services AthenaIntegrations='[{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00},{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00}]'
```

Windows:

```
aws ec2 get-flow-logs-integration-template ^
    --flow-log-id fl-1234567890abcdef0 ^
    --config-delivery-s3-destination-arn arn:aws:s3:::amzn-s3-demo-bucket ^
    --integrate-services AthenaIntegrations=[{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00},{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00}]
```

Output:

```
{
    "Result": "https://amzn-s3-demo-bucket.s3.us-east-2.amazonaws.com/VPCFlowLogsIntegrationTemplate_fl-1234567890abcdef0_Wed%20Jul%2021%2000%3A57%3A56%20UTC%202021.yml"
}
```

For information on using CloudFormation templates, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*.

For information on using Amazon Athena and flow logs, see [Query flow logs using Amazon Athena](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-athena.html) in the *Amazon Virtual Private Cloud User Guide*.

## Output

Result -> (string)

The generated CloudFormation template.