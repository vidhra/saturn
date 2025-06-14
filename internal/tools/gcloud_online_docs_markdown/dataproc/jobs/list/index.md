# gcloud dataproc jobs list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list)*

**NAME**

: **gcloud dataproc jobs list - list jobs in a project**

**SYNOPSIS**

: **`gcloud dataproc jobs list` [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--cluster)`=`CLUSTER`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--region)`=`REGION`] [`[--state-filter](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--state-filter)`=`STATE_FILTER`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--page-size)`=`PAGE_SIZE`; default=100] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/jobs/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List jobs in a project. An optional filter can be used to constrain the jobs
returned. Filters are case-sensitive and have the following syntax:

```
[field = value] AND [field [= value]] …
```

where `field` is `status.state` or
`labels.[KEY]`, and `[KEY]` is a label key.
`value` can be `*` to match all values.
`status.state` can be either `ACTIVE` or
`INACTIVE`. Only the logical `AND` operator is supported;
space-separated items are treated as having an implicit `AND`
operator.

**EXAMPLES**

: To see the list of all jobs in Dataproc's 'us-central1' region, run:

```
gcloud dataproc jobs list --region=us-central1
```

To see a list of all active jobs in cluster 'mycluster' with a label
`env=staging` located in 'us-central1', run:

```
gcloud dataproc jobs list --region=us-central1 --filter='status.state = ACTIVE AND
    placement.clusterName = 'mycluster' AND labels.env = staging'
```

**FLAGS**

: **--cluster**:
Restrict to the jobs of this Dataproc cluster.

**--region**:
Dataproc region to use. Each Dataproc region constitutes an independent resource
namespace constrained to deploying instances into Compute Engine zones inside
the region. Overrides the default `dataproc/region` property value
for this command invocation.

**--state-filter**:
Filter by job state. `STATE_FILTER` must be one of:
`active`, `inactive`.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is `100`. Paging
may be applied before or after `--filter` and `--limit`
depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha dataproc jobs list
```

```
gcloud beta dataproc jobs list
```