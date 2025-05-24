# list-image-scan-finding-aggregationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-scan-finding-aggregations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-scan-finding-aggregations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [imagebuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/index.html#cli-aws-imagebuilder) ]

# list-image-scan-finding-aggregations

## Description

Returns a list of image scan aggregations for your account. You can filter by the type of key that Image Builder uses to group results. For example, if you want to get a list of findings by severity level for one of your pipelines, you might specify your pipeline with the `imagePipelineArn` filter. If you donât specify a filter, Image Builder returns an aggregation for your account.

To streamline results, you can use the following filters in your request:

- `accountId`
- `imageBuildVersionArn`
- `imagePipelineArn`
- `vulnerabilityId`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/imagebuilder-2019-12-02/ListImageScanFindingAggregations)

## Synopsis

```
list-image-scan-finding-aggregations
[--filter <value>]
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

`--filter` (structure)

A filter name and value pair that is used to return a more specific list of results from a list operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

name -> (string)

The name of the filter. Filter names are case-sensitive.

values -> (list)

The filter values. Filter values are case-sensitive.

(string)

Shorthand Syntax:

```
name=string,values=string,string
```

JSON Syntax:

```
{
  "name": "string",
  "values": ["string", ...]
}
```

`--next-token` (string)

A token to specify where to start paginating. This is the nextToken from a previously truncated response.

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

requestId -> (string)

The request ID that uniquely identifies this request.

aggregationType -> (string)

The aggregation type specifies what type of key is used to group the image scan findings. Image Builder returns results based on the request filter. If you didnât specify a filter in the request, the type defaults to `accountId` .

**Aggregation types**

- accountId
- imageBuildVersionArn
- imagePipelineArn
- vulnerabilityId

Each aggregation includes counts by severity level for medium severity and higher level findings, plus a total for all of the findings for each key value.

responses -> (list)

An array of image scan finding aggregations that match the filter criteria.

(structure)

This returns exactly one type of aggregation, based on the filter that Image Builder applies in its API action.

accountAggregation -> (structure)

Returns an object that contains severity counts based on an account ID.

accountId -> (string)

Identifies the account that owns the aggregated resource findings.

severityCounts -> (structure)

Counts by severity level for medium severity and higher level findings, plus a total for all of the findings.

all -> (long)

The total number of findings across all severity levels for the specified filter.

critical -> (long)

The number of critical severity findings for the specified filter.

high -> (long)

The number of high severity findings for the specified filter.

medium -> (long)

The number of medium severity findings for the specified filter.

imageAggregation -> (structure)

Returns an object that contains severity counts based on the Amazon Resource Name (ARN) for a specific image.

imageBuildVersionArn -> (string)

The Amazon Resource Name (ARN) that identifies the image for this aggregation.

severityCounts -> (structure)

Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified image.

all -> (long)

The total number of findings across all severity levels for the specified filter.

critical -> (long)

The number of critical severity findings for the specified filter.

high -> (long)

The number of high severity findings for the specified filter.

medium -> (long)

The number of medium severity findings for the specified filter.

imagePipelineAggregation -> (structure)

Returns an object that contains severity counts based on an image pipeline ARN.

imagePipelineArn -> (string)

The Amazon Resource Name (ARN) that identifies the image pipeline for this aggregation.

severityCounts -> (structure)

Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified image pipeline.

all -> (long)

The total number of findings across all severity levels for the specified filter.

critical -> (long)

The number of critical severity findings for the specified filter.

high -> (long)

The number of high severity findings for the specified filter.

medium -> (long)

The number of medium severity findings for the specified filter.

vulnerabilityIdAggregation -> (structure)

Returns an object that contains severity counts based on vulnerability ID.

vulnerabilityId -> (string)

The vulnerability Id for this set of counts.

severityCounts -> (structure)

Counts by severity level for medium severity and higher level findings, plus a total for all of the findings for the specified vulnerability.

all -> (long)

The total number of findings across all severity levels for the specified filter.

critical -> (long)

The number of critical severity findings for the specified filter.

high -> (long)

The number of high severity findings for the specified filter.

medium -> (long)

The number of medium severity findings for the specified filter.

nextToken -> (string)

The next token used for paginated responses. When this field isnât empty, there are additional elements that the service hasnât included in this request. Use this token with the next request to retrieve additional objects.