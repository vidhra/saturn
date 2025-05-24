# create-dev-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-dev-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/create-dev-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codecatalyst](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecatalyst/index.html#cli-aws-codecatalyst) ]

# create-dev-environment

## Description

Creates a Dev Environment in Amazon CodeCatalyst, a cloud-based development environment that you can use to quickly work on the code stored in the source repositories of your project.

### Note

When created in the Amazon CodeCatalyst console, by default a Dev Environment is configured to have a 2 core processor, 4GB of RAM, and 16GB of persistent storage. None of these defaults apply to a Dev Environment created programmatically.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codecatalyst-2022-09-28/CreateDevEnvironment)

## Synopsis

```
create-dev-environment
--space-name <value>
--project-name <value>
[--repositories <value>]
[--client-token <value>]
[--alias <value>]
[--ides <value>]
--instance-type <value>
[--inactivity-timeout-minutes <value>]
--persistent-storage <value>
[--vpc-connection-name <value>]
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

`--space-name` (string)

The name of the space.

`--project-name` (string)

The name of the project in the space.

`--repositories` (list)

The source repository that contains the branch to clone into the Dev Environment.

(structure)

Information about a repository that will be cloned to a Dev Environment.

repositoryName -> (string)

The name of the source repository.

branchName -> (string)

The name of the branch in a source repository.

Shorthand Syntax:

```
repositoryName=string,branchName=string ...
```

JSON Syntax:

```
[
  {
    "repositoryName": "string",
    "branchName": "string"
  }
  ...
]
```

`--client-token` (string)

A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.

`--alias` (string)

The user-defined alias for a Dev Environment.

`--ides` (list)

Information about the integrated development environment (IDE) configured for a Dev Environment.

### Note

An IDE is required to create a Dev Environment. For Dev Environment creation, this field contains configuration information and must be provided.

(structure)

Information about the configuration of an integrated development environment (IDE) for a Dev Environment.

runtime -> (string)

A link to the IDE runtime image.

### Note

This parameter is not required for `VSCode` .

name -> (string)

The name of the IDE. Valid values include `Cloud9` , `IntelliJ` , `PyCharm` , `GoLand` , and `VSCode` .

Shorthand Syntax:

```
runtime=string,name=string ...
```

JSON Syntax:

```
[
  {
    "runtime": "string",
    "name": "string"
  }
  ...
]
```

`--instance-type` (string)

The Amazon EC2 instace type to use for the Dev Environment.

Possible values:

- `dev.standard1.small`
- `dev.standard1.medium`
- `dev.standard1.large`
- `dev.standard1.xlarge`

`--inactivity-timeout-minutes` (integer)

The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Only whole integers are allowed. Dev Environments consume compute minutes when running.

`--persistent-storage` (structure)

Information about the amount of storage allocated to the Dev Environment.

### Note

By default, a Dev Environment is configured to have 16GB of persistent storage when created from the Amazon CodeCatalyst console, but there is no default when programmatically creating a Dev Environment. Valid values for persistent storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.

sizeInGiB -> (integer)

The size of the persistent storage in gigabytes (specifically GiB).

### Note

Valid values for storage are based on memory sizes in 16GB increments. Valid values are 16, 32, and 64.

Shorthand Syntax:

```
sizeInGiB=integer
```

JSON Syntax:

```
{
  "sizeInGiB": integer
}
```

`--vpc-connection-name` (string)

The name of the connection that will be used to connect to Amazon VPC, if any.

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

spaceName -> (string)

The name of the space.

projectName -> (string)

The name of the project in the space.

id -> (string)

The system-generated unique ID of the Dev Environment.

vpcConnectionName -> (string)

The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.