# generate-embed-url-for-anonymous-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/generate-embed-url-for-anonymous-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/generate-embed-url-for-anonymous-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# generate-embed-url-for-anonymous-user

## Description

Generates an embed URL that you can use to embed an Amazon QuickSight dashboard or visual in your website, without having to register any reader users. Before you use this action, make sure that you have configured the dashboards and permissions.

The following rules apply to the generated URL:

- It contains a temporary bearer token. It is valid for 5 minutes after it is generated. Once redeemed within this period, it cannot be re-used again.
- The URL validity period should not be confused with the actual session lifetime that can be customized using the `` [SessionLifetimeInMinutes](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForAnonymousUser.html#QS-GenerateEmbedUrlForAnonymousUser-request-SessionLifetimeInMinutes) `` parameter. The resulting user session is valid for 15 minutes (minimum) to 10 hours (maximum). The default session duration is 10 hours.
- You are charged only when the URL is used or there is interaction with Amazon QuickSight.

For more information, see [Embedded Analytics](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html) in the *Amazon QuickSight User Guide* .

For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon QuickSight Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/GenerateEmbedUrlForAnonymousUser)

## Synopsis

```
generate-embed-url-for-anonymous-user
--aws-account-id <value>
[--session-lifetime-in-minutes <value>]
--namespace <value>
[--session-tags <value>]
--authorized-resource-arns <value>
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

`--namespace` (string)

The Amazon QuickSight namespace that the anonymous user virtually belongs to. If you are not using an Amazon QuickSight custom namespace, set this to `default` .

`--session-tags` (list)

The session tags used for row-level security. Before you use this parameter, make sure that you have configured the relevant datasets using the `DataSet$RowLevelPermissionTagConfiguration` parameter so that session tags can be used to provide row-level security.

These are not the tags used for the Amazon Web Services resource tagging feature. For more information, see [Using Row-Level Security (RLS) with Tags](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-rls-tags.html) in the *Amazon QuickSight User Guide* .

(structure)

The key-value pair used for the row-level security tags feature.

Key -> (string)

The key for the tag.

Value -> (string)

The value that you want to assign the tag.

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

`--authorized-resource-arns` (list)

The Amazon Resource Names (ARNs) for the Amazon QuickSight resources that the user is authorized to access during the lifetime of the session.

If you choose `Dashboard` embedding experience, pass the list of dashboard ARNs in the account that you want the user to be able to view.

If you want to make changes to the theme of your embedded content, pass a list of theme ARNs that the anonymous users need access to.

Currently, you can pass up to 25 theme ARNs in each API call.

(string)

Syntax:

```
"string" "string" ...
```

`--experience-configuration` (structure)

The configuration of the experience that you are embedding.

Dashboard -> (structure)

The type of embedding experience. In this case, Amazon QuickSight dashboards.

InitialDashboardId -> (string)

The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon QuickSight renders this dashboard.

The Amazon Resource Name (ARN) of this dashboard must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request will fail with `InvalidParameterValueException` .

EnabledFeatures -> (list)

A list of all enabled features of a specified anonymous dashboard.

(string)

DisabledFeatures -> (list)

A list of all disabled features of a specified anonymous dashboard.

(string)

FeatureConfigurations -> (structure)

The feature configuration for an embedded dashboard.

SharedView -> (structure)

The shared view settings of an embedded dashboard.

Enabled -> (boolean)

The shared view settings of an embedded dashboard.

DashboardVisual -> (structure)

The type of embedding experience. In this case, Amazon QuickSight visuals.

InitialDashboardVisualId -> (structure)

The visual ID for the visual that you want the user to see. This ID is included in the output URL. When the URL in response is accessed, Amazon QuickSight renders this visual.

The Amazon Resource Name (ARN) of the dashboard that the visual belongs to must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request will fail with `InvalidParameterValueException` .

DashboardId -> (string)

The ID of the dashboard that has the visual that you want to embed. The `DashboardId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visualâs on-visual menu of the Amazon QuickSight console. You can also get the `DashboardId` with a `ListDashboards` API operation.

SheetId -> (string)

The ID of the sheet that the has visual that you want to embed. The `SheetId` can be found in the `IDs for developers` section of the `Embed visual` pane of the visualâs on-visual menu of the Amazon QuickSight console.

VisualId -> (string)

The ID of the visual that you want to embed. The `VisualID` can be found in the `IDs for developers` section of the `Embed visual` pane of the visualâs on-visual menu of the Amazon QuickSight console.

QSearchBar -> (structure)

The Q search bar that you want to use for anonymous user embedding.

InitialTopicId -> (string)

The Amazon QuickSight Q topic ID of the legacy topic that you want the anonymous user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon QuickSight renders the Q search bar with this legacy topic pre-selected.

The Amazon Resource Name (ARN) of this Q legacy topic must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request fails with an `InvalidParameterValueException` error.

GenerativeQnA -> (structure)

The Generative Q&A experience that you want to use for anonymous user embedding.

InitialTopicId -> (string)

The Amazon QuickSight Q topic ID of the new reader experience topic that you want the anonymous user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon QuickSight renders the Generative Q&A experience with this new reader experience topic pre selected.

The Amazon Resource Name (ARN) of this Q new reader experience topic must be included in the `AuthorizedResourceArns` parameter. Otherwise, the request fails with an `InvalidParameterValueException` error.

JSON Syntax:

```
{
  "Dashboard": {
    "InitialDashboardId": "string",
    "EnabledFeatures": ["SHARED_VIEW", ...],
    "DisabledFeatures": ["SHARED_VIEW", ...],
    "FeatureConfigurations": {
      "SharedView": {
        "Enabled": true|false
      }
    }
  },
  "DashboardVisual": {
    "InitialDashboardVisualId": {
      "DashboardId": "string",
      "SheetId": "string",
      "VisualId": "string"
    }
  },
  "QSearchBar": {
    "InitialTopicId": "string"
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

The embed URL for the dashboard.

Status -> (integer)

The HTTP status of the request.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

AnonymousUserArn -> (string)

The Amazon Resource Name (ARN) to use for the anonymous Amazon QuickSight user.