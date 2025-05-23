# update-app-monitorÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/update-app-monitor.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/update-app-monitor.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rum](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/index.html#cli-aws-rum) ]

# update-app-monitor

## Description

Updates the configuration of an existing app monitor. When you use this operation, only the parts of the app monitor configuration that you specify in this operation are changed. For any parameters that you omit, the existing values are kept.

You canât use this operation to change the tags of an existing app monitor. To change the tags of an existing app monitor, use [TagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html) .

To create a new app monitor, use [CreateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html) .

After you update an app monitor, sign in to the CloudWatch RUM console to get the updated JavaScript code snippet to add to your web application. For more information, see [How do I find a code snippet that Iâve already generated?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rum-2018-05-10/UpdateAppMonitor)

## Synopsis

```
update-app-monitor
[--app-monitor-configuration <value>]
[--custom-events <value>]
[--cw-log-enabled | --no-cw-log-enabled]
[--deobfuscation-configuration <value>]
[--domain <value>]
[--domain-list <value>]
--name <value>
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

`--app-monitor-configuration` (structure)

A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you donât include `AppMonitorConfiguration` , you must set up your own authorization method. For more information, see [Authorize your application to send data to Amazon Web Services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html) .

AllowCookies -> (boolean)

If you set this to `true` , the RUM web client sets two cookies, a session cookie and a user cookie. The cookies allow the RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.

EnableXRay -> (boolean)

If you set this to `true` , RUM enables X-Ray tracing for the user sessions that RUM samples. RUM adds an X-Ray trace header to allowed HTTP requests. It also records an X-Ray segment for allowed HTTP requests. You can see traces and segments from these user sessions in the X-Ray console and the CloudWatch ServiceLens console. For more information, see [What is X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

ExcludedPages -> (list)

A list of URLs in your website or application to exclude from RUM data collection.

You canât include both `ExcludedPages` and `IncludedPages` in the same operation.

(string)

FavoritePages -> (list)

A list of pages in your application that are to be displayed with a âfavoriteâ icon in the CloudWatch RUM console.

(string)

GuestRoleArn -> (string)

The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.

### Note

It is possible that an app monitor does not have a value for `GuestRoleArn` . For example, this can happen when you use the console to create an app monitor and you allow CloudWatch RUM to create a new identity pool for Authorization. In this case, `GuestRoleArn` is not present in the [GetAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html) response because it is not stored by the service.

If this issue affects you, you can take one of the following steps:

- Use the Cloud Development Kit (CDK) to create an identity pool and the associated IAM role, and use that for your app monitor.
- Make a separate [GetIdentityPoolRoles](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/API_GetIdentityPoolRoles.html) call to Amazon Cognito to retrieve the `GuestRoleArn` .

IdentityPoolId -> (string)

The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.

IncludedPages -> (list)

If this app monitor is to collect data from only certain pages in your application, this structure lists those pages.

You canât include both `ExcludedPages` and `IncludedPages` in the same operation.

(string)

SessionSampleRate -> (double)

Specifies the portion of user sessions to use for RUM data collection. Choosing a higher portion gives you more data but also incurs more costs.

The range for this value is 0 to 1 inclusive. Setting this to 1 means that 100% of user sessions are sampled, and setting it to 0.1 means that 10% of user sessions are sampled.

If you omit this parameter, the default of 0.1 is used, and 10% of sessions will be sampled.

Telemetries -> (list)

An array that lists the types of telemetry data that this app monitor is to collect.

- `errors` indicates that RUM collects data about unhandled JavaScript errors raised by your application.
- `performance` indicates that RUM collects performance data about how your application and its resources are loaded and rendered. This includes Core Web Vitals.
- `http` indicates that RUM collects data about HTTP errors thrown by your application.

(string)

Shorthand Syntax:

```
AllowCookies=boolean,EnableXRay=boolean,ExcludedPages=string,string,FavoritePages=string,string,GuestRoleArn=string,IdentityPoolId=string,IncludedPages=string,string,SessionSampleRate=double,Telemetries=string,string
```

JSON Syntax:

```
{
  "AllowCookies": true|false,
  "EnableXRay": true|false,
  "ExcludedPages": ["string", ...],
  "FavoritePages": ["string", ...],
  "GuestRoleArn": "string",
  "IdentityPoolId": "string",
  "IncludedPages": ["string", ...],
  "SessionSampleRate": double,
  "Telemetries": ["errors"|"performance"|"http", ...]
}
```

`--custom-events` (structure)

Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be `DISABLED` .

For more information about custom events, see [Send custom events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html) .

Status -> (string)

Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be `DISABLED` .

Shorthand Syntax:

```
Status=string
```

JSON Syntax:

```
{
  "Status": "ENABLED"|"DISABLED"
}
```

`--cw-log-enabled` | `--no-cw-log-enabled` (boolean)

Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.

`--deobfuscation-configuration` (structure)

A structure that contains the configuration for how an app monitor can deobfuscate stack traces.

JavaScriptSourceMaps -> (structure)

A structure that contains the configuration for how an app monitor can unminify JavaScript error stack traces using source maps.

S3Uri -> (string)

The S3Uri of the bucket or folder that stores the source map files. It is required if status is ENABLED.

Status -> (string)

Specifies whether JavaScript error stack traces should be unminified for this app monitor. The default is for JavaScript error stack trace unminification to be `DISABLED` .

Shorthand Syntax:

```
JavaScriptSourceMaps={S3Uri=string,Status=string}
```

JSON Syntax:

```
{
  "JavaScriptSourceMaps": {
    "S3Uri": "string",
    "Status": "ENABLED"|"DISABLED"
  }
}
```

`--domain` (string)

The top-level internet domain name for which your application has administrative authority.

`--domain-list` (list)

List the domain names for which your application has administrative authority. The `UpdateAppMonitor` allows either the domain or the domain list.

(string)

Syntax:

```
"string" "string" ...
```

`--name` (string)

The name of the app monitor to update.

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