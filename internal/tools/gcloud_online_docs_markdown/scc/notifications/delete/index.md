# gcloud scc notifications delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete)*

**NAME**

: **gcloud scc notifications delete - delete a Security Command Center notification config**

**SYNOPSIS**

: **`gcloud scc notifications delete` `[NOTIFICATION_CONFIG_ID](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete#NOTIFICATION_CONFIG_ID)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete#--location)`=`LOCATION`; default="global"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Security Command Center notification config.
Notification configs that are created with Security Command Center API V2 and
later include a `location` attribute. If the `location`
attribute is included in the resource name of a Notification configs, you must
specify it when referencing the Notification config. For example, the following
Notification configs name has `location=eu`:
`organizations/123/locations/eu/notificationConfigs/test-config`.

**EXAMPLES**

: Delete notification config 'test-config' from organization `123`

```
gcloud scc notifications delete test-config --organization=123
```

Delete notification config 'test-config' from folder `456`

```
gcloud scc notifications delete test-config --folder=456
```

Delete notification config 'test-config' from project `789`

```
gcloud scc notifications delete test-config --project=789
```

Delete notification config 'test-config' with location `global` from
organization `123`

```
gcloud scc notifications delete test-config --organization=123 --location=global
```

Delete notification config 'test-config' with `location=eu` from
organization `123`

```
gcloud scc notifications delete test-config --organization=123 --location=eu
```

**POSITIONAL ARGUMENTS**

: **`NOTIFICATION_CONFIG_ID`**:
The ID of the notification config. Formatted as
"organizations/123/notificationConfigs/456" or just "456".

**FLAGS**

: **--location**:
Required if either data residency is enabled or the
`notificationConfig` was created by using the API v2.
If data residency is enabled, specify the Security Command Center location in
which the notification is stored.
If data residency is not enabled, include
`/locations/```LOCATION´´ in the full name or specify the
`--location flag` only if the `notificationConfig` was
created by using the Security Command Center API v2, in which case, the only
valid location is `global`.

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
gcloud alpha scc notifications delete
```

```
gcloud beta scc notifications delete
```