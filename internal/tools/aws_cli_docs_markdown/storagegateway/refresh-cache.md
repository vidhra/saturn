# refresh-cacheÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# refresh-cache

## Description

Refreshes the cached inventory of objects for the specified file share. This operation finds objects in the Amazon S3 bucket that were added, removed, or replaced since the gateway last listed the bucketâs contents and cached the results. This operation does not import files into the S3 File Gateway cache storage. It only updates the cached inventory to reflect changes in the inventory of the objects in the S3 bucket. This operation is only supported in the S3 File Gateway types.

You can subscribe to be notified through an Amazon CloudWatch event when your `RefreshCache` operation completes. For more information, see [Getting notified about file operations](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide* . This operation is Only supported for S3 File Gateways.

When this API is called, it only initiates the refresh operation. When the API call completes and returns a success code, it doesnât necessarily mean that the file refresh has completed. You should use the refresh-complete notification to determine that the operation has completed before you check for new files on the gateway file share. You can subscribe to be notified through a CloudWatch event when your `RefreshCache` operation completes.

Throttle limit: This API is asynchronous, so the gateway will accept no more than two refreshes at any time. We recommend using the refresh-complete CloudWatch event notification before issuing additional requests. For more information, see [Getting notified about file operations](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide* .

### Warning

- Wait at least 60 seconds between consecutive RefreshCache API requests.
- If you invoke the RefreshCache API when two requests are already being processed, any new request will cause an `InvalidGatewayRequestException` error because too many requests were sent to the server.

### Note

The S3 bucket name does not need to be included when entering the list of folders in the FolderList parameter.

For more information, see [Getting notified about file operations](https://docs.aws.amazon.com/filegateway/latest/files3/monitoring-file-gateway.html#get-notification) in the *Amazon S3 File Gateway User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/RefreshCache)

## Synopsis

```
refresh-cache
--file-share-arn <value>
[--folder-list <value>]
[--recursive | --no-recursive]
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

`--file-share-arn` (string)

The Amazon Resource Name (ARN) of the file share you want to refresh.

`--folder-list` (list)

A comma-separated list of the paths of folders to refresh in the cache. The default is [`"/"` ]. The default refreshes objects and folders at the root of the Amazon S3 bucket. If `Recursive` is set to `true` , the entire S3 bucket that the file share has access to is refreshed.

Do not include `/` when specifying folder names. For example, you would specify `samplefolder` rather than `samplefolder/` .

(string)

Syntax:

```
"string" "string" ...
```

`--recursive` | `--no-recursive` (boolean)

A value that specifies whether to recursively refresh folders in the cache. The refresh includes folders that were in the cache the last time the gateway listed the folderâs contents. If this value set to `true` , each folder that is listed in `FolderList` is recursively updated. Otherwise, subfolders listed in `FolderList` are not refreshed. Only objects that are in folders listed directly under `FolderList` are found and used for the update. The default is `true` .

Valid Values: `true` | `false`

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

**To refresh the file share cache**

The following `refresh-cache` example refreshes the cache for the specified file share.

```
aws storagegateway refresh-cache \
    --file-share-arn arn:aws:storagegateway:us-east-1:111122223333:share/share-2FA12345
```

Output:

```
{
    "FileShareARN": "arn:aws:storagegateway:us-east-1:111122223333:share/share-2FA12345",
    "NotificationId": "4954d4b1-abcd-ef01-1234-97950a7d3483"
}
```

For more information, see [ListFileShares](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html) in the *AWS Storage Gateway Service API Reference*.

## Output

FileShareARN -> (string)

The Amazon Resource Name (ARN) of the file share.

NotificationId -> (string)

The randomly generated ID of the notification that was sent. This ID is in UUID format.