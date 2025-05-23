# describe-orderable-db-instance-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-orderable-db-instance-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-orderable-db-instance-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-orderable-db-instance-options

## Description

Describes the orderable DB instance options for a specified DB engine.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeOrderableDBInstanceOptions)

`describe-orderable-db-instance-options` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `OrderableDBInstanceOptions`

## Synopsis

```
describe-orderable-db-instance-options
--engine <value>
[--engine-version <value>]
[--db-instance-class <value>]
[--license-model <value>]
[--availability-zone-group <value>]
[--vpc | --no-vpc]
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

`--engine` (string)

The name of the database engine to describe DB instance options for.

Valid Values:

- `aurora-mysql`
- `aurora-postgresql`
- `custom-oracle-ee`
- `custom-oracle-ee-cdb`
- `custom-oracle-se2`
- `custom-oracle-se2-cdb`
- `db2-ae`
- `db2-se`
- `mariadb`
- `mysql`
- `oracle-ee`
- `oracle-ee-cdb`
- `oracle-se2`
- `oracle-se2-cdb`
- `postgres`
- `sqlserver-ee`
- `sqlserver-se`
- `sqlserver-ex`
- `sqlserver-web`

`--engine-version` (string)

A filter to include only the available options for the specified engine version.

`--db-instance-class` (string)

A filter to include only the available options for the specified DB instance class.

`--license-model` (string)

A filter to include only the available options for the specified license model.

RDS Custom supports only the BYOL licensing model.

`--availability-zone-group` (string)

The Availability Zone group associated with a Local Zone. Specify this parameter to retrieve available options for the Local Zones in the group.

Omit this parameter to show the available options in the specified Amazon Web Services Region.

This setting doesnât apply to RDS Custom DB instances.

`--vpc` | `--no-vpc` (boolean)

Specifies whether to show only VPC or non-VPC offerings. RDS Custom supports only VPC offerings.

RDS Custom supports only VPC offerings. If you describe non-VPC offerings for RDS Custom, the output shows VPC offerings.

`--filters` (list)

This parameter isnât currently supported.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.

### Note

Currently, wildcards are not supported in filters.

The following actions can be filtered:

- `DescribeDBClusterBacktracks`
- `DescribeDBClusterEndpoints`
- `DescribeDBClusters`
- `DescribeDBInstances`
- `DescribeDBRecommendations`
- `DescribeDBShardGroups`
- `DescribePendingMaintenanceActions`

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

One or more filter values. Filter values are case-sensitive.

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

**To describe orderable DB instance options**

The following `describe-orderable-db-instance-options` example retrieves details about the orderable options for a DB instances running the MySQL DB engine.

```
aws rds describe-orderable-db-instance-options \
    --engine mysql
