# test-transformerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/test-transformer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/test-transformer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# test-transformer

## Description

Use this operation to test a log transformer. You enter the transformer configuration and a set of log events to test with. The operation responds with an array that includes the original log events and the transformed versions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/TestTransformer)

## Synopsis

```
test-transformer
--transformer-config <value>
--log-event-messages <value>
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

`--transformer-config` (list)

This structure contains the configuration of this log transformer that you want to test. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.

(structure)

This structure contains the information about one processor in a log transformer.

addKeys -> (structure)

Use this parameter to include the [addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKeys) processor in your transformer.

entries -> (list)

An array of objects, where each object contains the information about one key to add to the log event.

(structure)

This object defines one key that will be added with the [addKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-addKey) processor.

key -> (string)

The key of the new entry to be added to the log event

value -> (string)

The value of the new entry to be added to the log event

overwriteIfExists -> (boolean)

Specifies whether to overwrite the value if the key already exists in the log event. If you omit this, the default is `false` .

copyValue -> (structure)

Use this parameter to include the [copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-copyValue) processor in your transformer.

entries -> (list)

An array of `CopyValueEntry` objects, where each object contains the information about one field value to copy.

(structure)

This object defines one value to be copied with the [copyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-copoyValue) processor.

source -> (string)

The key to copy.

target -> (string)

The key of the field to copy the value to.

overwriteIfExists -> (boolean)

Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false` .

csv -> (structure)

Use this parameter to include the [CSV](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-CSV) processor in your transformer.

quoteCharacter -> (string)

The character used used as a text qualifier for a single column of data. If you omit this, the double quotation mark `"` character is used.

delimiter -> (string)

The character used to separate each column in the original comma-separated value log event. If you omit this, the processor looks for the comma `,` character as the delimiter.

columns -> (list)

An array of names to use for the columns in the transformed log event.

If you omit this, default column names (`[column_1, column_2 ...]` ) are used.

(string)

source -> (string)

The path to the field in the log event that has the comma separated values to be parsed. If you omit this value, the whole log message is processed.

dateTimeConverter -> (structure)

Use this parameter to include the [datetimeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-datetimeConverter) processor in your transformer.

source -> (string)

The key to apply the date conversion to.

target -> (string)

The JSON field to store the result in.

targetFormat -> (string)

The datetime format to use for the converted data in the target field.

If you omit this, the default of `yyyy-MM-dd'T'HH:mm:ss.SSS'Z` is used.

matchPatterns -> (list)

A list of patterns to match against the `source` field.

(string)

sourceTimezone -> (string)

The time zone of the source field. If you omit this, the default used is the UTC zone.

targetTimezone -> (string)

The time zone of the target field. If you omit this, the default used is the UTC zone.

locale -> (string)

The locale of the source field. If you omit this, the default of `locale.ROOT` is used.

deleteKeys -> (structure)

Use this parameter to include the [deleteKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-deleteKeys) processor in your transformer.

withKeys -> (list)

The list of keys to delete.

(string)

grok -> (structure)

Use this parameter to include the [grok](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-grok) processor in your transformer.

source -> (string)

The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.

match -> (string)

