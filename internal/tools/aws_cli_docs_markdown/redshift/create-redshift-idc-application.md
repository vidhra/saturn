# create-redshift-idc-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-redshift-idc-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-redshift-idc-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/index.html#cli-aws-redshift) ]

# create-redshift-idc-application

## Description

Creates an Amazon Redshift application for use with IAM Identity Center.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-2012-12-01/CreateRedshiftIdcApplication)

## Synopsis

```
create-redshift-idc-application
--idc-instance-arn <value>
--redshift-idc-application-name <value>
[--identity-namespace <value>]
--idc-display-name <value>
--iam-role-arn <value>
[--authorized-token-issuer-list <value>]
[--service-integrations <value>]
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

`--idc-instance-arn` (string)

The Amazon resource name (ARN) of the IAM Identity Center instance where Amazon Redshift creates a new managed application.

`--redshift-idc-application-name` (string)

The name of the Redshift application in IAM Identity Center.

`--identity-namespace` (string)

The namespace for the Amazon Redshift IAM Identity Center application instance. It determines which managed application verifies the connection token.

`--idc-display-name` (string)

The display name for the Amazon Redshift IAM Identity Center application instance. It appears in the console.

`--iam-role-arn` (string)

The IAM role ARN for the Amazon Redshift IAM Identity Center application instance. It has the required permissions to be assumed and invoke the IDC Identity Center API.

`--authorized-token-issuer-list` (list)

The token issuer list for the Amazon Redshift IAM Identity Center application instance.

(structure)

The authorized token issuer for the Amazon Redshift IAM Identity Center application.

TrustedTokenIssuerArn -> (string)

The ARN for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.

AuthorizedAudiencesList -> (list)

The list of audiences for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.

(string)

Shorthand Syntax:

```
TrustedTokenIssuerArn=string,AuthorizedAudiencesList=string,string ...
```

JSON Syntax:

```
[
  {
    "TrustedTokenIssuerArn": "string",
    "AuthorizedAudiencesList": ["string", ...]
  }
  ...
]
```

`--service-integrations` (list)

A collection of service integrations for the Redshift IAM Identity Center application.

(tagged union structure)

A list of service integrations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `LakeFormation`, `S3AccessGrants`.

LakeFormation -> (list)

A list of scopes set up for Lake Formation integration.

(tagged union structure)

A list of scopes set up for Lake Formation integration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `LakeFormationQuery`.

LakeFormationQuery -> (structure)

The Lake Formation scope.

Authorization -> (string)

Determines whether the query scope is enabled or disabled.

S3AccessGrants -> (list)

A list of scopes set up for S3 Access Grants integration.

(tagged union structure)

A list of scopes set up for S3 Access Grants integration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ReadWriteAccess`.

ReadWriteAccess -> (structure)

The S3 Access Grants scope.

Authorization -> (string)

Determines whether the read/write scope is enabled or disabled.

JSON Syntax:

```
[
  {
    "LakeFormation": [
      {
        "LakeFormationQuery": {
          "Authorization": "Enabled"|"Disabled"
        }
      }
      ...
    ],
    "S3AccessGrants": [
      {
        "ReadWriteAccess": {
          "Authorization": "Enabled"|"Disabled"
        }
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

RedshiftIdcApplication -> (structure)

Contains properties for the Redshift IDC application.

IdcInstanceArn -> (string)

The ARN for the IAM Identity Center instance that Redshift integrates with.

RedshiftIdcApplicationName -> (string)

The name of the Redshift application in IAM Identity Center.

RedshiftIdcApplicationArn -> (string)

The ARN for the Redshift application that integrates with IAM Identity Center.

IdentityNamespace -> (string)

The identity namespace for the Amazon Redshift IAM Identity Center application. It determines which managed application verifies the connection token.

IdcDisplayName -> (string)

The display name for the Amazon Redshift IAM Identity Center application. It appears on the console.

IamRoleArn -> (string)

The ARN for the Amazon Redshift IAM Identity Center application. It has the required permissions to be assumed and invoke the IDC Identity Center API.

IdcManagedApplicationArn -> (string)

The ARN for the Amazon Redshift IAM Identity Center application.

IdcOnboardStatus -> (string)

The onboarding status for the Amazon Redshift IAM Identity Center application.

AuthorizedTokenIssuerList -> (list)

The authorized token issuer list for the Amazon Redshift IAM Identity Center application.

(structure)

The authorized token issuer for the Amazon Redshift IAM Identity Center application.

TrustedTokenIssuerArn -> (string)

The ARN for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.

AuthorizedAudiencesList -> (list)

The list of audiences for the authorized token issuer for integrating Amazon Redshift with IDC Identity Center.

(string)

ServiceIntegrations -> (list)

A list of service integrations for the Redshift IAM Identity Center application.

(tagged union structure)

A list of service integrations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `LakeFormation`, `S3AccessGrants`.

LakeFormation -> (list)

A list of scopes set up for Lake Formation integration.

(tagged union structure)

A list of scopes set up for Lake Formation integration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `LakeFormationQuery`.

LakeFormationQuery -> (structure)

The Lake Formation scope.

Authorization -> (string)

Determines whether the query scope is enabled or disabled.

S3AccessGrants -> (list)

A list of scopes set up for S3 Access Grants integration.

(tagged union structure)

A list of scopes set up for S3 Access Grants integration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ReadWriteAccess`.

ReadWriteAccess -> (structure)

The S3 Access Grants scope.

Authorization -> (string)

Determines whether the read/write scope is enabled or disabled.