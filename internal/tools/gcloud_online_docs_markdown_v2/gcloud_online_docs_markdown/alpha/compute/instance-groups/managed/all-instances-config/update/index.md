# gcloud alpha compute instance-groups managed all-instances-config update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update)*

**NAME**

: **gcloud alpha compute instance-groups managed all-instances-config update - update the all-instances configuration of a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed all-instances-config update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#NAME)` [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#--labels)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#KEY)`=`VALUE`,…]] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#KEY)`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/all-instances-config/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
all-instances-config update` updates the group's all-instances
configuration and applies it only to new instances that are added to the group.
To apply a revised all-instances configuration to existing instances in the
group, use one of the following methods:

- Update instances using the `update-instances` command.
- Recreate instances using the `recreate-instances` command.
- Use the `rolling-action start-update` command.
- Use the API to set the group's `updatePolicy.type` to
`PROACTIVE`.

**EXAMPLES**

: To update an all-instances configuration in order to override the group's
instance template for a label with the key `label-key` and metadata
with the key `metadata-key` in group `my-group`, run:

```
gcloud alpha compute instance-groups managed all-instances-config update my-group --metadata=metadata-key=metadata-override-value --labels=qlabel-key=label-override-value
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to update the all instances configuration
for.

**FLAGS**

: **--labels**:
Add labels to the group's all instances configuration.

**--metadata**:
Add metadata to the group's all instances configuration.

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
gcloud compute instance-groups managed all-instances-config update
```

```
gcloud beta compute instance-groups managed all-instances-config update
```