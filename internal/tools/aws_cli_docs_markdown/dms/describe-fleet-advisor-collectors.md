# describe-fleet-advisor-collectorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-fleet-advisor-collectors.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-fleet-advisor-collectors.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# describe-fleet-advisor-collectors

## Description

Returns a list of the Fleet Advisor collectors in your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeFleetAdvisorCollectors)

## Synopsis

```
describe-fleet-advisor-collectors
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

If you specify any of the following filters, the output includes information for only those collectors that meet the filter criteria:

- `collector-referenced-id` â The ID of the collector agent, for example `d4610ac5-e323-4ad9-bc50-eaf7249dfe9d` .
- `collector-name` â The name of the collector agent.

An example is: `describe-fleet-advisor-collectors --filter Name="collector-referenced-id",Values="d4610ac5-e323-4ad9-bc50-eaf7249dfe9d"`

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

Sets the maximum number of records returned in the response.

`--next-token` (string)

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

Collectors -> (list)

Provides descriptions of the Fleet Advisor collectors, including the collectorsâ name and ID, and the latest inventory data.

(structure)

Describes a Fleet Advisor collector.

CollectorReferencedId -> (string)

The reference ID of the Fleet Advisor collector.

CollectorName -> (string)

The name of the Fleet Advisor collector .

CollectorVersion -> (string)

The version of your Fleet Advisor collector, in semantic versioning format, for example `1.0.2`

VersionStatus -> (string)

Whether the collector version is up to date.

Description -> (string)

A summary description of the Fleet Advisor collector.

S3BucketName -> (string)

The Amazon S3 bucket that the Fleet Advisor collector uses to store inventory metadata.

ServiceAccessRoleArn -> (string)

The IAM role that grants permissions to access the specified Amazon S3 bucket.

CollectorHealthCheck -> (structure)

Describes the last Fleet Advisor collector health check.

CollectorStatus -> (string)

The status of the Fleet Advisor collector.

LocalCollectorS3Access -> (boolean)

Whether the local collector can access its Amazon S3 bucket.

WebCollectorS3Access -> (boolean)

Whether the web collector can access its Amazon S3 bucket.

WebCollectorGrantedRoleBasedAccess -> (boolean)

Whether the role that you provided when creating the Fleet Advisor collector has sufficient permissions to access the Fleet Advisor web collector.

LastDataReceived -> (string)

The timestamp of the last time the collector received data, in the following format: `2022-01-24T19:04:02.596113Z`

RegisteredDate -> (string)

The timestamp when DMS registered the collector, in the following format: `2022-01-24T19:04:02.596113Z`

CreatedDate -> (string)

The timestamp when you created the collector, in the following format: `2022-01-24T19:04:02.596113Z`

ModifiedDate -> (string)

The timestamp when DMS last modified the collector, in the following format: `2022-01-24T19:04:02.596113Z`

InventoryData -> (structure)

Describes a Fleet Advisor collector inventory.

NumberOfDatabases -> (integer)

The number of databases in the Fleet Advisor collector inventory.

NumberOfSchemas -> (integer)

The number of schemas in the Fleet Advisor collector inventory.

NextToken -> (string)

If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.