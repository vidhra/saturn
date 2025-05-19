# gcloud app versions delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/versions/delete](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete)*

**NAME**

: **gcloud app versions delete - delete a specified version**

**SYNOPSIS**

: **`gcloud app versions delete` `[VERSIONS](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete#VERSIONS)` [`[VERSIONS](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete#VERSIONS)` …] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete#SERVICE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/versions/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: You cannot delete a version of a service that is currently receiving traffic.

**EXAMPLES**

: To delete a specific version of a specific service, run:

```
gcloud app versions delete --service=myService v1
```

To delete a named version across all services, run:

```
gcloud app versions delete v1
```

To delete multiple versions of a specific service, run:

```
gcloud app versions delete --service=myService v1 v2
```

To delete multiple named versions across all services, run:

```
gcloud app versions delete v1 v2
```

**POSITIONAL ARGUMENTS**

: **`VERSIONS` [`VERSIONS` …]**:
The versions to delete (optionally filtered by the --service flag).

**FLAGS**

: **--service**:
If specified, only delete versions from the given service.

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
gcloud beta app versions delete
```