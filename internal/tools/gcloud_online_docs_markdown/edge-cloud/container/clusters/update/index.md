# gcloud edge-cloud container clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update)*

**NAME**

: **gcloud edge-cloud container clusters update - update an Edge Container cluster**

**SYNOPSIS**

: **`gcloud edge-cloud container clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--async)`] [`[--container-default-runtime-class](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--container-default-runtime-class)`=`CONTAINER_DEFAULT_RUNTIME_CLASS`] [`[--offline-reboot-ttl](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--offline-reboot-ttl)`=`OFFLINE_REBOOT_TTL`] [`[--release-channel](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--release-channel)`=`RELEASE_CHANNEL`] [`[--clear-maintenance-window](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--clear-maintenance-window)`     | `[--remove-maintenance-exclusion-window](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--remove-maintenance-exclusion-window)`=`REMOVE_MAINTENANCE_EXCLUSION_WINDOW`     | `[--add-maintenance-exclusion-end](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--add-maintenance-exclusion-end)`=`ADD_MAINTENANCE_EXCLUSION_END` `[--add-maintenance-exclusion-name](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--add-maintenance-exclusion-name)`=`ADD_MAINTENANCE_EXCLUSION_NAME` `[--add-maintenance-exclusion-start](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--add-maintenance-exclusion-start)`=`ADD_MAINTENANCE_EXCLUSION_START`     | `[--maintenance-window-end](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--maintenance-window-end)`=`MAINTENANCE_WINDOW_END` `[--maintenance-window-recurrence](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--maintenance-window-recurrence)`=`MAINTENANCE_WINDOW_RECURRENCE` `[--maintenance-window-start](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--maintenance-window-start)`=`MAINTENANCE_WINDOW_START`] [`[--control-plane-kms-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--control-plane-kms-key)`=`CONTROL_PLANE_KMS_KEY`     | `[--use-google-managed-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--use-google-managed-key)`] [`[--use-google-managed-zone-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--use-google-managed-zone-key)`     | `[--zone-storage-kms-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#--zone-storage-kms-key)`=`ZONE_STORAGE_KMS_KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Edge Container cluster.

**EXAMPLES**

: To update the maintenance window recurrence rule of a cluster called
'my-cluster' in region us-central1, run:

```
gcloud edge-cloud container clusters update my-cluster --location=us-central1 --maintenance-window-recurrence="FREQ=WEEKLY"
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Edge Container cluster to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `edge_container/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--container-default-runtime-class**:
If set, use the specified default container runtime class for the cluster.

**--offline-reboot-ttl**:
Specifies the maximum duration a node can reboot offline (without connection to
Google) and then rejoin its cluster to resume its designated workloads. This
duration is relative to the machine's most recent connection to Google. The
maximum allowed duration is 7 days. If left unspecified, the default 0 means not
allowed. The parameter should be an ISO 8601 duration string, for example,
"P1DT1H2M3S".

**--release-channel**:
Release channel a cluster is subscribed to. It supports two values, NONE and
REGULAR. NONE is used to opt out of any release channel. Clusters subscribed to
the REGULAR channel will be automatically upgraded to versions that are
considered GA quality, and cannot be manually upgraded.
`RELEASE_CHANNEL` must be one of: `none`,
`regular`, `release-channel-unspecified`.

**--clear-maintenance-window**

**--control-plane-kms-key**

**--use-google-managed-zone-key**

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

: This command uses the `edgecontainer/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/edge-cloud](https://cloud.google.com/edge-cloud)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud container clusters update
```