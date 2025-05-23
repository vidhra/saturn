# create-license-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/index.html#cli-aws-license-manager) ]

# create-license-configuration

## Description

Creates a license configuration.

A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), license affinity to host (how long a license must be associated with a host), and the number of licenses purchased and used.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/CreateLicenseConfiguration)

## Synopsis

```
create-license-configuration
--name <value>
[--description <value>]
--license-counting-type <value>
[--license-count <value>]
[--license-count-hard-limit | --no-license-count-hard-limit]
[--license-rules <value>]
[--tags <value>]
[--disassociate-when-not-found | --no-disassociate-when-not-found]
[--product-information-list <value>]
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

`--name` (string)

Name of the license configuration.

`--description` (string)

Description of the license configuration.

`--license-counting-type` (string)

Dimension used to track the license inventory.

Possible values:

- `vCPU`
- `Instance`
- `Core`
- `Socket`

`--license-count` (long)

Number of licenses managed by the license configuration.

`--license-count-hard-limit` | `--no-license-count-hard-limit` (boolean)

Indicates whether hard or soft license enforcement is used. Exceeding a hard limit blocks the launch of new instances.

`--license-rules` (list)

License rules. The syntax is #name=value (for example, #allowedTenancy=EC2-DedicatedHost). The available rules vary by dimension, as follows.

- `Cores` dimension: `allowedTenancy` | `licenseAffinityToHost` | `maximumCores` | `minimumCores`
- `Instances` dimension: `allowedTenancy` | `maximumVcpus` | `minimumVcpus`
- `Sockets` dimension: `allowedTenancy` | `licenseAffinityToHost` | `maximumSockets` | `minimumSockets`
- `vCPUs` dimension: `allowedTenancy` | `honorVcpuOptimization` | `maximumVcpus` | `minimumVcpus`

The unit for `licenseAffinityToHost` is days and the range is 1 to 180. The possible values for `allowedTenancy` are `EC2-Default` , `EC2-DedicatedHost` , and `EC2-DedicatedInstance` . The possible values for `honorVcpuOptimization` are `True` and `False` .

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

Tags to add to the license configuration.

(structure)

Details about the tags for a resource. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.

Key -> (string)

The tag key.

Value -> (string)

The tag value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--disassociate-when-not-found` | `--no-disassociate-when-not-found` (boolean)

When true, disassociates a resource when software is uninstalled.

`--product-information-list` (list)

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

JSON Syntax:

```
[
  {
    "ResourceType": "string",
    "ProductInformationFilterList": [
      {
        "ProductInformationFilterName": "string",
        "ProductInformationFilterValue": ["string", ...],
        "ProductInformationFilterComparator": "string"
      }
      ...
    ]
  }
  ...
]
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

**Example 1: To create a license configuration**

The following `create-license-configuration` example creates a license configuration with a hard limit of 10 cores.

```
aws license-manager create-license-configuration --name my-license-configuration \
    --license-counting-type Core \
    --license-count 10 \
    --license-count-hard-limit
```

Output:

```
{
  "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba41EXAMPLE1111"
}
```

**Example 2: To create a license configuration**

The following `create-license-configuration` example creates a license configuration with a soft limit of 100 vCPUs. It uses a rule to enable vCPU optimization.

```
aws license-manager create-license-configuration --name my-license-configuration
    --license-counting-type vCPU \
    --license-count 100 \
    --license-rules "#honorVcpuOptimization=true"
```

Output:

```
{
  "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba41EXAMPLE2222"
}
```

## Output

LicenseConfigurationArn -> (string)

Amazon Resource Name (ARN) of the license configuration.