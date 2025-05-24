# put-draft-app-version-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# put-draft-app-version-template

## Description

Adds or updates the app template for an Resilience Hub application draft version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)

## Synopsis

```
put-draft-app-version-template
--app-arn <value>
--app-template-body <value>
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

`--app-arn` (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

`--app-template-body` (string)

A JSON string that provides information about your application structure. To learn more about the `appTemplateBody` template, see the sample template provided in the *Examples* section.

The `appTemplateBody` JSON string has the following structure:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id1)`resources` **   The list of logical resources that must be included in the Resilience Hub application. Type: Array

### Note

Donât add the resources that you want to exclude.

Each `resources` array item includes the following fields:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id3)`logicalResourceId` *   Logical identifier of the resource. Type: Object Each `logicalResourceId` object includes the following fields:

- `identifier`   Identifier of the resource. Type: String
- `logicalStackName`   The name of the CloudFormation stack this resource belongs to. Type: String
- `resourceGroupName`   The name of the resource group this resource belongs to. Type: String
- `terraformSourceName`   The name of the Terraform S3 state file this resource belongs to. Type: String
- `eksSourceName`   Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.

### Note

This parameter accepts values in âeks-cluster/namespaceâ format.

Type: String
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id5)`type` *   The type of resource. Type: string
- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id7)`name` *   The name of the resource. Type: String
- `additionalInfo`   Additional configuration parameters for an Resilience Hub application. If you want to implement `additionalInfo` through the Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html) .

### Note

Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: `"failover-regions"`   Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id9)`appComponents` **   List of Application Components that this resource belongs to. If an Application Component is not part of the Resilience Hub application, it will be added. Type: Array Each `appComponents` array item includes the following fields:

- `name`   Name of the Application Component. Type: String
- `type`   Type of Application Component. For more information about the types of Application Component, see [Grouping resources in an AppComponent](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html) . Type: String
- `resourceNames`   The list of included resources that are assigned to the Application Component. Type: Array of strings
- `additionalInfo`   Additional configuration parameters for an Resilience Hub application. If you want to implement `additionalInfo` through the Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html) .

### Note

Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: `"failover-regions"`   Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id11)`excludedResources` **   The list of logical resource identifiers to be excluded from the application. Type: Array

### Note

Donât add the resources that you want to include.

Each `excludedResources` array item includes the following fields:

- [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id13)`logicalResourceIds` *   Logical identifier of the resource. Type: Object

### Note

You can configure only one of the following fields:

- `logicalStackName`
- `resourceGroupName`
- `terraformSourceName`
- `eksSourceName`

Each `logicalResourceIds` object includes the following fields:

- `identifier`   Identifier of the resource. Type: String
- `logicalStackName`   The name of the CloudFormation stack this resource belongs to. Type: String
- `resourceGroupName`   The name of the resource group this resource belongs to. Type: String
- `terraformSourceName`   The name of the Terraform S3 state file this resource belongs to. Type: String
- `eksSourceName`   Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.

### Note

This parameter accepts values in âeks-cluster/namespaceâ format.

Type: String

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/put-draft-app-version-template.html#id15)`version` **   Resilience Hub application version.
- `additionalInfo`   Additional configuration parameters for an Resilience Hub application. If you want to implement `additionalInfo` through the Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html) .

### Note

Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account. Key: `"failover-regions"`   Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`

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

appArn -> (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

appVersion -> (string)

The version of the application.