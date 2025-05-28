# gcloud spanner samples run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run)*

**NAME**

: **gcloud spanner samples run - run the given Cloud Spanner sample app**

**SYNOPSIS**

: **`gcloud spanner samples run` `[APPNAME](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#APPNAME)` `[--instance-id](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#--instance-id)`=`INSTANCE_ID` [`[--no-cleanup](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#--cleanup)`] [`[--database-id](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#--database-id)`=`DATABASE_ID`] [`[--duration](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#--duration)`=`DURATION`; default="1h"] [`[--skip-init](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#--skip-init)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Each Cloud Spanner sample application includes a backend gRPC service backed by
a Cloud Spanner database and a workload script that generates service traffic.
This command creates and initializes the Cloud Spanner database and runs both
the backend service and workload script.
These sample apps are open source and available at [https://github.com/GoogleCloudPlatform/cloud-spanner-samples](https://github.com/GoogleCloudPlatform/cloud-spanner-samples).
To see a list of available sample apps, run:

```
gcloud spanner samples list
```

**EXAMPLES**

: To run the 'finance' sample app using instance 'my-instance', run:

```
gcloud spanner samples run finance --instance-id=my-instance
```

**POSITIONAL ARGUMENTS**

: **`APPNAME`**:
The sample app name, e.g. "finance".

**REQUIRED FLAGS**

: **--instance-id**:
The Cloud Spanner instance ID for the sample app.

**OPTIONAL FLAGS**

: **--cleanup**:
Delete the instance after running the sample app. Enabled by default, use
`--no-cleanup` to disable.

**--database-id**:
ID of the new Cloud Spanner database to create for the sample app.

**--duration**:
Duration of time allowed to run the sample app before stopping the service.

**--skip-init**:
Use an existing database instead of creating a new one.

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
gcloud alpha spanner samples run
```

```
gcloud beta spanner samples run
```