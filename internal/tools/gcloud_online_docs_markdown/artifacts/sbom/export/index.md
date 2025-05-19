# gcloud artifacts sbom export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export)*

**NAME**

: **gcloud artifacts sbom export - export SBOM files to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud artifacts sbom export` `[--uri](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export#--uri)`=`URI` [`[--location](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/sbom/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export SBOM files to Google Cloud Storage.

**EXAMPLES**

: To export an SBOM file for the Artifact Registry image with URI
"us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz":

```
gcloud artifacts sbom export --uri=us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
```

**REQUIRED FLAGS**

: **--uri**:
The URI of the Artifact Registry image the SBOM is exported for. A 'gcr.io'
image can also be used if redirection is enabled in Artifact Registry. Make sure
'artifactregistry.projectsettings.get' permission is granted to the current
gcloud user to verify the redirection status.

**OPTIONAL FLAGS**

: **--location**:
If specified, all requests to Artifact Analysis for occurrences will go to
location specified

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