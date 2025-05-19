# gcloud artifacts docker tags list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list)*

**NAME**

: **gcloud artifacts docker tags list - list all tags associated with a container image in Artifact Registry**

**SYNOPSIS**

: **`gcloud artifacts docker tags list` [`[IMAGE_PATH](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list#IMAGE_PATH)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A valid Docker top layer image has the format of

```
[<location>-]docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH
```

A valid container image can be referenced by tag or digest, has the format of

```
[<location>-]docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH:tag
[<location>-]docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH@sha256:digest
```

To specify the maximum number of repositories to list, use the --limit flag.

**EXAMPLES**

: To list all tags under the current project, repository, and location:

```
gcloud artifacts docker tags list
```

To list all tags under the `my-project`, `my-repository`,
across all locations:

```
gcloud artifacts docker tags list docker.pkg.dev/my-project/my-repository
```

To list all tags in repository `my-repository` in
`us-west1`:

```
gcloud artifacts docker tags list us-west1-docker.pkg.dev/my-project/my-repository
```

To list tags for image `busy-box` in `us-west1`:

```
gcloud artifacts docker tags list us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

**POSITIONAL ARGUMENTS**

: **[`IMAGE_PATH`]**:
An Artifact Registry repository or a container image. If not specified, default
config values are used.
A valid docker repository has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID
A valid image has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH

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
gcloud alpha artifacts docker tags list
```

```
gcloud beta artifacts docker tags list
```