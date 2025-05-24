# send-commandÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb-session/send-command.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb-session/send-command.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qldb-session](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb-session/index.html#cli-aws-qldb-session) ]

# send-command

## Description

Sends a command to an Amazon QLDB ledger.

### Note

Instead of interacting directly with this API, we recommend using the QLDB driver or the QLDB shell to execute data transactions on a ledger.

- If you are working with an AWS SDK, use the QLDB driver. The driver provides a high-level abstraction layer above this *QLDB Session* data plane and manages `SendCommand` API calls for you. For information and a list of supported programming languages, see [Getting started with the driver](https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-driver.html) in the *Amazon QLDB Developer Guide* .
- If you are working with the AWS Command Line Interface (AWS CLI), use the QLDB shell. The shell is a command line interface that uses the QLDB driver to interact with a ledger. For information, see [Accessing Amazon QLDB using the QLDB shell](https://docs.aws.amazon.com/qldb/latest/developerguide/data-shell.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qldb-session-2019-07-11/SendCommand)

## Synopsis

```
send-command
[--session-token <value>]
[--start-session <value>]
[--start-transaction <value>]
[--end-session <value>]
[--commit-transaction <value>]
[--abort-transaction <value>]
[--execute-statement <value>]
[--fetch-page <value>]
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

`--session-token` (string)

Specifies the session token for the current command. A session token is constant throughout the life of the session.

To obtain a session token, run the `StartSession` command. This `SessionToken` is required for every subsequent command that is issued during the current session.

`--start-session` (structure)

Command to start a new session. A session token is obtained as part of the response.

LedgerName -> (string)

The name of the ledger to start a new session against.

Shorthand Syntax:

```
LedgerName=string
```

JSON Syntax:

```
{
  "LedgerName": "string"
}
```

`--start-transaction` (structure)

Command to start a new transaction.

JSON Syntax:

```
{

}
```

`--end-session` (structure)

Command to end the current session.

JSON Syntax:

```
{

}
```

`--commit-transaction` (structure)

Command to commit the specified transaction.

TransactionId -> (string)

Specifies the transaction ID of the transaction to commit.

CommitDigest -> (blob)

Specifies the commit digest for the transaction to commit. For every active transaction, the commit digest must be passed. QLDB validates `CommitDigest` and rejects the commit with an error if the digest computed on the client does not match the digest computed by QLDB.

The purpose of the `CommitDigest` parameter is to ensure that QLDB commits a transaction if and only if the server has processed the exact set of statements sent by the client, in the same order that client sent them, and with no duplicates.

Shorthand Syntax:

```
TransactionId=string,CommitDigest=blob
```

JSON Syntax:

```
{
  "TransactionId": "string",
  "CommitDigest": blob
}
```

`--abort-transaction` (structure)

Command to abort the current transaction.

JSON Syntax:

```
{

}
```

`--execute-statement` (structure)

Command to execute a statement in the specified transaction.

TransactionId -> (string)

Specifies the transaction ID of the request.

Statement -> (string)

Specifies the statement of the request.

Parameters -> (list)

Specifies the parameters for the parameterized statement in the request.

(structure)

A structure that can contain a value in multiple encoding formats.

IonBinary -> (blob)

An Amazon Ion binary value contained in a `ValueHolder` structure.

IonText -> (string)

An Amazon Ion plaintext value contained in a `ValueHolder` structure.

Shorthand Syntax:

```
TransactionId=string,Statement=string,Parameters=[{IonBinary=blob,IonText=string},{IonBinary=blob,IonText=string}]
```

JSON Syntax:

```
{
  "TransactionId": "string",
  "Statement": "string",
  "Parameters": [
    {
      "IonBinary": blob,
      "IonText": "string"
    }
    ...
  ]
}
```

`--fetch-page` (structure)

Command to fetch a page.

TransactionId -> (string)

Specifies the transaction ID of the page to be fetched.

NextPageToken -> (string)

Specifies the next page token of the page to be fetched.

Shorthand Syntax:

```
TransactionId=string,NextPageToken=string
```

JSON Syntax:

```
{
  "TransactionId": "string",
  "NextPageToken": "string"
}
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

StartSession -> (structure)

Contains the details of the started session that includes a session token. This `SessionToken` is required for every subsequent command that is issued during the current session.

SessionToken -> (string)

Session token of the started session. This `SessionToken` is required for every subsequent command that is issued during the current session.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

StartTransaction -> (structure)

Contains the details of the started transaction.

TransactionId -> (string)

The transaction ID of the started transaction.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

EndSession -> (structure)

Contains the details of the ended session.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

CommitTransaction -> (structure)

Contains the details of the committed transaction.

TransactionId -> (string)

The transaction ID of the committed transaction.

CommitDigest -> (blob)

The commit digest of the committed transaction.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

ConsumedIOs -> (structure)

Contains metrics about the number of I/O requests that were consumed.

ReadIOs -> (long)

The number of read I/O requests that the command made.

WriteIOs -> (long)

The number of write I/O requests that the command made.

AbortTransaction -> (structure)

Contains the details of the aborted transaction.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

ExecuteStatement -> (structure)

Contains the details of the executed statement.

FirstPage -> (structure)

Contains the details of the first fetched page.

Values -> (list)

A structure that contains values in multiple encoding formats.

(structure)

A structure that can contain a value in multiple encoding formats.

IonBinary -> (blob)

An Amazon Ion binary value contained in a `ValueHolder` structure.

IonText -> (string)

An Amazon Ion plaintext value contained in a `ValueHolder` structure.

NextPageToken -> (string)

The token of the next page.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

ConsumedIOs -> (structure)

Contains metrics about the number of I/O requests that were consumed.

ReadIOs -> (long)

The number of read I/O requests that the command made.

WriteIOs -> (long)

The number of write I/O requests that the command made.

FetchPage -> (structure)

Contains the details of the fetched page.

Page -> (structure)

Contains details of the fetched page.

Values -> (list)

A structure that contains values in multiple encoding formats.

(structure)

A structure that can contain a value in multiple encoding formats.

IonBinary -> (blob)

An Amazon Ion binary value contained in a `ValueHolder` structure.

IonText -> (string)

An Amazon Ion plaintext value contained in a `ValueHolder` structure.

NextPageToken -> (string)

The token of the next page.

TimingInformation -> (structure)

Contains server-side performance information for the command.

ProcessingTimeMilliseconds -> (long)

The amount of time that QLDB spent on processing the command, measured in milliseconds.

ConsumedIOs -> (structure)

Contains metrics about the number of I/O requests that were consumed.

ReadIOs -> (long)

The number of read I/O requests that the command made.

WriteIOs -> (long)

The number of write I/O requests that the command made.