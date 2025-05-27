# gcloud container images delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/images/delete](https://cloud.google.com/sdk/gcloud/reference/container/images/delete)*

**NAME**

: **gcloud container images delete - delete existing images**

**SYNOPSIS**

: **`gcloud container images delete` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/images/delete#IMAGE_NAME)` [`[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/images/delete#IMAGE_NAME)` …] [`[--force-delete-tags](https://cloud.google.com/sdk/gcloud/reference/container/images/delete#--force-delete-tags)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/images/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The container images delete command deletes the specified image from the
registry. All associated tags are also deleted.

**EXAMPLES**

: Deletes the image as long as there aren't additional, unspecified tags
referencing it:

```
gcloud container images delete <IMAGE_NAME>
```

Deletes the image (and tags) from the input IMAGE_NAME:

```
gcloud container images delete <IMAGE_NAME> --force-delete-tags
```

Deletes the image (and tags) from the input IMAGE_NAME, without additional
prompting:

```
gcloud container images delete <IMAGE_NAME> --force-delete-tags --quiet
```

To easily identify and delete untagged images in a project, first filter digests
that lack tags:

```
gcloud container images list-tags [HOSTNAME]/[PROJECT-ID]/[IMAGE] --filter='-tags:*' --format="get(digest)" --limit=$BIG_NUMBER
```

Then, delete these tagless images without prompting by running:

```
gcloud container images delete [HOSTNAME]/[PROJECT-ID]/[IMAGE]@DIGEST --quiet
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME` [`IMAGE_NAME` …]**:
The fully qualified name(s) of image(s) to delete. The name(s) should be
formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH@sha256:DIGEST or
*.gcr.io/PROJECT_ID/IMAGE_PATH:TAG.

**FLAGS**

: **--force-delete-tags**:
If there are tags pointing to an image to be deleted then they must all be
specified explicitly, or this flag must be specified, for the command to
succeed.

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
gcloud alpha container images delete
```

```
gcloud beta container images delete
```