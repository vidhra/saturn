# gcloud container vmware clusters upgrade  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/upgrade](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/upgrade)*

**NAME**

: **gcloud container vmware clusters upgrade - centrally upgrade an Anthos cluster on VMware**

**SYNOPSIS**

: **`gcloud container vmware clusters upgrade` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/upgrade#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/upgrade#--location)`=`LOCATION`) `[--version](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/upgrade#--version)`=`VERSION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/upgrade#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Centrally upgrade an Anthos cluster on VMware.

**EXAMPLES**

: To upgrade a cluster named ``my-cluster``
managed in location ``us-west1`` to version
``1.13.0-gke.1000``, run:

```
gcloud container vmware clusters upgrade my-cluster --location=us-west1 --version=1.13.0-gke.1000
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to upgrade The arguments in this group can be used to
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
gcloud alpha container vmware clusters upgrade
```

```
gcloud beta container vmware clusters upgrade
```