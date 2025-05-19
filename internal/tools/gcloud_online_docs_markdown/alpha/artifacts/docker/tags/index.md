# gcloud alpha artifacts docker tags  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags)*

**NAME**

: **gcloud alpha artifacts docker tags - manage Artifact Registry container image tags**

**SYNOPSIS**

: **`gcloud alpha artifacts docker tags` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` To add tag `my-tag` to image
`busy-box` referenced by digest `abcxyz` in
`us-west1`:

```
gcloud alpha artifacts docker tags add us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To add tag `my-tag` to image `busy-box` referenced by tag
`latest` in `us-west1`:

```
gcloud alpha artifacts docker tags add us-west1-docker.pkg.dev/my-project/my-repository/busy-box:latest us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To delete tag `my-tag` from image `busy-box` in
`us-west1`:

```
gcloud alpha artifacts docker tags delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To list all tags in repository `my-repository` in
`us-west1`:

```
gcloud alpha artifacts docker tags list us-west1-docker.pkg.dev/my-project/my-repository
```

To list tags for image `busy-box` in `us-west1`:

```
gcloud alpha artifacts docker tags list us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add)`**:
`(ALPHA)` Add a tag to a container image in Artifact Registry.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/delete)`**:
`(ALPHA)` Delete a tag from a container image in Artifact Registry.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/list)`**:
`(ALPHA)` List all tags associated with a container image in Artifact
Registry.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts docker tags
```

```
gcloud beta artifacts docker tags
```