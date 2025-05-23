# add-custom-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/add-custom-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/add-custom-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# add-custom-attributes

## Description

Adds additional user attributes to the user pool schema. Custom attributes can be mutable or immutable and have a `custom:` or `dev:` prefix. For more information, see [Custom attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-custom-attributes) .

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AddCustomAttributes)

## Synopsis

```
add-custom-attributes
--user-pool-id <value>
--custom-attributes <value>
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

The ID of the user pool where you want to add custom attributes.

`--custom-attributes` (list)

An array of custom attribute names and other properties. Sets the following characteristics:

AttributeDataType

The expected data type. Can be a string, a number, a date and time, or a boolean.

Mutable

If true, you can grant app clients write access to the attribute value. If false, the attribute value can only be set up on sign-up or administrator creation of users.

Name

The attribute name. For an attribute like `custom:myAttribute` , enter `myAttribute` for this field.

Required

When true, users who sign up or are created must set a value for the attribute.

NumberAttributeConstraints

The minimum and maximum length of accepted values for a `Number` -type attribute.

StringAttributeConstraints

The minimum and maximum length of accepted values for a `String` -type attribute.

DeveloperOnlyAttribute

This legacy option creates an attribute with a `dev:` prefix. You can only set the value of a developer-only attribute with administrative IAM credentials.

(structure)

A list of the user attributes and their properties in your user pool. The attribute schema contains standard attributes, custom attributes with a `custom:` prefix, and developer attributes with a `dev:` prefix. For more information, see [User pool attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html) .

Developer-only `dev:` attributes are a legacy feature of user pools, and are read-only to all app clients. You can create and update developer-only attributes only with IAM-authenticated API operations. Use app client read/write permissions instead.

Name -> (string)

The name of your user pool attribute. When you create or update a user pool, adding a schema attribute creates a custom or developer-only attribute. When you add an attribute with a `Name` value of `MyAttribute` , Amazon Cognito creates the custom attribute `custom:MyAttribute` . When `DeveloperOnlyAttribute` is `true` , Amazon Cognito creates your attribute as `dev:MyAttribute` . In an operation that describes a user pool, Amazon Cognito returns this value as `value` for standard attributes, `custom:value` for custom attributes, and `dev:value` for developer-only attributes..

AttributeDataType -> (string)

The data format of the values for your attribute. When you choose an `AttributeDataType` , Amazon Cognito validates the input against the data type. A custom attribute value in your userâs ID token is always a string, for example `"custom:isMember" : "true"` or `"custom:YearsAsMember" : "12"` .

DeveloperOnlyAttribute -> (boolean)

### Note

You should use [WriteAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolClientType.html#CognitoUserPools-Type-UserPoolClientType-WriteAttributes) in the user pool client to control how attributes can be mutated for new use cases instead of using `DeveloperOnlyAttribute` .

Specifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users wonât be able to modify this attribute using their access token. For example, `DeveloperOnlyAttribute` can be modified using AdminUpdateUserAttributes but canât be updated using UpdateUserAttributes.

Mutable -> (boolean)

Specifies whether the value of the attribute can be changed.

Any user pool attribute whose value you map from an IdP attribute must be mutable, with a parameter value of `true` . Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see [Specifying Identity Provider Attribute Mappings for Your User Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html) .

Required -> (boolean)

Specifies whether a user pool attribute is required. If the attribute is required and the user doesnât provide a value, registration or sign-in will fail.

NumberAttributeConstraints -> (structure)

Specifies the constraints for an attribute of the number type.

MinValue -> (string)

The minimum value of an attribute that is of the number data type.

MaxValue -> (string)

The maximum length of a number attribute value. Must be a number less than or equal to `2^1023` , represented as a string with a length of 131072 characters or fewer.

StringAttributeConstraints -> (structure)

Specifies the constraints for an attribute of the string type.

MinLength -> (string)

The minimum length of a string attribute value.

MaxLength -> (string)

The maximum length of a string attribute value. Must be a number less than or equal to `2^1023` , represented as a string with a length of 131072 characters or fewer.

Shorthand Syntax:

```
Name=string,AttributeDataType=string,DeveloperOnlyAttribute=boolean,Mutable=boolean,Required=boolean,NumberAttributeConstraints={MinValue=string,MaxValue=string},StringAttributeConstraints={MinLength=string,MaxLength=string} ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "AttributeDataType": "String"|"Number"|"DateTime"|"Boolean",
    "DeveloperOnlyAttribute": true|false,
    "Mutable": true|false,
    "Required": true|false,
    "NumberAttributeConstraints": {
      "MinValue": "string",
      "MaxValue": "string"
    },
    "StringAttributeConstraints": {
      "MinLength": "string",
      "MaxLength": "string"
    }
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To add a custom attribute**

This example adds a custom attribute CustomAttr1 to a user pool. It is a String type,
and requires a minimum of 1 character and a maximum of 15. It is not required.

Command:

```
aws cognito-idp add-custom-attributes --user-pool-id us-west-2_aaaaaaaaa --custom-attributes Name="CustomAttr1",AttributeDataType="String",DeveloperOnlyAttribute=false,Required=false,StringAttributeConstraints="{MinLength=1,MaxLength=15}"
```

## Output

None