# associate-principal-with-portfolioÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# associate-principal-with-portfolio

## Description

Associates the specified principal ARN with the specified portfolio.

If you share the portfolio with principal name sharing enabled, the `PrincipalARN` association is included in the share.

The `PortfolioID` , `PrincipalARN` , and `PrincipalType` parameters are required.

You can associate a maximum of 10 Principals with a portfolio using `PrincipalType` as `IAM_PATTERN` .

### Note

When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is *not* an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using `PrincipalType` as `IAM` . With this configuration, the `PrincipalARN` must already exist in the recipient account before it can be associated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio)

## Synopsis

```
associate-principal-with-portfolio
[--accept-language <value>]
--portfolio-id <value>
--principal-arn <value>
--principal-type <value>
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

`--accept-language` (string)

The language code.

- `jp` - Japanese
- `zh` - Chinese

`--portfolio-id` (string)

The portfolio identifier.

`--principal-arn` (string)

The ARN of the principal (user, role, or group). If the `PrincipalType` is `IAM` , the supported value is a fully defined [IAM Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) . If the `PrincipalType` is `IAM_PATTERN` , the supported value is an `IAM` ARN *without an AccountID* in the following format:

*arn:partition:iam:::resource-type/resource-id*

The ARN resource-id can be either:

- A fully formed resource-id. For example, *arn:aws:iam:::role/resource-name* or *arn:aws:iam:::role/resource-path/resource-name*
- A wildcard ARN. The wildcard ARN accepts `IAM_PATTERN` values with a â*â or â?â in the resource-id segment of the ARN. For example *arn:partition:service:::resource-type/resource-path/resource-name* . The new symbols are exclusive to the **resource-path** and **resource-name** and cannot replace the **resource-type** or other ARN values.  The ARN path and principal name allow unlimited wildcard characters.

Examples of an **acceptable** wildcard ARN:

- arn:aws:iam:::role/ResourceName_*
- arn:aws:iam:::role/[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html#id1)/[ResourceName_](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html#id5)?

Examples of an **unacceptable** wildcard ARN:

- arn:aws:iam:::[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html#id3)/ResourceName

You can associate multiple `IAM_PATTERN` s even if the account has no principal with that name.

The â?â wildcard character matches zero or one of any character. This is similar to â.?â in regular regex context. The â*â wildcard character matches any number of any characters. This is similar to â.*â in regular regex context.

In the IAM Principal ARN format (*arn:partition:iam:::resource-type/resource-path/resource-name* ), valid resource-type values include **user/** , **group/** , or **role/** . The â?â and â*â characters are allowed only after the resource-type in the resource-id segment. You can use special characters anywhere within the resource-id.

The â*â character also matches the â/â character, allowing paths to be formed *within* the resource-id. For example, *arn:aws:iam:::role/***** /[ResourceName_](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html#id7)?* matches both *arn:aws:iam:::role/pathA/pathB/ResourceName_1* and *arn:aws:iam:::role/pathA/ResourceName_1* .

`--principal-type` (string)

The principal type. The supported value is `IAM` if you use a fully defined Amazon Resource Name (ARN), or `IAM_PATTERN` if you use an ARN with no `accountID` , with or without wildcard characters.

Possible values:

- `IAM`
- `IAM_PATTERN`

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

**To associate a principal with a portfolio**

The following `associate-principal-with-portfolio` example associates a user with the specified portfolio.

```
aws servicecatalog associate-principal-with-portfolio \
    --portfolio-id port-2s6abcdefwdh4 \
    --principal-arn arn:aws:iam::123456789012:user/usertest \
    --principal-type IAM
```

This command produces no output.

## Output

None