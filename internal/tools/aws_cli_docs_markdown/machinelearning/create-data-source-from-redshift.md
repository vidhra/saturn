# create-data-source-from-redshiftÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [machinelearning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/index.html#cli-aws-machinelearning) ]

# create-data-source-from-redshift

## Description

Creates a `DataSource` from a database hosted on an Amazon Redshift cluster. A `DataSource` references data that can be used to perform either `CreateMLModel` , `CreateEvaluation` , or `CreateBatchPrediction` operations.

`CreateDataSourceFromRedshift` is an asynchronous operation. In response to `CreateDataSourceFromRedshift` , Amazon Machine Learning (Amazon ML) immediately returns and sets the `DataSource` status to `PENDING` . After the `DataSource` is created and ready for use, Amazon ML sets the `Status` parameter to `COMPLETED` . `DataSource` in `COMPLETED` or `PENDING` states can be used to perform only `CreateMLModel` , `CreateEvaluation` , or `CreateBatchPrediction` operations.

If Amazon ML canât accept the input source, it sets the `Status` parameter to `FAILED` and includes an error message in the `Message` attribute of the `GetDataSource` operation response.

The observations should be contained in the database hosted on an Amazon Redshift cluster and should be specified by a `SelectSqlQuery` query. Amazon ML executes an `Unload` command in Amazon Redshift to transfer the result set of the `SelectSqlQuery` query to `S3StagingLocation` .

After the `DataSource` has been created, itâs ready for use in evaluations and batch predictions. If you plan to use the `DataSource` to train an `MLModel` , the `DataSource` also requires a recipe. A recipe describes how each input variable will be used in training an `MLModel` . Will the variable be included or excluded from training? Will the variable be manipulated; for example, will it be combined with another variable or will it be split apart into word combinations? The recipe provides answers to these questions.

You canât change an existing datasource, but you can copy and modify the settings from an existing Amazon Redshift datasource to create a new datasource. To do so, call `GetDataSource` for an existing datasource and copy the values to a `CreateDataSource` call. Change the settings that you want to change and make sure that all required fields have the appropriate values.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/CreateDataSourceFromRedshift)

## Synopsis

```
create-data-source-from-redshift
--data-source-id <value>
[--data-source-name <value>]
--data-spec <value>
--role-arn <value>
[--compute-statistics | --no-compute-statistics]
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

`--data-source-id` (string)

A user-supplied ID that uniquely identifies the `DataSource` .

`--data-source-name` (string)

A user-supplied name or description of the `DataSource` .

`--data-spec` (structure)

The data specification of an Amazon Redshift `DataSource` :

- DatabaseInformation -
- `DatabaseName` - The name of the Amazon Redshift database.
- `ClusterIdentifier` - The unique ID for the Amazon Redshift cluster.
- DatabaseCredentials - The AWS Identity and Access Management (IAM) credentials that are used to connect to the Amazon Redshift database.
- SelectSqlQuery - The query that is used to retrieve the observation data for the `Datasource` .
- S3StagingLocation - The Amazon Simple Storage Service (Amazon S3) location for staging Amazon Redshift data. The data retrieved from Amazon Redshift using the `SelectSqlQuery` query is stored in this location.
- DataSchemaUri - The Amazon S3 location of the `DataSchema` .
- DataSchema - A JSON string representing the schema. This is not required if `DataSchemaUri` is specified.
- DataRearrangement - A JSON string that represents the splitting and rearrangement requirements for the `DataSource` . Sample - `"{\"splitting\":{\"percentBegin\":10,\"percentEnd\":60}}"`

DatabaseInformation -> (structure)

Describes the `DatabaseName` and `ClusterIdentifier` for an Amazon Redshift `DataSource` .

DatabaseName -> (string)

The name of a database hosted on an Amazon Redshift cluster.

ClusterIdentifier -> (string)

The ID of an Amazon Redshift cluster.

SelectSqlQuery -> (string)

Describes the SQL Query to execute on an Amazon Redshift database for an Amazon Redshift `DataSource` .

DatabaseCredentials -> (structure)

Describes AWS Identity and Access Management (IAM) credentials that are used connect to the Amazon Redshift database.

Username -> (string)

A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the `RedshiftSelectSqlQuery` query. The username should be valid for an Amazon Redshift [USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html) .

Password -> (string)

A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster. The password should have sufficient permissions to execute a `RedshiftSelectSqlQuery` query. The password should be valid for an Amazon Redshift [USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html) .

S3StagingLocation -> (string)

Describes an Amazon S3 location to store the result set of the `SelectSqlQuery` query.

DataRearrangement -> (string)

A JSON string that represents the splitting and rearrangement processing to be applied to a `DataSource` . If the `DataRearrangement` parameter is not provided, all of the input data is used to create the `Datasource` .

There are multiple parameters that control what data is used to create a datasource:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html#id1)`percentBegin` **   Use `percentBegin` to indicate the beginning of the range of the data used to create the Datasource. If you do not include `percentBegin` and `percentEnd` , Amazon ML includes all of the data when creating the datasource.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html#id3)`percentEnd` **   Use `percentEnd` to indicate the end of the range of the data used to create the Datasource. If you do not include `percentBegin` and `percentEnd` , Amazon ML includes all of the data when creating the datasource.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html#id5)`complement` **   The `complement` parameter instructs Amazon ML to use the data that is not included in the range of `percentBegin` to `percentEnd` to create a datasource. The `complement` parameter is useful if you need to create complementary datasources for training and evaluation. To create a complementary datasource, use the same values for `percentBegin` and `percentEnd` , along with the `complement` parameter. For example, the following two datasources do not share any data, and can be used to train and evaluate a model. The first datasource has 25 percent of the data, and the second one has 75 percent of the data. Datasource for evaluation: `{"splitting":{"percentBegin":0, "percentEnd":25}}`   Datasource for training: `{"splitting":{"percentBegin":0, "percentEnd":25, "complement":"true"}}`
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/create-data-source-from-redshift.html#id7)`strategy` **   To change how Amazon ML splits the data for a datasource, use the `strategy` parameter. The default value for the `strategy` parameter is `sequential` , meaning that Amazon ML takes all of the data records between the `percentBegin` and `percentEnd` parameters for the datasource, in the order that the records appear in the input data. The following two `DataRearrangement` lines are examples of sequentially ordered training and evaluation datasources: Datasource for evaluation: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential"}}`   Datasource for training: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"sequential", "complement":"true"}}`   To randomly split the input data into the proportions indicated by the percentBegin and percentEnd parameters, set the `strategy` parameter to `random` and provide a string that is used as the seed value for the random data splitting (for example, you can use the S3 path to your data as the random seed string). If you choose the random split strategy, Amazon ML assigns each row of data a pseudo-random number between 0 and 100, and then selects the rows that have an assigned number between `percentBegin` and `percentEnd` . Pseudo-random numbers are assigned using both the input seed string value and the byte offset as a seed, so changing the data results in a different split. Any existing ordering is preserved. The random splitting strategy ensures that variables in the training and evaluation data are distributed similarly. It is useful in the cases where the input data may have an implicit sort order, which would otherwise result in training and evaluation datasources containing non-similar data records. The following two `DataRearrangement` lines are examples of non-sequentially ordered training and evaluation datasources: Datasource for evaluation: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv"}}`   Datasource for training: `{"splitting":{"percentBegin":70, "percentEnd":100, "strategy":"random", "randomSeed"="s3://my_s3_path/bucket/file.csv", "complement":"true"}}`

