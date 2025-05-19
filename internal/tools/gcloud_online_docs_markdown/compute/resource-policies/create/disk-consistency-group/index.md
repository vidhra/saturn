# gcloud compute resource-policies create disk-consistency-group  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group)*

**NAME**

: **gcloud compute resource-policies create disk-consistency-group - create a Compute Engine Disk Consistency Group resource policy**

**SYNOPSIS**

: **`gcloud compute resource-policies create disk-consistency-group` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group#--description)`=`DESCRIPTION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Compute Engine disk consistency group resource policy.

**EXAMPLES**

: Create a disk consistency group policy:

```
gcloud compute resource-policies create disk-consistency-group my-resource-policy --region=REGION
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the resource policy to operate on.

**FLAGS**

: **--description**:
An optional, textual description for the backend.

**--region**:
Region of the resource policy to operate on. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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
gcloud alpha compute resource-policies create disk-consistency-group
```

```
gcloud beta compute resource-policies create disk-consistency-group
```