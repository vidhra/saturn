# gcloud compute instance-groups managed all-instances-config delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete)*

**NAME**

: **gcloud compute instance-groups managed all-instances-config delete - delete values defined in the all-instances configuration of a managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed all-instances-config delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#NAME)` [`[--labels](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#--labels)`=`KEY`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#KEY)`,…]] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#--metadata)`=`KEY`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#KEY)`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed all-instances-config delete`
deletes one or more values defined in the all-instances configuration of a
managed instance group.
To apply a revised all-instances configuration to existing instances in the
group, use one of the following methods:

- Update instances using the `update-instances` command.
- Recreate instances using the `recreate-instances` command.
- Use the `rolling-action start-update` command.
- Use the API to set the group's `updatePolicy.type` to
`PROACTIVE`.

**EXAMPLES**

: To delete the group's all-instances configuration in order to stop overriding
the group's instance template for a label with the key `label-key`
and metadata with the key `metadata-key` in group
`my-group`, run:

```
gcloud compute instance-groups managed all-instances-config delete my-group --metadata=metadata-key --labels=label-key
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to delete the all instances configuration
for.

**FLAGS**

: **--labels**:
Remove labels keys from the group's all instances configuration.

**--metadata**:
Remove metadata keys from the group's all instances configuration.

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

: These variants are also available:

```
gcloud alpha compute instance-groups managed all-instances-config delete
```

```
gcloud beta compute instance-groups managed all-instances-config delete
```