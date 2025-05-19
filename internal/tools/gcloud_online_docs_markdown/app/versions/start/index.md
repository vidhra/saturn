# gcloud app versions start  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/versions/start](https://cloud.google.com/sdk/gcloud/reference/app/versions/start)*

**NAME**

: **gcloud app versions start - start serving specified versions**

**SYNOPSIS**

: **`gcloud app versions start` `[VERSIONS](https://cloud.google.com/sdk/gcloud/reference/app/versions/start#VERSIONS)` [`[VERSIONS](https://cloud.google.com/sdk/gcloud/reference/app/versions/start#VERSIONS)` …] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/versions/start#--service)`=`SERVICE`, `[-s](https://cloud.google.com/sdk/gcloud/reference/app/versions/start#-s)` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/app/versions/start#SERVICE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/versions/start#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command starts serving the specified versions. It may only be used if the
scaling module for your service has been set to manual.

**EXAMPLES**

: To start a specific version across all services, run:

```
gcloud app versions start v1
```

To start multiple named versions across all services, run:

```
gcloud app versions start v1 v2
```

To start a single version on a single service, run:

```
gcloud app versions start --service=servicename v1
```

To start multiple versions in a single service, run:

```
gcloud app versions start --service=servicename v1 v2
```

**POSITIONAL ARGUMENTS**

: **`VERSIONS` [`VERSIONS` …]**:
The versions to start. (optionally filtered by the --service flag).

**FLAGS**

: **--service**:
If specified, only start versions from the given service.

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
gcloud beta app versions start
```