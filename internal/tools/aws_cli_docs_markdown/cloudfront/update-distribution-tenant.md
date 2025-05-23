# update-distribution-tenantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution-tenant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution-tenant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudfront](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/index.html#cli-aws-cloudfront) ]

# update-distribution-tenant

## Description

Updates a distribution tenant.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudfront-2020-05-31/UpdateDistributionTenant)

## Synopsis

```
update-distribution-tenant
--id <value>
[--distribution-id <value>]
[--domains <value>]
[--customizations <value>]
[--parameters <value>]
[--connection-group-id <value>]
--if-match <value>
[--managed-certificate-request <value>]
[--enabled | --no-enabled]
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

`--id` (string)

The ID of the distribution tenant.

`--distribution-id` (string)

The ID for the multi-tenant distribution.

`--domains` (list)

The domains to update for the distribution tenant. A domain object can contain only a domain property. You must specify at least one domain. Each distribution tenant can have up to 5 domains.

(structure)

The domain for the specified distribution tenant.

Domain -> (string)

The domain name.

Shorthand Syntax:

```
Domain=string ...
```

JSON Syntax:

```
[
  {
    "Domain": "string"
  }
  ...
]
```

`--customizations` (structure)

Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.

WebAcl -> (structure)

The WAF web ACL.

Action -> (string)

The action for the WAF web ACL customization. You can specify `override` to specify a separate WAF web ACL for the distribution tenant. If you specify `disable` , the distribution tenant wonât have WAF web ACL protections and wonât inherit from the multi-tenant distribution.

Arn -> (string)

The Amazon Resource Name (ARN) of the WAF web ACL.

Certificate -> (structure)

The Certificate Manager (ACM) certificate.

Arn -> (string)

The Amazon Resource Name (ARN) of the ACM certificate.

GeoRestrictions -> (structure)

The geographic restrictions.

RestrictionType -> (string)

The method that you want to use to restrict distribution of your content by country:

- `none` : No geographic restriction is enabled, meaning access to content is not restricted by client geo location.
- `blacklist` : The `Location` elements specify the countries in which you donât want CloudFront to distribute your content.
- `whitelist` : The `Location` elements specify the countries in which you want CloudFront to distribute your content.

Locations -> (list)

The locations for geographic restrictions.

(string)

Shorthand Syntax:

```
WebAcl={Action=string,Arn=string},Certificate={Arn=string},GeoRestrictions={RestrictionType=string,Locations=[string,string]}
```

JSON Syntax:

```
{
  "WebAcl": {
    "Action": "override"|"disable",
    "Arn": "string"
  },
  "Certificate": {
    "Arn": "string"
  },
  "GeoRestrictions": {
    "RestrictionType": "blacklist"|"whitelist"|"none",
    "Locations": ["string", ...]
  }
}
```

`--parameters` (list)

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

(structure)

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

Name -> (string)

The parameter name.

Value -> (string)

The parameter value.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--connection-group-id` (string)

The ID of the target connection group.

`--if-match` (string)

The value of the `ETag` header that you received when retrieving the distribution tenant to update. This value is returned in the response of the `GetDistributionTenant` API operation.

`--managed-certificate-request` (structure)

An object that contains the CloudFront managed ACM certificate request.

ValidationTokenHost -> (string)

Specify how the HTTP validation token will be served when requesting the CloudFront managed ACM certificate.

- For `cloudfront` , CloudFront will automatically serve the validation token. Choose this mode if you can point the domainâs DNS to CloudFront immediately.
- For `self-hosted` , you serve the validation token from your existing infrastructure. Choose this mode when you need to maintain current traffic flow while your certificate is being issued. You can place the validation token at the well-known path on your existing web server, wait for ACM to validate and issue the certificate, and then update your DNS to point to CloudFront.

PrimaryDomainName -> (string)

The primary domain name associated with the CloudFront managed ACM certificate.

CertificateTransparencyLoggingPreference -> (string)

You can opt out of certificate transparency logging by specifying the `disabled` option. Opt in by specifying `enabled` . For more information, see [Certificate Transparency Logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-transparency) in the *Certificate Manager User Guide* .

Shorthand Syntax:

```
ValidationTokenHost=string,PrimaryDomainName=string,CertificateTransparencyLoggingPreference=string
```

JSON Syntax:

```
{
  "ValidationTokenHost": "cloudfront"|"self-hosted",
  "PrimaryDomainName": "string",
  "CertificateTransparencyLoggingPreference": "enabled"|"disabled"
}
```

`--enabled` | `--no-enabled` (boolean)

Indicates whether the distribution tenant should be updated to an enabled state. If you update the distribution tenant and itâs not enabled, the distribution tenant wonât serve traffic.

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

DistributionTenant -> (structure)

The distribution tenant that youâre updating.

Id -> (string)

The ID of the distribution tenant.

DistributionId -> (string)

The ID of the multi-tenant distribution.

Name -> (string)

The name of the distribution tenant.

Arn -> (string)

The Amazon Resource Name (ARN) of the distribution tenant.

Domains -> (list)

The domains associated with the distribution tenant.

(structure)

The details about the domain result.

Domain -> (string)

The specified domain.

Status -> (string)

Whether the domain is active or inactive.

Tags -> (structure)

A complex type that contains zero or more `Tag` elements.

Items -> (list)

A complex type that contains `Tag` elements.

(structure)

A complex type that contains `Tag` key and `Tag` value.

Key -> (string)

A string that contains `Tag` key.

The string length should be between 1 and 128 characters. Valid characters include `a-z` , `A-Z` , `0-9` , space, and the special characters `_ - . : / = + @` .

Value -> (string)

A string that contains an optional `Tag` value.

The string length should be between 0 and 256 characters. Valid characters include `a-z` , `A-Z` , `0-9` , space, and the special characters `_ - . : / = + @` .

Customizations -> (structure)

Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.

WebAcl -> (structure)

The WAF web ACL.

Action -> (string)

The action for the WAF web ACL customization. You can specify `override` to specify a separate WAF web ACL for the distribution tenant. If you specify `disable` , the distribution tenant wonât have WAF web ACL protections and wonât inherit from the multi-tenant distribution.

Arn -> (string)

The Amazon Resource Name (ARN) of the WAF web ACL.

Certificate -> (structure)

The Certificate Manager (ACM) certificate.

Arn -> (string)

The Amazon Resource Name (ARN) of the ACM certificate.

GeoRestrictions -> (structure)

The geographic restrictions.

RestrictionType -> (string)

The method that you want to use to restrict distribution of your content by country:

- `none` : No geographic restriction is enabled, meaning access to content is not restricted by client geo location.
- `blacklist` : The `Location` elements specify the countries in which you donât want CloudFront to distribute your content.
- `whitelist` : The `Location` elements specify the countries in which you want CloudFront to distribute your content.

Locations -> (list)

The locations for geographic restrictions.

(string)

Parameters -> (list)

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

(structure)

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

Name -> (string)

The parameter name.

Value -> (string)

The parameter value.

ConnectionGroupId -> (string)

The ID of the connection group for the distribution tenant. If you donât specify a connection group, CloudFront uses the default connection group.

CreatedTime -> (timestamp)

The date and time when the distribution tenant was created.

LastModifiedTime -> (timestamp)

The date and time when the distribution tenant was updated.

Enabled -> (boolean)

Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant wonât serve traffic.

Status -> (string)

The status of the distribution tenant.

ETag -> (string)

The current version of the distribution tenant.