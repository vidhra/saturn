# gcloud app instances delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/instances/delete](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete)*

**NAME**

: **gcloud app instances delete - delete a specified instance**

**SYNOPSIS**

: **`gcloud app instances delete` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#INSTANCE)` `[--service](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#SERVICE)` `[--version](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#--version)`=`VERSION`, `[-v](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#-v)` `[VERSION](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#VERSION)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a specified instance.

**EXAMPLES**

: To delete instance i1 of service s1 and version v1, run:

```
gcloud app instances delete i1 --service=s1 --version=v1
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
gcloud beta app instances delete
```