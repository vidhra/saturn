# gcloud compute instance-groups managed rolling-action stop-proactive-update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/stop-proactive-update](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/stop-proactive-update)*

**NAME**

: **gcloud compute instance-groups managed rolling-action stop-proactive-update - stop the proactive update process of managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed rolling-action stop-proactive-update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/stop-proactive-update#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/stop-proactive-update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/stop-proactive-update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/stop-proactive-update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command changes the update type of the managed instance group to
opportunistic.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--region**

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
gcloud alpha compute instance-groups managed rolling-action stop-proactive-update
```

```
gcloud beta compute instance-groups managed rolling-action stop-proactive-update
```