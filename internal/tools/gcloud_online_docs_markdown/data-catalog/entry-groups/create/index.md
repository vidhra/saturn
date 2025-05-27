# gcloud data-catalog entry-groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create)*

**NAME**

: **gcloud data-catalog entry-groups create - create a Data Catalog entry group**

**SYNOPSIS**

: **`gcloud data-catalog entry-groups create` (`[ENTRY_GROUP](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create#ENTRY_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create#--location)`=`LOCATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/data-catalog/entry-groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` This command is deprecated. Please use `[gcloud dataplex
entry-groups](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-groups)` instead.
Create a Data Catalog entry group.

**EXAMPLES**

: To create an entry group for some data, run:

```
gcloud data-catalog entry-groups create group1 --location=us-central1 --display-name="analytics data - jan 2011" --description="Entries related to January 2011 analytics data."
```

**POSITIONAL ARGUMENTS**

: **Entry group resource - Entry group to create. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entry_group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY_GROUP`**:
ID of the entry group or fully qualified identifier for the entry group.
To set the `entry_group` attribute:

- provide the argument `entry_group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the entry group.
To set the `location` attribute:

- provide the argument `entry_group` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--description**:
Description of the entry group.

**--display-name**:
Human-readable name of the entry group.

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
gcloud alpha data-catalog entry-groups create
```

```
gcloud beta data-catalog entry-groups create
```