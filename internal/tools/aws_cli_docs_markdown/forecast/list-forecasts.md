# list-forecastsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-forecasts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/list-forecasts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [forecast](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/forecast/index.html#cli-aws-forecast) ]

# list-forecasts

## Description

Returns a list of forecasts created using the  CreateForecast operation. For each forecast, this operation returns a summary of its properties, including its Amazon Resource Name (ARN). To retrieve the complete set of properties, specify the ARN with the  DescribeForecast operation. You can filter the list using an array of  Filter objects.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/forecast-2018-06-26/ListForecasts)

`list-forecasts` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Forecasts`

## Synopsis

```
list-forecasts
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

`--filters` (list)

An array of filters. For each filter, you provide a condition and a match statement. The condition is either `IS` or `IS_NOT` , which specifies whether to include or exclude the forecasts that match the statement from the list, respectively. The match statement consists of a key and a value.

**Filter properties**

- `Condition` - The condition to apply. Valid values are `IS` and `IS_NOT` . To include the forecasts that match the statement, specify `IS` . To exclude matching forecasts, specify `IS_NOT` .
- `Key` - The name of the parameter to filter on. Valid values are `DatasetGroupArn` , `PredictorArn` , and `Status` .
- `Value` - The value to match.

For example, to list all forecasts whose status is not ACTIVE, you would specify:

`"Filters": [ { "Condition": "IS_NOT", "Key": "Status", "Value": "ACTIVE" } ]`

(structure)

Describes a filter for choosing a subset of objects. Each filter consists of a condition and a match statement. The condition is either `IS` or `IS_NOT` , which specifies whether to include or exclude the objects that match the statement, respectively. The match statement consists of a key and a value.

Key -> (string)

The name of the parameter to filter on.

Value -> (string)

The value to match.

Condition -> (string)

The condition to apply. To include the objects that match the statement, specify `IS` . To exclude matching objects, specify `IS_NOT` .

Shorthand Syntax:

```
Key=string,Value=string,Condition=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string",
    "Condition": "IS"|"IS_NOT"
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

Forecasts -> (list)

An array of objects that summarize each forecastâs properties.

(structure)

Provides a summary of the forecast properties used in the  ListForecasts operation. To get the complete set of properties, call the  DescribeForecast operation, and provide the `ForecastArn` that is listed in the summary.

ForecastArn -> (string)

The ARN of the forecast.

ForecastName -> (string)

The name of the forecast.

PredictorArn -> (string)

The ARN of the predictor used to generate the forecast.

CreatedUsingAutoPredictor -> (boolean)

Whether the Forecast was created from an AutoPredictor.

DatasetGroupArn -> (string)

The Amazon Resource Name (ARN) of the dataset group that provided the data used to train the predictor.

Status -> (string)

The status of the forecast. States include:

- `ACTIVE`
- `CREATE_PENDING` , `CREATE_IN_PROGRESS` , `CREATE_FAILED`
- `CREATE_STOPPING` , `CREATE_STOPPED`
- `DELETE_PENDING` , `DELETE_IN_PROGRESS` , `DELETE_FAILED`

### Note

The `Status` of the forecast must be `ACTIVE` before you can query or export the forecast.

Message -> (string)

If an error occurred, an informational message about the error.

CreationTime -> (timestamp)

When the forecast creation task was created.

LastModificationTime -> (timestamp)

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime` .
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or failed.

NextToken -> (string)

If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.