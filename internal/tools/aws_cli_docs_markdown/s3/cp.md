# cpÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [s3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html#cli-aws-s3) ]

# cp

## Description

Copies a local file or S3 object to another location locally or in S3.

## Synopsis

```
cp
<LocalPath> <S3Uri> or <S3Uri> <LocalPath> or <S3Uri> <S3Uri>
[--dryrun]
[--quiet]
[--include <value>]
[--exclude <value>]
[--acl <value>]
[--follow-symlinks | --no-follow-symlinks]
[--no-guess-mime-type]
[--sse <value>]
[--sse-c <value>]
[--sse-c-key <value>]
[--sse-kms-key-id <value>]
[--sse-c-copy-source <value>]
[--sse-c-copy-source-key <value>]
[--storage-class <value>]
[--grants <value> [<value>...]]
[--website-redirect <value>]
[--content-type <value>]
[--cache-control <value>]
[--content-disposition <value>]
[--content-encoding <value>]
[--content-language <value>]
[--expires <value>]
[--source-region <value>]
[--only-show-errors]
[--no-progress]
[--page-size <value>]
[--ignore-glacier-warnings]
[--force-glacier-transfer]
[--request-payer <value>]
[--checksum-mode <value>]
[--checksum-algorithm <value>]
[--metadata <value>]
[--copy-props <value>]
[--metadata-directive <value>]
[--expected-size <value>]
[--recursive]
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

`--include` (string)
Donât exclude files or objects in the command that match the specified pattern. See [Use of Exclude and Include Filters](http://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters) for details.

`--exclude` (string)
Exclude all files or objects from the command that matches the specified pattern.

`--acl` (string)
Sets the ACL for the object when the command is performed. If you use this parameter you must have the âs3:PutObjectAclâ permission included in the list of actions for your IAM policy. Only accepts values of `private`, `public-read`, `public-read-write`, `authenticated-read`, `aws-exec-read`, `bucket-owner-read`, `bucket-owner-full-control` and `log-delivery-write`. See [Canned ACL](http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) for details

`--follow-symlinks` | `--no-follow-symlinks` (boolean)
Symbolic links are followed only when uploading to S3 from the local filesystem. Note that S3 does not support symbolic links, so the contents of the link target are uploaded under the name of the link. When neither `--follow-symlinks` nor `--no-follow-symlinks` is specified, the default is to follow symlinks.

`--no-guess-mime-type` (boolean)
Do not try to guess the mime type for uploaded files. By default the mime type of a file is guessed when it is uploaded.

`--sse` (string)
Specifies server-side encryption of the object in S3. Valid values are `AES256` and `aws:kms`. If the parameter is specified but no value is provided, `AES256` is used.

`--sse-c` (string)
Specifies server-side encryption using customer provided keys of the the object in S3. `AES256` is the only valid value. If the parameter is specified but no value is provided, `AES256` is used. If you provide this value, `--sse-c-key` must be specified as well.

`--sse-c-key` (blob)
The customer-provided encryption key to use to server-side encrypt the object in S3. If you provide this value, `--sse-c` must be specified as well. The key provided should **not** be base64 encoded.

`--sse-kms-key-id` (string)
The customer-managed AWS Key Management Service (KMS) key ID that should be used to server-side encrypt the object in S3. You should only provide this parameter if you are using a customer managed customer master key (CMK) and not the AWS managed KMS CMK.

`--sse-c-copy-source` (string)
This parameter should only be specified when copying an S3 object that was encrypted server-side with a customer-provided key. It specifies the algorithm to use when decrypting the source object. `AES256` is the only valid value. If the parameter is specified but no value is provided, `AES256` is used. If you provide this value, `--sse-c-copy-source-key` must be specified as well.

`--sse-c-copy-source-key` (blob)
This parameter should only be specified when copying an S3 object that was encrypted server-side with a customer-provided key. Specifies the customer-provided encryption key for Amazon S3 to use to decrypt the source object. The encryption key provided must be one that was used when the source object was created. If you provide this value, `--sse-c-copy-source` be specified as well. The key provided should **not** be base64 encoded.

`--storage-class` (string)
The type of storage to use for the object. Valid choices are: STANDARD | REDUCED_REDUNDANCY | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | GLACIER | DEEP_ARCHIVE | GLACIER_IR. Defaults to âSTANDARDâ

`--grants` (string)

Grant specific permissions to individual users or groups. You can supply a list of grants of the form

```
--grants Permission=Grantee_Type=Grantee_ID [Permission=Grantee_Type=Grantee_ID ...]
```

To specify the same permission type for multiple grantees, specify the permission as such as

```
--grants Permission=Grantee_Type=Grantee_ID,Grantee_Type=Grantee_ID,...
```

Each value contains the following elements:

- `Permission` - Specifies the granted permissions, and can be set to read, readacl, writeacl, or full.
- `Grantee_Type` - Specifies how the grantee is to be identified, and can be set to uri or id.
- `Grantee_ID` - Specifies the grantee based on Grantee_Type. The `Grantee_ID` value can be one of:
- **uri** - The groupâs URI. For more information, see [Who Is a Grantee?](http://docs.aws.amazon.com/AmazonS3/latest/dev/ACLOverview.html#SpecifyingGrantee)
- **id** - The accountâs canonical ID

For more information on Amazon S3 access control, see [Access Control](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAuthAccess.html)

`--website-redirect` (string)
If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Amazon S3 stores the value of this header in the object metadata.

`--content-type` (string)
Specify an explicit content type for this operation. This value overrides any guessed mime types.

`--cache-control` (string)
Specifies caching behavior along the request/reply chain.

`--content-disposition` (string)
Specifies presentational information for the object.

`--content-encoding` (string)
Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.

`--content-language` (string)
The language the content is in.

`--expires` (string)
The date and time at which the object is no longer cacheable.

`--source-region` (string)
When transferring objects from an s3 bucket to an s3 bucket, this specifies the region of the source bucket. Note the region specified by `--region` or through configuration of the CLI refers to the region of the destination bucket. If `--source-region` is not specified the region of the source will be the same as the region of the destination bucket.

`--only-show-errors` (boolean)
Only errors and warnings are displayed. All other output is suppressed.

`--no-progress` (boolean)
File transfer progress is not displayed. This flag is only applied when the quiet and only-show-errors flags are not provided.

`--page-size` (integer)
The number of results to return in each response to a list operation. The default value is 1000 (the maximum allowed). Using a lower value may help if an operation times out.

`--ignore-glacier-warnings` (boolean)
Turns off glacier warnings. Warnings about an operation that cannot be performed because it involves copying, downloading, or moving a glacier object will no longer be printed to standard error and will no longer cause the return code of the command to be `2`.

`--force-glacier-transfer` (boolean)
Forces a transfer request on all Glacier objects in a sync or recursive copy.

`--request-payer` (string)
Confirms that the requester knows that they will be charged for the request. Bucket owners need not specify this parameter in their requests. Documentation on downloading objects from requester pays buckets can be found at [http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html](http://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html)

`--checksum-mode` (string)
To retrieve the checksum, this mode must be enabled. If the object has a checksum, it will be verified.

`--checksum-algorithm` (string)
Indicates the algorithm used to create the checksum for the object.

`--metadata` (map)
A map of metadata to store with the objects in S3. This will be applied to every object which is part of this request. In a sync, this means that files which havenât changed wonât receive the new metadata. key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--copy-props` (string)
Determines which properties are copied from the source S3 object. This parameter only applies for S3 to S3 copies. Valid values are:

