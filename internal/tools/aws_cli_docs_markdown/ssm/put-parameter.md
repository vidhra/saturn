# put-parameterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# put-parameter

## Description

Create or update a parameter in Parameter Store.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/PutParameter)

## Synopsis

```
put-parameter
--name <value>
[--description <value>]
--value <value>
[--type <value>]
[--key-id <value>]
[--overwrite | --no-overwrite]
[--allowed-pattern <value>]
[--tags <value>]
[--tier <value>]
[--policies <value>]
[--data-type <value>]
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

`--name` (string)

The fully qualified name of the parameter that you want to create or update.

### Note

You canât enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.

The fully qualified name includes the complete hierarchy of the parameter path and name. For parameters in a hierarchy, you must include a leading forward slash character (/) when you create or reference a parameter. For example: `/Dev/DBServer/MySQL/db-string13`

Naming Constraints:

- Parameter names are case sensitive.
- A parameter name must be unique within an Amazon Web Services Region
- A parameter name canât be prefixed with â`aws` â or â`ssm` â (case-insensitive).
- Parameter names can include only the following symbols and letters: `a-zA-Z0-9_.-`   In addition, the slash character ( / ) is used to delineate hierarchies in parameter names. For example: `/Dev/Production/East/Project-ABC/MyParameter`
- A parameter name canât include spaces.
- Parameter hierarchies are limited to a maximum depth of fifteen levels.

For additional information about valid values for parameter names, see [Creating Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html) in the *Amazon Web Services Systems Manager User Guide* .

### Note

The reported maximum length of 2048 characters for a parameter name includes 1037 characters that are reserved for internal use by Systems Manager. The maximum length for a parameter name that you specify is 1011 characters.

This count of 1011 characters includes the characters in the ARN that precede the name you specify. This ARN length will vary depending on your partition and Region. For example, the following 45 characters count toward the 1011 character maximum for a parameter created in the US East (Ohio) Region: `arn:aws:ssm:us-east-2:111122223333:parameter/` .

`--description` (string)

Information about the parameter that you want to add to the system. Optional but recommended.

### Warning

Donât enter personally identifiable information in this field.

`--value` (string)

The parameter value that you want to add to the system. Standard parameters have a value limit of 4 KB. Advanced parameters have a value limit of 8 KB.

### Note

Parameters canât be referenced or nested in the values of other parameters. You canât include values wrapped in double brackets `{{}}` or `{{ssm:*parameter-name* }}` in a parameter value.

`--type` (string)

The type of parameter that you want to create.

### Note

`SecureString` isnât currently supported for CloudFormation templates.

Items in a `StringList` must be separated by a comma (,). You canât use other punctuation or special character to escape items in the list. If you have a parameter value that requires a comma, then use the `String` data type.

### Warning

Specifying a parameter type isnât required when updating a parameter. You must specify a parameter type when creating a parameter.

Possible values:

- `String`
- `StringList`
- `SecureString`

`--key-id` (string)

The Key Management Service (KMS) ID that you want to use to encrypt a parameter. Use a custom key for better security. Required for parameters that use the `SecureString` data type.

If you donât specify a key ID, the system uses the default key associated with your Amazon Web Services account, which is not as secure as using a custom key.

- To use a custom KMS key, choose the `SecureString` data type with the `Key ID` parameter.

`--overwrite` | `--no-overwrite` (boolean)

Overwrite an existing parameter. The default value is `false` .

`--allowed-pattern` (string)

A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^d+$

`--tags` (list)

Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter. In this case, you could specify the following key-value pairs:

- `Key=Resource,Value=S3bucket`
- `Key=OS,Value=Windows`
- `Key=ParameterType,Value=LicenseKey`

### Note

To add tags to an existing Systems Manager parameter, use the  AddTagsToResource operation.

(structure)

Metadata that you assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Amazon Web Services Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

Key -> (string)

The name of the tag.

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

`--tier` (string)

The parameter tier to assign to a parameter.

Parameter Store offers a standard tier and an advanced tier for parameters. Standard parameters have a content size limit of 4 KB and canât be configured to use parameter policies. You can create a maximum of 10,000 standard parameters for each Region in an Amazon Web Services account. Standard parameters are offered at no additional cost.

Advanced parameters have a content size limit of 8 KB and can be configured to use parameter policies. You can create a maximum of 100,000 advanced parameters for each Region in an Amazon Web Services account. Advanced parameters incur a charge. For more information, see [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html) in the *Amazon Web Services Systems Manager User Guide* .

You can change a standard parameter to an advanced parameter any time. But you canât revert an advanced parameter to a standard parameter. Reverting an advanced parameter to a standard parameter would result in data loss because the system would truncate the size of the parameter from 8 KB to 4 KB. Reverting would also remove any policies attached to the parameter. Lastly, advanced parameters use a different form of encryption than standard parameters.

If you no longer need an advanced parameter, or if you no longer want to incur charges for an advanced parameter, you must delete it and recreate it as a new standard parameter.

**Using the Default Tier Configuration**

In `PutParameter` requests, you can specify the tier to create the parameter in. Whenever you specify a tier in the request, Parameter Store creates or updates the parameter according to that request. However, if you donât specify a tier in a request, Parameter Store assigns the tier based on the current Parameter Store default tier configuration.

The default tier when you begin using Parameter Store is the standard-parameter tier. If you use the advanced-parameter tier, you can specify one of the following as the default:

- **Advanced** : With this option, Parameter Store evaluates all requests as advanced parameters.
- **Intelligent-Tiering** : With this option, Parameter Store evaluates each request to determine if the parameter is standard or advanced.  If the request doesnât include any options that require an advanced parameter, the parameter is created in the standard-parameter tier. If one or more options requiring an advanced parameter are included in the request, Parameter Store create a parameter in the advanced-parameter tier. This approach helps control your parameter-related costs by always creating standard parameters unless an advanced parameter is necessary.

Options that require an advanced parameter include the following:

- The content size of the parameter is more than 4 KB.
- The parameter uses a parameter policy.
- More than 10,000 parameters already exist in your Amazon Web Services account in the current Amazon Web Services Region.

For more information about configuring the default tier option, see [Specifying a default parameter tier](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html#ps-default-tier) in the *Amazon Web Services Systems Manager User Guide* .

Possible values:

- `Standard`
- `Advanced`
- `Intelligent-Tiering`

`--policies` (string)

One or more policies to apply to a parameter. This operation takes a JSON array. Parameter Store, a tool in Amazon Web Services Systems Manager supports the following policy types:

Expiration: This policy deletes the parameter after it expires. When you create the policy, you specify the expiration date. You can update the expiration date and time by updating the policy. Updating the *parameter* doesnât affect the expiration date and time. When the expiration time is reached, Parameter Store deletes the parameter.

ExpirationNotification: This policy initiates an event in Amazon CloudWatch Events that notifies you about the expiration. By using this policy, you can receive notification before or after the expiration time is reached, in units of days or hours.

NoChangeNotification: This policy initiates a CloudWatch Events event if a parameter hasnât been modified for a specified period of time. This policy type is useful when, for example, a secret needs to be changed within a period of time, but it hasnât been changed.

All existing policies are preserved until you send new policies or an empty policy. For more information about parameter policies, see [Assigning parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) .

`--data-type` (string)

The data type for a `String` parameter. Supported data types include plain text and Amazon Machine Image (AMI) IDs.

**The following data type values are supported.**

- `text`
- `aws:ec2:image`
- `aws:ssm:integration`

When you create a `String` parameter and specify `aws:ec2:image` , Amazon Web Services Systems Manager validates the parameter value is in the required format, such as `ami-12345abcdeEXAMPLE` , and that the specified AMI is available in your Amazon Web Services account.

### Note

If the action is successful, the service sends back an HTTP 200 response which indicates a successful `PutParameter` call for all cases except for data type `aws:ec2:image` . If you call `PutParameter` with `aws:ec2:image` data type, a successful HTTP 200 response does not guarantee that your parameter was successfully created or updated. The `aws:ec2:image` value is validated asynchronously, and the `PutParameter` call returns before the validation is complete. If you submit an invalid AMI value, the PutParameter operation will return success, but the asynchronous validation will fail and the parameter will not be created or updated. To monitor whether your `aws:ec2:image` parameters are created successfully, see [Setting up notifications or trigger actions based on Parameter Store events](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-cwe.html) . For more information about AMI format validation , see [Native parameter support for Amazon Machine Image IDs](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-ec2-aliases.html) .

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

**Example 1: To change a parameter value**

The following `put-parameter` example changes the value of the specified parameter.

```
aws ssm put-parameter \
    --name "MyStringParameter" \
    --type "String" \
    --value "Vici" \
    --overwrite
