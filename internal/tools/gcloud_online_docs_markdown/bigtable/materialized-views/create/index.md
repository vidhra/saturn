# gcloud bigtable materialized-views create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create)*

**NAME**

: **gcloud bigtable materialized-views create - create a new Bigtable materialized view**

**SYNOPSIS**

: **`gcloud bigtable materialized-views create` (`[MATERIALIZED_VIEW](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create#MATERIALIZED_VIEW)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create#--instance)`=`INSTANCE`) `[--query](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create#--query)`=`QUERY` [`[--async](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create#--async)`] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create#--deletion-protection)`=`DELETION_PROTECTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Bigtable materialized view.

**EXAMPLES**

: To create a materialized view, run:
```
gcloud bigtable materialized-views create my-materialized-view-id --instance=my-instance-id --query="SELECT my-column-family FROM my-table --deletion-protection=false"
```

**POSITIONAL ARGUMENTS**

: **Materialized view resource - The materialized view to create. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `materialized_view` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MATERIALIZED_VIEW`**:
ID of the materialized view or fully qualified identifier for the materialized
view.
To set the `name` attribute:

- provide the argument `materialized_view` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Bigtable instance for the materialized view.
To set the `instance` attribute:

- provide the argument `materialized_view` on the command line with a
fully specified name;
- provide the argument `--instance` on the command line.**

**REQUIRED FLAGS**

: **--query**:
The query of the view.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--deletion-protection**:
Whether the view is protected from deletion.

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

: These variants are also available:

```
gcloud alpha bigtable materialized-views create
```

```
gcloud beta bigtable materialized-views create
```