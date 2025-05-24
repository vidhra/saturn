# describe-security-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-security-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/describe-security-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-containers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html#cli-aws-emr-containers) ]

# describe-security-configuration

## Description

Displays detailed information about a specified security configuration. Security configurations in Amazon EMR on EKS are templates for different security setups. You can use security configurations to configure the Lake Formation integration setup. You can also create a security configuration to re-use a security setup each time you create a virtual cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/emr-containers-2020-10-01/DescribeSecurityConfiguration)

## Synopsis

```
describe-security-configuration
--id <value>
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

The ID of the security configuration.

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

securityConfiguration -> (structure)

Details of the security configuration.

id -> (string)

The ID of the security configuration.

name -> (string)

The name of the security configuration.

arn -> (string)

The ARN (Amazon Resource Name) of the security configuration.

createdAt -> (timestamp)

The date and time that the job run was created.

createdBy -> (string)

The user who created the job run.

securityConfigurationData -> (structure)

Security configuration inputs for the request.

authorizationConfiguration -> (structure)

Authorization-related configuration input for the security configuration.

lakeFormationConfiguration -> (structure)

Lake Formation related configuration inputs for the security configuration.

authorizedSessionTagValue -> (string)

The session tag to authorize Amazon EMR on EKS for API calls to Lake Formation.

secureNamespaceInfo -> (structure)

The namespace input of the system job.

clusterId -> (string)

The ID of the Amazon EKS cluster where Amazon EMR on EKS jobs run.

namespace -> (string)

The namespace of the Amazon EKS cluster where the system jobs run.

queryEngineRoleArn -> (string)

The query engine IAM role ARN that is tied to the secure Spark job. The `QueryEngine` role assumes the `JobExecutionRole` to execute all the Lake Formation calls.

encryptionConfiguration -> (structure)

Encryption-related configuration input for the security configuration.

inTransitEncryptionConfiguration -> (structure)

In-transit encryption-related input for the security configuration.

tlsCertificateConfiguration -> (structure)

TLS certificate-related configuration input for the security configuration.

certificateProviderType -> (string)

The TLS certificate type. Acceptable values: `PEM` or `Custom` .

publicCertificateSecretArn -> (string)

Secrets Manager ARN that contains the public TLS certificate contents, used for communication between the user job and the system job.

privateCertificateSecretArn -> (string)

Secrets Manager ARN that contains the private TLS certificate contents, used for communication between the user job and the system job.

tags -> (map)

The tags to assign to the security configuration.

key -> (string)

value -> (string)