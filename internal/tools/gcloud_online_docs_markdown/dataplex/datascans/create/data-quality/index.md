# gcloud dataplex datascans create data-quality  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality)*

**NAME**

: **gcloud dataplex datascans create data-quality - create a Dataplex data quality scan job**

**SYNOPSIS**

: **`gcloud dataplex datascans create data-quality` (`[DATASCAN](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#DATASCAN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--location)`=`LOCATION`) `[--data-quality-spec-file](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--data-quality-spec-file)`=`DATA_QUALITY_SPEC_FILE` (`[--data-source-entity](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--data-source-entity)`=`DATA_SOURCE_ENTITY`     | `[--data-source-resource](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--data-source-resource)`=`DATA_SOURCE_RESOURCE`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--validate-only)`] [`[--incremental-field](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--incremental-field)`=`INCREMENTAL_FIELD` `[--on-demand](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--on-demand)`=`ON_DEMAND`     | `[--schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#--schedule)`=`SCHEDULE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-quality#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Represents a user-visible job which provides the insights for the related data
source and generates queries based on the rules and runs against the data to get
data quality check results.

**EXAMPLES**

: To create a data quality scan `data-quality-datascan` in project
`test-project` located in `us-central1` on bigquery
resource table `test-table` in dataset `test-dataset` with
data spec file `data-quality-spec.json`, run:

```
gcloud dataplex datascans create data-quality data-quality-datascan --project=test-project --location=us-central1 --data-source-resource="//bigquery.googleapis.com/projects/test-project/datasets/test-dataset/tables/test-table" --data-quality-spec-file="data-quality-spec.json"
```

**POSITIONAL ARGUMENTS**

: **Datascan resource - Arguments and flags that define the Dataplex datascan you
want to create a data quality scan for. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `datascan` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATASCAN`**:
ID of the datascan or fully qualified identifier for the datascan.
To set the `dataScans` attribute:

- provide the argument `datascan` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `datascan` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**REQUIRED FLAGS**

: **--data-quality-spec-file**:
path to the JSON/YAML file containing the spec for the data quality scan. The
json representation reference: [https://cloud.google.com/dataplex/docs/reference/rest/v1/DataQualitySpec](https://cloud.google.com/dataplex/docs/reference/rest/v1/DataQualitySpec)

**--data-source-entity**

**OPTIONAL FLAGS**

: **--description**:
Description of the data quality scan.

**--display-name**:
Display name of the data quality scan.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--async**

**--incremental-field**

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

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex datascans create data-quality
```