# describe-suggestersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-suggesters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/describe-suggesters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudsearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/index.html#cli-aws-cloudsearch) ]

# describe-suggesters

## Description

Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the `Deployed` option to `true` to show the active configuration and exclude pending changes. For more information, see [Getting Search Suggestions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html) in the *Amazon CloudSearch Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudsearch-2013-01-01/DescribeSuggesters)

## Synopsis

```
describe-suggesters
--domain-name <value>
[--suggester-names <value>]
[--deployed | --no-deployed]
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

`--domain-name` (string)

The name of the domain you want to describe.

`--suggester-names` (list)

The suggesters you want to describe.

(string)

Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).

Syntax:

```
"string" "string" ...
```

`--deployed` | `--no-deployed` (boolean)

Whether to display the deployed configuration (`true` ) or include any pending changes (`false` ). Defaults to `false` .

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

Suggesters -> (list)

The suggesters configured for the domain specified in the request.

(structure)

The value of a `Suggester` and its current status.

Options -> (structure)

Configuration information for a search suggester. Each suggester has a unique name and specifies the text field you want to use for suggestions. The following options can be configured for a suggester: `FuzzyMatching` , `SortExpression` .

SuggesterName -> (string)

Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore).

DocumentSuggesterOptions -> (structure)

Options for a search suggester.

SourceField -> (string)

The name of the index field you want to use for suggestions.

FuzzyMatching -> (string)

The level of fuzziness allowed when suggesting matches for a string: `none` , `low` , or `high` . With none, the specified string is treated as an exact prefix. With low, suggestions must differ from the specified string by no more than one character. With high, suggestions can differ by up to two characters. The default is none.

SortExpression -> (string)

An expression that computes a score for each suggestion to control how they are sorted. The scores are rounded to the nearest integer, with a floor of 0 and a ceiling of 2^31-1. A documentâs relevance score is not computed for suggestions, so sort expressions cannot reference the `_score` value. To sort suggestions using a numeric field or existing expression, simply specify the name of the field or expression. If no expression is configured for the suggester, the suggestions are sorted with the closest matches listed first.

Status -> (structure)

The status of domain configuration option.

CreationDate -> (timestamp)

A timestamp for when this option was created.

UpdateDate -> (timestamp)

A timestamp for when this option was last updated.

UpdateVersion -> (integer)

A unique integer that indicates when this option was last updated.

State -> (string)

The state of processing a change to an option. Possible values:

- `RequiresIndexDocuments` : the optionâs latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
- `Processing` : the optionâs latest value is in the process of being activated.
- `Active` : the optionâs latest value is completely deployed.
- `FailedToValidate` : the option value is not compatible with the domainâs data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.

PendingDeletion -> (boolean)

Indicates that the option will be deleted once processing is complete.