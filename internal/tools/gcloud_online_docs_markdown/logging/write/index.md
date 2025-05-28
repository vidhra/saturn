# gcloud logging write  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/write](https://cloud.google.com/sdk/gcloud/reference/logging/write)*

**NAME**

: **gcloud logging write - write a log entry**

**SYNOPSIS**

: **`gcloud logging write` `[LOG_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/write#LOG_NAME)` `[MESSAGE](https://cloud.google.com/sdk/gcloud/reference/logging/write#MESSAGE)` [`[--monitored-resource-labels](https://cloud.google.com/sdk/gcloud/reference/logging/write#--monitored-resource-labels)`=[`KEY`=`VALUE`, …,…]] [`[--monitored-resource-type](https://cloud.google.com/sdk/gcloud/reference/logging/write#--monitored-resource-type)`=`MONITORED_RESOURCE_TYPE`; default="global"] [`[--payload-type](https://cloud.google.com/sdk/gcloud/reference/logging/write#--payload-type)`=`PAYLOAD_TYPE`; default="text"] [`[--severity](https://cloud.google.com/sdk/gcloud/reference/logging/write#--severity)`=`SEVERITY`; default="DEFAULT"] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/write#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/write#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/write#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/write#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/write#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Write a log entry. If the destination log does not exist, it will be created. By
default, all log entries written with this command are written with the "global"
resource type.
gcloud logging write should be used for simple testing purposes. Check Cloud
Logging agent for a proper way to send log entries: [https://cloud.google.com/logging/docs/agent/](https://cloud.google.com/logging/docs/agent/)

**EXAMPLES**

: To create a log entry in a given log, run:

```
gcloud logging write LOG_NAME "A simple entry"
```

To create a high severity log entry, run:

```
gcloud logging write LOG_NAME "Urgent message" --severity=ALERT
```

To create a structured log, run:

```
gcloud logging write LOG_NAME '{"key": "value"}' --payload-type=json
```

To create a log entry with a custom resource type, run:

```
gcloud logging write LOG_NAME "A simple entry" --monitored-resource-type=gce_instance --monitored-resource-labels=zone=us-centra1-a,instance_id=1234
```

**POSITIONAL ARGUMENTS**

: **`LOG_NAME`**:
Name of the log where the log entry will be written.

**`MESSAGE`**:
Message to put in the log entry. It can be JSON if you include
`--payload-type=json`.

**FLAGS**

: **--monitored-resource-labels**:
Monitored Resource labels to add to the payload

**--monitored-resource-type**:
Monitored Resource type to add to the payload

**--payload-type**:
Type of the log entry payload. `PAYLOAD_TYPE` must be one
of: `text`, `json`.

**--severity**:
Severity level of the log entry. `SEVERITY` must be one
of: `DEFAULT`, `DEBUG`, `INFO`,
`NOTICE`, `WARNING`, `ERROR`,
`CRITICAL`, `ALERT`, `EMERGENCY`.

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
gcloud alpha logging write
```

```
gcloud beta logging write
```