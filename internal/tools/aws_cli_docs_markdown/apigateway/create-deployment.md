# create-deploymentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html#cli-aws-apigateway) ]

# create-deployment

## Description

Creates a Deployment resource, which makes a specified RestApi callable over the internet.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateDeployment)

## Synopsis

```
create-deployment
--rest-api-id <value>
[--stage-name <value>]
[--stage-description <value>]
[--description <value>]
[--cache-cluster-enabled | --no-cache-cluster-enabled]
[--cache-cluster-size <value>]
[--variables <value>]
[--canary-settings <value>]
[--tracing-enabled | --no-tracing-enabled]
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

`--rest-api-id` (string)

The string identifier of the associated RestApi.

`--stage-name` (string)

The name of the Stage resource for the Deployment resource to create.

`--stage-description` (string)

The description of the Stage resource for the Deployment resource to create.

`--description` (string)

The description for the Deployment resource to create.

`--cache-cluster-enabled` | `--no-cache-cluster-enabled` (boolean)

Enables a cache cluster for the Stage resource specified in the input.

`--cache-cluster-size` (string)

The stageâs cache capacity in GB. For more information about choosing a cache size, see [Enabling API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html) .

Possible values:

- `0.5`
- `1.6`
- `6.1`
- `13.5`
- `28.4`
- `58.2`
- `118`
- `237`

`--variables` (map)

A map that defines the stage variables for the Stage resource that is associated with the new deployment. Variable names can have alphanumeric and underscore characters, and the values must match `[A-Za-z0-9-._~:/?#&=,]+` .

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

`--canary-settings` (structure)

The input configuration for the canary deployment when the deployment is a canary release deployment.

percentTraffic -> (double)

The percentage (0.0-100.0) of traffic routed to the canary deployment.

stageVariableOverrides -> (map)

A stage variable overrides used for the canary release deployment. They can override existing stage variables or add new stage variables for the canary release deployment. These stage variables are represented as a string-to-string map between stage variable names and their values.

key -> (string)

value -> (string)

useStageCache -> (boolean)

A Boolean flag to indicate whether the canary release deployment uses the stage cache or not.

Shorthand Syntax:

```
percentTraffic=double,stageVariableOverrides={KeyName1=string,KeyName2=string},useStageCache=boolean
```

JSON Syntax:

```
{
  "percentTraffic": double,
  "stageVariableOverrides": {"string": "string"
    ...},
  "useStageCache": true|false
}
```

`--tracing-enabled` | `--no-tracing-enabled` (boolean)

Specifies whether active tracing with X-ray is enabled for the Stage.

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

**To deploy the configured resources for an API to a new Stage**

Command:

```
aws apigateway create-deployment --rest-api-id 1234123412 --stage-name dev --stage-description 'Development Stage' --description 'First deployment to the dev stage'
```

**To deploy the configured resources for an API to an existing stage**

Command:

```
aws apigateway create-deployment --rest-api-id 1234123412 --stage-name dev --description 'Second deployment to the dev stage'
```

**To deploy the configured resources for an API to an existing stage with Stage Variables**

aws apigateway create-deployment ârest-api-id 1234123412 âstage-name dev âdescription âThird deployment to the dev stageâ âvariables key=âvalueâ,otherKey=âotherValueâ

## Output

id -> (string)

The identifier for the deployment resource.

description -> (string)

The description for the deployment resource.

createdDate -> (timestamp)

The date and time that the deployment resource was created.

apiSummary -> (map)

A summary of the RestApi at the date and time that the deployment resource was created.

key -> (string)

value -> (map)

key -> (string)

value -> (structure)

Represents a summary of a Method resource, given a particular date and time.

authorizationType -> (string)

The methodâs authorization type. Valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a custom authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.

apiKeyRequired -> (boolean)

Specifies whether the method requires a valid ApiKey.