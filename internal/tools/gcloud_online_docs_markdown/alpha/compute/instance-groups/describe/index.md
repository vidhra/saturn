# gcloud alpha compute instance-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe)*

**NAME**

: **gcloud alpha compute instance-groups describe - display detailed information about an instance group**

**SYNOPSIS**

: **`gcloud alpha compute instance-groups describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute instance-groups describe`
displays all data associated with an instance group in a project.

**EXAMPLES**

: To get details about a regional instance group in the
``us-central1`` regions, run:

```
gcloud alpha compute instance-groups describe --region=us-central1
```

To get details about a zonal instance group in the
``us-central1-b`` zone, run:

```
gcloud alpha compute instance-groups describe --zone=us-central1-b
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the instance group to describe.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute instance-groups describe
```

```
gcloud beta compute instance-groups describe
```