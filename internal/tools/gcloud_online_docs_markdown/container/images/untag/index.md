# gcloud container images untag  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/images/untag](https://cloud.google.com/sdk/gcloud/reference/container/images/untag)*

**NAME**

: **gcloud container images untag - remove existing image tags**

**SYNOPSIS**

: **`gcloud container images untag` `[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/images/untag#IMAGE_NAME)` [`[IMAGE_NAME](https://cloud.google.com/sdk/gcloud/reference/container/images/untag#IMAGE_NAME)` …] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/images/untag#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The container images untag command removes the specified tag from the image.

**EXAMPLES**

: Removes the tag from the input IMAGE_NAME:

```
gcloud container images untag <IMAGE_NAME>
```

**POSITIONAL ARGUMENTS**

: **`IMAGE_NAME` [`IMAGE_NAME` …]**:
The fully qualified name(s) of image(s) to untag. The name(s) should be
formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH:TAG.

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
gcloud alpha container images untag
```

```
gcloud beta container images untag
```