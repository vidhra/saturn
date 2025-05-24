# create-subscription-targetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/create-subscription-target.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/create-subscription-target.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# create-subscription-target

## Description

Creates a subscription target in Amazon DataZone.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/CreateSubscriptionTarget)

## Synopsis

```
create-subscription-target
--applicable-asset-types <value>
--authorized-principals <value>
[--client-token <value>]
--domain-identifier <value>
--environment-identifier <value>
--manage-access-role <value>
--name <value>
[--provider <value>]
--subscription-target-config <value>
--type <value>
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

`--applicable-asset-types` (list)

The asset types that can be included in the subscription target.

(string)

Syntax:

```
"string" "string" ...
```

`--authorized-principals` (list)

The authorized principals of the subscription target.

(string)

Syntax:

```
"string" "string" ...
```

`--client-token` (string)

A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

`--domain-identifier` (string)

The ID of the Amazon DataZone domain in which subscription target is created.

`--environment-identifier` (string)

The ID of the environment in which subscription target is created.

`--manage-access-role` (string)

The manage access role that is used to create the subscription target.

`--name` (string)

The name of the subscription target.

`--provider` (string)

The provider of the subscription target.

`--subscription-target-config` (list)

The configuration of the subscription target.

(structure)

The details of the subscription target configuration.

content -> (string)

The content of the subscription target configuration.

formName -> (string)

The form name included in the subscription target configuration.

Shorthand Syntax:

```
content=string,formName=string ...
```

JSON Syntax:

```
[
  {
    "content": "string",
    "formName": "string"
  }
  ...
]
```

`--type` (string)

The type of the subscription target.

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

applicableAssetTypes -> (list)

The asset types that can be included in the subscription target.

(string)

authorizedPrincipals -> (list)

The authorised principals of the subscription target.

(string)

createdAt -> (timestamp)

The timestamp of when the subscription target was created.

createdBy -> (string)

The Amazon DataZone user who created the subscription target.

domainId -> (string)

The ID of the Amazon DataZone domain in which the subscription target was created.

environmentId -> (string)

The ID of the environment in which the subscription target was created.

id -> (string)

The ID of the subscription target.

manageAccessRole -> (string)

The manage access role with which the subscription target was created.

name -> (string)

The name of the subscription target.

projectId -> (string)

???

provider -> (string)

The provider of the subscription target.

subscriptionTargetConfig -> (list)

The configuration of the subscription target.

(structure)

The details of the subscription target configuration.

content -> (string)

The content of the subscription target configuration.

formName -> (string)

The form name included in the subscription target configuration.

type -> (string)

The type of the subscription target.

updatedAt -> (timestamp)

The timestamp of when the subscription target was updated.

updatedBy -> (string)

The Amazon DataZone user who updated the subscription target.