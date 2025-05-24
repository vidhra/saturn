# create-usage-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apigateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/index.html#cli-aws-apigateway) ]

# create-usage-plan

## Description

Creates a usage plan with the throttle and quota limits, as well as the associated API stages, specified in the payload.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/CreateUsagePlan)

## Synopsis

```
create-usage-plan
--name <value>
[--description <value>]
[--api-stages <value>]
[--throttle <value>]
[--quota <value>]
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

`--name` (string)

The name of the usage plan.

`--description` (string)

The description of the usage plan.

`--api-stages` (list)

The associated API stages of the usage plan.

(structure)

API stage name of the associated API stage in a usage plan.

apiId -> (string)

API Id of the associated API stage in a usage plan.

stage -> (string)

API stage name of the associated API stage in a usage plan.

throttle -> (map)

Map containing method level throttling information for API stage in a usage plan.

key -> (string)

value -> (structure)

The API request rate limits.

burstLimit -> (integer)

The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.

rateLimit -> (double)

The API target request rate limit.

Shorthand Syntax:

```
apiId=string,stage=string,throttle={KeyName1={burstLimit=integer,rateLimit=double},KeyName2={burstLimit=integer,rateLimit=double}} ...
```

JSON Syntax:

```
[
  {
    "apiId": "string",
    "stage": "string",
    "throttle": {"string": {
          "burstLimit": integer,
          "rateLimit": double
        }
      ...}
  }
  ...
]
```

`--throttle` (structure)

The throttling limits of the usage plan.

burstLimit -> (integer)

The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.

rateLimit -> (double)

The API target request rate limit.

Shorthand Syntax:

```
burstLimit=integer,rateLimit=double
```

JSON Syntax:

```
{
  "burstLimit": integer,
  "rateLimit": double
}
```

`--quota` (structure)

The quota of the usage plan.

limit -> (integer)

The target maximum number of requests that can be made in a given time period.

offset -> (integer)

The number of requests subtracted from the given limit in the initial time period.

period -> (string)

The time period in which the limit applies. Valid values are âDAYâ, âWEEKâ or âMONTHâ.

Shorthand Syntax:

```
limit=integer,offset=integer,period=string
```

JSON Syntax:

```
{
  "limit": integer,
  "offset": integer,
  "period": "DAY"|"WEEK"|"MONTH"
}
```

`--tags` (map)

The key-value map of strings. The valid character set is [a-zA-Z+-=._:/]. The tag key can be up to 128 characters and must not start with `aws:` . The tag value can be up to 256 characters.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To create a usage plan with throttle and quota limits that resets at the beginning of the month**

Command:

```
aws apigateway create-usage-plan --name "New Usage Plan" --description "A new usage plan" --throttle burstLimit=10,rateLimit=5 --quota limit=500,offset=0,period=MONTH
```

## Output

id -> (string)

The identifier of a UsagePlan resource.

name -> (string)

The name of a usage plan.

description -> (string)

The description of a usage plan.

apiStages -> (list)

The associated API stages of a usage plan.

(structure)

API stage name of the associated API stage in a usage plan.

apiId -> (string)

API Id of the associated API stage in a usage plan.

stage -> (string)

API stage name of the associated API stage in a usage plan.

throttle -> (map)

Map containing method level throttling information for API stage in a usage plan.

key -> (string)

value -> (structure)

The API request rate limits.

burstLimit -> (integer)

The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.

rateLimit -> (double)

The API target request rate limit.

throttle -> (structure)

A map containing method level throttling information for API stage in a usage plan.

burstLimit -> (integer)

The API target request burst rate limit. This allows more requests through for a period of time than the target rate limit.

rateLimit -> (double)

The API target request rate limit.

quota -> (structure)

The target maximum number of permitted requests per a given unit time interval.

limit -> (integer)

The target maximum number of requests that can be made in a given time period.

offset -> (integer)

The number of requests subtracted from the given limit in the initial time period.

period -> (string)

The time period in which the limit applies. Valid values are âDAYâ, âWEEKâ or âMONTHâ.

productCode -> (string)

The Amazon Web Services Marketplace product identifier to associate with the usage plan as a SaaS product on the Amazon Web Services Marketplace.

tags -> (map)

The collection of tags. Each tag element is associated with a given resource.

key -> (string)

value -> (string)