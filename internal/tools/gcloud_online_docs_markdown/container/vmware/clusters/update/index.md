# gcloud container vmware clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update)*

**NAME**

: **gcloud container vmware clusters update - update an Anthos cluster on VMware**

**SYNOPSIS**

: **`gcloud container vmware clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--location)`=`LOCATION`) [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--admin-users)`=`ADMIN_USERS`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--description)`=`DESCRIPTION`] [`[--metal-lb-config-address-pools](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--metal-lb-config-address-pools)`=[`addresses`=`ADDRESSES`],[`avoid-buggy-ips`=`AVOID-BUGGY-IPS`],[`manual-assign`=`MANUAL-ASSIGN`],[`pool`=`POOL`]] [`[--static-ip-config-ip-blocks](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--static-ip-config-ip-blocks)`=[`gateway`=`GATEWAY`],[`ips`=`IPS`],[`netmask`=`NETMASK`]] [`[--upgrade-policy](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--upgrade-policy)`=[`control-plane-only`=`CONTROL-PLANE-ONLY`]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--validate-only)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--version)`=`VERSION`] [`[--add-annotations](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--add-annotations)`=[`KEY1`=`VALUE1`,`[KEY2](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#KEY2)`=`VALUE2`,…]     | `[--remove-annotations](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--remove-annotations)`=[`KEY1`,`[KEY2](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#KEY2)`,…]] [`[--cpus](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--cpus)`=`CPUS` `[--memory](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--memory)`=`MEMORY` `[--disable-auto-resize](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--disable-auto-resize)`     | `[--enable-auto-resize](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--enable-auto-resize)`] [`[--disable-aag-config](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--disable-aag-config)`     | `[--enable-aag-config](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--enable-aag-config)`] [`[--disable-auto-repair](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--disable-auto-repair)`     | `[--enable-auto-repair](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--enable-auto-repair)`] [`[--disable-vsphere-csi](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--disable-vsphere-csi)`     | `[--enable-vsphere-csi](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#--enable-vsphere-csi)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Anthos cluster on VMware.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container vmware clusters update my-cluster --location=us-west1
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
- set the property `container_vmware/location`.**

**FLAGS**

: **--admin-users**

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description for the resource.

**--metal-lb-config-address-pools**

**--static-ip-config-ip-blocks**

**--upgrade-policy**

**--validate-only**:
If set, only validate the request, but do not actually perform the operation.

**--version**:
Anthos Cluster on VMware version for the cluster resource

**--add-annotations**

**--cpus**

**--disable-aag-config**

**--disable-auto-repair**

**--disable-vsphere-csi**

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
gcloud alpha container vmware clusters update
```

```
gcloud beta container vmware clusters update
```