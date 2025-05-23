# batch-put-attributesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/batch-put-attributes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/batch-put-attributes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sdb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sdb/index.html#cli-aws-sdb) ]

# batch-put-attributes

## Description

The `BatchPutAttributes` operation creates or replaces attributes within one or more items. By using this operation, the client can perform multiple  PutAttribute operation with a single call. This helps yield savings in round trips and latencies, enabling Amazon SimpleDB to optimize requests and generally produce better throughput.

The client may specify the item name with the `Item.X.ItemName` parameter. The client may specify new attributes using a combination of the `Item.X.Attribute.Y.Name` and `Item.X.Attribute.Y.Value` parameters. The client may specify the first attribute for the first item using the parameters `Item.0.Attribute.0.Name` and `Item.0.Attribute.0.Value` , and for the second attribute for the first item by the parameters `Item.0.Attribute.1.Name` and `Item.0.Attribute.1.Value` , and so on.

Attributes are uniquely identified within an item by their name/value combination. For example, a single item can have the attributes `{ "first_name", "first_value" }` and `{ "first_name", "second_value" }` . However, it cannot have two attribute instances where both the `Item.X.Attribute.Y.Name` and `Item.X.Attribute.Y.Value` are the same.

Optionally, the requester can supply the `Replace` parameter for each individual value. Setting this value to `true` will cause the new attribute values to replace the existing attribute values. For example, if an item `I` has the attributes `{ 'a', '1' }, { 'b', '2'}` and `{ 'b', '3' }` and the requester does a BatchPutAttributes of `{'I', 'b', '4' }` with the Replace parameter set to true, the final attributes of the item will be `{ 'a', '1' }` and `{ 'b', '4' }` , replacing the previous values of the âbâ attribute with the new value.

### Warning

This operation is vulnerable to exceeding the maximum URL size when making a REST request using the HTTP GET method. This operation does not support conditions using `Expected.X.Name` , `Expected.X.Value` , or `Expected.X.Exists` .

You can execute multiple `BatchPutAttributes` operations and other operations in parallel. However, large numbers of concurrent `BatchPutAttributes` calls can result in Service Unavailable (503) responses.

The following limitations are enforced for this operation:

- 256 attribute name-value pairs per item
- 1 MB request size
- 1 billion attributes per domain
- 10 GB of total user data storage per domain
- 25 item limit per `BatchPutAttributes` operation

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sdb-2009-04-15/BatchPutAttributes)

## Synopsis

```
batch-put-attributes
--domain-name <value>
--items <value>
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
The name of the domain in which the attributes are being stored.

`--items` (list)
A list of items on which to perform the operation.(structure)

Name -> (string)

The name of the replaceable item.

Attributes -> (list)

The list of attributes for a replaceable item.

(structure)

Name -> (string)

The name of the replaceable attribute.

Value -> (string)

The value of the replaceable attribute.

Replace -> (boolean)

A flag specifying whether or not to replace the attribute/value pair or to add a new attribute/value pair. The default setting is `false` .

Shorthand Syntax:

```
Name=string,Attributes=[{Name=string,Value=string,Replace=boolean},{Name=string,Value=string,Replace=boolean}] ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Attributes": [
      {
        "Name": "string",
        "Value": "string",
        "Replace": true|false
      }
      ...
    ]
  }
  ...
]
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