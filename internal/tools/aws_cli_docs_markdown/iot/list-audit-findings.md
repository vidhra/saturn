# list-audit-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# list-audit-findings

## Description

Lists the findings (results) of a Device Defender audit or of the audits performed during a specified time period. (Findings are retained for 90 days.)

Requires permission to access the [ListAuditFindings](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListAuditFindings)

`list-audit-findings` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `findings`

## Synopsis

```
list-audit-findings
[--task-id <value>]
[--check-name <value>]
[--resource-identifier <value>]
[--start-time <value>]
[--end-time <value>]
[--list-suppressed-findings | --no-list-suppressed-findings]
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

`--task-id` (string)

A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.

`--check-name` (string)

A filter to limit results to the findings for the specified audit check.

`--resource-identifier` (structure)

Information identifying the noncompliant resource.

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

`--start-time` (timestamp)

A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.

`--end-time` (timestamp)

A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.

`--list-suppressed-findings` | `--no-list-suppressed-findings` (boolean)

Boolean flag indicating whether only the suppressed findings or the unsuppressed findings should be listed. If this parameter isnât provided, the response will list both suppressed and unsuppressed findings.

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

**Example 1: To list all findings from an audit**

The following `list-audit-findings` example lists all findings from an AWS IoT Device Defender audit with a specified task ID.

```
aws iot list-audit-findings \
    --task-id a3aea009955e501a31b764abe1bebd3d
```

Output:

```
{
    "findings": []
}
```

**Example 2: To list findings for an audit check type**

The following `list-audit-findings` example shows findings from AWS IoT Device Defender audits that ran between June 5, 2019 and June 19, 2019 in which devices are sharing a device certificate. When you specify a check name, you must provide a start and end time.

```
aws iot list-audit-findings \
    --check-name DEVICE_CERTIFICATE_SHARED_CHECK \
    --start-time 1559747125 \
    --end-time 1560962028
```

Output:

```
{
    "findings": [
        {
            "taskId": "eeef61068b0eb03c456d746c5a26ee04",
            "checkName": "DEVICE_CERTIFICATE_SHARED_CHECK",
            "taskStartTime": 1560161017.172,
            "findingTime": 1560161017.592,
            "severity": "CRITICAL",
            "nonCompliantResource": {
                "resourceType": "DEVICE_CERTIFICATE",
                "resourceIdentifier": {
                    "deviceCertificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b"
                }
            },
            "relatedResources": [
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "ZipxgAIl"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1560086374068"
                    }
                },
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "ZipxgAIl"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1560081552187",
                        "DISCONNECTION_TIME": "1560086371552"
                    }
                },
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "ZipxgAIl"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1559289863631",
                        "DISCONNECTION_TIME": "1560081532716"
                    }
                }
            ],
            "reasonForNonCompliance": "Certificate shared by one or more devices.",
            "reasonForNonComplianceCode": "CERTIFICATE_SHARED_BY_MULTIPLE_DEVICES"
        },
        {
            "taskId": "bade6b5efd2e1b1569822f6021b39cf5",
            "checkName": "DEVICE_CERTIFICATE_SHARED_CHECK",
            "taskStartTime": 1559988217.27,
            "findingTime": 1559988217.655,
            "severity": "CRITICAL",
            "nonCompliantResource": {
                "resourceType": "DEVICE_CERTIFICATE",
                "resourceIdentifier": {
                    "deviceCertificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b"
                }
            },
            "relatedResources": [
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "xShGENLW"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1559972350825"
                    }
                },
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "xShGENLW"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1559255062002",
                        "DISCONNECTION_TIME": "1559972350616"
                    }
                }
            ],
            "reasonForNonCompliance": "Certificate shared by one or more devices.",
            "reasonForNonComplianceCode": "CERTIFICATE_SHARED_BY_MULTIPLE_DEVICES"
        },
        {
            "taskId": "c23f6233ba2d35879c4bb2810fb5ffd6",
            "checkName": "DEVICE_CERTIFICATE_SHARED_CHECK",
            "taskStartTime": 1559901817.31,
            "findingTime": 1559901817.767,
            "severity": "CRITICAL",
            "nonCompliantResource": {
                "resourceType": "DEVICE_CERTIFICATE",
                "resourceIdentifier": {
                    "deviceCertificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b"
                }
            },
            "relatedResources": [
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "TvnQoEoU"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1559826729768"
                    }
                },
                {
                    "resourceType": "CLIENT_ID",
                    "resourceIdentifier": {
                        "clientId": "TvnQoEoU"
                    },
                    "additionalInfo": {
                        "CONNECTION_TIME": "1559345920964",
                        "DISCONNECTION_TIME": "1559826728402"
                    }
                }
            ],
            "reasonForNonCompliance": "Certificate shared by one or more devices.",
            "reasonForNonComplianceCode": "CERTIFICATE_SHARED_BY_MULTIPLE_DEVICES"
        }
    ]
}
```

For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html) in the *AWS IoT Developer Guide*.

## Output

findings -> (list)

The findings (results) of the audit.

(structure)

The findings (results) of the audit.

findingId -> (string)

A unique identifier for this set of audit findings. This identifier is used to apply mitigation tasks to one or more sets of findings.

taskId -> (string)

The ID of the audit that generated this result (finding).

checkName -> (string)

The audit check that generated this result.

taskStartTime -> (timestamp)

The time the audit started.

findingTime -> (timestamp)

The time the result (finding) was discovered.

severity -> (string)

The severity of the result (finding).

nonCompliantResource -> (structure)

The resource that was found to be noncompliant with the audit check.

resourceType -> (string)

The type of the noncompliant resource.

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

additionalInfo -> (map)

Other information about the noncompliant resource.

key -> (string)

value -> (string)

relatedResources -> (list)

The list of related resources.

(structure)

Information about a related resource.

resourceType -> (string)

The type of resource.

resourceIdentifier -> (structure)

Information that identifies the resource.

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

additionalInfo -> (map)

Other information about the resource.

key -> (string)

value -> (string)

reasonForNonCompliance -> (string)

The reason the resource was noncompliant.

reasonForNonComplianceCode -> (string)

A code that indicates the reason that the resource was noncompliant.

isSuppressed -> (boolean)

Indicates whether the audit finding was suppressed or not during reporting.

nextToken -> (string)

A token that can be used to retrieve the next set of results, or `null` if there are no additional results.