# update-application-resource-lifecycleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application-resource-lifecycle.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application-resource-lifecycle.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# update-application-resource-lifecycle

## Description

Modifies lifecycle settings for an application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)

## Synopsis

```
update-application-resource-lifecycle
--application-name <value>
--resource-lifecycle-config <value>
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

`--application-name` (string)

The name of the application.

`--resource-lifecycle-config` (structure)

The lifecycle configuration.

ServiceRole -> (string)

The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

The `ServiceRole` property is required the first time that you provide a `VersionLifecycleConfig` for the application in one of the supporting calls (`CreateApplication` or `UpdateApplicationResourceLifecycle` ). After you provide it once, in either one of the calls, Elastic Beanstalk persists the Service Role with the application, and you donât need to specify it again in subsequent `UpdateApplicationResourceLifecycle` calls. You can, however, specify it in subsequent calls to change the Service Role to another value.

VersionLifecycleConfig -> (structure)

Defines lifecycle settings for application versions.

MaxCountRule -> (structure)

Specify a max count rule to restrict the number of application versions that are retained for an application.

Enabled -> (boolean)

Specify `true` to apply the rule, or `false` to disable it.

MaxCount -> (integer)

Specify the maximum number of application versions to retain.

DeleteSourceFromS3 -> (boolean)

Set to `true` to delete a versionâs source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

MaxAgeRule -> (structure)

Specify a max age rule to restrict the length of time that application versions are retained for an application.

Enabled -> (boolean)

Specify `true` to apply the rule, or `false` to disable it.

MaxAgeInDays -> (integer)

Specify the number of days to retain an application versions.

DeleteSourceFromS3 -> (boolean)

Set to `true` to delete a versionâs source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

Shorthand Syntax:

```
ServiceRole=string,VersionLifecycleConfig={MaxCountRule={Enabled=boolean,MaxCount=integer,DeleteSourceFromS3=boolean},MaxAgeRule={Enabled=boolean,MaxAgeInDays=integer,DeleteSourceFromS3=boolean}}
```

JSON Syntax:

```
{
  "ServiceRole": "string",
  "VersionLifecycleConfig": {
    "MaxCountRule": {
      "Enabled": true|false,
      "MaxCount": integer,
      "DeleteSourceFromS3": true|false
    },
    "MaxAgeRule": {
      "Enabled": true|false,
      "MaxAgeInDays": integer,
      "DeleteSourceFromS3": true|false
    }
  }
}
```

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

ApplicationName -> (string)

The name of the application.

ResourceLifecycleConfig -> (structure)

The lifecycle configuration.

ServiceRole -> (string)

The ARN of an IAM service role that Elastic Beanstalk has permission to assume.

The `ServiceRole` property is required the first time that you provide a `VersionLifecycleConfig` for the application in one of the supporting calls (`CreateApplication` or `UpdateApplicationResourceLifecycle` ). After you provide it once, in either one of the calls, Elastic Beanstalk persists the Service Role with the application, and you donât need to specify it again in subsequent `UpdateApplicationResourceLifecycle` calls. You can, however, specify it in subsequent calls to change the Service Role to another value.

VersionLifecycleConfig -> (structure)

Defines lifecycle settings for application versions.

MaxCountRule -> (structure)

Specify a max count rule to restrict the number of application versions that are retained for an application.

Enabled -> (boolean)

Specify `true` to apply the rule, or `false` to disable it.

MaxCount -> (integer)

Specify the maximum number of application versions to retain.

DeleteSourceFromS3 -> (boolean)

Set to `true` to delete a versionâs source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.

MaxAgeRule -> (structure)

Specify a max age rule to restrict the length of time that application versions are retained for an application.

Enabled -> (boolean)

Specify `true` to apply the rule, or `false` to disable it.

MaxAgeInDays -> (integer)

Specify the number of days to retain an application versions.

DeleteSourceFromS3 -> (boolean)

Set to `true` to delete a versionâs source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.