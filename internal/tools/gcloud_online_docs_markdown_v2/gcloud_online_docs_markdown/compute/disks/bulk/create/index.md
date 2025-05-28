# gcloud compute disks bulk create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create](https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create)*

**NAME**

: **gcloud compute disks bulk create - create multiple Compute Engine disks**

**SYNOPSIS**

: **`gcloud compute disks bulk create` `[--source-consistency-group-policy](https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create#--source-consistency-group-policy)`=`SOURCE_CONSISTENCY_GROUP_POLICY` (`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create#--zone)`=`ZONE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks bulk create` facilitates the creation of
multiple Compute Engine disks with a single command. This includes cloning a set
of Async PD secondary disks with the same consistency group policy.

**EXAMPLES**

: To consistently clone secondary disks with the same consistency group policy
'projects/example-project/regions/us-central1/resourcePolicies/example-group-policy'
to target zone 'us-central1-a', run:

```
gcloud compute disks bulk create --source-consistency-group-policy=projects/example-project/regions/us-central1/resourcePolicies/example-group-policy --zone=us-central1-a
```

**REQUIRED FLAGS**

: **--source-consistency-group-policy**:
URL of the source consistency group resource policy. The resource policy is
always the same region as the source disks.

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
gcloud alpha compute disks bulk create
```

```
gcloud beta compute disks bulk create
```