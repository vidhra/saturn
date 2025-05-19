# gcloud container bare-metal admin-clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update)*

**NAME**

: **gcloud container bare-metal admin-clusters update - update an Anthos on bare metal admin cluster**

**SYNOPSIS**

: **`gcloud container bare-metal admin-clusters update` (`[ADMIN_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#ADMIN_CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--async)`] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--description)`=`DESCRIPTION`] [`[--enable-application-logs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--enable-application-logs)`] [`[--island-mode-service-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--island-mode-service-address-cidr-blocks)`=`SERVICE_ADDRESS`,[…]] [`[--login-user](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--login-user)`=`LOGIN_USER`] [`[--maintenance-address-cidr-blocks](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--maintenance-address-cidr-blocks)`=[`MAINTENANCE_ADDRESS_CIDR_BLOCKS`,…]] [`[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--max-pods-per-node)`=`MAX_PODS_PER_NODE`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--validate-only)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--version)`=`VERSION`] [`[--api-server-args](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--api-server-args)`=[`KEY`=`VALUE`,…] `[--control-plane-node-configs](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--control-plane-node-configs)`=[`labels`=`LABELS`],[`node-ip`=`NODE-IP`] `[--control-plane-node-labels](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--control-plane-node-labels)`=[`KEY`=`VALUE`,…] `[--control-plane-node-taints](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--control-plane-node-taints)`=[`KEY`=`VALUE`:`[EFFECT](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#EFFECT)`,…]] [`[--no-proxy](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--proxy)`=[`NO_PROXY`,…] `[--uri](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#--uri)`=`URI`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Anthos on bare metal admin cluster.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container bare-metal admin-clusters update my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Admin cluster resource - admin cluster to update The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `admin_cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ADMIN_CLUSTER`**:
ID of the admin_cluster or fully qualified identifier for the admin_cluster.
To set the `admin_cluster` attribute:

- provide the argument `admin_cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the admin_cluster.
To set the `location` attribute:

- provide the argument `admin_cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_bare_metal/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--binauthz-evaluation-mode**:
Set Binary Authorization evaluation mode for this cluster.
`BINAUTHZ_EVALUATION_MODE` must be one of:
`DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`.

**--description**:
Description for the resource.

**--enable-application-logs**

**--island-mode-service-address-cidr-blocks**

**--login-user**

**--maintenance-address-cidr-blocks**

**--max-pods-per-node**

**--validate-only**:
If set, only validate the request, but do not actually perform the operation.

**--version**:
Anthos cluster on bare metal version for the admin cluster resource.

**--api-server-args**

**--no-proxy**

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
gcloud alpha container bare-metal admin-clusters update
```

```
gcloud beta container bare-metal admin-clusters update
```