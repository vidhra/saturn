# gcloud data-catalog entries update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update)*

**NAME**

: **gcloud data-catalog entries update - update a Data Catalog entry**

**SYNOPSIS**

: **`gcloud data-catalog entries update` [`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--location)`=`LOCATION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--display-name)`=`DISPLAY_NAME`] [`[--lookup-entry](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--lookup-entry)`=`RESOURCE`] [`[--add-file-patterns](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--add-file-patterns)`=[`PATTERN`,…] `[--clear-file-patterns](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--clear-file-patterns)`     | `[--remove-file-patterns](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--remove-file-patterns)`=[`PATTERN`,…]     | `[--linked-resource](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--linked-resource)`=`LINKED_RESOURCE` `[--user-specified-system](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--user-specified-system)`=`USER_SPECIFIED_SYSTEM` `[--user-specified-type](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--user-specified-type)`=`USER_SPECIFIED_TYPE`] [`[--schema](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--schema)`=[`COLUMN_NAME`=`COLUMN_TYPE`,…]     | `[--schema-from-file](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#--schema-from-file)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)`
instead.
Update a Data Catalog entry. The entry to update can either be specified
directly, or the `--lookup-entry` flag may be used to update the
entry corresponding to the lookup of the given resource.

**EXAMPLES**

: To update the schema of a Cloud Pub/Sub entry inline, run:

```
gcloud data-catalog entries update entry1 --location=global --entry-group=@pubsub --schema="column1=type1,column2=type2"
```

To update the schema of a Cloud Pub/Sub entry from a file, run:

```
gcloud data-catalog entries update entry1 --location=global --entry-group=@pubsub --schema-from-file="/tmp/schema.json"
```

To lookup the entry of a Cloud Pub/Sub topic by its SQL name and update its
schema in one command, run:

```
gcloud data-catalog entries update --lookup-entry='pubsub.topic.`my-project1`.topic1' --schema="column1=type1,column2=type2"
```

**POSITIONAL ARGUMENTS**

: **Entry resource - Entry to update. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entry` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

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

**FLAGS**

: **--description**:
Textual description of the entry.

**--display-name**:
Human-readable name for the entry.

**--lookup-entry**:
The name of the target resource whose entry to update. This can be either the
Google Cloud Platform resource name or the SQL name of a Google Cloud Platform
resource. This flag allows one to update the entry corresponding to the lookup
of the given resource, without needing to specify the entry directly.

**--add-file-patterns**

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
gcloud alpha data-catalog entries update
```

```
gcloud beta data-catalog entries update
```