DataSchema -> (string)

A JSON string that represents the schema for an Amazon Redshift `DataSource` . The `DataSchema` defines the structure of the observation data in the data file(s) referenced in the `DataSource` .

A `DataSchema` is not required if you specify a `DataSchemaUri` .

Define your `DataSchema` as a series of key-value pairs. `attributes` and `excludedVariableNames` have an array of key-value pairs for their value. Use the following format to define your `DataSchema` .

{ âversionâ: â1.0â,

ârecordAnnotationFieldNameâ: âF1â,

ârecordWeightFieldNameâ: âF2â,

âtargetFieldNameâ: âF3â,

âdataFormatâ: âCSVâ,

âdataFileContainsHeaderâ: true,

âattributesâ: [

{ âfieldNameâ: âF1â, âfieldTypeâ: âTEXTâ }, { âfieldNameâ: âF2â, âfieldTypeâ: âNUMERICâ }, { âfieldNameâ: âF3â, âfieldTypeâ: âCATEGORICALâ }, { âfieldNameâ: âF4â, âfieldTypeâ: âNUMERICâ }, { âfieldNameâ: âF5â, âfieldTypeâ: âCATEGORICALâ }, { âfieldNameâ: âF6â, âfieldTypeâ: âTEXTâ }, { âfieldNameâ: âF7â, âfieldTypeâ: âWEIGHTED_INT_SEQUENCEâ }, { âfieldNameâ: âF8â, âfieldTypeâ: âWEIGHTED_STRING_SEQUENCEâ } ],

âexcludedVariableNamesâ: [ âF6â ] }

DataSchemaUri -> (string)

Describes the schema location for an Amazon Redshift `DataSource` .

Shorthand Syntax:

```
DatabaseInformation={DatabaseName=string,ClusterIdentifier=string},SelectSqlQuery=string,DatabaseCredentials={Username=string,Password=string},S3StagingLocation=string,DataRearrangement=string,DataSchema=string,DataSchemaUri=string
```

JSON Syntax:

```
{
  "DatabaseInformation": {
    "DatabaseName": "string",
    "ClusterIdentifier": "string"
  },
  "SelectSqlQuery": "string",
  "DatabaseCredentials": {
    "Username": "string",
    "Password": "string"
  },
  "S3StagingLocation": "string",
  "DataRearrangement": "string",
  "DataSchema": "string",
  "DataSchemaUri": "string"
}
```

`--role-arn` (string)

A fully specified role Amazon Resource Name (ARN). Amazon ML assumes the role on behalf of the user to create the following:

- A security group to allow Amazon ML to execute the `SelectSqlQuery` query on an Amazon Redshift cluster
- An Amazon S3 bucket policy to grant Amazon ML read/write permissions on the `S3StagingLocation`

`--compute-statistics` | `--no-compute-statistics` (boolean)

The compute statistics for a `DataSource` . The statistics are generated from the observation data referenced by a `DataSource` . Amazon ML uses the statistics internally during `MLModel` training. This parameter must be set to `true` if the `DataSource` needs to be used for `MLModel` training.

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

DataSourceId -> (string)

A user-supplied ID that uniquely identifies the datasource. This value should be identical to the value of the `DataSourceID` in the request.