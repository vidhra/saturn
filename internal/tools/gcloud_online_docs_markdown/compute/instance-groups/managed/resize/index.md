# gcloud compute instance-groups managed resize  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize)*

**NAME**

: **gcloud compute instance-groups managed resize - set managed instance group size**

**SYNOPSIS**

: **`gcloud compute instance-groups managed resize` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize#NAME)` `[--size](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize#--size)`=`SIZE` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instance-groups managed resize` resize a managed
instance group to a provided size.
If you resize down, the Instance Group Manager service deletes instances from
the group until the group reaches the desired size. Instances are deleted in
arbitrary order but the Instance Group Manager takes into account some
considerations before it chooses which instance to delete. For more information,
see [https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/resize](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/resize).
If you resize up, the service adds instances to the group using the current
instance template until the group reaches the desired size.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**REQUIRED FLAGS**

: **--size**:
Target number of running instances in managed instance group.

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
gcloud alpha compute instance-groups managed resize
```

```
gcloud beta compute instance-groups managed resize
```