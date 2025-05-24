# list-resource-data-syncÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-data-sync.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-data-sync.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# list-resource-data-sync

## Description

Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.

The number of sync configurations might be too large to return using a single call to `ListResourceDataSync` . You can limit the number of sync configurations returned by using the `MaxResults` parameter. To determine whether there are more sync configurations to list, check the value of `NextToken` in the output. If there are more sync configurations to list, you can request them by specifying the `NextToken` returned in the call to the parameter of a subsequent call.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceDataSync)

`list-resource-data-sync` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResourceDataSyncItems`

## Synopsis

```
list-resource-data-sync
[--sync-type <value>]
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

`--sync-type` (string)

View a list of resource data syncs according to the sync type. Specify `SyncToDestination` to view resource data syncs that synchronize data to an Amazon S3 bucket. Specify `SyncFromSource` to view resource data syncs from Organizations or from multiple Amazon Web Services Regions.

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

**To list your resource data sync configurations**

This example retrieves information about your resource data sync configurations.

```
aws ssm list-resource-data-sync
```

Output:

```
{
    "ResourceDataSyncItems": [
        {
            "SyncName": "MyResourceDataSync",
            "S3Destination": {
                "BucketName": "ssm-resource-data-sync",
                "SyncFormat": "JsonSerDe",
                "Region": "us-east-1"
            },
            "LastSyncTime": 1550261472.003,
            "LastSuccessfulSyncTime": 1550261472.003,
            "LastStatus": "Successful",
            "SyncCreatedTime": 1543235736.72,
            "LastSyncStatusMessage": "The sync was successfully completed"
        }
    ]
}
```

## Output

ResourceDataSyncItems -> (list)

A list of your current resource data sync configurations and their statuses.

(structure)

Information about a resource data sync configuration, including its current status and last successful sync.

SyncName -> (string)

The name of the resource data sync.

SyncType -> (string)

The type of resource data sync. If `SyncType` is `SyncToDestination` , then the resource data sync synchronizes data to an S3 bucket. If the `SyncType` is `SyncFromSource` then the resource data sync synchronizes data from Organizations or from multiple Amazon Web Services Regions.

SyncSource -> (structure)

Information about the source where the data was synchronized.

SourceType -> (string)

The type of data source for the resource data sync. `SourceType` is either `AwsOrganizations` (if an organization is present in Organizations) or `singleAccountMultiRegions` .

AwsOrganizationsSource -> (structure)

The field name in `SyncSource` for the `ResourceDataSyncAwsOrganizationsSource` type.

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

State -> (string)

The data type name for including resource data sync state. There are four sync states:

`OrganizationNotExists` : Your organization doesnât exist.

`NoPermissions` : The system canât locate the service-linked role. This role is automatically created when a user creates a resource data sync in Explorer.

`InvalidOrganizationalUnit` : You specified or selected an invalid unit in the resource data sync configuration.

`TrustedAccessDisabled` : You disabled Systems Manager access in the organization in Organizations.

EnableAllOpsDataSources -> (boolean)

When you create a resource data sync, if you choose one of the Organizations options, then Systems Manager automatically enables all OpsData sources in the selected Amazon Web Services Regions for all Amazon Web Services accounts in your organization (or in the selected organization units). For more information, see [Setting up Systems Manager Explorer to display data from multiple accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the *Amazon Web Services Systems Manager User Guide* .

S3Destination -> (structure)

Configuration information for the target S3 bucket.

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

LastSyncTime -> (timestamp)

The last time the configuration attempted to sync (UTC).

LastSuccessfulSyncTime -> (timestamp)

The last time the sync operations returned a status of `SUCCESSFUL` (UTC).

SyncLastModifiedTime -> (timestamp)

The date and time the resource data sync was changed.

LastStatus -> (string)

The status reported by the last sync.

SyncCreatedTime -> (timestamp)

The date and time the configuration was created (UTC).

LastSyncStatusMessage -> (string)

The status message details reported by the last sync.

NextToken -> (string)

The token for the next set of items to return. Use this token to get the next set of results.