# gcloud dataplex datascans update data-profile  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile)*

**NAME**

: **gcloud dataplex datascans update data-profile - update a Dataplex data profile scan job**

**SYNOPSIS**

: **`gcloud dataplex datascans update data-profile` (`[DATASCAN](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#DATASCAN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--labels)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--async)`     | `[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--validate-only)`] [`[--data-profile-spec-file](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--data-profile-spec-file)`=`DATA_PROFILE_SPEC_FILE`     | `[--exclude-field-names](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--exclude-field-names)`=`EXCLUDE_FIELD_NAMES` `[--include-field-names](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--include-field-names)`=`INCLUDE_FIELD_NAMES` `[--row-filter](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--row-filter)`=`ROW_FILTER` `[--sampling-percent](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--sampling-percent)`=`SAMPLING_PERCENT`] [`[--on-demand](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--on-demand)`=`ON_DEMAND`     | `[--schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#--schedule)`=`SCHEDULE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Represents a user-visible job which provides the insights for the related data
source about the structure, content and relationships (such as null percent,
cardinality, min/max/mean, etc).

**EXAMPLES**

: To update description of a data profile scan `data-profile-datascan`
in project `test-project` located in `us-central1`, run:

```
gcloud dataplex datascans update data-profile data-profile-datascan --project=test-project --location=us-central1 --description="Description is updated."
```

**POSITIONAL ARGUMENTS**

: **Datascan resource - Arguments and flags that define the Dataplex datascan you
want to update a data profile scan for. The arguments in this group can be used
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

: **--description**:
Description of the data profile scan

**--display-name**:
Display name of the data profile scan

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--async**

**--data-profile-spec-file**

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
gcloud alpha dataplex datascans update data-profile
```