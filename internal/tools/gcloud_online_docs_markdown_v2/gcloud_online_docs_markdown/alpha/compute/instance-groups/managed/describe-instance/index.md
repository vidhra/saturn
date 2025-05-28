# gcloud alpha compute instance-groups managed describe-instance  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance)*

**NAME**

: **gcloud alpha compute instance-groups managed describe-instance - describe an instance in a managed instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups managed describe-instance` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance#NAME)` `[--instance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance#--instance)`=`INSTANCE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/describe-instance#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups managed
describe-instance` describes an instance in a managed instance group,
listing all its attributes in YAML format.

**EXAMPLES**

: To describe an instance `instance-1` in `my-group` (in
region europe-west4), run:

```
gcloud alpha compute instance-groups managed describe-instance my-group --instance=instance-1 --region=europe-west4
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to describe an instance in.

**REQUIRED FLAGS**

: **--instance**:
Name of the managed instance to describe.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups managed describe-instance
```

```
gcloud beta compute instance-groups managed describe-instance
```