The grok pattern to match against the log event. For a list of supported grok patterns, see [Supported grok patterns](https://docs.aws.amazon.com/mazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#Grok-Patterns) .

listToMap -> (structure)

Use this parameter to include the [listToMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-listToMap) processor in your transformer.

source -> (string)

The key in the log event that has a list of objects that will be converted to a map.

key -> (string)

The key of the field to be extracted as keys in the generated map

valueKey -> (string)

If this is specified, the values that you specify in this parameter will be extracted from the `source` objects and put into the values of the generated map. Otherwise, original objects in the source list will be put into the values of the generated map.

target -> (string)

The key of the field that will hold the generated map

flatten -> (boolean)

A Boolean value to indicate whether the list will be flattened into single items. Specify `true` to flatten the list. The default is `false`

flattenedElement -> (string)

If you set `flatten` to `true` , use `flattenedElement` to specify which element, `first` or `last` , to keep.

You must specify this parameter if `flatten` is `true`

lowerCaseString -> (structure)

Use this parameter to include the [lowerCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-lowerCaseString) processor in your transformer.

withKeys -> (list)

The array caontaining the keys of the fields to convert to lowercase.

(string)

moveKeys -> (structure)

Use this parameter to include the [moveKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKeys) processor in your transformer.

entries -> (list)

An array of objects, where each object contains the information about one key to move.

(structure)

This object defines one key that will be moved with the [moveKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKey) processor.

source -> (string)

The key to move.

target -> (string)

The key to move to.

overwriteIfExists -> (boolean)

Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false` .

parseCloudfront -> (structure)

Use this parameter to include the [parseCloudfront](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseCloudfront) processor in your transformer.

If you use this processor, it must be the first processor in your transformer.

source -> (string)

Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source` .

parseJSON -> (structure)

Use this parameter to include the [parseJSON](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseJSON) processor in your transformer.

source -> (string)

Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, `store.book`

destination -> (string)

The location to put the parsed key value pair into. If you omit this parameter, it is placed under the root node.

parseKeyValue -> (structure)

Use this parameter to include the [parseKeyValue](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseKeyValue) processor in your transformer.

source -> (string)

Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, `store.book`

destination -> (string)

The destination field to put the extracted key-value pairs into

fieldDelimiter -> (string)

The field delimiter string that is used between key-value pairs in the original log events. If you omit this, the ampersand `&` character is used.

keyValueDelimiter -> (string)

The delimiter string to use between the key and value in each pair in the transformed log event.

If you omit this, the equal `=` character is used.

keyPrefix -> (string)

If you want to add a prefix to all transformed keys, specify it here.

nonMatchValue -> (string)

A value to insert into the value field in the result, when a key-value pair is not successfully split.

overwriteIfExists -> (boolean)

Specifies whether to overwrite the value if the destination key already exists. If you omit this, the default is `false` .

parseRoute53 -> (structure)

Use this parameter to include the [parseRoute53](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseRoute53) processor in your transformer.

If you use this processor, it must be the first processor in your transformer.

source -> (string)

Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source` .

parsePostgres -> (structure)

Use this parameter to include the [parsePostGres](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parsePostGres) processor in your transformer.

If you use this processor, it must be the first processor in your transformer.

source -> (string)

Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source` .

parseVPC -> (structure)

Use this parameter to include the [parseVPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseVPC) processor in your transformer.

If you use this processor, it must be the first processor in your transformer.

source -> (string)

Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source` .

parseWAF -> (structure)

Use this parameter to include the [parseWAF](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-parseWAF) processor in your transformer.

If you use this processor, it must be the first processor in your transformer.

source -> (string)

Omit this parameter and the whole log message will be processed by this processor. No other value than `@message` is allowed for `source` .

renameKeys -> (structure)

Use this parameter to include the [renameKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKeys) processor in your transformer.

entries -> (list)

An array of `RenameKeyEntry` objects, where each object contains the information about a single key to rename.

(structure)

This object defines one key that will be renamed with the [renameKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKey) processor.

key -> (string)

The key to rename

renameTo -> (string)

The string to use for the new key name

overwriteIfExists -> (boolean)

Specifies whether to overwrite the existing value if the destination key already exists. The default is `false`

splitString -> (structure)

Use this parameter to include the [splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-splitString) processor in your transformer.

entries -> (list)

An array of `SplitStringEntry` objects, where each object contains the information about one field to split.

(structure)

This object defines one log field that will be split with the [splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-splitString) processor.

source -> (string)

The key of the field to split.

delimiter -> (string)

The separator characters to split the string entry on.

substituteString -> (structure)

Use this parameter to include the [substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString) processor in your transformer.

entries -> (list)

An array of objects, where each object contains the information about one key to match and replace.

(structure)

This object defines one log field key that will be replaced using the [substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString) processor.

source -> (string)

The key to modify

from -> (string)

The regular expression string to be replaced. Special regex characters such as [ and ] must be escaped using \ when using double quotes and with when using single quotes. For more information, see [Class Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html) on the Oracle web site.

to -> (string)

The string to be substituted for each match of `from`

trimString -> (structure)

Use this parameter to include the [trimString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-trimString) processor in your transformer.

withKeys -> (list)

The array containing the keys of the fields to trim.

(string)

typeConverter -> (structure)

Use this parameter to include the [typeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-typeConverter) processor in your transformer.

entries -> (list)

An array of `TypeConverterEntry` objects, where each object contains the information about one field to change the type of.

(structure)

This object defines one value type that will be converted using the [typeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-typeConverter) processor.

key -> (string)

The key with the value that is to be converted to a different type.

type -> (string)

The type to convert the field value to. Valid values are `integer` , `double` , `string` and `boolean` .

upperCaseString -> (structure)

Use this parameter to include the [upperCaseString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-upperCaseString) processor in your transformer.

withKeys -> (list)

The array of containing the keys of the field to convert to uppercase.

(string)

JSON Syntax:

```
[
  {
    "addKeys": {
      "entries": [
        {
          "key": "string",
          "value": "string",
          "overwriteIfExists": true|false
        }
        ...
      ]
    },
    "copyValue": {
      "entries": [
        {
          "source": "string",
          "target": "string",
          "overwriteIfExists": true|false
        }
        ...
      ]
    },
    "csv": {
      "quoteCharacter": "string",
      "delimiter": "string",
      "columns": ["string", ...],
      "source": "string"
    },
    "dateTimeConverter": {
      "source": "string",
      "target": "string",
      "targetFormat": "string",
      "matchPatterns": ["string", ...],
      "sourceTimezone": "string",
      "targetTimezone": "string",
      "locale": "string"
    },
    "deleteKeys": {
      "withKeys": ["string", ...]
    },
    "grok": {
      "source": "string",
      "match": "string"
    },
    "listToMap": {
      "source": "string",
      "key": "string",
      "valueKey": "string",
      "target": "string",
      "flatten": true|false,
      "flattenedElement": "first"|"last"
    },
    "lowerCaseString": {
      "withKeys": ["string", ...]
    },
    "moveKeys": {
      "entries": [
        {
          "source": "string",
          "target": "string",
          "overwriteIfExists": true|false
        }
        ...
      ]
    },
    "parseCloudfront": {
      "source": "string"
    },
    "parseJSON": {
      "source": "string",
      "destination": "string"
    },
    "parseKeyValue": {
      "source": "string",
      "destination": "string",
      "fieldDelimiter": "string",
      "keyValueDelimiter": "string",
      "keyPrefix": "string",
      "nonMatchValue": "string",
      "overwriteIfExists": true|false
    },
    "parseRoute53": {
      "source": "string"
    },
    "parsePostgres": {
      "source": "string"
    },
    "parseVPC": {
      "source": "string"
    },
    "parseWAF": {
      "source": "string"
    },
    "renameKeys": {
      "entries": [
        {
          "key": "string",
          "renameTo": "string",
          "overwriteIfExists": true|false
        }
        ...
      ]
    },
    "splitString": {
      "entries": [
        {
          "source": "string",
          "delimiter": "string"
        }
        ...
      ]
    },
    "substituteString": {
      "entries": [
        {
          "source": "string",
          "from": "string",
          "to": "string"
        }
        ...
      ]
    },
    "trimString": {
      "withKeys": ["string", ...]
    },
    "typeConverter": {
      "entries": [
        {
          "key": "string",
          "type": "boolean"|"integer"|"double"|"string"
        }
        ...
      ]
    },
    "upperCaseString": {
      "withKeys": ["string", ...]
    }
  }
  ...
]
```

`--log-event-messages` (list)

An array of the raw log events that you want to use to test this transformer.

(string)

Syntax:

```
"string" "string" ...
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

transformedLogs -> (list)

An array where each member of the array includes both the original version and the transformed version of one of the log events that you input.

(structure)

This structure contains information for one log event that has been processed by a log transformer.

eventNumber -> (long)

The event number.

eventMessage -> (string)

The original log event message before it was transformed.

transformedEventMessage -> (string)

The log event message after being transformed.