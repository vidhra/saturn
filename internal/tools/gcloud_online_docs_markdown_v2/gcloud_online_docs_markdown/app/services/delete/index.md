# gcloud app services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/services/delete](https://cloud.google.com/sdk/gcloud/reference/app/services/delete)*

**NAME**

: **gcloud app services delete - delete services in the current project**

**SYNOPSIS**

: **`gcloud app services delete` `[SERVICES](https://cloud.google.com/sdk/gcloud/reference/app/services/delete#SERVICES)` [`[SERVICES](https://cloud.google.com/sdk/gcloud/reference/app/services/delete#SERVICES)` …] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/services/delete#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete services in the current project.

**EXAMPLES**

: To delete a service (and all of its accompanying versions) in the current
project, run:

```
gcloud app services delete service1
```

To delete multiple services (and all of their accompanying versions) in the
current project, run:

```
gcloud app services delete service1 service2
```

**POSITIONAL ARGUMENTS**

: **`SERVICES` [`SERVICES` …]**:
The service(s) to delete.

**FLAGS**

: **--version**:
Delete a specific version of the given service(s).

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
gcloud beta app services delete
```