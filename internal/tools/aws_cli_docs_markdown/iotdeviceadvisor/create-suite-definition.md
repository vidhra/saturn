# create-suite-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/create-suite-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/create-suite-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotdeviceadvisor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotdeviceadvisor/index.html#cli-aws-iotdeviceadvisor) ]

# create-suite-definition

## Description

Creates a Device Advisor test suite.

Requires permission to access the [CreateSuiteDefinition](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)

## Synopsis

```
create-suite-definition
--suite-definition-configuration <value>
[--tags <value>]
[--client-token <value>]
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

`--suite-definition-configuration` (structure)

Creates a Device Advisor test suite with suite definition configuration.

suiteDefinitionName -> (string)

Gets the suite definition name. This is a required parameter.

devices -> (list)

Gets the devices configured.

(structure)

Information of a test device. A thing ARN, certificate ARN or device role ARN is required.

thingArn -> (string)

Lists deviceâs thing ARN.

certificateArn -> (string)

Lists deviceâs certificate ARN.

deviceRoleArn -> (string)

Lists deviceâs role ARN.

intendedForQualification -> (boolean)

Gets the tests intended for qualification in a suite.

isLongDurationTest -> (boolean)

Verifies if the test suite is a long duration test.

rootGroup -> (string)

Gets the test suite root group. This is a required parameter. For updating or creating the latest qualification suite, if `intendedForQualification` is set to true, `rootGroup` can be an empty string. If `intendedForQualification` is false, `rootGroup` cannot be an empty string. If `rootGroup` is empty, and `intendedForQualification` is set to true, all the qualification tests are included, and the configuration is default.

For a qualification suite, the minimum length is 0, and the maximum is 2048. For a non-qualification suite, the minimum length is 1, and the maximum is 2048.

devicePermissionRoleArn -> (string)

Gets the device permission ARN. This is a required parameter.

protocol -> (string)

Sets the MQTT protocol that is configured in the suite definition.

Shorthand Syntax:

```
suiteDefinitionName=string,devices=[{thingArn=string,certificateArn=string,deviceRoleArn=string},{thingArn=string,certificateArn=string,deviceRoleArn=string}],intendedForQualification=boolean,isLongDurationTest=boolean,rootGroup=string,devicePermissionRoleArn=string,protocol=string
```

JSON Syntax:

```
{
  "suiteDefinitionName": "string",
  "devices": [
    {
      "thingArn": "string",
      "certificateArn": "string",
      "deviceRoleArn": "string"
    }
    ...
  ],
  "intendedForQualification": true|false,
  "isLongDurationTest": true|false,
  "rootGroup": "string",
  "devicePermissionRoleArn": "string",
  "protocol": "MqttV3_1_1"|"MqttV5"|"MqttV3_1_1_OverWebSocket"|"MqttV5_OverWebSocket"
}
```

`--tags` (map)

The tags to be attached to the suite definition.

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

`--client-token` (string)

The client token for the test suite definition creation. This token is used for tracking test suite definition creation using retries and obtaining its status. This parameter is optional.

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

**Example 1: To create an IoT Device Advisor test suite**

The following `create-suite-definition` example creates a device advisor test suite in the AWS IoT with the specified suite definition configuration.

```
aws iotdeviceadvisor create-suite-definition \
    --suite-definition-configuration '{ \
        "suiteDefinitionName": "TestSuiteName", \
        "devices": [{"thingArn":"arn:aws:iot:us-east-1:123456789012:thing/MyIotThing"}], \
        "intendedForQualification": false, \
        "rootGroup": "{\"configuration\":{},\"tests\":[{\"name\":\"MQTT Connect\",\"configuration\":{\"EXECUTION_TIMEOUT\":120},\"tests\":[{\"name\":\"MQTT_Connect\",\"configuration\":{},\"test\":{\"id\":\"MQTT_Connect\",\"testCase\":null,\"version\":\"0.0.0\"}}]}]}", \
        "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole"}'
```

Output:

```
{
    "suiteDefinitionId": "0jtsgio7yenu",
    "suiteDefinitionArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/0jtsgio7yenu",
    "suiteDefinitionName": "TestSuiteName",
    "createdAt": "2022-12-02T11:38:13.263000-05:00"
}
```

For more information, see [Create a test suite definition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition) in the *AWS IoT Core Developer Guide*.

**Example 2: To create an IoT Device Advisor Latest Qualification test suite**

The following `create-suite-definition` example creates a device advisor qualification test suite with the latest version in the AWS IoT with the specified suite definition configuration.

```
aws iotdeviceadvisor create-suite-definition \
    --suite-definition-configuration '{ \
        "suiteDefinitionName": "TestSuiteName", \
        "devices": [{"thingArn":"arn:aws:iot:us-east-1:123456789012:thing/MyIotThing"}], \
        "intendedForQualification": true, \
        "rootGroup": "", \
        "devicePermissionRoleArn": "arn:aws:iam::123456789012:role/Myrole"}'
```

Output:

```
{
    "suiteDefinitionId": "txgsuolk2myj",
    "suiteDefinitionArn": "arn:aws:iotdeviceadvisor:us-east-1:123456789012:suitedefinition/txgsuolk2myj",
    "suiteDefinitionName": "TestSuiteName",
    "createdAt": "2022-12-02T11:38:13.263000-05:00"
}
```

For more information, see [Create a test suite definition](https://docs.aws.amazon.com/iot/latest/developerguide/device-advisor-workflow.html#device-advisor-workflow-create-suite-definition) in the *AWS IoT Core Developer Guide*.

## Output

suiteDefinitionId -> (string)

The UUID of the test suite created.

suiteDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the test suite.

suiteDefinitionName -> (string)

The suite definition name of the test suite. This is a required parameter.

createdAt -> (timestamp)

The timestamp of when the test suite was created.