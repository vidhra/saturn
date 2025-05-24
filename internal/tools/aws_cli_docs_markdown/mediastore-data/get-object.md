# get-objectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/get-object.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/get-object.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediastore-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/index.html#cli-aws-mediastore-data) ]

# get-object

## Description

Downloads the object at the specified path. If the objectâs upload availability is set to `streaming` , AWS Elemental MediaStore downloads the object even if itâs still uploading the object.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediastore-data-2017-09-01/GetObject)

## Synopsis

```
get-object
--path <value>
[--range <value>]
<outfile>
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

`--path` (string)

The path (including the file name) where the object is stored in the container. Format: <folder name>/<folder name>/<file name>

For example, to upload the file `mlaw.avi` to the folder path `premium\canada` in the container `movies` , enter the path `premium/canada/mlaw.avi` .

Do not include the container name in this path.

If the path includes any folders that donât exist yet, the service creates them. For example, suppose you have an existing `premium/usa` subfolder. If you specify `premium/canada` , the service creates a `canada` subfolder in the `premium` folder. You then have two subfolders, `usa` and `canada` , in the `premium` folder.

There is no correlation between the path to the source and the path (folders) in the container in AWS Elemental MediaStore.

For more information about folders and how they exist in a container, see the [AWS Elemental MediaStore User Guide](http://docs.aws.amazon.com/mediastore/latest/ug/) .

The file name is the name that is assigned to the file that you upload. The file can have the same name inside and outside of AWS Elemental MediaStore, or it can have the same name. The file name can include or omit an extension.

`--range` (string)

The range bytes of an object to retrieve. For more information about the `Range` header, see [http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35) . AWS Elemental MediaStore ignores this header for partially uploaded objects that have streaming upload availability.

`outfile` (string)
Filename where the content will be saved

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

**Example 1: To download an entire object**

The following `get-object` example downloads the specified object.

```
aws mediastore-data get-object \
    --endpoint https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com \
    --path events/baseball/setup.jpg setup.jpg
```

Output:

```
{
    "ContentType": "image/jpeg",
    "StatusCode": 200,
    "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3",
    "ContentLength": "3860266",
    "LastModified": "Fri, 19 Jul 2019 21:50:31 GMT"
}
```

**Example 2: To download part of an object**

The following `get-object` example downloads the specified part of an object.

```
aws mediastore-data get-object \
    --endpoint https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com \
    --path events/baseball/setup.jpg setup.jpg \
    --range "bytes=0-100"
```

Output:

```
{
    "StatusCode": 206,
    "LastModified": "Fri, 19 Jul 2019 21:50:31 GMT",
    "ContentType": "image/jpeg",
    "ContentRange": "bytes 0-100/3860266",
    "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3",
    "ContentLength": "101"
}
```

For more information, see [Downloading an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-download.html) in the *AWS Elemental MediaStore User Guide*.

## Output

Body -> (streaming blob)

The bytes of the object.

CacheControl -> (string)

An optional `CacheControl` header that allows the caller to control the objectâs cache behavior. Headers can be passed in as specified in the HTTP spec at [https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) .

Headers with a custom user-defined value are also accepted.

ContentRange -> (string)

The range of bytes to retrieve.

ContentLength -> (long)

The length of the object in bytes.

ContentType -> (string)

The content type of the object.

ETag -> (string)

The ETag that represents a unique instance of the object.

LastModified -> (timestamp)

The date and time that the object was last modified.

StatusCode -> (integer)

The HTML status code of the request. Status codes ranging from 200 to 299 indicate success. All other status codes indicate the type of error that occurred.