```

Output:

```
{
    "Version": 2,
    "Tier": "Standard"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html), [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and [Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the *AWS Systems Manager User Guide*.

**Example 2: To create an advanced parameter**

The following `put-parameter` example creates an advanced parameter.

```
aws ssm put-parameter \
    --name "MyAdvancedParameter" \
    --description "This is an advanced parameter" \
    --value "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat [truncated]" \
    --type "String" \
    --tier Advanced
```

Output:

```
{
    "Version": 1,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html), [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and [Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the *AWS Systems Manager User Guide*.

**Example 3: To convert a standard parameter to an advanced parameter**

The following `put-parameter` example converts an existing standard parameter into an advanced parameter.

```
aws ssm put-parameter \
    --name "MyConvertedParameter" \
    --value "abc123" \
    --type "String" \
    --tier Advanced \
    --overwrite
```

Output:

```
{
    "Version": 2,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html), [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and [Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the *AWS Systems Manager User Guide*.

**Example 4: To create a parameter with a policy attached**

The following `put-parameter` example creates an advanced parameter with a parameter policy attached.

```
aws ssm put-parameter \
    --name "/Finance/Payroll/q2accesskey" \
    --value "P@sSwW)rd" \
    --type "SecureString" \
    --tier Advanced \
    --policies "[{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-06-30T00:00:00.000Z\"}},{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"5\",\"Unit\":\"Days\"}},{\"Type\":\"NoChangeNotification\",\"Version\":\"1.0\",\"Attributes\":{\"After\":\"60\",\"Unit\":\"Days\"}}]"
```

Output:

```
{
    "Version": 1,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html), [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and [Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the *AWS Systems Manager User Guide*.

**Example 5: To add a policy to an existing parameter**

The following `put-parameter` example attaches a policy to an existing advanced parameter.

```
aws ssm put-parameter \
    --name "/Finance/Payroll/q2accesskey" \
    --value "N3wP@sSwW)rd" \
    --type "SecureString" \
    --tier Advanced \
    --policies "[{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-06-30T00:00:00.000Z\"}},{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"5\",\"Unit\":\"Days\"}},{\"Type\":\"NoChangeNotification\",\"Version\":\"1.0\",\"Attributes\":{\"After\":\"60\",\"Unit\":\"Days\"}}]"
    --overwrite
```

Output:

```
{
    "Version": 2,
    "Tier": "Advanced"
}
```

For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html), [Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and [Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html) in the *AWS Systems Manager User Guide*.

## Output

Version -> (long)

The new version number of a parameter. If you edit a parameter value, Parameter Store automatically creates a new version and assigns this new version a unique ID. You can reference a parameter version ID in API operations or in Systems Manager documents (SSM documents). By default, if you donât specify a specific version, the system returns the latest parameter value when a parameter is called.

Tier -> (string)

The tier assigned to the parameter.