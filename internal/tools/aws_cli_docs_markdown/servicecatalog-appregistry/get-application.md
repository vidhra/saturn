# get-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog-appregistry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/index.html#cli-aws-servicecatalog-appregistry) ]

# get-application

## Description

Retrieves metadata information about one of your applications. The application can be specified by its ARN, ID, or name (which is unique within one account in one region at a given point in time). Specify by ARN or ID in automated workflows if you want to make sure that the exact same application is returned or a `ResourceNotFoundException` is thrown, avoiding the ABA addressing problem.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/AWS242AppRegistry-2020-06-24/GetApplication)

## Synopsis

```
get-application
--application <value>
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

`--application` (string)

The name, ID, or ARN of the application.

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

**To get an application**

The following `get-application` example retrieves metadata information about a specific application in your AWS account.

```
aws servicecatalog-appregistry get-application \
    --application "ExampleApplication"
```

Output:

```
{
    "id": "0ars38r6btoohvpvd9gqrptt9l",
    "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/0ars38r6btoohvpvd9gqrptt9l",
    "name": "ExampleApplication",
    "creationTime": "2023-02-28T21:10:10.820000+00:00",
    "lastUpdateTime": "2023-02-28T21:10:10.820000+00:00",
    "associatedResourceCount": 0,
    "tags": {
        "aws:servicecatalog:applicationName": "ExampleApplication"
    },
    "integrations": {
        "resourceGroup": {
            "state": "CREATE_COMPLETE",
            "arn": "arn:aws:resource-groups:us-west-2:813737243517:group/AWS_AppRegistry_Application-ExampleApplication"
        }
    }
}
```

For more information, see [Using Application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-app-details.html) in the *AWS Service Catalog AppRegistry Administrator Guide*.

## Output

id -> (string)

The identifier of the application.

arn -> (string)

The Amazon resource name (ARN) that specifies the application across services.

name -> (string)

The name of the application. The name must be unique in the region in which you are creating the application.

description -> (string)

The description of the application.

creationTime -> (timestamp)

The ISO-8601 formatted timestamp of the moment when the application was created.

lastUpdateTime -> (timestamp)

The ISO-8601 formatted timestamp of the moment when the application was last updated.

associatedResourceCount -> (integer)

The number of top-level resources that were registered as part of this application.

tags -> (map)

Key-value pairs associated with the application.

key -> (string)

value -> (string)

integrations -> (structure)

The information about the integration of the application with other services, such as Resource Groups.

resourceGroup -> (structure)

The information about the resource group integration.

state -> (string)

The state of the propagation process for the resource group. The states includes:

`CREATING` if the resource group is in the process of being created.

`CREATE_COMPLETE` if the resource group was created successfully.

`CREATE_FAILED` if the resource group failed to be created.

`UPDATING` if the resource group is in the process of being updated.

`UPDATE_COMPLETE` if the resource group updated successfully.

`UPDATE_FAILED` if the resource group could not update successfully.

arn -> (string)

The Amazon resource name (ARN) of the resource group.

errorMessage -> (string)

The error message that generates when the propagation process for the resource group fails.

applicationTagResourceGroup -> (structure)

The information about the resource group integration.

state -> (string)

The state of the propagation process for the resource group. The states includes:

`CREATING` if the resource group is in the process of being created.

`CREATE_COMPLETE` if the resource group was created successfully.

`CREATE_FAILED` if the resource group failed to be created.

`UPDATING` if the resource group is in the process of being updated.

`UPDATE_COMPLETE` if the resource group updated successfully.

`UPDATE_FAILED` if the resource group could not update successfully.

arn -> (string)

The Amazon resource name (ARN) of the resource group.

errorMessage -> (string)

The error message that generates when the propagation process for the resource group fails.

applicationTag -> (map)

A key-value pair that identifies an associated resource.

key -> (string)

value -> (string)