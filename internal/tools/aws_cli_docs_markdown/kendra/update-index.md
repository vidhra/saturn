# update-indexÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# update-index

## Description

Updates an Amazon Kendra index.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/UpdateIndex)

## Synopsis

```
update-index
--id <value>
[--name <value>]
[--role-arn <value>]
[--description <value>]
[--document-metadata-configuration-updates <value>]
[--capacity-units <value>]
[--user-token-configurations <value>]
[--user-context-policy <value>]
[--user-group-resolution-configuration <value>]
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

The identifier of the index you want to update.

`--name` (string)

A new name for the index.

`--role-arn` (string)

An Identity and Access Management (IAM) role that gives Amazon Kendra permission to access Amazon CloudWatch logs and metrics.

`--description` (string)

A new description for the index.

`--document-metadata-configuration-updates` (list)

The document metadata configuration you want to update for the index. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document.

(structure)

Specifies the properties, such as relevance tuning and searchability, of an index field.

Name -> (string)

The name of the index field.

Type -> (string)

The data type of the index field.

Relevance -> (structure)

Provides tuning parameters to determine how the field affects the search results.

Freshness -> (boolean)

Indicates that this field determines how âfreshâ a document is. For example, if document 1 was created on November 5, and document 2 was created on October 31, document 1 is âfresherâ than document 2. Only applies to `DATE` fields.

Importance -> (integer)

The relative importance of the field in the search. Larger numbers provide more of a boost than smaller numbers.

Duration -> (string)

Specifies the time period that the boost applies to. For example, to make the boost apply to documents with the field value within the last month, you would use â2628000sâ. Once the field value is beyond the specified range, the effect of the boost drops off. The higher the importance, the faster the effect drops off. If you donât specify a value, the default is 3 months. The value of the field is a numeric string followed by the character âsâ, for example â86400sâ for one day, or â604800sâ for one week.

Only applies to `DATE` fields.

RankOrder -> (string)

Determines how values should be interpreted.

When the `RankOrder` field is `ASCENDING` , higher numbers are better. For example, a document with a rating score of 10 is higher ranking than a document with a rating score of 1.

When the `RankOrder` field is `DESCENDING` , lower numbers are better. For example, in a task tracking application, a priority 1 task is more important than a priority 5 task.

Only applies to `LONG` fields.

ValueImportanceMap -> (map)

A list of values that should be given a different boost when they appear in the result list. For example, if you are boosting a field called âdepartmentâ, query terms that match the department field are boosted in the result. However, you can add entries from the department field to boost documents with those values higher.

For example, you can add entries to the map with names of departments. If you add âHRâ,5 and âLegalâ,3 those departments are given special attention when they appear in the metadata of a document. When those terms appear they are given the specified importance instead of the regular importance for the boost.

key -> (string)

value -> (integer)

Search -> (structure)

Provides information about how the field is used during a search.

Facetable -> (boolean)

Indicates that the field can be used to create search facets, a count of results for each value in the field. The default is `false` .

Searchable -> (boolean)

Determines whether the field is used in the search. If the `Searchable` field is `true` , you can use relevance tuning to manually tune how Amazon Kendra weights the field in the search. The default is `true` for string fields and `false` for number and date fields.

Displayable -> (boolean)

Determines whether the field is returned in the query response. The default is `true` .

Sortable -> (boolean)

Determines whether the field can be used to sort the results of a query. If you specify sorting on a field that does not have `Sortable` set to `true` , Amazon Kendra returns an exception. The default is `false` .

Shorthand Syntax:

```
Name=string,Type=string,Relevance={Freshness=boolean,Importance=integer,Duration=string,RankOrder=string,ValueImportanceMap={KeyName1=integer,KeyName2=integer}},Search={Facetable=boolean,Searchable=boolean,Displayable=boolean,Sortable=boolean} ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Type": "STRING_VALUE"|"STRING_LIST_VALUE"|"LONG_VALUE"|"DATE_VALUE",
    "Relevance": {
      "Freshness": true|false,
      "Importance": integer,
      "Duration": "string",
      "RankOrder": "ASCENDING"|"DESCENDING",
      "ValueImportanceMap": {"string": integer
        ...}
    },
    "Search": {
      "Facetable": true|false,
      "Searchable": true|false,
      "Displayable": true|false,
      "Sortable": true|false
    }
  }
  ...
]
```

`--capacity-units` (structure)

Sets the number of additional document storage and query capacity units that should be used by the index. You can change the capacity of the index up to 5 times per day, or make 5 API calls.

If you are using extra storage units, you canât reduce the storage capacity below what is required to meet the storage needs for your index.

StorageCapacityUnits -> (integer)

The amount of extra storage capacity for an index. A single capacity unit provides 30 GB of storage space or 100,000 documents, whichever is reached first. You can add up to 100 extra capacity units.

QueryCapacityUnits -> (integer)

The amount of extra query capacity for an index and [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html) capacity.

A single extra capacity unit for an index provides 0.1 queries per second or approximately 8,000 queries per day. You can add up to 100 extra capacity units.

`GetQuerySuggestions` capacity is five times the provisioned query capacity for an index, or the base capacity of 2.5 calls per second, whichever is higher. For example, the base capacity for an index is 0.1 queries per second, and `GetQuerySuggestions` capacity has a base of 2.5 calls per second. If you add another 0.1 queries per second to total 0.2 queries per second for an index, the `GetQuerySuggestions` capacity is 2.5 calls per second (higher than five times 0.2 queries per second).

Shorthand Syntax:

```
StorageCapacityUnits=integer,QueryCapacityUnits=integer
```

JSON Syntax:

```
{
  "StorageCapacityUnits": integer,
  "QueryCapacityUnits": integer
}
```

`--user-token-configurations` (list)

The user token configuration.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `UserTokenConfigurations` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

(structure)

Provides the configuration information for a token.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `UserTokenConfigurations` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

JwtTokenTypeConfiguration -> (structure)

Information about the JWT token type configuration.

KeyLocation -> (string)

The location of the key.

URL -> (string)

The signing key URL.

SecretManagerArn -> (string)

The Amazon Resource Name (arn) of the secret.

UserNameAttributeField -> (string)

The user name attribute field.

GroupAttributeField -> (string)

The group attribute field.

Issuer -> (string)

The issuer of the token.

ClaimRegex -> (string)

The regular expression that identifies the claim.

JsonTokenTypeConfiguration -> (structure)

Information about the JSON token type configuration.

UserNameAttributeField -> (string)

The user name attribute field.

GroupAttributeField -> (string)

The group attribute field.

Shorthand Syntax:

```
JwtTokenTypeConfiguration={KeyLocation=string,URL=string,SecretManagerArn=string,UserNameAttributeField=string,GroupAttributeField=string,Issuer=string,ClaimRegex=string},JsonTokenTypeConfiguration={UserNameAttributeField=string,GroupAttributeField=string} ...
```

JSON Syntax:

```
[
  {
    "JwtTokenTypeConfiguration": {
      "KeyLocation": "URL"|"SECRET_MANAGER",
      "URL": "string",
      "SecretManagerArn": "string",
      "UserNameAttributeField": "string",
      "GroupAttributeField": "string",
      "Issuer": "string",
      "ClaimRegex": "string"
    },
    "JsonTokenTypeConfiguration": {
      "UserNameAttributeField": "string",
      "GroupAttributeField": "string"
    }
  }
  ...
]
```

`--user-context-policy` (string)

The user context policy.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index, you can only use `ATTRIBUTE_FILTER` to filter search results by user context. If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `USER_TOKEN` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

Possible values:

- `ATTRIBUTE_FILTER`
- `USER_TOKEN`

`--user-group-resolution-configuration` (structure)

Gets users and groups from IAM Identity Center identity source. To configure this, see [UserGroupResolutionConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html) . This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index, `UserGroupResolutionConfiguration` isnât supported.

UserGroupResolutionMode -> (string)

The identity store provider (mode) you want to use to get users and groups. IAM Identity Center is currently the only available mode. Your users and groups must exist in an IAM Identity Center identity source in order to use this mode.

Shorthand Syntax:

```
UserGroupResolutionMode=string
```

JSON Syntax:

```
{
  "UserGroupResolutionMode": "AWS_SSO"|"NONE"
}
```

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

**To update an Amazon Kendra index**

The following `update-index` updates the configuration of an Amazon Kendra index. If the action is successful, the service either sends back no output, the HTTP status code 200, or the AWS CLI return code 0. You can use `describe-index` to view the configuration and status of an index.

```
aws kendra update-index \
    --id enterpriseindex1 \
    --name "new name for Enterprise Edition index 1" \
    --description "new description for Enterprise Edition index 1" \
    --role-arn arn:aws:iam::my-account-id:role/KendraNewRoleForEnterpriseIndex \
    --capacity-units '{"QueryCapacityUnits": 2, "StorageCapacityUnits": 1}' \
    --document-metadata-configuration-updates '{"Name": "_document_title", "Relevance": {"Importance": 6}}, {"Name": "_last_updated_at", "Relevance": {"Importance": 8}}' \
    --user-context-policy "USER_TOKEN" \
    --user-token-configurations '{"JsonTokenTypeConfiguration": {"GroupAttributeField": "groupNameField", "UserNameAttributeField": "userNameField"}}'
```

This command produces no output.

For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html) in the *Amazon Kendra Developer Guide*.

## Output

None