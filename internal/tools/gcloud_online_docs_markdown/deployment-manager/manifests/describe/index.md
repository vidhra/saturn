# gcloud deployment-manager manifests describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/describe](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/describe)*

**NAME**

: **gcloud deployment-manager manifests describe - provide information about a manifest**

**SYNOPSIS**

: **`gcloud deployment-manager manifests describe` [`[MANIFEST](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/describe#MANIFEST)`] `[--deployment](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/describe#--deployment)`=`DEPLOYMENT` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/manifests/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command prints out all available details about a manifest.

**EXAMPLES**

: To display information about a manifest, run:

```
gcloud deployment-manager manifests describe --deployment=my-deployment manifest-name
```

To display information about the latest manifest, run:

```
gcloud deployment-manager manifests describe --deployment=my-deployment
```

**POSITIONAL ARGUMENTS**

: **[`MANIFEST`]**:
Manifest name.

**REQUIRED FLAGS**

: **--deployment**:
Deployment name.

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
gcloud alpha deployment-manager manifests describe
```

```
gcloud beta deployment-manager manifests describe
```