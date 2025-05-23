# delete-audit-suppressionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-audit-suppression.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-audit-suppression.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# delete-audit-suppression

## Description

Deletes a Device Defender audit suppression.

Requires permission to access the [DeleteAuditSuppression](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/DeleteAuditSuppression)

## Synopsis

```
delete-audit-suppression
--check-name <value>
--resource-identifier <value>
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

`--check-name` (string)

An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)

`--resource-identifier` (structure)

Information that identifies the noncompliant resource.

deviceCertificateId -> (string)

The ID of the certificate attached to the resource.

caCertificateId -> (string)

The ID of the CA certificate used to authorize the certificate.

cognitoIdentityPoolId -> (string)

The ID of the Amazon Cognito identity pool.

clientId -> (string)

The client ID.

policyVersionIdentifier -> (structure)

The version of the policy associated with the resource.

policyName -> (string)

The name of the policy.

policyVersionId -> (string)

The ID of the version of the policy associated with the resource.

account -> (string)

The account with which the resource is associated.

iamRoleArn -> (string)

The ARN of the IAM role that has overly permissive actions.

roleAliasArn -> (string)

The ARN of the role alias that has overly permissive actions.

issuerCertificateIdentifier -> (structure)

The issuer certificate identifier.

issuerCertificateSubject -> (string)

The subject of the issuer certificate.

issuerId -> (string)

The issuer ID.

issuerCertificateSerialNumber -> (string)

The issuer certificate serial number.

deviceCertificateArn -> (string)

The ARN of the identified device certificate.

Shorthand Syntax:

```
deviceCertificateId=string,caCertificateId=string,cognitoIdentityPoolId=string,clientId=string,policyVersionIdentifier={policyName=string,policyVersionId=string},account=string,iamRoleArn=string,roleAliasArn=string,issuerCertificateIdentifier={issuerCertificateSubject=string,issuerId=string,issuerCertificateSerialNumber=string},deviceCertificateArn=string
```

JSON Syntax:

```
{
  "deviceCertificateId": "string",
  "caCertificateId": "string",
  "cognitoIdentityPoolId": "string",
  "clientId": "string",
  "policyVersionIdentifier": {
    "policyName": "string",
    "policyVersionId": "string"
  },
  "account": "string",
  "iamRoleArn": "string",
  "roleAliasArn": "string",
  "issuerCertificateIdentifier": {
    "issuerCertificateSubject": "string",
    "issuerId": "string",
    "issuerCertificateSerialNumber": "string"
  },
  "deviceCertificateArn": "string"
}
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

**To delete an audit finding suppression**

The following `delete-audit-suppression` example deletes an audit finding suppression for DEVICE_CERTIFICATE_EXPIRING_CHECK.

```
aws iot delete-audit-suppression \
    --check-name DEVICE_CERTIFICATE_EXPIRING_CHECK \
    --resource-identifier deviceCertificateId="c7691e<shortened>"
```

This command produces no output.

For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html) in the *AWS IoT Developers Guide*.

## Output

None