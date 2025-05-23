# update-access-control-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-access-control-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-access-control-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# update-access-control-configuration

## Description

Updates an access control configuration for your documents in an index. This includes user and group access information for your documents. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

You can update an access control configuration you created without indexing all of your documents again. For example, your index contains top-secret company documents that only certain employees or users should access. You created an âallowâ access control configuration for one user who recently joined the âtop-secretâ team, switching from a team with âdenyâ access to top-secret documents. However, the user suddenly returns to their previous team and should no longer have access to top secret documents. You can update the access control configuration to re-configure access control for your documents as circumstances change.

You call the [BatchPutDocument](https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html) API to apply the updated access control configuration, with the `AccessControlConfigurationId` included in the [Document](https://docs.aws.amazon.com/kendra/latest/dg/API_Document.html) object. If you use an S3 bucket as a data source, you synchronize your data source to apply the `AccessControlConfigurationId` in the `.metadata.json` file. Amazon Kendra currently only supports access control configuration for S3 data sources and documents indexed using the `BatchPutDocument` API.

### Warning

You canât configure access control using `CreateAccessControlConfiguration` for an Amazon Kendra Gen AI Enterprise Edition index. Amazon Kendra will return a `ValidationException` error for a `Gen_AI_ENTERPRISE_EDITION` index.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/UpdateAccessControlConfiguration)

## Synopsis

```
update-access-control-configuration
--index-id <value>
--id <value>
[--name <value>]
[--description <value>]
[--access-control-list <value>]
[--hierarchical-access-control-list <value>]
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

`--index-id` (string)

The identifier of the index for an access control configuration.

`--id` (string)

The identifier of the access control configuration you want to update.

`--name` (string)

A new name for the access control configuration.

`--description` (string)

A new description for the access control configuration.

`--access-control-list` (list)

Information you want to update on principals (users and/or groups) and which documents they should have access to. This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

(structure)

Provides user and group information for [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) .

Name -> (string)

The name of the user or group.

Type -> (string)

The type of principal.

Access -> (string)

Whether to allow or deny document access to the principal.

DataSourceId -> (string)

The identifier of the data source the principal should access documents from.

Shorthand Syntax:

```
Name=string,Type=string,Access=string,DataSourceId=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Type": "USER"|"GROUP",
    "Access": "ALLOW"|"DENY",
    "DataSourceId": "string"
  }
  ...
]
```

`--hierarchical-access-control-list` (list)

The updated list of [principal](https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html) lists that define the hierarchy for which documents users should have access to.

(structure)

Information to define the hierarchy for which documents users should have access to.

PrincipalList -> (list)

A list of [principal](https://docs.aws.amazon.com/kendra/latest/dg/API_Principal.html) lists that define the hierarchy for which documents users should have access to. Each hierarchical list specifies which user or group has allow or deny access for each document.

(structure)

Provides user and group information for [user context filtering](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) .

Name -> (string)

The name of the user or group.

Type -> (string)

The type of principal.

Access -> (string)

Whether to allow or deny document access to the principal.

DataSourceId -> (string)

The identifier of the data source the principal should access documents from.

Shorthand Syntax:

```
PrincipalList=[{Name=string,Type=string,Access=string,DataSourceId=string},{Name=string,Type=string,Access=string,DataSourceId=string}] ...
```

JSON Syntax:

```
[
  {
    "PrincipalList": [
      {
        "Name": "string",
        "Type": "USER"|"GROUP",
        "Access": "ALLOW"|"DENY",
        "DataSourceId": "string"
      }
      ...
    ]
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

None