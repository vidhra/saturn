# gcloud logging operations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/operations/list](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list)*

**NAME**

: **gcloud logging operations list - list long running operations**

**SYNOPSIS**

: **`gcloud logging operations list` `[--location](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--location)`=`LOCATION` `[--operation-filter](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--operation-filter)`=`OPERATION_FILTER` [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--project)`=`PROJECT_ID`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/operations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Return a list of long running operation details in given LOCATION. The
operations were scheduled by other gcloud commands. For example: a
copy_log_entries operation scheduled by command: gcloud alpha logging operations
copy BUCKET_ID DESTINATION --location=LOCATION. Note: while listing the
operations, the request_type must be specified in filter. Example:
--operation-filter=request_type=CopyLogEntries, Supported operation types are:
CopyLogEntries, CreateBucket and UpdateBucket. Other supported filter expression
are: operation_start_time, operation_finish_time and operation_state.

**EXAMPLES**

: To list CopyLogEntries operations, run:

```
gcloud logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries'
```

To list CopyLogEntries operations that started after a specified time, run:

```
gcloud logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
operation_start_time>="2023-11-20T00:00:00Z"'
```

To list CopyLogEntries operations that finished before a specified time, run:

```
gcloud logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
operation_finish_time<="2023-11-20T00:00:00Z"'
```

To list CopyLogEntries operations that have a specified state, run:

```
gcloud logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
operation_state=STATE'
```

To list CopyLogEntries operations that don't have a specified state, run:

```
gcloud logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
operation_state!=STATE'
```

**REQUIRED FLAGS**

: **--location**:
Location of the operations.

**--operation-filter**:
Filter expression that specifies the operations to return.

**FLAGS**

: **--billing-account**

**LIST COMMAND FLAGS**

: **--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

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
gcloud alpha logging operations list
```

```
gcloud beta logging operations list
```