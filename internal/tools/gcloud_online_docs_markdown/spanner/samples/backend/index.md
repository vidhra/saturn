# gcloud spanner samples backend  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend)*

**NAME**

: **gcloud spanner samples backend - run the backend gRPC service for the given Cloud Spanner sample app**

**SYNOPSIS**

: **`gcloud spanner samples backend` `[APPNAME](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend#APPNAME)` `[--instance-id](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend#--instance-id)`=`INSTANCE_ID` [`[--database-id](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend#--database-id)`=`DATABASE_ID`] [`[--duration](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend#--duration)`=`DURATION`; default="1h"] [`[--port](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend#--port)`=`PORT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/backend#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command starts the backend gRPC service for the given sample application.
Before starting the service, create the database and load any initial data with:

```
gcloud spanner samples init APPNAME --instance-id=INSTANCE_ID
```

After starting the service, generate traffic with:

```
gcloud spanner samples workload APPNAME
```

To run all three steps together, use:

```
gcloud spanner samples run APPNAME --instance-id=INSTANCE_ID
```

**EXAMPLES**

: To run the backend gRPC service for the 'finance' sample app using instance
'my-instance', run:

```
gcloud spanner samples backend finance --instance-id=my-instance
```

**POSITIONAL ARGUMENTS**

: **`APPNAME`**:
The sample app name, e.g. "finance".

**REQUIRED FLAGS**

: **--instance-id**:
The Cloud Spanner instance ID for the sample app.

**OPTIONAL FLAGS**

: **--database-id**:
The Cloud Spanner database ID for the sample app.

**--duration**:
Duration of time allowed to run before stopping the service.

**--port**:
Port on which to receive gRPC requests.

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
gcloud alpha spanner samples backend
```

```
gcloud beta spanner samples backend
```