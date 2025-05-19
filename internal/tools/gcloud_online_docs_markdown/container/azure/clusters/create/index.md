# gcloud container azure clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create)*

**NAME**

: **gcloud container azure clusters create - create an Anthos cluster on Azure**

**SYNOPSIS**

: **`gcloud container azure clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--location)`=`LOCATION`) `[--azure-region](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--azure-region)`=`AZURE_REGION` `[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--cluster-version)`=`CLUSTER_VERSION` `[--fleet-project](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--fleet-project)`=`FLEET_PROJECT` `[--pod-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--pod-address-cidr-blocks)`=`POD_ADDRESS_CIDR_BLOCKS` `[--resource-group-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--resource-group-id)`=`RESOURCE_GROUP_ID` `[--service-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--service-address-cidr-blocks)`=`SERVICE_ADDRESS_CIDR_BLOCKS` `[--ssh-public-key](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--ssh-public-key)`=`SSH_PUBLIC_KEY` `[--vnet-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--vnet-id)`=`VNET_ID` (`[--client](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--client)`=`CLIENT`     | `[--azure-application-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--azure-application-id)`=`AZURE_APPLICATION_ID` `[--azure-tenant-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--azure-tenant-id)`=`AZURE_TENANT_ID`) [`[--admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--admin-groups)`=[`GROUP`,…]] [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--admin-users)`=`USER`,[`[USER](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#USER)`,…]] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#ANNOTATION)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--async)`] [`[--config-encryption-key-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--config-encryption-key-id)`=`CONFIG_ENCRYPTION_KEY_ID`] [`[--config-encryption-public-key](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--config-encryption-public-key)`=`CONFIG_ENCRYPTION_PUBLIC_KEY`] [`[--database-encryption-key-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--database-encryption-key-id)`=`DATABASE_ENCRYPTION_KEY_ID`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--description)`=`DESCRIPTION`] [`[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--enable-managed-prometheus)`] [`[--endpoint-subnet-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--endpoint-subnet-id)`=`ENDPOINT_SUBNET_ID`] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--logging)`=`COMPONENT`,[`[COMPONENT](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#COMPONENT)`,…]] [`[--main-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--main-volume-size)`=`MAIN_VOLUME_SIZE`] [`[--replica-placements](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--replica-placements)`=[`REPLICA_PLACEMENT`,…]] [`[--root-volume-size](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--root-volume-size)`=`ROOT_VOLUME_SIZE`] [`[--service-load-balancer-subnet-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--service-load-balancer-subnet-id)`=`SERVICE_LOAD_BALANCER_SUBNET_ID`] [`[--subnet-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--subnet-id)`=`SUBNET_ID`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#TAG)`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--validate-only)`] [`[--vm-size](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--vm-size)`=`VM_SIZE`] [`[--proxy-resource-group-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--proxy-resource-group-id)`=`PROXY_RESOURCE_GROUP_ID` `[--proxy-secret-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--proxy-secret-id)`=`PROXY_SECRET_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Create an Anthos cluster on Azure.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To create a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container azure clusters create my-cluster --location=us-west1 --azure-region=AZURE_REGION --cluster-version=CLUSTER_VERSION --client=CLIENT --pod-address-cidr-blocks=POD_ADDRESS_CIDR_BLOCKS --resource-group-id=RESOURCE_GROUP_ID --ssh-public-key=SSH_PUBLIC_KEY --subnet-id=SUBNET_ID --vnet-id=VNET_ID
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Azure cluster to create. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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
- set the property `container_azure/location`.**

**REQUIRED FLAGS**

: **--azure-region**:
Azure location to deploy the cluster. Refer to your Azure subscription for
available locations.

**--cluster-version**:
Kubernetes version to use for the cluster.

**--fleet-project**:
ID or number of the Fleet host project where the cluster is registered.

**--pod-address-cidr-blocks**:
IP address range for the pods in this cluster in CIDR notation (e.g.
10.0.0.0/8).

**--resource-group-id**:
ID of the Azure Resource Group to associate the cluster with.

**--service-address-cidr-blocks**:
IP address range for the services IPs in CIDR notation (e.g. 10.0.0.0/8).

**--ssh-public-key**:
SSH public key to use for authentication.

**--vnet-id**:
ID of the Azure Virtual Network to associate with the cluster.

**Authentication configuration
Exactly one of these must be specified:

**Client resource - Azure client to use for cluster creation. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--client` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--client` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_azure/location`.

**--client**:
ID of the client or fully qualified identifier for the client.
To set the `client` attribute:

- provide the argument `--client` on the command line.**

**--azure-application-id****

**OPTIONAL FLAGS**

: **--admin-groups**:
Groups of users that can perform operations as a cluster administrator.

**--admin-users**:
Users that can perform operations as a cluster administrator. If not specified,
the value of property core/account is used.

**--annotations**:
Annotations for the cluster.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--config-encryption-key-id**:
URL the of the Azure Key Vault key (with its version) to use to encrypt /
decrypt config data.

**--config-encryption-public-key**:
RSA key of the Azure Key Vault public key to use for encrypting config data.

**--database-encryption-key-id**:
URL the of the Azure Key Vault key (with its version) to use to encrypt /
decrypt cluster secrets.

**--description**:
Description for the cluster.

**--enable-managed-prometheus**:
Enables managed collection for Managed Service for Prometheus in the cluster.
See [https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke)
for more info.
Managed Prometheus is enabled by default for cluster versions 1.27 or greater,
use --no-enable-managed-prometheus to disable.

**--endpoint-subnet-id**:
ARM ID of the subnet where the control plane load balancer is deployed. When
unspecified, it defaults to the control plane subnet ID.

**--logging**:
Set the components that have logging enabled.
Examples:

```
gcloud container azure clusters create --logging=SYSTEM
gcloud container azure clusters create --logging=SYSTEM,WORKLOAD
```

`COMPONENT` must be one of: `SYSTEM`,
`WORKLOAD`.

**--main-volume-size**:
Size of the main volume. The value must be a whole number followed by a size
unit of `GB` for gigabyte, or `TB` for terabyte. If no
size unit is specified, GB is assumed.

**--replica-placements**:
Placement info for the control plane replicas. Replica placement is of format
subnetid:zone, for example subnetid12345:1

**--root-volume-size**:
Size of the root volume. The value must be a whole number followed by a size
unit of `GB` for gigabyte, or `TB` for terabyte. If no
size unit is specified, GB is assumed.

**--service-load-balancer-subnet-id**:
ARM ID of the subnet where Kubernetes private service type load balancers are
deployed, when the Service lacks a subnet annotation.

**--subnet-id**:
Subnet ID of an existing VNET to use for the cluster control plane.

**--tags**:
Applies the given tags (comma separated) on the cluster. Example:

```
gcloud container azure clusters create EXAMPLE_CLUSTER --tags=tag1=one,tag2=two
```

**--validate-only**:
Validate the creation of the cluster, but don't actually perform it.

**--vm-size**:
Azure Virtual Machine Size (e.g. Standard_DS1_v).

**--proxy-resource-group-id**

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

: This variant is also available:

```
gcloud alpha container azure clusters create
```