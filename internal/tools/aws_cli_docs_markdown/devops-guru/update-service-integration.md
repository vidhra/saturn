# update-service-integrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-service-integration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/update-service-integration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [devops-guru](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/index.html#cli-aws-devops-guru) ]

# update-service-integration

## Description

Enables or disables integration with a service that can be integrated with DevOps Guru. The one service that can be integrated with DevOps Guru is Amazon Web Services Systems Manager, which can be used to create an OpsItem for each generated insight.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/devops-guru-2020-12-01/UpdateServiceIntegration)

## Synopsis

```
update-service-integration
--service-integration <value>
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

`--service-integration` (structure)

An `IntegratedServiceConfig` object used to specify the integrated service you want to update, and whether you want to update it to enabled or disabled.

OpsCenter -> (structure)

Information about whether DevOps Guru is configured to create an OpsItem in Amazon Web Services Systems Manager OpsCenter for each created insight. You can use this to update the configuration.

OptInStatus -> (string)

Specifies if DevOps Guru is enabled to create an Amazon Web Services Systems Manager OpsItem for each created insight.

LogsAnomalyDetection -> (structure)

Information about whether DevOps Guru is configured to perform log anomaly detection on Amazon CloudWatch log groups.

OptInStatus -> (string)

Specifies if DevOps Guru is configured to perform log anomaly detection on CloudWatch log groups.

KMSServerSideEncryption -> (structure)

Information about whether DevOps Guru is configured to encrypt server-side data using KMS.

KMSKeyId -> (string)

Describes the specified KMS key.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with âalias/â. If you specify a predefined Amazon Web Services alias (an Amazon Web Services alias with no key ID), Amazon Web Services KMS associates the alias with an Amazon Web Services managed key and returns its KeyId and Arn in the response. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

Key ID: 1234abcd-12ab-34cd-56ef-1234567890ab

Key ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab

Alias name: alias/ExampleAlias

Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias

OptInStatus -> (string)

Specifies if DevOps Guru is enabled for KMS integration.

Type -> (string)

The type of KMS key used. Customer managed keys are the KMS keys that you create. Amazon Web Services owned keys are keys that are owned and managed by DevOps Guru.

Shorthand Syntax:

```
OpsCenter={OptInStatus=string},LogsAnomalyDetection={OptInStatus=string},KMSServerSideEncryption={KMSKeyId=string,OptInStatus=string,Type=string}
```

JSON Syntax:

```
{
  "OpsCenter": {
    "OptInStatus": "ENABLED"|"DISABLED"
  },
  "LogsAnomalyDetection": {
    "OptInStatus": "ENABLED"|"DISABLED"
  },
  "KMSServerSideEncryption": {
    "KMSKeyId": "string",
    "OptInStatus": "ENABLED"|"DISABLED",
    "Type": "CUSTOMER_MANAGED_KEY"|"AWS_OWNED_KMS_KEY"
  }
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

## Output

None