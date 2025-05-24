# list-test-setsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-test-sets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/list-test-sets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lexv2-models](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lexv2-models/index.html#cli-aws-lexv2-models) ]

# list-test-sets

## Description

The list of the test sets

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/models.lex.v2-2020-08-07/ListTestSets)

## Synopsis

```
list-test-sets
[--sort-by <value>]
[--max-results <value>]
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

`--sort-by` (structure)

The sort order for the list of test sets.

attribute -> (string)

Specifies whether to sort the test sets by name or by the time they were last updated.

order -> (string)

Specifies whether to sort in ascending or descending order.

Shorthand Syntax:

```
attribute=string,order=string
```

JSON Syntax:

```
{
  "attribute": "TestSetName"|"LastUpdatedDateTime",
  "order": "Ascending"|"Descending"
}
```

`--max-results` (integer)

The maximum number of test sets to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.

`--next-token` (string)

If the response from the ListTestSets operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.

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

testSets -> (list)

The selected test sets in a list of test sets.

(structure)

Contains summary information about the test set.

testSetId -> (string)

The unique identifier of the test set.

testSetName -> (string)

The name of the test set.

description -> (string)

The description of the test set.

modality -> (string)

Specifies whether the test set contains written or spoken data.

status -> (string)

The status of the test set.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that has permission to access the test set.

numTurns -> (integer)

The number of turns in the test set.

storageLocation -> (structure)

Contains information about the location at which the test set is stored.

s3BucketName -> (string)

The name of the Amazon S3 bucket in which the test set is stored.

s3Path -> (string)

The path inside the Amazon S3 bucket where the test set is stored.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting the test set.

creationDateTime -> (timestamp)

The date and time at which the test set was created.

lastUpdatedDateTime -> (timestamp)

The date and time at which the test set was last updated.

nextToken -> (string)

A token that indicates whether there are more results to return in a response to the ListTestSets operation. If the nextToken field is present, you send the contents as the nextToken parameter of a ListTestSets operation request to get the next page of results.