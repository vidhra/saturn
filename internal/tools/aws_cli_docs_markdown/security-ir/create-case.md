# create-caseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/security-ir/create-case.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/security-ir/create-case.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [security-ir](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/security-ir/index.html#cli-aws-security-ir) ]

# create-case

## Description

Grants permission to create a new case.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/security-ir-2018-05-10/CreateCase)

## Synopsis

```
create-case
[--client-token <value>]
--resolver-type <value>
--title <value>
--description <value>
--engagement-type <value>
--reported-incident-start-date <value>
--impacted-accounts <value>
--watchers <value>
[--threat-actor-ip-addresses <value>]
[--impacted-services <value>]
[--impacted-aws-regions <value>]
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

Required element used in combination with CreateCase.

`--resolver-type` (string)

Required element used in combination with CreateCase to identify the resolver type. Available resolvers include self-supported | aws-supported.

Possible values:

- `AWS`
- `Self`

`--title` (string)

Required element used in combination with CreateCase to provide a title for the new case.

`--description` (string)

Required element used in combination with CreateCase to provide a description for the new case.

`--engagement-type` (string)

Required element used in combination with CreateCase to provide an engagement type for the new cases. Available engagement types include Security Incident | Investigation

Possible values:

- `Security Incident`
- `Investigation`

`--reported-incident-start-date` (timestamp)

Required element used in combination with CreateCase to provide an initial start date for the unauthorized activity.

`--impacted-accounts` (list)

Required element used in combination with CreateCase to provide a list of impacted accounts.

(string)

Syntax:

```
"string" "string" ...
```

`--watchers` (list)

Required element used in combination with CreateCase to provide a list of entities to receive notifications for case updates.

(structure)

email -> (string)

name -> (string)

jobTitle -> (string)

Shorthand Syntax:

```
email=string,name=string,jobTitle=string ...
```

JSON Syntax:

```
[
  {
    "email": "string",
    "name": "string",
    "jobTitle": "string"
  }
  ...
]
```

`--threat-actor-ip-addresses` (list)

An optional element used in combination with CreateCase to provide a list of suspicious internet protocol addresses associated with unauthorized activity.

(structure)

ipAddress -> (string)

userAgent -> (string)

Shorthand Syntax:

```
ipAddress=string,userAgent=string ...
```

JSON Syntax:

```
[
  {
    "ipAddress": "string",
    "userAgent": "string"
  }
  ...
]
```

`--impacted-services` (list)

An optional element used in combination with CreateCase to provide a list of services impacted.

(string)

Syntax:

```
"string" "string" ...
```

`--impacted-aws-regions` (list)

An optional element used in combination with CreateCase to provide a list of impacted regions.

(structure)

region -> (string)

Shorthand Syntax:

```
region=string ...
```

JSON Syntax:

```
[
  {
    "region": "af-south-1"|"ap-east-1"|"ap-northeast-1"|"ap-northeast-2"|"ap-northeast-3"|"ap-south-1"|"ap-south-2"|"ap-southeast-1"|"ap-southeast-2"|"ap-southeast-3"|"ap-southeast-4"|"ap-southeast-5"|"ca-central-1"|"ca-west-1"|"cn-north-1"|"cn-northwest-1"|"eu-central-1"|"eu-central-2"|"eu-north-1"|"eu-south-1"|"eu-south-2"|"eu-west-1"|"eu-west-2"|"eu-west-3"|"il-central-1"|"me-central-1"|"me-south-1"|"sa-east-1"|"us-east-1"|"us-east-2"|"us-west-1"|"us-west-2"
  }
  ...
]
```

`--tags` (map)

An optional element used in combination with CreateCase to add customer specified tags to a case.

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

caseId -> (string)

A response element providing responses for requests to CreateCase. This element responds with the case ID.