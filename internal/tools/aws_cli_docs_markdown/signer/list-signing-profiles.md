# list-signing-profilesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-profiles.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-profiles.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [signer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/index.html#cli-aws-signer) ]

# list-signing-profiles

## Description

Lists all available signing profiles in your AWS account. Returns only profiles with an `ACTIVE` status unless the `includeCanceled` request field is set to `true` . If additional jobs remain to be listed, AWS Signer returns a `nextToken` value. Use this value in subsequent calls to `ListSigningJobs` to fetch the remaining values. You can continue calling `ListSigningJobs` with your `maxResults` parameter and with new values that Signer returns in the `nextToken` parameter until all of your signing jobs have been returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/ListSigningProfiles)

`list-signing-profiles` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `profiles`

## Synopsis

```
list-signing-profiles
[--include-canceled | --no-include-canceled]
[--platform-id <value>]
[--statuses <value>]
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

`--include-canceled` | `--no-include-canceled` (boolean)

Designates whether to include profiles with the status of `CANCELED` .

`--platform-id` (string)

Filters results to return only signing jobs initiated for a specified signing platform.

`--statuses` (list)

Filters results to return only signing jobs with statuses in the specified list.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Active
  Canceled
  Revoked
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

**To list all signing profiles**

The following `list-signing-profiles` example displays details about all signing profiles for the account.

```
aws signer list-signing-profiles
```

Output:

```
{
    "profiles": [
        {
            "platformId": "AmazonFreeRTOS-TI-CC3220SF",
            "profileName": "MyProfile4",
            "status": "Active",
            "signingMaterial": {
                "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc"
            }
        },
        {
            "platformId": "AWSIoTDeviceManagement-SHA256-ECDSA",
            "profileName": "MyProfile5",
            "status": "Active",
            "signingMaterial": {
                "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc"
            }
        }
    ]
}
```

## Output

profiles -> (list)

A list of profiles that are available in the AWS account. This includes profiles with the status of `CANCELED` if the `includeCanceled` parameter is set to `true` .

(structure)

Contains information about the ACM certificates and signing configuration parameters that can be used by a given code signing user.

profileName -> (string)

The name of the signing profile.

profileVersion -> (string)

The version of a signing profile.

profileVersionArn -> (string)

The ARN of a signing profile, including the profile version.

signingMaterial -> (structure)

The ACM certificate that is available for use by a signing profile.

certificateArn -> (string)

The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

signatureValidityPeriod -> (structure)

The validity period for a signing job created using this signing profile.

value -> (integer)

The numerical value of the time unit for signature validity.

type -> (string)

The time unit for signature validity.

platformId -> (string)

The ID of a platform that is available for use by a signing profile.

platformDisplayName -> (string)

The name of the signing platform.

signingParameters -> (map)

The parameters that are available for use by a Signer user.

key -> (string)

value -> (string)

status -> (string)

The status of a signing profile.

arn -> (string)

The Amazon Resource Name (ARN) for the signing profile.

tags -> (map)

A list of tags associated with the signing profile.

key -> (string)

value -> (string)

nextToken -> (string)

Value for specifying the next set of paginated results to return.