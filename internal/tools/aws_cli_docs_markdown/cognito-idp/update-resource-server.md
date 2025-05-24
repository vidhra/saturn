# update-resource-serverÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp) ]

# update-resource-server

## Description

Updates the name and scopes of a resource server. All other fields are read-only. For more information about resource servers, see [Access control with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html) .

### Warning

If you donât provide a value for an attribute, it is set to the default value.

### Note

Amazon Cognito evaluates Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.

**Learn more**

- [Signing Amazon Web Services API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
- [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/UpdateResourceServer)

## Synopsis

```
update-resource-server
--user-pool-id <value>
--identifier <value>
--name <value>
[--scopes <value>]
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

`--user-pool-id` (string)

The ID of the user pool that contains the resource server that you want to update.

`--identifier` (string)

A unique resource server identifier for the resource server. The identifier can be an API friendly name like `solar-system-data` . You can also set an API URL like `https://solar-system-data-api.example.com` as your identifier.

Amazon Cognito represents scopes in the access token in the format `$resource-server-identifier/$scope` . Longer scope-identifier strings increase the size of your access tokens.

`--name` (string)

The updated name of the resource server.

`--scopes` (list)

An array of updated custom scope names and descriptions that you want to associate with your resource server.

(structure)

One custom scope associated with a user pool resource server. This data type is a member of `ResourceServerScopeType` . For more information, see [Scopes, M2M, and API authorization with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html) .

ScopeName -> (string)

The name of the scope. Amazon Cognito renders custom scopes in the format `resourceServerIdentifier/ScopeName` . For example, if this parameter is `exampleScope` in the resource server with the identifier `exampleResourceServer` , you request and receive the scope `exampleResourceServer/exampleScope` .

ScopeDescription -> (string)

A friendly description of a custom scope.

Shorthand Syntax:

```
ScopeName=string,ScopeDescription=string ...
```

JSON Syntax:

```
[
  {
    "ScopeName": "string",
    "ScopeDescription": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update a resource server**

This example updates the the resource server Weather. It adds a new scope.

Command:

```
aws cognito-idp update-resource-server --user-pool-id us-west-2_aaaaaaaaa --identifier weather.example.com --name Weather --scopes ScopeName=NewScope,ScopeDescription="New scope description"
```

Output:

```
{
  "ResourceServer": {
      "UserPoolId": "us-west-2_aaaaaaaaa",
      "Identifier": "weather.example.com",
      "Name": "Happy",
      "Scopes": [
          {
              "ScopeName": "NewScope",
              "ScopeDescription": "New scope description"
          }
      ]
  }
}
```

## Output

ResourceServer -> (structure)

The updated details of the requested resource server.

UserPoolId -> (string)

The ID of the user pool that contains the resource server configuration.

Identifier -> (string)

A unique resource server identifier for the resource server. The identifier can be an API friendly name like `solar-system-data` . You can also set an API URL like `https://solar-system-data-api.example.com` as your identifier.

Amazon Cognito represents scopes in the access token in the format `$resource-server-identifier/$scope` . Longer scope-identifier strings increase the size of your access tokens.

Name -> (string)

The name of the resource server.

Scopes -> (list)

A list of scopes that are defined for the resource server.

(structure)

One custom scope associated with a user pool resource server. This data type is a member of `ResourceServerScopeType` . For more information, see [Scopes, M2M, and API authorization with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html) .

ScopeName -> (string)

The name of the scope. Amazon Cognito renders custom scopes in the format `resourceServerIdentifier/ScopeName` . For example, if this parameter is `exampleScope` in the resource server with the identifier `exampleResourceServer` , you request and receive the scope `exampleResourceServer/exampleScope` .

ScopeDescription -> (string)

A friendly description of a custom scope.