# update-test-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/update-test-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/update-test-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apptest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apptest/index.html#cli-aws-apptest) ]

# update-test-configuration

## Description

Updates a test configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apptest-2022-12-06/UpdateTestConfiguration)

## Synopsis

```
update-test-configuration
--test-configuration-id <value>
[--description <value>]
[--resources <value>]
[--properties <value>]
[--service-settings <value>]
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

`--test-configuration-id` (string)

The test configuration ID of the test configuration.

`--description` (string)

The description of the test configuration.

`--resources` (list)

The resources of the test configuration.

(structure)

Specifies a resource.

name -> (string)

The name of the resource.

type -> (tagged union structure)

The type of the resource.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `cloudFormation`, `m2ManagedApplication`, `m2NonManagedApplication`.

cloudFormation -> (structure)

The CloudFormation template of the resource type.

templateLocation -> (string)

The template location of the CloudFormation template.

parameters -> (map)

The CloudFormation properties in the CloudFormation template.

key -> (string)

value -> (string)

m2ManagedApplication -> (structure)

The AWS Mainframe Modernization managed application of the resource type.

applicationId -> (string)

The application ID of the AWS Mainframe Modernization managed application.

runtime -> (string)

The runtime of the AWS Mainframe Modernization managed application.

vpcEndpointServiceName -> (string)

The VPC endpoint service name of the AWS Mainframe Modernization managed application.

listenerPort -> (string)

The listener port of the AWS Mainframe Modernization managed application.

m2NonManagedApplication -> (structure)

The AWS Mainframe Modernization non-managed application of the resource type.

vpcEndpointServiceName -> (string)

The VPC endpoint service name of the AWS Mainframe Modernization non-managed application.

listenerPort -> (string)

The listener port of the AWS Mainframe Modernization non-managed application.

runtime -> (string)

The runtime of the AWS Mainframe Modernization non-managed application.

webAppName -> (string)

The web application name of the AWS Mainframe Modernization non-managed application.

Shorthand Syntax:

```
name=string,type={cloudFormation={templateLocation=string,parameters={KeyName1=string,KeyName2=string}},m2ManagedApplication={applicationId=string,runtime=string,vpcEndpointServiceName=string,listenerPort=string},m2NonManagedApplication={vpcEndpointServiceName=string,listenerPort=string,runtime=string,webAppName=string}} ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "type": {
      "cloudFormation": {
        "templateLocation": "string",
        "parameters": {"string": "string"
          ...}
      },
      "m2ManagedApplication": {
        "applicationId": "string",
        "runtime": "MicroFocus",
        "vpcEndpointServiceName": "string",
        "listenerPort": "string"
      },
      "m2NonManagedApplication": {
        "vpcEndpointServiceName": "string",
        "listenerPort": "string",
        "runtime": "BluAge",
        "webAppName": "string"
      }
    }
  }
  ...
]
```

`--properties` (map)

The properties of the test configuration.

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

`--service-settings` (structure)

The service settings of the test configuration.

kmsKeyId -> (string)

The KMS key ID of the service settings.

Shorthand Syntax:

```
kmsKeyId=string
```

JSON Syntax:

```
{
  "kmsKeyId": "string"
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

testConfigurationId -> (string)

The configuration ID of the test configuration.

testConfigurationVersion -> (integer)

The configuration version of the test configuration.