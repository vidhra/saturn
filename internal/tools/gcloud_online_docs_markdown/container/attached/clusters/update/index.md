# gcloud container attached clusters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update)*

**NAME**

: **gcloud container attached clusters update - update an Attached cluster**

**SYNOPSIS**

: **`gcloud container attached clusters update` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--location)`=`LOCATION`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#ANNOTATION)`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--async)`] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--clear-description](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--clear-description)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--description)`=`DESCRIPTION`] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--logging)`=`COMPONENT`,[`[COMPONENT](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#COMPONENT)`,…]] [`[--platform-version](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--platform-version)`=`PLATFORM_VERSION`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--validate-only)`] [`[--admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--admin-groups)`=[`GROUP`,…]     | `[--clear-admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--clear-admin-groups)`] [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--admin-users)`=[`USER`,…]     | `[--clear-admin-users](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--clear-admin-users)`] [`[--disable-cloud-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--disable-cloud-monitoring)`     | `[--enable-cloud-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--enable-cloud-monitoring)`] [`[--disable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--disable-managed-prometheus)`     | `[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--enable-managed-prometheus)`] [`[--proxy-secret-name](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--proxy-secret-name)`=`PROXY_SECRET_NAME` `[--proxy-secret-namespace](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#--proxy-secret-namespace)`=`PROXY_SECRET_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Attached cluster.

**EXAMPLES**

: To update a cluster named ``my-cluster``
managed in location ``us-west1``, run:

```
gcloud container attached clusters update my-cluster --location=us-west1 --description=testcluster
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to update. The arguments in this group can be used to
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
- set the property `container_attached/location`.**

**FLAGS**

: **--annotations**:
Annotations for the cluster.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--binauthz-evaluation-mode**:
Set Binary Authorization evaluation mode for this cluster.
`BINAUTHZ_EVALUATION_MODE` must be one of:
`DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`.

**--clear-description**:
Clear the description for the cluster.

**--description**:
Description for the cluster.

**--logging**:
Set the components that have logging enabled.
Examples:

```
gcloud container attached clusters update --logging=SYSTEM
gcloud container attached clusters update --logging=SYSTEM,WORKLOAD
gcloud container attached clusters update --logging=NONE
```

`COMPONENT` must be one of: `NONE`,
`SYSTEM`, `WORKLOAD`.

**--platform-version**:
Platform version to use for the cluster.
To retrieve a list of valid versions, run:

```
gcloud alpha container attached get-server-config --location=LOCATION
```

Replace ``LOCATION`` with the target Google
Cloud location for the cluster.

**--validate-only**:
Validate the update of the cluster, but don't actually perform it.

**--admin-groups**

**--admin-users**

**--disable-cloud-monitoring**

**--disable-managed-prometheus**

**--proxy-secret-name**

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
gcloud alpha container attached clusters update
```