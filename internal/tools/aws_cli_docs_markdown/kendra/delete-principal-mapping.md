# delete-principal-mappingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-principal-mapping.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/delete-principal-mapping.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# delete-principal-mapping

## Description

Deletes a group so that all users that belong to the group can no longer access documents only available to that group.

For example, after deleting the group âSummer Internsâ, all interns who belonged to that group no longer see intern-only documents in their search results.

If you want to delete or replace users or sub groups of a group, you need to use the `PutPrincipalMapping` operation. For example, if a user in the group âEngineeringâ leaves the engineering team and another user takes their place, you provide an updated list of users or sub groups that belong to the âEngineeringâ group when calling `PutPrincipalMapping` . You can update your internal list of users or sub groups and input this list when calling `PutPrincipalMapping` .

`DeletePrincipalMapping` is currently not supported in the Amazon Web Services GovCloud (US-West) region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/DeletePrincipalMapping)

## Synopsis

```
delete-principal-mapping
--index-id <value>
[--data-source-id <value>]
--group-id <value>
[--ordering-id <value>]
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

`--index-id` (string)

The identifier of the index you want to delete a group from.

`--data-source-id` (string)

The identifier of the data source you want to delete a group from.

A group can be tied to multiple data sources. You can delete a group from accessing documents in a certain data source. For example, the groups âResearchâ, âEngineeringâ, and âSales and Marketingâ are all tied to the companyâs documents stored in the data sources Confluence and Salesforce. You want to delete âResearchâ and âEngineeringâ groups from Salesforce, so that these groups cannot access customer-related documents stored in Salesforce. Only âSales and Marketingâ should access documents in the Salesforce data source.

`--group-id` (string)

The identifier of the group you want to delete.

`--ordering-id` (long)

The timestamp identifier you specify to ensure Amazon Kendra does not override the latest `DELETE` action with previous actions. The highest number ID, which is the ordering ID, is the latest action you want to process and apply on top of other actions with lower number IDs. This prevents previous actions with lower number IDs from possibly overriding the latest action.

The ordering ID can be the Unix time of the last update you made to a group members list. You would then provide this list when calling `PutPrincipalMapping` . This ensures your `DELETE` action for that updated group with the latest members list doesnât get overwritten by earlier `DELETE` actions for the same group which are yet to be processed.

The default ordering ID is the current Unix time in milliseconds that the action was received by Amazon Kendra.

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

None