- `none` - Do not copy any of the properties from the source S3 object.
- `metadata-directive` - Copies the following properties from the source S3 object: `content-type`, `content-language`, `content-encoding`, `content-disposition`, `cache-control`, `--expires`, and `metadata`
- `default` - The default value. Copies tags and properties covered under the `metadata-directive` value from the source S3 object.

In order to copy the appropriate properties for multipart copies, some of the options may require additional API calls if a multipart copy is involved. Specifically:

- `metadata-directive` may require additional `HeadObject` API calls.
- `default` may require additional `HeadObject`, `GetObjectTagging`, and `PutObjectTagging` API calls. Note this list of API calls may grow in the future in order to ensure multipart copies preserve the exact properties a `CopyObject` API call would preserve.

If you want to guarantee no additional API calls are made other than than the ones needed to perform the actual copy, set this option to `none`.

`--metadata-directive` (string)
Sets the `x-amz-metadata-directive` header for CopyObject operations. It is recommended to use the `--copy-props` parameter instead to control copying of metadata properties. If `--metadata-directive` is set, the `--copy-props` parameter will be disabled and will have no affect on the transfer.

`--expected-size` (string)
This argument specifies the expected size of a stream in terms of bytes. Note that this argument is needed only when a stream is being uploaded to s3 and the size is larger than 50GB. Failure to include this argument under these conditions may result in a failed upload due to too many parts in upload.

