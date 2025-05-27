# gcloud dataplex datascans update data-quality  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality)*

**NAME**

: **gcloud dataplex datascans update data-quality - update a Dataplex data quality scan job**

**SYNOPSIS**

: **`gcloud dataplex datascans update data-quality` (`[DATASCAN](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#DATASCAN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--location)`=`LOCATION`) [`[--data-quality-spec-file](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--data-quality-spec-file)`=`DATA_QUALITY_SPEC_FILE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--validate-only)`] [`[--on-demand](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--on-demand)`=`ON_DEMAND`     | `[--schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#--schedule)`=`SCHEDULE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Represents a user-visible job which provides the insights for the related data
source and generates queries based on the rules and runs against the data to get
data quality check results.

**EXAMPLES**

: To update description of a data quality scan `data-quality-datascan`
in project `test-project` located in `us-central1`, run:

```
gcloud dataplex datascans update data-quality data-quality-datascan --project=test-project --location=us-central1 --description="Description is updated."
```

**POSITIONAL ARGUMENTS**

: **Datascan resource - Arguments and flags that define the Dataplex datascan you
want to update a data quality scan for. The arguments in this group can be used
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

**FLAGS**

: **--data-quality-spec-file**:
path to the JSON/YAML file containing the spec for the data quality scan. The
json representation reference: [https://cloud.google.com/dataplex/docs/reference/rest/v1/DataQualitySpec](https://cloud.google.com/dataplex/docs/reference/rest/v1/DataQualitySpec)

**--description**:
Description of the data quality scan

**--display-name**:
Display name of the data quality scan

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--async**

**--on-demand**

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
gcloud alpha dataplex datascans update data-quality
```