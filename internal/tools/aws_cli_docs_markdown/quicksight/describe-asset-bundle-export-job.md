# describe-asset-bundle-export-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-asset-bundle-export-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-asset-bundle-export-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# describe-asset-bundle-export-job

## Description

Describes an existing export job.

Poll job descriptions after a job starts to know the status of the job. When a job succeeds, a URL is provided to download the exported assetsâ data from. Download URLs are valid for five minutes after they are generated. You can call the `DescribeAssetBundleExportJob` API for a new download URL as needed.

Job descriptions are available for 14 days after the job starts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/DescribeAssetBundleExportJob)

## Synopsis

```
describe-asset-bundle-export-job
--aws-account-id <value>
--asset-bundle-export-job-id <value>
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

`--aws-account-id` (string)

The ID of the Amazon Web Services account the export job is executed in.

`--asset-bundle-export-job-id` (string)

The ID of the job that you want described. The job ID is set when you start a new job with a `StartAssetBundleExportJob` API call.

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

JobStatus -> (string)

Indicates the status of a job through its queuing and execution.

Poll this `DescribeAssetBundleExportApi` until `JobStatus` is either `SUCCESSFUL` or `FAILED` .

DownloadUrl -> (string)

The URL to download the exported asset bundle data from.

This URL is available only after the job has succeeded. This URL is valid for 5 minutes after issuance. Call `DescribeAssetBundleExportJob` again for a fresh URL if needed.

The downloaded asset bundle is a zip file named `assetbundle-{jobId}.qs` . The file has a `.qs` extension.

This URL canât be used in a `StartAssetBundleImportJob` API call and should only be used for download purposes.

Errors -> (list)

An array of error records that describes any failures that occurred during the export job processing.

Error records accumulate while the job runs. The complete set of error records is available after the job has completed and failed.

(structure)

Describes an error that occurred during an Asset Bundle export job.

Arn -> (string)

The ARN of the resource whose processing caused an error.

Type -> (string)

The specific error type of the error that occurred.

Message -> (string)

A description of the error.

Arn -> (string)

The Amazon Resource Name (ARN) for the export job.

CreatedTime -> (timestamp)

The time that the export job was created.

AssetBundleExportJobId -> (string)

The ID of the job. The job ID is set when you start a new job with a `StartAssetBundleExportJob` API call.

AwsAccountId -> (string)

The ID of the Amazon Web Services account that the export job was executed in.

ResourceArns -> (list)

A list of resource ARNs that exported with the job.

(string)

IncludeAllDependencies -> (boolean)

The include dependencies flag.

ExportFormat -> (string)

The format of the exported asset bundle. A `QUICKSIGHT_JSON` formatted file can be used to make a `StartAssetBundleImportJob` API call. A `CLOUDFORMATION_JSON` formatted file can be used in the CloudFormation console and with the CloudFormation APIs.

CloudFormationOverridePropertyConfiguration -> (structure)

The CloudFormation override property configuration for the export job.

ResourceIdOverrideConfiguration -> (structure)

An optional list of structures that control how resource IDs are parameterized in the returned CloudFormation template.

PrefixForAllResources -> (boolean)

An option to request a CloudFormation variable for a prefix to be prepended to each resourceâs ID before import. The prefix is only added to the asset IDs and does not change the name of the asset.

VPCConnections -> (list)

An optional list of structures that control how `VPCConnection` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `VPCConnection` resource is parameterized in the outputted CloudFormation template.

Arn -> (string)

The ARN of the specific `VPCConnection` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `VPCConnection` resource properties to generate variables for in the returned CloudFormation template.

(string)

RefreshSchedules -> (list)

An optional list of structures that control how `RefreshSchedule` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `RefreshSchedule` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `RefreshSchedule` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `RefreshSchedule` resource properties to generate variables for in the returned CloudFormation template.

(string)

DataSources -> (list)

An optional list of structures that control how `DataSource` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `DataSource` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `DataSource` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `DataSource` resource properties to generate variables for in the returned CloudFormation template.

(string)

DataSets -> (list)

An optional list of structures that control how `DataSet` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `DataSet` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `DataSet` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `DataSet` resource properties to generate variables for in the returned CloudFormation template.

(string)

Themes -> (list)

An optional list of structures that control how `Theme` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `Theme` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `Theme` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `Theme` resource properties to generate variables for in the returned CloudFormation template.

(string)

Analyses -> (list)

An optional list of structures that control how `Analysis` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `Analysis` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `Analysis` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `Analysis` resource properties to generate variables for in the returned CloudFormation template.

(string)

Dashboards -> (list)

An optional list of structures that control how `Dashboard` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `Dashboard` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `Dashboard` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `Dashboard` resource properties to generate variables for in the returned CloudFormation template.

(string)

Folders -> (list)

An optional list of structures that controls how `Folder` resources are parameterized in the returned CloudFormation template.

(structure)

Controls how a specific `Folder` resource is parameterized in the returned CloudFormation template.

Arn -> (string)

The ARN of the specific `Folder` resource whose override properties are configured in this structure.

Properties -> (list)

A list of `Folder` resource properties to generate variables for in the returned CloudFormation template.

(string)

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the response.

IncludePermissions -> (boolean)

The include permissions flag.

IncludeTags -> (boolean)

The include tags flag.

ValidationStrategy -> (structure)

The validation strategy that is used to export the analysis or dashboard.

StrictModeForAllResources -> (boolean)

A Boolean value that indicates whether to export resources under strict or lenient mode.

Warnings -> (list)

An array of warning records that describe the analysis or dashboard that is exported. This array includes UI errors that can be skipped during the validation process.

This property only appears if `StrictModeForAllResources` in `ValidationStrategy` is set to `FALSE` .

(structure)

Describes a warning that occurred during an Asset Bundle export job.

Arn -> (string)

The ARN of the resource whose processing caused a warning.

Message -> (string)

A description of the warning.

IncludeFolderMemberships -> (boolean)

The include folder memberships flag.

IncludeFolderMembers -> (string)

A setting that determines whether folder members are included.