`--recursive` (boolean)
Command is performed on all files or objects under the specified directory or prefix.

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

**Example 1: Copying a local file to S3**

The following `cp` command copies a single file to a specified
bucket and key:

```
aws s3 cp test.txt s3://amzn-s3-demo-bucket/test2.txt
```

Output:

```
upload: test.txt to s3://amzn-s3-demo-bucket/test2.txt
```

**Example 2: Copying a local file to S3 with an expiration date**

The following `cp` command copies a single file to a specified
bucket and key that expires at the specified ISO 8601 timestamp:

```
aws s3 cp test.txt s3://amzn-s3-demo-bucket/test2.txt \
    --expires 2014-10-01T20:30:00Z
```

Output:

```
upload: test.txt to s3://amzn-s3-demo-bucket/test2.txt
```

**Example 3: Copying a file from S3 to S3**

The following `cp` command copies a single s3 object to a specified bucket and key:

```
aws s3 cp s3://amzn-s3-demo-bucket/test.txt s3://amzn-s3-demo-bucket/test2.txt
```

Output:

```
copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket/test2.txt
```

**Example 4: Copying an S3 object to a local file**

The following `cp` command copies a single object to a specified file locally:

```
aws s3 cp s3://amzn-s3-demo-bucket/test.txt test2.txt
```

Output:

```
download: s3://amzn-s3-demo-bucket/test.txt to test2.txt
```

**Example 5: Copying an S3 object from one bucket to another**

The following `cp` command copies a single object to a specified bucket while retaining its original name:

```
aws s3 cp s3://amzn-s3-demo-bucket/test.txt s3://amzn-s3-demo-bucket2/
```

Output:

```
copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket2/test.txt
```

**Example 6: Recursively copying S3 objects to a local directory**

When passed with the parameter `--recursive`, the following `cp` command recursively copies all objects under a
specified prefix and bucket to a specified directory.  In this example, the bucket `amzn-s3-demo-bucket` has the objects
`test1.txt` and `test2.txt`:

```
aws s3 cp s3://amzn-s3-demo-bucket . \
    --recursive
```

Output:

```
download: s3://amzn-s3-demo-bucket/test1.txt to test1.txt
download: s3://amzn-s3-demo-bucket/test2.txt to test2.txt
```

**Example 7: Recursively copying local files to S3**

When passed with the parameter `--recursive`, the following `cp` command recursively copies all files under a
specified directory to a specified bucket and prefix while excluding some files by using an `--exclude` parameter.  In
this example, the directory `myDir` has the files `test1.txt` and `test2.jpg`:

```
aws s3 cp myDir s3://amzn-s3-demo-bucket/ \
    --recursive \
    --exclude "*.jpg"
```

Output:

```
upload: myDir/test1.txt to s3://amzn-s3-demo-bucket/test1.txt
```

**Example 8: Recursively copying S3 objects to another bucket**

When passed with the parameter `--recursive`, the following `cp` command recursively copies all objects under a
specified bucket to another bucket while excluding some objects by using an `--exclude` parameter.  In this example,
the bucket `amzn-s3-demo-bucket` has the objects `test1.txt` and `another/test1.txt`:

