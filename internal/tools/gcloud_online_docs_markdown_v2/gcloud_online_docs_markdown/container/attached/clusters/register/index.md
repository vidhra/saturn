# gcloud container attached clusters register  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register)*

**NAME**

: **gcloud container attached clusters register - register an Attached cluster**

**SYNOPSIS**

: **`gcloud container attached clusters register` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--location)`=`LOCATION`) `[--distribution](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--distribution)`=`DISTRIBUTION` `[--fleet-project](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--fleet-project)`=`FLEET_PROJECT` `[--platform-version](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--platform-version)`=`PLATFORM_VERSION` (`[--context](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--context)`=`CONTEXT` : `[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--kubeconfig)`=`KUBECONFIG`) (`[--has-private-issuer](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--has-private-issuer)`     | `[--issuer-url](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--issuer-url)`=`ISSUER_URL`) [`[--admin-groups](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--admin-groups)`=[`GROUP`,…]] [`[--admin-users](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--admin-users)`=[`USER`,…]] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--annotations)`=`ANNOTATION`,[`[ANNOTATION](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#ANNOTATION)`,…]] [`[--binauthz-evaluation-mode](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--binauthz-evaluation-mode)`=`BINAUTHZ_EVALUATION_MODE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--description)`=`DESCRIPTION`] [`[--enable-managed-prometheus](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--enable-managed-prometheus)`] [`[--logging](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--logging)`=`COMPONENT`,[`[COMPONENT](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#COMPONENT)`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--validate-only)`] [`[--disable-cloud-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--disable-cloud-monitoring)`     | `[--enable-cloud-monitoring](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--enable-cloud-monitoring)`] [`[--proxy-secret-name](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--proxy-secret-name)`=`PROXY_SECRET_NAME` `[--proxy-secret-namespace](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#--proxy-secret-namespace)`=`PROXY_SECRET_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Register an Attached cluster.

**EXAMPLES**

: Register a cluster to a fleet.
To register a cluster with a private OIDC issuer, run:

```
gcloud container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --has-private-issuer
```

To register a cluster with a public OIDC issuer, run:

```
gcloud container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --issuer-url=https://ISSUER_URL
```

To specify a kubeconfig file, run:

```
gcloud container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --has-private-issuer --kubeconfig=KUBECONFIG_PATH
```

To register and set cluster admin users, run:

```
gcloud container attached clusters register my-cluster --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-project=FLEET_PROJECT_NUM --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --issuer-url=https://ISSUER_URL --admin-users=USER1,USER2
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - cluster to register. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
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

**REQUIRED FLAGS**

: **--distribution**:
Set the base platform type of the cluster to attach.
Examples:

```
gcloud container attached clusters register --distribution=aks
gcloud container attached clusters register --distribution=eks
gcloud container attached clusters register --distribution=generic
```

**--fleet-project**:
ID or number of the Fleet host project where the cluster is registered.

**--platform-version**:
Platform version to use for the cluster.
To retrieve a list of valid versions, run:

```
gcloud alpha container attached get-server-config --location=LOCATION
```

Replace ``LOCATION`` with the target Google
Cloud location for the cluster.

**--context**

**--has-private-issuer**

**OPTIONAL FLAGS**

: **--admin-groups**:
Groups of users that can perform operations as a cluster administrator.

**--admin-users**:
Users that can perform operations as a cluster administrator.

**--annotations**:
Annotations for the cluster.

**--binauthz-evaluation-mode**:
Set Binary Authorization evaluation mode for this cluster.
`BINAUTHZ_EVALUATION_MODE` must be one of:
`DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`.

**--description**:
Description for the cluster.

**--enable-managed-prometheus**:
Enables managed collection for Managed Service for Prometheus in the cluster.
See [https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke](https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke)
for more info.
Managed Prometheus is enabled by default for cluster versions 1.27 or greater,
use --no-enable-managed-prometheus to disable.

**--logging**:
Set the components that have logging enabled.
Examples:

```
gcloud container attached clusters register --logging=SYSTEM
gcloud container attached clusters register --logging=SYSTEM,WORKLOAD
gcloud container attached clusters register --logging=NONE
```

`COMPONENT` must be one of: `NONE`,
`SYSTEM`, `WORKLOAD`.

**--validate-only**:
Validate the cluster to create, but don't actually perform it.

**--disable-cloud-monitoring**

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
gcloud alpha container attached clusters register
```