# gcloud container images add-tag  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/images/add-tag](https://cloud.google.com/sdk/gcloud/reference/container/images/add-tag)*

**NAME**

: **gcloud container images add-tag - adds tags to existing image**

**SYNOPSIS**

: **`gcloud container images add-tag` `[SRC_IMAGE](https://cloud.google.com/sdk/gcloud/reference/container/images/add-tag#SRC_IMAGE)` `[DEST_IMAGE](https://cloud.google.com/sdk/gcloud/reference/container/images/add-tag#DEST_IMAGE)` [`[DEST_IMAGE](https://cloud.google.com/sdk/gcloud/reference/container/images/add-tag#DEST_IMAGE)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/images/add-tag#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The container images add-tag command adds the tag(s) specified in the second
(and following) tag parameter(s) to the image referenced in the first tag
parameter. Repositories must be hosted by the Google Container Registry.

**EXAMPLES**

: Add a tag to another tag:

```
gcloud container images add-tag gcr.io/myproject/myimage:mytag1 gcr.io/myproject/myimage:mytag2
```

Add a tag to a digest

```
gcloud container images add-tag gcr.io/myproject/myimage@sha256:digest gcr.io/myproject/myimage:mytag2
```

Add a tag to latest

```
gcloud container images add-tag gcr.io/myproject/myimage gcr.io/myproject/myimage:mytag2
```

Promote a tag to latest

```
gcloud container images add-tag gcr.io/myproject/myimage:mytag1 gcr.io/myproject/myimage:latest
```

**POSITIONAL ARGUMENTS**

: **`SRC_IMAGE`**:
The fully qualified name(s) of image(s) to add tags for. The name(s) should be
formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH@sha256:DIGEST or
*.gcr.io/PROJECT_ID/IMAGE_PATH:TAG.

**`DEST_IMAGE` [`DEST_IMAGE` …]**:
The fully qualified name(s) of image(s) to be the new tags. The name(s) should
be formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH:TAG.

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
gcloud alpha container images add-tag
```

```
gcloud beta container images add-tag
```