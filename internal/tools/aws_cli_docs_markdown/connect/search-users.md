# search-usersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/search-users.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/search-users.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# search-users

## Description

Searches users in an Amazon Connect instance, with optional filtering.

### Note

`AfterContactWorkTimeLimit` is returned in milliseconds.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/SearchUsers)

`search-users` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Users`

## Synopsis

```
search-users
--instance-id <value>
[--search-filter <value>]
[--search-criteria <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--search-filter` (structure)

Filters to be applied to search results.

TagFilter -> (structure)

An object that can be used to specify Tag conditions inside the `SearchFilter` . This accepts an `OR` of `AND` (List of List) input where:

- Top level list specifies conditions that need to be applied with `OR` operator
- Inner list specifies conditions that need to be applied with `AND` operator.

OrConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(list)

(structure)

A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123` .

TagKey -> (string)

The tag key in the tag condition.

TagValue -> (string)

The tag value in the tag condition.

AndConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123` .

TagKey -> (string)

The tag key in the tag condition.

TagValue -> (string)

The tag value in the tag condition.

TagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition.

TagKey -> (string)

The tag key in the tag condition.

TagValue -> (string)

The tag value in the tag condition.

UserAttributeFilter -> (structure)

An object that can be used to specify Tag conditions or Hierarchy Group conditions inside the SearchFilter.

This accepts an `OR` of `AND` (List of List) input where:

- The top level list specifies conditions that need to be applied with `OR` operator.
- The inner list specifies conditions that need to be applied with `AND` operator.

### Note

Only one field can be populated. This object canât be used along with TagFilter. Request can either contain TagFilter or UserAttributeFilter if SearchFilter is specified, combination of both is not supported and such request will throw AccessDeniedException.

OrConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(structure)

A list of conditions which would be applied together with an `AND` condition.

TagConditions -> (list)

A leaf node condition which can be used to specify a tag condition.

(structure)

A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123` .

TagKey -> (string)

The tag key in the tag condition.

TagValue -> (string)

The tag value in the tag condition.

HierarchyGroupCondition -> (structure)

A leaf node condition which can be used to specify a hierarchy group condition.

Value -> (string)

The value in the hierarchy group condition.

HierarchyGroupMatchType -> (string)

The type of hierarchy group match.

AndCondition -> (structure)

A list of conditions which would be applied together with an `AND` condition.

TagConditions -> (list)

A leaf node condition which can be used to specify a tag condition.

(structure)

A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123` .

TagKey -> (string)

The tag key in the tag condition.

TagValue -> (string)

The tag value in the tag condition.

HierarchyGroupCondition -> (structure)

A leaf node condition which can be used to specify a hierarchy group condition.

Value -> (string)

The value in the hierarchy group condition.

HierarchyGroupMatchType -> (string)

The type of hierarchy group match.

TagCondition -> (structure)

A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123` .

TagKey -> (string)

The tag key in the tag condition.

TagValue -> (string)

The tag value in the tag condition.

HierarchyGroupCondition -> (structure)

A leaf node condition which can be used to specify a hierarchy group condition.

Value -> (string)

The value in the hierarchy group condition.

HierarchyGroupMatchType -> (string)

The type of hierarchy group match.

JSON Syntax:

```
{
  "TagFilter": {
    "OrConditions": [
      [
        {
          "TagKey": "string",
          "TagValue": "string"
        }
        ...
      ]
      ...
    ],
    "AndConditions": [
      {
        "TagKey": "string",
        "TagValue": "string"
      }
      ...
    ],
    "TagCondition": {
      "TagKey": "string",
      "TagValue": "string"
    }
  },
  "UserAttributeFilter": {
    "OrConditions": [
      {
        "TagConditions": [
          {
            "TagKey": "string",
            "TagValue": "string"
          }
          ...
        ],
        "HierarchyGroupCondition": {
          "Value": "string",
          "HierarchyGroupMatchType": "EXACT"|"WITH_CHILD_GROUPS"
        }
      }
      ...
    ],
    "AndCondition": {
      "TagConditions": [
        {
          "TagKey": "string",
          "TagValue": "string"
        }
        ...
      ],
      "HierarchyGroupCondition": {
        "Value": "string",
        "HierarchyGroupMatchType": "EXACT"|"WITH_CHILD_GROUPS"
      }
    },
    "TagCondition": {
      "TagKey": "string",
      "TagValue": "string"
    },
    "HierarchyGroupCondition": {
      "Value": "string",
      "HierarchyGroupMatchType": "EXACT"|"WITH_CHILD_GROUPS"
    }
  }
}
```

`--search-criteria` (structure)

The search criteria to be used to return users.

### Note

The `name` and `description` fields support âcontainsâ queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.

OrConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

(structure)

The search criteria to be used to return users.

### Note

The `name` and `description` fields support âcontainsâ queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.

OrConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

( â¦ recursive â¦ )

AndConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

( â¦ recursive â¦ )

StringCondition -> (structure)

A leaf node condition which can be used to specify a string condition.

The currently supported values for `FieldName` are `Username` , `FirstName` , `LastName` , `RoutingProfileId` , `SecurityProfileId` , `ResourceId` .

FieldName -> (string)

The name of the field in the string condition.

Value -> (string)

The value of the string.

ComparisonType -> (string)

The type of comparison to be made when evaluating the string condition.

ListCondition -> (structure)

A leaf node condition which can be used to specify a List condition to search users with attributes included in Lists like Proficiencies.

TargetListType -> (string)

The type of target list that will be used to filter the users.

Conditions -> (list)

A list of Condition objects which would be applied together with an AND condition.

(structure)

A leaf node condition which can be used to specify a ProficiencyName, ProficiencyValue and ProficiencyLimit.

StringCondition -> (structure)

A leaf node condition which can be used to specify a string condition.

### Note

The currently supported values for `FieldName` are `name` and `value` .

FieldName -> (string)

The name of the field in the string condition.

Value -> (string)

The value of the string.

ComparisonType -> (string)

The type of comparison to be made when evaluating the string condition.

NumberCondition -> (structure)

A leaf node condition which can be used to specify a numeric condition.

FieldName -> (string)

The name of the field in the number condition.

MinValue -> (integer)

The minValue to be used while evaluating the number condition.

MaxValue -> (integer)

The maxValue to be used while evaluating the number condition.

ComparisonType -> (string)

The type of comparison to be made when evaluating the number condition.

HierarchyGroupCondition -> (structure)

A leaf node condition which can be used to specify a hierarchy group condition.

Value -> (string)

The value in the hierarchy group condition.

HierarchyGroupMatchType -> (string)

The type of hierarchy group match.

AndConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

(structure)

The search criteria to be used to return users.

### Note

The `name` and `description` fields support âcontainsâ queries with a minimum of 2 characters and a maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.

OrConditions -> (list)

A list of conditions which would be applied together with an `OR` condition.

( â¦ recursive â¦ )

AndConditions -> (list)

A list of conditions which would be applied together with an `AND` condition.

( â¦ recursive â¦ )

StringCondition -> (structure)

A leaf node condition which can be used to specify a string condition.

The currently supported values for `FieldName` are `Username` , `FirstName` , `LastName` , `RoutingProfileId` , `SecurityProfileId` , `ResourceId` .

FieldName -> (string)

The name of the field in the string condition.

Value -> (string)

The value of the string.

ComparisonType -> (string)

The type of comparison to be made when evaluating the string condition.

ListCondition -> (structure)

A leaf node condition which can be used to specify a List condition to search users with attributes included in Lists like Proficiencies.

TargetListType -> (string)

The type of target list that will be used to filter the users.

Conditions -> (list)

A list of Condition objects which would be applied together with an AND condition.

(structure)

A leaf node condition which can be used to specify a ProficiencyName, ProficiencyValue and ProficiencyLimit.

StringCondition -> (structure)

A leaf node condition which can be used to specify a string condition.

### Note

The currently supported values for `FieldName` are `name` and `value` .

FieldName -> (string)

The name of the field in the string condition.

Value -> (string)

The value of the string.

ComparisonType -> (string)

The type of comparison to be made when evaluating the string condition.

NumberCondition -> (structure)

A leaf node condition which can be used to specify a numeric condition.

FieldName -> (string)

The name of the field in the number condition.

MinValue -> (integer)

The minValue to be used while evaluating the number condition.

MaxValue -> (integer)

The maxValue to be used while evaluating the number condition.

ComparisonType -> (string)

The type of comparison to be made when evaluating the number condition.

HierarchyGroupCondition -> (structure)

A leaf node condition which can be used to specify a hierarchy group condition.

Value -> (string)

The value in the hierarchy group condition.

HierarchyGroupMatchType -> (string)

The type of hierarchy group match.

StringCondition -> (structure)

A leaf node condition which can be used to specify a string condition.

The currently supported values for `FieldName` are `Username` , `FirstName` , `LastName` , `RoutingProfileId` , `SecurityProfileId` , `ResourceId` .

FieldName -> (string)

The name of the field in the string condition.

Value -> (string)

The value of the string.

ComparisonType -> (string)

The type of comparison to be made when evaluating the string condition.

ListCondition -> (structure)

A leaf node condition which can be used to specify a List condition to search users with attributes included in Lists like Proficiencies.

TargetListType -> (string)

The type of target list that will be used to filter the users.

Conditions -> (list)

A list of Condition objects which would be applied together with an AND condition.

(structure)

A leaf node condition which can be used to specify a ProficiencyName, ProficiencyValue and ProficiencyLimit.

StringCondition -> (structure)

A leaf node condition which can be used to specify a string condition.

### Note

The currently supported values for `FieldName` are `name` and `value` .

FieldName -> (string)

The name of the field in the string condition.

Value -> (string)

The value of the string.

ComparisonType -> (string)

The type of comparison to be made when evaluating the string condition.

NumberCondition -> (structure)

A leaf node condition which can be used to specify a numeric condition.

FieldName -> (string)

The name of the field in the number condition.

MinValue -> (integer)

The minValue to be used while evaluating the number condition.

MaxValue -> (integer)

The maxValue to be used while evaluating the number condition.

ComparisonType -> (string)

The type of comparison to be made when evaluating the number condition.

HierarchyGroupCondition -> (structure)

A leaf node condition which can be used to specify a hierarchy group condition.

Value -> (string)

The value in the hierarchy group condition.

HierarchyGroupMatchType -> (string)

The type of hierarchy group match.

JSON Syntax:

```
{
  "OrConditions": [
    {
      "OrConditions": [
        { ... recursive ... }
        ...
      ],
      "AndConditions": [
        { ... recursive ... }
        ...
      ],
      "StringCondition": {
        "FieldName": "string",
        "Value": "string",
        "ComparisonType": "STARTS_WITH"|"CONTAINS"|"EXACT"
      },
      "ListCondition": {
        "TargetListType": "PROFICIENCIES",
        "Conditions": [
          {
            "StringCondition": {
              "FieldName": "string",
              "Value": "string",
              "ComparisonType": "STARTS_WITH"|"CONTAINS"|"EXACT"
            },
            "NumberCondition": {
              "FieldName": "string",
              "MinValue": integer,
              "MaxValue": integer,
              "ComparisonType": "GREATER_OR_EQUAL"|"GREATER"|"LESSER_OR_EQUAL"|"LESSER"|"EQUAL"|"NOT_EQUAL"|"RANGE"
            }
          }
          ...
        ]
      },
      "HierarchyGroupCondition": {
        "Value": "string",
        "HierarchyGroupMatchType": "EXACT"|"WITH_CHILD_GROUPS"
      }
    }
    ...
  ],
  "AndConditions": [
    {
      "OrConditions": [
        { ... recursive ... }
        ...
      ],
      "AndConditions": [
        { ... recursive ... }
        ...
      ],
      "StringCondition": {
        "FieldName": "string",
        "Value": "string",
        "ComparisonType": "STARTS_WITH"|"CONTAINS"|"EXACT"
      },
      "ListCondition": {
        "TargetListType": "PROFICIENCIES",
        "Conditions": [
          {
            "StringCondition": {
              "FieldName": "string",
              "Value": "string",
              "ComparisonType": "STARTS_WITH"|"CONTAINS"|"EXACT"
            },
            "NumberCondition": {
              "FieldName": "string",
              "MinValue": integer,
              "MaxValue": integer,
              "ComparisonType": "GREATER_OR_EQUAL"|"GREATER"|"LESSER_OR_EQUAL"|"LESSER"|"EQUAL"|"NOT_EQUAL"|"RANGE"
            }
          }
          ...
        ]
      },
      "HierarchyGroupCondition": {
        "Value": "string",
        "HierarchyGroupMatchType": "EXACT"|"WITH_CHILD_GROUPS"
      }
    }
    ...
  ],
  "StringCondition": {
    "FieldName": "string",
    "Value": "string",
    "ComparisonType": "STARTS_WITH"|"CONTAINS"|"EXACT"
  },
  "ListCondition": {
    "TargetListType": "PROFICIENCIES",
    "Conditions": [
      {
        "StringCondition": {
          "FieldName": "string",
          "Value": "string",
          "ComparisonType": "STARTS_WITH"|"CONTAINS"|"EXACT"
        },
        "NumberCondition": {
          "FieldName": "string",
          "MinValue": integer,
          "MaxValue": integer,
          "ComparisonType": "GREATER_OR_EQUAL"|"GREATER"|"LESSER_OR_EQUAL"|"LESSER"|"EQUAL"|"NOT_EQUAL"|"RANGE"
        }
      }
      ...
    ]
  },
  "HierarchyGroupCondition": {
    "Value": "string",
    "HierarchyGroupMatchType": "EXACT"|"WITH_CHILD_GROUPS"
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

Users -> (list)

Information about the users.

(structure)

Information about the returned users.

Arn -> (string)

The Amazon Resource Name (ARN) of the user.

DirectoryUserId -> (string)

The directory identifier of the user.

HierarchyGroupId -> (string)

The identifier of the userâs hierarchy group.

Id -> (string)

The identifier of the userâs summary.

IdentityInfo -> (structure)

The userâs first name and last name.

FirstName -> (string)

The userâs first name.

LastName -> (string)

The userâs last name.

PhoneConfig -> (structure)

Contains information about the phone configuration settings for a user.

PhoneType -> (string)

The phone type.

AutoAccept -> (boolean)

The Auto accept setting.

AfterContactWorkTimeLimit -> (integer)

The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you donât want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW.

### Note

When returned by a `SearchUsers` call, `AfterContactWorkTimeLimit` is returned in milliseconds.

DeskPhoneNumber -> (string)

The phone number for the userâs desk phone.

RoutingProfileId -> (string)

The identifier of the userâs routing profile.

SecurityProfileIds -> (list)

The identifiers of the userâs security profiles.

(string)

Tags -> (map)

The tags used to organize, track, or control access for this resource. For example, { âTagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

key -> (string)

value -> (string)

Username -> (string)

The name of the user.

NextToken -> (string)

If there are additional results, this is the token for the next set of results.

ApproximateTotalCount -> (long)

The total number of users who matched your search query.