# gcloud dataflow jobs list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list)*

**NAME**

: **gcloud dataflow jobs list - lists all jobs in a particular project, optionally filtered by region**

**SYNOPSIS**

: **`gcloud dataflow jobs list` [`[--created-after](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--created-after)`=`CREATED_AFTER`] [`[--created-before](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--created-before)`=`CREATED_BEFORE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--region)`=`REGION`] [`[--status](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--status)`=`STATUS`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--limit)`=`LIMIT`; default=100] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--page-size)`=`PAGE_SIZE`; default=20] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: By default, 100 jobs in the current project are listed; this can be overridden
with the gcloud --project flag, and the --limit flag.
Using the --region flag will only list jobs from the given regional endpoint.

**EXAMPLES**

: Filter jobs with the given name:

```
gcloud dataflow jobs list --filter="name=my-wordcount"
```

List jobs with from a given region:

```
gcloud dataflow jobs list --region="europe-west1"
```

List jobs created this year:

```
gcloud dataflow jobs list --created-after=2018-01-01
```

List jobs created more than a week ago:

```
gcloud dataflow jobs list --created-before=-P1W
```

**FLAGS**

: **--created-after**:
Filter the jobs to those created after the given time. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats. For example, `2018-01-01` is the first
day of the year, and `-P2W` is 2 weeks ago.

**--created-before**:
Filter the jobs to those created before the given time. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--region**:
Only resources from the given region are queried. If not provided, an attempt
will be made to query from all available regions. In the event of an outage,
jobs from certain regions may not be available.

**--status**:
Filter the jobs to those with the selected status.
`STATUS` must be one of:

**`active`**:
Filters the jobs that are running ordered on the creation timestamp.

**`all`**:
Returns running jobs first, ordered on creation timestamp, then, returns all
terminated jobs ordered on the termination timestamp.

**`terminated`**:
Filters the jobs that have a terminated state, ordered on the termination
timestamp. Example terminated states: Done, Updated, Cancelled, etc.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `100`. This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is `20`. Paging may
be applied before or after `--filter` and `--limit`
depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--uri**:
Print a list of resource URIs instead of the default output, and change the
command output to a list of URIs. If this flag is used with
`--format`, the formatting is applied on this URI list. To display
URIs alongside other keys instead, use the `uri()` transform.

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
gcloud beta dataflow jobs list
```