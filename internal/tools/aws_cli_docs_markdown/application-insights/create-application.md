# create-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/create-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/index.html#cli-aws-application-insights) ]

# create-application

## Description

Adds an application that is created from a resource group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-insights-2018-11-25/CreateApplication)

## Synopsis

```
create-application
[--resource-group-name <value>]
[--ops-center-enabled | --no-ops-center-enabled]
[--cwe-monitor-enabled | --no-cwe-monitor-enabled]
[--ops-item-sns-topic-arn <value>]
[--sns-notification-arn <value>]
[--tags <value>]
[--auto-config-enabled | --no-auto-config-enabled]
[--auto-create | --no-auto-create]
[--grouping-type <value>]
[--attach-missing-permission | --no-attach-missing-permission]
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

`--resource-group-name` (string)

The name of the resource group.

`--ops-center-enabled` | `--no-ops-center-enabled` (boolean)

When set to `true` , creates opsItems for any problems detected on an application.

`--cwe-monitor-enabled` | `--no-cwe-monitor-enabled` (boolean)

Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as `instance terminated` , `failed deployment` , and others.

`--ops-item-sns-topic-arn` (string)

The SNS topic provided to Application Insights that is associated to the created opsItem. Allows you to receive notifications for updates to the opsItem.

`--sns-notification-arn` (string)

The SNS notification topic ARN.

`--tags` (list)

List of tags to add to the application. tag key (`Key` ) and an associated tag value (`Value` ). The maximum length of a tag key is 128 characters. The maximum length of a tag value is 256 characters.

(structure)

An object that defines the tags associated with an application. A *tag* is a label that you optionally define and associate with an application. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria.

Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

- Tag keys and values are case sensitive.
- For each associated resource, each tag key must be unique and it can have only one value.
- The `aws:` prefix is reserved for use by Amazon Web Services; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want an application to have a specific tag value, donât specify a value for this parameter.

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

`--auto-config-enabled` | `--no-auto-config-enabled` (boolean)

Indicates whether Application Insights automatically configures unmonitored resources in the resource group.

`--auto-create` | `--no-auto-create` (boolean)

Configures all of the resources in the resource group by applying the recommended configurations.

`--grouping-type` (string)

Application Insights can create applications based on a resource group or on an account. To create an account-based application using all of the resources in the account, set this parameter to `ACCOUNT_BASED` .

Possible values:

- `ACCOUNT_BASED`

`--attach-missing-permission` | `--no-attach-missing-permission` (boolean)

If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.

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

ApplicationInfo -> (structure)

Information about the application.

AccountId -> (string)

The Amazon Web Services account ID for the owner of the application.

ResourceGroupName -> (string)

The name of the resource group used for the application.

LifeCycle -> (string)

The lifecycle of the application.

OpsItemSNSTopicArn -> (string)

The SNS topic provided to Application Insights that is associated to the created opsItems to receive SNS notifications for opsItem updates.

SNSNotificationArn -> (string)

The SNS topic ARN that is associated with SNS notifications for updates or issues.

OpsCenterEnabled -> (boolean)

Indicates whether Application Insights will create opsItems for any problem detected by Application Insights for an application.

CWEMonitorEnabled -> (boolean)

Indicates whether Application Insights can listen to CloudWatch events for the application resources, such as `instance terminated` , `failed deployment` , and others.

Remarks -> (string)

The issues on the user side that block Application Insights from successfully monitoring an application. Example remarks include:

- âConfiguring application, detected 1 Errors, 3 Warningsâ
- âConfiguring application, detected 1 Unconfigured Componentsâ

AutoConfigEnabled -> (boolean)

Indicates whether auto-configuration is turned on for this application.

DiscoveryType -> (string)

The method used by Application Insights to onboard your resources.

AttachMissingPermission -> (boolean)

If set to true, the managed policies for SSM and CW will be attached to the instance roles if they are missing.