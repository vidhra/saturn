# gcloud workstations configs list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list)*

**NAME**

: **gcloud workstations configs list - list workstation configurations**

**SYNOPSIS**

: **`gcloud workstations configs list` [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#--region)`=`REGION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all workstation configurations under the specified cluster.

**EXAMPLES**

: To list workstation configurations, run:

```
gcloud workstations configs list
```

**FLAGS**

: **Cluster resource - The cluster of the configurations to display. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- set the property `workstations/cluster` with a fully specified name;
- default is all clusters with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--cluster**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `--cluster` on the command line;
- set the property `workstations/cluster`;
- default is all clusters .

**--region**:
The name of the region of the cluster.
To set the `region` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- set the property `workstations/cluster` with a fully specified name;
- default is all clusters with a fully specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`;
- default is all regions .**

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

: This command uses the `workstations/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/workstations](https://cloud.google.com/workstations)

**NOTES**

: These variants are also available:

```
gcloud alpha workstations configs list
```

```
gcloud beta workstations configs list
```