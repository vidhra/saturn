# create-uploadÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-upload.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-upload.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# create-upload

## Description

Uploads an app or test scripts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/CreateUpload)

## Synopsis

```
create-upload
--project-arn <value>
--name <value>
--type <value>
[--content-type <value>]
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

`--project-arn` (string)

The ARN of the project for the upload.

`--name` (string)

The uploadâs file name. The name should not contain any forward slashes (`/` ). If you are uploading an iOS app, the file name must end with the `.ipa` extension. If you are uploading an Android app, the file name must end with the `.apk` extension. For all others, the file name must end with the `.zip` file extension.

`--type` (string)

The uploadâs upload type.

Must be one of the following values:

- ANDROID_APP
- IOS_APP
- WEB_APP
- EXTERNAL_DATA
- APPIUM_JAVA_JUNIT_TEST_PACKAGE
- APPIUM_JAVA_TESTNG_TEST_PACKAGE
- APPIUM_PYTHON_TEST_PACKAGE
- APPIUM_NODE_TEST_PACKAGE
- APPIUM_RUBY_TEST_PACKAGE
- APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
- APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
- APPIUM_WEB_PYTHON_TEST_PACKAGE
- APPIUM_WEB_NODE_TEST_PACKAGE
- APPIUM_WEB_RUBY_TEST_PACKAGE
- INSTRUMENTATION_TEST_PACKAGE
- XCTEST_TEST_PACKAGE
- XCTEST_UI_TEST_PACKAGE
- APPIUM_JAVA_JUNIT_TEST_SPEC
- APPIUM_JAVA_TESTNG_TEST_SPEC
- APPIUM_PYTHON_TEST_SPEC
- APPIUM_NODE_TEST_SPEC
- APPIUM_RUBY_TEST_SPEC
- APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
- APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
- APPIUM_WEB_PYTHON_TEST_SPEC
- APPIUM_WEB_NODE_TEST_SPEC
- APPIUM_WEB_RUBY_TEST_SPEC
- INSTRUMENTATION_TEST_SPEC
- XCTEST_UI_TEST_SPEC

If you call `CreateUpload` with `WEB_APP` specified, AWS Device Farm throws an `ArgumentException` error.

Possible values:

- `ANDROID_APP`
- `IOS_APP`
- `WEB_APP`
- `EXTERNAL_DATA`
- `APPIUM_JAVA_JUNIT_TEST_PACKAGE`
- `APPIUM_JAVA_TESTNG_TEST_PACKAGE`
- `APPIUM_PYTHON_TEST_PACKAGE`
- `APPIUM_NODE_TEST_PACKAGE`
- `APPIUM_RUBY_TEST_PACKAGE`
- `APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE`
- `APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE`
- `APPIUM_WEB_PYTHON_TEST_PACKAGE`
- `APPIUM_WEB_NODE_TEST_PACKAGE`
- `APPIUM_WEB_RUBY_TEST_PACKAGE`
- `CALABASH_TEST_PACKAGE`
- `INSTRUMENTATION_TEST_PACKAGE`
- `UIAUTOMATION_TEST_PACKAGE`
- `UIAUTOMATOR_TEST_PACKAGE`
- `XCTEST_TEST_PACKAGE`
- `XCTEST_UI_TEST_PACKAGE`
- `APPIUM_JAVA_JUNIT_TEST_SPEC`
- `APPIUM_JAVA_TESTNG_TEST_SPEC`
- `APPIUM_PYTHON_TEST_SPEC`
- `APPIUM_NODE_TEST_SPEC`
- `APPIUM_RUBY_TEST_SPEC`
- `APPIUM_WEB_JAVA_JUNIT_TEST_SPEC`
- `APPIUM_WEB_JAVA_TESTNG_TEST_SPEC`
- `APPIUM_WEB_PYTHON_TEST_SPEC`
- `APPIUM_WEB_NODE_TEST_SPEC`
- `APPIUM_WEB_RUBY_TEST_SPEC`
- `INSTRUMENTATION_TEST_SPEC`
- `XCTEST_UI_TEST_SPEC`

`--content-type` (string)

The uploadâs content type (for example, `application/octet-stream` ).

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

**To create an upload**

The following command creates an upload for an Android app:

```
aws devicefarm create-upload --project-arn "arn:aws:devicefarm:us-west-2:123456789012:project:070fc3ca-7ec1-4741-9c1f-d3e044efc506" --name app.apk --type ANDROID_APP
```

You can get the project ARN from the output of create-project or list-projects.

Output:

```
{
    "upload": {
        "status": "INITIALIZED",
        "name": "app.apk",
        "created": 1503614408.769,
        "url": "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aproject%3A070fc3ca-c7e1-4471-91cf-d3e4efc50604/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aupload%3A070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514/app.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170824T224008Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAEXAMPLEPBUMBC3GA%2F20170824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=05050370c38894ef5bd09f5d009f36fc8f96fa4bb04e1bba9aca71b8dbe49a0f",
        "type": "ANDROID_APP",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:upload:070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514"
    }
}
```

Use the signed URL in the output to upload a file to Device Farm:

```
curl -T app.apk "https://prod-us-west-2-uploads.s3-us-west-2.amazonaws.com/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aproject%3A070fc3ca-c7e1-4471-91cf-d3e4efc50604/uploads/arn%3Aaws%3Adevicefarm%3Aus-west-2%3A123456789012%3Aupload%3A070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514/app.apk?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170824T224008Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAEXAMPLEPBUMBC3GA%2F20170824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=05050370c38894ef5bd09f5d009f36fc8f96fa4bb04e1bba9aca71b8dbe49a0f"
```

## Output

upload -> (structure)

The newly created upload.

arn -> (string)

The uploadâs ARN.

name -> (string)

The uploadâs file name.

created -> (timestamp)

When the upload was created.

type -> (string)

The uploadâs type.

Must be one of the following values:

- ANDROID_APP
- IOS_APP
- WEB_APP
- EXTERNAL_DATA
- APPIUM_JAVA_JUNIT_TEST_PACKAGE
- APPIUM_JAVA_TESTNG_TEST_PACKAGE
- APPIUM_PYTHON_TEST_PACKAGE
- APPIUM_NODE_TEST_PACKAGE
- APPIUM_RUBY_TEST_PACKAGE
- APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE
- APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE
- APPIUM_WEB_PYTHON_TEST_PACKAGE
- APPIUM_WEB_NODE_TEST_PACKAGE
- APPIUM_WEB_RUBY_TEST_PACKAGE
- INSTRUMENTATION_TEST_PACKAGE
- XCTEST_TEST_PACKAGE
- XCTEST_UI_TEST_PACKAGE
- APPIUM_JAVA_JUNIT_TEST_SPEC
- APPIUM_JAVA_TESTNG_TEST_SPEC
- APPIUM_PYTHON_TEST_SPEC
- APPIUM_NODE_TEST_SPEC
- APPIUM_RUBY_TEST_SPEC
- APPIUM_WEB_JAVA_JUNIT_TEST_SPEC
- APPIUM_WEB_JAVA_TESTNG_TEST_SPEC
- APPIUM_WEB_PYTHON_TEST_SPEC
- APPIUM_WEB_NODE_TEST_SPEC
- APPIUM_WEB_RUBY_TEST_SPEC
- INSTRUMENTATION_TEST_SPEC
- XCTEST_UI_TEST_SPEC

status -> (string)

The uploadâs status.

Must be one of the following values:

- FAILED
- INITIALIZED
- PROCESSING
- SUCCEEDED

url -> (string)

The presigned Amazon S3 URL that was used to store a file using a PUT request.

metadata -> (string)

The uploadâs metadata. For example, for Android, this contains information that is parsed from the manifest and is displayed in the AWS Device Farm console after the associated app is uploaded.

contentType -> (string)

The uploadâs content type (for example, `application/octet-stream` ).

message -> (string)

A message about the uploadâs result.

category -> (string)

The uploadâs category. Allowed values include:

- CURATED: An upload managed by AWS Device Farm.
- PRIVATE: An upload managed by the AWS Device Farm customer.