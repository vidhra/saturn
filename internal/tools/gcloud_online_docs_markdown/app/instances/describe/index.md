# gcloud app instances describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/instances/describe](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe)*

**NAME**

: **gcloud app instances describe - display all data about an existing instance**

**SYNOPSIS**

: **`gcloud app instances describe` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#INSTANCE)` `[--service](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#SERVICE)` `[--version](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#VERSION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display all data about an existing instance.

**EXAMPLES**

: To show all data about instance i1 for service s1 and version v1, run:

```
gcloud app instances describe --service=s1 --version=v1 i1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
The instance ID.

**REQUIRED FLAGS**

: **--service**:
The service ID.

**--version**:
The version ID.

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

: This variant is also available:

```
gcloud beta app instances describe
```