# describe-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# describe-recommendations

## Description

Returns a paginated list of target engine recommendations for your source databases.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeRecommendations)

## Synopsis

```
describe-recommendations
[--filters <value>]
[--max-records <value>]
[--next-token <value>]
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

`--filters` (list)

Filters applied to the target engine recommendations described in the form of key-value pairs.

Valid filter names: `database-id` | `engine-name`

(structure)

Identifies the name and value of a filter object. This filter is used to limit the number and type of DMS objects that are returned for a particular `Describe*` call or similar operation. Filters are used as an optional parameter for certain API operations.

Name -> (string)

The name of the filter as specified for a `Describe*` or similar operation.

Values -> (list)

The filter value, which can specify one or more values used to narrow the returned results.

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

`--max-records` (integer)

The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, Fleet Advisor includes a pagination token in the response so that you can retrieve the remaining results.

`--next-token` (string)

Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

If `NextToken` is returned by a previous response, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.

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

NextToken -> (string)

The unique pagination token returned for you to pass to a subsequent request. Fleet Advisor returns this token when the number of records in the response is greater than the `MaxRecords` value. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.

Recommendations -> (list)

The list of recommendations of target engines that Fleet Advisor created for the source database.

(structure)

Provides information that describes a recommendation of a target engine.

A *recommendation* is a set of possible Amazon Web Services target engines that you can choose to migrate your source on-premises database. In this set, Fleet Advisor suggests a single target engine as the right sized migration destination. To determine this rightsized migration destination, Fleet Advisor uses the inventory metadata and metrics from data collector. You can use recommendations before the start of migration to save costs and reduce risks.

With recommendations, you can explore different target options and compare metrics, so you can make an informed decision when you choose the migration target.

DatabaseId -> (string)

The identifier of the source database for which Fleet Advisor provided this recommendation.

EngineName -> (string)

The name of the target engine. Valid values include `"rds-aurora-mysql"` , `"rds-aurora-postgresql"` , `"rds-mysql"` , `"rds-oracle"` , `"rds-sql-server"` , and `"rds-postgresql"` .

CreatedDate -> (string)

The date when Fleet Advisor created the target engine recommendation.

Status -> (string)

The status of the target engine recommendation. Valid values include `"alternate"` , `"in-progress"` , `"not-viable"` , and `"recommended"` .

Preferred -> (boolean)

Indicates that this target is the rightsized migration destination.

Settings -> (structure)

The settings in JSON format for the preferred target engine parameters. These parameters include capacity, resource utilization, and the usage type (production, development, or testing).

InstanceSizingType -> (string)

The size of your target instance. Fleet Advisor calculates this value based on your data collection type, such as total capacity and resource utilization. Valid values include `"total-capacity"` and `"utilization"` .

WorkloadType -> (string)

The deployment option for your target engine. For production databases, Fleet Advisor chooses Multi-AZ deployment. For development or test databases, Fleet Advisor chooses Single-AZ deployment. Valid values include `"development"` and `"production"` .

Data -> (structure)

The recommendation of a target engine for the specified source database.

RdsEngine -> (structure)

The recommendation of a target Amazon RDS database engine.

RequirementsToTarget -> (structure)

Supplemental information about the requirements to the recommended target database on Amazon RDS.

EngineEdition -> (string)

The required target Amazon RDS engine edition.

InstanceVcpu -> (double)

The required number of virtual CPUs (vCPU) on the Amazon RDS DB instance.

InstanceMemory -> (double)

The required memory on the Amazon RDS DB instance.

StorageSize -> (integer)

The required Amazon RDS DB instance storage size.

StorageIops -> (integer)

The required number of I/O operations completed each second (IOPS) on your Amazon RDS DB instance.

DeploymentOption -> (string)

The required deployment option for the Amazon RDS DB instance. Valid values include `"MULTI_AZ"` for Multi-AZ deployments and `"SINGLE_AZ"` for Single-AZ deployments.

EngineVersion -> (string)

The required target Amazon RDS engine version.

TargetConfiguration -> (structure)

Supplemental information about the configuration of the recommended target database on Amazon RDS.

EngineEdition -> (string)

Describes the recommended target Amazon RDS engine edition.

InstanceType -> (string)

Describes the recommended target Amazon RDS instance type.

InstanceVcpu -> (double)

Describes the number of virtual CPUs (vCPU) on the recommended Amazon RDS DB instance that meets your requirements.

InstanceMemory -> (double)

Describes the memory on the recommended Amazon RDS DB instance that meets your requirements.

StorageType -> (string)

Describes the storage type of the recommended Amazon RDS DB instance that meets your requirements.

Amazon RDS provides three storage types: General Purpose SSD (also known as gp2 and gp3), Provisioned IOPS SSD (also known as io1), and magnetic (also known as standard).

StorageSize -> (integer)

Describes the storage size of the recommended Amazon RDS DB instance that meets your requirements.

StorageIops -> (integer)

Describes the number of I/O operations completed each second (IOPS) on the recommended Amazon RDS DB instance that meets your requirements.

DeploymentOption -> (string)

Describes the deployment option for the recommended Amazon RDS DB instance. The deployment options include Multi-AZ and Single-AZ deployments. Valid values include `"MULTI_AZ"` and `"SINGLE_AZ"` .

EngineVersion -> (string)

Describes the recommended target Amazon RDS engine version.