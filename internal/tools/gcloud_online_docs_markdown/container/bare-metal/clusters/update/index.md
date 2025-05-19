# gcloud container bare-metal clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update)*

**NAME**

: **gcloud container bare-metal clusters update - update an Anthos cluster on bare metal**

**SYNOPSIS**

: **`gcloud container bare-metal clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--location)`=`LOCATION`) [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--admin-users)`=`ADMIN_USERS`] [`[--allow-missing](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--allow-missing)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--async)`] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--description)`=`DESCRIPTION`] [`[--enable-application-logs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-application-logs)`] [`[--login-user](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--login-user)`=`LOGIN_USER`] [`[--maintenance-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--maintenance-address-cidr-blocks)`=[`MAINTENANCE_ADDRESS_CIDR_BLOCKS`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--validate-only)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--version)`=`VERSION`] [`[--add-annotations](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--add-annotations)`=[`KEY1`=`VALUE1`,`[KEY2](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#KEY2)`=`VALUE2`,…]     | `[--remove-annotations](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--remove-annotations)`=[`KEY1`,`[KEY2](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#KEY2)`,…]] [`[--api-server-args](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--api-server-args)`=[`KEY`=`VALUE`,…] `[--control-plane-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-node-configs)`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] `[--control-plane-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-node-labels)`=[`KEY`=`VALUE`,…] `[--control-plane-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#EFFECT)`,…] `[--control-plane-registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-registry-burst)`=`CONTROL_PLANE_REGISTRY_BURST` `[--control-plane-registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--control-plane-registry-pull-qps)`=`CONTROL_PLANE_REGISTRY_PULL_QPS` `[--disable-control-plane-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-control-plane-serialize-image-pulls)`     | `[--enable-control-plane-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-control-plane-serialize-image-pulls)`] [`[--bgp-address-pools](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-address-pools)`=[`addresses`=`ADDRESSES`],[`avoid-buggy-ips`=`AVOID-BUGGY-IPS`],[`manual-assign`=`MANUAL-ASSIGN`],[`pool`=`POOL`] `[--bgp-asn](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-asn)`=`BGP_ASN` `[--bgp-peer-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-peer-configs)`=[`asn`=`ASN`,`ip`=`IP`,`control-plane-nodes`=`NODE_IP_1`;`[NODE_IP_2](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#NODE_IP_2)`,…] `[--bgp-load-balancer-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-node-configs)`=[`node-ip`=`IP`,`labels`=`KEY1`=`VALUE1`;`[KEY2](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#KEY2)`=`VALUE2`,…] `[--bgp-load-balancer-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-node-labels)`=[`KEY`=`VALUE`,…] `[--bgp-load-balancer-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#EFFECT)`,…] `[--bgp-load-balancer-registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-registry-burst)`=`BGP_LOAD_BALANCER_REGISTRY_BURST` `[--bgp-load-balancer-registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--bgp-load-balancer-registry-pull-qps)`=`BGP_LOAD_BALANCER_REGISTRY_PULL_QPS` `[--disable-bgp-load-balancer-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-bgp-load-balancer-serialize-image-pulls)`     | `[--enable-bgp-load-balancer-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-bgp-load-balancer-serialize-image-pulls)`     | `[--metal-lb-address-pools](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-address-pools)`=[`addresses`=`ADDRESSES`],[`avoid-buggy-ips`=`AVOID-BUGGY-IPS`],[`manual-assign`=`MANUAL-ASSIGN`],[`pool`=`POOL`] `[--metal-lb-load-balancer-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-node-configs)`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] `[--metal-lb-load-balancer-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-node-labels)`=[`KEY`=`VALUE`,…] `[--metal-lb-load-balancer-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#EFFECT)`,…] `[--metal-lb-load-balancer-registry-burst](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-registry-burst)`=`METAL_LB_LOAD_BALANCER_REGISTRY_BURST` `[--metal-lb-load-balancer-registry-pull-qps](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--metal-lb-load-balancer-registry-pull-qps)`=`METAL_LB_LOAD_BALANCER_REGISTRY_PULL_QPS` `[--disable-metal-lb-load-balancer-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-metal-lb-load-balancer-serialize-image-pulls)`     | `[--enable-metal-lb-load-balancer-serialize-image-pulls](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-metal-lb-load-balancer-serialize-image-pulls)`] [`[--island-mode-service-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--island-mode-service-address-cidr-blocks)`=`SERVICE_ADDRESS`,[…] `[--disable-sr-iov-config](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--disable-sr-iov-config)`     | `[--enable-sr-iov-config](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#--enable-sr-iov-config)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Anthos cluster on bare metal.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container bare-metal clusters update my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to update The arguments in this group can be used to
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

**FLAGS**

: **--admin-users**

**--allow-missing**:
If set, and the Anthos cluster on bare metal is not found, the update request
will try to create a new cluster with the provided configuration.

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

**--version**:
Anthos cluster on bare metal version for the user cluster resource.

**--add-annotations**

**--api-server-args**

**--bgp-address-pools**

**--island-mode-service-address-cidr-blocks**

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
gcloud alpha container bare-metal clusters update
```

```
gcloud beta container bare-metal clusters update
```