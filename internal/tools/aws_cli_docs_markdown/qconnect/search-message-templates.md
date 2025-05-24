# search-message-templatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/search-message-templates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/search-message-templates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# search-message-templates

## Description

Searches for Amazon Q in Connect message templates in the specified knowledge base.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/SearchMessageTemplates)

`search-message-templates` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `results`

## Synopsis

```
search-message-templates
--knowledge-base-id <value>
--search-expression <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--knowledge-base-id` (string)

The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.

`--search-expression` (structure)

The search expression for querying the message template.

queries -> (list)

The message template query expressions.

(structure)

The message template fields to query message templates by. The following is the list of supported field names:

- name
- description

name -> (string)

The name of the attribute to query the message templates by.

values -> (list)

The values of the attribute to query the message templates by.

(string)

operator -> (string)

The operator to use for matching attribute field values in the query.

allowFuzziness -> (boolean)

Whether the query expects only exact matches on the attribute field values. The results of the query will only include exact matches if this parameter is set to false.

priority -> (string)

The importance of the attribute field when calculating query result relevancy scores. The value set for this parameter affects the ordering of search results.

filters -> (list)

The configuration of filtering rules applied to message template query results.

(structure)

The message template fields to filter the message template query results by. The following is the list of supported field names:

- name
- description
- channel
- channelSubtype
- language
- qualifier
- createdTime
- lastModifiedTime
- lastModifiedBy
- groupingConfiguration.criteria
- groupingConfiguration.values

name -> (string)

The name of the attribute field to filter the message templates by.

values -> (list)

The values of attribute field to filter the message template by.

(string)

operator -> (string)

The operator to use for filtering.

includeNoExistence -> (boolean)

Whether to treat null value as a match for the attribute field.

orderOnField -> (structure)

The message template attribute fields on which the query results are ordered.

name -> (string)

The name of the message template.

order -> (string)

The order at which the message templates are sorted by.

JSON Syntax:

```
{
  "queries": [
    {
      "name": "string",
      "values": ["string", ...],
      "operator": "CONTAINS"|"CONTAINS_AND_PREFIX",
      "allowFuzziness": true|false,
      "priority": "HIGH"|"MEDIUM"|"LOW"
    }
    ...
  ],
  "filters": [
    {
      "name": "string",
      "values": ["string", ...],
      "operator": "EQUALS"|"PREFIX",
      "includeNoExistence": true|false
    }
    ...
  ],
  "orderOnField": {
    "name": "string",
    "order": "ASC"|"DESC"
  }
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

results -> (list)

The results of the message template search.

(structure)

The result of message template search.

messageTemplateArn -> (string)

The Amazon Resource Name (ARN) of the message template.

messageTemplateId -> (string)

The identifier of the message template.

knowledgeBaseArn -> (string)

The Amazon Resource Name (ARN) of the knowledge base.

knowledgeBaseId -> (string)

The identifier of the knowledge base.

name -> (string)

The name of the message template.

channelSubtype -> (string)

The channel subtype this message template applies to.

createdTime -> (timestamp)

The timestamp when the message template was created.

lastModifiedTime -> (timestamp)

The timestamp when the message template data was last modified.

lastModifiedBy -> (string)

The Amazon Resource Name (ARN) of the user who last updated the message template data.

isActive -> (boolean)

Whether the version of the message template is activated.

versionNumber -> (long)

The version number of the message template version.

description -> (string)

The description of the message template.

groupingConfiguration -> (structure)

The configuration information of the grouping of Amazon Q in Connect users.

criteria -> (string)

The criteria used for grouping Amazon Q in Connect users.

The following is the list of supported criteria values.

- `RoutingProfileArn` : Grouping the users by their [Amazon Connect routing profile ARN](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) . User should have [SearchRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) permissions when setting criteria to this value.

values -> (list)

The list of values that define different groups of Amazon Q in Connect users.

- When setting `criteria` to `RoutingProfileArn` , you need to provide a list of ARNs of [Amazon Connect routing profiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) as values of this parameter.

(string)

language -> (string)

The language code value for the language in which the quick response is written. The supported language codes include `de_DE` , `en_US` , `es_ES` , `fr_FR` , `id_ID` , `it_IT` , `ja_JP` , `ko_KR` , `pt_BR` , `zh_CN` , `zh_TW`

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

nextToken -> (string)

If there are additional results, this is the token for the next set of results.