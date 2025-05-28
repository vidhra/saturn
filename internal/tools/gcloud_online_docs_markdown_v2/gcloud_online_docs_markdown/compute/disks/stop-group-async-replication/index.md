# gcloud compute disks stop-group-async-replication  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication)*

**NAME**

: **gcloud compute disks stop-group-async-replication - consistently stops a group of asynchronously replicating disks**

**SYNOPSIS**

: **`gcloud compute disks stop-group-async-replication` `[DISK_CONSISTENCY_GROUP_POLICY](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication#DISK_CONSISTENCY_GROUP_POLICY)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/disks/stop-group-async-replication#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute disks stop-group-async-replication` consistently
stops a group of asynchronously replicating disks. This command can be invoked
in either in the primary or secondary scope of the replicating disks.

**EXAMPLES**

: To stop group replication in the primary scope, include the zone or region of
the primary disks. The URL of the disk consistency group resource policy always
uses the region of the primary disks:

```
gcloud compute disks stop-group-async-replication projects/my-project/regions/us-west1/resourcePolicies/my-policy --zone=us-west1-a
```

Alternatively, you can stop replication in the secondary scope. Include the
region or zone of the secondary disks. The URL of the disk consistency group
resource policy always uses the region of the primary disks:

```
gcloud compute disks stop-group-async-replication projects/my-project/regions/us-west1/resourcePolicies/my-policy --zone=us-west2-a
```

**POSITIONAL ARGUMENTS**

: **`DISK_CONSISTENCY_GROUP_POLICY`**:
URL of the disk consistency group resource policy. The resourcepolicy is always
in the region of the primary disks.

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

: These variants are also available:

```
gcloud alpha compute disks stop-group-async-replication
```

```
gcloud beta compute disks stop-group-async-replication
```