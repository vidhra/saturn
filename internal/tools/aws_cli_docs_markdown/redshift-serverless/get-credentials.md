# get-credentialsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/get-credentials.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/get-credentials.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/index.html#cli-aws-redshift-serverless) ]

# get-credentials

## Description

Returns a database user name and temporary password with temporary authorization to log in to Amazon Redshift Serverless.

By default, the temporary credentials expire in 900 seconds. You can optionally specify a duration between 900 seconds (15 minutes) and 3600 seconds (60 minutes).

The Identity and Access Management (IAM) user or role that runs GetCredentials must have an IAM policy attached that allows access to all necessary actions and resources.

If the `DbName` parameter is specified, the IAM policy must allow access to the resource dbname for the specified database name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-serverless-2021-04-21/GetCredentials)

## Synopsis

```
get-credentials
[--custom-domain-name <value>]
[--db-name <value>]
[--duration-seconds <value>]
[--workgroup-name <value>]
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

`--custom-domain-name` (string)

The custom domain name associated with the workgroup. The custom domain name or the workgroup name must be included in the request.

`--db-name` (string)

The name of the database to get temporary authorization to log on to.

Constraints:

- Must be 1 to 64 alphanumeric characters or hyphens.
- Must contain only uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.
- The first character must be a letter.
- Must not contain a colon ( : ) or slash ( / ).
- Cannot be a reserved word. A list of reserved words can be found in [Reserved Words](https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html) in the Amazon Redshift Database Developer Guide

`--duration-seconds` (integer)

The number of seconds until the returned temporary password expires. The minimum is 900 seconds, and the maximum is 3600 seconds.

`--workgroup-name` (string)

The name of the workgroup associated with the database.

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

dbPassword -> (string)

A temporary password that authorizes the user name returned by `DbUser` to log on to the database `DbName` .

dbUser -> (string)

A database user name that is authorized to log on to the database `DbName` using the password `DbPassword` . If the specified `DbUser` exists in the database, the new user name has the same database privileges as the the user named in `DbUser` . By default, the user is added to PUBLIC.

expiration -> (timestamp)

The date and time the password in `DbPassword` expires.

nextRefreshTime -> (timestamp)

The date and time of when the `DbUser` and `DbPassword` authorization refreshes.