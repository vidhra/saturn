# search-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/search-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/search-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# search-types

## Description

Searches for types in Amazon DataZone.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/SearchTypes)

`search-types` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
search-types
--domain-identifier <value>
[--filters <value>]
--managed | --no-managed
[--search-in <value>]
--search-scope <value>
[--search-text <value>]
[--sort <value>]
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

`--domain-identifier` (string)

The identifier of the Amazon DataZone domain in which to invoke the `SearchTypes` action.

`--filters` (tagged union structure)

The filters for the `SearchTypes` action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `filter`, `or`.

and -> (list)

The âandâ search filter clause in Amazon DataZone.

(tagged union structure)

A search filter clause in Amazon DataZone.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `filter`, `or`.

and -> (list)

The âandâ search filter clause in Amazon DataZone.

( â¦ recursive â¦ )

filter -> (structure)

A search filter in Amazon DataZone.

attribute -> (string)

A search filter attribute in Amazon DataZone.

value -> (string)

A search filter value in Amazon DataZone.

or -> (list)

The âorâ search filter clause in Amazon DataZone.

( â¦ recursive â¦ )

filter -> (structure)

A search filter in Amazon DataZone.

attribute -> (string)

A search filter attribute in Amazon DataZone.

value -> (string)

A search filter value in Amazon DataZone.

or -> (list)

The âorâ search filter clause in Amazon DataZone.

(tagged union structure)

A search filter clause in Amazon DataZone.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `filter`, `or`.

and -> (list)

The âandâ search filter clause in Amazon DataZone.

( â¦ recursive â¦ )

filter -> (structure)

A search filter in Amazon DataZone.

attribute -> (string)

A search filter attribute in Amazon DataZone.

value -> (string)

A search filter value in Amazon DataZone.

or -> (list)

The âorâ search filter clause in Amazon DataZone.

( â¦ recursive â¦ )

JSON Syntax:

```
{
  "and": [
    {
      "and": [
        { ... recursive ... }
        ...
      ],
      "filter": {
        "attribute": "string",
        "value": "string"
      },
      "or": [
        { ... recursive ... }
        ...
      ]
    }
    ...
  ],
  "filter": {
    "attribute": "string",
    "value": "string"
  },
  "or": [
    {
      "and": [
        { ... recursive ... }
        ...
      ],
      "filter": {
        "attribute": "string",
        "value": "string"
      },
      "or": [
        { ... recursive ... }
        ...
      ]
    }
    ...
  ]
}
```

`--managed` | `--no-managed` (boolean)

Specifies whether the search is managed.

`--search-in` (list)

The details of the search.

(structure)

The details of the search.

attribute -> (string)

The search attribute.

Shorthand Syntax:

```
attribute=string ...
```

JSON Syntax:

```
[
  {
    "attribute": "string"
  }
  ...
]
```

`--search-scope` (string)

Specifies the scope of the search for types.

Possible values:

- `ASSET_TYPE`
- `FORM_TYPE`
- `LINEAGE_NODE_TYPE`

`--search-text` (string)

Specifies the text for which to search.

`--sort` (structure)

The specifies the way to sort the `SearchTypes` results.

attribute -> (string)

The attribute detail of the way to sort search results.

order -> (string)

The order detail of the wya to sort search results.

Shorthand Syntax:

```
attribute=string,order=string
```

JSON Syntax:

```
{
  "attribute": "string",
  "order": "ASCENDING"|"DESCENDING"
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

items -> (list)

The results of the `SearchTypes` action.

(tagged union structure)

The details of the results of the `SearchTypes` action.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `assetTypeItem`, `formTypeItem`, `lineageNodeTypeItem`.

assetTypeItem -> (structure)

The asset type included in the results of the `SearchTypes` action.

createdAt -> (timestamp)

The timestamp of when the asset type was created.

createdBy -> (string)

The Amazon DataZone user who created the asset type.

description -> (string)

The description of the asset type.

domainId -> (string)

The identifier of the Amazon DataZone domain where the asset type exists.

formsOutput -> (map)

The forms included in the details of the asset type.

key -> (string)

value -> (structure)

The details of the form entry.

required -> (boolean)

Specifies whether a form entry is required.

typeName -> (string)

The name of the type of the form entry.

typeRevision -> (string)

The type revision of the form entry.

name -> (string)

The name of the asset type.

originDomainId -> (string)

The identifier of the Amazon DataZone domain where the asset type was originally created.

originProjectId -> (string)

The identifier of the Amazon DataZone project where the asset type exists.

owningProjectId -> (string)

The identifier of the Amazon DataZone project that owns the asset type.

revision -> (string)

The revision of the asset type.

updatedAt -> (timestamp)

The timestamp of when the asset type was updated.

updatedBy -> (string)

The Amazon DataZone user who updated the asset type.

formTypeItem -> (structure)

The form type included in the results of the `SearchTypes` action.

createdAt -> (timestamp)

The timestamp of when the metadata form type was created.

createdBy -> (string)

The Amazon DataZone user who created teh metadata form type.

description -> (string)

The description of the metadata form type.

domainId -> (string)

The identifier of the Amazon DataZone domain in which the form type exists.

imports -> (list)

The imports specified in the form type.

(structure)

The details of the import of the metadata form type.

name -> (string)

The name of the import.

revision -> (string)

The revision of the import.

model -> (tagged union structure)

The model of the form type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `smithy`.

smithy -> (string)

Indicates the smithy model of the API.

name -> (string)

The name of the form type.

originDomainId -> (string)

The identifier of the Amazon DataZone domain in which the form type was originally created.

originProjectId -> (string)

The identifier of the project in which the form type was originally created.

owningProjectId -> (string)

The identifier of the project that owns the form type.

revision -> (string)

The revision of the form type.

status -> (string)

The status of the form type.

lineageNodeTypeItem -> (structure)

The details of a data lineage node type.

createdAt -> (timestamp)

The timestamp at which the data lineage node type was created.

createdBy -> (string)

The user who created the data lineage node type.

description -> (string)

The description of the data lineage node type.

domainId -> (string)

The ID of the domain where the data lineage node type lives.

formsOutput -> (map)

The forms output of the data lineage node type.

key -> (string)

value -> (structure)

The details of the form entry.

required -> (boolean)

Specifies whether a form entry is required.

typeName -> (string)

The name of the type of the form entry.

typeRevision -> (string)

The type revision of the form entry.

name -> (string)

The name of the data lineage node type.

revision -> (string)

The revision of the data lineage node type.

updatedAt -> (timestamp)

The timestamp at which the data lineage node type was updated.

updatedBy -> (string)

The user who updated the data lineage node type.

nextToken -> (string)

When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken` . You can specify this `NextToken` value in a subsequent call to `SearchTypes` to list the next set of results.

totalMatchCount -> (integer)

Total number of search results.