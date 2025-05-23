# describe-provisioned-product-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [servicecatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/index.html#cli-aws-servicecatalog) ]

# describe-provisioned-product-plan

## Description

Gets information about the resource changes for the specified plan.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/servicecatalog-2015-12-10/DescribeProvisionedProductPlan)

## Synopsis

```
describe-provisioned-product-plan
[--accept-language <value>]
--plan-id <value>
[--page-size <value>]
[--page-token <value>]
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

`--accept-language` (string)

The language code.

- `jp` - Japanese
- `zh` - Chinese

`--plan-id` (string)

The plan identifier.

`--page-size` (integer)

The maximum number of items to return with this call.

`--page-token` (string)

The page token for the next set of results. To retrieve the first set of results, use null.

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

ProvisionedProductPlanDetails -> (structure)

Information about the plan.

CreatedTime -> (timestamp)

The UTC time stamp of the creation time.

PathId -> (string)

The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use  ListLaunchPaths .

ProductId -> (string)

The product identifier.

PlanName -> (string)

The name of the plan.

PlanId -> (string)

The plan identifier.

ProvisionProductId -> (string)

The product identifier.

ProvisionProductName -> (string)

The user-friendly name of the provisioned product.

PlanType -> (string)

The plan type.

ProvisioningArtifactId -> (string)

The identifier of the provisioning artifact.

Status -> (string)

The status.

UpdatedTime -> (timestamp)

The UTC time stamp when the plan was last updated.

NotificationArns -> (list)

Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.

(string)

ProvisioningParameters -> (list)

Parameters specified by the administrator that are required for provisioning the product.

(structure)

The parameter key-value pair used to update a provisioned product.

Key -> (string)

The parameter key.

Value -> (string)

The parameter value.

UsePreviousValue -> (boolean)

If set to true, `Value` is ignored and the previous parameter value is kept.

Tags -> (list)

One or more tags.

(structure)

Information about a tag. A tag is a key-value pair. Tags are propagated to the resources created when provisioning a product.

Key -> (string)

The tag key.

Value -> (string)

The value for this key.

StatusMessage -> (string)

The status message.

ResourceChanges -> (list)

Information about the resource changes that will occur when the plan is executed.

(structure)

Information about a resource change that will occur when a plan is executed.

Action -> (string)

The change action.

LogicalResourceId -> (string)

The ID of the resource, as defined in the CloudFormation template.

PhysicalResourceId -> (string)

The ID of the resource, if it was already created.

ResourceType -> (string)

The type of resource.

Replacement -> (string)

If the change type is `Modify` , indicates whether the existing resource is deleted and replaced with a new one.

Scope -> (list)

The change scope.

(string)

Details -> (list)

Information about the resource changes.

(structure)

Information about a change to a resource attribute.

Target -> (structure)

Information about the resource attribute to be modified.

Attribute -> (string)

The attribute to be changed.

Name -> (string)

If the attribute is `Properties` , the value is the name of the property. Otherwise, the value is null.

RequiresRecreation -> (string)

If the attribute is `Properties` , indicates whether a change to this property causes the resource to be re-created.

Evaluation -> (string)

For static evaluations, the value of the resource attribute will change and the new value is known. For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.

CausingEntity -> (string)

The ID of the entity that caused the change.

NextPageToken -> (string)

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.