```

Output:

```
{
    "OrderableDBInstanceOptions": [
        {
            "MinStorageSize": 5,
            "ReadReplicaCapable": true,
            "MaxStorageSize": 6144,
            "AvailabilityZones": [
                {
                    "Name": "us-east-1a"
                },
                {
                    "Name": "us-east-1b"
                },
                {
                    "Name": "us-east-1c"
                },
                {
                    "Name": "us-east-1d"
                }
            ],
            "SupportsIops": false,
            "AvailableProcessorFeatures": [],
            "MultiAZCapable": true,
            "DBInstanceClass": "db.m1.large",
            "Vpc": true,
            "StorageType": "gp2",
            "LicenseModel": "general-public-license",
            "EngineVersion": "5.5.46",
            "SupportsStorageEncryption": false,
            "SupportsEnhancedMonitoring": true,
            "Engine": "mysql",
            "SupportsIAMDatabaseAuthentication": false,
            "SupportsPerformanceInsights": false
        }
    ]
    ...some output truncated...
}
```

## Output

OrderableDBInstanceOptions -> (list)

An `OrderableDBInstanceOption` structure containing information about orderable options for the DB instance.

(structure)

Contains a list of available options for a DB instance.

This data type is used as a response element in the `DescribeOrderableDBInstanceOptions` action.

Engine -> (string)

The engine type of a DB instance.

EngineVersion -> (string)

The engine version of a DB instance.

DBInstanceClass -> (string)

The DB instance class for a DB instance.

LicenseModel -> (string)

The license model for a DB instance.

AvailabilityZoneGroup -> (string)

The Availability Zone group for a DB instance.

AvailabilityZones -> (list)

A list of Availability Zones for a DB instance.

(structure)

Contains Availability Zone information.

This data type is used as an element in the `OrderableDBInstanceOption` data type.

Name -> (string)

The name of the Availability Zone.

MultiAZCapable -> (boolean)

Indicates whether a DB instance is Multi-AZ capable.

ReadReplicaCapable -> (boolean)

Indicates whether a DB instance can have a read replica.

Vpc -> (boolean)

Indicates whether a DB instance is in a VPC.

SupportsStorageEncryption -> (boolean)

Indicates whether a DB instance supports encrypted storage.

StorageType -> (string)

The storage type for a DB instance.

SupportsIops -> (boolean)

Indicates whether a DB instance supports provisioned IOPS.

SupportsEnhancedMonitoring -> (boolean)

Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.

SupportsIAMDatabaseAuthentication -> (boolean)

Indicates whether a DB instance supports IAM database authentication.

SupportsPerformanceInsights -> (boolean)

Indicates whether a DB instance supports Performance Insights.

MinStorageSize -> (integer)

Minimum storage size for a DB instance.

MaxStorageSize -> (integer)

Maximum storage size for a DB instance.

MinIopsPerDbInstance -> (integer)

Minimum total provisioned IOPS for a DB instance.

MaxIopsPerDbInstance -> (integer)

Maximum total provisioned IOPS for a DB instance.

MinIopsPerGib -> (double)

Minimum provisioned IOPS per GiB for a DB instance.

MaxIopsPerGib -> (double)

Maximum provisioned IOPS per GiB for a DB instance.

AvailableProcessorFeatures -> (list)

A list of the available processor features for the DB instance class of a DB instance.

(structure)

Contains the available processor feature information for the DB instance class of a DB instance.

For more information, see [Configuring the Processor of the DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html#USER_ConfigureProcessor) in the *Amazon RDS User Guide.*

Name -> (string)

The name of the processor feature. Valid names are `coreCount` and `threadsPerCore` .

DefaultValue -> (string)

The default value for the processor feature of the DB instance class.

AllowedValues -> (string)

The allowed values for the processor feature of the DB instance class.

SupportedEngineModes -> (list)

A list of the supported DB engine modes.

(string)

SupportsStorageAutoscaling -> (boolean)

Indicates whether Amazon RDS can automatically scale storage for DB instances that use the specified DB instance class.

SupportsKerberosAuthentication -> (boolean)

Indicates whether a DB instance supports Kerberos Authentication.

OutpostCapable -> (boolean)

Indicates whether a DB instance supports RDS on Outposts.

For more information about RDS on Outposts, see [Amazon RDS on Amazon Web Services Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html) in the *Amazon RDS User Guide.*

SupportedActivityStreamModes -> (list)

The list of supported modes for Database Activity Streams. Aurora PostgreSQL returns the value `[sync, async]` . Aurora MySQL and RDS for Oracle return `[async]` only. If Database Activity Streams isnât supported, the return value is an empty list.

(string)

SupportsGlobalDatabases -> (boolean)

Indicates whether you can use Aurora global databases with a specific combination of other DB engine attributes.

SupportsClusters -> (boolean)

Indicates whether DB instances can be configured as a Multi-AZ DB cluster.

For more information on Multi-AZ DB clusters, see [Multi-AZ deployments with two readable standby DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.*

SupportedNetworkTypes -> (list)

The network types supported by the DB instance (`IPV4` or `DUAL` ).

A DB instance can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (`DUAL` ).

For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) in the *Amazon RDS User Guide.*

(string)

SupportsStorageThroughput -> (boolean)

Indicates whether a DB instance supports storage throughput.

MinStorageThroughputPerDbInstance -> (integer)

Minimum storage throughput for a DB instance.

MaxStorageThroughputPerDbInstance -> (integer)

Maximum storage throughput for a DB instance.

MinStorageThroughputPerIops -> (double)

Minimum storage throughput to provisioned IOPS ratio for a DB instance.

MaxStorageThroughputPerIops -> (double)

Maximum storage throughput to provisioned IOPS ratio for a DB instance.

SupportsDedicatedLogVolume -> (boolean)

Indicates whether a DB instance supports using a dedicated log volume (DLV).

Marker -> (string)

An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .