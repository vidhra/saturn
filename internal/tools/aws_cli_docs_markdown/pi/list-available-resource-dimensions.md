# list-available-resource-dimensionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-available-resource-dimensions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/list-available-resource-dimensions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pi/index.html#cli-aws-pi) ]

# list-available-resource-dimensions

## Description

Retrieve the dimensions that can be queried for each specified metric type on a specified DB instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pi-2018-02-27/ListAvailableResourceDimensions)

## Synopsis

```
list-available-resource-dimensions
--service-type <value>
--identifier <value>
--metrics <value>
[--max-results <value>]
[--next-token <value>]
[--authorized-actions <value>]
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

`--service-type` (string)

The Amazon Web Services service for which Performance Insights returns metrics.

Possible values:

- `RDS`
- `DOCDB`

`--identifier` (string)

An immutable identifier for a data source that is unique within an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its `DbiResourceId` value. For example, specify `db-ABCDEFGHIJKLMNOPQRSTU1VWZ` .

`--metrics` (list)

The types of metrics for which to retrieve dimensions. Valid values include `db.load` .

(string)

A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections.

Syntax:

```
"string" "string" ...
```

`--max-results` (integer)

The maximum number of items to return in the response. If more items exist than the specified `MaxRecords` value, a pagination token is included in the response so that the remaining results can be retrieved.

`--next-token` (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords` .

`--authorized-actions` (list)

The actions to discover the dimensions you are authorized to access. If you specify multiple actions, then the response will contain the dimensions common for all the actions.

When you donât specify this request parameter or provide an empty list, the response contains all the available dimensions for the target database engine whether or not you are authorized to access them.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  DescribeDimensionKeys
  GetDimensionKeyDetails
  GetResourceMetrics
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

## Output

MetricDimensions -> (list)

The dimension information returned for requested metric types.

(structure)

The available dimension information for a metric type.

Metric -> (string)

The metric type to which the dimension information belongs.

Groups -> (list)

The available dimension groups for a metric type.

(structure)

Information about dimensions within a dimension group.

Group -> (string)

The name of the dimension group.

Dimensions -> (list)

The dimensions within a dimension group.

(structure)

The information about a dimension.

Identifier -> (string)

The identifier of a dimension.

NextToken -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by `MaxRecords` .