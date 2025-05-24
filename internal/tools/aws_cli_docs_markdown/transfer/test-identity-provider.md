# test-identity-providerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/test-identity-provider.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/test-identity-provider.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# test-identity-provider

## Description

If the `IdentityProviderType` of a file transfer protocol-enabled server is `AWS_DIRECTORY_SERVICE` or `API_Gateway` , tests whether your identity provider is set up successfully. We highly recommend that you call this operation to test your authentication method as soon as you create your server. By doing so, you can troubleshoot issues with the identity provider integration to ensure that your users can successfully use the service.

The `ServerId` and `UserName` parameters are required. The `ServerProtocol` , `SourceIp` , and `UserPassword` are all optional.

Note the following:

- You cannot use `TestIdentityProvider` if the `IdentityProviderType` of your server is `SERVICE_MANAGED` .
- `TestIdentityProvider` does not work with keys: it only accepts passwords.
- `TestIdentityProvider` can test the password operation for a custom Identity Provider that handles keys and passwords.
- If you provide any incorrect values for any parameters, the `Response` field is empty.
- If you provide a server ID for a server that uses service-managed users, you get an error:   `An error occurred (InvalidRequestException) when calling the TestIdentityProvider operation: s-*server-ID* not configured for external auth`
- If you enter a Server ID for the `--server-id` parameter that does not identify an actual Transfer server, you receive the following error:   `An error occurred (ResourceNotFoundException) when calling the TestIdentityProvider operation: Unknown server` .  It is possible your sever is in a different region. You can specify a region by adding the following: `--region region-code` , such as `--region us-east-2` to specify a server in **US East (Ohio)** .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/TestIdentityProvider)

## Synopsis

```
test-identity-provider
--server-id <value>
[--server-protocol <value>]
[--source-ip <value>]
--user-name <value>
[--user-password <value>]
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

`--server-id` (string)

A system-assigned identifier for a specific server. That serverâs user authentication method is tested with a user name and password.

`--server-protocol` (string)

The type of file transfer protocol to be tested.

The available protocols are:

- Secure Shell (SSH) File Transfer Protocol (SFTP)
- File Transfer Protocol Secure (FTPS)
- File Transfer Protocol (FTP)
- Applicability Statement 2 (AS2)

Possible values:

- `SFTP`
- `FTP`
- `FTPS`
- `AS2`

`--source-ip` (string)

The source IP address of the account to be tested.

`--user-name` (string)

The name of the account to be tested.

`--user-password` (string)

The password of the account to be tested.

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

Response -> (string)

The response that is returned from your API Gateway or your Lambda function.

StatusCode -> (integer)

The HTTP status code that is the response from your API Gateway or your Lambda function.

Message -> (string)

A message that indicates whether the test was successful or not.

### Note

If an empty string is returned, the most likely cause is that the authentication failed due to an incorrect username or password.

Url -> (string)

The endpoint of the service used to authenticate a user.