# get-project-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/get-project-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/get-project-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# get-project-profile

## Description

The details of the project profile.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/GetProjectProfile)

## Synopsis

```
get-project-profile
--domain-identifier <value>
--identifier <value>
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

`--domain-identifier` (string)

The ID of the domain.

`--identifier` (string)

The ID of the project profile.

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

createdAt -> (timestamp)

The timestamp of when the project profile was created.

createdBy -> (string)

The user who created the project profile.

description -> (string)

The description of the project profile.

domainId -> (string)

The ID of the domain of the project profile.

domainUnitId -> (string)

The ID of the domain unit of the project profile.

environmentConfigurations -> (list)

The environment configurations of the project profile.

(structure)

The configuration of an environment.

awsAccount -> (tagged union structure)

The Amazon Web Services account of the environment.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `awsAccountId`, `awsAccountIdPath`.

awsAccountId -> (string)

The account ID of a project.

awsAccountIdPath -> (string)

The account ID path of a project.

awsRegion -> (tagged union structure)

The Amazon Web Services Region of the environment.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `regionName`, `regionNamePath`.

regionName -> (string)

The Amazon Web Services Region name.

regionNamePath -> (string)

The region name path.

configurationParameters -> (structure)

The configuration parameters of the environment.

parameterOverrides -> (list)

The parameter overrides.

(structure)

The environment configuration parameter.

isEditable -> (boolean)

Specifies whether the environment parameter is editable.

name -> (string)

The name of the environment configuration parameter.

value -> (string)

The value of the environment configuration parameter.

resolvedParameters -> (list)

The resolved environment configuration parameters.

(structure)

The environment configuration parameter.

isEditable -> (boolean)

Specifies whether the environment parameter is editable.

name -> (string)

The name of the environment configuration parameter.

value -> (string)

The value of the environment configuration parameter.

ssmPath -> (string)

Ssm path environment configuration parameters.

deploymentMode -> (string)

The deployment mode of the environment.

deploymentOrder -> (integer)

The deployment order of the environment.

description -> (string)

The environment description.

environmentBlueprintId -> (string)

The environment blueprint ID.

id -> (string)

The environment ID.

name -> (string)

The environment name.

id -> (string)

The ID of the project profile.

lastUpdatedAt -> (timestamp)

The timestamp of when project profile was last updated.

name -> (string)

The name of the project profile.

status -> (string)

The status of the project profile.