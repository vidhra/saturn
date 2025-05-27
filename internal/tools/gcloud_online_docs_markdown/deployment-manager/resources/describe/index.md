# gcloud deployment-manager resources describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/describe](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/describe)*

**NAME**

: **gcloud deployment-manager resources describe - provide information about a resource**

**SYNOPSIS**

: **`gcloud deployment-manager resources describe` `[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/describe#RESOURCE)` [`[--deployment](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/describe#--deployment)`=`DEPLOYMENT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/resources/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command prints out all available details about a resource.

**EXAMPLES**

: To display information about a resource, run:

```
gcloud deployment-manager resources describe --deployment=my-deployment my-resource-name
```

**POSITIONAL ARGUMENTS**

: **`RESOURCE`**:
Resource name.

**FLAGS**

: **--deployment**:
Deployment name

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
gcloud alpha deployment-manager resources describe
```

```
gcloud beta deployment-manager resources describe
```