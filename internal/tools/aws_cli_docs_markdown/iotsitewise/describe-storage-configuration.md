# describe-storage-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-storage-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-storage-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# describe-storage-configuration

## Description

Retrieves information about the storage configuration for IoT SiteWise.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/DescribeStorageConfiguration)

## Synopsis

```
describe-storage-configuration
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

storageType -> (string)

The storage tier that you specified for your data. The `storageType` parameter can be one of the following values:

- `SITEWISE_DEFAULT_STORAGE` â IoT SiteWise saves your data into the hot tier. The hot tier is a service-managed database.
- `MULTI_LAYER_STORAGE` â IoT SiteWise saves your data in both the cold tier and the hot tier. The cold tier is a customer-managed Amazon S3 bucket.

multiLayerStorage -> (structure)

Contains information about the storage destination.

customerManagedS3Storage -> (structure)

Contains information about a customer managed Amazon S3 bucket.

s3ResourceArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon S3 object. For more information about how to find the ARN for an Amazon S3 object, see [Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-arn-format.html) in the *Amazon Simple Storage Service User Guide* .

roleArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Identity and Access Management role that allows IoT SiteWise to send data to Amazon S3.

disassociatedDataStorage -> (string)

Contains the storage configuration for time series (data streams) that arenât associated with asset properties. The `disassociatedDataStorage` can be one of the following values:

- `ENABLED` â IoT SiteWise accepts time series that arenât associated with asset properties.

### Warning

After the `disassociatedDataStorage` is enabled, you canât disable it.

- `DISABLED` â IoT SiteWise doesnât accept time series (data streams) that arenât associated with asset properties.

For more information, see [Data streams](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html) in the *IoT SiteWise User Guide* .

retentionPeriod -> (structure)

The number of days your data is kept in the hot tier. By default, your data is kept indefinitely in the hot tier.

numberOfDays -> (integer)

The number of days that your data is kept.

### Note

If you specified a value for this parameter, the `unlimited` parameter must be `false` .

unlimited -> (boolean)

If true, your data is kept indefinitely.

### Note

If configured to `true` , you must not specify a value for the `numberOfDays` parameter.

configurationStatus -> (structure)

Contains current status information for the configuration.

state -> (string)

The current state of the configuration.

error -> (structure)

Contains associated error information, if any.

code -> (string)

The error code.

message -> (string)

The error message.

lastUpdateDate -> (timestamp)

The date the storage configuration was last updated, in Unix epoch time.

warmTier -> (string)

A service managed storage tier optimized for analytical queries. It stores periodically uploaded, buffered and historical data ingested with the CreaeBulkImportJob API.

warmTierRetentionPeriod -> (structure)

Set this period to specify how long your data is stored in the warm tier before it is deleted. You can set this only if cold tier is enabled.

numberOfDays -> (integer)

The number of days the data is stored in the warm tier.

unlimited -> (boolean)

If set to true, the data is stored indefinitely in the warm tier.

disallowIngestNullNaN -> (boolean)

Describes the configuration for ingesting NULL and NaN data. By default the feature is allowed. The feature is disallowed if the value is `true` .