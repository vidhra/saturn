# describe-orderable-db-instance-optionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-orderable-db-instance-options.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-orderable-db-instance-options.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/index.html#cli-aws-neptune) ]

# describe-orderable-db-instance-options

## Description

Returns a list of orderable DB instance options for the specified engine.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeOrderableDBInstanceOptions)

`describe-orderable-db-instance-options` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `OrderableDBInstanceOptions`

## Synopsis

```
describe-orderable-db-instance-options
--engine <value>
[--engine-version <value>]
[--db-instance-class <value>]
[--license-model <value>]
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

The name of the engine to retrieve DB instance options for.

`--engine-version` (string)

The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.

`--db-instance-class` (string)

The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.

`--license-model` (string)

The license model filter value. Specify this parameter to show only the available offerings matching the specified license model.

`--vpc` | `--no-vpc` (boolean)

The VPC filter value. Specify this parameter to show only the available VPC or non-VPC offerings.

`--filters` (list)

This parameter is not currently supported.

(structure)

This type is not currently supported.

Name -> (string)

This parameter is not currently supported.

Values -> (list)

This parameter is not currently supported.

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

## Output

OrderableDBInstanceOptions -> (list)

An  OrderableDBInstanceOption structure containing information about orderable options for the DB instance.

(structure)

Contains a list of available options for a DB instance.

This data type is used as a response element in the  DescribeOrderableDBInstanceOptions action.

Engine -> (string)

The engine type of a DB instance.

EngineVersion -> (string)

The engine version of a DB instance.

DBInstanceClass -> (string)

The DB instance class for a DB instance.

LicenseModel -> (string)

The license model for a DB instance.

AvailabilityZones -> (list)

A list of Availability Zones for a DB instance.

(structure)

Specifies an Availability Zone.

Name -> (string)

The name of the availability zone.

MultiAZCapable -> (boolean)

Indicates whether a DB instance is Multi-AZ capable.

ReadReplicaCapable -> (boolean)

Indicates whether a DB instance can have a Read Replica.

Vpc -> (boolean)

Indicates whether a DB instance is in a VPC.

SupportsStorageEncryption -> (boolean)

Indicates whether a DB instance supports encrypted storage.

StorageType -> (string)

Not applicable. In Neptune the storage type is managed at the DB Cluster level.

SupportsIops -> (boolean)

Indicates whether a DB instance supports provisioned IOPS.

SupportsEnhancedMonitoring -> (boolean)

Indicates whether a DB instance supports Enhanced Monitoring at intervals from 1 to 60 seconds.

SupportsIAMDatabaseAuthentication -> (boolean)

Indicates whether a DB instance supports IAM database authentication.

SupportsPerformanceInsights -> (boolean)

*(Not supported by Neptune)*

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

SupportsGlobalDatabases -> (boolean)

A value that indicates whether you can use Neptune global databases with a specific combination of other DB engine attributes.

Marker -> (string)

An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .