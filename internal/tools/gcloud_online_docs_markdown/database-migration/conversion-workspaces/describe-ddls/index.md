# gcloud database-migration conversion-workspaces describe-ddls  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls)*

**NAME**

: **gcloud database-migration conversion-workspaces describe-ddls - describe DDLs in a Database Migration Service conversion workspace**

**SYNOPSIS**

: **`gcloud database-migration conversion-workspaces describe-ddls` (`[CONVERSION_WORKSPACE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#CONVERSION_WORKSPACE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--region)`=`REGION`) [`[--commit-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--commit-id)`=`COMMIT_ID`] [`[--tree-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--tree-type)`=`TREE_TYPE`; default="DRAFT"] [`[--uncommitted](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--uncommitted)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--page-size)`=`PAGE_SIZE`; default=100] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--sort-by)`=[`FIELD`,…]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#--uri)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/describe-ddls#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe DDLs in a Database Migration Service conversion workspace.

**EXAMPLES**

: To describe the DDLs of the draft tree in my-conversion-workspace in a project
and location `us-central1`, run:

```
gcloud database-migration conversion-workspaces describe-ddls my-conversion-workspace --region=us-central1
```

To describe the DDLs of the source tree in a conversion workspace in a project
and location `us-central1`, run:

```
gcloud database-migration conversion-workspaces describe-ddls my-conversion-workspace --region=us-central1 --tree-type=SOURCE
```

**POSITIONAL ARGUMENTS**

: **Conversion workspace resource - The conversion workspace to describe DDLs. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `conversion_workspace` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONVERSION_WORKSPACE`**:
ID of the conversion_workspace or fully qualified identifier for the
conversion_workspace.
To set the `conversion_workspace` attribute:

- provide the argument `conversion_workspace` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the conversion_workspace.
To set the `region` attribute:

- provide the argument `conversion_workspace` on the command line with
a fully specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--commit-id**:
Request a specific commit id. If not specified, the entities from the latest
commit are returned.

**--tree-type**:
Tree type for database entities. `TREE_TYPE` must be one
of: `SOURCE`, `DRAFT`.

**--uncommitted**:
Whether to retrieve the latest committed version of the entities or the latest
version. This field is ignored if a specific commit_id is specified.

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
maximum number of resources per page. The default is `100`. Paging
may be applied before or after `--filter` and `--limit`
depending on the service.

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