# create-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/create-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sso-admin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso-admin/index.html#cli-aws-sso-admin) ]

# create-application

## Description

Creates an OAuth 2.0 customer managed application in IAM Identity Center for the given application provider.

### Note

This API does not support creating SAML 2.0 customer managed applications or Amazon Web Services managed applications. To learn how to create an Amazon Web Services managed application, see the application user guide. You can create a SAML 2.0 customer managed application in the Amazon Web Services Management Console only. See [Setting up customer managed SAML 2.0 applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-setup.html) . For more information on these application types, see [Amazon Web Services managed applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/awsapps.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sso-admin-2020-07-20/CreateApplication)

## Synopsis

```
create-application
--instance-arn <value>
--application-provider-arn <value>
--name <value>
[--description <value>]
[--portal-options <value>]
[--tags <value>]
[--status <value>]
[--client-token <value>]
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

`--instance-arn` (string)

The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://awscli.amazonaws.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

`--application-provider-arn` (string)

The ARN of the application provider under which the operation will run.

`--name` (string)

The name of the .

`--description` (string)

The description of the .

`--portal-options` (structure)

A structure that describes the options for the portal associated with an application.

SignInOptions -> (structure)

A structure that describes the sign-in options for the access portal.

Origin -> (string)

This determines how IAM Identity Center navigates the user to the target application. It can be one of the following values:

- `APPLICATION` : IAM Identity Center redirects the customer to the configured `ApplicationUrl` .
- `IDENTITY_CENTER` : IAM Identity Center uses SAML identity-provider initiated authentication to sign the customer directly into a SAML-based application.

ApplicationUrl -> (string)

The URL that accepts authentication requests for an application. This is a required parameter if the `Origin` parameter is `APPLICATION` .

Visibility -> (string)

Indicates whether this application is visible in the access portal.

Shorthand Syntax:

```
SignInOptions={Origin=string,ApplicationUrl=string},Visibility=string
```

JSON Syntax:

```
{
  "SignInOptions": {
    "Origin": "IDENTITY_CENTER"|"APPLICATION",
    "ApplicationUrl": "string"
  },
  "Visibility": "ENABLED"|"DISABLED"
}
```

`--tags` (list)

Specifies tags to be attached to the application.

(structure)

A set of key-value pairs that are used to manage the resource. Tags can only be applied to permission sets and cannot be applied to corresponding roles that IAM Identity Center creates in Amazon Web Services accounts.

Key -> (string)

The key for the tag.

Value -> (string)

The value of the tag.

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

`--status` (string)

Specifies whether the application is enabled or disabled.

Possible values:

- `ENABLED`
- `DISABLED`

`--client-token` (string)

Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier) .

If you donât provide this value, then Amazon Web Services generates a random one for you.

If you retry the operation with the same `ClientToken` , but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.

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

ApplicationArn -> (string)

Specifies the ARN of the application.