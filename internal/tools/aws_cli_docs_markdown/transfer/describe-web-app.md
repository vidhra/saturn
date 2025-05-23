# describe-web-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-web-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/describe-web-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transfer/index.html#cli-aws-transfer) ]

# describe-web-app

## Description

Describes the web app thatâs identified by `WebAppId` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/DescribeWebApp)

## Synopsis

```
describe-web-app
--web-app-id <value>
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

`--web-app-id` (string)

Provide the unique identifier for the web app.

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

WebApp -> (structure)

Returns a structure that contains the details of the web app.

Arn -> (string)

The Amazon Resource Name (ARN) of the web app.

WebAppId -> (string)

The unique identifier for the web app.

DescribedIdentityProviderDetails -> (tagged union structure)

A structure that contains the details for the identity provider used by the web app.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `IdentityCenterConfig`.

IdentityCenterConfig -> (structure)

Returns a structure for your identity provider details. This structure contains the instance ARN and role being used for the web app.

ApplicationArn -> (string)

The Amazon Resource Name (ARN) for the IAM Identity Center application: this value is set automatically when you create your web app.

InstanceArn -> (string)

The Amazon Resource Name (ARN) for the IAM Identity Center used for the web app.

Role -> (string)

The IAM role in IAM Identity Center used for the web app.

AccessEndpoint -> (string)

The `AccessEndpoint` is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.

WebAppEndpoint -> (string)

The `WebAppEndpoint` is the unique URL for your Transfer Family web app. This is the value that you use when you configure **Origins** on CloudFront.

WebAppUnits -> (tagged union structure)

A union that contains the value for number of concurrent connections or the user sessions on your web app.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Provisioned`.

Provisioned -> (integer)

An integer that represents the number of units for your desired number of concurrent connections, or the number of user sessions on your web app at the same time.

Each increment allows an additional 250 concurrent sessions: a value of `1` sets the number of concurrent sessions to 250; `2` sets a value of 500, and so on.

Tags -> (list)

Key-value pairs that can be used to group and search for web apps. Tags are metadata attached to web apps for any purpose.

(structure)

Creates a key-value pair for a specific resource. Tags are metadata that you can use to search for and group a resource for various purposes. You can apply tags to servers, users, and roles. A tag key can take more than one value. For example, to group servers for accounting purposes, you might create a tag called `Group` and assign the values `Research` and `Accounting` to that group.

Key -> (string)

The name assigned to the tag that you create.

Value -> (string)

Contains one or more values that you assigned to the key name you create.

WebAppEndpointPolicy -> (string)

Setting for the type of endpoint policy for the web app. The default value is `STANDARD` .

If your web app was created in an Amazon Web Services GovCloud (US) Region, the value of this parameter can be `FIPS` , which indicates the web app endpoint is FIPS-compliant.