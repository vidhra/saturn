# list-usersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-users.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/list-users.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# list-users

## Description

Lists the users for a file transfer protocol-enabled server that you specify by passing the `ServerId` parameter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/ListUsers)

`list-users` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Users`

## Synopsis

```
list-users
--server-id <value>
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

`--server-id` (string)

A system-assigned unique identifier for a server that has users assigned to it.

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

## Output

NextToken -> (string)

When you can get additional results from the `ListUsers` call, a `NextToken` parameter is returned in the output. You can then pass in a subsequent command to the `NextToken` parameter to continue listing additional users.

ServerId -> (string)

A system-assigned unique identifier for a server that the users are assigned to.

Users -> (list)

Returns the Transfer Family users and their properties for the `ServerId` value that you specify.

(structure)

Returns properties of the user that you specify.

Arn -> (string)

Provides the unique Amazon Resource Name (ARN) for the user that you want to learn about.

HomeDirectory -> (string)

The landing directory (folder) for a user when they log in to the server using the client.

A `HomeDirectory` example is `/bucket_name/home/mydirectory` .

### Note

The `HomeDirectory` parameter is only used if `HomeDirectoryType` is set to `PATH` .

HomeDirectoryType -> (string)

The type of landing directory (folder) that you want your usersâ home directory to be when they log in to the server. If you set it to `PATH` , the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to `LOGICAL` , you need to provide mappings in the `HomeDirectoryMappings` for how you want to make Amazon S3 or Amazon EFS paths visible to your users.

### Note

If `HomeDirectoryType` is `LOGICAL` , you must provide mappings, using the `HomeDirectoryMappings` parameter. If, on the other hand, `HomeDirectoryType` is `PATH` , you provide an absolute path using the `HomeDirectory` parameter. You cannot have both `HomeDirectory` and `HomeDirectoryMappings` in your template.

Role -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your usersâ access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your usersâ transfer requests.

### Note

The IAM role that controls your usersâ access to your Amazon S3 bucket for servers with `Domain=S3` , or your EFS file system for servers with `Domain=EFS` .

The policies attached to this role determine the level of access you want to provide your users when transferring files into and out of your S3 buckets or EFS file systems.

SshPublicKeyCount -> (integer)

Specifies the number of SSH public keys stored for the user you specified.

UserName -> (string)

Specifies the name of the user whose ARN was specified. User names are used for authentication purposes.