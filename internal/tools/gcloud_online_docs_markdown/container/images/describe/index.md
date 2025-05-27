# gcloud container images describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/images/describe](https://cloud.google.com/sdk/gcloud/reference/container/images/describe)*

**NAME**

: **gcloud container images describe - lists information about the specified image**

**SYNOPSIS**

: **`gcloud container images describe` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/images/describe#IMAGE_NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/images/describe#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: Describe the specified image:

```
gcloud container images describe gcr.io/myproject/myimage@digest
```

```
Or:
```

```
gcloud container images describe gcr.io/myproject/myimage:tag
```

Find the digest for a tag:

```
gcloud container images describe gcr.io/myproject/myimage:tag --format="value(image_summary.digest)"
```

```
Or:
```

```
gcloud container images describe gcr.io/myproject/myimage:tag --format="value(image_summary.fully_qualified_digest)"
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME`**:
The fully qualified name(s) of image(s) to describe. The name(s) should be
formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH@sha256:DIGEST or
*.gcr.io/PROJECT_ID/IMAGE_PATH:TAG.

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
gcloud alpha container images describe
```

```
gcloud beta container images describe
```