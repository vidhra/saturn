# gcloud edge-cloud container clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create)*

**NAME**

: **gcloud edge-cloud container clusters create - create an Edge Container cluster**

**SYNOPSIS**

: **`gcloud edge-cloud container clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--location)`=`LOCATION`) [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--admin-users)`=`ADMIN_USERS`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--async)`] [`[--cluster-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--cluster-ipv4-cidr)`=`CLUSTER_IPV4_CIDR`; default="10.0.0.0/17"] [`[--container-default-runtime-class](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--container-default-runtime-class)`=`CONTAINER_DEFAULT_RUNTIME_CLASS`] [`[--control-plane-kms-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--control-plane-kms-key)`=`CONTROL_PLANE_KMS_KEY`] [`[--control-plane-machine-filter](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--control-plane-machine-filter)`=`CONTROL_PLANE_MACHINE_FILTER`] [`[--control-plane-node-count](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--control-plane-node-count)`=`CONTROL_PLANE_NODE_COUNT`] [`[--control-plane-node-location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--control-plane-node-location)`=`CONTROL_PLANE_NODE_LOCATION`] [`[--control-plane-node-storage-schema](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--control-plane-node-storage-schema)`=`CONTROL_PLANE_NODE_STORAGE_SCHEMA`] [`[--control-plane-shared-deployment-policy](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--control-plane-shared-deployment-policy)`=`CONTROL_PLANE_SHARED_DEPLOYMENT_POLICY`] [`[--default-max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--default-max-pods-per-node)`=`DEFAULT_MAX_PODS_PER_NODE`] [`[--external-lb-ipv4-address-pools](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--external-lb-ipv4-address-pools)`=[`EXTERNAL_LB_IPV4_ADDRESS`,…]] [`[--fleet-project](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--fleet-project)`=`FLEET_PROJECT`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--lro-timeout](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--lro-timeout)`=`LRO_TIMEOUT`] [`[--maintenance-window-end](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--maintenance-window-end)`=`MAINTENANCE_WINDOW_END`] [`[--maintenance-window-recurrence](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--maintenance-window-recurrence)`=`MAINTENANCE_WINDOW_RECURRENCE`] [`[--maintenance-window-start](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--maintenance-window-start)`=`MAINTENANCE_WINDOW_START`] [`[--offline-reboot-ttl](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--offline-reboot-ttl)`=`OFFLINE_REBOOT_TTL`] [`[--release-channel](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--release-channel)`=`RELEASE_CHANNEL`; default=`"RELEASE_CHANNEL_UNSPECIFIED"`] [`[--services-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--services-ipv4-cidr)`=`SERVICES_IPV4_CIDR`; default="10.96.0.0/12"] [`[--system-addons-config](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--system-addons-config)`=`SYSTEM_ADDONS_CONFIG`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--version)`=`VERSION`] [`[--zone-storage-kms-key](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#--zone-storage-kms-key)`=`ZONE_STORAGE_KMS_KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Edge Container cluster.

**EXAMPLES**

: To create a cluster called `my-cluster` in region us-central1, run:

```
gcloud edge-cloud container clusters create my-cluster --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Edge Container cluster to create. The arguments in this group
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
Google Cloud location for the cluster.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--admin-users**:
Username (Google email address) of the user who should be granted cluster-admin
initially. This currently supports exactly one admin. If not set, the account
issuing the creation request will be used by default.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster-ipv4-cidr**:
All pods in the cluster are assigned an RFC1918 IPv4 address from this block.
This field cannot be changed after creation.

**--container-default-runtime-class**:
Name of the default runtime class for containers. It supports two values RUNC
and GVISOR.

**--control-plane-kms-key**:
Google Cloud KMS key that will be used to secure persistent disks of the control
plane VMs of a remote control plane cluster. The Edge Container service account
for this project must have
`roles/cloudkms.cryptoKeyEncrypterDecrypter` on the key.
If not provided, a Google-managed key will be used by default.

**--control-plane-machine-filter**:
Only machines matching this filter will be allowed to host local control plane
nodes. The filtering language accepts strings like "name=<name>", and is
documented here: [AIP-160](https://google.aip.dev/160).

**--control-plane-node-count**:
The number of local control plane nodes in a cluster. Use one to create a
single-node control plane or use three to create a high availability control
plane. Any other numbers of nodes will not be accepted.

**--control-plane-node-location**:
Google Edge Cloud zone where the local control plane nodes will be created.

**--control-plane-node-storage-schema**:
Name for the storage schema of control plane nodes.

**--control-plane-shared-deployment-policy**:
Policy configuration about how user application is deployed for local control
plane cluster. It supports two values, ALLOWED and DISALLOWED. ALLOWED means
that user application can be deployed on control plane nodes. DISALLOWED means
that user application can not be deployed on control plane nodes. Instead, it
can only be deployed on worker nodes. By default, this value is DISALLOWED. The
input is case insensitive.

**--default-max-pods-per-node**:
The default maximum number of pods per node.

**--external-lb-ipv4-address-pools**:
IPv4 address pools that are used for data plane load balancing of local control
plane clusters. Existing pools cannot be updated after cluster creation; only
adding new pools is allowed. Each address pool must be specified as one of the
following two types of values: 1. A IPv4 address range, for example,
"10.0.0.1-10.0.0.10". A range that contains a single IP (e.g.
"10.0.0.1-10.0.0.1") is allowed. 2. A IPv4 CIDR block, for example,
"10.0.0.1/24" Use comma when specifying multiple address pools, for example:
--external-lb-ipv4-address-pools 10.0.0.1-10.0.0.10,10.0.0.1/24

**--fleet-project**:
Name of the Fleet host project where the cluster is registered.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens (-),
underscores (`_`), lowercase characters, and numbers. Values must
contain only hyphens (-), underscores (`_`), lowercase characters,
and numbers.

**--lro-timeout**:
Overwrite the default LRO maximum timeout.

**--maintenance-window-end**:
End time of the recurring cluster maintenance window in the RFC 3339
(https://www.ietf.org/rfc/rfc3339.txt) format. E.g. "2021-01-01T00:00:00Z" or
"2021-01-01T00:00:00-05:00"

**--maintenance-window-recurrence**:
An RFC 5545 (https://tools.ietf.org/html/rfc5545#section-3.8.5.3) recurrence
rule for how the cluster maintenance window recurs. They go on for the span of
time between the start and the end time. E.g. FREQ=WEEKLY;BYDAY=SU.

**--maintenance-window-start**:
Start time of the recurring cluster maintenance window in the RFC 3339
(https://www.ietf.org/rfc/rfc3339.txt) format. E.g. "2021-01-01T00:00:00Z" or
"2021-01-01T00:00:00-05:00"

**--offline-reboot-ttl**:
Specifies the maximum duration a node can reboot offline (without connection to
Google) and then rejoin its cluster to resume its designated workloads. This
duration is relative to the machine's most recent connection to Google. The
maximum allowed duration is 7 days. To disallow offline reboot, set the duration
to "PT0S". The parameter should be an ISO 8601 duration string, for example,
"P1DT1H2M3S".

**--release-channel**:
Release channel a cluster is subscribed to. It supports two values, NONE and
REGULAR. NONE is used to opt out of any release channel. Clusters subscribed to
the REGULAR channel will be automatically upgraded to versions that are
considered GA quality, and cannot be manually upgraded. Additionally, if the
REGULAR channel is used, a specific target version cannot be set with the
'version' flag. If left unspecified, the release channel will default to
REGULAR.

**--services-ipv4-cidr**:
All services in the cluster are assigned an RFC1918 IPv4 address from this
block. This field cannot be changed after creation.

**--system-addons-config**:
If specified as a YAML/JSON file, customized configuration in this file will be
applied to the system add-ons.
For example,
{ "systemAddonsConfig": { "ingress": { "disabled": true, "ipv4_vip": "10.0.0.1"
} } }

**--version**:
Target cluster version. For example: "1.5.0".

**--zone-storage-kms-key**:
Google Cloud KMS key that will be used to encrypt and decrypt the root key for
zone storage encryption. The zone storage KMS key is only applicable to the
storage infra cluster. The Edge Container service account for this project must
have `roles/cloudkms.cryptoKeyEncrypterDecrypter` on the key.
If not provided, a Google-managed key will be used by default.

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

: This command uses the edgecontainer/v1 API. The full documentation for this API
can be found at: [https://cloud.google.com/edge-cloud](https://cloud.google.com/edge-cloud)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud container clusters create
```