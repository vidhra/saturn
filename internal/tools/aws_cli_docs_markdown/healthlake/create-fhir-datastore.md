# create-fhir-datastoreÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/create-fhir-datastore.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/create-fhir-datastore.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [healthlake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/index.html#cli-aws-healthlake) ]

# create-fhir-datastore

## Description

Creates a data store that can ingest and export FHIR formatted data.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/healthlake-2017-07-01/CreateFHIRDatastore)

## Synopsis

```
create-fhir-datastore
[--datastore-name <value>]
--datastore-type-version <value>
[--sse-configuration <value>]
[--preload-data-config <value>]
[--client-token <value>]
[--tags <value>]
[--identity-provider-configuration <value>]
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

`--datastore-name` (string)

The user generated name for the data store.

`--datastore-type-version` (string)

The FHIR version of the data store. The only supported version is R4.

Possible values:

- `R4`

`--sse-configuration` (structure)

The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.

KmsEncryptionConfig -> (structure)

The KMS encryption configuration used to provide details for data encryption.

CmkType -> (string)

The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and AWS owned CMKs.

KmsKeyId -> (string)

The KMS encryption key id/alias used to encrypt the data store contents at rest.

Shorthand Syntax:

```
KmsEncryptionConfig={CmkType=string,KmsKeyId=string}
```

JSON Syntax:

```
{
  "KmsEncryptionConfig": {
    "CmkType": "CUSTOMER_MANAGED_KMS_KEY"|"AWS_OWNED_KMS_KEY",
    "KmsKeyId": "string"
  }
}
```

`--preload-data-config` (structure)

Optional parameter to preload data upon creation of the data store. Currently, the only supported preloaded data is synthetic data generated from Synthea.

PreloadDataType -> (string)

The type of preloaded data. Only Synthea preloaded data is supported.

Shorthand Syntax:

```
PreloadDataType=string
```

JSON Syntax:

```
{
  "PreloadDataType": "SYNTHEA"
}
```

`--client-token` (string)

Optional user provided token used for ensuring idempotency.

`--tags` (list)

Resource tags that are applied to a data store when it is created.

(structure)

A tag is a label consisting of a user-defined key and value. The form for tags is {âKeyâ, âValueâ}

Key -> (string)

The key portion of a tag. Tag keys are case sensitive.

Value -> (string)

The value portion of a tag. Tag values are case sensitive.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--identity-provider-configuration` (structure)

The configuration of the identity provider that you want to use for your data store.

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

Shorthand Syntax:

```
AuthorizationStrategy=string,FineGrainedAuthorizationEnabled=boolean,Metadata=string,IdpLambdaArn=string
```

JSON Syntax:

```
{
  "AuthorizationStrategy": "SMART_ON_FHIR_V1"|"SMART_ON_FHIR"|"AWS_AUTH",
  "FineGrainedAuthorizationEnabled": true|false,
  "Metadata": "string",
  "IdpLambdaArn": "string"
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

**Example 1: Create a SigV4-enabled HealthLake data store**

The following `create-fhir-datastore` example demonstrates how to create a new data store in AWS HealthLake.

```
aws healthlake create-fhir-datastore \
    --datastore-type-version R4 \
    --datastore-name "FhirTestDatastore"
```

Output:

```
{
    "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/",
    "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)",
    "DatastoreStatus": "CREATING",
    "DatastoreId": "(Data store ID)"
}
```

**Example 2: Create a SMART on FHIR-enabled HealthLake data store**

The following `create-fhir-datastore` example demonstrates how to create a new SMART on FHIR-enabled data store in AWS HealthLake.

```
aws healthlake create-fhir-datastore \
    --datastore-name "your-data-store-name" \
    --datastore-type-version R4 \
    --preload-data-config PreloadDataType="SYNTHEA" \
    --sse-configuration '{ "KmsEncryptionConfig": {  "CmkType": "CUSTOMER_MANAGED_KMS_KEY", "KmsKeyId": "arn:aws:kms:us-east-1:your-account-id:key/your-key-id" } }' \
    --identity-provider-configuration  file://identity_provider_configuration.json
```

Contents of `identity_provider_configuration.json`:

```
{
    "AuthorizationStrategy": "SMART_ON_FHIR_V1",
    "FineGrainedAuthorizationEnabled": true,
    "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
    "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\"]}"
}
```

Output:

```
{
    "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/",
    "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)",
    "DatastoreStatus": "CREATING",
    "DatastoreId": "(Data store ID)"
}
```

For more information, see [Creating and monitoring a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/working-with-FHIR-healthlake.html) in the *AWS HealthLake Developer Guide*.

## Output

DatastoreId -> (string)

The AWS-generated data store id. This id is in the output from the initial data store creation call.

DatastoreArn -> (string)

The data store ARN is generated during the creation of the data store and can be found in the output from the initial data store creation call.

DatastoreStatus -> (string)

The status of the FHIR data store.

DatastoreEndpoint -> (string)

The AWS endpoint for the created data store.