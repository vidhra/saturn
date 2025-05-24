# update-resource-data-syncÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-resource-data-sync.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-resource-data-sync.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# update-resource-data-sync

## Description

Update a resource data sync. After you create a resource data sync for a Region, you canât change the account options for that sync. For example, if you create a sync in the us-east-2 (Ohio) Region and you choose the `Include only the current account` option, you canât edit that sync later and choose the `Include all accounts from my Organizations configuration` option. Instead, you must delete the first resource data sync, and create a new one.

### Note

This API operation only supports a resource data sync that was created with a SyncFromSource `SyncType` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateResourceDataSync)

## Synopsis

```
update-resource-data-sync
--sync-name <value>
--sync-type <value>
--sync-source <value>
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

The name of the resource data sync you want to update.

`--sync-type` (string)

The type of resource data sync. The supported `SyncType` is SyncFromSource.

`--sync-source` (structure)

Specify information about the data sources to synchronize.

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

**To update a resource data sync**

The following `update-resource-data-sync` example updates a SyncFromSource resource data sync.

```
aws ssm update-resource-data-sync \
    --sync-name exampleSync \
    --sync-type SyncFromSource \
    --sync-source '{"SourceType":"SingleAccountMultiRegions", "SourceRegions":["us-east-1", "us-west-2"]}'
```

This command produces no output.

For more information, see [Setting Up Systems Manager Explorer to Display Data from Multiple Accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html) in the *AWS Systems Manager User Guide*.

## Output

None