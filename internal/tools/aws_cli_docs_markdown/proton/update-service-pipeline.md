# update-service-pipelineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-pipeline.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/update-service-pipeline.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# update-service-pipeline

## Description

Update the service pipeline.

There are four modes for updating a service pipeline. The `deploymentType` field defines the mode.

`NONE`

In this mode, a deployment *doesnât* occur. Only the requested metadata parameters are updated.

`CURRENT_VERSION`

In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. *Donât* include major or minor version parameters when you use this `deployment-type` .

`MINOR_VERSION`

In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.

`MAJOR_VERSION`

In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version thatâs higher than the major version in use and a minor version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/UpdateServicePipeline)

## Synopsis

```
update-service-pipeline
--deployment-type <value>
--service-name <value>
--spec <value>
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

`--deployment-type` (string)

The deployment type.

There are four modes for updating a service pipeline. The `deploymentType` field defines the mode.

`NONE`

In this mode, a deployment *doesnât* occur. Only the requested metadata parameters are updated.

`CURRENT_VERSION`

In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. *Donât* include major or minor version parameters when you use this `deployment-type` .

`MINOR_VERSION`

In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.

`MAJOR_VERSION`

In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version thatâs higher than the major version in use and a minor version.

Possible values:

- `NONE`
- `CURRENT_VERSION`
- `MINOR_VERSION`
- `MAJOR_VERSION`

`--service-name` (string)

The name of the service to that the pipeline is associated with.

`--spec` (string)

The spec for the service pipeline to update.

`--template-major-version` (string)

The major version of the service template that was used to create the service that the pipeline is associated with.

`--template-minor-version` (string)

The minor version of the service template that was used to create the service that the pipeline is associated with.

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

**To update a service pipeline**

The following `update-service-pipeline` example updates a service pipeline to a new minor version of its service template.

```
aws proton update-service-pipeline \
    --service-name "simple-svc" \
    --spec "file://service-spec.yaml" \
    --template-major-version "1" \
    --template-minor-version "1" \
    --deployment-type "MINOR_VERSION"
```

Output:

```
{
    "pipeline": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc/pipeline/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "createdAt": "2021-04-02T21:29:59.962000+00:00",
        "deploymentStatus": "IN_PROGRESS",
        "lastDeploymentAttemptedAt": "2021-04-02T21:39:28.991000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T21:29:59.962000+00:00",
        "spec": "proton: ServiceSpec\n\npipeline:\n  my_sample_pipeline_optional_input: \"abc\"\n  my_sample_pipeline_required_input: \"123\"\n\ninstances:\n  - name: \"my-instance\"\n    environment: \"MySimpleEnv\"\n    spec:\n      my_sample_service_instance_optional_input: \"def\"\n      my_sample_service_instance_required_input: \"456\"\n  - name: \"my-other-instance\"\n    environment: \"MySimpleEnv\"\n    spec:\n      my_sample_service_instance_required_input: \"789\"\n",
        "templateMajorVersion": "1",
        "templateMinorVersion": "0",
        "templateName": "svc-simple"
    }
}
```

For more information, see [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/adminguide/ag-svc-pipeline-update.html) in the *The AWS Proton Administrator Guide* or [Update a service pipeline](https://docs.aws.amazon.com/proton/latest/userguide/ag-svc-pipeline-update.html) in the *The AWS Proton User Guide*.

## Output

pipeline -> (structure)

The pipeline details that are returned by Proton.

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