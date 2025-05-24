# create-workflow-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-workflow-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-workflow-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# create-workflow-version

## Description

Creates a new workflow version for the workflow that you specify with the `workflowId` parameter.

When you create a new version of a workflow, you need to specify the configuration for the new version. It doesnât inherit any configuration values from the workflow.

Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.

### Note

Donât include any personally identifiable information (PII) in the version name. Version names appear in the workflow version ARN.

For more information, see [Workflow versioning in Amazon Web Services HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the Amazon Web Services HealthOmics User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/CreateWorkflowVersion)

## Synopsis

```
create-workflow-version
--workflow-id <value>
--version-name <value>
[--definition-zip <value>]
[--definition-uri <value>]
[--accelerators <value>]
[--description <value>]
[--engine <value>]
[--main <value>]
[--parameter-template <value>]
[--request-id <value>]
[--storage-type <value>]
[--storage-capacity <value>]
[--tags <value>]
[--workflow-bucket-owner-id <value>]
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

`--workflow-id` (string)

The ID of the workflow where you are creating the new version.

`--version-name` (string)

A name for the workflow version. Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.

The version name must start with a letter or number and it can include upper-case and lower-case letters, numbers, hyphens, periods and underscores. The maximum length is 64 characters. You can use a simple naming scheme, such as version1, version2, version3. You can also match your workflow versions with your own internal versioning conventions, such as 2.7.0, 2.7.1, 2.7.2.

`--definition-zip` (blob)

A zip archive containing the workflow definition for this workflow version.

`--definition-uri` (string)

The URI specifies the location of the workflow definition for this workflow version.

`--accelerators` (string)

The computational accelerator for this workflow version.

Possible values:

- `GPU`

`--description` (string)

A description for this workflow version.

`--engine` (string)

The workflow engine for this workflow version.

Possible values:

- `WDL`
- `NEXTFLOW`
- `CWL`

`--main` (string)

The path of the main definition file for this workflow version.

`--parameter-template` (map)

The parameter template defines the input parameters for runs that use this workflow version.

key -> (string)

value -> (structure)

A workflow parameter.

description -> (string)

The parameterâs description.

optional -> (boolean)

Whether the parameter is optional.

Shorthand Syntax:

```
KeyName1=description=string,optional=boolean,KeyName2=description=string,optional=boolean
```

JSON Syntax:

```
{"string": {
      "description": "string",
      "optional": true|false
    }
  ...}
```

`--request-id` (string)

To ensure that requests donât run multiple times, specify a unique ID for each request.

`--storage-type` (string)

The default storage type for runs that use this workflow. STATIC storage allocates a fixed amount of storage. DYNAMIC storage dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see [Running workflows](https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html) in the *Amazon Web Services HealthOmics User Guide* .

Possible values:

- `STATIC`
- `DYNAMIC`

`--storage-capacity` (integer)

The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.

`--tags` (map)

Optional tags to associate with this workflow version.

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

`--workflow-bucket-owner-id` (string)

Amazon Web Services Id of the owner of the S3 bucket that contains the workflow definition. You need to specify this parameter if your account is not the bucket owner.

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

arn -> (string)

ARN of the workflow version.

workflowId -> (string)

The workflowâs ID.

versionName -> (string)

The workflow version name.

status -> (string)

The workflow version status.

tags -> (map)

The workflow versionâs tags.

key -> (string)

value -> (string)

uuid -> (string)

The universally unique identifier (UUID) value for this workflow version.