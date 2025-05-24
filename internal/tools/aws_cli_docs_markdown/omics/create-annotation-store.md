# create-annotation-storeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-annotation-store.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-annotation-store.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# create-annotation-store

## Description

Creates an annotation store.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/CreateAnnotationStore)

## Synopsis

```
create-annotation-store
[--reference <value>]
[--name <value>]
[--description <value>]
[--tags <value>]
[--version-name <value>]
[--sse-config <value>]
--store-format <value>
[--store-options <value>]
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

`--reference` (tagged union structure)

The genome reference for the storeâs annotations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `referenceArn`.

referenceArn -> (string)

The referenceâs ARN.

Shorthand Syntax:

```
referenceArn=string
```

JSON Syntax:

```
{
  "referenceArn": "string"
}
```

`--name` (string)

A name for the store.

`--description` (string)

A description for the store.

`--tags` (map)

Tags for the store.

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

`--version-name` (string)

The name given to an annotation store version to distinguish it from other versions.

`--sse-config` (structure)

Server-side encryption (SSE) settings for the store.

type -> (string)

The encryption type.

keyArn -> (string)

An encryption key ARN.

Shorthand Syntax:

```
type=string,keyArn=string
```

JSON Syntax:

```
{
  "type": "KMS",
  "keyArn": "string"
}
```

`--store-format` (string)

The annotation file format of the store.

Possible values:

- `GFF`
- `TSV`
- `VCF`

`--store-options` (tagged union structure)

File parsing options for the annotation store.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tsvStoreOptions`.

tsvStoreOptions -> (structure)

File settings for a TSV store.

annotationType -> (string)

The storeâs annotation type.

formatToHeader -> (map)

The storeâs header key to column name mapping.

key -> (string)

value -> (string)

schema -> (list)

The storeâs schema.

(map)

key -> (string)

value -> (string)

Shorthand Syntax:

```
tsvStoreOptions={annotationType=string,formatToHeader={KeyName1=string,KeyName2=string},schema=[{KeyName1=string,KeyName2=string},{KeyName1=string,KeyName2=string}]}
```

JSON Syntax:

```
{
  "tsvStoreOptions": {
    "annotationType": "GENERIC"|"CHR_POS"|"CHR_POS_REF_ALT"|"CHR_START_END_ONE_BASE"|"CHR_START_END_REF_ALT_ONE_BASE"|"CHR_START_END_ZERO_BASE"|"CHR_START_END_REF_ALT_ZERO_BASE",
    "formatToHeader": {"CHR"|"START"|"END"|"REF"|"ALT"|"POS": "string"
      ...},
    "schema": [
      {"string": "LONG"|"INT"|"STRING"|"FLOAT"|"DOUBLE"|"BOOLEAN"
        ...}
      ...
    ]
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

**Example 1: To create a VCF annotation store**

The following `create-annotation-store` example creates a VCF format annotation store.

```
aws omics create-annotation-store \
    --name my_ann_store \
    --store-format VCF \
    --reference referenceArn=arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890
```

Output:

```
{
    "creationTime": "2022-11-23T22:48:39.226492Z",
    "id": "0a91xmplc71f",
    "name": "my_ann_store",
    "reference": {
        "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890"
    },
    "status": "CREATING",
    "storeFormat": "VCF"
}
```

**Example 2: To create a TSV annotation store**

The following `create-annotation-store` example creates a TSV format annotation store.

```
aws omics create-annotation-store \
    --name tsv_ann_store \
    --store-format TSV \
    --reference referenceArn=arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890 \
    --store-options file://tsv-store-options.json
```

`tsv-store-options.json` configures format options for annotations.

```
{
    "tsvStoreOptions": {
        "annotationType": "CHR_START_END_ZERO_BASE",
        "formatToHeader": {
            "CHR": "chromosome",
            "START": "start",
            "END": "end"
        },
        "schema": [
            {
                "chromosome": "STRING"
            },
            {
                "start": "LONG"
            },
            {
                "end": "LONG"
            },
            {
                "name": "STRING"
            }
        ]
    }
}
```

Output:

```
{
    "creationTime": "2022-11-30T01:28:08.525586Z",
    "id": "861cxmpl96b0",
    "name": "tsv_ann_store",
    "reference": {
        "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890"
    },
    "status": "CREATING",
    "storeFormat": "TSV",
    "storeOptions": {
        "tsvStoreOptions": {
            "annotationType": "CHR_START_END_ZERO_BASE",
            "formatToHeader": {
                "CHR": "chromosome",
                "END": "end",
                "START": "start"
            },
            "schema": [
                {
                    "chromosome": "STRING"
                },
                {
                    "start": "LONG"
                },
                {
                    "end": "LONG"
                },
                {
                    "name": "STRING"
                }
            ]
        }
    }
}
```

For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html) in the Amazon Omics Developer Guide.

## Output

id -> (string)

The storeâs ID.

reference -> (tagged union structure)

The storeâs genome reference. Required for all stores except TSV format with generic annotations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `referenceArn`.

referenceArn -> (string)

The referenceâs ARN.

storeFormat -> (string)

The annotation file format of the store.

storeOptions -> (tagged union structure)

The storeâs file parsing options.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `tsvStoreOptions`.

tsvStoreOptions -> (structure)

File settings for a TSV store.

annotationType -> (string)

The storeâs annotation type.

formatToHeader -> (map)

The storeâs header key to column name mapping.

key -> (string)

value -> (string)

schema -> (list)

The storeâs schema.

(map)

key -> (string)

value -> (string)

status -> (string)

The storeâs status.

name -> (string)

The storeâs name.

versionName -> (string)

The name given to an annotation store version to distinguish it from other versions.

creationTime -> (timestamp)

When the store was created.