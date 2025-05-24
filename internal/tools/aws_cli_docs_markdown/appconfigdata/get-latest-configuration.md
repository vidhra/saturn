# get-latest-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/get-latest-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/get-latest-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appconfigdata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfigdata/index.html#cli-aws-appconfigdata) ]

# get-latest-configuration

## Description

Retrieves the latest deployed configuration. This API may return empty configuration data if the client already has the latest version. For more information about this API action and to view example CLI commands that show how to use it with the  StartConfigurationSession API action, see [Retrieving the configuration](http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration) in the *AppConfig User Guide* .

### Warning

Note the following important information.

- Each configuration token is only valid for one call to `GetLatestConfiguration` . The `GetLatestConfiguration` response includes a `NextPollConfigurationToken` that should always replace the token used for the just-completed call in preparation for the next one.
- `GetLatestConfiguration` is a priced call. For more information, see [Pricing](https://aws.amazon.com/systems-manager/pricing/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appconfigdata-2021-11-11/GetLatestConfiguration)

## Synopsis

```
get-latest-configuration
--configuration-token <value>
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

`--configuration-token` (string)

Token describing the current state of the configuration session. To obtain a token, first call the  StartConfigurationSession API. Note that every call to `GetLatestConfiguration` will return a new `ConfigurationToken` (`NextPollConfigurationToken` in the response) and *must* be provided to subsequent `GetLatestConfiguration` API calls.

### Warning

This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException` .

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

## Output

NextPollConfigurationToken -> (string)

The latest token describing the current state of the configuration session. This *must* be provided to the next call to `GetLatestConfiguration.`

### Warning

This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a `GetLatestConfiguration` call uses an expired token, the system returns `BadRequestException` .

NextPollIntervalInSeconds -> (integer)

The amount of time the client should wait before polling for configuration updates again. Use `RequiredMinimumPollIntervalInSeconds` to set the desired poll interval.

ContentType -> (string)

A standard MIME type describing the format of the configuration content.

Configuration -> (blob)

The data of the configuration. This may be empty if the client already has the latest version of configuration.

VersionLabel -> (string)

The user-defined label for the AppConfig hosted configuration version. This attribute doesnât apply if the configuration is not from an AppConfig hosted configuration version. If the client already has the latest version of the configuration data, this value is empty.