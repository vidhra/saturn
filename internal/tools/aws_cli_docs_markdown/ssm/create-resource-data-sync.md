# create-resource-data-syncÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-resource-data-sync.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-resource-data-sync.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# create-resource-data-sync

## Description

A resource data sync helps you view data from multiple sources in a single location. Amazon Web Services Systems Manager offers two types of resource data sync: `SyncToDestination` and `SyncFromSource` .

You can configure Systems Manager Inventory to use the `SyncToDestination` type to synchronize Inventory data from multiple Amazon Web Services Regions to a single Amazon Simple Storage Service (Amazon S3) bucket. For more information, see [Creating a resource data sync for Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html) in the *Amazon Web Services Systems Manager User Guide* .

You can configure Systems Manager Explorer to use the `SyncFromSource` type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple Amazon Web Services Regions to a single Amazon S3 bucket. This type can synchronize OpsItems and OpsData from multiple Amazon Web Services accounts and Amazon Web Services Regions or `EntireOrganization` by using Organizations. For more information, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the *Amazon Web Services Systems Manager User Guide* .

A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data. To check the status of a sync, use the  ListResourceDataSync .

### Note

By default, data isnât encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/CreateResourceDataSync)

## Synopsis

```
create-resource-data-sync
--sync-name <value>
[--s3-destination <value>]
[--sync-type <value>]
[--sync-source <value>]
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

`--sync-name` (string)

A name for the configuration.

`--s3-destination` (structure)

Amazon S3 configuration details for the sync. This parameter is required if the `SyncType` value is SyncToDestination.

BucketName -> (string)

The name of the S3 bucket where the aggregated data is stored.

Prefix -> (string)

An Amazon S3 prefix for the bucket.

SyncFormat -> (string)

A supported sync format. The following format is currently supported: JsonSerDe

Region -> (string)

The Amazon Web Services Region with the S3 bucket targeted by the resource data sync.

AWSKMSKeyARN -> (string)

The ARN of an encryption key for a destination in Amazon S3. Must belong to the same Region as the destination S3 bucket.

DestinationDataSharing -> (structure)

Enables destination data sharing. By default, this field is `null` .

DestinationDataSharingType -> (string)

The sharing data type. Only `Organization` is supported.

Shorthand Syntax:

```
BucketName=string,Prefix=string,SyncFormat=string,Region=string,AWSKMSKeyARN=string,DestinationDataSharing={DestinationDataSharingType=string}
```

JSON Syntax:

```
{
  "BucketName": "string",
  "Prefix": "string",
  "SyncFormat": "JsonSerDe",
  "Region": "string",
  "AWSKMSKeyARN": "string",
  "DestinationDataSharing": {
    "DestinationDataSharingType": "string"
  }
}
```

`--sync-type` (string)

Specify `SyncToDestination` to create a resource data sync that synchronizes data to an S3 bucket for Inventory. If you specify `SyncToDestination` , you must provide a value for `S3Destination` . Specify `SyncFromSource` to synchronize data from a single account and multiple Regions, or multiple Amazon Web Services accounts and Amazon Web Services Regions, as listed in Organizations for Explorer. If you specify `SyncFromSource` , you must provide a value for `SyncSource` . The default value is `SyncToDestination` .

`--sync-source` (structure)

Specify information about the data sources to synchronize. This parameter is required if the `SyncType` value is SyncFromSource.

SourceType -> (string)

The type of data source for the resource data sync. `SourceType` is either `AwsOrganizations` (if an organization is present in Organizations) or `SingleAccountMultiRegions` .

AwsOrganizationsSource -> (structure)

Information about the `AwsOrganizationsSource` resource data sync source. A sync source of this type can synchronize data from Organizations.

OrganizationSourceType -> (string)

If an Amazon Web Services organization is present, this is either `OrganizationalUnits` or `EntireOrganization` . For `OrganizationalUnits` , the data is aggregated from a set of organization units. For `EntireOrganization` , the data is aggregated from the entire Amazon Web Services organization.

OrganizationalUnits -> (list)

The Organizations organization units included in the sync.

(structure)

The Organizations organizational unit data source for the sync.

OrganizationalUnitId -> (string)

The Organizations unit ID data source for the sync.

SourceRegions -> (list)

The `SyncSource` Amazon Web Services Regions included in the resource data sync.

(string)

IncludeFutureRegions -> (boolean)

Whether to automatically synchronize and aggregate data from new Amazon Web Services Regions when those Regions come online.

EnableAllOpsDataSources -> (boolean)

When you create a resource data sync, if you choose one of the Organizations options, then Systems Manager automatically enables all OpsData sources in the selected Amazon Web Services Regions for all Amazon Web Services accounts in your organization (or in the selected organization units). For more information, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the *Amazon Web Services Systems Manager User Guide* .

JSON Syntax:

```
{
  "SourceType": "string",
  "AwsOrganizationsSource": {
    "OrganizationSourceType": "string",
    "OrganizationalUnits": [
      {
        "OrganizationalUnitId": "string"
      }
      ...
    ]
  },
  "SourceRegions": ["string", ...],
  "IncludeFutureRegions": true|false,
  "EnableAllOpsDataSources": true|false
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

**To create a resource data sync**

This example creates a resource data sync. There is no output if the command succeeds.

Command:

```
aws ssm create-resource-data-sync --sync-name "ssm-resource-data-sync" --s3-destination "BucketName=ssm-bucket,Prefix=inventory,SyncFormat=JsonSerDe,Region=us-east-1"
```

## Output

None