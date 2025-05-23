# create-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [comprehend](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/index.html#cli-aws-comprehend) ]

# create-endpoint

## Description

Creates a model-specific endpoint for synchronous inference for a previously trained custom model For information about endpoints, see [Managing endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/comprehend-2017-11-27/CreateEndpoint)

## Synopsis

```
create-endpoint
--endpoint-name <value>
[--model-arn <value>]
--desired-inference-units <value>
[--client-request-token <value>]
[--tags <value>]
[--data-access-role-arn <value>]
[--flywheel-arn <value>]
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

`--endpoint-name` (string)

This is the descriptive suffix that becomes part of the `EndpointArn` used for all subsequent requests to this resource.

`--model-arn` (string)

The Amazon Resource Number (ARN) of the model to which the endpoint will be attached.

`--desired-inference-units` (integer)

The desired number of inference units to be used by the model using this endpoint. Each inference unit represents of a throughput of 100 characters per second.

`--client-request-token` (string)

An idempotency token provided by the customer. If this token matches a previous endpoint creation request, Amazon Comprehend will not return a `ResourceInUseException` .

`--tags` (list)

Tags to associate with the endpoint. A tag is a key-value pair that adds metadata to the endpoint. For example, a tag with âSalesâ as the key might be added to an endpoint to indicate its use by the sales department.

(structure)

A key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with the key-value pair âDepartmentâ:âSalesâ might be added to a resource to indicate its use by a particular department.

Key -> (string)

The initial part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use âDepartmentâ as the key portion of the pair, with multiple possible values such as âsales,â âlegal,â and âadministration.â

Value -> (string)

The second part of a key-value pair that forms a tag associated with a given resource. For instance, if you want to show which resources are used by which departments, you might use âDepartmentâ as the initial (key) portion of the pair, with a value of âsalesâ to indicate the sales department.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--data-access-role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to trained custom models encrypted with a customer managed key (ModelKmsKeyId).

`--flywheel-arn` (string)

The Amazon Resource Number (ARN) of the flywheel to which the endpoint will be attached.

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

**To create an endpoint for a custom model**

The following `create-endpoint` example creates an endpoint for synchronous inference for a previously trained custom model.

```
aws comprehend create-endpoint \
    --endpoint-name example-classifier-endpoint-1 \
    --model-arn arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier \
    --desired-inference-units 1
```

Output:

```
{
    "EndpointArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint-1"
}
```

For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html) in the *Amazon Comprehend Developer Guide*.

## Output

EndpointArn -> (string)

The Amazon Resource Number (ARN) of the endpoint being created.

ModelArn -> (string)

The Amazon Resource Number (ARN) of the model to which the endpoint is attached.