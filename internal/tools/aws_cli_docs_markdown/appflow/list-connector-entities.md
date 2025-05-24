# list-connector-entitiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-connector-entities.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/list-connector-entities.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# list-connector-entities

## Description

Returns the list of available connector entities supported by Amazon AppFlow. For example, you can query Salesforce for *Account* and *Opportunity* entities, or query ServiceNow for the *Incident* entity.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/ListConnectorEntities)

## Synopsis

```
list-connector-entities
[--connector-profile-name <value>]
[--connector-type <value>]
[--entities-path <value>]
[--api-version <value>]
[--max-results <value>]
[--next-token <value>]
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

`--connector-profile-name` (string)

The name of the connector profile. The name is unique for each `ConnectorProfile` in the Amazon Web Services account, and is used to query the downstream connector.

`--connector-type` (string)

The type of connector, such as Salesforce, Amplitude, and so on.

Possible values:

- `Salesforce`
- `Singular`
- `Slack`
- `Redshift`
- `S3`
- `Marketo`
- `Googleanalytics`
- `Zendesk`
- `Servicenow`
- `Datadog`
- `Trendmicro`
- `Snowflake`
- `Dynatrace`
- `Infornexus`
- `Amplitude`
- `Veeva`
- `EventBridge`
- `LookoutMetrics`
- `Upsolver`
- `Honeycode`
- `CustomerProfiles`
- `SAPOData`
- `CustomConnector`
- `Pardot`

`--entities-path` (string)

This optional parameter is specific to connector implementation. Some connectors support multiple levels or categories of entities. You can find out the list of roots for such providers by sending a request without the `entitiesPath` parameter. If the connector supports entities at different roots, this initial request returns the list of roots. Otherwise, this request returns all entities supported by the provider.

`--api-version` (string)

The version of the API thatâs used by the connector.

`--max-results` (integer)

The maximum number of items that the operation returns in the response.

`--next-token` (string)

A token that was provided by your prior `ListConnectorEntities` operation if the response was too big for the page size. You specify this token to get the next page of results in paginated response.

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

connectorEntityMap -> (map)

The response of `ListConnectorEntities` lists entities grouped by category. This mapâs key represents the group name, and its value contains the list of entities belonging to that group.

key -> (string)

value -> (list)

(structure)

The high-level entity that can be queried in Amazon AppFlow. For example, a Salesforce entity might be an *Account* or *Opportunity* , whereas a ServiceNow entity might be an *Incident* .

name -> (string)

The name of the connector entity.

label -> (string)

The label applied to the connector entity.

hasNestedEntities -> (boolean)

Specifies whether the connector entity is a parent or a category and has more entities nested underneath it. If another call is made with `entitiesPath = "the_current_entity_name_with_hasNestedEntities_true"` , then it returns the nested entities underneath it. This provides a way to retrieve all supported entities in a recursive fashion.

nextToken -> (string)

A token that you specify in your next `ListConnectorEntities` operation to get the next page of results in paginated response. The `ListConnectorEntities` operation provides this token if the response is too big for the page size.