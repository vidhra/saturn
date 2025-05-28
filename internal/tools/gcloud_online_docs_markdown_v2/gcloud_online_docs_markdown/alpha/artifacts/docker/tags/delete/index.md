# gcloud alpha artifacts docker tags delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/delete)*

**NAME**

: **gcloud alpha artifacts docker tags delete - delete a tag from a container image in Artifact Registry**

**SYNOPSIS**

: **`gcloud alpha artifacts docker tags delete` `[DOCKER_TAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/delete#DOCKER_TAG)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` A valid Docker tag has the format of

```
[<location>-]docker.pkg.dev/PROJECT_ID/REPOSITORY-ID/IMAGE_PATH:tag
```

**EXAMPLES**

: To delete tag `my-tag` from image `busy-box` in
`us-west1`:

```
gcloud alpha artifacts docker tags delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

**POSITIONAL ARGUMENTS**

: **`DOCKER_TAG`**:
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
gcloud artifacts docker tags delete
```

```
gcloud beta artifacts docker tags delete
```