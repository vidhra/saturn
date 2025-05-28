# gcloud logging sinks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update)*

**NAME**

: **gcloud logging sinks update - update a sink**

**SYNOPSIS**

: **`gcloud logging sinks update` `[SINK_NAME](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#SINK_NAME)` [`[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#DESTINATION)`] [`[--add-exclusion](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--add-exclusion)`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]] [`[--clear-exclusions](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--clear-exclusions)`] [`[--custom-writer-identity](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--custom-writer-identity)`=`SERVICE_ACCOUNT_EMAIL`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--disabled)`] [`[--include-children](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--include-children)`] [`[--intercept-children](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--intercept-children)`] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--log-filter)`=`LOG_FILTER`] [`[--remove-exclusions](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--remove-exclusions)`=[`EXCLUSION` `[ID](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#ID)`,…]] [`[--update-exclusion](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--update-exclusion)`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]] [`[--use-partitioned-tables](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--use-partitioned-tables)`] [`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--billing-account)`=`BILLING_ACCOUNT_ID`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#--project)`=`PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/logging/sinks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Change the `[DESTINATION]` or `--log-filter` associated
with a sink. The new destination must already exist and Cloud Logging must have
permission to write to it.
Log entries are exported to the new destination immediately.

**EXAMPLES**

: To only update a sink filter, run:

```
gcloud logging sinks update my-sink --log-filter='severity>=ERROR'
```

Detailed information about filters can be found at: [https://cloud.google.com/logging/docs/view/logging-query-language](https://cloud.google.com/logging/docs/view/logging-query-language)

**POSITIONAL ARGUMENTS**

: **`SINK_NAME`**:
The name of the sink to update.

**[`DESTINATION`]**:
A new destination for the sink. If omitted, the sink's existing destination is
unchanged.

**FLAGS**

: **--add-exclusion**:
Add an exclusion filter for log entries that are not to be routed to the sink'
destination. This flag can be repeated.
The ``name`` and
``filter`` attributes are required. The
following keys are accepted:

**`name`**:
Required. An identifier, such as
``load-balancer-exclusion``. Identifiers are
limited to 100 characters and can include only letters, digits, underscores,
hyphens, and periods.

**`description`**:
Optional. A description of this exclusion.

**`filter`**:
Required. Entries that match this advanced log filter will be excluded. Filter
cannot be empty.

**`disabled`**:
Optional. By default, an exclusion is not disabled. To disable an exclusion,
include this key and specify any value.

**--clear-exclusions**:
Remove all logging exclusions from the sink.

**--custom-writer-identity**:
Writer identity for the sink. This flag can only be used if the destination is a
log bucket in a different project. The writer identity is automatically
generated when it is not provided for a sink.

**--description**:
Description of the sink.

**--disabled**:
Disable the sink. Disabled sinks do not route logs to the sink destination.
Specify --no-disabled to enable a disabled sink. If this flag is not specified,
the value will not be updated.

**--include-children**:
Whether to export logs from all child projects and folders. Only applies to
sinks for organizations and folders.

**--intercept-children**:
Whether to intercept logs from all child projects and folders. Only applies to
sinks for organizations and folders.

**--log-filter**:
A new filter expression for the sink. If omitted, the sink's existing filter (if
any) is unchanged.

**--remove-exclusions**:
Specify the name of the Logging exclusion(s) to delete.

**--update-exclusion**:
Update an exclusion filter for a log entry that is not to be exported. This flag
can be repeated.
The ``name`` attribute is required. The
following keys are accepted:

**`name`**:
Required. An identifier, such as
``load-balancer-exclusion``. Identifiers are
limited to 100 characters and can include only letters, digits, underscores,
hyphens, and periods.

**`description`**:
Optional. A description of this exclusion.

**`filter`**:
Optional. Entries that match this advanced log filter will be excluded. Filter
cannot be empty.

**`disabled`**:
Optional. To disable an exclusion, include this key and specify any value. To
enable a disabled exclusion, include this key, but do not specify any value. Do
not include this key unless you want to change its value.

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
gcloud alpha logging sinks update
```

```
gcloud beta logging sinks update
```