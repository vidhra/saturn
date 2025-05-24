# rmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html#cli-aws-s3) ]

# rm

## Description

Deletes an S3 object.

## Synopsis

```
rm
<S3Uri>
[--dryrun]
[--quiet]
[--recursive]
[--request-payer <value>]
[--include <value>]
[--exclude <value>]
[--only-show-errors]
[--page-size <value>]
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

`paths` (string)

`--dryrun` (boolean)
Displays the operations that would be performed using the specified command without actually running them.

`--quiet` (boolean)
Does not display the operations performed from the specified command.

`--recursive` (boolean)
Command is performed on all files or objects under the specified directory or prefix.

`--request-payer` (string)
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at [http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html](http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html)

`--include` (string)
Donât exclude files or objects in the command that match the specified pattern. See [Use of Exclude and Include Filters](http://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters) for details.

`--exclude` (string)
Exclude all files or objects from the command that matches the specified pattern.

`--only-show-errors` (boolean)
Only errors and warnings are displayed. All other output is suppressed.

`--page-size` (integer)
The number of results to return in each response to a list operation. The default value is 1000 (the maximum allowed). Using a lower value may help if an operation times out.

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

**Example 1: Delete an S3 object**

The following `rm` command deletes a single s3 object:

```
aws s3 rm s3://amzn-s3-demo-bucket/test2.txt
```

Output:

```
delete: s3://amzn-s3-demo-bucket/test2.txt
```

**Example 2: Delete all contents in a bucket**

The following `rm` command recursively deletes all objects under a specified bucket and prefix when passed with the
parameter `--recursive`.  In this example, the bucket `amzn-s3-demo-bucket` contains the objects `test1.txt` and
`test2.txt`:

```
aws s3 rm s3://amzn-s3-demo-bucket \
    --recursive
```

Output:

```
delete: s3://amzn-s3-demo-bucket/test1.txt
delete: s3://amzn-s3-demo-bucket/test2.txt
```

**Example 3: Delete all contents in a bucket, except ``.jpg`` files**

The following `rm` command recursively deletes all objects under a specified bucket and prefix when passed with the
parameter `--recursive` while excluding some objects by using an `--exclude` parameter.  In this example, the bucket
`amzn-s3-demo-bucket` has the objects `test1.txt` and `test2.jpg`:

```
aws s3 rm s3://amzn-s3-demo-bucket/ \
    --recursive \
    --exclude "*.jpg"
```

Output:

```
delete: s3://amzn-s3-demo-bucket/test1.txt
```

**Example 4: Delete all contents in a bucket, except objects under the specified prefix**

The following `rm` command recursively deletes all objects under a specified bucket and prefix when passed with the
parameter `--recursive` while excluding all objects under a particular prefix by using an `--exclude` parameter.  In
this example, the bucket `amzn-s3-demo-bucket` has the objects `test1.txt` and `another/test.txt`:

```
aws s3 rm s3://amzn-s3-demo-bucket/ \
    --recursive \
    --exclude "another/*"
```

Output:

```
delete: s3://amzn-s3-demo-bucket/test1.txt
```

**Example 5: Delete an object from an S3 access point**

The following `rm` command deletes a single object (`mykey`) from the access point (`myaccesspoint`). ::
The following `rm` command deletes a single object (`mykey`) from the access point (`myaccesspoint`).

```
aws s3 rm s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey
```

Output:

```
delete: s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey
```