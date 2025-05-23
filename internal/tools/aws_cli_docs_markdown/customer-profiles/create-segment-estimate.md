# create-segment-estimateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-segment-estimate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-segment-estimate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# create-segment-estimate

## Description

Creates a segment estimate query.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/CreateSegmentEstimate)

## Synopsis

```
create-segment-estimate
--domain-name <value>
--segment-query <value>
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

`--domain-name` (string)

The unique name of the domain.

`--segment-query` (structure)

The segment query for calculating a segment estimate.

Groups -> (list)

Holds the list of groups within the segment definition.

(structure)

Contains dimensions that determine what to segment on.

Dimensions -> (list)

Defines the attributes to segment on.

(tagged union structure)

Object that holds what profile and calculated attributes to segment on.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ProfileAttributes`, `CalculatedAttributes`.

ProfileAttributes -> (structure)

Object that holds the profile attributes to segment on.

AccountNumber -> (structure)

A field to describe values to segment on within account number.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

AdditionalInformation -> (structure)

A field to describe values to segment on within additional information.

DimensionType -> (string)

The action to segment with.

Values -> (list)

The values to apply the DimensionType on.

(string)

FirstName -> (structure)

A field to describe values to segment on within first name.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

LastName -> (structure)

A field to describe values to segment on within last name.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

MiddleName -> (structure)

A field to describe values to segment on within middle name.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

GenderString -> (structure)

A field to describe values to segment on within genderString.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

PartyTypeString -> (structure)

A field to describe values to segment on within partyTypeString.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

BirthDate -> (structure)

A field to describe values to segment on within birthDate.

DimensionType -> (string)

The action to segment with.

Values -> (list)

The values to apply the DimensionType on.

(string)

PhoneNumber -> (structure)

A field to describe values to segment on within phone number.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

BusinessName -> (structure)

A field to describe values to segment on within business name.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

BusinessPhoneNumber -> (structure)

A field to describe values to segment on within business phone number.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

HomePhoneNumber -> (structure)

A field to describe values to segment on within home phone number.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

MobilePhoneNumber -> (structure)

A field to describe values to segment on within mobile phone number.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

EmailAddress -> (structure)

A field to describe values to segment on within email address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

PersonalEmailAddress -> (structure)

A field to describe values to segment on within personal email address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

BusinessEmailAddress -> (structure)

A field to describe values to segment on within business email address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Address -> (structure)

A field to describe values to segment on within address.

City -> (structure)

The city belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Country -> (structure)

The country belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

County -> (structure)

The county belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

PostalCode -> (structure)

The postal code belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Province -> (structure)

The province belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

State -> (structure)

The state belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

ShippingAddress -> (structure)

A field to describe values to segment on within shipping address.

City -> (structure)

The city belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Country -> (structure)

The country belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

County -> (structure)

The county belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

PostalCode -> (structure)

The postal code belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Province -> (structure)

The province belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

State -> (structure)

The state belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

MailingAddress -> (structure)

A field to describe values to segment on within mailing address.

City -> (structure)

The city belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Country -> (structure)

The country belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

County -> (structure)

The county belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

PostalCode -> (structure)

The postal code belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Province -> (structure)

The province belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

State -> (structure)

The state belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

BillingAddress -> (structure)

A field to describe values to segment on within billing address.

City -> (structure)

The city belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Country -> (structure)

The country belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

County -> (structure)

The county belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

PostalCode -> (structure)

The postal code belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Province -> (structure)

The province belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

State -> (structure)

The state belonging to the address.

DimensionType -> (string)

The action to segment on.

Values -> (list)

The values to apply the DimensionType on.

(string)

Attributes -> (map)

A field to describe values to segment on within attributes.

key -> (string)

value -> (structure)

Object that segments on various Customer Profileâs fields.

DimensionType -> (string)

The action to segment with.

Values -> (list)

The values to apply the DimensionType on.

