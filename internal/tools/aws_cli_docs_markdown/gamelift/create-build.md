# create-buildÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-build.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# create-build

## Description

Creates a new Amazon GameLift build resource for your game server binary files. Combine game server binaries into a zip file for use with Amazon GameLift.

### Warning

When setting up a new game build for Amazon GameLift, we recommend using the CLI command ** [upload-build](https://docs.aws.amazon.com/cli/latest/reference/gamelift/upload-build.html) ** . This helper command combines two tasks: (1) it uploads your build files from a file directory to an Amazon GameLift Amazon S3 location, and (2) it creates a new build resource.

You can use the `CreateBuild` operation in the following scenarios:

- Create a new game build with build files that are in an Amazon S3 location under an Amazon Web Services account that you control. To use this option, you give Amazon GameLift access to the Amazon S3 bucket. With permissions in place, specify a build name, operating system, and the Amazon S3 storage location of your game build.
- Upload your build files to a Amazon GameLift Amazon S3 location. To use this option, specify a build name and operating system. This operation creates a new build resource and also returns an Amazon S3 location with temporary access credentials. Use the credentials to manually upload your build files to the specified Amazon S3 location. For more information, see [Uploading Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html) in the *Amazon S3 Developer Guide* . After you upload build files to the Amazon GameLift Amazon S3 location, you canât update them.

If successful, this operation creates a new build resource with a unique build ID and places it in `INITIALIZED` status. A build must be in `READY` status before you can create fleets with it.

**Learn more**

[Uploading Your Game](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html)

[Create a Build with Files in Amazon S3](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build)

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateBuild)

## Synopsis

```
create-build
[--name <value>]
[--storage-location <value>]
[--operating-system <value>]
[--tags <value>]
[--server-sdk-version <value>]
[--build-version <value>]
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

A descriptive label that is associated with a build. Build names do not need to be unique. You can change this value later.

`--storage-location` (structure)

Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.

If a `StorageLocation` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift will report a `SizeOnDisk` of 0.

Bucket -> (string)

An Amazon S3 bucket identifier. Thename of the S3 bucket.

### Note

Amazon GameLift doesnât support uploading from Amazon S3 buckets with names that contain a dot (.).

Key -> (string)

The name of the zip file that contains the build files or script files.

RoleArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion -> (string)

The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.

Shorthand Syntax:

```
Bucket=string,Key=string,RoleArn=string,ObjectVersion=string
```

JSON Syntax:

```
{
  "Bucket": "string",
  "Key": "string",
  "RoleArn": "string",
  "ObjectVersion": "string"
}
```

`--operating-system` (string)

The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You canât change a buildâs operating system later.

### Note

Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/) . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)

Possible values:

- `WINDOWS_2012`
- `AMAZON_LINUX`
- `AMAZON_LINUX_2`
- `WINDOWS_2016`
- `AMAZON_LINUX_2023`

`--tags` (list)

A list of labels to assign to the new build resource. Tags are developer defined key-value pairs. Tagging Amazon Web Services resources are useful for resource management, access management and cost allocation. For more information, see [Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* . Once the resource is created, you can use [TagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html) , [UntagResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html) , and [ListTagsForResource](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html) to add, remove, and view tags. The maximum tag limit may be lower than stated. See the Amazon Web Services General Reference for actual tagging limits.

(structure)

A label that you can assign to a Amazon GameLift resource.

**Learn more**

[Tagging Amazon Web Services Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference*

[Amazon Web Services Tagging Strategies](http://aws.amazon.com/answers/account-management/aws-tagging-strategies/)

**Related actions**

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

Key -> (string)

The key for a developer-defined key value pair for tagging an Amazon Web Services resource.

Value -> (string)

The value for a developer-defined key value pair for tagging an Amazon Web Services resource.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--server-sdk-version` (string)

A server SDK version you used when integrating your game server build with Amazon GameLift. For more information see [Integrate games with custom game servers](https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html) . By default Amazon GameLift sets this value to `4.0.2` .

`--build-version` (string)

Version information that is associated with a build or script. Version strings do not need to be unique. You can change this value later.

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

**Example1: To create a game build from files in an S3 bucket**

The following `create-build` example creates a custom game build resource. It uses zipped files that are stored in an S3 location in an AWS account that you control. This example assumes that youâve already created an IAM role that gives Amazon GameLift permission to access the S3 location. Since the request does not specify an operating system, the new build resource defaults to WINDOWS_2012.

