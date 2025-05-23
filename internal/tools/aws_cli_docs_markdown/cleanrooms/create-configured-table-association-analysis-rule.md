# create-configured-table-association-analysis-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/create-configured-table-association-analysis-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/create-configured-table-association-analysis-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# create-configured-table-association-analysis-rule

## Description

Creates a new analysis rule for an associated configured table.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/CreateConfiguredTableAssociationAnalysisRule)

## Synopsis

```
create-configured-table-association-analysis-rule
--membership-identifier <value>
--configured-table-association-identifier <value>
--analysis-rule-type <value>
--analysis-rule-policy <value>
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

`--membership-identifier` (string)

A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.

`--configured-table-association-identifier` (string)

The unique ID for the configured table association. Currently accepts the configured table association ID.

`--analysis-rule-type` (string)

The type of analysis rule.

Possible values:

- `AGGREGATION`
- `LIST`
- `CUSTOM`

`--analysis-rule-policy` (tagged union structure)

The analysis rule policy that was created for the configured table association.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

The policy for the configured table association analysis rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`.

list -> (structure)

Analysis rule type that enables only list queries on a configured table.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

(string)

aggregation -> (structure)

Analysis rule type that enables only aggregation queries on a configured table.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

The `allowedAdditionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList` ) and the custom analysis rule (`AnalysisRuleCustom` ).

(string)

custom -> (structure)

Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

(string)

JSON Syntax:

```
{
  "v1": {
    "list": {
      "allowedResultReceivers": ["string", ...],
      "allowedAdditionalAnalyses": ["string", ...]
    },
    "aggregation": {
      "allowedResultReceivers": ["string", ...],
      "allowedAdditionalAnalyses": ["string", ...]
    },
    "custom": {
      "allowedResultReceivers": ["string", ...],
      "allowedAdditionalAnalyses": ["string", ...]
    }
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

analysisRule -> (structure)

The analysis rule for the conï¬gured table association. In the console, the `ConfiguredTableAssociationAnalysisRule` is referred to as the *collaboration analysis rule* .

membershipIdentifier -> (string)

The membership identifier for the configured table association analysis rule.

configuredTableAssociationId -> (string)

The unique identifier for the configured table association.

configuredTableAssociationArn -> (string)

The Amazon Resource Name (ARN) of the configured table association.

policy -> (tagged union structure)

The policy of the configured table association analysis rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `v1`.

v1 -> (tagged union structure)

The policy for the configured table association analysis rule.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `list`, `aggregation`, `custom`.

list -> (structure)

Analysis rule type that enables only list queries on a configured table.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

(string)

aggregation -> (structure)

Analysis rule type that enables only aggregation queries on a configured table.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

The `allowedAdditionalAnalyses` parameter is currently supported for the list analysis rule (`AnalysisRuleList` ) and the custom analysis rule (`AnalysisRuleCustom` ).

(string)

custom -> (structure)

Analysis rule type that enables the table owner to approve custom SQL queries on their configured tables. It supports differential privacy.

allowedResultReceivers -> (list)

The list of collaboration members who are allowed to receive results of queries run with this configured table.

(string)

allowedAdditionalAnalyses -> (list)

The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.

(string)

type -> (string)

The type of the configured table association analysis rule.

createTime -> (timestamp)

The creation time of the configured table association analysis rule.

updateTime -> (timestamp)

The update time of the configured table association analysis rule.