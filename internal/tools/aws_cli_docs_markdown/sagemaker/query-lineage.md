# query-lineageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/query-lineage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/query-lineage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# query-lineage

## Description

Use this action to inspect your lineage and discover relationships between entities. For more information, see [Querying Lineage Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/querying-lineage-entities.html) in the *Amazon SageMaker Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/QueryLineage)

## Synopsis

```
query-lineage
[--start-arns <value>]
[--direction <value>]
[--include-edges | --no-include-edges]
[--filters <value>]
[--max-depth <value>]
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

`--start-arns` (list)

A list of resource Amazon Resource Name (ARN) that represent the starting point for your lineage query.

(string)

Syntax:

```
"string" "string" ...
```

`--direction` (string)

Associations between lineage entities have a direction. This parameter determines the direction from the StartArn(s) that the query traverses.

Possible values:

- `Both`
- `Ascendants`
- `Descendants`

`--include-edges` | `--no-include-edges` (boolean)

Setting this value to `True` retrieves not only the entities of interest but also the [Associations](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html) and lineage entities on the path. Set to `False` to only return lineage entities that match your query.

`--filters` (structure)

A set of filtering parameters that allow you to specify which entities should be returned.

- Properties - Key-value pairs to match on the lineage entitiesâ properties.
- LineageTypes - A set of lineage entity types to match on. For example: `TrialComponent` , `Artifact` , or `Context` .
- CreatedBefore - Filter entities created before this date.
- ModifiedBefore - Filter entities modified before this date.
- ModifiedAfter - Filter entities modified after this date.

Types -> (list)

Filter the lineage entities connected to the `StartArn` by type. For example: `DataSet` , `Model` , `Endpoint` , or `ModelDeployment` .

(string)

LineageTypes -> (list)

Filter the lineage entities connected to the `StartArn` (s) by the type of the lineage entity.

(string)

CreatedBefore -> (timestamp)

Filter the lineage entities connected to the `StartArn` (s) by created date.

CreatedAfter -> (timestamp)

Filter the lineage entities connected to the `StartArn` (s) after the create date.

ModifiedBefore -> (timestamp)

Filter the lineage entities connected to the `StartArn` (s) before the last modified date.

ModifiedAfter -> (timestamp)

Filter the lineage entities connected to the `StartArn` (s) after the last modified date.

Properties -> (map)

Filter the lineage entities connected to the `StartArn` (s) by a set if property key value pairs. If multiple pairs are provided, an entity is included in the results if it matches any of the provided pairs.

key -> (string)

value -> (string)

Shorthand Syntax:

```
Types=string,string,LineageTypes=string,string,CreatedBefore=timestamp,CreatedAfter=timestamp,ModifiedBefore=timestamp,ModifiedAfter=timestamp,Properties={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "Types": ["string", ...],
  "LineageTypes": ["TrialComponent"|"Artifact"|"Context"|"Action", ...],
  "CreatedBefore": timestamp,
  "CreatedAfter": timestamp,
  "ModifiedBefore": timestamp,
  "ModifiedAfter": timestamp,
  "Properties": {"string": "string"
    ...}
}
```

`--max-depth` (integer)

The maximum depth in lineage relationships from the `StartArns` that are traversed. Depth is a measure of the number of `Associations` from the `StartArn` entity to the matched results.

`--max-results` (integer)

Limits the number of vertices in the results. Use the `NextToken` in a response to to retrieve the next page of results.

`--next-token` (string)

Limits the number of vertices in the request. Use the `NextToken` in a response to to retrieve the next page of results.

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

Vertices -> (list)

A list of vertices connected to the start entity(ies) in the lineage graph.

(structure)

A lineage entity connected to the starting entity(ies).

Arn -> (string)

The Amazon Resource Name (ARN) of the lineage entity resource.

Type -> (string)

The type of the lineage entity resource. For example: `DataSet` , `Model` , `Endpoint` , etcâ¦

LineageType -> (string)

The type of resource of the lineage entity.

Edges -> (list)

A list of edges that connect vertices in the response.

(structure)

A directed edge connecting two lineage entities.

SourceArn -> (string)

The Amazon Resource Name (ARN) of the source lineage entity of the directed edge.

DestinationArn -> (string)

The Amazon Resource Name (ARN) of the destination lineage entity of the directed edge.

AssociationType -> (string)

The type of the Association(Edge) between the source and destination. For example `ContributedTo` , `Produced` , or `DerivedFrom` .

NextToken -> (string)

Limits the number of vertices in the response. Use the `NextToken` in a response to to retrieve the next page of results.