# update-classifierÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-classifier.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-classifier.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# update-classifier

## Description

Modifies an existing classifier (a `GrokClassifier` , an `XMLClassifier` , a `JsonClassifier` , or a `CsvClassifier` , depending on which field is present).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateClassifier)

## Synopsis

```
update-classifier
[--grok-classifier <value>]
[--xml-classifier <value>]
[--json-classifier <value>]
[--csv-classifier <value>]
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

`--grok-classifier` (structure)

A `GrokClassifier` object with updated fields.

Name -> (string)

The name of the `GrokClassifier` .

Classification -> (string)

An identifier of the data format that the classifier matches, such as Twitter, JSON, Omniture logs, Amazon CloudWatch Logs, and so on.

GrokPattern -> (string)

The grok pattern used by this classifier.

CustomPatterns -> (string)

Optional custom grok patterns used by this classifier.

Shorthand Syntax:

```
Name=string,Classification=string,GrokPattern=string,CustomPatterns=string
```

JSON Syntax:

```
{
  "Name": "string",
  "Classification": "string",
  "GrokPattern": "string",
  "CustomPatterns": "string"
}
```

`--xml-classifier` (structure)

An `XMLClassifier` object with updated fields.

Name -> (string)

The name of the classifier.

Classification -> (string)

An identifier of the data format that the classifier matches.

RowTag -> (string)

The XML tag designating the element that contains each record in an XML document being parsed. This cannot identify a self-closing element (closed by `/>` ). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, `<row item_a="A" item_b="B"></row>` is okay, but `<row item_a="A" item_b="B" />` is not).

Shorthand Syntax:

```
Name=string,Classification=string,RowTag=string
```

JSON Syntax:

```
{
  "Name": "string",
  "Classification": "string",
  "RowTag": "string"
}
```

`--json-classifier` (structure)

A `JsonClassifier` object with updated fields.

Name -> (string)

The name of the classifier.

JsonPath -> (string)

A `JsonPath` string defining the JSON data for the classifier to classify. Glue supports a subset of JsonPath, as described in [Writing JsonPath Custom Classifiers](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json) .

Shorthand Syntax:

```
Name=string,JsonPath=string
```

JSON Syntax:

```
{
  "Name": "string",
  "JsonPath": "string"
}
```

`--csv-classifier` (structure)

A `CsvClassifier` object with updated fields.

Name -> (string)

The name of the classifier.

Delimiter -> (string)

A custom symbol to denote what separates each column entry in the row.

QuoteSymbol -> (string)

A custom symbol to denote what combines content into a single column value. It must be different from the column delimiter.

ContainsHeader -> (string)

Indicates whether the CSV file contains a header.

Header -> (list)

A list of strings representing column names.

(string)

DisableValueTrimming -> (boolean)

Specifies not to trim values before identifying the type of column values. The default value is true.

AllowSingleColumn -> (boolean)

Enables the processing of files that contain only one column.

CustomDatatypeConfigured -> (boolean)

Specifies the configuration of custom datatypes.

CustomDatatypes -> (list)

Specifies a list of supported custom datatypes.

(string)

Serde -> (string)

Sets the SerDe for processing CSV in the classifier, which will be applied in the Data Catalog. Valid values are `OpenCSVSerDe` , `LazySimpleSerDe` , and `None` . You can specify the `None` value when you want the crawler to do the detection.

Shorthand Syntax:

```
Name=string,Delimiter=string,QuoteSymbol=string,ContainsHeader=string,Header=string,string,DisableValueTrimming=boolean,AllowSingleColumn=boolean,CustomDatatypeConfigured=boolean,CustomDatatypes=string,string,Serde=string
```

JSON Syntax:

```
{
  "Name": "string",
  "Delimiter": "string",
  "QuoteSymbol": "string",
  "ContainsHeader": "UNKNOWN"|"PRESENT"|"ABSENT",
  "Header": ["string", ...],
  "DisableValueTrimming": true|false,
  "AllowSingleColumn": true|false,
  "CustomDatatypeConfigured": true|false,
  "CustomDatatypes": ["string", ...],
  "Serde": "OpenCSVSerDe"|"LazySimpleSerDe"|"None"
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

None