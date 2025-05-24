# update-service-instanceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-instance.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-instance.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# update-service-instance

## Description

Update a service instance.

There are a few modes for updating a service instance. The `deploymentType` field defines the mode.

### Note

You canât update a service instance while its deployment status, or the deployment status of a component attached to it, is `IN_PROGRESS` .

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/UpdateServiceInstance)

## Synopsis

```
update-service-instance
[--client-token <value>]
--deployment-type <value>
--name <value>
--service-name <value>
[--spec <value>]
[--template-major-version <value>]
[--template-minor-version <value>]
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

`--client-token` (string)

The client token of the service instance to update.

`--deployment-type` (string)

The deployment type. It defines the mode for updating a service instance, as follows:

`NONE`

In this mode, a deployment *doesnât* occur. Only the requested metadata parameters are updated.

`CURRENT_VERSION`

In this mode, the service instance is deployed and updated with the new spec that you provide. Only requested parameters are updated. *Donât* include major or minor version parameters when you use this deployment type.

`MINOR_VERSION`

In this mode, the service instance is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can also specify a different minor version of the current major version in use.

`MAJOR_VERSION`

In this mode, the service instance is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version thatâs higher than the major version in use and a minor version.

Possible values:

- `NONE`
- `CURRENT_VERSION`
- `MINOR_VERSION`
- `MAJOR_VERSION`

`--name` (string)

The name of the service instance to update.

`--service-name` (string)

The name of the service that the service instance belongs to.

`--spec` (string)

The formatted specification that defines the service instance update.

`--template-major-version` (string)

The major version of the service template to update.

`--template-minor-version` (string)

The minor version of the service template to update.

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

**To update a service instance to a new minor version**

The following `update-service-instance` example updates a service instance to a new minor version of its service template that adds a new instance named âmy-other-instanceâ with a new required input.

```
aws proton update-service-instance \
    --service-name "simple-svc" \
    --spec "file://service-spec.yaml " \
    --template-major-version "1" \
    --template-minor-version "1" \
    --deployment-type "MINOR_VERSION" \
    --name "instance-one"
```

Contents of `service-spec.yaml`:

```
proton: ServiceSpec
pipeline:
    my_sample_pipeline_optional_input: "abc"
    my_sample_pipeline_required_input: "123"
instances:
    - name: "instance-one"
        environment: "simple-env"
        spec:
            my_sample_service_instance_optional_input: "def"
            my_sample_service_instance_required_input: "456"
    - name: "my-other-instance"
        environment: "simple-env"
        spec:
            my_sample_service_instance_required_input: "789"
```

Output:

```
{
    "serviceInstance": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/service-instance/instance-one",
        "createdAt": "2021-04-02T21:29:59.962000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "environmentName": "arn:aws:proton:region-id:123456789012:environment/simple-env",
        "lastDeploymentAttemptedAt": "2021-04-02T21:38:00.823000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T21:29:59.962000+00:00",
        "name": "instance-one",
        "serviceName": "simple-svc",
        "templateMajorVersion": "1",
        "templateMinorVersion": "0",
        "templateName": "svc-simple"
    }
}
```

For more information, see [Update a service instance](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-instance-update.html) in the *The AWS Proton Administrator Guide* or [Update a service instance](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-instance-update.html) in the *The AWS Proton User Guide*.

## Output

serviceInstance -> (structure)

The service instance summary data thatâs returned by Proton.

arn -> (string)

The Amazon Resource Name (ARN) of the service instance.

createdAt -> (timestamp)

The time when the service instance was created.

deploymentStatus -> (string)

The service instance deployment status.

deploymentStatusMessage -> (string)

The message associated with the service instance deployment status.

environmentName -> (string)

The name of the environment that the service instance was deployed into.

lastAttemptedDeploymentId -> (string)

The ID of the last attempted deployment of this service instance.

lastClientRequestToken -> (string)

The last client request token received.

lastDeploymentAttemptedAt -> (timestamp)

The time when a deployment of the service instance was last attempted.

lastDeploymentSucceededAt -> (timestamp)

The time when the service instance was last deployed successfully.

lastSucceededDeploymentId -> (string)

The ID of the last successful deployment of this service instance.

name -> (string)

The name of the service instance.

serviceName -> (string)

The name of the service that the service instance belongs to.

spec -> (string)

The service spec that was used to create the service instance.

templateMajorVersion -> (string)

The major version of the service template that was used to create the service instance.

templateMinorVersion -> (string)

The minor version of the service template that was used to create the service instance.

templateName -> (string)

The name of the service template that was used to create the service instance.