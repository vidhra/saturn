# list-audit-suppressionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-suppressions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-suppressions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# list-audit-suppressions

## Description

Lists your Device Defender audit listings.

Requires permission to access the [ListAuditSuppressions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuditSuppressions)

`list-audit-suppressions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `suppressions`

## Synopsis

```
list-audit-suppressions
[--check-name <value>]
[--resource-identifier <value>]
[--ascending-order | --no-ascending-order]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--ascending-order` | `--no-ascending-order` (boolean)

Determines whether suppressions are listed in ascending order by expiration date or not. If parameter isnât provided, `ascendingOrder=true` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To list all audit finding suppressions**

The following `list-audit-suppressions` example lists all active audit finding suppressions.

```
aws iot list-audit-suppressions
```

Output:

```
{
    "suppressions": [
        {
        "checkName": "DEVICE_CERTIFICATE_EXPIRING_CHECK",
            "resourceIdentifier": {
                "deviceCertificateId": "c7691e<shortened>"
            },
        "expirationDate": 1597881600.0,
        "suppressIndefinitely": false
        }
    ]
}
```

For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html) in the *AWS IoT Developers Guide*.

## Output

suppressions -> (list)

List of audit suppressions.

(structure)

Filters out specific findings of a Device Defender audit.

checkName -> (string)

An audit check name. Checks must be enabled for your account. (Use `DescribeAccountAuditConfiguration` to see the list of all checks, including those that are enabled or use `UpdateAccountAuditConfiguration` to select which checks are enabled.)

resourceIdentifier -> (structure)

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

expirationDate -> (timestamp)

The expiration date (epoch timestamp in seconds) that you want the suppression to adhere to.

suppressIndefinitely -> (boolean)

Indicates whether a suppression should exist indefinitely or not.

description -> (string)

The description of the audit suppression.

nextToken -> (string)

A token that can be used to retrieve the next set of results, or `null` if there are no additional results.