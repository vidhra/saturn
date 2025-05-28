# gcloud logging sinks create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create)*

**NAME**

: **gcloud logging sinks create - create a log sink**

**SYNOPSIS**

: **`gcloud logging sinks create` `[SINK_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#SINK_NAME)` `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#DESTINATION)` [`[--custom-writer-identity](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--custom-writer-identity)`=`SERVICE_ACCOUNT_EMAIL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--disabled)`] [`[--exclusion](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--exclusion)`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]] [`[--include-children](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--include-children)`] [`[--intercept-children](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--intercept-children)`] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--log-filter)`=`LOG_FILTER`] [`[--use-partitioned-tables](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--use-partitioned-tables)`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a log sink used to route log entries to a destination. The sink routes
all log entries that match its `--log-filter` flag.
An empty filter matches all logs.
Detailed information about filters can be found at: [https://cloud.google.com/logging/docs/view/logging-query-language](https://cloud.google.com/logging/docs/view/logging-query-language)
The sink's destination can be a Cloud Logging log bucket, a Cloud Storage
bucket, a BigQuery dataset, a Cloud Pub/Sub topic, or a Google Cloud project.
The destination must already exist.
If creating a log sink to route logs to a destination outside of Cloud Logging
or to a Cloud Logging log bucket in another project, the log sink's service
account must be granted permission to write to the destination.
For more information about destination permissions, see: [https://cloud.google.com/logging/docs/export/configure_export_v2#dest-auth](https://cloud.google.com/logging/docs/export/configure_export_v2#dest-auth)
Matching log entries are routed to the destination after the sink is created.

**EXAMPLES**

: To route all Google Compute Engine logs to BigQuery, run:

```
gcloud logging sinks create my-bq-sink bigquery.googleapis.com/projects/my-project/datasets/my_dataset --log-filter='resource.type="gce_instance"'
```

To route "syslog" from App Engine Flexible to a Cloud Storage bucket, run:

```
gcloud logging sinks create my-gcs-sink storage.googleapis.com/my-bucket --log-filter='logName="projects/my-project/appengine.googleapis.com%2Fsyslog"'
```

To route Google App Engine logs with ERROR severity, run:

```
gcloud logging sinks create my-error-logs bigquery.googleapis.com/projects/my-project/datasets/my_dataset --log-filter='resource.type="gae_app" AND severity=ERROR'
```

To route all logs to a log bucket in a different project, run:

```
gcloud logging sinks create my-sink logging.googleapis.com/projects/my-central-project/locations/global/buckets/my-central-bucket
```

To route all logs to another project, run:

```
gcloud logging sinks create my-sink logging.googleapis.com/projects/my-destination-project
```

**POSITIONAL ARGUMENTS**

: **`SINK_NAME`**:
The name for the sink.

**`DESTINATION`**:
The destination for the sink.

**FLAGS**

: **--custom-writer-identity**:
Writer identity for the sink. This flag can only be used if the destination is a
log bucket in a different project. The writer identity is automatically
generated when it is not provided for a sink.

**--description**:
Description of the sink.

**--disabled**:
Sink will be disabled. Disabled sinks do not export logs.

**--exclusion**:
Specify an exclusion filter for a log entry that is not to be exported. This
flag can be repeated.
The ``name`` and
``filter`` attributes are required. The
following keys are accepted:

**`name`**:
An identifier, such as
``load-balancer-exclusion``. Identifiers are
limited to 100 characters and can include only letters, digits, underscores,
hyphens, and periods.

**`description`**:
A description of this exclusion.

**`filter`**:
An advanced log filter that matches the log entries to be excluded.

**`disabled`**:
If this exclusion should be disabled and not exclude the log entries.

**--include-children**:
Whether to export logs from all child projects and folders. Only applies to
sinks for organizations and folders.

**--intercept-children**:
Whether to intercept logs from all child projects and folders. Only applies to
sinks for organizations and folders.

**--log-filter**:
A filter expression for the sink. If present, the filter specifies which log
entries to export.

**--use-partitioned-tables**

**--billing-account**

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
gcloud alpha logging sinks create
```

```
gcloud beta logging sinks create
```