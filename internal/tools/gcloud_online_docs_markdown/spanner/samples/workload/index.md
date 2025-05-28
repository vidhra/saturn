# gcloud spanner samples workload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload)*

**NAME**

: **gcloud spanner samples workload - generate gRPC traffic for a given sample app's backend service**

**SYNOPSIS**

: **`gcloud spanner samples workload` `[APPNAME](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload#APPNAME)` [`[--duration](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload#--duration)`=`DURATION`; default="1h"] [`[--port](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload#--port)`=`PORT`] [`[--target-qps](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload#--target-qps)`=`TARGET_QPS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/workload#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Before sending traffic to the backend service, create the database and start the
service with:

```
gcloud spanner samples init APPNAME --instance-id=INSTANCE_ID
gcloud spanner samples backend APPNAME --instance-id=INSTANCE_ID
```

To run all three steps together, use:

```
gcloud spanner samples run APPNAME --instance-id=INSTANCE_ID
```

**EXAMPLES**

: To generate traffic for the 'finance' sample app, run:

```
gcloud spanner samples workload finance
```

**POSITIONAL ARGUMENTS**

: **`APPNAME`**:
The sample app name, e.g. "finance".

**FLAGS**

: **--duration**:
Duration of time allowed to run before stopping the workload.

**--port**:
Port of the running backend service.

**--target-qps**:
Target requests per second.

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
gcloud alpha spanner samples workload
```

```
gcloud beta spanner samples workload
```