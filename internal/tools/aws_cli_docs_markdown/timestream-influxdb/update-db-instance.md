# update-db-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/update-db-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/update-db-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [timestream-influxdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/timestream-influxdb/index.html#cli-aws-timestream-influxdb) ]

# update-db-instance

## Description

Updates a Timestream for InfluxDB DB instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/timestream-influxdb-2023-01-27/UpdateDbInstance)

## Synopsis

```
update-db-instance
--identifier <value>
[--log-delivery-configuration <value>]
[--db-parameter-group-identifier <value>]
[--port <value>]
[--db-instance-type <value>]
[--deployment-type <value>]
[--db-storage-type <value>]
[--allocated-storage <value>]
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

`--identifier` (string)

The id of the DB instance.

`--log-delivery-configuration` (structure)

Configuration for sending InfluxDB engine logs to send to specified S3 bucket.

s3Configuration -> (structure)

Configuration for S3 bucket log delivery.

bucketName -> (string)

The name of the S3 bucket to deliver logs to.

enabled -> (boolean)

Indicates whether log delivery to the S3 bucket is enabled.

Shorthand Syntax:

```
s3Configuration={bucketName=string,enabled=boolean}
```

JSON Syntax:

```
{
  "s3Configuration": {
    "bucketName": "string",
    "enabled": true|false
  }
}
```

`--db-parameter-group-identifier` (string)

The id of the DB parameter group to assign to your DB instance. DB parameter groups specify how the database is configured. For example, DB parameter groups can specify the limit for query concurrency.

`--port` (integer)

The port number on which InfluxDB accepts connections.

If you change the Port value, your database restarts immediately.

Valid Values: 1024-65535

Default: 8086

Constraints: The value canât be 2375-2376, 7788-7799, 8090, or 51678-51680

`--db-instance-type` (string)

The Timestream for InfluxDB DB instance type to run InfluxDB on.

Possible values:

- `db.influx.medium`
- `db.influx.large`
- `db.influx.xlarge`
- `db.influx.2xlarge`
- `db.influx.4xlarge`
- `db.influx.8xlarge`
- `db.influx.12xlarge`
- `db.influx.16xlarge`

`--deployment-type` (string)

Specifies whether the DB instance will be deployed as a standalone instance or with a Multi-AZ standby for high availability.

Possible values:

- `SINGLE_AZ`
- `WITH_MULTIAZ_STANDBY`

`--db-storage-type` (string)

The Timestream for InfluxDB DB storage type that InfluxDB stores data on.

Possible values:

- `InfluxIOIncludedT1`
- `InfluxIOIncludedT2`
- `InfluxIOIncludedT3`

`--allocated-storage` (integer)

The amount of storage to allocate for your DB storage type (in gibibytes).

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

id -> (string)

A service-generated unique identifier.

name -> (string)

This customer-supplied name uniquely identifies the DB instance when interacting with the Amazon Timestream for InfluxDB API and CLI commands.

arn -> (string)

The Amazon Resource Name (ARN) of the DB instance.

status -> (string)

The status of the DB instance.

endpoint -> (string)

The endpoint used to connect to InfluxDB. The default InfluxDB port is 8086.

port -> (integer)

The port number on which InfluxDB accepts connections.

networkType -> (string)

Specifies whether the networkType of the Timestream for InfluxDB instance is IPV4, which can communicate over IPv4 protocol only, or DUAL, which can communicate over both IPv4 and IPv6 protocols.

dbInstanceType -> (string)

The Timestream for InfluxDB instance type that InfluxDB runs on.

dbStorageType -> (string)

The Timestream for InfluxDB DB storage type that InfluxDB stores data on.

allocatedStorage -> (integer)

The amount of storage allocated for your DB storage type (in gibibytes).

deploymentType -> (string)

Specifies whether the Timestream for InfluxDB is deployed as Single-AZ or with a MultiAZ Standby for High availability.

vpcSubnetIds -> (list)

A list of VPC subnet IDs associated with the DB instance.

(string)

publiclyAccessible -> (boolean)

Indicates if the DB instance has a public IP to facilitate access.

vpcSecurityGroupIds -> (list)

A list of VPC security group IDs associated with the DB instance.

(string)

dbParameterGroupIdentifier -> (string)

The id of the DB parameter group assigned to your DB instance.

availabilityZone -> (string)

The Availability Zone in which the DB instance resides.

secondaryAvailabilityZone -> (string)

The Availability Zone in which the standby instance is located when deploying with a MultiAZ standby instance.

logDeliveryConfiguration -> (structure)

Configuration for sending InfluxDB engine logs to send to specified S3 bucket.

s3Configuration -> (structure)

Configuration for S3 bucket log delivery.

bucketName -> (string)

The name of the S3 bucket to deliver logs to.

enabled -> (boolean)

Indicates whether log delivery to the S3 bucket is enabled.

influxAuthParametersSecretArn -> (string)

The Amazon Resource Name (ARN) of the Secrets Manager secret containing the initial InfluxDB authorization parameters. The secret value is a JSON formatted key-value pair holding InfluxDB authorization values: organization, bucket, username, and password.

dbClusterId -> (string)

Specifies the DbCluster to which this DbInstance belongs to.

instanceMode -> (string)

Specifies the DbInstanceâs role in the cluster.