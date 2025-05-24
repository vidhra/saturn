# update-domain-nameÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-domain-name.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-domain-name.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html#cli-aws-apigateway) ]

# update-domain-name

## Description

Changes information about the DomainName resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/UpdateDomainName)

## Synopsis

```
update-domain-name
--domain-name <value>
[--domain-name-id <value>]
[--patch-operations <value>]
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

`--domain-name` (string)

The name of the DomainName resource to be changed.

`--domain-name-id` (string)

The identifier for the domain name resource. Supported only for private custom domain names.

`--patch-operations` (list)

For more information about supported patch operations, see [Patch Operations](https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html) .

(structure)

For more information about supported patch operations, see [Patch Operations](https://docs.aws.amazon.com/apigateway/latest/api/patch-operations.html) .

op -> (string)

An update operation to be performed with this PATCH request. The valid value can be add, remove, replace or copy. Not all valid operations are supported for a given resource. Support of the operations depends on specific operational contexts. Attempts to apply an unsupported operation on a resource will return an error message..

path -> (string)

The op operationâs target, as identified by a JSON Pointer value that references a location within the targeted resource. For example, if the target resource has an updateable property of {ânameâ:âvalueâ}, the path for this property is /name. If the name property value is a JSON object (e.g., {ânameâ: {âchild/nameâ: âchild-valueâ}}), the path for the child/name property will be /name/child~1name. Any slash (â/â) character appearing in path names must be escaped with â~1â, as shown in the example above. Each op operation can have only one path associated with it.

value -> (string)

The new target value of the update operation. It is applicable for the add or replace operation. When using AWS CLI to update a property of a JSON value, enclose the JSON object with a pair of single quotes in a Linux shell, e.g., â{âaâ: â¦}â.

from -> (string)

The copy update operationâs source as identified by a JSON-Pointer value referencing the location within the targeted resource to copy the value from. For example, to promote a canary deployment, you copy the canary deployment ID to the affiliated deployment ID by calling a PATCH request on a Stage resource with âopâ:âcopyâ, âfromâ:â/canarySettings/deploymentIdâ and âpathâ:â/deploymentIdâ.

Shorthand Syntax:

```
op=string,path=string,value=string,from=string ...
```

JSON Syntax:

```
[
  {
    "op": "add"|"remove"|"replace"|"move"|"copy"|"test",
    "path": "string",
    "value": "string",
    "from": "string"
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

**To change the certificate name for a custom domain name**

The following `update-domain-name` example changes the certificate name for a custom domain.

```
aws apigateway update-domain-name \
    --domain-name api.domain.tld \
    --patch-operations op='replace',path='/certificateArn',value='arn:aws:acm:us-west-2:111122223333:certificate/CERTEXAMPLE123EXAMPLE'
```

Output:

```
{
    "domainName": "api.domain.tld",
    "distributionDomainName": "d123456789012.cloudfront.net",
    "certificateArn": "arn:aws:acm:us-west-2:111122223333:certificate/CERTEXAMPLE123EXAMPLE",
    "certificateUploadDate": 1462565487
}
```

For more information, see [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *Amazon API Gateway Developer Guide*.

## Output

domainName -> (string)

The custom domain name as an API host name, for example, `my-api.example.com` .

domainNameId -> (string)

The identifier for the domain name resource. Supported only for private custom domain names.

domainNameArn -> (string)

The ARN of the domain name. Supported only for private custom domain names.

certificateName -> (string)

The name of the certificate that will be used by edge-optimized endpoint or private endpoint for this domain name.

certificateArn -> (string)

The reference to an Amazon Web Services-managed certificate that will be used by edge-optimized endpoint or private endpoint for this domain name. Certificate Manager is the only supported source.

certificateUploadDate -> (timestamp)

The timestamp when the certificate that was used by edge-optimized endpoint or private endpoint for this domain name was uploaded.

regionalDomainName -> (string)

The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name. The regional domain name is returned by API Gateway when you create a regional endpoint.

regionalHostedZoneId -> (string)

The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.

regionalCertificateName -> (string)

The name of the certificate that will be used for validating the regional domain name.

regionalCertificateArn -> (string)

The reference to an Amazon Web Services-managed certificate that will be used for validating the regional domain name. Certificate Manager is the only supported source.

distributionDomainName -> (string)

The domain name of the Amazon CloudFront distribution associated with this custom domain name for an edge-optimized endpoint. You set up this association when adding a DNS record pointing the custom domain name to this distribution name. For more information about CloudFront distributions, see the Amazon CloudFront documentation.

distributionHostedZoneId -> (string)

The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The valid value is `Z2FDTNDATAQYW2` for all the regions. For more information, see Set up a Regional Custom Domain Name and AWS Regions and Endpoints for API Gateway.

endpointConfiguration -> (structure)

The endpoint configuration of this DomainName showing the endpoint types and IP address types of the domain name.

types -> (list)

A list of endpoint types of an API (RestApi) or its custom domain name (DomainName). For an edge-optimized API and its custom domain name, the endpoint type is `"EDGE"` . For a regional API and its custom domain name, the endpoint type is `REGIONAL` . For a private API, the endpoint type is `PRIVATE` .

(string)

The endpoint type. The valid values are `EDGE` for edge-optimized API setup, most suitable for mobile applications; `REGIONAL` for regional API endpoint setup, most suitable for calling from AWS Region; and `PRIVATE` for private APIs.

ipAddressType -> (string)

The IP address types that can invoke an API (RestApi) or a DomainName. Use `ipv4` to allow only IPv4 addresses to invoke an API or DomainName, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke an API or a DomainName. For the `PRIVATE` endpoint type, only `dualstack` is supported.

vpcEndpointIds -> (list)

A list of VpcEndpointIds of an API (RestApi) against which to create Route53 ALIASes. It is only supported for `PRIVATE` endpoint type.

(string)

domainNameStatus -> (string)

The status of the DomainName migration. The valid values are `AVAILABLE` and `UPDATING` . If the status is `UPDATING` , the domain cannot be modified further until the existing operation is complete. If it is `AVAILABLE` , the domain can be updated.

domainNameStatusMessage -> (string)

An optional text message containing detailed information about status of the DomainName migration.

securityPolicy -> (string)

The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2` .

tags -> (map)

The collection of tags. Each tag element is associated with a given resource.

key -> (string)

value -> (string)

mutualTlsAuthentication -> (structure)

The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.

truststoreUri -> (string)

An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example `s3://bucket-name/key-name` . The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.

truststoreVersion -> (string)

The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.

truststoreWarnings -> (list)

A list of warnings that API Gateway returns while processing your truststore. Invalid certificates produce warnings. Mutual TLS is still enabled, but some clients might not be able to access your API. To resolve warnings, upload a new truststore to S3, and then update you domain name to use the new version.

(string)

ownershipVerificationCertificateArn -> (string)

The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the regionalCertificateArn.

managementPolicy -> (string)

A stringified JSON policy document that applies to the API Gateway Management service for this DomainName. This policy document controls access for access association sources to create domain name access associations with this DomainName. Supported only for private custom domain names.

policy -> (string)

A stringified JSON policy document that applies to the `execute-api` service for this DomainName regardless of the caller and Method configuration. Supported only for private custom domain names.