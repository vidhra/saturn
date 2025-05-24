# get-grantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-grant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-grant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/index.html#cli-aws-license-manager) ]

# get-grant

## Description

Gets detailed information about the specified grant.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-2018-08-01/GetGrant)

## Synopsis

```
get-grant
--grant-arn <value>
[--grant-version <value>]
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

`--grant-arn` (string)

Amazon Resource Name (ARN) of the grant.

`--grant-version` (string)

Grant version.

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

Grant -> (structure)

Grant details.

GrantArn -> (string)

Amazon Resource Name (ARN) of the grant.

GrantName -> (string)

Grant name.

ParentArn -> (string)

Parent ARN.

LicenseArn -> (string)

License ARN.

GranteePrincipalArn -> (string)

The grantee principal ARN.

HomeRegion -> (string)

Home Region of the grant.

GrantStatus -> (string)

Grant status.

StatusReason -> (string)

Grant status reason.

Version -> (string)

Grant version.

GrantedOperations -> (list)

Granted operations.

(string)

Options -> (structure)

The options specified for the grant.

ActivationOverrideBehavior -> (string)

An activation option for your grant that determines the behavior of activating a grant. Activation options can only be used with granted licenses sourced from the Amazon Web Services Marketplace. Additionally, the operation must specify the value of `ACTIVE` for the `Status` parameter.

- As a license administrator, you can optionally specify an `ActivationOverrideBehavior` when activating a grant.
- As a grantor, you can optionally specify an `ActivationOverrideBehavior` when you activate a grant for a grantee account in your organization.
- As a grantee, if the grantor creating the distributed grant doesnât specify an `ActivationOverrideBehavior` , you can optionally specify one when you are activating the grant.

DISTRIBUTED_GRANTS_ONLY

Use this value to activate a grant without replacing any member accountâs active grants for the same product.

ALL_GRANTS_PERMITTED_BY_ISSUER

Use this value to activate a grant and disable other active grants in any member accounts for the same product. This action will also replace their previously activated grants with this activated grant.