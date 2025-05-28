# gcloud artifacts packages list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list)*

**NAME**

: **gcloud artifacts packages list - list Artifact Registry packages**

**SYNOPSIS**

: **`gcloud artifacts packages list` [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#--repository)`=`REPOSITORY`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/packages/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all Artifact Registry packages in the specified repository and project.
To specify the maximum number of packages to list, use the --limit flag.

**EXAMPLES**

: The following command lists a maximum of five packages:

```
gcloud artifacts packages list --limit=5
```

To list packages with name as `my-pkg`:

```
gcloud artifacts packages list --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my-pkg"
```

To list packages with a given partial name, use `*` to match any
character in name:

```
gcloud artifacts packages list --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/*pkg"'
```

```
gcloud artifacts packages list --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my*"'
```

To list files that have annotations:

```
gcloud artifacts packages list --filter=annotations:*
```

To list packages with annotations pair as [annotation_key: annotation_value]:

```
gcloud artifacts packages list --filter='annotations.annotation_key:annotation_value'
```

To list packages with annotations containing key as `my_key`:

```
gcloud artifacts packages list --filter='annotations.my_key'
```

```
If the key or value contains special characters, such as `my.key` or `my.value`, backtick("`") is required:
```

```
gcloud artifacts packages list --filter='annotations.`my.key`'
```

```
gcloud artifacts packages list --filter='annotations.`my.key`:`my.value`'
```

To list packages with given partial annotation key or value, use `*`
to match any character:

```
gcloud artifacts packages list --filter='annotations.my_*:`*.value`'
```

To list packages ordered by create_time:

```
gcloud artifacts packages list --sort-by=create_time
```

To list packages ordered by update_time reversely:

```
gcloud artifacts packages list --sort-by=~update_time
```

**FLAGS**

: **Repository resource - The Artifact Registry repository. If not specified, the
current artifacts/repository is used. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
Location of the repository.
To set the `location` attribute:

- provide the argument `--repository` on the command line with a fully
specified name;
- set the property `artifacts/repository` with a fully specified name;
- provide the argument `--location` on the command line;
- set the property `artifacts/location`.

**--repository**:
ID of the repository or fully qualified identifier for the repository.
To set the `repository` attribute:

- provide the argument `--repository` on the command line;
- set the property `artifacts/repository`.**

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

: These variants are also available:

```
gcloud alpha artifacts packages list
```

```
gcloud beta artifacts packages list
```