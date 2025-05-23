# get-ui-customizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-ui-customization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-ui-customization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# get-ui-customization

## Description

Given a user pool ID or app client, returns information about classic hosted UI branding that you applied, if any. Returns user-pool level branding information if no app client branding is applied, or if you donât specify an app client ID. Returns an empty object if you havenât applied hosted UI branding to either the client or the user pool. For more information, see [Hosted UI (classic) branding](https://docs.aws.amazon.com/cognito/latest/developerguide/hosted-ui-classic-branding.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/GetUICustomization)

## Synopsis

```
get-ui-customization
--user-pool-id <value>
[--client-id <value>]
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

`--user-pool-id` (string)

The ID of the user pool that you want to query for branding settings.

`--client-id` (string)

The ID of the app client that you want to query for branding settings.

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

**To display the classic hosted UI customization settings for an app client**

The following `get-ui-customization` example displays the classic hosted UI customization settings for an app client that doesnât inherit settings from the user pool.

```
aws cognito-idp get-ui-customization \
    --user-pool-id us-west-2_EXAMPLE \
    --client-id 1example23456789
```

Output:

```
{
    "UICustomization": {
        "UserPoolId": "us-west-2_EXAMPLE",
        "ClientId": "1example23456789",
        "ImageUrl": "https://example.cloudfront.net/us-west-2_EXAMPLE/1example23456789/20250115191928/assets/images/image.jpg",
        "CSS": "\n.logo-customizable {\n  max-width: 80%;\n  max-height: 30%;\n}\n\n.banner-customizable {\n  padding: 25px 0px 25px 0px;\n  background-color: lightgray;\n}\n\n.label-customizable {\n  font-weight: 400;\n}\n\n.textDescription-customizable {\n  padding-top: 100px;\n  padding-bottom: 10px;\n  display: block;\n  font-size: 12px;\n}\n\n.idpDescription-customizable {\n  padding-top: 10px;\n  padding-bottom: 10px;\n  display: block;\n  font-size: 16px;\n}\n\n.legalText-customizable {\n  color: #747474;\n  font-size: 11px;\n}\n\n.submitButton-customizable {\n  font-size: 14px;\n  font-weight: bold;\n  margin: 20px 0px 10px 0px;\n  height: 50px;\n  width: 100%;\n  color: #fff;\n  background-color: #337ab7;\n}\n\n.submitButton-customizable:hover {\n  color: #fff;\n  background-color: #286090;\n}\n\n.errorMessage-customizable {\n  padding: 5px;\n  font-size: 12px;\n  width: 100%;\n  background: #F5F5F5;\n  border: 2px solid #D64958;\n  color: #D64958;\n}\n\n.inputField-customizable {\n  width: 100%;\n  height: 34px;\n  color: #555;\n  background-color: #fff;\n  border: 1px solid #ccc;\n}\n\n.inputField-customizable:focus {\n  border-color: #66afe9;\n  outline: 0;\n}\n\n.idpButton-customizable {\n  height: 40px;\n  width: 100%;\n  width: 100%;\n  text-align: center;\n  margin-bottom: 15px;\n  color: #fff;\n  background-color: #5bc0de;\n  border-color: #46b8da;\n}\n\n.idpButton-customizable:hover {\n  color: #fff;\n  background-color: #31b0d5;\n}\n\n.socialButton-customizable {\n  border-radius: 2px;\n  height: 60px;\n  margin-bottom: 15px;\n  padding: 1px;\n  text-align: left;\n  width: 100%;\n}\n\n.redirect-customizable {\n  text-align: center;\n}\n\n.passwordCheck-notValid-customizable {\n  color: #DF3312;\n}\n\n.passwordCheck-valid-customizable {\n  color: #19BF00;\n}\n\n.background-customizable {\n  background-color: #fff;\n}\n",
        "CSSVersion": "20250115191928"
    }
}
```

For more information, see [Hosted UI (classic) branding](https://docs.aws.amazon.com/cognito/latest/developerguide/hosted-ui-classic-branding.html) in the *Amazon Cognito Developer Guide*.

## Output

UICustomization -> (structure)

Information about the classic hosted UI custom CSS and logo-image branding that you applied to the user pool or app client.

UserPoolId -> (string)

The ID of the user pool with hosted UI customizations.

ClientId -> (string)

The app client ID for your UI customization. When this value isnât present, the customization applies to all user pool app clients that donât have client-level settings..

ImageUrl -> (string)

A URL path to the hosted logo image of your UI customization.

CSS -> (string)

The CSS values in the UI customization.

CSSVersion -> (string)

The CSS version number.

LastModifiedDate -> (timestamp)

The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.

CreationDate -> (timestamp)

The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.