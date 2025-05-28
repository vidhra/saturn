# gcloud compute snapshot-settings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update](https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update)*

**NAME**

: **gcloud compute snapshot-settings update - update snapshot settings**

**SYNOPSIS**

: **`gcloud compute snapshot-settings update` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update#--async)`] [`[--storage-location-names](https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update#--storage-location-names)`=[`STORAGE_LOCATION_NAMES`,…]] [`[--storage-location-policy](https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update#--storage-location-policy)`=`STORAGE_LOCATION_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the snapshot settings of a project.

**EXAMPLES**

: To update the snapshot settings and set the storage location policy to the
nearest multi-region as the source disk, run:

```
gcloud compute snapshot-settings update --storage-location-policy=nearest-multi-region
```

To update the snapshot settings and set the storage location policy to the same
region as the source disk, run:

```
gcloud compute snapshot-settings update --storage-location-policy=local-region
```

To update the snapshot settings and set the storage location policy to store
snapshots in a specific location like `us-west1`, run:

```
gcloud compute snapshot-settings update --storage-location-policy=specific-locations --storage-location-names=us-west1
```

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--storage-location-names**:
The custom storage location that you specify for the project's snapshots. You
can specify only a single location. Use this flag only when you use the
specific-locations value for the `--storage-location-policy` flag.
For more information, refer to the snapshot settings documentation at [https://cloud.google.com/compute/docs/disks/snapshot-settings](https://cloud.google.com/compute/docs/disks/snapshot-settings).

**--storage-location-policy**:
The storage location policy. For more information, refer to the snapshot
settings documentation at [https://cloud.google.com/compute/docs/disks/snapshot-settings](https://cloud.google.com/compute/docs/disks/snapshot-settings).
STORAGE_LOCATION_POLICY must be one of: local-region, nearest-multi-region,
specific-locations.

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

**API REFERENCE**

: This command uses the compute/alpha or compute/beta or compute/v1 API. The full
documentation for this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute snapshot-settings update
```

```
gcloud beta compute snapshot-settings update
```