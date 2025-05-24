# update-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# update-service

## Description

Edit a service description or use a spec to add and delete service instances.

### Note

Existing service instances and the service pipeline *canât* be edited using this API. They can only be deleted.

Use the `description` parameter to modify the description.

Edit the `spec` parameter to add or delete instances.

### Note

You canât delete a service instance (remove it from the spec) if it has an attached component.

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/UpdateService)

## Synopsis

```
update-service
[--description <value>]
--name <value>
[--spec <value>]
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

`--description` (string)

The edited service description.

`--name` (string)

The name of the service to edit.

`--spec` (string)

Lists the service instances to add and the existing service instances to remain. Omit the existing service instances to delete from the list. *Donât* include edits to the existing service instances or pipeline. For more information, see [Edit a service](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-update.html) in the *Proton User Guide* .

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

**To update a service**

The following `update-service` example edits a service description.

```
aws proton update-service \
    --name "MySimpleService" \
    --description "Edit by updating description"
```

Output:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/MySimpleService",
        "branchName": "mainline",
        "createdAt": "2021-03-12T22:39:42.318000+00:00",
        "description": "Edit by updating description",
        "lastModifiedAt": "2021-03-12T22:44:21.975000+00:00",
        "name": "MySimpleService",
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "repositoryId": "myorg/myapp",
        "status": "ACTIVE",
        "templateName": "fargate-service"
    }
}
```

For more information, see [Edit a service](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-update.html) in the *The AWS Proton Administrator Guide* or [Edit a service](https://docs.aws.amazon.com/proton/latest/userguide/ug-svc-update.html) in the *The AWS Proton User Guide*.

## Output

service -> (structure)

The service detail data thatâs returned by Proton.

arn -> (string)

The Amazon Resource Name (ARN) of the service.

branchName -> (string)

The name of the code repository branch that holds the code thatâs deployed in Proton.

createdAt -> (timestamp)

The time when the service was created.

description -> (string)

A description of the service.

lastModifiedAt -> (timestamp)

The time when the service was last modified.

name -> (string)

The name of the service.

pipeline -> (structure)

The service pipeline detail data.

arn -> (string)

The Amazon Resource Name (ARN) of the service pipeline.

createdAt -> (timestamp)

The time when the service pipeline was created.

deploymentStatus -> (string)

The deployment status of the service pipeline.

deploymentStatusMessage -> (string)

A service pipeline deployment status message.

lastAttemptedDeploymentId -> (string)

The ID of the last attempted deployment of this service pipeline.

lastDeploymentAttemptedAt -> (timestamp)

The time when a deployment of the service pipeline was last attempted.

lastDeploymentSucceededAt -> (timestamp)

The time when the service pipeline was last deployed successfully.

lastSucceededDeploymentId -> (string)

The ID of the last successful deployment of this service pipeline.

spec -> (string)

The service spec that was used to create the service pipeline.

templateMajorVersion -> (string)

The major version of the service template that was used to create the service pipeline.

templateMinorVersion -> (string)

The minor version of the service template that was used to create the service pipeline.

templateName -> (string)

The name of the service template that was used to create the service pipeline.

repositoryConnectionArn -> (string)

The Amazon Resource Name (ARN) of the repository connection. For more information, see [Setting up an AWS CodeStar connection](https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html#setting-up-vcontrol) in the *Proton User Guide* .

repositoryId -> (string)

The ID of the source code repository.

spec -> (string)

The formatted specification that defines the service.

status -> (string)

The status of the service.

statusMessage -> (string)

A service status message.

templateName -> (string)

The name of the service template.