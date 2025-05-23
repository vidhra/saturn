# get-storage-lens-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-storage-lens-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3control](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/index.html#cli-aws-s3control) ]

# get-storage-lens-group

## Description

Retrieves the Storage Lens group configuration details.

To use this operation, you must have the permission to perform the `s3:GetStorageLensGroup` action. For more information about the required Storage Lens Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_iam_permissions.html#storage_lens_groups_permissions) .

For information about Storage Lens groups errors, see [List of Amazon S3 Storage Lens error codes](https://docs.aws.amazon.com/AmazonS3/latest/API/ErrorResponses.html#S3LensErrorCodeList) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3control-2018-08-20/GetStorageLensGroup)

## Synopsis

```
get-storage-lens-group
--name <value>
--account-id <value>
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

`--name` (string)

The name of the Storage Lens group that youâre trying to retrieve the configuration details for.

`--account-id` (string)

The Amazon Web Services account ID associated with the Storage Lens group that youâre trying to retrieve the details for.

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

StorageLensGroup -> (structure)

The name of the Storage Lens group that youâre trying to retrieve the configuration details for.

Name -> (string)

Contains the name of the Storage Lens group.

Filter -> (structure)

Sets the criteria for the Storage Lens group data that is displayed. For multiple filter conditions, the `AND` or `OR` logical operator is used.

MatchAnyPrefix -> (list)

Contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed.

(string)

MatchAnySuffix -> (list)

Contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed.

(string)

MatchAnyTag -> (list)

Contains the list of S3 object tags. At least one object tag must be specified. Up to 10 object tags are allowed.

(structure)

A container for a key-value name pair.

Key -> (string)

Key of the tag

Value -> (string)

Value of the tag

MatchObjectAge -> (structure)

Contains `DaysGreaterThan` and `DaysLessThan` to define the object age range (minimum and maximum number of days).

DaysGreaterThan -> (integer)

Specifies the maximum object age in days. Must be a positive whole number, greater than the minimum object age and less than or equal to 2,147,483,647.

DaysLessThan -> (integer)

Specifies the minimum object age in days. The value must be a positive whole number, greater than 0 and less than or equal to 2,147,483,647.

MatchObjectSize -> (structure)

Contains `BytesGreaterThan` and `BytesLessThan` to define the object size range (minimum and maximum number of Bytes).

BytesGreaterThan -> (long)

Specifies the minimum object size in Bytes. The value must be a positive number, greater than 0 and less than 5 TB.

BytesLessThan -> (long)

Specifies the maximum object size in Bytes. The value must be a positive number, greater than the minimum object size and less than 5 TB.

And -> (structure)

A logical operator that allows multiple filter conditions to be joined for more complex comparisons of Storage Lens group data. Objects must match all of the listed filter conditions that are joined by the `And` logical operator. Only one of each filter condition is allowed.

MatchAnyPrefix -> (list)

Contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed.

(string)

MatchAnySuffix -> (list)

Contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed.

(string)

MatchAnyTag -> (list)

Contains the list of object tags. At least one object tag must be specified. Up to 10 object tags are allowed.

(structure)

A container for a key-value name pair.

Key -> (string)

Key of the tag

Value -> (string)

Value of the tag

MatchObjectAge -> (structure)

Contains `DaysGreaterThan` and `DaysLessThan` to define the object age range (minimum and maximum number of days).

DaysGreaterThan -> (integer)

Specifies the maximum object age in days. Must be a positive whole number, greater than the minimum object age and less than or equal to 2,147,483,647.

DaysLessThan -> (integer)

Specifies the minimum object age in days. The value must be a positive whole number, greater than 0 and less than or equal to 2,147,483,647.

MatchObjectSize -> (structure)

Contains `BytesGreaterThan` and `BytesLessThan` to define the object size range (minimum and maximum number of Bytes).

BytesGreaterThan -> (long)

Specifies the minimum object size in Bytes. The value must be a positive number, greater than 0 and less than 5 TB.

BytesLessThan -> (long)

Specifies the maximum object size in Bytes. The value must be a positive number, greater than the minimum object size and less than 5 TB.

Or -> (structure)

A single logical operator that allows multiple filter conditions to be joined. Objects can match any of the listed filter conditions, which are joined by the `Or` logical operator. Only one of each filter condition is allowed.

MatchAnyPrefix -> (list)

Filters objects that match any of the specified prefixes.

(string)

MatchAnySuffix -> (list)

Filters objects that match any of the specified suffixes.

(string)

MatchAnyTag -> (list)

Filters objects that match any of the specified S3 object tags.

(structure)

A container for a key-value name pair.

Key -> (string)

Key of the tag

Value -> (string)

Value of the tag

MatchObjectAge -> (structure)

Filters objects that match the specified object age range.

DaysGreaterThan -> (integer)

Specifies the maximum object age in days. Must be a positive whole number, greater than the minimum object age and less than or equal to 2,147,483,647.

DaysLessThan -> (integer)

Specifies the minimum object age in days. The value must be a positive whole number, greater than 0 and less than or equal to 2,147,483,647.

MatchObjectSize -> (structure)

Filters objects that match the specified object size range.

BytesGreaterThan -> (long)

Specifies the minimum object size in Bytes. The value must be a positive number, greater than 0 and less than 5 TB.

BytesLessThan -> (long)

Specifies the maximum object size in Bytes. The value must be a positive number, greater than the minimum object size and less than 5 TB.

StorageLensGroupArn -> (string)

Contains the Amazon Resource Name (ARN) of the Storage Lens group. This property is read-only.