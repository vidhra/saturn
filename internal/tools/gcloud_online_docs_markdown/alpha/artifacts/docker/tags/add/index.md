# gcloud alpha artifacts docker tags add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add)*

**NAME**

: **gcloud alpha artifacts docker tags add - add a tag to a container image in Artifact Registry**

**SYNOPSIS**

: **`gcloud alpha artifacts docker tags add` `[DOCKER_IMAGE](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add#DOCKER_IMAGE)` `[DOCKER_TAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add#DOCKER_TAG)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create or update a tag for a container image in Artifact
Registry.
A valid Docker tag has the format of

```
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
```

A valid container image that can be referenced by tag or digest, has the format
of

```
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
```

**EXAMPLES**

: To add tag `my-tag` to image `busy-box` referenced by
digest `abcxyz` in `us-west1`:

```
gcloud alpha artifacts docker tags add us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To add tag `my-tag` to image `busy-box` referenced by tag
`latest` in `us-west1`:

```
gcloud alpha artifacts docker tags add us-west1-docker.pkg.dev/my-project/my-repository/busy-box:latest us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

**POSITIONAL ARGUMENTS**

: **`DOCKER_IMAGE`**:
Docker image - The container image that you want to tag.
A valid container image can be referenced by tag or digest, has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

**`DOCKER_TAG`**:
Image tag - The container image tag.
A valid Docker tag has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag

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
gcloud artifacts docker tags add
```

```
gcloud beta artifacts docker tags add
```