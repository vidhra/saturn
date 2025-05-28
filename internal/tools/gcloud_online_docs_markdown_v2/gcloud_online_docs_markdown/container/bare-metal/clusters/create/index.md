# gcloud container bare-metal clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create)*

**NAME**

: **gcloud container bare-metal clusters create - create an Anthos cluster on bare metal**

**SYNOPSIS**

: **`gcloud container bare-metal clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--location)`=`LOCATION`) `[--version](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--version)`=`VERSION` (`[--admin-cluster-membership](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--admin-cluster-membership)`=`ADMIN_CLUSTER_MEMBERSHIP` : `[--admin-cluster-membership-location](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--admin-cluster-membership-location)`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION` `[--admin-cluster-membership-project](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--admin-cluster-membership-project)`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`) (`[--control-plane-load-balancer-port](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-load-balancer-port)`=`CONTROL_PLANE_LOAD_BALANCER_PORT` (`[--control-plane-vip](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-vip)`=`CONTROL_PLANE_VIP` `[--ingress-vip](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--ingress-vip)`=`INGRESS_VIP`) (`[--enable-manual-lb](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--enable-manual-lb)` | [`[--bgp-address-pools](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-address-pools)`=[`addresses`=`ADDRESSES`],[`avoid-buggy-ips`=`AVOID-BUGGY-IPS`],[`manual-assign`=`MANUAL-ASSIGN`],[`pool`=`POOL`] `[--bgp-asn](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-asn)`=`BGP_ASN` `[--bgp-peer-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-peer-configs)`=[`asn`=`ASN`,`ip`=`IP`,`control-plane-nodes`=`NODE_IP_1`;`[NODE_IP_2](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#NODE_IP_2)`,…] : [`[--bgp-load-balancer-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-load-balancer-node-configs)`=[`node-ip`=`IP`,`labels`=`KEY1`=`VALUE1`;`[KEY2](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#KEY2)`=`VALUE2`,…] : `[--bgp-load-balancer-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-load-balancer-node-labels)`=[`KEY`=`VALUE`,…] `[--bgp-load-balancer-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-load-balancer-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#EFFECT)`,…] `[--bgp-load-balancer-registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-load-balancer-registry-burst)`=`BGP_LOAD_BALANCER_REGISTRY_BURST` `[--bgp-load-balancer-registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--bgp-load-balancer-registry-pull-qps)`=`BGP_LOAD_BALANCER_REGISTRY_PULL_QPS` `[--disable-bgp-load-balancer-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--disable-bgp-load-balancer-serialize-image-pulls)`]] | [`[--metal-lb-address-pools](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--metal-lb-address-pools)`=[`addresses`=`ADDRESSES`],[`avoid-buggy-ips`=`AVOID-BUGGY-IPS`],[`manual-assign`=`MANUAL-ASSIGN`],[`pool`=`POOL`] : `[--metal-lb-load-balancer-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--metal-lb-load-balancer-node-configs)`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] `[--metal-lb-load-balancer-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--metal-lb-load-balancer-node-labels)`=[`KEY`=`VALUE`,…] `[--metal-lb-load-balancer-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--metal-lb-load-balancer-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#EFFECT)`,…] `[--disable-metal-lb-load-balancer-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--disable-metal-lb-load-balancer-serialize-image-pulls)` `[--metal-lb-load-balancer-registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--metal-lb-load-balancer-registry-burst)`=`METAL_LB_LOAD_BALANCER_REGISTRY_BURST` `[--metal-lb-load-balancer-registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--metal-lb-load-balancer-registry-pull-qps)`=`METAL_LB_LOAD_BALANCER_REGISTRY_PULL_QPS`])) ((((`[--control-plane-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-node-configs)`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] : `[--control-plane-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-node-labels)`=[`KEY`=`VALUE`,…] `[--control-plane-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#EFFECT)`,…] `[--control-plane-registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-registry-burst)`=`CONTROL_PLANE_REGISTRY_BURST` `[--control-plane-registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--control-plane-registry-pull-qps)`=`CONTROL_PLANE_REGISTRY_PULL_QPS` `[--disable-control-plane-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--disable-control-plane-serialize-image-pulls)`))) : `[--api-server-args](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--api-server-args)`=[`KEY`=`VALUE`,…]) ((`[--lvp-node-mounts-config-path](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--lvp-node-mounts-config-path)`=`LVP_NODE_MOUNTS_CONFIG_PATH` `[--lvp-node-mounts-config-storage-class](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--lvp-node-mounts-config-storage-class)`=`LVP_NODE_MOUNTS_CONFIG_STORAGE_CLASS`) ((`[--lvp-share-path](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--lvp-share-path)`=`LVP_SHARE_PATH` `[--lvp-share-storage-class](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--lvp-share-storage-class)`=`LVP_SHARE_STORAGE_CLASS`) : `[--shared-path-pv-count](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--shared-path-pv-count)`=`SHARED_PATH_PV_COUNT`)) [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--admin-users)`=`ADMIN_USERS`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--async)`] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--description)`=`DESCRIPTION`] [`[--enable-application-logs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--enable-application-logs)`] [`[--login-user](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--login-user)`=`LOGIN_USER`] [`[--maintenance-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--maintenance-address-cidr-blocks)`=[`MAINTENANCE_ADDRESS_CIDR_BLOCKS`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--validate-only)`] [`[--container-runtime](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--container-runtime)`=`CONTAINER_RUNTIME` `[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--max-pods-per-node)`=`MAX_PODS_PER_NODE`] [[(`[--island-mode-pod-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--island-mode-pod-address-cidr-blocks)`=`POD_ADDRESS`,[`[POD_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#POD_ADDRESS)`,…] `[--island-mode-service-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--island-mode-service-address-cidr-blocks)`=`SERVICE_ADDRESS`,[…]) : `[--enable-advanced-networking](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--enable-advanced-networking)` `[--enable-multi-nic-config](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--enable-multi-nic-config)` `[--enable-sr-iov-config](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--enable-sr-iov-config)`]] [`[--uri](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--uri)`=`URI` : `[--no-proxy](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#--proxy)`=[`NO_PROXY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Anthos cluster on bare metal.

**EXAMPLES**

: To create a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container bare-metal clusters create my-cluster --location=us-west1
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
- set the property `container_bare_metal/location`.**

**REQUIRED FLAGS**

: **--version**:
Anthos cluster on bare metal version for the user cluster resource.

**Admin cluster membership resource - membership of the admin cluster. Membership
name is the same as the admin cluster name.
Examples:

```
gcloud container bare-metal clusters create
      --admin-cluster-membership=projects/example-project-12345/locations/us-west1/memberships/example-admin-cluster-name
```

or

```
gcloud container bare-metal clusters create
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

**--control-plane-load-balancer-port**

**--api-server-args**

**--lvp-node-mounts-config-path**

**OPTIONAL FLAGS**

: **--admin-users**

**--annotations**:
Annotations on the Anthos on bare metal resource.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--binauthz-evaluation-mode**:
Set Binary Authorization evaluation mode for this cluster.
`BINAUTHZ_EVALUATION_MODE` must be one of:
`DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`.

**--description**:
Description for the resource.

**--enable-application-logs**

**--login-user**

**--maintenance-address-cidr-blocks**

**--validate-only**:
If set, only validate the request, but do not actually perform the operation.

**--container-runtime**

**--enable-advanced-networking**

**--uri**

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
gcloud alpha container bare-metal clusters create
```

```
gcloud beta container bare-metal clusters create
```