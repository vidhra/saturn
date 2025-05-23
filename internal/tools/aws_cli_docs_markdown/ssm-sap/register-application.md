# register-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/register-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/register-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-sap](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-sap/index.html#cli-aws-ssm-sap) ]

# register-application

## Description

Register an SAP application with AWS Systems Manager for SAP. You must meet the following requirements before registering.

The SAP application you want to register with AWS Systems Manager for SAP is running on Amazon EC2.

AWS Systems Manager Agent must be setup on an Amazon EC2 instance along with the required IAM permissions.

Amazon EC2 instance(s) must have access to the secrets created in AWS Secrets Manager to manage SAP applications and components.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-sap-2018-05-10/RegisterApplication)

## Synopsis

```
register-application
--application-id <value>
--application-type <value>
--instances <value>
[--sap-instance-number <value>]
[--sid <value>]
[--tags <value>]
[--credentials <value>]
[--database-arn <value>]
[--components-info <value>]
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

`--application-id` (string)

The ID of the application.

`--application-type` (string)

The type of the application.

Possible values:

- `HANA`
- `SAP_ABAP`

`--instances` (list)

The Amazon EC2 instances on which your SAP application is running.

(string)

Syntax:

```
"string" "string" ...
```

`--sap-instance-number` (string)

The SAP instance number of the application.

`--sid` (string)

The System ID of the application.

`--tags` (map)

The tags to be attached to the SAP application.

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

`--credentials` (list)

The credentials of the SAP application.

(structure)

The credentials of your SAP application.

DatabaseName -> (string)

The name of the SAP HANA database.

CredentialType -> (string)

The type of the application credentials.

SecretId -> (string)

The secret ID created in AWS Secrets Manager to store the credentials of the SAP application.

Shorthand Syntax:

```
DatabaseName=string,CredentialType=string,SecretId=string ...
```

JSON Syntax:

```
[
  {
    "DatabaseName": "string",
    "CredentialType": "ADMIN",
    "SecretId": "string"
  }
  ...
]
```

`--database-arn` (string)

The Amazon Resource Name of the SAP HANA database.

`--components-info` (list)

This is an optional parameter for component details to which the SAP ABAP application is attached, such as Web Dispatcher.

This is an array of ApplicationComponent objects. You may input 0 to 5 items.

(structure)

This is information about the component of your SAP application, such as Web Dispatcher.

ComponentType -> (string)

This string is the type of the component.

Accepted value is `WD` .

Sid -> (string)

This string is the SAP System ID of the component.

Accepted values are alphanumeric.

Ec2InstanceId -> (string)

This is the Amazon EC2 instance on which your SAP component is running.

Accepted values are alphanumeric.

Shorthand Syntax:

```
ComponentType=string,Sid=string,Ec2InstanceId=string ...
```

JSON Syntax:

```
[
  {
    "ComponentType": "HANA"|"HANA_NODE"|"ABAP"|"ASCS"|"DIALOG"|"WEBDISP"|"WD"|"ERS",
    "Sid": "string",
    "Ec2InstanceId": "string"
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

Application -> (structure)

The application registered with AWS Systems Manager for SAP.

Id -> (string)

The ID of the application.

Type -> (string)

The type of the application.

Arn -> (string)

The Amazon Resource Name (ARN) of the application.

AppRegistryArn -> (string)

The Amazon Resource Name (ARN) of the Application Registry.

Status -> (string)

The status of the application.

DiscoveryStatus -> (string)

The latest discovery result for the application.

Components -> (list)

The components of the application.

(string)

LastUpdated -> (timestamp)

The time at which the application was last updated.

StatusMessage -> (string)

The status message.

AssociatedApplicationArns -> (list)

The Amazon Resource Names of the associated AWS Systems Manager for SAP applications.

(string)

OperationId -> (string)

The ID of the operation.