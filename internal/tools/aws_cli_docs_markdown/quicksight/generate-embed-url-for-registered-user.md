# generate-embed-url-for-registered-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/generate-embed-url-for-registered-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/generate-embed-url-for-registered-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# generate-embed-url-for-registered-user

## Description

Generates an embed URL that you can use to embed an Amazon QuickSight experience in your website. This action can be used for any type of user registered in an Amazon QuickSight account. Before you use this action, make sure that you have configured the relevant Amazon QuickSight resource and permissions.

The following rules apply to the generated URL:

- It contains a temporary bearer token. It is valid for 5 minutes after it is generated. Once redeemed within this period, it cannot be re-used again.
- The URL validity period should not be confused with the actual session lifetime that can be customized using the `` [SessionLifetimeInMinutes](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html#QS-GenerateEmbedUrlForRegisteredUser-request-SessionLifetimeInMinutes) `` parameter. The resulting user session is valid for 15 minutes (minimum) to 10 hours (maximum). The default session duration is 10 hours.
- You are charged only when the URL is used or there is interaction with Amazon QuickSight.

For more information, see [Embedded Analytics](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html) in the *Amazon QuickSight User Guide* .

For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon QuickSight Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser)

## Synopsis

```
generate-embed-url-for-registered-user
--aws-account-id <value>
[--session-lifetime-in-minutes <value>]
--user-arn <value>
--experience-configuration <value>
[--allowed-domains <value>]
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

`--aws-account-id` (string)

The ID for the Amazon Web Services account that contains the dashboard that youâre embedding.

`--session-lifetime-in-minutes` (long)

How many minutes the session is valid. The session lifetime must be in [15-600] minutes range.

`--user-arn` (string)

The Amazon Resource Name for the registered user.

`--experience-configuration` (structure)

The experience that you want to embed. For registered users, you can embed Amazon QuickSight dashboards, Amazon QuickSight visuals, the Amazon QuickSight Q search bar, the Amazon QuickSight Generative Q&A experience, or the entire Amazon QuickSight console.

Dashboard -> (structure)

The configuration details for providing a dashboard embedding experience.

InitialDashboardId -> (string)

The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon QuickSight renders this dashboard if the user has permissions to view it.

If the user does not have permission to view this dashboard, they see a permissions error message.

FeatureConfigurations -> (structure)

The feature configurations of an embbedded Amazon QuickSight dashboard.

StatePersistence -> (structure)

The state persistence settings of an embedded dashboard.

Enabled -> (boolean)

Determines if a Amazon QuickSight dashboardâs state persistence settings are turned on or off.

SharedView -> (structure)

The shared view settings of an embedded dashboard.

Enabled -> (boolean)

The shared view settings of an embedded dashboard.

Bookmarks -> (structure)

The bookmarks configuration for an embedded dashboard in Amazon QuickSight.

Enabled -> (boolean)

A Boolean value that determines whether a user can bookmark an embedded dashboard.

AmazonQInQuickSight -> (structure)

The Amazon Q configurations of an embedded Amazon QuickSight dashboard.

ExecutiveSummary -> (structure)

A generated executive summary of an embedded Amazon QuickSight dashboard.

Enabled -> (boolean)

The executive summary settings of an embedded Amazon QuickSight console or dashboard.

Schedules -> (structure)

The schedules configuration for an embedded Amazon QuickSight dashboard.

Enabled -> (boolean)

The schedules configuration for an embedded Amazon QuickSight dashboard.

RecentSnapshots -> (structure)

The recent snapshots configuration for an Amazon QuickSight embedded dashboard

Enabled -> (boolean)

The recent snapshots configuration for an embedded Amazon QuickSight dashboard.

ThresholdAlerts -> (structure)

The threshold alerts configuration for an Amazon QuickSight embedded dashboard.

Enabled -> (boolean)

The threshold alerts configuration for an embedded Amazon QuickSight dashboard.

QuickSightConsole -> (structure)

The configuration details for providing each Amazon QuickSight console embedding experience. This can be used along with custom permissions to restrict access to certain features. For more information, see [Customizing Access to the Amazon QuickSight Console](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html) in the *Amazon QuickSight User Guide* .

Use `` [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html) `` where you want to provide an authoring portal that allows users to create data sources, datasets, analyses, and dashboards. The users who accesses an embedded Amazon QuickSight console needs to belong to the author or admin security cohort. If you want to restrict permissions to some of these features, add a custom permissions profile to the user with the `` [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html) `` API operation. Use the `` [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html) `` API operation to add a new user with a custom permission profile attached. For more information, see the following sections in the *Amazon QuickSight User Guide* :

- [Embedding the Full Functionality of the Amazon QuickSight Console for Authenticated Users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-full-console-for-authenticated-users.html)
- [Customizing Access to the Amazon QuickSight Console](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html)

For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon QuickSight Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html) .

InitialPath -> (string)

The initial URL path for the Amazon QuickSight console. `InitialPath` is required.

The entry point URL is constrained to the following paths:

- `/start`
- `/start/analyses`
- `/start/dashboards`
- `/start/favorites`
- `/dashboards/DashboardId` . *DashboardId* is the actual ID key from the Amazon QuickSight console URL of the dashboard.
- `/analyses/AnalysisId` . *AnalysisId* is the actual ID key from the Amazon QuickSight console URL of the analysis.

FeatureConfigurations -> (structure)

The embedding configuration of an embedded Amazon QuickSight console.

StatePersistence -> (structure)

The state persistence configurations of an embedded Amazon QuickSight console.

Enabled -> (boolean)

Determines if a Amazon QuickSight dashboardâs state persistence settings are turned on or off.

SharedView -> (structure)

The shared view settings of an embedded dashboard.

Enabled -> (boolean)

The shared view settings of an embedded dashboard.

AmazonQInQuickSight -> (structure)

The Amazon Q configurations of an embedded Amazon QuickSight console.

DataQnA -> (structure)

Adds generative Q&A capabilitiees to an embedded Amazon QuickSight console.

Enabled -> (boolean)

The generative Q&A settings of an embedded Amazon QuickSight console.

GenerativeAuthoring -> (structure)

Adds the generative BI authoring experience to an embedded Amazon QuickSight console.

Enabled -> (boolean)

The generative BI authoring settings of an embedded Amazon QuickSight console.

ExecutiveSummary -> (structure)

Adds the executive summaries feature to an embedded Amazon QuickSight console.

Enabled -> (boolean)

The executive summary settings of an embedded Amazon QuickSight console or dashboard.

DataStories -> (structure)

Adds the data stories feature to an embedded Amazon QuickSight console.

Enabled -> (boolean)

The data story settings of an embedded Amazon QuickSight console.

Schedules -> (structure)

The schedules configuration for an embedded Amazon QuickSight dashboard.

Enabled -> (boolean)

The schedules configuration for an embedded Amazon QuickSight dashboard.

RecentSnapshots -> (structure)

The recent snapshots configuration for an embedded Amazon QuickSight dashboard.

Enabled -> (boolean)

The recent snapshots configuration for an embedded Amazon QuickSight dashboard.

ThresholdAlerts -> (structure)

The threshold alerts configuration for an embedded Amazon QuickSight dashboard.

Enabled -> (boolean)

The threshold alerts configuration for an embedded Amazon QuickSight dashboard.

QSearchBar -> (structure)

The configuration details for embedding the Q search bar.

For more information about embedding the Q search bar, see [Embedding Overview](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html) in the *Amazon QuickSight User Guide* .

InitialTopicId -> (string)

The ID of the legacy Q topic that you want to use as the starting topic in the Q search bar. To locate the topic ID of the topic that you want to use, open the [Amazon QuickSight console](https://quicksight.aws.amazon.com/) , navigate to the **Topics** pane, and choose thre topic that you want to use. The `TopicID` is located in the URL of the topic that opens. When you select an initial topic, you can specify whether or not readers are allowed to select other topics from the list of available topics.

If you donât specify an initial topic or if you specify a new reader experience topic, a list of all shared legacy topics is shown in the Q bar.

DashboardVisual -> (structure)

The type of embedding experience. In this case, Amazon QuickSight visuals.

InitialDashboardVisualId -> (structure)

The visual ID for the visual that you want the user to embed. This ID is included in the output URL. When the URL in response is accessed, Amazon QuickSight renders this visual.

The Amazon Resource Name (ARN) of the dashboard that the visual belongs to must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request will fail with `InvalidParameterValueException` .

DashboardId -> (string)

The ID of the dashboard that has the visual that you want to embed. The `DashboardId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visualâs on-visual menu of the Amazon QuickSight console. You can also get the `DashboardId` with a `ListDashboards` API operation.

