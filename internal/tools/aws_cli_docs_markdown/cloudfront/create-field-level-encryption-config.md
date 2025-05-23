# create-field-level-encryption-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# create-field-level-encryption-config

## Description

Create a new field-level encryption configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig)

## Synopsis

```
create-field-level-encryption-config
--field-level-encryption-config <value>
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

`--field-level-encryption-config` (structure)

The request to create a new field-level encryption configuration.

CallerReference -> (string)

A unique number that ensures the request canât be replayed.

Comment -> (string)

An optional comment about the configuration. The comment cannot be longer than 128 characters.

QueryArgProfileConfig -> (structure)

A complex data type that specifies when to forward content if a profile isnât found and the profile that can be provided as a query argument in a request.

ForwardWhenQueryArgProfileIsUnknown -> (boolean)

Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles -> (structure)

Profiles specified for query argument-profile mapping for field-level encryption.

Quantity -> (integer)

Number of profiles for query argument-profile mapping for field-level encryption.

Items -> (list)

Number of items for query argument-profile mapping for field-level encryption.

(structure)

Query argument-profile mapping for field-level encryption.

QueryArg -> (string)

Query argument for field-level encryption query argument-profile mapping.

ProfileId -> (string)

ID of profile to use for field-level encryption query argument-profile mapping

ContentTypeProfileConfig -> (structure)

A complex data type that specifies when to forward content if a content type isnât recognized and profiles to use as by default in a request if a query argument doesnât specify a profile to use.

ForwardWhenContentTypeIsUnknown -> (boolean)

The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles -> (structure)

The configuration for a field-level encryption content type-profile.

Quantity -> (integer)

The number of field-level encryption content type-profile mappings.

Items -> (list)

Items in a field-level encryption content type-profile mapping.

(structure)

A field-level encryption content type profile.

Format -> (string)

The format for a field-level encryption content type-profile mapping.

ProfileId -> (string)

The profile ID for a field-level encryption content type-profile mapping.

ContentType -> (string)

The content type for a field-level encryption content type-profile mapping.

JSON Syntax:

```
{
  "CallerReference": "string",
  "Comment": "string",
  "QueryArgProfileConfig": {
    "ForwardWhenQueryArgProfileIsUnknown": true|false,
    "QueryArgProfiles": {
      "Quantity": integer,
      "Items": [
        {
          "QueryArg": "string",
          "ProfileId": "string"
        }
        ...
      ]
    }
  },
  "ContentTypeProfileConfig": {
    "ForwardWhenContentTypeIsUnknown": true|false,
    "ContentTypeProfiles": {
      "Quantity": integer,
      "Items": [
        {
          "Format": "URLEncoded",
          "ProfileId": "string",
          "ContentType": "string"
        }
        ...
      ]
    }
  }
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

**To create a CloudFront field-level encryption configuration**

The following example creates a field-level encryption configuration by
providing the configuration parameters in a JSON file named
`fle-config.json`. Before you can create a field-level encryption
configuration, you must have a field-level encryption profile. To create a
profile, see the [create-field-level-encryption-profile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-profile.html) command.

For more information about CloudFront field-level
encryption, see
[Using Field-Level Encryption to Help Protect Sensitive Data](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)
in the *Amazon CloudFront Developer Guide*.

```
aws cloudfront create-field-level-encryption-config \
    --field-level-encryption-config file://fle-config.json
```

The file `fle-config.json` is a JSON document in the current
folder that contains the following:

```
{
    "CallerReference": "cli-example",
    "Comment": "Example FLE configuration",
    "QueryArgProfileConfig": {
        "ForwardWhenQueryArgProfileIsUnknown": true,
        "QueryArgProfiles": {
            "Quantity": 0
        }
    },
    "ContentTypeProfileConfig": {
        "ForwardWhenContentTypeIsUnknown": true,
        "ContentTypeProfiles": {
            "Quantity": 1,
            "Items": [
                {
                    "Format": "URLEncoded",
                    "ProfileId": "P280MFCLSYOCVU",
                    "ContentType": "application/x-www-form-urlencoded"
                }
            ]
        }
    }
}
```

Output:

```
{
    "Location": "https://cloudfront.amazonaws.com/2019-03-26/field-level-encryption/C3KM2WVD605UAY",
    "ETag": "E2P4Z4VU7TY5SG",
    "FieldLevelEncryption": {
        "Id": "C3KM2WVD605UAY",
        "LastModifiedTime": "2019-12-10T21:30:18.974Z",
        "FieldLevelEncryptionConfig": {
            "CallerReference": "cli-example",
            "Comment": "Example FLE configuration",
            "QueryArgProfileConfig": {
                "ForwardWhenQueryArgProfileIsUnknown": true,
                "QueryArgProfiles": {
                    "Quantity": 0,
                    "Items": []
                }
            },
            "ContentTypeProfileConfig": {
                "ForwardWhenContentTypeIsUnknown": true,
                "ContentTypeProfiles": {
                    "Quantity": 1,
                    "Items": [
                        {
                            "Format": "URLEncoded",
                            "ProfileId": "P280MFCLSYOCVU",
                            "ContentType": "application/x-www-form-urlencoded"
                        }
                    ]
                }
            }
        }
    }
}
```

## Output

FieldLevelEncryption -> (structure)

Returned when you create a new field-level encryption configuration.

Id -> (string)

The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.

LastModifiedTime -> (timestamp)

The last time the field-level encryption configuration was changed.

FieldLevelEncryptionConfig -> (structure)

A complex data type that includes the profile configurations specified for field-level encryption.

CallerReference -> (string)

A unique number that ensures the request canât be replayed.

Comment -> (string)

An optional comment about the configuration. The comment cannot be longer than 128 characters.

QueryArgProfileConfig -> (structure)

A complex data type that specifies when to forward content if a profile isnât found and the profile that can be provided as a query argument in a request.

ForwardWhenQueryArgProfileIsUnknown -> (boolean)

Flag to set if you want a request to be forwarded to the origin even if the profile specified by the field-level encryption query argument, fle-profile, is unknown.

QueryArgProfiles -> (structure)

Profiles specified for query argument-profile mapping for field-level encryption.

Quantity -> (integer)

Number of profiles for query argument-profile mapping for field-level encryption.

Items -> (list)

Number of items for query argument-profile mapping for field-level encryption.

(structure)

Query argument-profile mapping for field-level encryption.

QueryArg -> (string)

Query argument for field-level encryption query argument-profile mapping.

ProfileId -> (string)

ID of profile to use for field-level encryption query argument-profile mapping

ContentTypeProfileConfig -> (structure)

A complex data type that specifies when to forward content if a content type isnât recognized and profiles to use as by default in a request if a query argument doesnât specify a profile to use.

ForwardWhenContentTypeIsUnknown -> (boolean)

The setting in a field-level encryption content type-profile mapping that specifies what to do when an unknown content type is provided for the profile. If true, content is forwarded without being encrypted when the content type is unknown. If false (the default), an error is returned when the content type is unknown.

ContentTypeProfiles -> (structure)

The configuration for a field-level encryption content type-profile.

Quantity -> (integer)

The number of field-level encryption content type-profile mappings.

Items -> (list)

Items in a field-level encryption content type-profile mapping.

(structure)

A field-level encryption content type profile.

Format -> (string)

The format for a field-level encryption content type-profile mapping.

ProfileId -> (string)

The profile ID for a field-level encryption content type-profile mapping.

ContentType -> (string)

The content type for a field-level encryption content type-profile mapping.

Location -> (string)

The fully qualified URI of the new configuration resource just created.

ETag -> (string)

The current version of the field level encryption configuration. For example: `E2QWRUHAPOMQZL` .