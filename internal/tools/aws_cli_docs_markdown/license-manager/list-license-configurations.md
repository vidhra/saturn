# list-license-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/index.html#cli-aws-license-manager) ]

# list-license-configurations

## Description

Lists the license configurations for your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/ListLicenseConfigurations)

`list-license-configurations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `LicenseConfigurations`

## Synopsis

```
list-license-configurations
[--license-configuration-arns <value>]
[--filters <value>]
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

`--license-configuration-arns` (list)

Amazon Resource Names (ARN) of the license configurations.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

Filters to scope the results. The following filters and logical operators are supported:

- `licenseCountingType` - The dimension for which licenses are counted. Possible values are `vCPU` | `Instance` | `Core` | `Socket` .
- `enforceLicenseCount` - A Boolean value that indicates whether hard license enforcement is used.
- `usagelimitExceeded` - A Boolean value that indicates whether the available licenses have been exceeded.

(structure)

A filter name and value pair that is used to return more specific results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

Name -> (string)

Name of the filter. Filter names are case-sensitive.

Values -> (list)

The value of the filter, which is case-sensitive. You can only specify one value for the filter.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
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

**Example 1: To list all of your license configurations**

The following `list-license-configurations` example lists all your license configurations.

```
aws license-manager list-license-configurations
```

Output:

```
{
    "LicenseConfigurations": [
        {
            "LicenseConfigurationId": "lic-6eb6586f508a786a2ba4f56c1EXAMPLE",
            "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE",
            "Name": "my-license-configuration",
            "LicenseCountingType": "Core",
            "LicenseRules": [],
            "LicenseCount": 10,
            "LicenseCountHardLimit": true,
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
                    "AssociationCount": 0
                },
                {
                    "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE",
                    "AssociationCount": 0
                }
            ]
        },
        {
            ...
        }
    ]
}
```

**Example 2: To list a specific license configuration**

The following `list-license-configurations` example lists only the specified license configuration.

```
aws license-manager list-license-configurations \
    --license-configuration-arns arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE
```

## Output

LicenseConfigurations -> (list)

Information about the license configurations.

(structure)

A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.

LicenseConfigurationId -> (string)

Unique ID of the license configuration.

LicenseConfigurationArn -> (string)

Amazon Resource Name (ARN) of the license configuration.

Name -> (string)

Name of the license configuration.

Description -> (string)

Description of the license configuration.

LicenseCountingType -> (string)

Dimension to use to track the license inventory.

LicenseRules -> (list)

License rules.

(string)

LicenseCount -> (long)

Number of licenses managed by the license configuration.

LicenseCountHardLimit -> (boolean)

Number of available licenses as a hard limit.

DisassociateWhenNotFound -> (boolean)

When true, disassociates a resource when software is uninstalled.

ConsumedLicenses -> (long)

Number of licenses consumed.

Status -> (string)

Status of the license configuration.

OwnerAccountId -> (string)

Account ID of the license configurationâs owner.

ConsumedLicenseSummaryList -> (list)

Summaries for licenses consumed by various resources.

(structure)

Details about license consumption.

ResourceType -> (string)

Resource type of the resource consuming a license.

ConsumedLicenses -> (long)

Number of licenses consumed by the resource.

ManagedResourceSummaryList -> (list)

Summaries for managed resources.

(structure)

Summary information about a managed resource.

ResourceType -> (string)

Type of resource associated with a license.

AssociationCount -> (long)

Number of resources associated with licenses.

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

NextToken -> (string)

Token for the next set of results.