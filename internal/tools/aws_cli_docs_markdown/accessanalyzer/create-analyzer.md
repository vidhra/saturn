# create-analyzerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-analyzer.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-analyzer.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [accessanalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html#cli-aws-accessanalyzer) ]

# create-analyzer

## Description

Creates an analyzer for your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/accessanalyzer-2019-11-01/CreateAnalyzer)

## Synopsis

```
create-analyzer
--analyzer-name <value>
--type <value>
[--archive-rules <value>]
[--tags <value>]
[--client-token <value>]
[--configuration <value>]
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

`--analyzer-name` (string)

The name of the analyzer to create.

`--type` (string)

The type of analyzer to create. Only `ACCOUNT` , `ORGANIZATION` , `ACCOUNT_UNUSED_ACCESS` , and `ORGANIZATION_UNUSED_ACCESS` analyzers are supported. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.

Possible values:

- `ACCOUNT`
- `ORGANIZATION`
- `ACCOUNT_UNUSED_ACCESS`
- `ORGANIZATION_UNUSED_ACCESS`

`--archive-rules` (list)

Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.

(structure)

An criterion statement in an archive rule. Each archive rule may have multiple criteria.

ruleName -> (string)

The name of the rule.

filter -> (map)

The condition and values for a criterion.

key -> (string)

value -> (structure)

The criteria to use in the filter that defines the archive rule. For more information on available filter keys, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) .

eq -> (list)

An âequalsâ operator to match for the filter used to create the rule.

(string)

neq -> (list)

A ânot equalsâ operator to match for the filter used to create the rule.

(string)

contains -> (list)

A âcontainsâ operator to match for the filter used to create the rule.

(string)

exists -> (boolean)

An âexistsâ operator to match for the filter used to create the rule.

Shorthand Syntax:

```
ruleName=string,filter={KeyName1={eq=[string,string],neq=[string,string],contains=[string,string],exists=boolean},KeyName2={eq=[string,string],neq=[string,string],contains=[string,string],exists=boolean}} ...
```

JSON Syntax:

```
[
  {
    "ruleName": "string",
    "filter": {"string": {
          "eq": ["string", ...],
          "neq": ["string", ...],
          "contains": ["string", ...],
          "exists": true|false
        }
      ...}
  }
  ...
]
```

`--tags` (map)

An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, `_` , `.` , `/` , `=` , `+` , and `-` .

For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:` .

For the tag value, you can specify a value that is 0 to 256 characters in length.

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

`--client-token` (string)

A client token.

`--configuration` (tagged union structure)

Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `unusedAccess`.

unusedAccess -> (structure)

Specifies the configuration of an unused access analyzer for an Amazon Web Services organization or account.

unusedAccessAge -> (integer)

The specified access age in days for which to generate findings for unused access. For example, if you specify 90 days, the analyzer will generate findings for IAM entities within the accounts of the selected organization for any access that hasnât been used in 90 or more days since the analyzerâs last scan. You can choose a value between 1 and 365 days.

analysisRule -> (structure)

Contains information about analysis rules for the analyzer. Analysis rules determine which entities will generate findings based on the criteria you define when you create the rule.

exclusions -> (list)

A list of rules for the analyzer containing criteria to exclude from analysis. Entities that meet the rule criteria will not generate findings.

(structure)

The criteria for an analysis rule for an analyzer. The criteria determine which entities will generate findings.

accountIds -> (list)

A list of Amazon Web Services account IDs to apply to the analysis rule criteria. The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.

(string)

resourceTags -> (list)

An array of key-value pairs to match for your resources. You can use the set of Unicode letters, digits, whitespace, `_` , `.` , `/` , `=` , `+` , and `-` .

For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with `aws:` .

For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.

(map)

key -> (string)

value -> (string)

JSON Syntax:

```
{
  "unusedAccess": {
    "unusedAccessAge": integer,
    "analysisRule": {
      "exclusions": [
        {
          "accountIds": ["string", ...],
          "resourceTags": [
            {"string": "string"
              ...}
            ...
          ]
        }
        ...
      ]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create an analyzer**

The following `create-analyzer` example creates an analyzer in your AWS account.

```
aws accessanalyzer create-analyzer \
    --analyzer-name example \
    --type ACCOUNT
```

Output:

```
{
    "arn": "arn:aws:access-analyzer:us-east-2:111122223333:analyzer/example"
}
```

For more information, see [Getting started with AWS Identity and Access Management Access Analyzer findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html) in the *AWS IAM User Guide*.

## Output

arn -> (string)

The ARN of the analyzer that was created by the request.