(string)

CalculatedAttributes -> (map)

Object that holds the calculated attributes to segment on.

key -> (string)

value -> (structure)

Object that segments on Customer Profileâs Calculated Attributes.

DimensionType -> (string)

The action to segment with.

Values -> (list)

The values to apply the DimensionType with.

(string)

ConditionOverrides -> (structure)

Applies the given condition over the initial Calculated Attributeâs definition.

Range -> (structure)

The relative time period over which data is included in the aggregation for this override.

Start -> (integer)

The start time of when to include objects.

End -> (integer)

The end time of when to include objects.

Unit -> (string)

The unit for start and end.

SourceSegments -> (list)

Defines the starting source of data.

(structure)

The source segments to build off of.

SegmentDefinitionName -> (string)

The unique name of the segment definition.

SourceType -> (string)

Defines how to interact with the source data.

Type -> (string)

Defines how to interact with the profiles found in the current filtering.

Include -> (string)

Define whether to include or exclude the profiles that fit the segment criteria.

JSON Syntax:

```
{
  "Groups": [
    {
      "Dimensions": [
        {
          "ProfileAttributes": {
            "AccountNumber": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "AdditionalInformation": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "FirstName": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "LastName": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "MiddleName": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "GenderString": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "PartyTypeString": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "BirthDate": {
              "DimensionType": "BEFORE"|"AFTER"|"BETWEEN"|"NOT_BETWEEN"|"ON",
              "Values": ["string", ...]
            },
            "PhoneNumber": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "BusinessName": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "BusinessPhoneNumber": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "HomePhoneNumber": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "MobilePhoneNumber": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "EmailAddress": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "PersonalEmailAddress": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "BusinessEmailAddress": {
              "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
              "Values": ["string", ...]
            },
            "Address": {
              "City": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Country": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "County": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "PostalCode": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Province": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "State": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              }
            },
            "ShippingAddress": {
              "City": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Country": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "County": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "PostalCode": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Province": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "State": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              }
            },
            "MailingAddress": {
              "City": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Country": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "County": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "PostalCode": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Province": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "State": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              }
            },
            "BillingAddress": {
              "City": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Country": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "County": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "PostalCode": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "Province": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              },
              "State": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH",
                "Values": ["string", ...]
              }
            },
            "Attributes": {"string": {
                  "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH"|"BEFORE"|"AFTER"|"BETWEEN"|"NOT_BETWEEN"|"ON"|"GREATER_THAN"|"LESS_THAN"|"GREATER_THAN_OR_EQUAL"|"LESS_THAN_OR_EQUAL"|"EQUAL",
                  "Values": ["string", ...]
                }
              ...}
          },
          "CalculatedAttributes": {"string": {
                "DimensionType": "INCLUSIVE"|"EXCLUSIVE"|"CONTAINS"|"BEGINS_WITH"|"ENDS_WITH"|"BEFORE"|"AFTER"|"BETWEEN"|"NOT_BETWEEN"|"ON"|"GREATER_THAN"|"LESS_THAN"|"GREATER_THAN_OR_EQUAL"|"LESS_THAN_OR_EQUAL"|"EQUAL",
                "Values": ["string", ...],
                "ConditionOverrides": {
                  "Range": {
                    "Start": integer,
                    "End": integer,
                    "Unit": "DAYS"
                  }
                }
              }
            ...}
        }
        ...
      ],
      "SourceSegments": [
        {
          "SegmentDefinitionName": "string"
        }
        ...
      ],
      "SourceType": "ALL"|"ANY"|"NONE",
      "Type": "ALL"|"ANY"|"NONE"
    }
    ...
  ],
  "Include": "ALL"|"ANY"|"NONE"
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

## Output

DomainName -> (string)

The unique name of the domain.

EstimateId -> (string)

A unique identifier for the resource. The value can be passed to `GetSegmentEstimate` to retrieve the result of segment estimate status.

StatusCode -> (integer)

The status code for the response.