# describe-experienceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-experience.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-experience.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# describe-experience

## Description

Gets information about your Amazon Kendra experience such as a search application. For more information on creating a search application experience, see [Building a search experience with no code](https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/DescribeExperience)

## Synopsis

```
describe-experience
--id <value>
--index-id <value>
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

`--id` (string)

The identifier of your Amazon Kendra experience you want to get information on.

`--index-id` (string)

The identifier of the index for your Amazon Kendra experience.

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

Shows the identifier of your Amazon Kendra experience.

IndexId -> (string)

Shows the identifier of the index for your Amazon Kendra experience.

Name -> (string)

Shows the name of your Amazon Kendra experience.

Endpoints -> (list)

Shows the endpoint URLs for your Amazon Kendra experiences. The URLs are unique and fully hosted by Amazon Web Services.

(structure)

Provides the configuration information for the endpoint for your Amazon Kendra experience.

EndpointType -> (string)

The type of endpoint for your Amazon Kendra experience. The type currently available is `HOME` , which is a unique and fully hosted URL to the home page of your Amazon Kendra experience.

Endpoint -> (string)

The endpoint of your Amazon Kendra experience.

Configuration -> (structure)

Shows the configuration information for your Amazon Kendra experience. This includes `ContentSourceConfiguration` , which specifies the data source IDs and/or FAQ IDs, and `UserIdentityConfiguration` , which specifies the user or group information to grant access to your Amazon Kendra experience.

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

CreatedAt -> (timestamp)

The Unix timestamp when your Amazon Kendra experience was created.

UpdatedAt -> (timestamp)

The Unix timestamp when your Amazon Kendra experience was last updated.

Description -> (string)

Shows the description for your Amazon Kendra experience.

Status -> (string)

The current processing status of your Amazon Kendra experience. When the status is `ACTIVE` , your Amazon Kendra experience is ready to use. When the status is `FAILED` , the `ErrorMessage` field contains the reason that this failed.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role with permission to access the `Query` API, `QuerySuggestions` API, `SubmitFeedback` API, and IAM Identity Center that stores your users and groups information.

ErrorMessage -> (string)

The reason your Amazon Kendra experience could not properly process.