SheetId -> (string)

The ID of the sheet that the has visual that you want to embed. The `SheetId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visualâs on-visual menu of the Amazon QuickSight console.

VisualId -> (string)

The ID of the visual that you want to embed. The `VisualID` can be found in the `IDs for developers` section of the `Embed visual` pane of the visualâs on-visual menu of the Amazon QuickSight console.

GenerativeQnA -> (structure)

The configuration details for embedding the Generative Q&A experience.

For more information about embedding the Generative Q&A experience, see [Embedding Overview](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html) in the *Amazon QuickSight User Guide* .

InitialTopicId -> (string)

The ID of the new Q reader experience topic that you want to make the starting topic in the Generative Q&A experience. You can find a topic ID by navigating to the Topics pane in the Amazon QuickSight application and opening a topic. The ID is in the URL for the topic that you open.

If you donât specify an initial topic or you specify a legacy topic, a list of all shared new reader experience topics is shown in the Generative Q&A experience for your readers. When you select an initial new reader experience topic, you can specify whether or not readers are allowed to select other new reader experience topics from the available ones in the list.

JSON Syntax:

```
{
  "Dashboard": {
    "InitialDashboardId": "string",
    "FeatureConfigurations": {
      "StatePersistence": {
        "Enabled": true|false
      },
      "SharedView": {
        "Enabled": true|false
      },
      "Bookmarks": {
        "Enabled": true|false
      },
      "AmazonQInQuickSight": {
        "ExecutiveSummary": {
          "Enabled": true|false
        }
      },
      "Schedules": {
        "Enabled": true|false
      },
      "RecentSnapshots": {
        "Enabled": true|false
      },
      "ThresholdAlerts": {
        "Enabled": true|false
      }
    }
  },
  "QuickSightConsole": {
    "InitialPath": "string",
    "FeatureConfigurations": {
      "StatePersistence": {
        "Enabled": true|false
      },
      "SharedView": {
        "Enabled": true|false
      },
      "AmazonQInQuickSight": {
        "DataQnA": {
          "Enabled": true|false
        },
        "GenerativeAuthoring": {
          "Enabled": true|false
        },
        "ExecutiveSummary": {
          "Enabled": true|false
        },
        "DataStories": {
          "Enabled": true|false
        }
      },
      "Schedules": {
        "Enabled": true|false
      },
      "RecentSnapshots": {
        "Enabled": true|false
      },
      "ThresholdAlerts": {
        "Enabled": true|false
      }
    }
  },
  "QSearchBar": {
    "InitialTopicId": "string"
  },
  "DashboardVisual": {
    "InitialDashboardVisualId": {
      "DashboardId": "string",
      "SheetId": "string",
      "VisualId": "string"
    }
  },
  "GenerativeQnA": {
    "InitialTopicId": "string"
  }
}
```

`--allowed-domains` (list)

The domains that you want to add to the allow list for access to the generated URL that is then embedded. This optional parameter overrides the static domains that are configured in the Manage QuickSight menu in the Amazon QuickSight console. Instead, it allows only the domains that you include in this parameter. You can list up to three domains or subdomains in each API call.

To include all subdomains under a specific domain to the allow list, use `*` . For example, `https://*.sapp.amazon.com` includes all subdomains under `https://sapp.amazon.com` .

(string)

Syntax:

```
"string" "string" ...
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

EmbedUrl -> (string)

The embed URL for the Amazon QuickSight dashboard, visual, Q search bar, Generative Q&A experience, or console.

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.