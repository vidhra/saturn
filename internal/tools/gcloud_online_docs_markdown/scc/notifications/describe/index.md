# gcloud scc notifications describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe)*

**NAME**

: **gcloud scc notifications describe - describe a Security Command Center notification config**

**SYNOPSIS**

: **`gcloud scc notifications describe` `[NOTIFICATION_CONFIG_ID](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe#NOTIFICATION_CONFIG_ID)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe#--location)`=`LOCATION`; default="global"] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/notifications/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Security Command Center notification config.
Notification configs that are created with Security Command Center API V2 and
later include a `location` attribute. If the `location`
attribute is included in the resource name of a Notification configs, you must
specify it when referencing the Notification config. For example, the following
Notification configs name has `location=eu`:
`organizations/123/locations/eu/notificationConfigs/test-config`.

**EXAMPLES**

: Describe notification config 'test-config' from organization `123`

```
gcloud scc notifications describe test-config --organization=123
```

Describe notification config 'test-config' from folder `456`

```
gcloud scc notifications describe test-config --folder=456
```

Describe notification config 'test-config' from project `789`

```
gcloud scc notifications describe test-config --project=789
```

Describe notification config 'test-config' from organization `123`
and `location=global`

```
gcloud scc notifications describe test-config --organization=123 --location=global
```

**POSITIONAL ARGUMENTS**

: **`NOTIFICATION_CONFIG_ID`**:
The ID of the notification config. Formatted as
"organizations/123/notificationConfigs/456" or just "456".

**FLAGS**

: **--location**:
Required if either data residency is enabled or the
`notificationConfig` resources were created by using the API v2.
If data residency is enabled, specify the Security Command Center location in
which the notifications are stored.
If data residency is not enabled, include
`/locations/```LOCATION´´ only if the
`notificationConfig` resource was created by using the Security
Command Center API v2, in which case, the only valid location is
`global`.

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
gcloud alpha scc notifications describe
```

```
gcloud beta scc notifications describe
```