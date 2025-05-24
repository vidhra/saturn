# enable-security-hubÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-security-hub.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-security-hub.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# enable-security-hub

## Description

Enables Security Hub for your account in the current Region or the Region you specify in the request.

When you enable Security Hub, you grant to Security Hub the permissions necessary to gather findings from other services that are integrated with Security Hub.

When you use the `EnableSecurityHub` operation to enable Security Hub, you also automatically enable the following standards:

- Center for Internet Security (CIS) Amazon Web Services Foundations Benchmark v1.2.0
- Amazon Web Services Foundational Security Best Practices

Other standards are not automatically enabled.

To opt out of automatically enabled standards, set `EnableDefaultStandards` to `false` .

After you enable Security Hub, to enable a standard, use the `BatchEnableStandards` operation. To disable a standard, use the `BatchDisableStandards` operation.

To learn more, see the [setup information](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the *Security Hub User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/EnableSecurityHub)

## Synopsis

```
enable-security-hub
[--tags <value>]
[--enable-default-standards | --no-enable-default-standards]
[--control-finding-generator <value>]
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

`--tags` (map)

The tags to add to the hub resource when you enable Security Hub.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--enable-default-standards` | `--no-enable-default-standards` (boolean)

Whether to enable the security standards that Security Hub has designated as automatically enabled. If you donât provide a value for `EnableDefaultStandards` , it is set to `true` . To not enable the automatically enabled standards, set `EnableDefaultStandards` to `false` .

`--control-finding-generator` (string)

This field, used when enabling Security Hub, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to `SECURITY_CONTROL` , Security Hub generates a single finding for a control check even when the check applies to multiple enabled standards.

If the value for this field is set to `STANDARD_CONTROL` , Security Hub generates separate findings for a control check when the check applies to multiple enabled standards.

The value for this field in a member account matches the value in the administrator account. For accounts that arenât part of an organization, the default value of this field is `SECURITY_CONTROL` if you enabled Security Hub on or after February 23, 2023.

Possible values:

- `STANDARD_CONTROL`
- `SECURITY_CONTROL`

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

**To enable AWS Security Hub**

The following `enable-security-hub` example enables AWS Security Hub for the requesting account. It configures Security Hub to enable the default standards. For the hub resource, it assigns the value `Security` to the tag `Department`.

```
aws securityhub enable-security-hub \
    --enable-default-standards \
    --tags '{"Department": "Security"}'
```

This command produces no output.

For more information, see [Enabling Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html#securityhub-enable) in the *AWS Security Hub User Guide*.

## Output

None