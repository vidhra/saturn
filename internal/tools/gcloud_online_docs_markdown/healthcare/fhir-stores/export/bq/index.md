# gcloud healthcare fhir-stores export bq  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq)*

**NAME**

: **gcloud healthcare fhir-stores export bq - export Cloud Healthcare API FHIR resources to BigQuery**

**SYNOPSIS**

: **`gcloud healthcare fhir-stores export bq` (`[FHIR_STORE](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#FHIR_STORE)` : `[--dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--dataset)`=`DATASET` `[--location](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--location)`=`LOCATION`) `[--bq-dataset](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--bq-dataset)`=`BQ_DATASET` `[--schema-type](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--schema-type)`=`SCHEMA_TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--async)`] [`[--recursive-depth](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--recursive-depth)`=`RECURSIVE_DEPTH`] [`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--resource-type)`=`RESOURCE_TYPE`] [`[--since](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--since)`=`SINCE`] [`[--write-disposition](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#--write-disposition)`=`WRITE_DISPOSITION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/bq#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export Cloud Healthcare API FHIR resources to BigQuery.

**EXAMPLES**

: To export the fhir-store 'test-fhir-store' to the BigQuery dataset 'bqdataset',
run:

```
gcloud healthcare fhir-stores export bq test-fhir-store --bq-dataset=bq://my-project.bqdataset --dataset=test-dataset
```

To perform the same export, but with the 'ANALYTICS' schema and the recursive
structure depth of 3, run:

```
gcloud healthcare fhir-stores export bq test-fhir-store --bq-dataset=bq://my-project.bqdataset --dataset=test-dataset --schema-type=analytics --recursive-depth=3
```

**POSITIONAL ARGUMENTS**

: **FhirStore resource - Cloud Healthcare API FHIR store to export resources from.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`FHIR_STORE`**:
ID of the fhirStore or fully qualified identifier for the fhirStore.
To set the `fhir_store` attribute:

- provide the argument `fhir_store` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--dataset**:
Cloud Healthcare dataset.
To set the `dataset` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--dataset` on the command line.

**--location**:
Google Cloud location.
To set the `location` attribute:

- provide the argument `fhir_store` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `healthcare/location`.**

**REQUIRED FLAGS**

: **--bq-dataset**:
BigQuery dataset that houses the BigQuery tables.

**--schema-type**:
Specifies the output schema type. `SCHEMA_TYPE` must be
one of:

**`analytics`**:
Analytics schema defined by the FHIR community. See [https://github.com/rbrush/sql-on-fhir/blob/master/sql-on-fhir.md](https://github.com/rbrush/sql-on-fhir/blob/master/sql-on-fhir.md).

**`analytics_v2`**:
Analytics V2, similar to Analytics schema type, with added support for
extensions with one or more occurrences and contained resources to be
represented in stringified JSON.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--recursive-depth**:
The depth for all recursive structures in the output analytics schema. For
example, concept in the CodeSystem resource is a recursive structure; when the
depth is 2, the CodeSystem table will have a column called concept.concept but
not concept.concept.concept. If not specified or set to 0, the server will use
the default value 2.

**--resource-type**:
String of comma-delimited FHIR resource types. If provided, only resources of
the specified resource type(s) are exported.

**--since**:
If provided, only resources updated after this time are exported. The time uses
the format YYYY-MM-DDThh:mm:ss.sss+zz:zz. For example,
`2015-02-07T13:28:17.239+02:00` or `2017-01-01T00:00:00Z`.
The time must be specified to the second and include a time zone.

**--write-disposition**:
Determines whether existing tables in the destination dataset are overwritten or
appended to. `WRITE_DISPOSITION` must be one of:

**`write-append`**:
Append data to the existing tables.

**`write-empty`**:
Only export data if the destination tables are empty.

**`write-truncate`**:
Erase all existing data in the tables before writing the instances.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**API REFERENCE**

: This command uses the `healthcare/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/healthcare](https://cloud.google.com/healthcare)

**NOTES**

: These variants are also available:

```
gcloud alpha healthcare fhir-stores export bq
```

```
gcloud beta healthcare fhir-stores export bq
```