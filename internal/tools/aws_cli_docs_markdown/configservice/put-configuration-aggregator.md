# put-configuration-aggregatorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-aggregator.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-aggregator.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# put-configuration-aggregator

## Description

Creates and updates the configuration aggregator with the selected source accounts and regions. The source account can be individual account(s) or an organization.

`accountIds` that are passed will be replaced with existing accounts. If you want to add additional accounts into the aggregator, call `DescribeConfigurationAggregators` to get the previous accounts and then append new ones.

### Note

Config should be enabled in source accounts and regions you want to aggregate.

If your source type is an organization, you must be signed in to the management account or a registered delegated administrator and all the features must be enabled in your organization. If the caller is a management account, Config calls `EnableAwsServiceAccess` API to enable integration between Config and Organizations. If the caller is a registered delegated administrator, Config calls `ListDelegatedAdministrators` API to verify whether the caller is a valid delegated administrator.

To register a delegated administrator, see [Register a Delegated Administrator](https://docs.aws.amazon.com/config/latest/developerguide/set-up-aggregator-cli.html#register-a-delegated-administrator-cli) in the *Config developer guide* .

### Note

**Tags are added at creation and cannot be updated with this operation**

`PutConfigurationAggregator` is an idempotent API. Subsequent requests wonât create a duplicate resource if one was already created. If a following request has different `tags` values, Config will ignore these differences and treat it as an idempotent request of the previous. In this case, `tags` will not be updated, even if they are different.

Use [TagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/config/latest/APIReference/API_UntagResource.html) to update tags after creation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutConfigurationAggregator)

## Synopsis

```
put-configuration-aggregator
--configuration-aggregator-name <value>
[--account-aggregation-sources <value>]
[--organization-aggregation-source <value>]
[--tags <value>]
[--aggregator-filters <value>]
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

`--configuration-aggregator-name` (string)

The name of the configuration aggregator.

`--account-aggregation-sources` (list)

A list of AccountAggregationSource object.

(structure)

A collection of accounts and regions.

AccountIds -> (list)

The 12-digit account ID of the account being aggregated.

(string)

AllAwsRegions -> (boolean)

If true, aggregate existing Config regions and future regions.

AwsRegions -> (list)

The source regions being aggregated.

(string)

Shorthand Syntax:

```
AccountIds=string,string,AllAwsRegions=boolean,AwsRegions=string,string ...
```

JSON Syntax:

```
[
  {
    "AccountIds": ["string", ...],
    "AllAwsRegions": true|false,
    "AwsRegions": ["string", ...]
  }
  ...
]
```

`--organization-aggregation-source` (structure)

An OrganizationAggregationSource object.

RoleArn -> (string)

ARN of the IAM role used to retrieve Amazon Web Services Organization details associated with the aggregator account.

AwsRegions -> (list)

The source regions being aggregated.

(string)

AllAwsRegions -> (boolean)

If true, aggregate existing Config regions and future regions.

Shorthand Syntax:

```
RoleArn=string,AwsRegions=string,string,AllAwsRegions=boolean
```

JSON Syntax:

```
{
  "RoleArn": "string",
  "AwsRegions": ["string", ...],
  "AllAwsRegions": true|false
}
```

`--tags` (list)

An array of tag object.

(structure)

The tags for the resource. The metadata that you apply to a resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.

Key -> (string)

One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.

Value -> (string)

The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

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

`--aggregator-filters` (structure)

An object to filter configuration recorders in an aggregator. Either `ResourceType` or `ServicePrincipal` is required.

ResourceType -> (structure)

An object to filter the configuration recorders based on the resource types in scope for recording.

Type -> (string)

The type of resource type filter to apply. `INCLUDE` specifies that the list of resource types in the `Value` field will be aggregated and no other resource types will be filtered.

Value -> (list)

Comma-separate list of resource types to filter your aggregated configuration recorders.

(string)

ServicePrincipal -> (structure)

An object to filter service-linked configuration recorders in an aggregator based on the linked Amazon Web Services service.

Type -> (string)

The type of service principal filter to apply. `INCLUDE` specifies that the list of service principals in the `Value` field will be aggregated and no other service principals will be filtered.

Value -> (list)

Comma-separated list of service principals for the linked Amazon Web Services services to filter your aggregated service-linked configuration recorders.

(string)

Shorthand Syntax:

```
ResourceType={Type=string,Value=[string,string]},ServicePrincipal={Type=string,Value=[string,string]}
```

JSON Syntax:

```
{
  "ResourceType": {
    "Type": "INCLUDE",
    "Value": ["string", ...]
  },
  "ServicePrincipal": {
    "Type": "INCLUDE",
    "Value": ["string", ...]
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

ConfigurationAggregator -> (structure)

Returns a ConfigurationAggregator object.

ConfigurationAggregatorName -> (string)

The name of the aggregator.

ConfigurationAggregatorArn -> (string)

The Amazon Resource Name (ARN) of the aggregator.

AccountAggregationSources -> (list)

Provides a list of source accounts and regions to be aggregated.

(structure)

A collection of accounts and regions.

AccountIds -> (list)

The 12-digit account ID of the account being aggregated.

(string)

AllAwsRegions -> (boolean)

If true, aggregate existing Config regions and future regions.

AwsRegions -> (list)

The source regions being aggregated.

(string)

OrganizationAggregationSource -> (structure)

Provides an organization and list of regions to be aggregated.

RoleArn -> (string)

ARN of the IAM role used to retrieve Amazon Web Services Organization details associated with the aggregator account.

AwsRegions -> (list)

The source regions being aggregated.

(string)

AllAwsRegions -> (boolean)

If true, aggregate existing Config regions and future regions.

CreationTime -> (timestamp)

The time stamp when the configuration aggregator was created.

LastUpdatedTime -> (timestamp)

The time of the last update.

CreatedBy -> (string)

Amazon Web Services service that created the configuration aggregator.

AggregatorFilters -> (structure)

An object to filter the data you specify for an aggregator.

ResourceType -> (structure)

An object to filter the configuration recorders based on the resource types in scope for recording.

Type -> (string)

The type of resource type filter to apply. `INCLUDE` specifies that the list of resource types in the `Value` field will be aggregated and no other resource types will be filtered.

Value -> (list)

Comma-separate list of resource types to filter your aggregated configuration recorders.

(string)

ServicePrincipal -> (structure)

An object to filter service-linked configuration recorders in an aggregator based on the linked Amazon Web Services service.

Type -> (string)

The type of service principal filter to apply. `INCLUDE` specifies that the list of service principals in the `Value` field will be aggregated and no other service principals will be filtered.

Value -> (list)

Comma-separated list of service principals for the linked Amazon Web Services services to filter your aggregated service-linked configuration recorders.

(string)