```
aws s3 cp s3://amzn-s3-demo-bucket/ s3://amzn-s3-demo-bucket2/ \
    --recursive \
    --exclude "another/*"
```

Output:

```
copy: s3://amzn-s3-demo-bucket/test1.txt to s3://amzn-s3-demo-bucket2/test1.txt
```

You can combine `--exclude` and `--include` options to copy only objects that match a pattern, excluding all others:

```
aws s3 cp s3://amzn-s3-demo-bucket/logs/ s3://amzn-s3-demo-bucket2/logs/ \
    --recursive \
    --exclude "*" \
    --include "*.log"
```

Output:

```
copy: s3://amzn-s3-demo-bucket/logs/test/test.log to s3://amzn-s3-demo-bucket2/logs/test/test.log
copy: s3://amzn-s3-demo-bucket/logs/test3.log to s3://amzn-s3-demo-bucket2/logs/test3.log
```

**Example 9: Setting the Access Control List (ACL) while copying an S3 object**

The following `cp` command copies a single object to a specified bucket and key while setting the ACL to
`public-read-write`:

```
aws s3 cp s3://amzn-s3-demo-bucket/test.txt s3://amzn-s3-demo-bucket/test2.txt \
    --acl public-read-write
```

Output:

```
copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket/test2.txt
```

Note that if youâre using the `--acl` option, ensure that any associated IAM
policies include the `"s3:PutObjectAcl"` action:

```
aws iam get-user-policy \
    --user-name myuser \
    --policy-name mypolicy
```

Output:

```
{
    "UserName": "myuser",
    "PolicyName": "mypolicy",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "s3:PutObject",
                    "s3:PutObjectAcl"
                ],
                "Resource": [
                    "arn:aws:s3:::amzn-s3-demo-bucket/*"
                ],
                "Effect": "Allow",
                "Sid": "Stmt1234567891234"
            }
        ]
    }
}
```

**Example 10: Granting permissions for an S3 object**

The following `cp` command illustrates the use of the `--grants` option to grant read access to all users identified
by URI and full control to a specific user identified by their Canonical ID:

```
aws s3 cp file.txt s3://amzn-s3-demo-bucket/ --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers full=id=79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be
```

Output:

```
upload: file.txt to s3://amzn-s3-demo-bucket/file.txt
```

**Example 11: Uploading a local file stream to S3**

### Warning

PowerShell may alter the encoding of or add a CRLF to piped input.

The following `cp` command uploads a local file stream from standard input to a specified bucket and key:

```
aws s3 cp - s3://amzn-s3-demo-bucket/stream.txt
```

**Example 12: Uploading a local file stream that is larger than 50GB to S3**

The following `cp` command uploads a 51GB local file stream from standard input to a specified bucket and key.  The `--expected-size` option must be provided, or the upload may fail when it reaches the default part limit of 10,000:

```
aws s3 cp - s3://amzn-s3-demo-bucket/stream.txt --expected-size 54760833024
```

**Example 13: Downloading an S3 object as a local file stream**

### Warning

PowerShell may alter the encoding of or add a CRLF to piped or redirected output.

The following `cp` command downloads an S3 object locally as a stream to standard output. Downloading as a stream is not currently compatible with the `--recursive` parameter:

```
aws s3 cp s3://amzn-s3-demo-bucket/stream.txt -
```

**Example 14: Uploading to an S3 access point**

The following `cp` command uploads a single file (`mydoc.txt`) to the access point (`myaccesspoint`) at the key (`mykey`):

```
aws s3 cp mydoc.txt s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey
```

Output:

```
upload: mydoc.txt to s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey
```

**Example 15: Downloading from an S3 access point**

The following `cp` command downloads a single object (`mykey`) from the access point (`myaccesspoint`) to the local file (`mydoc.txt`):

```
aws s3 cp s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey mydoc.txt
```

Output:

```
download: s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey to mydoc.txt
```