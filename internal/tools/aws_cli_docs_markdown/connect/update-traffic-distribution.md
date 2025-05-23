# update-traffic-distributionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-traffic-distribution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-traffic-distribution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# update-traffic-distribution

## Description

Updates the traffic distribution for a given traffic distribution group.

### Warning

When you shift telephony traffic, also shift agents and/or agent sign-ins to ensure they can handle the calls in the other Region. If you donât shift the agents, voice calls will go to the shifted Region but there wonât be any agents available to receive the calls.

### Note

The `SignInConfig` distribution is available only on a default `TrafficDistributionGroup` (see the `IsDefault` parameter in the [TrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html) data type). If you call `UpdateTrafficDistribution` with a modified `SignInConfig` and a non-default `TrafficDistributionGroup` , an `InvalidRequestException` is returned.

For more information about updating a traffic distribution group, see [Update telephony traffic distribution across Amazon Web Services Regions](https://docs.aws.amazon.com/connect/latest/adminguide/update-telephony-traffic-distribution.html) in the *Amazon Connect Administrator Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateTrafficDistribution)

## Synopsis

```
update-traffic-distribution
--id <value>
[--telephony-config <value>]
[--sign-in-config <value>]
[--agent-config <value>]
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

The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.

`--telephony-config` (structure)

The distribution of traffic between the instance and its replica(s).

Distributions -> (list)

Information about traffic distributions.

(structure)

Information about a traffic distribution.

Region -> (string)

The Amazon Web Services Region where the traffic is distributed.

Percentage -> (integer)

The percentage of the traffic that is distributed, in increments of 10.

Shorthand Syntax:

```
Distributions=[{Region=string,Percentage=integer},{Region=string,Percentage=integer}]
```

JSON Syntax:

```
{
  "Distributions": [
    {
      "Region": "string",
      "Percentage": integer
    }
    ...
  ]
}
```

`--sign-in-config` (structure)

The distribution that determines which Amazon Web Services Regions should be used to sign in agents in to both the instance and its replica(s).

Distributions -> (list)

Information about traffic distributions.

(structure)

The distribution of sign in traffic between the instance and its replica(s).

Region -> (string)

The Amazon Web Services Region of the sign in distribution.

Enabled -> (boolean)

Whether sign in distribution is enabled.

Shorthand Syntax:

```
Distributions=[{Region=string,Enabled=boolean},{Region=string,Enabled=boolean}]
```

JSON Syntax:

```
{
  "Distributions": [
    {
      "Region": "string",
      "Enabled": true|false
    }
    ...
  ]
}
```

`--agent-config` (structure)

The distribution of agents between the instance and its replica(s).

Distributions -> (list)

Information about traffic distributions.

(structure)

Information about a traffic distribution.

Region -> (string)

The Amazon Web Services Region where the traffic is distributed.

Percentage -> (integer)

The percentage of the traffic that is distributed, in increments of 10.

Shorthand Syntax:

```
Distributions=[{Region=string,Percentage=integer},{Region=string,Percentage=integer}]
```

JSON Syntax:

```
{
  "Distributions": [
    {
      "Region": "string",
      "Percentage": integer
    }
    ...
  ]
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