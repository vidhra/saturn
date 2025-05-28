# gcloud transfer jobs list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list)*

**NAME**

: **gcloud transfer jobs list - list Transfer Service transfer jobs**

**SYNOPSIS**

: **`gcloud transfer jobs list` [`[--limit](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list#--page-size)`=`PAGE_SIZE`; default=256] [`[--job-names](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list#--job-names)`=[`JOB_NAMES`,…]] [`[--job-statuses](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list#--job-statuses)`=[`JOB_STATUSES`,…]] [`[--expand-table](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list#--expand-table)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/jobs/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Transfer Service transfer jobs in a given project to show their
configurations and latest operations.

**EXAMPLES**

: To list all jobs in your current project, run:

```
gcloud transfer jobs list
```

To list all disabled jobs in your project, run:

```
gcloud transfer jobs list --job-statuses=disabled
```

To list jobs 'foo' and 'bar', run:

```
gcloud transfer jobs list --job-names=foo,bar
```

To list all information about all jobs formatted as JSON, run:

```
gcloud transfer jobs list --format=json
```

To list all information about jobs 'foo' and 'bar' formatted as YAML, run:

```
gcloud transfer jobs list --job-names=foo,bar --format=YAML
```

**FLAGS**

: **--limit**:
Return the first items from the API up to this limit.

**--page-size**:
Retrieve batches of this many items from the API.

**--job-names**:
The names of the jobs you want to list. Separate multiple job names with commas
(e.g., --job-names=foo,bar). If not specified, all jobs will be listed.

**--job-statuses**:
List only jobs with the statuses you specify. Options include 'enabled',
'disabled', 'deleted' (case insensitive). Separate multiple statuses with commas
(e.g., --job-statuses=enabled,deleted). If not specified, all jobs will be
listed.

**--expand-table**:
Include additional table columns (job name, source, destination, frequency,
lastest operation name, job status) in command output. Tip: increase the size of
your terminal before running the command.

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
gcloud alpha transfer jobs list
```