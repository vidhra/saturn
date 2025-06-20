# gcloud container vmware admin-clusters enroll  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll)*

**NAME**

: **gcloud container vmware admin-clusters enroll - enroll an Anthos on VMware admin cluster**

**SYNOPSIS**

: **`gcloud container vmware admin-clusters enroll` (`[ADMIN_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll#ADMIN_CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll#--location)`=`LOCATION`) (`[--admin-cluster-membership](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll#--admin-cluster-membership)`=`ADMIN_CLUSTER_MEMBERSHIP` : `[--admin-cluster-membership-location](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll#--admin-cluster-membership-location)`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION`; default="global") [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/vmware/admin-clusters/enroll#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Enroll an Anthos on VMware admin cluster.

**EXAMPLES**

: To enroll a cluster named ``my-cluster``
managed in location ``us-west1`` with admin
cluster membership of
``projects/my-project/locations/us-west1/memberships/my-admin-cluster-membership``,
run:

```
gcloud container vmware admin-clusters enroll my-cluster --location=us-west1 --admin-cluster-membership=projects/my-project/locations/us-west1/memberships/my-admin-cluster-membership
```

**POSITIONAL ARGUMENTS**

: **Admin cluster resource - admin cluster to enroll The arguments in this group can
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

**REQUIRED FLAGS**

: **Admin cluster membership resource - membership of the admin cluster. Membership
can be the membership ID or the full resource name. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--admin-cluster-membership` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

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
command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha container vmware admin-clusters enroll
```

```
gcloud beta container vmware admin-clusters enroll
```