# get-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/get-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/get-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [importexport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/index.html#cli-aws-importexport) ]

# get-status

## Description

This operation returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. You can only return information about jobs you own.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/GetStatus)

## Synopsis

```
get-status
--job-id <value>
[--api-version <value>]
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

`--job-id` (string)
A unique identifier which refers to a particular job.

`--api-version` (string)
Specifies the version of the client tool.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

The following command returns the status the specified job:

```
aws importexport get-status  --job-id EX1ID
```

The output for the get-status command looks like the following:

```
2015-05-27T18:58:21Z    manifestVersion:2.0
generator:Text editor
bucket:amzn-s3-demo-bucket
deviceId:49382
eraseDevice:yes
notificationEmail:john.doe@example.com;jane.roe@example.com
trueCryptPassword:password123
acl:private
serviceLevel:standard
returnAddress:
    name: Jane Roe
    company: Example Corp.
    street1: 123 Any Street
    street2:
    street3:
    city: Anytown
    stateOrProvince: WA
    postalCode: 91011-1111
    country:USA
    phoneNumber:206-555-1111    0       EX1ID   Import  NotReceived     AWS has not received your device.       Pending The specified job has not started.
ktKDXpdbEXAMPLEyGFJmQO744UHw=    version:2.0
signingMethod:HmacSHA1
jobId:EX1ID
signature:ktKDXpdbEXAMPLEyGFJmQO744UHw=
```

When you ship your device, it will be delivered to a sorting facility, and then forwarded on to an AWS data center. Note that when you send a get-status command, the status of your job will not show as `At AWS` until the shipment has been received at the AWS data center.

## Output

JobId -> (string)

A unique identifier which refers to a particular job.

JobType -> (string)

Specifies whether the job to initiate is an import or export job.

LocationCode -> (string)

A token representing the location of the storage device, such as âAtAWSâ.

LocationMessage -> (string)

A more human readable form of the physical location of the storage device.

ProgressCode -> (string)

A token representing the state of the job, such as âStartedâ.

ProgressMessage -> (string)

A more human readable form of the job status.

Carrier -> (string)

Name of the shipping company. This value is included when the LocationCode is âReturnedâ.

TrackingNumber -> (string)

The shipping tracking number assigned by AWS Import/Export to the storage device when itâs returned to you. We return this value when the LocationCode is âReturnedâ.

LogBucket -> (string)

Amazon S3 bucket for user logs.

LogKey -> (string)

The key where the user logs were stored.

ErrorCount -> (integer)

Number of errors. We return this value when the ProgressCode is Success or SuccessWithErrors.

Signature -> (string)

An encrypted code used to authenticate the request and response, for example, âDV+TpDfx1/TdSE9ktyK9k/bDTVI=â. Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.

SignatureFileContents -> (string)

An encrypted code used to authenticate the request and response, for example, âDV+TpDfx1/TdSE9ktyK9k/bDTVI=â. Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.

CurrentManifest -> (string)

The last manifest submitted, which will be used to process the job.

CreationDate -> (timestamp)

Timestamp of the CreateJob request in ISO8601 date format. For example â2010-03-28T20:27:35Zâ.

ArtifactList -> (list)

A collection of artifacts.

(structure)

A discrete item that contains the description and URL of an artifact (such as a PDF).

Description -> (string)

The associated description for this object.

URL -> (string)

The URL for a given Artifact.