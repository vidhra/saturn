# gcloud compute project-zonal-metadata describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/describe](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/describe)*

**NAME**

: **gcloud compute project-zonal-metadata describe - describe project zonal metadata**

**SYNOPSIS**

: **`gcloud compute project-zonal-metadata describe` `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/describe#--zone)`=`ZONE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/project-zonal-metadata/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe project zonal metadata.

**EXAMPLES**

: To describe the project zonal metadata in the zone
``us-central1-a`` for the project
``my-gcp-project``, run:

```
gcloud compute project-zonal-metadata describe --zone=us-central1-a --project=my-gcp-project
```

**REQUIRED FLAGS**

: **--zone**:
Zone for project zonal metadata

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
gcloud alpha compute project-zonal-metadata describe
```

```
gcloud beta compute project-zonal-metadata describe
```