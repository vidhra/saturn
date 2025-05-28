# gcloud scc notifications update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update)*

**NAME**

: **gcloud scc notifications update - update a Security Command Center notification config**

**SYNOPSIS**

: **`gcloud scc notifications update` `[NOTIFICATION_CONFIG_ID](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#NOTIFICATION_CONFIG_ID)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--description)`=`DESCRIPTION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--filter)`=`FILTER`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--location)`=`LOCATION`; default="global"] [`[--pubsub-topic](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--pubsub-topic)`=`PUBSUB_TOPIC`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Security Command Center notification config.
Notification configs that are created with Security Command Center API V2 and
later include a `location` attribute. If the `location`
attribute is included in the resource name of a Notification configs, you must
specify it when referencing the Notification config. For example, the following
Notification configs name has `location=eu`:
`organizations/123/locations/eu/notificationConfigs/test-config`.

**EXAMPLES**

: Update all mutable fields under an organization parent `test-config`
(description + pubsub topic + filter):

```
gcloud scc notifications update scc notifications update test-config --organization=123 --description="New description" --pubsub-topic="projects/22222/topics/newtopic"
```

Update all mutable fields under a folder parent `test-config`
(description + pubsub topic + filter):

```
gcloud scc notifications update scc notifications update test-config --folder=456 --description="New description" --pubsub-topic="projects/22222/topics/newtopic"
```

Update all mutable fields under a project parent `test-config`
(description + pubsub topic + filter):

```
gcloud scc notifications update scc notifications update test-config --project=789 --description="New description" --pubsub-topic="projects/22222/topics/newtopic"
```

Update test-config's description

```
gcloud scc notifications update test-config --organization=123 --description="New description"
```

Update test-config's pubsub-topic

```
gcloud scc notifications update test-config --organization=123 --pubsub-topic="projects/22222/topics/newtopic"
```

Update test-config's filter

```
gcloud scc notifications update test-config --organization=123 --filter='state = \"ACTIVE\"'
```

Update all mutable fields for `test-config` with
`location=global` under an organization parent (description + pubsub
topic + filter):

```
gcloud scc notifications update scc notifications update test-config --organization=123 --description="New description" --pubsub-topic="projects/22222/topics/newtopic" --location=global
```

**POSITIONAL ARGUMENTS**

: **`NOTIFICATION_CONFIG_ID`**:
The ID of the notification config. Formatted as
"organizations/123/notificationConfigs/456" or just "456".

**FLAGS**

: **--description**:
The text that will be used to describe a notification configuration.

**--filter**:
The filter string which will applied to events of findings of a notification
configuration.

**--location**:
Required if either data residency is enabled or the
`notificationConfig` was created by using the API v2.
If data residency is enabled, specify the Security Command Center location in
which the notification is stored.
If data residency is not enabled, include
`/locations/```LOCATION´´ in the full name or specify the
`--location` flag only if the `notificationConfig`
resource was created by using the Security Command Center API v2, in which case,
the only valid location is `global`.

**--pubsub-topic**:
The Pub/Sub topic which will receive notifications. Its format is
"projects/[project_id]/topics/[topic]".

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
gcloud alpha scc notifications update
```

```
gcloud beta scc notifications update
```