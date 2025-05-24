# create-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/create-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/create-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# create-domain

## Description

Creates an Amazon DataZone domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/CreateDomain)

## Synopsis

```
create-domain
[--client-token <value>]
[--description <value>]
--domain-execution-role <value>
[--domain-version <value>]
[--kms-key-identifier <value>]
--name <value>
[--service-role <value>]
[--single-sign-on <value>]
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

A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

`--description` (string)

The description of the Amazon DataZone domain.

`--domain-execution-role` (string)

The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.

`--domain-version` (string)

The version of the domain that is created.

Possible values:

- `V1`
- `V2`

`--kms-key-identifier` (string)

The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.

`--name` (string)

The name of the Amazon DataZone domain.

`--service-role` (string)

The service role of the domain that is created.

`--single-sign-on` (structure)

The single-sign on configuration of the Amazon DataZone domain.

idcInstanceArn -> (string)

The ARN of the IDC instance.

type -> (string)

The type of single sign-on in Amazon DataZone.

userAssignment -> (string)

The single sign-on user assignment in Amazon DataZone.

Shorthand Syntax:

```
idcInstanceArn=string,type=string,userAssignment=string
```

JSON Syntax:

```
{
  "idcInstanceArn": "string",
  "type": "IAM_IDC"|"DISABLED",
  "userAssignment": "AUTOMATIC"|"MANUAL"
}
```

`--tags` (map)

The tags specified for the Amazon DataZone domain.

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

arn -> (string)

The ARN of the Amazon DataZone domain.

description -> (string)

The description of the Amazon DataZone domain.

domainExecutionRole -> (string)

The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.

domainVersion -> (string)

The version of the domain that is created.

id -> (string)

The identifier of the Amazon DataZone domain.

kmsKeyIdentifier -> (string)

The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data.

name -> (string)

The name of the Amazon DataZone domain.

portalUrl -> (string)

The URL of the data portal for this Amazon DataZone domain.

rootDomainUnitId -> (string)

The ID of the root domain unit.

serviceRole -> (string)

Te service role of the domain that is created.

singleSignOn -> (structure)

The single-sign on configuration of the Amazon DataZone domain.

idcInstanceArn -> (string)

The ARN of the IDC instance.

type -> (string)

The type of single sign-on in Amazon DataZone.

userAssignment -> (string)

The single sign-on user assignment in Amazon DataZone.

status -> (string)

The status of the Amazon DataZone domain.

tags -> (map)

The tags specified for the Amazon DataZone domain.

key -> (string)

value -> (string)