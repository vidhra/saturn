# gcloud data-catalog tags delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete)*

**NAME**

: **gcloud data-catalog tags delete - delete a Data Catalog entry tag**

**SYNOPSIS**

: **`gcloud data-catalog tags delete` (`[TAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete#TAG)` : `[--entry](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete#--entry)`=`ENTRY` `[--entry-group](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete#--entry-group)`=`ENTRY_GROUP` `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/tags/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)`
instead. Note that aspects - successors of tags - are part of the entry resource
and are managed by `[gcloud
dataplex entries](https://cloud.google.com/sdk/gcloud/reference/dataplex/entries)` command.
Delete a Data Catalog entry tag.

**EXAMPLES**

: Delete a Data Catalog entry tag:

```
gcloud data-catalog tags delete TAG
```

**POSITIONAL ARGUMENTS**

: **Tag resource - Entry tag to delete. The arguments in this group can be used to
specify the attributes of this resource. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TAG`**:
ID of the tag or fully qualified identifier for the tag.
To set the `tag` attribute:

- provide the argument `tag` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--entry**:
Entry of the tag.
To set the `entry` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--entry` on the command line.

**--entry-group**:
Entry group of the tag.
To set the `entry-group` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
- provide the argument `--entry-group` on the command line.

**--location**:
Location of the tag.
To set the `location` attribute:

- provide the argument `tag` on the command line with a fully specified
name;
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

**NOTES**

: These variants are also available:

```
gcloud alpha data-catalog tags delete
```

```
gcloud beta data-catalog tags delete
```