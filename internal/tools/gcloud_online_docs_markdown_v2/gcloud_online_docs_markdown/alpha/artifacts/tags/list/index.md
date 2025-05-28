# gcloud alpha artifacts tags list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list)*

**NAME**

: **gcloud alpha artifacts tags list - list Artifact Registry tags**

**SYNOPSIS**

: **`gcloud alpha artifacts tags list` `[--package](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--package)`=`PACKAGE` [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--location)`=`LOCATION` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--repository)`=`REPOSITORY`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/tags/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List all Artifact Registry tags in the specified package.
This command can fail for the following reasons:

- The specified version or package does not exist.
- The active account does not have permission to list tags.
- The specified package format doesn't support tag operations (e.g. maven).

To specify the maximum number of tags to list, use the --limit flag.

**EXAMPLES**

: To list tags for package `my-package`:

```
gcloud alpha artifacts tags list --package=my-package
```

The following command lists a maximum of five tags for package
`my-package`:

```
gcloud alpha artifacts tags list --package=my-package --limit=5
```

To list tags of package `my-package` with name as
`my-tag`:

```
gcloud alpha artifacts tags list --package=my-package --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my-package/tags/my-tag"'
```

To list tags of package `my-package` with a given partial name, use
`*` to match any character in name:

```
gcloud alpha artifacts tags list --package=my-package --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my-package/tags/my*"'
```

```
gcloud alpha artifacts tags list --package=my-package --filter='name="projects/my-project/locations/us/repositories/my-repo/packages/my-package/tags/*tag"'
```

**REQUIRED FLAGS**

: **--package**:
List all tags in a specified artifact, such as a container image or a language
package.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts tags list
```

```
gcloud beta artifacts tags list
```