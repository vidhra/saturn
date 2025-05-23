# create-componentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-component.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/create-component.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [proton](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/proton/index.html#cli-aws-proton) ]

# create-component

## Description

Create an Proton component. A component is an infrastructure extension for a service instance.

For more information about components, see [Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the *Proton User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/proton-2020-07-20/CreateComponent)

## Synopsis

```
create-component
[--client-token <value>]
[--description <value>]
[--environment-name <value>]
--manifest <value>
--name <value>
[--service-instance-name <value>]
[--service-name <value>]
[--service-spec <value>]
[--tags <value>]
--template-file <value>
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

The client token for the created component.

`--description` (string)

An optional customer-provided description of the component.

`--environment-name` (string)

The name of the Proton environment that you want to associate this component with. You must specify this when you donât specify `serviceInstanceName` and `serviceName` .

`--manifest` (string)

A path to a manifest file that lists the Infrastructure as Code (IaC) file, template language, and rendering engine for infrastructure that a custom component provisions.

`--name` (string)

The customer-provided name of the component.

`--service-instance-name` (string)

The name of the service instance that you want to attach this component to. If you donât specify this, the component isnât attached to any service instance. Specify both `serviceInstanceName` and `serviceName` or neither of them.

`--service-name` (string)

The name of the service that `serviceInstanceName` is associated with. If you donât specify this, the component isnât attached to any service instance. Specify both `serviceInstanceName` and `serviceName` or neither of them.

`--service-spec` (string)

The service spec that you want the component to use to access service inputs. Set this only when you attach the component to a service instance.

`--tags` (list)

An optional list of metadata items that you can associate with the Proton component. A tag is a key-value pair.

For more information, see [Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the *Proton User Guide* .

(structure)

A description of a resource tag.

key -> (string)

The key of the resource tag.

value -> (string)

The value of the resource tag.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--template-file` (string)

A path to the Infrastructure as Code (IaC) file describing infrastructure that a custom component provisions.

### Note

Components support a single IaC file, even if you use Terraform as your template language.

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

component -> (structure)

The detailed data of the created component.

arn -> (string)

The Amazon Resource Name (ARN) of the component.

createdAt -> (timestamp)

The time when the component was created.

deploymentStatus -> (string)

The component deployment status.

deploymentStatusMessage -> (string)

The message associated with the component deployment status.

description -> (string)

A description of the component.

environmentName -> (string)

The name of the Proton environment that this component is associated with.

lastAttemptedDeploymentId -> (string)

The ID of the last attempted deployment of this component.

lastClientRequestToken -> (string)

The last token the client requested.

lastDeploymentAttemptedAt -> (timestamp)

The time when a deployment of the component was last attempted.

lastDeploymentSucceededAt -> (timestamp)

The time when the component was last deployed successfully.

lastModifiedAt -> (timestamp)

The time when the component was last modified.

lastSucceededDeploymentId -> (string)

The ID of the last successful deployment of this component.

name -> (string)

The name of the component.

serviceInstanceName -> (string)

The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.

serviceName -> (string)

The name of the service that `serviceInstanceName` is associated with. Provided when a component is attached to a service instance.

serviceSpec -> (string)

The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.