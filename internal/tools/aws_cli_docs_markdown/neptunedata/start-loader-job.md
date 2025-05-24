# start-loader-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptunedata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/index.html#cli-aws-neptunedata) ]

# start-loader-job

## Description

Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into a Neptune DB instance. See [Using the Amazon Neptune Bulk Loader to Ingest Data](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load.html) .

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:StartLoaderJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startloaderjob) IAM action in that cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptunedata-2023-08-01/StartLoaderJob)

## Synopsis

```
start-loader-job
--source <value>
--format <value>
--s3-bucket-region <value>
--iam-role-arn <value>
[--mode <value>]
[--fail-on-error | --no-fail-on-error]
[--parallelism <value>]
[--parser-configuration <value>]
[--update-single-cardinality-properties | --no-update-single-cardinality-properties]
[--queue-request | --no-queue-request]
[--dependencies <value>]
[--user-provided-edge-ids | --no-user-provided-edge-ids]
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

`--source` (string)

The `source` parameter accepts an S3 URI that identifies a single file, multiple files, a folder, or multiple folders. Neptune loads every data file in any folder that is specified.

The URI can be in any of the following formats.

- `s3://(bucket_name)/(object-key-name)`
- `https://s3.amazonaws.com/(bucket_name)/(object-key-name)`
- `https://s3.us-east-1.amazonaws.com/(bucket_name)/(object-key-name)`

The `object-key-name` element of the URI is equivalent to the [prefix](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html#API_ListObjects_RequestParameters) parameter in an S3 [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) API call. It identifies all the objects in the specified S3 bucket whose names begin with that prefix. That can be a single file or folder, or multiple files and/or folders.

The specified folder or folders can contain multiple vertex files and multiple edge files.

`--format` (string)

The format of the data. For more information about data formats for the Neptune `Loader` command, see [Load Data Formats](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html) .

**Allowed values**

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id1)`csv` ** for the [Gremlin CSV data format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id3)`opencypher` ** for the [openCypher CSV data format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html) .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id5)`ntriples` ** for the [N-Triples RDF data format](https://www.w3.org/TR/n-triples/) .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id7)`nquads` ** for the [N-Quads RDF data format](https://www.w3.org/TR/n-quads/) .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id9)`rdfxml` ** for the [RDFXML RDF data format](https://www.w3.org/TR/rdf-syntax-grammar/) .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id11)`turtle` ** for the [Turtle RDF data format](https://www.w3.org/TR/turtle/) .

Possible values:

- `csv`
- `opencypher`
- `ntriples`
- `nquads`
- `rdfxml`
- `turtle`

`--s3-bucket-region` (string)

The Amazon region of the S3 bucket. This must match the Amazon Region of the DB cluster.

Possible values:

- `us-east-1`
- `us-east-2`
- `us-west-1`
- `us-west-2`
- `ca-central-1`
- `sa-east-1`
- `eu-north-1`
- `eu-west-1`
- `eu-west-2`
- `eu-west-3`
- `eu-central-1`
- `me-south-1`
- `af-south-1`
- `ap-east-1`
- `ap-northeast-1`
- `ap-northeast-2`
- `ap-southeast-1`
- `ap-southeast-2`
- `ap-south-1`
- `cn-north-1`
- `cn-northwest-1`
- `us-gov-west-1`
- `us-gov-east-1`

`--iam-role-arn` (string)

The Amazon Resource Name (ARN) for an IAM role to be assumed by the Neptune DB instance for access to the S3 bucket. The IAM role ARN provided here should be attached to the DB cluster (see [Adding the IAM Role to an Amazon Neptune Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM-add-role-cluster.html) .

`--mode` (string)

The load job mode.

*Allowed values* : `RESUME` , `NEW` , `AUTO` .

*Default value* : `AUTO` .

- `RESUME` â In RESUME mode, the loader looks for a previous load from this source, and if it finds one, resumes that load job. If no previous load job is found, the loader stops. The loader avoids reloading files that were successfully loaded in a previous job. It only tries to process failed files. If you dropped previously loaded data from your Neptune cluster, that data is not reloaded in this mode. If a previous load job loaded all files from the same source successfully, nothing is reloaded, and the loader returns success.
- `NEW` â In NEW mode, the creates a new load request regardless of any previous loads. You can use this mode to reload all the data from a source after dropping previously loaded data from your Neptune cluster, or to load new data available at the same source.
- `AUTO` â In AUTO mode, the loader looks for a previous load job from the same source, and if it finds one, resumes that job, just as in `RESUME` mode. If the loader doesnât find a previous load job from the same source, it loads all data from the source, just as in `NEW` mode.

Possible values:

- `RESUME`
- `NEW`
- `AUTO`

`--fail-on-error` | `--no-fail-on-error` (boolean)

** `failOnError` ** â A flag to toggle a complete stop on an error.

*Allowed values* : `"TRUE"` , `"FALSE"` .

*Default value* : `"TRUE"` .

When this parameter is set to `"FALSE"` , the loader tries to load all the data in the location specified, skipping any entries with errors.

When this parameter is set to `"TRUE"` , the loader stops as soon as it encounters an error. Data loaded up to that point persists.

`--parallelism` (string)

The optional `parallelism` parameter can be set to reduce the number of threads used by the bulk load process.

*Allowed values* :

- `LOW` â The number of threads used is the number of available vCPUs divided by 8.
- `MEDIUM` â The number of threads used is the number of available vCPUs divided by 2.
- `HIGH` â The number of threads used is the same as the number of available vCPUs.
- `OVERSUBSCRIBE` â The number of threads used is the number of available vCPUs multiplied by 2. If this value is used, the bulk loader takes up all available resources. This does not mean, however, that the `OVERSUBSCRIBE` setting results in 100% CPU utilization. Because the load operation is I/O bound, the highest CPU utilization to expect is in the 60% to 70% range.

*Default value* : `HIGH`

The `parallelism` setting can sometimes result in a deadlock between threads when loading openCypher data. When this happens, Neptune returns the `LOAD_DATA_DEADLOCK` error. You can generally fix the issue by setting `parallelism` to a lower setting and retrying the load command.

Possible values:

- `LOW`
- `MEDIUM`
- `HIGH`
- `OVERSUBSCRIBE`

`--parser-configuration` (map)

** `parserConfiguration` ** â An optional object with additional parser configuration values. Each of the child parameters is also optional:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id13)`namedGraphUri` ** â The default graph for all RDF formats when no graph is specified (for non-quads formats and NQUAD entries with no graph). The default is `https://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph` .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id15)`baseUri` ** â The base URI for RDF/XML and Turtle formats. The default is `https://aws.amazon.com/neptune/default` .
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/start-loader-job.html#id17)`allowEmptyStrings` ** â Gremlin users need to be able to pass empty string values(ââ) as node and edge properties when loading CSV data. If `allowEmptyStrings` is set to `false` (the default), such empty strings are treated as nulls and are not loaded. If `allowEmptyStrings` is set to `true` , the loader treats empty strings as valid property values and loads them accordingly.

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

