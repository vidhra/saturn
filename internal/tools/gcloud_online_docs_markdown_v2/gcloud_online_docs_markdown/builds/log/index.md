# gcloud builds log  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/log](https://cloud.google.com/sdk/gcloud/reference/builds/log)*

**NAME**

: **gcloud builds log - stream the logs for a build**

**SYNOPSIS**

: **`gcloud builds log` `[BUILD](https://cloud.google.com/sdk/gcloud/reference/builds/log#BUILD)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/builds/log#--region)`=`REGION`] [`[--stream](https://cloud.google.com/sdk/gcloud/reference/builds/log#--stream)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/log#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Stream the logs for a build.

**EXAMPLES**

: To stream logs for in progress build `123-456-789`:

```
gcloud builds log --stream `123-456-789`
```

To display logs for a completed build `098-765-432`:

```
gcloud builds log `098-765-432`
```

**POSITIONAL ARGUMENTS**

: **`BUILD`**:
The build whose logs shall be printed. The ID of the build is printed at the end
of the build submission process, or in the ID column when listing builds.

**FLAGS**

: **--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

**--stream**:
If a build is ongoing, stream the logs to stdout until the build completes.

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
gcloud alpha builds log
```

```
gcloud beta builds log
```