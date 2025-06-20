# create-kx-changesetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-changeset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-changeset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# create-kx-changeset

## Description

Creates a changeset for a kdb database. A changeset allows you to add and delete existing files by using an ordered list of change requests.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/CreateKxChangeset)

## Synopsis

```
create-kx-changeset
--environment-id <value>
--database-name <value>
--change-requests <value>
[--client-token <value>]
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

`--environment-id` (string)

A unique identifier of the kdb environment.

`--database-name` (string)

The name of the kdb database.

`--change-requests` (list)

A list of change request objects that are run in order. A change request object consists of `changeType` , `s3Path` , and `dbPath` . A changeType can have the following values:

- PUT â Adds or updates files in a database.
- DELETE â Deletes files in a database.

All the change requests require a mandatory `dbPath` attribute that defines the path within the database directory. All database paths must start with a leading / and end with a trailing /. The `s3Path` attribute defines the s3 source file path and is required for a PUT change type. The `s3path` must end with a trailing / if it is a directory and must end without a trailing / if it is a file.

Here are few examples of how you can use the change request object:

- This request adds a single sym file at database root location.   `{ "changeType": "PUT", "s3Path":"s3://bucket/db/sym", "dbPath":"/"}`
- This request adds files in the given `s3Path` under the 2020.01.02 partition of the database.  `{ "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/", "dbPath":"/2020.01.02/"}`
- This request adds files in the given `s3Path` under the *taq* table partition of the database.  `[ { "changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]`
- This request deletes the 2020.01.02 partition of the database.  `[{ "changeType": "DELETE", "dbPath": "/2020.01.02/"} ]`
- The *DELETE* request allows you to delete the existing files under the 2020.01.02 partition of the database, and the *PUT* request adds a new taq table under it.  `[ {"changeType": "DELETE", "dbPath":"/2020.01.02/"}, {"changeType": "PUT", "s3Path":"s3://bucket/db/2020.01.02/taq/", "dbPath":"/2020.01.02/taq/"}]`

(structure)

A list of change request objects.

changeType -> (string)

Defines the type of change request. A `changeType` can have the following values:

- PUT â Adds or updates files in a database.
- DELETE â Deletes files in a database.

s3Path -> (string)

Defines the S3 path of the source file that is required to add or update files in a database.

dbPath -> (string)

Defines the path within the database directory.

Shorthand Syntax:

```
changeType=string,s3Path=string,dbPath=string ...
```

JSON Syntax:

```
[
  {
    "changeType": "PUT"|"DELETE",
    "s3Path": "string",
    "dbPath": "string"
  }
  ...
]
```

`--client-token` (string)

A token that ensures idempotency. This token expires in 10 minutes.

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

changesetId -> (string)

A unique identifier for the changeset.

databaseName -> (string)

The name of the kdb database.

environmentId -> (string)

A unique identifier for the kdb environment.

changeRequests -> (list)

A list of change requests.

(structure)

A list of change request objects.

changeType -> (string)

Defines the type of change request. A `changeType` can have the following values:

- PUT â Adds or updates files in a database.
- DELETE â Deletes files in a database.

s3Path -> (string)

Defines the S3 path of the source file that is required to add or update files in a database.

dbPath -> (string)

Defines the path within the database directory.

createdTimestamp -> (timestamp)

The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

lastModifiedTimestamp -> (timestamp)

The timestamp at which the changeset was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

status -> (string)

Status of the changeset creation process.

- Pending â Changeset creation is pending.
- Processing â Changeset creation is running.
- Failed â Changeset creation has failed.
- Complete â Changeset creation has succeeded.

errorInfo -> (structure)

The details of the error that you receive when creating a changeset. It consists of the type of error and the error message.

errorMessage -> (string)

Specifies the error message that appears if a flow fails.

errorType -> (string)

Specifies the type of error.