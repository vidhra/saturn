# gcloud artifacts docker images  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images)*

**NAME**

: **gcloud artifacts docker images - manage Artifact Registry container images**

**SYNOPSIS**

: **`gcloud artifacts docker images` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To list images under the current project, repository, and location:

```
gcloud artifacts docker images list
```

To list images under repository `my-repo`, project
`my-project`, in `us-central1`:

```
gcloud artifacts docker images list us-central1-docker.pkg.dev/my-project/my-repo
```

To list images with tags, under repository `my-repo`, project
`my-project` across all locations:

```
gcloud artifacts docker images list docker.pkg.dev/my-project/my-repo --include-tags
```

To list all images under image `busy-box`, in repository
`my-repo`, project `my-project` across all locations:

```
gcloud artifacts docker images list docker.pkg.dev/my-project/my-repo/busy-box
```

To delete image `busy-box` in `us-west1` and all of its
digests and tags:

```
gcloud artifacts docker images delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

To delete image digest `abcxyz` under image `busy-box`:

```
gcloud artifacts docker images delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
```

To delete image digest `abcxyz` under image `busy-box`
while there're some other tags associate with the digest:

```
gcloud artifacts docker images delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
--delete-tags
```

To delete an image digest and its only tag `my-tag` under image
`busy-box`:

```
gcloud artifacts docker images delete
us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)`**:
Delete an Artifact Registry container image.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/describe)`**:
Describe an Artifact Registry container image.

**`[get-operation](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation)`**:
Get an On-Demand Scanning operation.

**`[list](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list)`**:
List Artifact Registry container images.

**`[list-vulnerabilities](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities)`**:
List On-Demand Scanning vulnerabilities.

**`[scan](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan)`**:
Perform a vulnerability scan on a container image.

**NOTES**

: These variants are also available:

```
gcloud alpha artifacts docker images
```

```
gcloud beta artifacts docker images
```