# update-portalÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# update-portal

## Description

Updates an IoT SiteWise Monitor portal.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/UpdatePortal)

## Synopsis

```
update-portal
--portal-id <value>
--portal-name <value>
[--portal-description <value>]
--portal-contact-email <value>
[--portal-logo-image <value>]
--role-arn <value>
[--client-token <value>]
[--notification-sender-email <value>]
[--alarms <value>]
[--portal-type <value>]
[--portal-type-configuration <value>]
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

`--portal-id` (string)

The ID of the portal to update.

`--portal-name` (string)

A new friendly name for the portal.

`--portal-description` (string)

A new description for the portal.

`--portal-contact-email` (string)

The Amazon Web Services administratorâs contact email address.

`--portal-logo-image` (structure)

Contains an image that is one of the following:

- An image file. Choose this option to upload a new image.
- The ID of an existing image. Choose this option to keep an existing image.

id -> (string)

The ID of an existing image. Specify this parameter to keep an existing image.

file -> (structure)

Contains an image file.

data -> (blob)

The image file contents, represented as a base64-encoded string. The file size must be less than 1 MB.

type -> (string)

The file type of the image.

Shorthand Syntax:

```
id=string,file={data=blob,type=string}
```

JSON Syntax:

```
{
  "id": "string",
  "file": {
    "data": blob,
    "type": "PNG"
  }
}
```

`--role-arn` (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of a service role that allows the portalâs users to access your IoT SiteWise resources on your behalf. For more information, see [Using service roles for IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html) in the *IoT SiteWise User Guide* .

`--client-token` (string)

A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Donât reuse this client token if a new idempotent request is required.

`--notification-sender-email` (string)

The email address that sends alarm notifications.

`--alarms` (structure)

Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see [Monitoring with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html) in the *IoT SiteWise Application Guide* .

alarmRoleArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the IAM role that allows the alarm to perform actions and access Amazon Web Services resources and services, such as IoT Events.

notificationLambdaArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Lambda function that manages alarm notifications. For more information, see [Managing alarm notifications](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) in the *IoT Events Developer Guide* .

Shorthand Syntax:

```
alarmRoleArn=string,notificationLambdaArn=string
```

JSON Syntax:

```
{
  "alarmRoleArn": "string",
  "notificationLambdaArn": "string"
}
```

`--portal-type` (string)

Define the type of portal. The value for IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1` . The value for IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2` .

Possible values:

- `SITEWISE_PORTAL_V1`
- `SITEWISE_PORTAL_V2`

`--portal-type-configuration` (map)

The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1` . The value for IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2` .

key -> (string)

value -> (structure)

The configuration entry associated with the specific portal type. The `portalTypeConfiguration` is a map of the `portalTypeKey` to the `PortalTypeEntry` .

portalTools -> (list)

The array of tools associated with the specified portal type. The possible values are `ASSISTANT` and `DASHBOARD` .

(string)

Shorthand Syntax:

```
KeyName1=portalTools=string,string,KeyName2=portalTools=string,string
```

JSON Syntax:

```
{"string": {
      "portalTools": ["string", ...]
    }
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

**To update a portalâs details**

The following `update-portal` example updates a web portal for a wind farm company.

```
aws iotsitewise update-portal \
    --portal-id a1b2c3d4-5678-90ab-cdef-aaaaaEXAMPLE \
    --portal-name WindFarmPortal \
    --portal-description "A portal that contains wind farm projects for Example Corp." \
    --portal-contact-email support@example.com \
    --role-arn arn:aws:iam::123456789012:role/MySiteWiseMonitorServiceRole
```

Output:

```
{
    "portalStatus": {
        "state": "UPDATING"
    }
}
```

For more information, see [Administering your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html) in the *AWS IoT SiteWise User Guide*.

## Output

portalStatus -> (structure)

The status of the portal, which contains a state (`UPDATING` after successfully calling this operation) and any error message.

state -> (string)

The current state of the portal.

error -> (structure)

Contains associated error information, if any.

code -> (string)

The error code.

message -> (string)

The error message.