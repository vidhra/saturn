# list-read-setsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-sets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-sets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# list-read-sets

## Description

Retrieves a list of read sets.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/ListReadSets)

`list-read-sets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `readSets`

## Synopsis

```
list-read-sets
--sequence-store-id <value>
[--filter <value>]
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

`--sequence-store-id` (string)

The jobsâ sequence store ID.

`--filter` (structure)

A filter to apply to the list.

name -> (string)

A name to filter on.

status -> (string)

A status to filter on.

referenceArn -> (string)

A genome reference ARN to filter on.

createdAfter -> (timestamp)

The filterâs start date.

createdBefore -> (timestamp)

The filterâs end date.

sampleId -> (string)

The read set sourceâs sample ID.

subjectId -> (string)

The read set sourceâs subject ID.

generatedFrom -> (string)

Where the source originated.

creationType -> (string)

The creation type of the read set.

Shorthand Syntax:

```
name=string,status=string,referenceArn=string,createdAfter=timestamp,createdBefore=timestamp,sampleId=string,subjectId=string,generatedFrom=string,creationType=string
```

JSON Syntax:

```
{
  "name": "string",
  "status": "ARCHIVED"|"ACTIVATING"|"ACTIVE"|"DELETING"|"DELETED"|"PROCESSING_UPLOAD"|"UPLOAD_FAILED",
  "referenceArn": "string",
  "createdAfter": timestamp,
  "createdBefore": timestamp,
  "sampleId": "string",
  "subjectId": "string",
  "generatedFrom": "string",
  "creationType": "IMPORT"|"UPLOAD"
}
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

**To get a list of read sets**

The following `list-read-sets` example gets a list of read sets for a sequence store with id `1234567890`.

```
aws omics list-read-sets \
    --sequence-store-id 1234567890
```

Output:

```
{
    "readSets": [
        {
            "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890/readSet/1234567890",
            "creationTime": "2022-11-23T21:55:00.515Z",
            "fileType": "FASTQ",
            "id": "1234567890",
            "name": "HG00146",
            "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890",
            "sampleId": "fastq-sample",
            "sequenceStoreId": "1234567890",
            "status": "ACTIVE",
            "subjectId": "fastq-subject"
        }
    ]
}
```

For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html) in the *Amazon Omics Developer Guide*.

## Output

nextToken -> (string)

A pagination token thatâs included if more results are available.

readSets -> (list)

A list of read sets.

(structure)

A read set.

id -> (string)

The read setâs ID.

arn -> (string)

The read setâs ARN.

sequenceStoreId -> (string)

The read setâs sequence store ID.

subjectId -> (string)

The read setâs subject ID.

sampleId -> (string)

The read setâs sample ID.

status -> (string)

The read setâs status.

name -> (string)

The read setâs name.

description -> (string)

The read setâs description.

referenceArn -> (string)

The read setâs genome reference ARN.

fileType -> (string)

The read setâs file type.

sequenceInformation -> (structure)

Details about a sequence.

totalReadCount -> (long)

The sequenceâs total read count.

totalBaseCount -> (long)

The sequenceâs total base count.

generatedFrom -> (string)

Where the sequence originated.

alignment -> (string)

The sequenceâs alignment setting.

creationTime -> (timestamp)

When the read set was created.

statusMessage -> (string)

The status for a read set. It provides more detail as to why the read set has a status.

creationType -> (string)

The creation type of the read set.

etag -> (structure)

The entity tag (ETag) is a hash of the object representing its semantic content.

algorithm -> (string)

The algorithm used to calculate the read setâs ETag(s).

source1 -> (string)

The ETag hash calculated on Source1 of the read set.

source2 -> (string)

The ETag hash calculated on Source2 of the read set.