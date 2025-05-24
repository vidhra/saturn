# create-asset-revisionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/create-asset-revision.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/create-asset-revision.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# create-asset-revision

## Description

Creates a revision of the asset.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/CreateAssetRevision)

## Synopsis

```
create-asset-revision
[--client-token <value>]
[--description <value>]
--domain-identifier <value>
[--forms-input <value>]
[--glossary-terms <value>]
--identifier <value>
--name <value>
[--prediction-configuration <value>]
[--type-revision <value>]
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

`--client-token` (string)

A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

`--description` (string)

The revised description of the asset.

`--domain-identifier` (string)

The unique identifier of the domain where the asset is being revised.

`--forms-input` (list)

The metadata forms to be attached to the asset as part of asset revision.

(structure)

The details of a metadata form.

content -> (string)

The content of the metadata form.

formName -> (string)

The name of the metadata form.

typeIdentifier -> (string)

The ID of the metadata form type.

typeRevision -> (string)

The revision of the metadata form type.

Shorthand Syntax:

```
content=string,formName=string,typeIdentifier=string,typeRevision=string ...
```

JSON Syntax:

```
[
  {
    "content": "string",
    "formName": "string",
    "typeIdentifier": "string",
    "typeRevision": "string"
  }
  ...
]
```

`--glossary-terms` (list)

The glossary terms to be attached to the asset as part of asset revision.

(string)

Syntax:

```
"string" "string" ...
```

`--identifier` (string)

The identifier of the asset.

`--name` (string)

Te revised name of the asset.

`--prediction-configuration` (structure)

The configuration of the automatically generated business-friendly metadata for the asset.

businessNameGeneration -> (structure)

The business name generation mechanism.

enabled -> (boolean)

Specifies whether the business name generation is enabled.

Shorthand Syntax:

```
businessNameGeneration={enabled=boolean}
```

JSON Syntax:

```
{
  "businessNameGeneration": {
    "enabled": true|false
  }
}
```

`--type-revision` (string)

The revision type of the asset.

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

createdAt -> (timestamp)

The timestamp of when the asset revision occured.

createdBy -> (string)

The Amazon DataZone user who performed the asset revision.

description -> (string)

The revised asset description.

domainId -> (string)

The unique identifier of the Amazon DataZone domain where the asset was revised.

externalIdentifier -> (string)

The external identifier of the asset.

firstRevisionCreatedAt -> (timestamp)

The timestamp of when the first asset revision occured.

firstRevisionCreatedBy -> (string)

The Amazon DataZone user who performed the first asset revision.

formsOutput -> (list)

The metadata forms that were attached to the asset as part of the asset revision.

(structure)

The details of a metadata form.

content -> (string)

The content of the metadata form.

formName -> (string)

The name of the metadata form.

typeName -> (string)

The name of the metadata form type.

typeRevision -> (string)

The revision of the metadata form type.

glossaryTerms -> (list)

The glossary terms that were attached to the asset as part of asset revision.

(string)

id -> (string)

The unique identifier of the asset revision.

latestTimeSeriesDataPointFormsOutput -> (list)

The latest data point that was imported into the time series form for the asset.

(structure)

The summary of the time series data points form.

contentSummary -> (string)

The content of the summary of the time series data points form.

formName -> (string)

The name of the time series data points summary form.

id -> (string)

The ID of the time series data points summary form.

timestamp -> (timestamp)

The timestamp of the time series data points summary form.

typeIdentifier -> (string)

The type ID of the time series data points summary form.

typeRevision -> (string)

The type revision of the time series data points summary form.

listing -> (structure)

The details of an asset published in an Amazon DataZone catalog.

listingId -> (string)

The identifier of an asset published in an Amazon DataZone catalog.

listingStatus -> (string)

The status of an asset published in an Amazon DataZone catalog.

name -> (string)

The revised name of the asset.

owningProjectId -> (string)

The unique identifier of the revised project that owns the asset.

predictionConfiguration -> (structure)

The configuration of the automatically generated business-friendly metadata for the asset.

businessNameGeneration -> (structure)

The business name generation mechanism.

enabled -> (boolean)

Specifies whether the business name generation is enabled.

readOnlyFormsOutput -> (list)

The read-only metadata forms that were attached to the asset as part of the asset revision.

(structure)

The details of a metadata form.

content -> (string)

The content of the metadata form.

formName -> (string)

The name of the metadata form.

typeName -> (string)

The name of the metadata form type.

typeRevision -> (string)

The revision of the metadata form type.

revision -> (string)

The revision of the asset.

typeIdentifier -> (string)

The identifier of the revision type.

typeRevision -> (string)

The revision type of the asset.