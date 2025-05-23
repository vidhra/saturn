# get-uploadÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-upload.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-upload.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devicefarm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/index.html#cli-aws-devicefarm) ]

# get-upload

## Description

Gets information about an upload.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devicefarm-2015-06-23/GetUpload)

## Synopsis

```
get-upload
--arn <value>
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

`--arn` (string)

The uploadâs ARN.

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

**To view an upload**

The following command retrieves information about an upload:

```
aws devicefarm get-upload --arn "arn:aws:devicefarm:us-west-2:123456789012:upload:070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514"
```

You can get the upload ARN from the output of `create-upload`.

Output:

```
{
    "upload": {
        "status": "SUCCEEDED",
        "name": "app.apk",
        "created": 1505262773.186,
        "type": "ANDROID_APP",
        "arn": "arn:aws:devicefarm:us-west-2:123456789012:upload:070fc3ca-7ec1-4741-9c1f-d3e044efc506/dd72723a-ae9e-4087-09e6-f4cea3599514",
        "metadata": "{\"device_admin\":false,\"activity_name\":\"ccom.example.client.LauncherActivity\",\"version_name\":\"1.0.2.94\",\"screens\":[\"small\",\"normal\",\"large\",\"xlarge\"],\"error_type\":null,\"sdk_version\":\"16\",\"package_name\":\"com.example.client\",\"version_code\":\"20994\",\"native_code\":[\"armeabi-v7a\"],\"target_sdk_version\":\"25\"}"
    }
}
```

## Output

upload -> (structure)

An app or a set of one or more tests to upload or that have been uploaded.

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