# gcloud compute storage-pools list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list)*

**NAME**

: **gcloud compute storage-pools list - view storage pools**

**SYNOPSIS**

: **`gcloud compute storage-pools list` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: View storage pools.
The compact, default output format is explained below:
The type column contains all three types -- storage pool type, capacity and
performance. For example, the value
> "Hdb/Adv/Std"
means the storage pool type is "hyperdisk-balanced", its capacity type is
"advanced", and its performance type is "standard."
The list of storage pool abbreviations is as follows:

- HdB: Hyperdisk Balanced
- HdT: Hyperdisk Throughput

The list of capacity/performance abbreviations is as follows:

- Adv: Advanced
- Std: Standard

The capacity column, and standard-performance iops and throughput columns
describe the used, provisioned, and the utilization rate. For example, the
following value for capacity:
40 / 50 (80%)
means 40 TB of it is used, 50 TB provisioned, and its utilization rate is 80%.
The utilization rate is equivalent to used capacity divided by provisioned
capacity.
For advanced-performance storage pools, the iops and throughput columns will
simply show the provisioned values.

**EXAMPLES**

: To display all storage pools in all regions and zones, run the following
command:

```
gcloud compute storage-pools list
```

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

: This command uses the `compute/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute storage-pools list
```

```
gcloud beta compute storage-pools list
```