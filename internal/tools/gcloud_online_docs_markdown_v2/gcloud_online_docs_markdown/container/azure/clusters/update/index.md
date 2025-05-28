# gcloud container azure clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update)*

**NAME**

: **gcloud container azure clusters update - update an Anthos cluster on Azure**

**SYNOPSIS**

: **`gcloud container azure clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--location)`=`LOCATION`) [`[--admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--admin-groups)`=[`GROUP`,…]] [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--admin-users)`=`USER`,[`[USER](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#USER)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--async)`] [`[--cluster-version](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--cluster-version)`=`CLUSTER_VERSION`] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--logging)`=`COMPONENT`,[`[COMPONENT](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#COMPONENT)`,…]] [`[--ssh-public-key](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--ssh-public-key)`=`SSH_PUBLIC_KEY`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--validate-only)`] [`[--vm-size](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--vm-size)`=`VM_SIZE`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#ANNOTATION)`,…]     | `[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--clear-annotations)`] [`[--clear-description](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--clear-description)`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--description)`=`DESCRIPTION`] [`[--client](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--client)`=`CLIENT`     | `[--azure-application-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--azure-application-id)`=`AZURE_APPLICATION_ID` `[--azure-tenant-id](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--azure-tenant-id)`=`AZURE_TENANT_ID` `[--clear-client](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--clear-client)`] [`[--disable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--disable-managed-prometheus)`     | `[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#--enable-managed-prometheus)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/azure/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(DEPRECATED)` Update an Anthos cluster on Azure.
This command is deprecated. See [https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
for more details.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container azure clusters update my-cluster --location=us-west1 --cluster-version=CLUSTER_VERSION --client=CLIENT
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Azure cluster to update. The arguments in this group can be
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

**FLAGS**

: **--admin-groups**:
Groups of users that can perform operations as a cluster administrator.

**--admin-users**:
Users that can perform operations as a cluster administrator.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cluster-version**:
Kubernetes version to use for the cluster.

**--logging**:
Set the components that have logging enabled.
Examples:

```
gcloud container azure clusters update --logging=SYSTEM
gcloud container azure clusters update --logging=SYSTEM,WORKLOAD
```

`COMPONENT` must be one of: `SYSTEM`,
`WORKLOAD`.

**--ssh-public-key**:
SSH public key to use for authentication.

**--validate-only**:
Validate the update of the cluster, but don't actually perform it.

**--vm-size**:
Azure Virtual Machine Size (e.g. Standard_DS1_v).

**--annotations**

**--clear-description**

**Authentication configuration
At most one of these can be specified:

**Client resource - Azure client to use for cluster update. This represents a
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

**--disable-managed-prometheus**

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
gcloud alpha container azure clusters update
```