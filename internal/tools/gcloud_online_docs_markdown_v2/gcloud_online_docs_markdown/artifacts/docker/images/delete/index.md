# gcloud artifacts docker images delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)*

**NAME**

: **gcloud artifacts docker images delete - delete an Artifact Registry container image**

**SYNOPSIS**

: **`gcloud artifacts docker images delete` `[IMAGE](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete#IMAGE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete#--async)`] [`[--delete-tags](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete#--delete-tags)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A valid container image has the format of

```
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE
```

A valid container image that can be referenced by tag or digest, has the format
of

```
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest
```

This command can fail for the following reasons:

- Trying to delete an image by digest when the image is still tagged. Add
--delete-tags to delete the digest and the tags.
- Trying to delete an image by tag when the image has other tags. Add
--delete-tags to delete all tags.
- A valid repository format was not provided.
- The specified image does not exist.
- The active account does not have permission to delete images.

**EXAMPLES**

: To delete image `busy-box` in `us-west1` and all of its
digests and tags:

```
gcloud artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box
```

To delete image digest `abcxyz` under image `busy-box`:

```
gcloud artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
```

To delete image digest `abcxyz` under image `busy-box`
while there're other tags associate with the digest:

```
gcloud artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --delete-tags
```

To delete an image digest and its only tag `my-tag` under image
`busy-box`:

```
gcloud artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag
```

**POSITIONAL ARGUMENTS**

: **`IMAGE`**:
A container image.
A valid container image has the format of
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE
A valid container image that can be referenced by tag or digest, has the format
of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--delete-tags**:
If specified, all tags associated with the image are deleted.

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
gcloud alpha artifacts docker images delete
```

```
gcloud beta artifacts docker images delete
```