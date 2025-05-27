# gcloud data-catalog tags create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create)*

**NAME**

: **gcloud data-catalog tags create - create a Data Catalog entry tag**

**SYNOPSIS**

: **`gcloud data-catalog tags create` `[--tag-file](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--tag-file)`=`TAG_FILE` (`[--entry](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--entry)`=`ENTRY` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--location)`=`LOCATION`) (`[--tag-template](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--tag-template)`=`TAG_TEMPLATE` : `[--tag-template-location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--tag-template-location)`=`TAG_TEMPLATE_LOCATION` `[--tag-template-project](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--tag-template-project)`=`TAG_TEMPLATE_PROJECT`) [`[--scope](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#--scope)`=`SCOPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)`
instead. Note that aspects - successors of tags - are part of the entry resource
and are managed by `[gcloud
dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)` command.
Create a Data Catalog entry tag.

**EXAMPLES**

: Create a Data Catalog entry tag:

```
gcloud data-catalog tags create --entry=ENTRY --tag-template=TAG_TEMPLATE --tag-file=TAG_FILE
```

**REQUIRED FLAGS**

: **--tag-file**:
Path to a JSON or YAML file containing the tag.
The file should contain a JSON/YAML object with a key and value for each field
that should be set. See $ [gcloud
topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on how to specify timestamp fields.
For example:

```
{
  "dbl_field": 123,
  "str_field": "String",
  "bool_field": true,
  "ts_field": "1970-01-01T00:00:00.000Z",
  "enum_field": "ENUM_A",
}
```

**Entry resource - Entry to attach the tag to. The arguments in this group can be
used to specify the attributes of this resource. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--entry` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--entry**:
ID of the entry or fully qualified identifier for the entry.
To set the `entry` attribute:

- provide the argument `--entry` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--entry-group**:
Entry group of the entry.
To set the `entry-group` attribute:

- provide the argument `--entry` on the command line with a fully
specified name;
- provide the argument `--entry-group` on the command line.

**--location**:
Location of the entry.
To set the `location` attribute:

- provide the argument `--entry` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**--tag-template-location**

**OPTIONAL FLAGS**

: **--scope**:
Scope within the parent resource that the tag is attached to. Scopes allow users
to attach tags to individual columns based on the parent resource's schema. To
attach a tag to a nested column, use '.' to separate the column names:
'outer_column.inner_column'.

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
gcloud alpha data-catalog tags create
```

```
gcloud beta data-catalog tags create
```