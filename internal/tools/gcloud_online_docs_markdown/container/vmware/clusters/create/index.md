# gcloud container vmware clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create)*

**NAME**

: **gcloud container vmware clusters create - create an Anthos cluster on VMware**

**SYNOPSIS**

: **`gcloud container vmware clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--location)`=`LOCATION`) `[--version](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--version)`=`VERSION` (`[--admin-cluster-membership](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--admin-cluster-membership)`=`ADMIN_CLUSTER_MEMBERSHIP` : `[--admin-cluster-membership-location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--admin-cluster-membership-location)`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION` `[--admin-cluster-membership-project](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--admin-cluster-membership-project)`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`) ((`[--control-plane-vip](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--control-plane-vip)`=`CONTROL_PLANE_VIP` `[--ingress-vip](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--ingress-vip)`=`INGRESS_VIP`) (`[--metal-lb-config-address-pools](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--metal-lb-config-address-pools)`=[`addresses`=`ADDRESSES`],[`avoid-buggy-ips`=`AVOID-BUGGY-IPS`],[`manual-assign`=`MANUAL-ASSIGN`],[`pool`=`POOL`] | `[--control-plane-node-port](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--control-plane-node-port)`=`CONTROL_PLANE_NODE_PORT` `[--ingress-http-node-port](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--ingress-http-node-port)`=`INGRESS_HTTP_NODE_PORT` `[--ingress-https-node-port](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--ingress-https-node-port)`=`INGRESS_HTTPS_NODE_PORT` `[--konnectivity-server-node-port](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--konnectivity-server-node-port)`=`KONNECTIVITY_SERVER_NODE_PORT` | [`[--f5-config-address](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--f5-config-address)`=`F5_CONFIG_ADDRESS` `[--f5-config-partition](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--f5-config-partition)`=`F5_CONFIG_PARTITION` : `[--f5-config-snat-pool](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--f5-config-snat-pool)`=`F5_CONFIG_SNAT_POOL`])) (`[--pod-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--pod-address-cidr-blocks)`=`POD_ADDRESS` `[--service-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--service-address-cidr-blocks)`=`SERVICE_ADDRESS` : `[--control-plane-ip-block](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--control-plane-ip-block)`=[`gateway`=`GATEWAY`],[`ips`=`IPS`],[`netmask`=`NETMASK`] `[--dns-search-domains](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--dns-search-domains)`=[`DNS_SEARCH_DOMAINS`,…] `[--dns-servers](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--dns-servers)`=[`DNS_SERVERS`,…] `[--ntp-servers](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--ntp-servers)`=[`NTP_SERVERS`,…] `[--enable-dhcp](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-dhcp)`     | `[--static-ip-config-ip-blocks](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--static-ip-config-ip-blocks)`=[`gateway`=`GATEWAY`],[`ips`=`IPS`],[`netmask`=`NETMASK`]) [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--admin-users)`=`ADMIN_USERS`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--description)`=`DESCRIPTION`] [`[--disable-aag-config](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--disable-aag-config)`] [`[--disable-vsphere-csi](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--disable-vsphere-csi)`] [`[--enable-auto-repair](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-auto-repair)`] [`[--enable-vm-tracking](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-vm-tracking)`] [`[--upgrade-policy](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--upgrade-policy)`=[`control-plane-only`=`CONTROL-PLANE-ONLY`]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--validate-only)`] [`[--cpus](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--cpus)`=`CPUS` `[--enable-auto-resize](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-auto-resize)` `[--memory](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--memory)`=`MEMORY` `[--replicas](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--replicas)`=`REPLICAS`] [`[--disable-control-plane-v2](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--disable-control-plane-v2)`     | `[--enable-control-plane-v2](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-control-plane-v2)`] [`[--enable-advanced-networking](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-advanced-networking)` `[--enable-dataplane-v2](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--enable-dataplane-v2)`] [`[--vcenter-ca-cert-data](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-ca-cert-data)`=`VCENTER_CA_CERT_DATA` `[--vcenter-cluster](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-cluster)`=`VCENTER_CLUSTER` `[--vcenter-datacenter](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-datacenter)`=`VCENTER_DATACENTER` `[--vcenter-datastore](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-datastore)`=`VCENTER_DATASTORE` `[--vcenter-folder](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-folder)`=`VCENTER_FOLDER` `[--vcenter-resource-pool](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-resource-pool)`=`VCENTER_RESOURCE_POOL` `[--vcenter-storage-policy-name](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#--vcenter-storage-policy-name)`=`VCENTER_STORAGE_POLICY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Anthos cluster on VMware.

**EXAMPLES**

: To create a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container vmware clusters create my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to create The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
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
- provide the argument `--location` on the command line;
- set the property `container_vmware/location`.**

**REQUIRED FLAGS**

: **--version**:
Anthos Cluster on VMware version for the cluster resource

**Admin cluster membership resource - membership of the admin cluster. Membership
name is the same as the admin cluster name.
Examples:

```
gcloud container vmware clusters create
      --admin-cluster-membership=projects/example-project-12345/locations/us-west1/memberships/example-admin-cluster-name
```

or

```
gcloud container vmware clusters create
      --admin-cluster-membership-project=example-project-12345
      --admin-cluster-membership-location=us-west1
      --admin-cluster-membership=example-admin-cluster-name
```

```
The arguments in this group can be used to specify the attributes of this resource.
```

This must be specified.

**--admin-cluster-membership**:
ID of the admin_cluster_membership or fully qualified identifier for the
admin_cluster_membership.
To set the `admin_cluster_membership` attribute:

- provide the argument `--admin-cluster-membership` on the command
line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--admin-cluster-membership-location**:
Google Cloud location for the admin_cluster_membership.
To set the `location` attribute:

- provide the argument `--admin-cluster-membership` on the command line
with a fully specified name;
- provide the argument `--admin-cluster-membership-location` on the
command line.

**--admin-cluster-membership-project**:
Google Cloud project for the admin_cluster_membership.
To set the `project` attribute:

- provide the argument `--admin-cluster-membership` on the command line
with a fully specified name;
- provide the argument `--admin-cluster-membership-project` on the
command line.**

**--control-plane-vip**

**--pod-address-cidr-blocks**

**OPTIONAL FLAGS**

: **--admin-users**

**--annotations**:
Annotations on the VMware user cluster.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description for the resource.

**--disable-aag-config**

**--disable-vsphere-csi**

**--enable-auto-repair**

**--enable-vm-tracking**:
If set, enable VM tracking.

**--upgrade-policy**

**--validate-only**:
If set, only validate the request, but do not actually perform the operation.

**--cpus**

**--disable-control-plane-v2**

**--enable-advanced-networking**

**--vcenter-ca-cert-data**

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
gcloud alpha container vmware clusters create
```

```
gcloud beta container vmware clusters create
```