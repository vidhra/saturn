# gcloud container vmware clusters query-version-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config)*

**NAME**

: **gcloud container vmware clusters query-version-config - query versions for creating or upgrading an Anthos on VMware user cluster**

**SYNOPSIS**

: **`gcloud container vmware clusters query-version-config` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config#--location)`=`LOCATION`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config#--cluster)`=`CLUSTER`     | [`[--admin-cluster-membership](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config#--admin-cluster-membership)`=`ADMIN_CLUSTER_MEMBERSHIP` : `[--admin-cluster-membership-location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config#--admin-cluster-membership-location)`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION`; default="global" `[--admin-cluster-membership-project](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config#--admin-cluster-membership-project)`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/query-version-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Query versions for creating or upgrading an Anthos on VMware user cluster.

**EXAMPLES**

: To query all available versions in location `us-west1`, run:

```
gcloud container vmware clusters query-version-config --location=us-west1
```

To query versions for creating a cluster with an admin cluster membership named
`my-admin-cluster-membership` managed in project
`my-admin-cluster-project` and location `us-west`, run:

```
gcloud container vmware clusters query-version-config --location=us-west1 --admin-cluster-membership=my-admin-cluster-membership --admin-cluster-membership-project=my-admin-cluster-project
```

To query versions for upgrading a user cluster named
`my-user-cluster` in location `us-west1`, run:

```
gcloud container vmware clusters query-version-config --location=us-west1 --cluster=my-user-cluster
```

**FLAGS**

: **Location resource - Google Cloud location to query versions. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `container_vmware/location` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `container_vmware/location`.**

**Use cases for querying versions.
At most one of these can be specified:

**Upgrade an Anthos on VMware user cluster use case.

**Cluster resource - Cluster to query versions for upgrade. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `container_vmware/location`.

**--cluster**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `--cluster` on the command line.****

**--admin-cluster-membership****

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
gcloud alpha container vmware clusters query-version-config
```

```
gcloud beta container vmware clusters query-version-config
```