```
aws gamelift create-build \
    --storage-location file://storage-loc.json \
    --name MegaFrogRaceServer.NA \
    --build-version 12345.678
```

Contents of `storage-loc.json`:

```
{
    "Bucket":"MegaFrogRaceServer_NA_build_files"
    "Key":"MegaFrogRaceServer_build_123.zip"
    "RoleArn":"arn:aws:iam::123456789012:role/gamelift"
}
```

Output:

```
{
    "Build": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreationTime": 1496708916.18,
        "Name": "MegaFrogRaceServer.NA",
        "OperatingSystem": "WINDOWS_2012",
        "SizeOnDisk": 479303,
        "Status": "INITIALIZED",
        "Version": "12345.678"
    },
    "StorageLocation": {
        "Bucket": "MegaFrogRaceServer_NA_build_files",
        "Key": "MegaFrogRaceServer_build_123.zip"
    }
}
```

**Example2: To create a game build resource for manually uploading files to GameLift**

The following `create-build` example creates a new build resource. It also gets a storage location and temporary credentials that allow you to manually upload your game build to the GameLift location in Amazon S3. Once youâve successfully uploaded your build, the GameLift service validates the build and updates the new buildâs status.

```
aws gamelift create-build \
    --name MegaFrogRaceServer.NA \
    --build-version 12345.678 \
    --operating-system AMAZON_LINUX
```

Output:

```
{
    "Build": {
        "BuildArn": "arn:aws:gamelift:us-west-2::build/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "BuildId": "build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreationTime": 1496708916.18,
        "Name": "MegaFrogRaceServer.NA",
        "OperatingSystem": "AMAZON_LINUX",
        "SizeOnDisk": 0,
        "Status": "INITIALIZED",
        "Version": "12345.678"
    },
    "StorageLocation": {
        "Bucket": "gamelift-builds-us-west-2",
        "Key": "123456789012/build-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    },
    "UploadCredentials": {
        "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        "SessionToken": "AgoGb3JpZ2luENz...EXAMPLETOKEN=="
    }
}
```

For more information, see [Upload a Custom Server Build to GameLift](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html) in the *Amazon GameLift Developer Guide*.

## Output

Build -> (structure)

The newly created build resource, including a unique build IDs and status.

BuildId -> (string)

A unique identifier for the build.

BuildArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift build resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::build/build-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` . In a GameLift build ARN, the resource ID matches the *BuildId* value.

Name -> (string)

A descriptive label that is associated with a build. Build names do not need to be unique. It can be set using [CreateBuild](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html) or [UpdateBuild](https://docs.aws.amazon.com/gamelift/latest/apireference/UpdateBuild) .

Version -> (string)

Version information that is associated with a build or script. Version strings do not need to be unique.

Status -> (string)

Current status of the build.

Possible build statuses include the following:

- **INITIALIZED** â A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value.
- **READY** â The game build has been successfully uploaded. You can now create new fleets for this build.
- **FAILED** â The game build upload failed. You cannot create new fleets for this build.

SizeOnDisk -> (long)

File size of the uploaded game build, expressed in bytes. When the build status is `INITIALIZED` or when using a custom Amazon S3 storage location, this value is 0.

OperatingSystem -> (string)

Operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build.

### Note

Amazon Linux 2 (AL2) will reach end of support on 6/30/2025. See more details in the [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/) . For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

ServerSdkVersion -> (string)

The Amazon GameLift Server SDK version used to develop your game server.

UploadCredentials -> (structure)

This element is returned only when the operation is called without a storage location. It contains credentials to use when you are uploading a build file to an Amazon S3 bucket that is owned by Amazon GameLift. Credentials have a limited life span. To refresh these credentials, call [RequestUploadCredentials](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html) .

AccessKeyId -> (string)

The access key ID that identifies the temporary security credentials.

SecretAccessKey -> (string)

The secret access key that can be used to sign requests.

SessionToken -> (string)

The token that users must pass to the service API to use the temporary credentials.

StorageLocation -> (structure)

Amazon S3 location for your game build file, including bucket name and key.

Bucket -> (string)

An Amazon S3 bucket identifier. Thename of the S3 bucket.

### Note

Amazon GameLift doesnât support uploading from Amazon S3 buckets with names that contain a dot (.).

Key -> (string)

The name of the zip file that contains the build files or script files.

RoleArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

ObjectVersion -> (string)

The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.