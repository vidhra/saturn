# delete-domain-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-domain-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/delete-domain-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplify](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplify/index.html#cli-aws-amplify) ]

# delete-domain-association

## Description

Deletes a domain association for an Amplify app.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplify-2017-07-25/DeleteDomainAssociation)

## Synopsis

```
delete-domain-association
--app-id <value>
--domain-name <value>
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

`--app-id` (string)

The unique id for an Amplify app.

`--domain-name` (string)

The name of the domain.

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

domainAssociation -> (structure)

Describes the association between a custom domain and an Amplify app.

domainAssociationArn -> (string)

The Amazon Resource Name (ARN) for the domain association.

domainName -> (string)

The name of the domain.

enableAutoSubDomain -> (boolean)

Enables the automated creation of subdomains for branches.

autoSubDomainCreationPatterns -> (list)

Sets branch patterns for automatic subdomain creation.

(string)

autoSubDomainIAMRole -> (string)

The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains.

domainStatus -> (string)

The current status of the domain association.

updateStatus -> (string)

The status of the domain update operation that is currently in progress. The following list describes the valid update states.

REQUESTING_CERTIFICATE

The certificate is in the process of being updated.

PENDING_VERIFICATION

Indicates that an Amplify managed certificate is in the process of being verified. This occurs during the creation of a custom domain or when a custom domain is updated to use a managed certificate.

IMPORTING_CUSTOM_CERTIFICATE

Indicates that an Amplify custom certificate is in the process of being imported. This occurs during the creation of a custom domain or when a custom domain is updated to use a custom certificate.

PENDING_DEPLOYMENT

Indicates that the subdomain or certificate changes are being propagated.

AWAITING_APP_CNAME

Amplify is waiting for CNAME records corresponding to subdomains to be propagated. If your custom domain is on Route 53, Amplify handles this for you automatically. For more information about custom domains, see [Setting up custom domains](https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html) in the *Amplify Hosting User Guide* .

UPDATE_COMPLETE

The certificate has been associated with a domain.

UPDATE_FAILED

The certificate has failed to be provisioned or associated, and there is no existing active certificate to roll back to.

statusReason -> (string)

Additional information that describes why the domain association is in the current state.

certificateVerificationDNSRecord -> (string)

The DNS record for certificate verification.

subDomains -> (list)

The subdomains for the domain association.

(structure)

The subdomain for the domain association.

subDomainSetting -> (structure)

Describes the settings for the subdomain.

prefix -> (string)

The prefix setting for the subdomain.

branchName -> (string)

The branch name setting for the subdomain.

verified -> (boolean)

The verified status of the subdomain

dnsRecord -> (string)

The DNS record for the subdomain.

certificate -> (structure)

Describes the SSL/TLS certificate for the domain association. This can be your own custom certificate or the default certificate that Amplify provisions for you.

If you are updating your domain to use a different certificate, `certificate` points to the new certificate that is being created instead of the current active certificate. Otherwise, `certificate` points to the current active certificate.

type -> (string)

The type of SSL/TLS certificate that you want to use.

Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.

Specify `CUSTOM` to use your own certificate that you have already added to Certificate Manager in your Amazon Web Services account. Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide* .

customCertificateArn -> (string)

The Amazon resource name (ARN) for a custom certificate that you have already added to Certificate Manager in your Amazon Web Services account.

This field is required only when the certificate type is `CUSTOM` .

certificateVerificationDNSRecord -> (string)

The DNS record for certificate verification.