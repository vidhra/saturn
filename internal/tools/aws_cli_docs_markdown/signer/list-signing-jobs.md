# list-signing-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [signer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/index.html#cli-aws-signer) ]

# list-signing-jobs

## Description

Lists all your signing jobs. You can use the `maxResults` parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, AWS Signer returns a `nextToken` value. Use this value in subsequent calls to `ListSigningJobs` to fetch the remaining values. You can continue calling `ListSigningJobs` with your `maxResults` parameter and with new values that Signer returns in the `nextToken` parameter until all of your signing jobs have been returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/ListSigningJobs)

`list-signing-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `jobs`

## Synopsis

```
list-signing-jobs
[--status <value>]
[--platform-id <value>]
[--requested-by <value>]
[--is-revoked | --no-is-revoked]
[--signature-expires-before <value>]
[--signature-expires-after <value>]
[--job-invoker <value>]
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

`--status` (string)

A status value with which to filter your results.

Possible values:

- `InProgress`
- `Failed`
- `Succeeded`

`--platform-id` (string)

The ID of microcontroller platform that you specified for the distribution of your code image.

`--requested-by` (string)

The IAM principal that requested the signing job.

`--is-revoked` | `--no-is-revoked` (boolean)

Filters results to return only signing jobs with revoked signatures.

`--signature-expires-before` (timestamp)

Filters results to return only signing jobs with signatures expiring before a specified timestamp.

`--signature-expires-after` (timestamp)

Filters results to return only signing jobs with signatures expiring after a specified timestamp.

`--job-invoker` (string)

Filters results to return only signing jobs initiated by a specified IAM entity.

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

**To list all signing jobs**

The following `list-signing-jobs` example displays details about all signing jobs for the account.

```
aws signer list-signing-jobs
```

In this example, two jobs are returned, one successful, and one failed.

```
{
    "jobs": [
        {
            "status": "Succeeded",
            "signingMaterial": {
                "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc"
            },
            "jobId": "2065c468-73e2-4385-a6c9-0123456789abc",
            "source": {
                "s3": {
                    "version": "PNyFaUTgsQh5ZdMCcoCe6pT1gOpgB_M4",
                    "bucketName": "signer-source",
                    "key": "MyCode.rb"
                }
            },
            "signedObject": {
                "s3": {
                    "bucketName": "signer-destination",
                    "key": "signed-2065c468-73e2-4385-a6c9-0123456789abc"
                }
            },
            "createdAt": 1568412036
        },
        {
            "status": "Failed",
            "source": {
                "s3": {
                    "version": "PNyFaUTgsQh5ZdMCcoCe6pT1gOpgB_M4",
                    "bucketName": "signer-source",
                    "key": "MyOtherCode.rb"
                }
            },
            "signingMaterial": {
                "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc"
            },
            "createdAt": 1568402690,
            "jobId": "74d9825e-22fc-4a0d-b962-0123456789abc"
        }
    ]
}
```

## Output

jobs -> (list)

A list of your signing jobs.

(structure)

Contains information about a signing job.

jobId -> (string)

The ID of the signing job.

source -> (structure)

A `Source` that contains information about a signing jobâs code image source.

s3 -> (structure)

The `S3Source` object.

bucketName -> (string)

Name of the S3 bucket.

key -> (string)

Key name of the bucket object that contains your unsigned code.

version -> (string)

Version of your source image in your version enabled S3 bucket.

signedObject -> (structure)

A `SignedObject` structure that contains information about a signing jobâs signed code image.

s3 -> (structure)

The `S3SignedObject` .

bucketName -> (string)

Name of the S3 bucket.

key -> (string)

Key name that uniquely identifies a signed code image in your bucket.

signingMaterial -> (structure)

A `SigningMaterial` object that contains the Amazon Resource Name (ARN) of the certificate used for the signing job.

certificateArn -> (string)

The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

createdAt -> (timestamp)

The date and time that the signing job was created.

status -> (string)

The status of the signing job.

isRevoked -> (boolean)

Indicates whether the signing job is revoked.

profileName -> (string)

The name of the signing profile that created a signing job.

profileVersion -> (string)

The version of the signing profile that created a signing job.

platformId -> (string)

The unique identifier for a signing platform.

platformDisplayName -> (string)

The name of a signing platform.

signatureExpiresAt -> (timestamp)

The time when the signature of a signing job expires.

jobOwner -> (string)

The AWS account ID of the job owner.

jobInvoker -> (string)

The AWS account ID of the job invoker.

nextToken -> (string)

String for specifying the next set of paginated results.