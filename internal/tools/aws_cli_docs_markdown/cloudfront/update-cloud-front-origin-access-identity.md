# update-cloud-front-origin-access-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cloud-front-origin-access-identity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cloud-front-origin-access-identity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# update-cloud-front-origin-access-identity

## Description

Update an origin access identity.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/UpdateCloudFrontOriginAccessIdentity)

## Synopsis

```
update-cloud-front-origin-access-identity
--cloud-front-origin-access-identity-config <value>
--id <value>
[--if-match <value>]
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

`--cloud-front-origin-access-identity-config` (structure)

The identityâs configuration information.

CallerReference -> (string)

A unique value (for example, a date-time stamp) that ensures that the request canât be replayed.

If the value of `CallerReference` is new (regardless of the content of the `CloudFrontOriginAccessIdentityConfig` object), a new origin access identity is created.

If the `CallerReference` is a value already sent in a previous identity request, and the content of the `CloudFrontOriginAccessIdentityConfig` is identical to the original request (ignoring white space), the response includes the same information returned to the original request.

If the `CallerReference` is a value you already sent in a previous request to create an identity, but the content of the `CloudFrontOriginAccessIdentityConfig` is different from the original request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists` error.

Comment -> (string)

A comment to describe the origin access identity. The comment cannot be longer than 128 characters.

Shorthand Syntax:

```
CallerReference=string,Comment=string
```

JSON Syntax:

```
{
  "CallerReference": "string",
  "Comment": "string"
}
```

`--id` (string)

The identityâs id.

`--if-match` (string)

The value of the `ETag` header that you received when retrieving the identityâs configuration. For example: `E2QWRUHAPOMQZL` .

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

**To update a CloudFront origin access identity**

The following example updates the origin access identity (OAI) with the ID
`E74FTE3AEXAMPLE`. The only field that you can update is the OAIâs
`Comment`.

To update an OAI, you must have the OAIâs ID and `ETag`. The OAI ID is returned in the output of the
[create-cloud-front-origin-access-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cloud-front-origin-access-identity.html) and
[list-cloud-front-origin-access-identities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html) commands.
To get the `ETag`, use the
[get-cloud-front-origin-access-identity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html) or
[get-cloud-front-origin-access-identity-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity-config.html) command.
Use the `--if-match` option to provide the OAIâs `ETag`.

```
aws cloudfront update-cloud-front-origin-access-identity \
    --id E74FTE3AEXAMPLE \
    --if-match E2QWRUHEXAMPLE \
    --cloud-front-origin-access-identity-config \
        CallerReference=cli-example,Comment="Example OAI Updated"
```

You can accomplish the same thing by providing the OAI configuration in a JSON
file, as shown in the following example:

```
aws cloudfront update-cloud-front-origin-access-identity \
    --id E74FTE3AEXAMPLE \
    --if-match E2QWRUHEXAMPLE \
    --cloud-front-origin-access-identity-config file://OAI-config.json
```

The file `OAI-config.json` is a JSON document in the current directory that
contains the following:

```
{
    "CallerReference": "cli-example",
    "Comment": "Example OAI Updated"
}
```

Whether you provide the OAI configuration with a command line argument or a
JSON file, the output is the same:

```
{
    "ETag": "E9LHASXEXAMPLE",
    "CloudFrontOriginAccessIdentity": {
        "Id": "E74FTE3AEXAMPLE",
        "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE",
        "CloudFrontOriginAccessIdentityConfig": {
            "CallerReference": "cli-example",
            "Comment": "Example OAI Updated"
        }
    }
}
```

## Output

CloudFrontOriginAccessIdentity -> (structure)

The origin access identityâs information.

Id -> (string)

The ID for the origin access identity, for example, `E74FTE3AJFJ256A` .

S3CanonicalUserId -> (string)

The Amazon S3 canonical user ID for the origin access identity, used when giving the origin access identity read permission to an object in Amazon S3.

CloudFrontOriginAccessIdentityConfig -> (structure)

The current configuration information for the identity.

CallerReference -> (string)

A unique value (for example, a date-time stamp) that ensures that the request canât be replayed.

If the value of `CallerReference` is new (regardless of the content of the `CloudFrontOriginAccessIdentityConfig` object), a new origin access identity is created.

If the `CallerReference` is a value already sent in a previous identity request, and the content of the `CloudFrontOriginAccessIdentityConfig` is identical to the original request (ignoring white space), the response includes the same information returned to the original request.

If the `CallerReference` is a value you already sent in a previous request to create an identity, but the content of the `CloudFrontOriginAccessIdentityConfig` is different from the original request, CloudFront returns a `CloudFrontOriginAccessIdentityAlreadyExists` error.

Comment -> (string)

A comment to describe the origin access identity. The comment cannot be longer than 128 characters.

ETag -> (string)

The current version of the configuration. For example: `E2QWRUHAPOMQZL` .