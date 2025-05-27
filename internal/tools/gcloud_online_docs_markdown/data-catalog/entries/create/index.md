# gcloud data-catalog entries create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create)*

**NAME**

: **gcloud data-catalog entries create - create a Data Catalog entry**

**SYNOPSIS**

: **`gcloud data-catalog entries create` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--location)`=`LOCATION`) ([`[--type](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--type)`=`TYPE` : `[--gcs-file-patterns](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--gcs-file-patterns)`=[`GCS_FILE_PATTERNS`,…]]     | `[--user-specified-system](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--user-specified-system)`=`USER_SPECIFIED_SYSTEM` ([`[--user-specified-type](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--user-specified-type)`=`USER_SPECIFIED_TYPE` : `[--linked-resource](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--linked-resource)`=`LINKED_RESOURCE` `[--source-system-create-time](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--source-system-create-time)`=`SOURCE_SYSTEM_CREATE_TIME` `[--source-system-update-time](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--source-system-update-time)`=`SOURCE_SYSTEM_UPDATE_TIME`])) [`[--description](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--display-name)`=`DISPLAY_NAME`] [`[--fully-qualified-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--fully-qualified-name)`=`FULLY_QUALIFIED_NAME`] [`[--schema](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--schema)`=[`COLUMN_NAME`=`COLUMN_TYPE`,…]     | `[--schema-from-file](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#--schema-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)`
instead.
Create a Data Catalog entry.

**EXAMPLES**

: To create an entry for a Google Cloud Storage fileset, run:

```
gcloud data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --gcs-file-patterns="gs://bucket1/abc/*,gs://bucket1/file1" --display-name="analytics data" --type=FILESET
```

To create an entry for a Google Cloud Storage fileset with an inline schema,
run:

```
gcloud data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --gcs-file-patterns="gs://bucket1/*" --display-name="sales data" --schema="qtr=STRING,sales=FLOAT,year=STRING"
```

To create an entry for a resource of a custom type, run:

```
gcloud data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --display-name="sales data" --linked-resource="www.resource.com" --user-specified-type="type_name" --user-specified-system="system_name"
```

To create an entry for a Google Cloud Storage fileset with a schema from a file,
run:

```
gcloud data-catalog entries create entry1 --location=us-central1 --entry-group=group1 --gcs-file-patterns="gs://bucket1/*" --display-name="sales data" --schema-from-file=/tmp/schema.json --type=FILESET
```

**POSITIONAL ARGUMENTS**

: **Entry resource - Entry to create. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY`**:
ID of the entry or fully qualified identifier for the entry.
To set the `entry` attribute:

- provide the argument `entry` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--entry-group**:
Entry group of the entry.
To set the `entry-group` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--entry-group` on the command line.

**--location**:
Location of the entry.
To set the `location` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--type**

**OPTIONAL FLAGS**

: **--description**:
Textual description of the entry.

**--display-name**:
Human-readable name for the entry.

**--fully-qualified-name**:
Fully qualified name of the resource.

**--schema**

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

: This command uses the `datacatalog/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/data-catalog/docs/](https://cloud.google.com/data-catalog/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha data-catalog entries create
```

```
gcloud beta data-catalog entries create
```