# gcloud alpha asset list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list)*

**NAME**

: **gcloud alpha asset list - list the Cloud assets**

**SYNOPSIS**

: **`gcloud alpha asset list` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--project)`=`PROJECT_ID`) [`[--asset-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--asset-types)`=[`ASSET_TYPES`,…]] [`[--content-type](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--content-type)`=`CONTENT_TYPE`] [`[--relationship-types](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--relationship-types)`=[`RELATIONSHIP_TYPES`,…]] [`[--snapshot-time](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--snapshot-time)`=`SNAPSHOT_TIME`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List the Cloud assets. Note that to list a project
different from the project you want to bill, you can use --billing-project or
authenticate with a service account. See [https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/gcloud-asset](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/gcloud-asset)
for examples of using a service account.

**EXAMPLES**

: To list a snapshot of assets of type 'compute.googleapis.com/Disk' in project
'test-project' at '2019-03-05T00:00:00Z', run:

```
gcloud alpha asset list --project='test-project' --asset-types='compute.googleapis.com/Disk' --snapshot-time='2019-03-05T00:00:00Z'
```

**REQUIRED FLAGS**

: **--folder**

**FLAGS**

: **--asset-types**:
A list of asset types (i.e., "compute.googleapis.com/Disk") to take a snapshot.
If specified and non-empty, only assets matching the specified types will be
returned. See [http://cloud.google.com/asset-inventory/docs/supported-asset-types](http://cloud.google.com/asset-inventory/docs/supported-asset-types)
for supported asset types.

**--content-type**:
Asset content type. If not specified, no content but the asset name and type
will be returned in the feed. For more information, see [https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType).
`CONTENT_TYPE` must be one of: `resource`,
`iam-policy`, `org-policy`, `access-policy`,
`os-inventory`, `relationship`.

**--relationship-types**:
A list of relationship types (i.e., "INSTANCE_TO_INSTANCEGROUP") to take a
snapshot. This argument will only be honoured if content_type=RELATIONSHIP. If
specified and non-empty, only relationships matching the specified types will be
returned. See [http://cloud.google.com/asset-inventory/docs/supported-asset-types](http://cloud.google.com/asset-inventory/docs/supported-asset-types)
for supported relationship types.

**--snapshot-time**:
Timestamp to take a snapshot on assets. This can only be a current or past time.
If not specified, the current time will be used. Due to delays in resource data
collection and indexing, there is a volatile window during which running the
same query at different times may return different results. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset list
```

```
gcloud beta asset list
```