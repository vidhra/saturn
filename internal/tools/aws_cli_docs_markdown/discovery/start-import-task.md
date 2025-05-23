# start-import-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-import-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/start-import-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [discovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html#cli-aws-discovery) ]

# start-import-task

## Description

Starts an import task, which allows you to import details of your on-premises environment directly into Amazon Web Services Migration Hub without having to use the Amazon Web Services Application Discovery Service (Application Discovery Service) tools such as the Amazon Web Services Application Discovery Service Agentless Collector or Application Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data, including the ability to group your devices as applications and track their migration status.

To start an import request, do this:

- Download the specially formatted comma separated value (CSV) import template, which you can find here: [https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv](https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv) .
- Fill out the template with your server and application data.
- Upload your import file to an Amazon S3 bucket, and make a note of itâs Object URL. Your import file must be in the CSV format.
- Use the console or the `StartImportTask` command with the Amazon Web Services CLI or one of the Amazon Web Services SDKs to import the records from your file.

For more information, including step-by-step procedures, see [Migration Hub Import](https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html) in the *Amazon Web Services Application Discovery Service User Guide* .

### Note

There are limits to the number of import tasks you can create (and delete) in an Amazon Web Services account. For more information, see [Amazon Web Services Application Discovery Service Limits](https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html) in the *Amazon Web Services Application Discovery Service User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/StartImportTask)

## Synopsis

```
start-import-task
[--client-request-token <value>]
--name <value>
--import-url <value>
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

`--client-request-token` (string)

Optional. A unique token that you can provide to prevent the same import request from occurring more than once. If you donât provide a token, a token is automatically generated.

Sending more than one `StartImportTask` request with the same client request token will return information about the original import task with that client request token.

`--name` (string)

A descriptive name for this request. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.

`--import-url` (string)

The URL for your import file that youâve uploaded to Amazon S3.

### Note

If youâre using the Amazon Web Services CLI, this URL is structured as follows: `s3://BucketName/ImportFileName.CSV`

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

task -> (structure)

An array of information related to the import task request including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

importTaskId -> (string)

The unique ID for a specific import task. These IDs arenât globally unique, but they are unique within an Amazon Web Services account.

clientRequestToken -> (string)

A unique token used to prevent the same import request from occurring more than once. If you didnât provide a token, a token was automatically generated when the import task request was sent.

name -> (string)

A descriptive name for an import task. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.

importUrl -> (string)

The URL for your import file that youâve uploaded to Amazon S3.

status -> (string)

The status of the import task. An import can have the status of `IMPORT_COMPLETE` and still have some records fail to import from the overall request. More information can be found in the downloadable archive defined in the `errorsAndFailedEntriesZip` field, or in the Migration Hub management console.

importRequestTime -> (timestamp)

The time that the import task request was made, presented in the Unix time stamp format.

importCompletionTime -> (timestamp)

The time that the import task request finished, presented in the Unix time stamp format.

importDeletedTime -> (timestamp)

The time that the import task request was deleted, presented in the Unix time stamp format.

fileClassification -> (string)

The type of file detected by the import task.

serverImportSuccess -> (integer)

The total number of server records in the import file that were successfully imported.

serverImportFailure -> (integer)

The total number of server records in the import file that failed to be imported.

applicationImportSuccess -> (integer)

The total number of application records in the import file that were successfully imported.

applicationImportFailure -> (integer)

The total number of application records in the import file that failed to be imported.

errorsAndFailedEntriesZip -> (string)

A link to a compressed archive folder (in the ZIP format) that contains an error log and a file of failed records. You can use these two files to quickly identify records that failed, why they failed, and correct those records. Afterward, you can upload the corrected file to your Amazon S3 bucket and create another import task request.

This field also includes authorization information so you can confirm the authenticity of the compressed archive before you download it.

If some records failed to be imported we recommend that you correct the records in the failed entries file and then imports that failed entries file. This prevents you from having to correct and update the larger original file and attempt importing it again.