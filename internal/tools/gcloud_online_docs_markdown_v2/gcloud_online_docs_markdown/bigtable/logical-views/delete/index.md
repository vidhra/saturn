# gcloud bigtable logical-views delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/delete](https://cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/delete)*

**NAME**

: **gcloud bigtable logical-views delete - delete a Bigtable logical view**

**SYNOPSIS**

: **`gcloud bigtable logical-views delete` (`[LOGICAL_VIEW](https://cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/delete#LOGICAL_VIEW)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/delete#--instance)`=`INSTANCE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Bigtable logical view.

**EXAMPLES**

: To delete a logical view, run:

```
gcloud bigtable logical-views delete my-logical-view-id --instance=my-instance-id
```

**POSITIONAL ARGUMENTS**

: **Logical view resource - The logical view to delete. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `logical_view` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`LOGICAL_VIEW`**:
ID of the logical view or fully qualified identifier for the logical view.
To set the `name` attribute:

- provide the argument `logical_view` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Bigtable instance for the logical view.
To set the `instance` attribute:

- provide the argument `logical_view` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

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
gcloud alpha bigtable logical-views delete
```

```
gcloud beta bigtable logical-views delete
```