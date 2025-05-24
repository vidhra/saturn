# describe-launch-configuration-templatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/describe-launch-configuration-templates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/describe-launch-configuration-templates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mgn](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/index.html#cli-aws-mgn) ]

# describe-launch-configuration-templates

## Description

Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mgn-2020-02-26/DescribeLaunchConfigurationTemplates)

`describe-launch-configuration-templates` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
describe-launch-configuration-templates
[--launch-configuration-template-ids <value>]
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

`--launch-configuration-template-ids` (list)

Request to filter Launch Configuration Templates list by Launch Configuration Template ID.

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

## Output

items -> (list)

List of items returned by DescribeLaunchConfigurationTemplates.

(structure)

arn -> (string)

ARN of the Launch Configuration Template.

associatePublicIpAddress -> (boolean)

Associate public Ip address.

bootMode -> (string)

Launch configuration template boot mode.

copyPrivateIp -> (boolean)

Copy private Ip.

copyTags -> (boolean)

Copy tags.

ec2LaunchTemplateID -> (string)

EC2 launch template ID.

enableMapAutoTagging -> (boolean)

Enable map auto tagging.

largeVolumeConf -> (structure)

Large volume config.

iops -> (long)

Launch template disk iops configuration.

throughput -> (long)

Launch template disk throughput configuration.

volumeType -> (string)

Launch template disk volume type configuration.

launchConfigurationTemplateID -> (string)

ID of the Launch Configuration Template.

launchDisposition -> (string)

Launch disposition.

licensing -> (structure)

Configure Licensing.

osByol -> (boolean)

Configure BYOL OS licensing.

mapAutoTaggingMpeID -> (string)

Launch configuration template map auto tagging MPE ID.

postLaunchActions -> (structure)

Post Launch Actions of the Launch Configuration Template.

cloudWatchLogGroupName -> (string)

AWS Systems Manager Commandâs CloudWatch log group name.

deployment -> (string)

Deployment type in which AWS Systems Manager Documents will be executed.

s3LogBucket -> (string)

AWS Systems Manager Commandâs logs S3 log bucket.

s3OutputKeyPrefix -> (string)

AWS Systems Manager Commandâs logs S3 output key prefix.

ssmDocuments -> (list)

AWS Systems Manager Documents.

(structure)

AWS Systems Manager Document.

actionName -> (string)

User-friendly name for the AWS Systems Manager Document.

externalParameters -> (map)

AWS Systems Manager Document external parameters.

key -> (string)

value -> (tagged union structure)

AWS Systems Manager Document external parameter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dynamicPath`.

dynamicPath -> (string)

AWS Systems Manager Document external parameters dynamic path.

mustSucceedForCutover -> (boolean)

If true, Cutover will not be enabled if the document has failed.

parameters -> (map)

AWS Systems Manager Document parameters.

key -> (string)

value -> (list)

(structure)

AWS Systems Manager Parameter Store parameter.

parameterName -> (string)

AWS Systems Manager Parameter Store parameter name.

parameterType -> (string)

AWS Systems Manager Parameter Store parameter type.

ssmDocumentName -> (string)

AWS Systems Manager Document name or full ARN.

timeoutSeconds -> (integer)

AWS Systems Manager Document timeout seconds.

smallVolumeConf -> (structure)

Small volume config.

iops -> (long)

Launch template disk iops configuration.

throughput -> (long)

Launch template disk throughput configuration.

volumeType -> (string)

Launch template disk volume type configuration.

smallVolumeMaxSize -> (long)

Small volume maximum size.

tags -> (map)

Tags of the Launch Configuration Template.

key -> (string)

value -> (string)

targetInstanceTypeRightSizingMethod -> (string)

Target instance type right-sizing method.

nextToken -> (string)

Next pagination token returned from DescribeLaunchConfigurationTemplates.