# update-asset-filterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/update-asset-filter.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/update-asset-filter.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# update-asset-filter

## Description

Updates an asset filter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/UpdateAssetFilter)

## Synopsis

```
update-asset-filter
--asset-identifier <value>
[--configuration <value>]
[--description <value>]
--domain-identifier <value>
--identifier <value>
[--name <value>]
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

`--asset-identifier` (string)

The ID of the data asset.

`--configuration` (tagged union structure)

The configuration of the asset filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `columnConfiguration`, `rowConfiguration`.

columnConfiguration -> (structure)

The column configuration of the asset filter.

includedColumnNames -> (list)

Specifies whether to include column names.

(string)

rowConfiguration -> (structure)

The row configuration of the asset filter.

rowFilter -> (tagged union structure)

The row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `expression`, `or`.

and -> (list)

The âandâ clause of the row filter.

(tagged union structure)

The row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `expression`, `or`.

and -> (list)

The âandâ clause of the row filter.

( â¦ recursive â¦ )

expression -> (tagged union structure)

The expression of the row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `greaterThan`, `greaterThanOrEqualTo`, `in`, `isNotNull`, `isNull`, `lessThan`, `lessThanOrEqualTo`, `like`, `notEqualTo`, `notIn`, `notLike`.

equalTo -> (structure)

The âequal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be equal to an expression.

greaterThan -> (structure)

The âgreater thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than an expression.

greaterThanOrEqualTo -> (structure)

The âgreater than or equal toâ clause of the filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than or equal to an expression.

in -> (structure)

The âinâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The values that might be in the expression.

(string)

isNotNull -> (structure)

The âis not nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

isNull -> (structure)

The âis nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

lessThan -> (structure)

The âless thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than the expression.

lessThanOrEqualTo -> (structure)

The âless than or equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than or equal to an expression.

like -> (structure)

The âlikeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be like the expression.

notEqualTo -> (structure)

The âno equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be equal to the expression.

notIn -> (structure)

The ânot inâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The value that might not be in the expression.

(string)

notLike -> (structure)

The ânot likeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be like the expression.

or -> (list)

The âorâ clause of the row filter.

( â¦ recursive â¦ )

expression -> (tagged union structure)

The expression of the row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `greaterThan`, `greaterThanOrEqualTo`, `in`, `isNotNull`, `isNull`, `lessThan`, `lessThanOrEqualTo`, `like`, `notEqualTo`, `notIn`, `notLike`.

equalTo -> (structure)

The âequal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be equal to an expression.

greaterThan -> (structure)

The âgreater thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than an expression.

greaterThanOrEqualTo -> (structure)

The âgreater than or equal toâ clause of the filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than or equal to an expression.

in -> (structure)

The âinâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The values that might be in the expression.

(string)

isNotNull -> (structure)

The âis not nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

isNull -> (structure)

The âis nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

lessThan -> (structure)

The âless thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than the expression.

lessThanOrEqualTo -> (structure)

The âless than or equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than or equal to an expression.

like -> (structure)

The âlikeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be like the expression.

notEqualTo -> (structure)

The âno equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be equal to the expression.

notIn -> (structure)

The ânot inâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The value that might not be in the expression.

(string)

notLike -> (structure)

The ânot likeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be like the expression.

or -> (list)

The âorâ clause of the row filter.

(tagged union structure)

The row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `expression`, `or`.

and -> (list)

The âandâ clause of the row filter.

( â¦ recursive â¦ )

expression -> (tagged union structure)

The expression of the row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `greaterThan`, `greaterThanOrEqualTo`, `in`, `isNotNull`, `isNull`, `lessThan`, `lessThanOrEqualTo`, `like`, `notEqualTo`, `notIn`, `notLike`.

equalTo -> (structure)

The âequal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be equal to an expression.

greaterThan -> (structure)

The âgreater thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than an expression.

greaterThanOrEqualTo -> (structure)

The âgreater than or equal toâ clause of the filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than or equal to an expression.

in -> (structure)

The âinâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The values that might be in the expression.

(string)

isNotNull -> (structure)

The âis not nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

isNull -> (structure)

The âis nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

lessThan -> (structure)

The âless thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than the expression.

lessThanOrEqualTo -> (structure)

The âless than or equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than or equal to an expression.

like -> (structure)

The âlikeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be like the expression.

notEqualTo -> (structure)

The âno equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be equal to the expression.

notIn -> (structure)

The ânot inâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The value that might not be in the expression.

(string)

notLike -> (structure)

The ânot likeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be like the expression.

or -> (list)

The âorâ clause of the row filter.

( â¦ recursive â¦ )

sensitive -> (boolean)

Specifies whether the row filter is sensitive.

JSON Syntax:

```
{
  "columnConfiguration": {
    "includedColumnNames": ["string", ...]
  },
  "rowConfiguration": {
    "rowFilter": {
      "and": [
        {
          "and": [
            { ... recursive ... }
            ...
          ],
          "expression": {
            "equalTo": {
              "columnName": "string",
              "value": "string"
            },
            "greaterThan": {
              "columnName": "string",
              "value": "string"
            },
            "greaterThanOrEqualTo": {
              "columnName": "string",
              "value": "string"
            },
            "in": {
              "columnName": "string",
              "values": ["string", ...]
            },
            "isNotNull": {
              "columnName": "string"
            },
            "isNull": {
              "columnName": "string"
            },
            "lessThan": {
              "columnName": "string",
              "value": "string"
            },
            "lessThanOrEqualTo": {
              "columnName": "string",
              "value": "string"
            },
            "like": {
              "columnName": "string",
              "value": "string"
            },
            "notEqualTo": {
              "columnName": "string",
              "value": "string"
            },
            "notIn": {
              "columnName": "string",
              "values": ["string", ...]
            },
            "notLike": {
              "columnName": "string",
              "value": "string"
            }
          },
          "or": [
            { ... recursive ... }
            ...
          ]
        }
        ...
      ],
      "expression": {
        "equalTo": {
          "columnName": "string",
          "value": "string"
        },
        "greaterThan": {
          "columnName": "string",
          "value": "string"
        },
        "greaterThanOrEqualTo": {
          "columnName": "string",
          "value": "string"
        },
        "in": {
          "columnName": "string",
          "values": ["string", ...]
        },
        "isNotNull": {
          "columnName": "string"
        },
        "isNull": {
          "columnName": "string"
        },
        "lessThan": {
          "columnName": "string",
          "value": "string"
        },
        "lessThanOrEqualTo": {
          "columnName": "string",
          "value": "string"
        },
        "like": {
          "columnName": "string",
          "value": "string"
        },
        "notEqualTo": {
          "columnName": "string",
          "value": "string"
        },
        "notIn": {
          "columnName": "string",
          "values": ["string", ...]
        },
        "notLike": {
          "columnName": "string",
          "value": "string"
        }
      },
      "or": [
        {
          "and": [
            { ... recursive ... }
            ...
          ],
          "expression": {
            "equalTo": {
              "columnName": "string",
              "value": "string"
            },
            "greaterThan": {
              "columnName": "string",
              "value": "string"
            },
            "greaterThanOrEqualTo": {
              "columnName": "string",
              "value": "string"
            },
            "in": {
              "columnName": "string",
              "values": ["string", ...]
            },
            "isNotNull": {
              "columnName": "string"
            },
            "isNull": {
              "columnName": "string"
            },
            "lessThan": {
              "columnName": "string",
              "value": "string"
            },
            "lessThanOrEqualTo": {
              "columnName": "string",
              "value": "string"
            },
            "like": {
              "columnName": "string",
              "value": "string"
            },
            "notEqualTo": {
              "columnName": "string",
              "value": "string"
            },
            "notIn": {
              "columnName": "string",
              "values": ["string", ...]
            },
            "notLike": {
              "columnName": "string",
              "value": "string"
            }
          },
          "or": [
            { ... recursive ... }
            ...
          ]
        }
        ...
      ]
    },
    "sensitive": true|false
  }
}
```

`--description` (string)

The description of the asset filter.

`--domain-identifier` (string)

The ID of the domain where you want to update an asset filter.

`--identifier` (string)

The ID of the asset filter.

`--name` (string)

The name of the asset filter.

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

assetId -> (string)

The ID of the data asset.

configuration -> (tagged union structure)

The configuration of the asset filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `columnConfiguration`, `rowConfiguration`.

columnConfiguration -> (structure)

The column configuration of the asset filter.

includedColumnNames -> (list)

Specifies whether to include column names.

(string)

rowConfiguration -> (structure)

The row configuration of the asset filter.

rowFilter -> (tagged union structure)

The row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `expression`, `or`.

and -> (list)

The âandâ clause of the row filter.

(tagged union structure)

The row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `expression`, `or`.

and -> (list)

The âandâ clause of the row filter.

( â¦ recursive â¦ )

expression -> (tagged union structure)

The expression of the row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `greaterThan`, `greaterThanOrEqualTo`, `in`, `isNotNull`, `isNull`, `lessThan`, `lessThanOrEqualTo`, `like`, `notEqualTo`, `notIn`, `notLike`.

equalTo -> (structure)

The âequal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be equal to an expression.

greaterThan -> (structure)

The âgreater thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than an expression.

greaterThanOrEqualTo -> (structure)

The âgreater than or equal toâ clause of the filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than or equal to an expression.

in -> (structure)

The âinâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The values that might be in the expression.

(string)

isNotNull -> (structure)

The âis not nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

isNull -> (structure)

The âis nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

lessThan -> (structure)

The âless thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than the expression.

lessThanOrEqualTo -> (structure)

The âless than or equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than or equal to an expression.

like -> (structure)

The âlikeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be like the expression.

notEqualTo -> (structure)

The âno equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be equal to the expression.

notIn -> (structure)

The ânot inâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The value that might not be in the expression.

(string)

notLike -> (structure)

The ânot likeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be like the expression.

or -> (list)

The âorâ clause of the row filter.

( â¦ recursive â¦ )

expression -> (tagged union structure)

The expression of the row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `greaterThan`, `greaterThanOrEqualTo`, `in`, `isNotNull`, `isNull`, `lessThan`, `lessThanOrEqualTo`, `like`, `notEqualTo`, `notIn`, `notLike`.

equalTo -> (structure)

The âequal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be equal to an expression.

greaterThan -> (structure)

The âgreater thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than an expression.

greaterThanOrEqualTo -> (structure)

The âgreater than or equal toâ clause of the filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than or equal to an expression.

in -> (structure)

The âinâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The values that might be in the expression.

(string)

isNotNull -> (structure)

The âis not nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

isNull -> (structure)

The âis nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

lessThan -> (structure)

The âless thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than the expression.

lessThanOrEqualTo -> (structure)

The âless than or equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than or equal to an expression.

like -> (structure)

The âlikeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be like the expression.

notEqualTo -> (structure)

The âno equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be equal to the expression.

notIn -> (structure)

The ânot inâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The value that might not be in the expression.

(string)

notLike -> (structure)

The ânot likeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be like the expression.

or -> (list)

The âorâ clause of the row filter.

(tagged union structure)

The row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `and`, `expression`, `or`.

and -> (list)

The âandâ clause of the row filter.

( â¦ recursive â¦ )

expression -> (tagged union structure)

The expression of the row filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `greaterThan`, `greaterThanOrEqualTo`, `in`, `isNotNull`, `isNull`, `lessThan`, `lessThanOrEqualTo`, `like`, `notEqualTo`, `notIn`, `notLike`.

equalTo -> (structure)

The âequal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be equal to an expression.

greaterThan -> (structure)

The âgreater thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than an expression.

greaterThanOrEqualTo -> (structure)

The âgreater than or equal toâ clause of the filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be greater than or equal to an expression.

in -> (structure)

The âinâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The values that might be in the expression.

(string)

isNotNull -> (structure)

The âis not nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

isNull -> (structure)

The âis nullâ clause of the row filter expression.

columnName -> (string)

The name of the column.

lessThan -> (structure)

The âless thanâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than the expression.

lessThanOrEqualTo -> (structure)

The âless than or equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be less than or equal to an expression.

like -> (structure)

The âlikeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might be like the expression.

notEqualTo -> (structure)

The âno equal toâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be equal to the expression.

notIn -> (structure)

The ânot inâ clause of the row filter expression.

columnName -> (string)

The name of the column.

values -> (list)

The value that might not be in the expression.

(string)

notLike -> (structure)

The ânot likeâ clause of the row filter expression.

columnName -> (string)

The name of the column.

value -> (string)

The value that might not be like the expression.

or -> (list)

The âorâ clause of the row filter.

( â¦ recursive â¦ )

sensitive -> (boolean)

Specifies whether the row filter is sensitive.

createdAt -> (timestamp)

The timestamp at which the asset filter was created.

description -> (string)

The description of the asset filter.

domainId -> (string)

The ID of the domain where the asset filter was created.

effectiveColumnNames -> (list)

The column names of the asset filter.

(string)

effectiveRowFilter -> (string)

The row filter of the asset filter.

errorMessage -> (string)

The error message that is displayed if the action is not completed successfully.

id -> (string)

The ID of the asset filter.

name -> (string)

The name of the asset filter.

status -> (string)

The status of the asset filter.