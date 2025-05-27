# gcloud data-catalog entries star  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/star](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/star)*

**NAME**

: **gcloud data-catalog entries star - star a Data Catalog entry**

**SYNOPSIS**

: **`gcloud data-catalog entries star` (`[ENTRY](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/star#ENTRY)` : `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/star#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/star#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entries/star#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated.
Star a Data Catalog entry.

**EXAMPLES**

: To star the entry 'entry1' in the group 'group1', run:

```
gcloud data-catalog entries star entry1 --entry-group=group1 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Entry resource - Entry to star. The arguments in this group can be used to
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