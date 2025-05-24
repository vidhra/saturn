# start-asset-bundle-export-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/start-asset-bundle-export-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/start-asset-bundle-export-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# start-asset-bundle-export-job

## Description

Starts an Asset Bundle export job.

An Asset Bundle export job exports specified Amazon QuickSight assets. You can also choose to export any asset dependencies in the same job. Export jobs run asynchronously and can be polled with a `DescribeAssetBundleExportJob` API call. When a job is successfully completed, a download URL that contains the exported assets is returned. The URL is valid for 5 minutes and can be refreshed with a `DescribeAssetBundleExportJob` API call. Each Amazon QuickSight account can run up to 5 export jobs concurrently.

The API caller must have the necessary permissions in their IAM role to access each resource before the resources can be exported.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/StartAssetBundleExportJob)

## Synopsis

```
start-asset-bundle-export-job
--aws-account-id <value>
--asset-bundle-export-job-id <value>
--resource-arns <value>
[--include-all-dependencies | --no-include-all-dependencies]
--export-format <value>
[--cloud-formation-override-property-configuration <value>]
[--include-permissions | --no-include-permissions]
[--include-tags | --no-include-tags]
[--validation-strategy <value>]
[--include-folder-memberships | --no-include-folder-memberships]
[--include-folder-members <value>]
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

The ID of the Amazon Web Services account to export assets from.

`--asset-bundle-export-job-id` (string)

The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.

`--resource-arns` (list)

An array of resource ARNs to export. The following resources are supported.

- `Analysis`
- `Dashboard`
- `DataSet`
- `DataSource`
- `RefreshSchedule`
- `Theme`
- `VPCConnection`

The API caller must have the necessary permissions in their IAM role to access each resource before the resources can be exported.

(string)

Syntax:

```
"string" "string" ...
```

`--include-all-dependencies` | `--no-include-all-dependencies` (boolean)

A Boolean that determines whether all dependencies of each resource ARN are recursively exported with the job. For example, say you provided a Dashboard ARN to the `ResourceArns` parameter. If you set `IncludeAllDependencies` to `TRUE` , any theme, dataset, and data source resource that is a dependency of the dashboard is also exported.

`--export-format` (string)

The export data format.

Possible values:

- `CLOUDFORMATION_JSON`
- `QUICKSIGHT_JSON`

`--cloud-formation-override-property-configuration` (structure)

An optional collection of structures that generate CloudFormation parameters to override the existing resource property values when the resource is exported to a new CloudFormation template.

Use this field if the `ExportFormat` field of a `StartAssetBundleExportJobRequest` API call is set to `CLOUDFORMATION_JSON` .

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

JSON Syntax:

```
{
  "ResourceIdOverrideConfiguration": {
    "PrefixForAllResources": true|false
  },
  "VPCConnections": [
    {
      "Arn": "string",
      "Properties": ["Name"|"DnsResolvers"|"RoleArn", ...]
    }
    ...
  ],
  "RefreshSchedules": [
    {
      "Arn": "string",
      "Properties": ["StartAfterDateTime", ...]
    }
    ...
  ],
  "DataSources": [
    {
      "Arn": "string",
      "Properties": ["Name"|"DisableSsl"|"SecretArn"|"Username"|"Password"|"Domain"|"WorkGroup"|"Host"|"Port"|"Database"|"DataSetName"|"Catalog"|"InstanceId"|"ClusterId"|"ManifestFileLocation"|"Warehouse"|"RoleArn"|"ProductType", ...]
    }
    ...
  ],
  "DataSets": [
    {
      "Arn": "string",
      "Properties": ["Name"|"RefreshFailureEmailAlertStatus", ...]
    }
    ...
  ],
  "Themes": [
    {
      "Arn": "string",
      "Properties": ["Name", ...]
    }
    ...
  ],
  "Analyses": [
    {
      "Arn": "string",
      "Properties": ["Name", ...]
    }
    ...
  ],
  "Dashboards": [
    {
      "Arn": "string",
      "Properties": ["Name", ...]
    }
    ...
  ],
  "Folders": [
    {
      "Arn": "string",
      "Properties": ["Name"|"ParentFolderArn", ...]
    }
    ...
  ]
}
```

`--include-permissions` | `--no-include-permissions` (boolean)

A Boolean that determines whether all permissions for each resource ARN are exported with the job. If you set `IncludePermissions` to `TRUE` , any permissions associated with each resource are exported.

`--include-tags` | `--no-include-tags` (boolean)

A Boolean that determines whether all tags for each resource ARN are exported with the job. If you set `IncludeTags` to `TRUE` , any tags associated with each resource are exported.

`--validation-strategy` (structure)

An optional parameter that determines which validation strategy to use for the export job. If `StrictModeForAllResources` is set to `TRUE` , strict validation for every error is enforced. If it is set to `FALSE` , validation is skipped for specific UI errors that are shown as warnings. The default value for `StrictModeForAllResources` is `FALSE` .

StrictModeForAllResources -> (boolean)

A Boolean value that indicates whether to export resources under strict or lenient mode.

Shorthand Syntax:

```
StrictModeForAllResources=boolean
```

JSON Syntax:

```
{
  "StrictModeForAllResources": true|false
}
```

`--include-folder-memberships` | `--no-include-folder-memberships` (boolean)

A Boolean that determines if the exported asset carries over information about the folders that the asset is a member of.

`--include-folder-members` (string)

A setting that indicates whether you want to include folder assets. You can also use this setting to recusrsively include all subfolders of an exported folder.

Possible values:

- `RECURSE`
- `ONE_LEVEL`
- `NONE`

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

Arn -> (string)

The Amazon Resource Name (ARN) for the export job.

AssetBundleExportJobId -> (string)

The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.

RequestId -> (string)

The Amazon Web Services response ID for this operation.

Status -> (integer)

The HTTP status of the response.