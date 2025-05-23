# create-experienceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-experience.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-experience.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# create-experience

## Description

Creates an Amazon Kendra experience such as a search application. For more information on creating a search application experience, including using the Python and Java SDKs, see [Building a search experience with no code](https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/CreateExperience)

## Synopsis

```
create-experience
--name <value>
--index-id <value>
[--role-arn <value>]
[--configuration <value>]
[--description <value>]
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

`--name` (string)

A name for your Amazon Kendra experience.

`--index-id` (string)

The identifier of the index for your Amazon Kendra experience.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access `Query` API, `GetQuerySuggestions` API, and other required APIs. The role also must include permission to access IAM Identity Center that stores your user and group information. For more information, see [IAM access roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

`--configuration` (structure)

Configuration information for your Amazon Kendra experience. This includes `ContentSourceConfiguration` , which specifies the data source IDs and/or FAQ IDs, and `UserIdentityConfiguration` , which specifies the user or group information to grant access to your Amazon Kendra experience.

ContentSourceConfiguration -> (structure)

The identifiers of your data sources and FAQs. Or, you can specify that you want to use documents indexed via the `BatchPutDocument` API. This is the content you want to use for your Amazon Kendra experience.

DataSourceIds -> (list)

The identifier of the data sources you want to use for your Amazon Kendra experience.

(string)

FaqIds -> (list)

The identifier of the FAQs that you want to use for your Amazon Kendra experience.

(string)

DirectPutContent -> (boolean)

`TRUE` to use documents you indexed directly using the `BatchPutDocument` API.

UserIdentityConfiguration -> (structure)

The IAM Identity Center field name that contains the identifiers of your users, such as their emails.

IdentityAttributeName -> (string)

The IAM Identity Center field name that contains the identifiers of your users, such as their emails. This is used for [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) and for granting access to your Amazon Kendra experience. You must set up IAM Identity Center with Amazon Kendra. You must include your users and groups in your Access Control List when you ingest documents into your index. For more information, see [Getting started with an IAM Identity Center identity source](https://docs.aws.amazon.com/kendra/latest/dg/getting-started-aws-sso.html) .

Shorthand Syntax:

```
ContentSourceConfiguration={DataSourceIds=[string,string],FaqIds=[string,string],DirectPutContent=boolean},UserIdentityConfiguration={IdentityAttributeName=string}
```

JSON Syntax:

```
{
  "ContentSourceConfiguration": {
    "DataSourceIds": ["string", ...],
    "FaqIds": ["string", ...],
    "DirectPutContent": true|false
  },
  "UserIdentityConfiguration": {
    "IdentityAttributeName": "string"
  }
}
```

`--description` (string)

A description for your Amazon Kendra experience.

`--client-token` (string)

A token that you provide to identify the request to create your Amazon Kendra experience. Multiple calls to the `CreateExperience` API with the same client token creates only one Amazon Kendra experience.

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

Id -> (string)

The identifier of your Amazon Kendra experience.