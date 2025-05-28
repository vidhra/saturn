# gcloud artifacts docker  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker)*

**NAME**

: **gcloud artifacts docker - manage Artifact Registry container images and tags**

**SYNOPSIS**

: **`gcloud artifacts docker` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker#GROUP)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To list images under repository `my-repo`, project
`my-project`, in `us-central1`:

```
gcloud artifacts docker images list us-central1-docker.pkg.dev/my-project/my-repo
```

To delete image `busy-box` in `us-west1` and all of its
digests and tags:

```
gcloud artifacts docker images delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

To add tag `my-tag` to image `busy-box` referenced by
digest `abcxyz` in `us-west1`:

```
gcloud artifacts docker tags add
us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To delete tag `my-tag` from image `busy-box` in
`us-west1`:

```
gcloud artifacts docker tags delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

To list tags for image `busy-box` in `us-west1`:

```
gcloud artifacts docker tags list
us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[images](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images)`**:
Manage Artifact Registry container images.

**`[tags](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags)`**:
Manage Artifact Registry container image tags.

**`[upgrade](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade)`**:
Commands to support Container Registry to Artifact Registry upgrade.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts docker
```

```
gcloud beta artifacts docker
```