# gcloud compute instance-groups managed wait-until-stable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable)*

**NAME**

: **gcloud compute instance-groups managed wait-until-stable - waits until state of managed instance group is stable**

**SYNOPSIS**

: **`gcloud compute instance-groups managed wait-until-stable` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable#NAME)` [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable#--timeout)`=`TIMEOUT`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until-stable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Waits until state of managed instance group is stable.
`gcloud compute instance-groups managed wait-until-stable` is
deprecated. Please use `gcloud compute instance-groups managed wait-until
--stable` instead.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the managed instance group to operate on.

**FLAGS**

: **--timeout**:
Timeout in seconds for waiting for group becoming stable.

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
gcloud alpha compute instance-groups managed wait-until-stable
```

```
gcloud beta compute instance-groups managed wait-until-stable
```