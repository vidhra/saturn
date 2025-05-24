# start-product-subscriptionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-user-subscriptions/start-product-subscription.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-user-subscriptions/start-product-subscription.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [license-manager-user-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager-user-subscriptions/index.html#cli-aws-license-manager-user-subscriptions) ]

# start-product-subscription

## Description

Starts a product subscription for a user with the specified identity provider.

### Note

Your estimated bill for charges on the number of users and related costs will take 48 hours to appear for billing periods that havenât closed (marked as **Pending** billing status) in Amazon Web Services Billing. For more information, see [Viewing your monthly charges](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html) in the *Amazon Web Services Billing User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/license-manager-user-subscriptions-2018-05-10/StartProductSubscription)

## Synopsis

```
start-product-subscription
[--domain <value>]
--identity-provider <value>
--product <value>
[--tags <value>]
--username <value>
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

`--domain` (string)

The domain name of the Active Directory that contains the user for whom to start the product subscription.

`--identity-provider` (tagged union structure)

An object that specifies details for the identity provider.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ActiveDirectoryIdentityProvider`.

ActiveDirectoryIdentityProvider -> (structure)

The `ActiveDirectoryIdentityProvider` resource contains settings and other details about a specific Active Directory identity provider.

ActiveDirectorySettings -> (structure)

The `ActiveDirectorySettings` resource contains details about the Active Directory, including network access details such as domain name and IP addresses, and the credential provider for user administration.

DomainCredentialsProvider -> (tagged union structure)

Points to the `CredentialsProvider` resource that contains information about the credential provider for user administration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `SecretsManagerCredentialsProvider`.

SecretsManagerCredentialsProvider -> (structure)

Identifies the Secrets Manager secret that contains credentials needed for user administration in the Active Directory.

SecretId -> (string)

The ID of the Secrets Manager secret that contains credentials.

DomainIpv4List -> (list)

A list of domain IPv4 addresses that are used for the Active Directory.

(string)

DomainName -> (string)

The domain name for the Active Directory.

DomainNetworkSettings -> (structure)

The `DomainNetworkSettings` resource contains an array of subnets that apply for the Active Directory.

Subnets -> (list)

Contains a list of subnets that apply for the Active Directory domain.

(string)

ActiveDirectoryType -> (string)

The type of Active Directory â either a self-managed Active Directory or an Amazon Web Services Managed Active Directory.

DirectoryId -> (string)

The directory ID for an Active Directory identity provider.

JSON Syntax:

```
{
  "ActiveDirectoryIdentityProvider": {
    "ActiveDirectorySettings": {
      "DomainCredentialsProvider": {
        "SecretsManagerCredentialsProvider": {
          "SecretId": "string"
        }
      },
      "DomainIpv4List": ["string", ...],
      "DomainName": "string",
      "DomainNetworkSettings": {
        "Subnets": ["string", ...]
      }
    },
    "ActiveDirectoryType": "SELF_MANAGED"|"AWS_MANAGED",
    "DirectoryId": "string"
  }
}
```

`--product` (string)

The name of the user-based subscription product.

Valid values: `VISUAL_STUDIO_ENTERPRISE` | `VISUAL_STUDIO_PROFESSIONAL` | `OFFICE_PROFESSIONAL_PLUS` | `REMOTE_DESKTOP_SERVICES`

`--tags` (map)

The tags that apply to the product subscription.

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

`--username` (string)

The user name from the identity provider of the user.

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

ProductUserSummary -> (structure)

Metadata that describes the start product subscription operation.

Domain -> (string)

The domain name of the Active Directory that contains the user information for the product subscription.

IdentityProvider -> (tagged union structure)

An object that specifies details for the identity provider.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ActiveDirectoryIdentityProvider`.

ActiveDirectoryIdentityProvider -> (structure)

The `ActiveDirectoryIdentityProvider` resource contains settings and other details about a specific Active Directory identity provider.

ActiveDirectorySettings -> (structure)

The `ActiveDirectorySettings` resource contains details about the Active Directory, including network access details such as domain name and IP addresses, and the credential provider for user administration.

DomainCredentialsProvider -> (tagged union structure)

Points to the `CredentialsProvider` resource that contains information about the credential provider for user administration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `SecretsManagerCredentialsProvider`.

SecretsManagerCredentialsProvider -> (structure)

Identifies the Secrets Manager secret that contains credentials needed for user administration in the Active Directory.

SecretId -> (string)

The ID of the Secrets Manager secret that contains credentials.

DomainIpv4List -> (list)

A list of domain IPv4 addresses that are used for the Active Directory.

(string)

DomainName -> (string)

The domain name for the Active Directory.

DomainNetworkSettings -> (structure)

The `DomainNetworkSettings` resource contains an array of subnets that apply for the Active Directory.

Subnets -> (list)

Contains a list of subnets that apply for the Active Directory domain.

(string)

ActiveDirectoryType -> (string)

The type of Active Directory â either a self-managed Active Directory or an Amazon Web Services Managed Active Directory.

DirectoryId -> (string)

The directory ID for an Active Directory identity provider.

Product -> (string)

The name of the user-based subscription product.

ProductUserArn -> (string)

The Amazon Resource Name (ARN) for this product user.

Status -> (string)

The status of a product for this user.

StatusMessage -> (string)

The status message for a product for this user.

SubscriptionEndDate -> (string)

The end date of a subscription.

SubscriptionStartDate -> (string)

The start date of a subscription.

Username -> (string)

The user name from the identity provider for this product user.