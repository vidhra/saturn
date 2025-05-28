# gcloud filestore instances snapshots list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list)*

**NAME**

: **gcloud filestore instances snapshots list - list Filestore snapshots**

**SYNOPSIS**

: **`gcloud filestore instances snapshots list` `[--instance](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--instance)`=`INSTANCE` (`[--instance-location](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--instance-location)`=`INSTANCE_LOCATION`     | `[--instance-region](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--instance-region)`=`INSTANCE_REGION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/filestore/instances/snapshots/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all Filestore snapshots for the specified instance.
To limit the number of snapshots to list, use the `--limit` flag.
This command can fail for the following reasons:

- Specified instance does not exist.
- The active account does not have permission to list snapshots for the given
instance.
- The service tier of the instance does not support snapshots.

**EXAMPLES**

: To list up to five snapshots for the instance
``my-instance`` from
``us-central1``, run:

```
gcloud filestore instances snapshots list --instance=my-instance --instance-region=us-central1 --limit=5
```

**REQUIRED FLAGS**

: **--instance**:
Name of the Filestore instance the snapshot belongs to.

**--instance-location**

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

**API REFERENCE**

: This command uses the `file/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/filestore/](https://cloud.google.com/filestore/)

**NOTES**

: This variant is also available:

```
gcloud beta filestore instances snapshots list
```