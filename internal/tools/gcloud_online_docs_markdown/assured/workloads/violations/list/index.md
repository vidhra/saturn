# gcloud assured workloads violations list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list)*

**NAME**

: **gcloud assured workloads violations list - list all Assured Workloads violations that belong to a assured workloads environment**

**SYNOPSIS**

: **`gcloud assured workloads violations list` `[--location](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--organization)`=`ORGANIZATION` `[--workload](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--workload)`=`WORKLOAD` [`[--filter](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all Violations that belong to the given Assured Workloads environment.

**EXAMPLES**

: The following example command lists all violations with these properties:

- belonging to an organization with ID 123
- belonging to the assured workload with ID w123
- located in the `us-central1` region
- returning no more than 30 results
- requesting 10 results at a time from the backend

```
gcloud assured workloads violations list --organization=123 --location=us-central1 --workload=w123 --limit=30 --page-size=10
```

**REQUIRED FLAGS**

: **--location**:
The location of the Assured Workloads environments. For a current list of
supported LOCATION values, see [Assured
Workloads locations](https://cloud.google.com/assured-workloads/docs/locations).

**--organization**:
The parent organization of the Assured Workloads environments, provided as an
organization ID.

**--workload**:
The parent workload of the Assured Workloads violations, provided as workload
ID.

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
gcloud alpha assured workloads violations list
```

```
gcloud beta assured workloads violations list
```