# update-portfolio-shareÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-portfolio-share.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-portfolio-share.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# update-portfolio-share

## Description

Updates the specified portfolio share. You can use this API to enable or disable `TagOptions` sharing or Principal sharing for an existing portfolio share.

The portfolio share cannot be updated if the `CreatePortfolioShare` operation is `IN_PROGRESS` , as the share is not available to recipient entities. In this case, you must wait for the portfolio share to be completed.

You must provide the `accountId` or organization node in the input, but not both.

If the portfolio is shared to both an external account and an organization node, and both shares need to be updated, you must invoke `UpdatePortfolioShare` separately for each share type.

This API cannot be used for removing the portfolio share. You must use `DeletePortfolioShare` API for that action.

### Note

When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is then shared with other accounts. For a user in a recipient account who is *not* an Service Catalog Admin, but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal name association for the portfolio. Although this user may not know which principal names are associated through Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then Service Catalog recommends using `PrincipalType` as `IAM` . With this configuration, the `PrincipalARN` must already exist in the recipient account before it can be associated.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/UpdatePortfolioShare)

## Synopsis

```
update-portfolio-share
[--accept-language <value>]
--portfolio-id <value>
[--account-id <value>]
[--organization-node <value>]
[--share-tag-options | --no-share-tag-options]
[--share-principals | --no-share-principals]
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

The unique identifier of the portfolio for which the share will be updated.

`--account-id` (string)

The Amazon Web Services account Id of the recipient account. This field is required when updating an external account to account type share.

`--organization-node` (structure)

Information about the organization node.

Type -> (string)

The organization node type.

Value -> (string)

The identifier of the organization node.

Shorthand Syntax:

```
Type=string,Value=string
```

JSON Syntax:

```
{
  "Type": "ORGANIZATION"|"ORGANIZATIONAL_UNIT"|"ACCOUNT",
  "Value": "string"
}
```

`--share-tag-options` | `--no-share-tag-options` (boolean)

Enables or disables `TagOptions` sharing for the portfolio share. If this field is not provided, the current state of TagOptions sharing on the portfolio share will not be modified.

`--share-principals` | `--no-share-principals` (boolean)

A flag to enables or disables `Principals` sharing in the portfolio. If this field is not provided, the current state of the `Principals` sharing on the portfolio share will not be modified.

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

PortfolioShareToken -> (string)

The token that tracks the status of the `UpdatePortfolioShare` operation for external account to account or organizational type sharing.

Status -> (string)

The status of `UpdatePortfolioShare` operation. You can also obtain the operation status using `DescribePortfolioShareStatus` API.