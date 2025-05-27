# gcloud dataplex assets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create)*

**NAME**

: **gcloud dataplex assets create - create a Dataplex asset resource**

**SYNOPSIS**

: **`gcloud dataplex assets create` (`[ASSET](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#ASSET)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--zone)`=`ZONE`) (`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--resource-type)`=`RESOURCE_TYPE` : `[--resource-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--resource-name)`=`RESOURCE_NAME` `[--resource-read-access-mode](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--resource-read-access-mode)`=`RESOURCE_READ_ACCESS_MODE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--validate-only)`] [`[--[no-]discovery-enabled](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--[no-]discovery-enabled)` `[--discovery-exclude-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--discovery-exclude-patterns)`=[`EXCLUDE_PATTERNS`,…] `[--discovery-include-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--discovery-include-patterns)`=[`INCLUDE_PATTERNS`,…] `[--discovery-schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--discovery-schedule)`=`DISCOVERY_SCHEDULE` `[--csv-delimiter](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--csv-delimiter)`=`CSV_DELIMITER` `[--[no-]csv-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--[no-]csv-disable-type-inference)` `[--csv-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--csv-encoding)`=`CSV_ENCODING` `[--csv-header-rows](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--csv-header-rows)`=`CSV_HEADER_ROWS` `[--[no-]json-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--[no-]json-disable-type-inference)` `[--json-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#--json-encoding)`=`JSON_ENCODING`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: An asset represents a cloud resource that is being managed within a lake as a
member of a zone.
This asset ID will be used to generate names such as table names when publishing
metadata to Hive Metastore and BigQuery.

- Must contain only lowercase letters, numbers, and hyphens.
- Must start with a letter.
- Must end with a number or a letter.
- Must be between 1-63 characters.
- Must be unique within the zone.

**EXAMPLES**

: To create a Dataplex asset with name `test-asset`, within zone
`test-zone`, in lake `test-lake`, in location
`us-central1`, with resource type `STORAGE_BUCKET`, with
resource name `projects/test-project/buckets/test-bucket`, run:

```
gcloud dataplex assets create test-asset --location=us-central --lake=test-lake --zone=test-zone --resource-type=STORAGE_BUCKET --resource-name=projects/test-project/buckets/test-bucket
```

To create a Dataplex asset with name `test-asset`, within zone
`test-zone`, in lake `test-lake`, in location
`us-central1`, with resource type `STORAGE_BUCKET`, with
resource name `projects/test-project/buckets/test-bucket`, with
discovery-enabled, and discovery schedule `0 * * * *`, run:

```
gcloud dataplex assets create test-asset --location=us-central --lake=test-lake --zone=test-zone --resource-type=STORAGE_BUCKET --resource-name=projects/test-project/buckets/test-bucket --discovery-enabled --discovery-schedule="0 * * * *"
```

**POSITIONAL ARGUMENTS**

: **Assets resource - Arguments and flags that define the Dataplex asset you want to
create. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ASSET`**:
ID of the assets or fully qualified identifier for the assets.
To set the `asset` attribute:

- provide the argument `asset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.

**--zone**:
The identifier of the Dataplex zone resource.
To set the `zone` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--resource-type**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the asset

**--display-name**:
Display name of the asset

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--validate-only**:
Validate the create action, but don't actually perform it.

**--[no-]discovery-enabled**

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
gcloud alpha dataplex assets create
```