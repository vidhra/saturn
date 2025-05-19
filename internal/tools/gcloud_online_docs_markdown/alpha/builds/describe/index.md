# gcloud alpha builds describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/describe)*

**NAME**

: **gcloud alpha builds describe - get information about a particular build**

**SYNOPSIS**

: **`gcloud alpha builds describe` `[BUILD](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/describe#BUILD)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Get information about a particular build.

**EXAMPLES**

: To describe a build `123-456-789`:

```
gcloud alpha builds describe '123-456-789'
```

**POSITIONAL ARGUMENTS**

: **`BUILD`**:
The build to describe. The ID of the build is printed at the end of the build
submission process, or in the ID column when listing builds.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds describe
```

```
gcloud beta builds describe
```