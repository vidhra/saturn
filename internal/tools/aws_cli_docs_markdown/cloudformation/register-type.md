# register-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/register-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/register-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# register-type

## Description

Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:

- Validating the extension schema.
- Determining which handlers, if any, have been specified for the extension.
- Making the extension available for use in your account.

For more information about how to develop extensions and ready them for registration, see [Creating resource types using the CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html) in the *CloudFormation Command Line Interface (CLI) User Guide* .

You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per Region. Use [DeregisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html) to deregister specific extension versions if necessary.

Once you have initiated a registration request using  RegisterType , you can use  DescribeTypeRegistration to monitor the progress of the registration request.

Once you have registered a private extension in your account and Region, use [SetTypeConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html) to specify configuration properties for the extension. For more information, see [Edit configuration data for extensions in your account](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html) in the *CloudFormation User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RegisterType)

## Synopsis

```
register-type
[--type <value>]
--type-name <value>
--schema-handler-package <value>
[--logging-config <value>]
[--execution-role-arn <value>]
[--client-request-token <value>]
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

`--type` (string)

The kind of extension.

Possible values:

- `RESOURCE`
- `MODULE`
- `HOOK`

`--type-name` (string)

The name of the extension being registered.

We suggest that extension names adhere to the following patterns:

- For resource types, `company_or_organization::service::type` .
- For modules, `company_or_organization::service::type::MODULE` .
- For Hooks, `MyCompany::Testing::MyTestHook` .

### Note

The following organization namespaces are reserved and canât be used in your extension names:

- `Alexa`
- `AMZN`
- `Amazon`
- `AWS`
- `Custom`
- `Dev`

`--schema-handler-package` (string)

A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.

For information about generating a schema handler package for the extension you want to register, see [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html) in the *CloudFormation Command Line Interface (CLI) User Guide* .

### Note

The user registering the extension must be able to access the package in the S3 bucket. Thatâs, the user needs to have [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) permissions for the schema handler package. For more information, see [Actions, Resources, and Condition Keys for Amazon S3](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html) in the *Identity and Access Management User Guide* .

`--logging-config` (structure)

Specifies logging configuration information for an extension.

LogRoleArn -> (string)

The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.

LogGroupName -> (string)

The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extensionâs handlers.

Shorthand Syntax:

```
LogRoleArn=string,LogGroupName=string
```

JSON Syntax:

```
{
  "LogRoleArn": "string",
  "LogGroupName": "string"
}
```

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.

For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principal (`resources.cloudformation.amazonaws.com` ). For more information about adding trust relationships, see [Modifying a role trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy) in the *Identity and Access Management User Guide* .

If your extension calls Amazon Web Services APIs in any of its handlers, you must create an * [IAM execution role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) * that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.

`--client-request-token` (string)

A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.

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

**To register a resource type**

The following `register-type` example registers the specified resource type as a private resource type in the userâs account.

```
aws cloudformation register-type \
    --type-name My::Organization::ResourceName \
    --schema-handler-package s3://bucket_name/my-organization-resource_name.zip \
    --type RESOURCE
```

Output:

```
{
    "RegistrationToken": "f5525280-104e-4d35-bef5-8f1f1example"
}
```

For more information, see [Registering Resource Providers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-register.html) in the *CloudFormation Command Line Interface User Guide for Type Development*.

## Output

RegistrationToken -> (string)

The identifier for this registration request.

Use this registration token when calling  DescribeTypeRegistration , which returns information about the status and IDs of the extension registration.