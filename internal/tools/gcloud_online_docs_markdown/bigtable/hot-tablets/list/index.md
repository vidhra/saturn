# gcloud bigtable hot-tablets list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list)*

**NAME**

: **gcloud bigtable hot-tablets list - list hot tablets in a Cloud Bigtable cluster**

**SYNOPSIS**

: **`gcloud bigtable hot-tablets list` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#CLUSTER)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--instance)`=`INSTANCE`) [`[--end-time](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--end-time)`=`END_TIME`] [`[--start-time](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--start-time)`=`START_TIME`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List hot tablets in a Cloud Bigtable cluster.

**EXAMPLES**

: Search for hot tablets in the past 24 hours:

```
gcloud bigtable hot-tablets list my-cluster-id --instance=my-instance-id
```

Search for hot tablets with start and end times by minute:

```
gcloud bigtable hot-tablets list my-cluster-id --instance=my-instance-id --start-time="2018-08-12 03:30:00" --end-time="2018-08-13 17:00:00"
```

Search for hot tablets with start and end times by day:

```
gcloud bigtable hot-tablets list my-cluster-id --instance=my-instance-id --start-time=2018-01-01 --end-time=2018-01-05
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - The cluster to list hot tablets for. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
Bigtable instance for the cluster.
To set the `instance` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line.**

**FLAGS**

: **--end-time**:
End time of the time range to search for hot tablets. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

**--start-time**:
Start time of the time range to search for hot tablets. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on time formats.

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

: These variants are also available:

```
gcloud alpha bigtable hot-tablets list
```

```
gcloud beta bigtable hot-tablets list
```