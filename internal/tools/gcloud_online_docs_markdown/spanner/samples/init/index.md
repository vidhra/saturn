# gcloud spanner samples init  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/samples/init](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/init)*

**NAME**

: **gcloud spanner samples init - initialize a Cloud Spanner sample app**

**SYNOPSIS**

: **`gcloud spanner samples init` `[APPNAME](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/init#APPNAME)` `[--instance-id](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/init#--instance-id)`=`INSTANCE_ID` [`[--database-id](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/init#--database-id)`=`DATABASE_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/samples/init#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a Cloud Spanner database in the given instance for the
sample app and loads any initial data required by the application.

**EXAMPLES**

: To initialize the 'finance' sample app using instance 'my-instance', run:

```
gcloud spanner samples init finance --instance-id=my-instance
```

To initialize the 'finance-graph' sample app using instance 'my-instance', run:

```
gcloud spanner samples init finance-graph --instance-id=my-instance
```

**POSITIONAL ARGUMENTS**

: **`APPNAME`**:
The sample app name, e.g. "finance", "finance-graph".

**REQUIRED FLAGS**

: **--instance-id**:
The Cloud Spanner instance ID for the sample app.

**OPTIONAL FLAGS**

: **--database-id**:
ID of the new Cloud Spanner database to create for the sample app.

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
gcloud alpha spanner samples init
```

```
gcloud beta spanner samples init
```