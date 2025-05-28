# gcloud scc notifications create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create)*

**NAME**

: **gcloud scc notifications create - create a Security Command Center notification config**

**SYNOPSIS**

: **`gcloud scc notifications create` `[NOTIFICATION_CONFIG_ID](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#NOTIFICATION_CONFIG_ID)` `[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--pubsub-topic)`=`PUBSUB_TOPIC` [`[--description](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--description)`=`DESCRIPTION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--filter)`=`FILTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--location)`=`LOCATION`; default="global"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Security Command Center notification config.
Notification configs that are created with Security Command Center API V2 and
later include a `location` attribute. If a location is not specified,
the default `global` location is used. For example, the following
Notification config name has `location=global` attribute:
`organizations/123/locations/global/notificationConfigs/my-config`.

**EXAMPLES**

: Create a notification config test-config under organization 123 for findings for
pubsub-topic projects/test-project/topics/notification-test with a filter on
resource name:

```
gcloud scc notifications create test-config --organization=123 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\""
```

Create a notification config `test-config` under folder
`456` for findings for pubsub-topic
`projects/test-project/topics/notification-test` with a filter on
resource name:

```
gcloud scc notifications create test-config --folder=456 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\""
```

Create a notification config `test-config` under project
`789` for findings for pubsub-topic
`projects/test-project/topics/notification-test` with a filter on
resource name:

```
gcloud scc notifications create test-config --project=789 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\""
```

Create a notification config `test-config` under organization
`123` for findings for `pubsub-topic
projects/test-project/topics/notification-test` with a filter on resource
name and `location=eu`

```
gcloud scc notifications create test-config --project=789 --pubsub-topic=projects/test-project/topics/notification-test --filter="resource_name: \"a\"" --location=eu
```

**POSITIONAL ARGUMENTS**

: **`NOTIFICATION_CONFIG_ID`**:
The ID of the notification config. Formatted as
"organizations/123/notificationConfigs/456" or just "456".

**REQUIRED FLAGS**

: **--pubsub-topic**:
The Pub/Sub topic which will receive notifications. Its format is
"projects/[project_id]/topics/[topic]".

**OPTIONAL FLAGS**

: **--description**:
The text that will be used to describe a notification configuration.

**--filter**:
Filter to be used for notification config.

**--location**:
If data residency is enabled, specify the Security Command Center location in
which to create the notification. The resulting `notificationConfig`
resource is stored only in this location. Only findings that are issued in this
location are sent to Pub/Sub.
If data residency is not enabled, specifying the `--location` flag
creates the notification by using Security Command Center API v2, and the only
valid value for the flag is `global`.

**--folder**

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

**API REFERENCE**

: This command uses the Security Command Center API. For more information, see [Security
Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)

**NOTES**

: These variants are also available:

```
gcloud alpha scc notifications create
```

```
gcloud beta scc notifications create
```