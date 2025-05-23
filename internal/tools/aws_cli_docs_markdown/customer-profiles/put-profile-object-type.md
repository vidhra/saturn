# put-profile-object-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# put-profile-object-type

## Description

Defines a ProfileObjectType.

To add or remove tags on an existing ObjectType, see [TagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html) /[UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/PutProfileObjectType)

## Synopsis

```
put-profile-object-type
--domain-name <value>
--object-type-name <value>
--description <value>
[--template-id <value>]
[--expiration-days <value>]
[--encryption-key <value>]
[--allow-profile-creation | --no-allow-profile-creation]
[--source-last-updated-timestamp-format <value>]
[--max-profile-object-count <value>]
[--fields <value>]
[--keys <value>]
[--tags <value>]
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

`--object-type-name` (string)

The name of the profile object type.

`--description` (string)

Description of the profile object type.

`--template-id` (string)

A unique identifier for the object template. For some attributes in the request, the service will use the default value from the object template when TemplateId is present. If these attributes are present in the request, the service may return a `BadRequestException` . These attributes include: AllowProfileCreation, SourceLastUpdatedTimestampFormat, Fields, and Keys. For example, if AllowProfileCreation is set to true when TemplateId is set, the service may return a `BadRequestException` .

`--expiration-days` (integer)

The number of days until the data in the object expires.

`--encryption-key` (string)

The customer-provided key to encrypt the profile object that will be created in this profile object type.

`--allow-profile-creation` | `--no-allow-profile-creation` (boolean)

Indicates whether a profile should be created when data is received if one doesnât exist for an object of this type. The default is `FALSE` . If the AllowProfileCreation flag is set to `FALSE` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE` , and if no match is found, then the service creates a new standard profile.

`--source-last-updated-timestamp-format` (string)

The format of your `sourceLastUpdatedTimestamp` that was previously set up.

`--max-profile-object-count` (integer)

The amount of profile object max count assigned to the object type

`--fields` (map)

A map of the name and ObjectType field.

key -> (string)

value -> (structure)

Represents a field in a ProfileObjectType.

Source -> (string)

A field of a ProfileObject. For example: _source.FirstName, where â_sourceâ is a ProfileObjectType of a Zendesk user and âFirstNameâ is a field in that ObjectType.

Target -> (string)

The location of the data in the standard ProfileObject model. For example: _profile.Address.PostalCode.

ContentType -> (string)

The content type of the field. Used for determining equality when searching.

Shorthand Syntax:

```
KeyName1=Source=string,Target=string,ContentType=string,KeyName2=Source=string,Target=string,ContentType=string
```

JSON Syntax:

```
{"string": {
      "Source": "string",
      "Target": "string",
      "ContentType": "STRING"|"NUMBER"|"PHONE_NUMBER"|"EMAIL_ADDRESS"|"NAME"
    }
  ...}
```

`--keys` (map)

A list of unique keys that can be used to map data to the profile.

key -> (string)

value -> (list)

(structure)

An object that defines the Key element of a ProfileObject. A Key is a special element that can be used to search for a customer profile.

StandardIdentifiers -> (list)

The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE, ASSET, CASE, or ORDER means that this key can be used to tie an object to a PROFILE, ASSET, CASE, or ORDER respectively. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.

(string)

FieldNames -> (list)

The reference for the key name of the fields map.

(string)

Shorthand Syntax:

```
KeyName1=[{StandardIdentifiers=[string,string],FieldNames=[string,string]},{StandardIdentifiers=[string,string],FieldNames=[string,string]}],KeyName2=[{StandardIdentifiers=[string,string],FieldNames=[string,string]},{StandardIdentifiers=[string,string],FieldNames=[string,string]}]
```

JSON Syntax:

```
{"string": [
      {
        "StandardIdentifiers": ["PROFILE"|"ASSET"|"CASE"|"ORDER"|"COMMUNICATION_RECORD"|"UNIQUE"|"SECONDARY"|"LOOKUP_ONLY"|"NEW_ONLY", ...],
        "FieldNames": ["string", ...]
      }
      ...
    ]
  ...}
```

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

ObjectTypeName -> (string)

The name of the profile object type.

Description -> (string)

Description of the profile object type.

TemplateId -> (string)

A unique identifier for the object template.

ExpirationDays -> (integer)

The number of days until the data in the object expires.

EncryptionKey -> (string)

The customer-provided key to encrypt the profile object that will be created in this profile object type.

AllowProfileCreation -> (boolean)

Indicates whether a profile should be created when data is received if one doesnât exist for an object of this type. The default is `FALSE` . If the AllowProfileCreation flag is set to `FALSE` , then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE` , and if no match is found, then the service creates a new standard profile.

SourceLastUpdatedTimestampFormat -> (string)

The format of your `sourceLastUpdatedTimestamp` that was previously set up in fields that were parsed using [SimpleDateFormat](https://docs.oracle.com/javase/10/docs/api/java/text/SimpleDateFormat.html) . If you have `sourceLastUpdatedTimestamp` in your field, you must set up `sourceLastUpdatedTimestampFormat` .

MaxProfileObjectCount -> (integer)

The amount of profile object max count assigned to the object type.

MaxAvailableProfileObjectCount -> (integer)

The amount of provisioned profile object max count available.

Fields -> (map)

A map of the name and ObjectType field.

key -> (string)

value -> (structure)

Represents a field in a ProfileObjectType.

Source -> (string)

A field of a ProfileObject. For example: _source.FirstName, where â_sourceâ is a ProfileObjectType of a Zendesk user and âFirstNameâ is a field in that ObjectType.

Target -> (string)

The location of the data in the standard ProfileObject model. For example: _profile.Address.PostalCode.

ContentType -> (string)

The content type of the field. Used for determining equality when searching.

Keys -> (map)

A list of unique keys that can be used to map data to the profile.

key -> (string)

value -> (list)

(structure)

An object that defines the Key element of a ProfileObject. A Key is a special element that can be used to search for a customer profile.

StandardIdentifiers -> (list)

The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE, ASSET, CASE, or ORDER means that this key can be used to tie an object to a PROFILE, ASSET, CASE, or ORDER respectively. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.

(string)

FieldNames -> (list)

The reference for the key name of the fields map.

(string)

CreatedAt -> (timestamp)

The timestamp of when the domain was created.

LastUpdatedAt -> (timestamp)

The timestamp of when the domain was most recently edited.

Tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)