`--update-single-cardinality-properties` | `--no-update-single-cardinality-properties` (boolean)

`updateSingleCardinalityProperties` is an optional parameter that controls how the bulk loader treats a new value for single-cardinality vertex or edge properties. This is not supported for loading openCypher data.

*Allowed values* : `"TRUE"` , `"FALSE"` .

*Default value* : `"FALSE"` .

By default, or when `updateSingleCardinalityProperties` is explicitly set to `"FALSE"` , the loader treats a new value as an error, because it violates single cardinality.

When `updateSingleCardinalityProperties` is set to `"TRUE"` , on the other hand, the bulk loader replaces the existing value with the new one. If multiple edge or single-cardinality vertex property values are provided in the source file(s) being loaded, the final value at the end of the bulk load could be any one of those new values. The loader only guarantees that the existing value has been replaced by one of the new ones.

`--queue-request` | `--no-queue-request` (boolean)

This is an optional flag parameter that indicates whether the load request can be queued up or not.

You donât have to wait for one load job to complete before issuing the next one, because Neptune can queue up as many as 64 jobs at a time, provided that their `queueRequest` parameters are all set to `"TRUE"` . The queue order of the jobs will be first-in-first-out (FIFO).

If the `queueRequest` parameter is omitted or set to `"FALSE"` , the load request will fail if another load job is already running.

*Allowed values* : `"TRUE"` , `"FALSE"` .

*Default value* : `"FALSE"` .

`--dependencies` (list)

This is an optional parameter that can make a queued load request contingent on the successful completion of one or more previous jobs in the queue.

Neptune can queue up as many as 64 load requests at a time, if their `queueRequest` parameters are set to `"TRUE"` . The `dependencies` parameter lets you make execution of such a queued request dependent on the successful completion of one or more specified previous requests in the queue.

For example, if load `Job-A` and `Job-B` are independent of each other, but load `Job-C` needs `Job-A` and `Job-B` to be finished before it begins, proceed as follows:

- Submit `load-job-A` and `load-job-B` one after another in any order, and save their load-ids.
- Submit `load-job-C` with the load-ids of the two jobs in its `dependencies` field:

Because of the `dependencies` parameter, the bulk loader will not start `Job-C` until `Job-A` and `Job-B` have completed successfully. If either one of them fails, Job-C will not be executed, and its status will be set to `LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED` .

You can set up multiple levels of dependency in this way, so that the failure of one job will cause all requests that are directly or indirectly dependent on it to be cancelled.

(string)

Syntax:

```
"string" "string" ...
```

`--user-provided-edge-ids` | `--no-user-provided-edge-ids` (boolean)

This parameter is required only when loading openCypher data that contains relationship IDs. It must be included and set to `True` when openCypher relationship IDs are explicitly provided in the load data (recommended).

When `userProvidedEdgeIds` is absent or set to `True` , an `:ID` column must be present in every relationship file in the load.

When `userProvidedEdgeIds` is present and set to `False` , relationship files in the load **must not** contain an `:ID` column. Instead, the Neptune loader automatically generates an ID for each relationship.

Itâs useful to provide relationship IDs explicitly so that the loader can resume loading after error in the CSV data have been fixed, without having to reload any relationships that have already been loaded. If relationship IDs have not been explicitly assigned, the loader cannot resume a failed load if any relationship file has had to be corrected, and must instead reload all the relationships.

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

status -> (string)

The HTTP return code indicating the status of the load job.

payload -> (map)

Contains a `loadId` name-value pair that provides an identifier for the load operation.

key -> (string)

value -> (string)