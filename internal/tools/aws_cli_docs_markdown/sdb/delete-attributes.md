# delete-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/delete-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/delete-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/index.html#cli-aws-sdb) ]

# delete-attributes

## Description

Deletes one or more attributes associated with an item. If all attributes of the item are deleted, the item is deleted.

`DeleteAttributes` is an idempotent operation; running it multiple times on the same item or attribute does not result in an error response.

Because Amazon SimpleDB makes multiple copies of item data and uses an eventual consistency update model, performing a  GetAttributes or  Select operation (read) immediately after a `DeleteAttributes` or  PutAttributes operation (write) might not return updated item data.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/DeleteAttributes)

## Synopsis

```
delete-attributes
--domain-name <value>
--item-name <value>
[--attributes <value>]
[--expected <value>]
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
The name of the domain in which to perform the operation.

`--item-name` (string)
The name of the item. Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs.

`--attributes` (list)
A list of Attributes. Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items.(structure)

Name -> (string)

The name of the attribute.

AlternateNameEncoding -> (string)

Value -> (string)

The value of the attribute.

AlternateValueEncoding -> (string)

Shorthand Syntax:

```
Name=string,AlternateNameEncoding=string,Value=string,AlternateValueEncoding=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "AlternateNameEncoding": "string",
    "Value": "string",
    "AlternateValueEncoding": "string"
  }
  ...
]
```

`--expected` (structure)
The update condition which, if specified, determines whether the specified attributes will be deleted or not. The update condition must be satisfied in order for this request to be processed and the attributes to be deleted.Name -> (string)

The name of the attribute involved in the condition.

Value -> (string)

The value of an attribute. This value can only be specified when the `Exists` parameter is equal to `true` .

Exists -> (boolean)

A value specifying whether or not the specified attribute must exist with the specified value in order for the update condition to be satisfied. Specify `true` if the attribute must exist for the update condition to be satisfied. Specify `false` if the attribute should not exist in order for the update condition to be satisfied.

Shorthand Syntax:

```
Name=string,Value=string,Exists=boolean
```

JSON Syntax:

```
{
  "Name": "string",
  "Value": "string",
  "Exists": true|false
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