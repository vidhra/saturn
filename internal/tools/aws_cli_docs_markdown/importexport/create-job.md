# create-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/create-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/create-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [importexport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/importexport/index.html#cli-aws-importexport) ]

# create-job

## Description

This operation initiates the process of scheduling an upload or download of your data. You include in the request a manifest that describes the data transfer specifics. The response to the request includes a job ID, which you can use in other operations, a signature that you use to identify your storage device, and the address where you should ship your storage device.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/importexport-2010-06-01/CreateJob)

## Synopsis

```
create-job
--job-type <value>
--manifest <value>
[--manifest-addendum <value>]
--validate-only | --no-validate-only
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

`--job-type` (string)
Specifies whether the job to initiate is an import or export job.

Possible values:

- `Import`
- `Export`

`--manifest` (string)
The UTF-8 encoded text of the manifest file.

`--manifest-addendum` (string)
For internal use only.

`--validate-only` | `--no-validate-only` (boolean)
Validate the manifest and parameter values in the request but do not actually create a job.

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

The following command creates an import job from a manifest file:

```
aws importexport create-job --job-type import --manifest file://manifest --no-validate-only
```

The file `manifest` is a YAML formatted text file in the current directory with the following content:

```
manifestVersion: 2.0;
returnAddress:
name: Jane Roe
company: Example Corp.
street1: 123 Any Street
city: Anytown
stateOrProvince: WA
postalCode: 91011-1111
phoneNumber: 206-555-1111
country: USA
deviceId: 49382
eraseDevice: yes
notificationEmail: john.doe@example.com;jane.roe@example.com
bucket: amzn-s3-demo-bucket
```

For more information on the manifest file format, see [Creating Import Manifests](http://docs.aws.amazon.com/AWSImportExport/latest/DG/ImportManifestFile.html) in the *AWS Import/Export Developer Guide*.

You can also pass the manifest as a string in quotes:

```
aws importexport create-job --job-type import --manifest 'manifestVersion: 2.0;
 returnAddress:
 name: Jane Roe
 company: Example Corp.
 street1: 123 Any Street
 city: Anytown
 stateOrProvince: WA
 postalCode: 91011-1111
 phoneNumber: 206-555-1111
 country: USA
 deviceId: 49382
 eraseDevice: yes
 notificationEmail: john.doe@example.com;jane.roe@example.com
 bucket: amzn-s3-demo-bucket'
```

For information on quoting string arguments and using files, see [Specifying Parameter Values](http://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html) in the *AWS CLI User Guide*.

## Output

JobId -> (string)

A unique identifier which refers to a particular job.

JobType -> (string)

Specifies whether the job to initiate is an import or export job.

Signature -> (string)

An encrypted code used to authenticate the request and response, for example, âDV+TpDfx1/TdSE9ktyK9k/bDTVI=â. Only use this value is you want to create the signature file yourself. Generally you should use the SignatureFileContents value.

SignatureFileContents -> (string)

The actual text of the SIGNATURE file to be written to disk.

WarningMessage -> (string)

An optional message notifying you of non-fatal issues with the job, such as use of an incompatible Amazon S3 bucket name.

ArtifactList -> (list)

A collection of artifacts.

(structure)

A discrete item that contains the description and URL of an artifact (such as a PDF).

Description -> (string)

The associated description for this object.

URL -> (string)

The URL for a given Artifact.