# gcloud alpha compute instance-groups managed stop-instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances)*

**NAME**

: **gcloud alpha compute instance-groups managed stop-instances - stop instances owned by a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed stop-instances` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#NAME)` `[--instances](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#--instances)`=`INSTANCE`,[`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#INSTANCE)`,…] [`[--force](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#--force)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/stop-instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
stop-instances` stops one or more instances from a managed instance group

**EXAMPLES**

: To stop an instance from a managed instance group in the us-central1-a zone,
run:

```
gcloud alpha compute instance-groups managed stop-instances example-managed-instance-group --zone=us-central1-a --instances=example-instance
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--instances**:
Names of instances to stop.

**OPTIONAL FLAGS**

: **--force**:
Immediately stop the specified instances, skipping the initial delay, if one is
specified in the standby policy.

**--region**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups managed stop-instances
```

```
gcloud beta compute instance-groups managed stop-instances
```