# gcloud scc manage custom-modules sha list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list)*

**NAME**

: **gcloud scc manage custom-modules sha list - list the details of Security Health Analyics custom modules**

**SYNOPSIS**

: **`gcloud scc manage custom-modules sha list` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--project)`=`PROJECT_ID_OR_NUMBER`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List the details of the resident and inherited Security Health Analytics custom
modules for the specified folder or project. For an organization, this command
lists only the custom modules that are created at the organization level. Custom
modules created in child folders or projects are not included in the list. To
list the resident custom modules and the modules that are created in child
folders or projects, use `gcloud scc manage custom-modules sha
list-descendant`.

**EXAMPLES**

: To list resident and inherited Security Health Analytics custom modules for
organization `123`, run:

```
gcloud scc manage custom-modules sha list --organization=organizations/123
```

To list resident and inherited Security Health Analytics custom modules for
folder `456`, run:

```
gcloud scc manage custom-modules sha list --folder=folders/456
```

To list resident and inherited Security Health Analytics custom modules for
project `789`, run:

```
gcloud scc manage custom-modules sha list --project=projects/789
```

You can also specify the parent more generally:

```
gcloud scc manage custom-modules sha list 123456 --parent=organizations/123
```

Or just specify the fully qualified module name:

```
gcloud scc manage custom-modules sha list organizations/123/locations/global/securityHealthAnalyticsCustomModules/123456
```

**REQUIRED FLAGS**

: **--folder**

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

: This variant is also available:

```
gcloud alpha scc manage custom-modules sha list
```