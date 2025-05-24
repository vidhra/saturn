# get-license-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/index.html#cli-aws-license-manager) ]

# get-license-configuration

## Description

Gets detailed information about the specified license configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/GetLicenseConfiguration)

## Synopsis

```
get-license-configuration
--license-configuration-arn <value>
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

`--license-configuration-arn` (string)

Amazon Resource Name (ARN) of the license configuration.

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

**To get license configuration information**

The following `get-license-configuration` example displays details for the specified license configuration.

```
aws license-manager get-license-configuration \
    --license-configuration-arn arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE
```

Output:

```
{
    "LicenseConfigurationId": "lic-38b658717b87478aaa7c00883EXAMPLE",
    "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE",
    "Name": "my-license-configuration",
    "LicenseCountingType": "vCPU",
    "LicenseRules": [],
    "LicenseCountHardLimit": false,
    "ConsumedLicenses": 0,
    "Status": "AVAILABLE",
    "OwnerAccountId": "123456789012",
    "ConsumedLicenseSummaryList": [
        {
            "ResourceType": "EC2_INSTANCE",
            "ConsumedLicenses": 0
        },
        {
            "ResourceType": "EC2_HOST",
            "ConsumedLicenses": 0
        },
        {
            "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE",
            "ConsumedLicenses": 0
        }
    ],
    "ManagedResourceSummaryList": [
        {
            "ResourceType": "EC2_INSTANCE",
            "AssociationCount": 0
        },
        {
            "ResourceType": "EC2_HOST",
            "AssociationCount": 0
        },
        {
            "ResourceType": "EC2_AMI",
            "AssociationCount": 2
        },
        {
            "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE",
            "AssociationCount": 0
        }
    ]
}
```

## Output

LicenseConfigurationId -> (string)

Unique ID for the license configuration.

LicenseConfigurationArn -> (string)

Amazon Resource Name (ARN) of the license configuration.

Name -> (string)

Name of the license configuration.

Description -> (string)

Description of the license configuration.

LicenseCountingType -> (string)

Dimension for which the licenses are counted.

LicenseRules -> (list)

License rules.

(string)

LicenseCount -> (long)

Number of available licenses.

LicenseCountHardLimit -> (boolean)

Sets the number of available licenses as a hard limit.

ConsumedLicenses -> (long)

Number of licenses assigned to resources.

Status -> (string)

License configuration status.

OwnerAccountId -> (string)

Account ID of the owner of the license configuration.

ConsumedLicenseSummaryList -> (list)

Summaries of the licenses consumed by resources.

(structure)

Details about license consumption.

ResourceType -> (string)

Resource type of the resource consuming a license.

ConsumedLicenses -> (long)

Number of licenses consumed by the resource.

ManagedResourceSummaryList -> (list)

Summaries of the managed resources.

(structure)

Summary information about a managed resource.

ResourceType -> (string)

Type of resource associated with a license.

AssociationCount -> (long)

Number of resources associated with licenses.

Tags -> (list)

Tags for the license configuration.

(structure)

Details about the tags for a resource. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

ProductInformationList -> (list)

Product information.

(structure)

Describes product information for a license configuration.

ResourceType -> (string)

Resource type. The possible values are `SSM_MANAGED` | `RDS` .

ProductInformationFilterList -> (list)

A Product information filter consists of a `ProductInformationFilterComparator` which is a logical operator, a `ProductInformationFilterName` which specifies the type of filter being declared, and a `ProductInformationFilterValue` that specifies the value to filter on.

Accepted values for `ProductInformationFilterName` are listed here along with descriptions and valid options for `ProductInformationFilterComparator` .

The following filters and are supported when the resource type is `SSM_MANAGED` :

- `Application Name` - The name of the application. Logical operator is `EQUALS` .
- `Application Publisher` - The publisher of the application. Logical operator is `EQUALS` .
- `Application Version` - The version of the application. Logical operator is `EQUALS` .
- `Platform Name` - The name of the platform. Logical operator is `EQUALS` .
- `Platform Type` - The platform type. Logical operator is `EQUALS` .
- `Tag:key` - The key of a tag attached to an Amazon Web Services resource you wish to exclude from automated discovery. Logical operator is `NOT_EQUALS` . The key for your tag must be appended to `Tag:` following the example: `Tag:name-of-your-key` . `ProductInformationFilterValue` is optional if you are not using values for the key.
- `AccountId` - The 12-digit ID of an Amazon Web Services account you wish to exclude from automated discovery. Logical operator is `NOT_EQUALS` .
- `License Included` - The type of license included. Logical operators are `EQUALS` and `NOT_EQUALS` . Possible values are: `sql-server-enterprise` | `sql-server-standard` | `sql-server-web` | `windows-server-datacenter` .

The following filters and logical operators are supported when the resource type is `RDS` :

- `Engine Edition` - The edition of the database engine. Logical operator is `EQUALS` . Possible values are: `oracle-ee` | `oracle-se` | `oracle-se1` | `oracle-se2` | `db2-se` | `db2-ae` .
- `License Pack` - The license pack. Logical operator is `EQUALS` . Possible values are: `data guard` | `diagnostic pack sqlt` | `tuning pack sqlt` | `ols` | `olap` .

(structure)

Describes product information filters.

ProductInformationFilterName -> (string)

Filter name.

ProductInformationFilterValue -> (list)

Filter value.

(string)

ProductInformationFilterComparator -> (string)

Logical operator.

AutomatedDiscoveryInformation -> (structure)

Automated discovery information.

LastRunTime -> (timestamp)

Time that automated discovery last ran.

DisassociateWhenNotFound -> (boolean)

When true, disassociates a resource when software is uninstalled.