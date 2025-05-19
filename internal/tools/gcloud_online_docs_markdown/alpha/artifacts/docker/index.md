# gcloud alpha artifacts docker  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker)*

**NAME**

: **gcloud alpha artifacts docker - manage Artifact Registry container images and tags**

**SYNOPSIS**

: **`gcloud alpha artifacts docker` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` To list images under repository `my-repo`,
project `my-project`, in `us-central1`:

```
gcloud alpha artifacts docker images list us-central1-docker.pkg.dev/my-project/my-repo
```

To delete image `busy-box` in `us-west1` and all of its
digests and tags:

```
gcloud alpha artifacts docker images delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

To add tag `my-tag` to image `busy-box` referenced by
digest `abcxyz` in `us-west1`:

```
gcloud alpha artifacts docker tags add
us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To delete tag `my-tag` from image `busy-box` in
`us-west1`:

```
gcloud alpha artifacts docker tags delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To list tags for image `busy-box` in `us-west1`:

```
gcloud alpha artifacts docker tags list
us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[images](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images)`**:
`(ALPHA)` Manage Artifact Registry container images.

**`[tags](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags)`**:
`(ALPHA)` Manage Artifact Registry container image tags.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud artifacts docker
```

```
gcloud beta artifacts docker
```