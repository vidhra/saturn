# describe-connection-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/describe-connection-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/describe-connection-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# describe-connection-type

## Description

The `DescribeConnectionType` API provides full details of the supported options for a given connection type in Glue.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DescribeConnectionType)

## Synopsis

```
describe-connection-type
--connection-type <value>
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

`--connection-type` (string)

The name of the connection type to be described.

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

ConnectionType -> (string)

The name of the connection type.

Description -> (string)

A description of the connection type.

Capabilities -> (structure)

The supported authentication types, data interface types (compute environments), and data operations of the connector.

SupportedAuthenticationTypes -> (list)

A list of supported authentication types.

(string)

SupportedDataOperations -> (list)

A list of supported data operations.

(string)

SupportedComputeEnvironments -> (list)

A list of supported compute environments.

(string)

ConnectionProperties -> (map)

Connection properties which are common across compute environments.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

ConnectionOptions -> (map)

Returns properties that can be set when creating a connection in the `ConnectionInput.ConnectionProperties` . `ConnectionOptions` defines parameters that can be set in a Spark ETL script in the connection options map passed to a dataframe.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

AuthenticationConfiguration -> (structure)

The type of authentication used for the connection.

AuthenticationType -> (structure)

The type of authentication for a connection.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

SecretArn -> (structure)

The Amazon Resource Name (ARN) for the Secrets Manager.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

OAuth2Properties -> (map)

A map of key-value pairs for the OAuth2 properties. Each value is a a `Property` object.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

BasicAuthenticationProperties -> (map)

A map of key-value pairs for the OAuth2 properties. Each value is a a `Property` object.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

CustomAuthenticationProperties -> (map)

A map of key-value pairs for the custom authentication properties. Each value is a a `Property` object.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

ComputeEnvironmentConfigurations -> (map)

The compute environments that are supported by the connection.

key -> (string)

value -> (structure)

An object containing configuration for a compute environment (such as Spark, Python or Athena) returned by the `DescribeConnectionType` API.

Name -> (string)

A name for the compute environment configuration.

Description -> (string)

A description of the compute environment.

ComputeEnvironment -> (string)

The type of compute environment.

SupportedAuthenticationTypes -> (list)

The supported authentication types for the compute environment.

(string)

ConnectionOptions -> (map)

The parameters used as connection options for the compute environment.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

ConnectionPropertyNameOverrides -> (map)

The connection property name overrides for the compute environment.

key -> (string)

value -> (string)

ConnectionOptionNameOverrides -> (map)

The connection option name overrides for the compute environment.

key -> (string)

value -> (string)

ConnectionPropertiesRequiredOverrides -> (list)

The connection properties that are required as overrides for the compute environment.

(string)

PhysicalConnectionPropertiesRequired -> (boolean)

Indicates whether `PhysicalConnectionProperties` are required for the compute environment.

PhysicalConnectionRequirements -> (map)

Physical requirements for a connection, such as VPC, Subnet and Security Group specifications.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

AthenaConnectionProperties -> (map)

Connection properties specific to the Athena compute environment.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

PythonConnectionProperties -> (map)

Connection properties specific to the Python compute environment.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)

SparkConnectionProperties -> (map)

Connection properties specific to the Spark compute environment.

key -> (string)

value -> (structure)

An object that defines a connection type for a compute environment.

Name -> (string)

The name of the property.

Description -> (string)

A description of the property.

Required -> (boolean)

Indicates whether the property is required.

DefaultValue -> (string)

The default value for the property.

PropertyTypes -> (list)

Describes the type of property.

(string)

AllowedValues -> (list)

A list of `AllowedValue` objects representing the values allowed for the property.

(structure)

An object representing a value allowed for a property.

Description -> (string)

A description of the allowed value.

Value -> (string)

The value allowed for the property.

DataOperationScopes -> (list)

Indicates which data operations are applicable to the property.

(string)