# describe-fhir-datastoreÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-datastore.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-datastore.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [healthlake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html#cli-aws-healthlake) ]

# describe-fhir-datastore

## Description

Gets the properties associated with the FHIR data store, including the data store ID, data store ARN, data store name, data store status, when the data store was created, data store type version, and the data storeâs endpoint.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/healthlake-2017-07-01/DescribeFHIRDatastore)

## Synopsis

```
describe-fhir-datastore
--datastore-id <value>
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

`--datastore-id` (string)

The AWS-generated data store ID.

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

**To describe a FHIR data store**

The following `describe-fhir-datastore` example demonstrates how to find the properties of a data store in AWS HealthLake.

```
aws healthlake describe-fhir-datastore \
    --datastore-id "1f2f459836ac6c513ce899f9e4f66a59"
```

Output:

```
{
    "DatastoreProperties": {
        "PreloadDataConfig": {
            "PreloadDataType": "SYNTHEA"
        },
        "SseConfiguration": {
            "KmsEncryptionConfig": {
                "CmkType": "CUSTOMER_MANAGED_KMS_KEY",
                "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
            }
        },
        "DatastoreName": "Demo",
        "DatastoreArn": "arn:aws:healthlake:us-east-1:<AWS Account ID>:datastore/<Data store ID>",
        "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/<Data store ID>/r4/",
        "DatastoreStatus": "ACTIVE",
        "DatastoreTypeVersion": "R4",
        "CreatedAt": 1603761064.881,
        "DatastoreId": "<Data store ID>",
        "IdentityProviderConfiguration": {
            "AuthorizationStrategy": "AWS_AUTH",
            "FineGrainedAuthorizationEnabled": false
        }
    }
}
```

For more information, see [Creating and monitoring a FHIR data stores](https://docs.aws.amazon.com/healthlake/latest/devguide/working-with-FHIR-healthlake.html) in the *AWS HealthLake Developer Guide*.

## Output

DatastoreProperties -> (structure)

All properties associated with a data store, including the data store ID, data store ARN, data store name, data store status, when the data store was created, data store type version, and the data storeâs endpoint.

DatastoreId -> (string)

The AWS-generated ID number for the data store.

DatastoreArn -> (string)

The Amazon Resource Name used in the creation of the data store.

DatastoreName -> (string)

The user-generated name for the data store.

DatastoreStatus -> (string)

The status of the data store.

CreatedAt -> (timestamp)

The time that a data store was created.

DatastoreTypeVersion -> (string)

The FHIR version. Only R4 version data is supported.

DatastoreEndpoint -> (string)

The AWS endpoint for the data store. Each data store will have itâs own endpoint with data store ID in the endpoint URL.

SseConfiguration -> (structure)

The server-side encryption key configuration for a customer provided encryption key (CMK).

KmsEncryptionConfig -> (structure)

The KMS encryption configuration used to provide details for data encryption.

CmkType -> (string)

The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.

KmsKeyId -> (string)

The KMS encryption key id/alias used to encrypt the data store contents at rest.

PreloadDataConfig -> (structure)

The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.

PreloadDataType -> (string)

The type of preloaded data. Only Synthea preloaded data is supported.

IdentityProviderConfiguration -> (structure)

The identity provider that you selected when you created the data store.

AuthorizationStrategy -> (string)

The authorization strategy that you selected when you created the data store.

FineGrainedAuthorizationEnabled -> (boolean)

If you enabled fine-grained authorization when you created the data store.

Metadata -> (string)

The JSON metadata elements that you want to use in your identity provider configuration. Required elements are listed based on the launch specification of the SMART application. For more information on all possible elements, see [Metadata](https://build.fhir.org/ig/HL7/smart-app-launch/conformance.html#metadata) in SMARTâs App Launch specification.

`authorization_endpoint` : The URL to the OAuth2 authorization endpoint.

`grant_types_supported` : An array of grant types that are supported at the token endpoint. You must provide at least one grant type option. Valid options are `authorization_code` and `client_credentials` .

`token_endpoint` : The URL to the OAuth2 token endpoint.

`capabilities` : An array of strings of the SMART capabilities that the authorization server supports.

`code_challenge_methods_supported` : An array of strings of supported PKCE code challenge methods. You must include the `S256` method in the array of PKCE code challenge methods.

IdpLambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function that you want to use to decode the access token created by the authorization server.

ErrorCause -> (structure)

The error cause for the current data store operation.

ErrorMessage -> (string)

The text of the error message.

ErrorCategory -> (string)

The error category of the create/delete data store operation. Possible statuses are RETRYABLE_ERROR or NON_RETRYABLE_ERROR.