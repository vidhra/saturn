# create-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/create-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/create-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [m2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/index.html#cli-aws-m2) ]

# create-environment

## Description

Creates a runtime environment for a given runtime engine.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/m2-2021-04-28/CreateEnvironment)

## Synopsis

```
create-environment
[--client-token <value>]
[--description <value>]
--engine-type <value>
[--engine-version <value>]
[--high-availability-config <value>]
--instance-type <value>
[--kms-key-id <value>]
--name <value>
[--network-type <value>]
[--preferred-maintenance-window <value>]
[--publicly-accessible | --no-publicly-accessible]
[--security-group-ids <value>]
[--storage-configurations <value>]
[--subnet-ids <value>]
[--tags <value>]
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

Unique, case-sensitive identifier you provide to ensure the idempotency of the request to create an environment. The service generates the clientToken when the API call is triggered. The token expires after one hour, so if you retry the API within this timeframe with the same clientToken, you will get the same response. The service also handles deleting the clientToken after it expires.

`--description` (string)

The description of the runtime environment.

`--engine-type` (string)

The engine type for the runtime environment.

Possible values:

- `microfocus`
- `bluage`

`--engine-version` (string)

The version of the engine type for the runtime environment.

`--high-availability-config` (structure)

The details of a high availability configuration for this runtime environment.

desiredCapacity -> (integer)

The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.

Shorthand Syntax:

```
desiredCapacity=integer
```

JSON Syntax:

```
{
  "desiredCapacity": integer
}
```

`--instance-type` (string)

The type of instance for the runtime environment.

`--kms-key-id` (string)

The identifier of a customer managed key.

`--name` (string)

The name of the runtime environment. Must be unique within the account.

`--network-type` (string)

The network type required for the runtime environment.

Possible values:

- `ipv4`
- `dual`

`--preferred-maintenance-window` (string)

Configures the maintenance window that you want for the runtime environment. The maintenance window must have the format `ddd:hh24:mi-ddd:hh24:mi` and must be less than 24 hours. The following two examples are valid maintenance windows: `sun:23:45-mon:00:15` or `sat:01:00-sat:03:00` .

If you do not provide a value, a random system-generated value will be assigned.

`--publicly-accessible` | `--no-publicly-accessible` (boolean)

Specifies whether the runtime environment is publicly accessible.

`--security-group-ids` (list)

The list of security groups for the VPC associated with this runtime environment.

(string)

Syntax:

```
"string" "string" ...
```

`--storage-configurations` (list)

Optional. The storage configurations for this runtime environment.

(tagged union structure)

Defines the storage configuration for a runtime environment.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `efs`, `fsx`.

efs -> (structure)

Defines the storage configuration for an Amazon EFS file system.

fileSystemId -> (string)

The file system identifier.

mountPoint -> (string)

The mount point for the file system.

fsx -> (structure)

Defines the storage configuration for an Amazon FSx file system.

fileSystemId -> (string)

The file system identifier.

mountPoint -> (string)

The mount point for the file system.

Shorthand Syntax:

```
efs={fileSystemId=string,mountPoint=string},fsx={fileSystemId=string,mountPoint=string} ...
```

JSON Syntax:

```
[
  {
    "efs": {
      "fileSystemId": "string",
      "mountPoint": "string"
    },
    "fsx": {
      "fileSystemId": "string",
      "mountPoint": "string"
    }
  }
  ...
]
```

`--subnet-ids` (list)

The list of subnets associated with the VPC for this runtime environment.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (map)

The tags for the runtime environment.

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

environmentId -> (string)

The unique identifier of the runtime environment.