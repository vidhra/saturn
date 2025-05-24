# create-auto-scaling-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-auto-scaling-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-auto-scaling-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apprunner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/index.html#cli-aws-apprunner) ]

# create-auto-scaling-configuration

## Description

Create an App Runner automatic scaling configuration resource. App Runner requires this resource when you create or update App Runner services and you require non-default auto scaling settings. You can share an auto scaling configuration across multiple services.

Create multiple revisions of a configuration by calling this action multiple times using the same `AutoScalingConfigurationName` . The call returns incremental `AutoScalingConfigurationRevision` values. When you create a service and configure an auto scaling configuration resource, the service uses the latest active revision of the auto scaling configuration by default. You can optionally configure the service to use a specific revision.

Configure a higher `MinSize` to increase the spread of your App Runner service over more Availability Zones in the Amazon Web Services Region. The tradeoff is a higher minimal cost.

Configure a lower `MaxSize` to control your cost. The tradeoff is lower responsiveness during peak demand.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apprunner-2020-05-15/CreateAutoScalingConfiguration)

## Synopsis

```
create-auto-scaling-configuration
--auto-scaling-configuration-name <value>
[--max-concurrency <value>]
[--min-size <value>]
[--max-size <value>]
[--tags <value>]
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

`--auto-scaling-configuration-name` (string)

A name for the auto scaling configuration. When you use it for the first time in an Amazon Web Services Region, App Runner creates revision number `1` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.

### Note

Prior to the release of [Auto scale configuration enhancements](https://docs.aws.amazon.com/apprunner/latest/relnotes/release-2023-09-22-auto-scale-config.html) , the name `DefaultConfiguration` was reserved.

This restriction is no longer in place. You can now manage `DefaultConfiguration` the same way you manage your custom auto scaling configurations. This means you can do the following with the `DefaultConfiguration` that App Runner provides:

- Create new revisions of the `DefaultConfiguration` .
- Delete the revisions of the `DefaultConfiguration` .
- Delete the auto scaling configuration for which the App Runner `DefaultConfiguration` was created.
- If you delete the auto scaling configuration you can create another custom auto scaling configuration with the same `DefaultConfiguration` name. The original `DefaultConfiguration` resource provided by App Runner remains in your account unless you make changes to it.

`--max-concurrency` (integer)

The maximum number of concurrent requests that you want an instance to process. If the number of concurrent requests exceeds this limit, App Runner scales up your service.

Default: `100`

`--min-size` (integer)

The minimum number of instances that App Runner provisions for your service. The service always has at least `MinSize` provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.

App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.

Default: `1`

`--max-size` (integer)

The maximum number of instances that your service scales up to. At most `MaxSize` instances actively serve traffic for your service.

Default: `25`

`--tags` (list)

A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.

(structure)

Describes a tag that is applied to an App Runner resource. A tag is a metadata item consisting of a key-value pair.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

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

**To create a high availability auto scaling configuration**

The following `create-auto-scaling-configuration` example creates an auto scaling configuration optimized for high availability by setting `MinSize` to 5.
With this configuration, App Runner attempts to spread your service instances over the most Availability Zones possible, up to five, depending on the AWS Region.

The call returns an `AutoScalingConfiguration` object with the other settings set to their defaults.
In the example, this is the first call to create a configuration named `high-availability`. The revision is set to 1, and itâs the latest revision.

```
aws apprunner create-auto-scaling-configuration \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "AutoScalingConfigurationName": "high-availability",
    "MinSize": 5
}
```

Output:

```
{
    "AutoScalingConfiguration": {
        "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/2f50e7656d7819fead0f59672e68042e",
        "AutoScalingConfigurationName": "high-availability",
        "AutoScalingConfigurationRevision": 1,
        "CreatedAt": "2020-11-03T00:29:17Z",
        "Latest": true,
        "Status": "ACTIVE",
        "MaxConcurrency": 100,
        "MaxSize": 50,
        "MinSize": 5
    }
}
```

## Output

AutoScalingConfiguration -> (structure)

A description of the App Runner auto scaling configuration thatâs created by this request.

AutoScalingConfigurationArn -> (string)

The Amazon Resource Name (ARN) of this auto scaling configuration.

AutoScalingConfigurationName -> (string)

The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.

AutoScalingConfigurationRevision -> (integer)

The revision of this auto scaling configuration. Itâs unique among all the active configurations (`"Status": "ACTIVE"` ) that share the same `AutoScalingConfigurationName` .

Latest -> (boolean)

Itâs set to `true` for the configuration with the highest `Revision` among all configurations that share the same `AutoScalingConfigurationName` . Itâs set to `false` otherwise.

Status -> (string)

The current state of the auto scaling configuration. If the status of a configuration revision is `INACTIVE` , it was deleted and canât be used. Inactive configuration revisions are permanently removed some time after they are deleted.

MaxConcurrency -> (integer)

The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up.

MinSize -> (integer)

The minimum number of instances that App Runner provisions for a service. The service always has at least `MinSize` provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.

App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.

MaxSize -> (integer)

The maximum number of instances that a service scales up to. At most `MaxSize` instances actively serve traffic for your service.

CreatedAt -> (timestamp)

The time when the auto scaling configuration was created. Itâs in Unix time stamp format.

DeletedAt -> (timestamp)

The time when the auto scaling configuration was deleted. Itâs in Unix time stamp format.

HasAssociatedService -> (boolean)

Indicates if this auto scaling configuration has an App Runner service associated with it. A value of `true` indicates one or more services are associated. A value of `false` indicates no services are associated.

IsDefault -> (boolean)

Indicates if this auto scaling configuration should be used as the default for a new App Runner service that does not have an auto scaling configuration ARN specified during creation. Each account can have only one default `AutoScalingConfiguration` per region. The default `AutoScalingConfiguration` can be any revision under the same `AutoScalingConfigurationName` .