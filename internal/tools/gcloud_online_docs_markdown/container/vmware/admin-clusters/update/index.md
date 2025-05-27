# gcloud container vmware admin-clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update)*

**NAME**

: **gcloud container vmware admin-clusters update - update an Anthos on VMware admin cluster**

**SYNOPSIS**

: **`gcloud container vmware admin-clusters update` (`[ADMIN_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update#ADMIN_CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update#--async)`] [`[--required-platform-version](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update#--required-platform-version)`=`REQUIRED_PLATFORM_VERSION`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Anthos on VMware admin cluster.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container vmware admin-clusters update my-cluster --location=us-west1
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
- set the property `container_vmware/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--required-platform-version**:
Platform version required for upgrading an admin cluster or a user cluster. If
the current platform version is lower than the required version, the platform
version will be updated to the required version. If it is not installed in the
platform, download the required version bundle.

**--version**:
Anthos Cluster on VMware version for the cluster resource

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
gcloud alpha container vmware admin-clusters update
```

```
gcloud beta container vmware admin-clusters update
```