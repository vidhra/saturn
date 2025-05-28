# gcloud transfer operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list)*

**NAME**

: **gcloud transfer operations list - list Transfer Service transfer operations**

**SYNOPSIS**

: **`gcloud transfer operations list` [`[--limit](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#--page-size)`=`PAGE_SIZE`; default=256] [`[--job-names](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#--job-names)`=[`JOB_NAMES`,…]] [`[--operation-names](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#--operation-names)`=[`OPERATION_NAMES`,…]] [`[--operation-statuses](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#--operation-statuses)`=[`OPERATION_STATUSES`,…]] [`[--expand-table](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#--expand-table)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Transfer Service transfer operations to view their progress details at a
glance.

**EXAMPLES**

: To list all transfer operations in your current project, run:

```
gcloud transfer operations list
```

To list all failed operations in your project, run:

```
gcloud transfer operations list --operation-statuses=failed
```

To list operations 'foo' and 'bar', run:

```
gcloud transfer operations list --operation-names=foo,bar
```

To list all operations in your current project as JSON, which provides all
fields and formatting available in the API, run:

```
gcloud transfer operations list --format=json
```

**FLAGS**

: **--limit**:
Return the first items from the API up to this limit.

**--page-size**:
Retrieve batches of this many items from the API.

**--job-names**:
The names of the jobs whose operations you want to list. Separate multiple job
names with commas (e.g., --job-names=foo,bar). If not specified, operations for
all jobs are listed.

**--operation-names**:
The names of operations you want to list. Separate multiple operation names with
commas (e.g., --operation-names-name=foo,bar). If not specified, all operations
are listed.

**--operation-statuses**:
List only transfer operations with the statuses you specify. Options include
'in_progress', 'paused', 'success','failed', 'aborted'. Separate multiple
statuses with commas (e.g., --operation-statuses=failed,aborted).

**--expand-table**:
Include additional table columns (operation name, start time, status, data
copied, status, has errors, job name) in command output. Tip: increase the size
of your terminal before running the command.

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
gcloud alpha transfer operations list
```