# update-dashboardÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-dashboard.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-dashboard.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# update-dashboard

## Description

Updates the specified dashboard.

To set a refresh schedule, CloudTrail must be granted permissions to run the `StartDashboardRefresh` operation to refresh the dashboard on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to the dashboard. For more information, see [Resource-based policy example for a dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards) in the *CloudTrail User Guide* .

CloudTrail runs queries to populate the dashboardâs widgets during a manual or scheduled refresh. CloudTrail must be granted permissions to run the `StartQuery` operation on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to each event data store. For more information, see [Example: Allow CloudTrail to run queries to populate a dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard) in the *CloudTrail User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/UpdateDashboard)

## Synopsis

```
update-dashboard
--dashboard-id <value>
[--widgets <value>]
[--refresh-schedule <value>]
[--termination-protection-enabled | --no-termination-protection-enabled]
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

`--dashboard-id` (string)

The name or ARN of the dashboard.

`--widgets` (list)

An array of widgets for the dashboard. A custom dashboard can have a maximum of 10 widgets.

To add new widgets, pass in an array that includes the existing widgets along with any new widgets. Run the `GetDashboard` operation to get the list of widgets for the dashboard.

To remove widgets, pass in an array that includes the existing widgets minus the widgets you want removed.

(structure)

Contains information about a widget on a CloudTrail Lake dashboard.

QueryStatement -> (string)

The query statement for the widget. For custom dashboard widgets, you can query across multiple event data stores as long as all event data stores exist in your account.

### Note

When a query uses `?` with `eventTime` , `?` must be surrounded by single quotes as follows: `'?'` .

QueryParameters -> (list)

The optional query parameters. The following query parameters are valid: `$StartTime$` , `$EndTime$` , and `$Period$` .

(string)

ViewProperties -> (map)

The view properties for the widget. For more information about view properties, see [View properties for widgets](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html) in the *CloudTrail User Guide* .

key -> (string)

value -> (string)

Shorthand Syntax:

```
QueryStatement=string,QueryParameters=string,string,ViewProperties={KeyName1=string,KeyName2=string} ...
```

JSON Syntax:

```
[
  {
    "QueryStatement": "string",
    "QueryParameters": ["string", ...],
    "ViewProperties": {"string": "string"
      ...}
  }
  ...
]
```

`--refresh-schedule` (structure)

The refresh schedule configuration for the dashboard.

Frequency -> (structure)

The frequency at which you want the dashboard refreshed.

Unit -> (string)

The unit to use for the refresh.

For custom dashboards, the unit can be `HOURS` or `DAYS` .

For the Highlights dashboard, the `Unit` must be `HOURS` .

Value -> (integer)

The value for the refresh schedule.

For custom dashboards, the following values are valid when the unit is `HOURS` : `1` , `6` , `12` , `24`

For custom dashboards, the only valid value when the unit is `DAYS` is `1` .

For the Highlights dashboard, the `Value` must be `6` .

Status -> (string)

Specifies whether the refresh schedule is enabled. Set the value to `ENABLED` to enable the refresh schedule, or to `DISABLED` to turn off the refresh schedule.

TimeOfDay -> (string)

The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00.

Shorthand Syntax:

```
Frequency={Unit=string,Value=integer},Status=string,TimeOfDay=string
```

JSON Syntax:

```
{
  "Frequency": {
    "Unit": "HOURS"|"DAYS",
    "Value": integer
  },
  "Status": "ENABLED"|"DISABLED",
  "TimeOfDay": "string"
}
```

`--termination-protection-enabled` | `--no-termination-protection-enabled` (boolean)

Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled.

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

DashboardArn -> (string)

The ARN for the dashboard.

Name -> (string)

The name for the dashboard.

Type -> (string)

The type of dashboard.

Widgets -> (list)

An array of widgets for the dashboard.

(structure)

A widget on a CloudTrail Lake dashboard.

QueryAlias -> (string)

The query alias used to identify the query for the widget.

QueryStatement -> (string)

The SQL query statement for the widget.

QueryParameters -> (list)

The query parameters for the widget.

(string)

ViewProperties -> (map)

The view properties for the widget. For more information about view properties, see [View properties for widgets](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html) in the *CloudTrail User Guide* ..

key -> (string)

value -> (string)

RefreshSchedule -> (structure)

The refresh schedule for the dashboard, if configured.

Frequency -> (structure)

The frequency at which you want the dashboard refreshed.

Unit -> (string)

The unit to use for the refresh.

For custom dashboards, the unit can be `HOURS` or `DAYS` .

For the Highlights dashboard, the `Unit` must be `HOURS` .

Value -> (integer)

The value for the refresh schedule.

For custom dashboards, the following values are valid when the unit is `HOURS` : `1` , `6` , `12` , `24`

For custom dashboards, the only valid value when the unit is `DAYS` is `1` .

For the Highlights dashboard, the `Value` must be `6` .

Status -> (string)

Specifies whether the refresh schedule is enabled. Set the value to `ENABLED` to enable the refresh schedule, or to `DISABLED` to turn off the refresh schedule.

TimeOfDay -> (string)

The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00.

TerminationProtectionEnabled -> (boolean)

Indicates whether termination protection is enabled for the dashboard.

CreatedTimestamp -> (timestamp)

The timestamp that shows when the dashboard was created.

UpdatedTimestamp -> (timestamp)

The timestamp that shows when the dashboard was updated.