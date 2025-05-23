# verify-query-resultsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/verify-query-results.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/verify-query-results.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# verify-query-results

## Description

Validates CloudTrail Lake queryâs export files.

This command uses the query export and sign file delivered to you to
perform the validation.

The AWS CLI allows you to detect the following types of changes:

- Modification or deletion of CloudTrail Lake queryâs export files.

To validate export files with the AWS CLI, the following preconditions must
be met:

- You must have online connectivity to AWS.
- You must put the sign file and export file in the specified path prefix
- You must not rename the delivered export file and sign file
- For validate export files from S3: (1) You must have read access to the
S3 bucket that contains the sign and export file. (2) The digest and log
files must not have been moved from the original S3 location where
CloudTrail delivered them.

### Note

For verify export file from S3, this command requires that the user or
role executing the command has permission to call GetObject, and
GetBucketLocation for the bucket that store the export file.

## Synopsis

```
verify-query-results
[--local-export-path <value>]
[--s3-bucket <value>]
[--s3-prefix <value>]
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

`--local-export-path` (string)
Specifies the local directory of export and sign file, e.g. /local/path/to/export/file/

`--s3-bucket` (string)
Specifies the S3 bucket name that store the query result and sign file This parameter can not coexist with local-export-path.

`--s3-prefix` (string)
Specifies the S3 path of the S3 folder that containexport and sign file, e.g. bucket_name/s3/path/ . This parameter can not coexist with local-export-path. If the files located in s3 bucket root directory, then no need to provide this parameter.

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