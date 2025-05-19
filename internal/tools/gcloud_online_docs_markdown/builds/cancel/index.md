# gcloud builds cancel  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/cancel](https://cloud.google.com/sdk/gcloud/reference/builds/cancel)*

**NAME**

: **gcloud builds cancel - cancel an ongoing build**

**SYNOPSIS**

: **`gcloud builds cancel` `[BUILDS](https://cloud.google.com/sdk/gcloud/reference/builds/cancel#BUILDS)` [`[BUILDS](https://cloud.google.com/sdk/gcloud/reference/builds/cancel#BUILDS)` …] [`[--region](https://cloud.google.com/sdk/gcloud/reference/builds/cancel#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/cancel#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Cancel an ongoing build.

**EXAMPLES**

: To cancel a build `123-456-789`:

```
gcloud builds cancel '123-456-789'
```

You may also cancel multiple builds at the same time:

```
gcloud builds cancel '123-456-789', '987-654-321'
```

**POSITIONAL ARGUMENTS**

: **`BUILDS` [`BUILDS` …]**:
IDs of builds to cancel

**FLAGS**

: **--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

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
gcloud alpha builds cancel
```

```
gcloud beta builds cancel
```