# gcloud alpha artifacts docker images list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list)*

**NAME**

: **gcloud alpha artifacts docker images list - list Artifact Registry container images**

**SYNOPSIS**

: **`gcloud alpha artifacts docker images list` [`[IMAGE_PATH](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#IMAGE_PATH)`] [`[--include-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--include-tags)`] [`[--occurrence-filter](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--occurrence-filter)`=`OCCURRENCE_FILTER`; default=`'kind="BUILD" OR kind="IMAGE" OR kind="DISCOVERY" OR kind="SBOM_REFERENCE"'`] [`[--show-occurrences](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--show-occurrences)`] [`[--show-occurrences-from](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--show-occurrences-from)`=`SHOW_OCCURRENCES_FROM`; default=10] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List all Artifact Registry container images in the
specified repository or image path.
A valid Docker repository has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID
A valid image has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH
To specify the maximum number of images to list, use the --limit flag.

**EXAMPLES**

: To list images under the current project, repository, and location:

```
gcloud alpha artifacts docker images list
```

To list images with tags under the current project, repository, and location:

```
gcloud alpha artifacts docker images list --include-tags
```

To list images under repository `my-repo`, project
`my-project`, in `us-central1`:

```
gcloud alpha artifacts docker images list us-central1-docker.pkg.dev/my-project/my-repo
```

The following command lists a maximum of five images:

```
gcloud alpha artifacts docker images list docker.pkg.dev/my-project/my-repo --limit=5
```

**POSITIONAL ARGUMENTS**

: **[`IMAGE_PATH`]**:
An Artifact Registry repository or a container image. If not specified, default
config values are used.
A valid docker repository has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID
A valid image has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH

**FLAGS**

: **--include-tags**:
If specified, tags associated with each image digest are displayed up to a
maximum of 100 tags per version.

**--occurrence-filter**:
A filter for the occurrences which will be summarized.

**--show-occurrences**:
Show summaries of the various occurrence types.

**--show-occurrences-from**:
The number of the most recent images for which to summarize occurrences.

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
gcloud artifacts docker images list
```

```
gcloud beta artifacts docker images list
```