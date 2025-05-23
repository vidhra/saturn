# modify-image-attributeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-image-attribute

## Description

Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time.

To specify the attribute, you can use the `Attribute` parameter, or one of the following parameters: `Description` , `ImdsSupport` , or `LaunchPermission` .

Images with an Amazon Web Services Marketplace product code cannot be made public.

To enable the SriovNetSupport enhanced networking attribute of an image, enable SriovNetSupport on an instance and create an AMI from the instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyImageAttribute)

## Synopsis

```
modify-image-attribute
[--attribute <value>]
[--description <value>]
--image-id <value>
[--launch-permission <value>]
[--operation-type <value>]
[--product-codes <value>]
[--user-groups <value>]
[--user-ids <value>]
[--value <value>]
[--organization-arns <value>]
[--organizational-unit-arns <value>]
[--imds-support <value>]
[--dry-run | --no-dry-run]
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

`--attribute` (string)

The name of the attribute to modify.

Valid values: `description` | `imdsSupport` | `launchPermission`

`--description` (structure)

A new description for the AMI.

Value -> (string)

The attribute value. The value is case-sensitive.

`--image-id` (string)

The ID of the AMI.

`--launch-permission` (structure)

A new launch permission for the AMI.

Add -> (list)

The Amazon Web Services account ID, organization ARN, or OU ARN to add to the list of launch permissions for the AMI.

(structure)

Describes a launch permission.

OrganizationArn -> (string)

The Amazon Resource Name (ARN) of an organization.

OrganizationalUnitArn -> (string)

The Amazon Resource Name (ARN) of an organizational unit (OU).

UserId -> (string)

The Amazon Web Services account ID.

Constraints: Up to 10 000 account IDs can be specified in a single request.

Group -> (string)

The name of the group.

Remove -> (list)

The Amazon Web Services account ID, organization ARN, or OU ARN to remove from the list of launch permissions for the AMI.

(structure)

Describes a launch permission.

OrganizationArn -> (string)

The Amazon Resource Name (ARN) of an organization.

OrganizationalUnitArn -> (string)

The Amazon Resource Name (ARN) of an organizational unit (OU).

UserId -> (string)

The Amazon Web Services account ID.

Constraints: Up to 10 000 account IDs can be specified in a single request.

Group -> (string)

The name of the group.

Shorthand Syntax:

```
Add=[{OrganizationArn=string,OrganizationalUnitArn=string,UserId=string,Group=string},{OrganizationArn=string,OrganizationalUnitArn=string,UserId=string,Group=string}],Remove=[{OrganizationArn=string,OrganizationalUnitArn=string,UserId=string,Group=string},{OrganizationArn=string,OrganizationalUnitArn=string,UserId=string,Group=string}]
```

JSON Syntax:

```
{
  "Add": [
    {
      "OrganizationArn": "string",
      "OrganizationalUnitArn": "string",
      "UserId": "string",
      "Group": "all"
    }
    ...
  ],
  "Remove": [
    {
      "OrganizationArn": "string",
      "OrganizationalUnitArn": "string",
      "UserId": "string",
      "Group": "all"
    }
    ...
  ]
}
```

`--operation-type` (string)

The operation type. This parameter can be used only when the `Attribute` parameter is `launchPermission` .

Possible values:

- `add`
- `remove`

`--product-codes` (list)

Not supported.

(string)

Syntax:

```
"string" "string" ...
```

`--user-groups` (list)

The user groups. This parameter can be used only when the `Attribute` parameter is `launchPermission` .

(string)

Syntax:

```
"string" "string" ...
```

`--user-ids` (list)

The Amazon Web Services account IDs. This parameter can be used only when the `Attribute` parameter is `launchPermission` .

(string)

Syntax:

```
"string" "string" ...
```

`--value` (string)

The value of the attribute being modified. This parameter can be used only when the `Attribute` parameter is `description` or `imdsSupport` .

`--organization-arns` (list)

The Amazon Resource Name (ARN) of an organization. This parameter can be used only when the `Attribute` parameter is `launchPermission` .

(string)

Syntax:

```
"string" "string" ...
```

`--organizational-unit-arns` (list)

The Amazon Resource Name (ARN) of an organizational unit (OU). This parameter can be used only when the `Attribute` parameter is `launchPermission` .

(string)

Syntax:

```
"string" "string" ...
```

`--imds-support` (structure)

Set to `v2.0` to indicate that IMDSv2 is specified in the AMI. Instances launched from this AMI will have `HttpTokens` automatically set to `required` so that, by default, the instance requires that IMDSv2 is used when requesting instance metadata. In addition, `HttpPutResponseHopLimit` is set to `2` . For more information, see [Configure the AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.html#configure-IMDS-new-instances-ami-configuration) in the *Amazon EC2 User Guide* .

### Warning

Do not use this parameter unless your AMI software supports IMDSv2. After you set the value to `v2.0` , you canât undo it. The only way to âresetâ your AMI is to create a new AMI from the underlying snapshot.

Value -> (string)

The attribute value. The value is case-sensitive.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**Example 1: To make an AMI public**

The following `modify-instance-attribute` example makes the specified AMI public.

```
aws ec2 modify-image-attribute \
    --image-id ami-5731123e \
    --launch-permission "Add=[{Group=all}]"
```

This command produces no output.

**Example 2: To make an AMI private**

The following `modify-instance-attribute` example makes the specified AMI private.

```
aws ec2 modify-image-attribute \
    --image-id ami-5731123e \
    --launch-permission "Remove=[{Group=all}]"
```

This command produces no output.

**Example 3: To grant launch permission to an AWS account**

The following `modify-instance-attribute` example grants launch permissions to the specified AWS account.

```
aws ec2 modify-image-attribute \
    --image-id ami-5731123e \
    --launch-permission "Add=[{UserId=123456789012}]"
```

This command produces no output.

**Example 4: To remove launch permission from an AWS account**

The following `modify-instance-attribute` example removes launch permissions from the specified AWS account.

```
aws ec2 modify-image-attribute \
    --image-id ami-5731123e \
    --launch-permission "Remove=[{UserId=123456789012}]"
```

## Output

None