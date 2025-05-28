# gcloud compute instance-groups managed set-instance-template  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template)*

**NAME**

: **gcloud compute instance-groups managed set-instance-template - set the instance template for a managed instance group**

**SYNOPSIS**

: **`gcloud compute instance-groups managed set-instance-template` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template#NAME)` `[--template](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template#--template)`=`TEMPLATE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed set-instance-template` sets
the instance template for an existing managed instance group.
The new template applies to all new instances added to the managed instance
group.
To apply the new template to existing instances in the group, use one of the
following methods:

- Update instances using the `update-instances` command.
- Recreate instances using the `recreate-instances` command.
- Use the `rolling-action start-update` command.
- Use the API to set the group's `updatePolicy.type` to
`PROACTIVE`.

**EXAMPLES**

: Running:

```
gcloud compute instance-groups managed set-instance-template \
example-managed-instance-group --template=example-global-instance-template
```

Sets the instance template for the 'example-managed-instance-group' group to a
global resource 'example-global-instance-template'.
To use a regional instance template, specify the full or partial URL of the
template.
Running:

```
gcloud compute instance-groups managed set-instance-template \
example-managed-instance-group \
--template=projects/example-project/regions/us-central1/instanceTemplates/example-regional-instance-template
```

Sets the instance template for the 'example-managed-instance-group' group to a
regional resource 'example-regional-instance-template'.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--template**:
Specifies the instance template to use when creating new instances. An instance
template is either a global or regional resource.

**OPTIONAL FLAGS**

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
gcloud alpha compute instance-groups managed set-instance-template
```

```
gcloud beta compute instance-groups managed set-instance-template
```