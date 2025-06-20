# gcloud edge-cloud container clusters get-credentials  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials)*

**NAME**

: **gcloud edge-cloud container clusters get-credentials - get credentials of an edge-container cluster**

**SYNOPSIS**

: **`gcloud edge-cloud container clusters get-credentials` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials#--location)`=`LOCATION`) [`[--auth-provider-cmd-path](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials#--auth-provider-cmd-path)`=`AUTH_PROVIDER_CMD_PATH`] [`[--offline-credential](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials#--offline-credential)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/clusters/get-credentials#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Fetch credentials for a running Edge Container cluster. This command updates a
kubeconfig file with appropriate credentials and endpoint information to point
kubectl at a specific Edge Container cluster. By default, credentials are
written to ``HOME/.kube/config``. You can
provide an alternate path by setting the
``KUBECONFIG`` environment variable. If
``KUBECONFIG`` contains multiple paths, the
first one is used. This command enables switching to a specific cluster, when
working with multiple clusters. It can also be used to access a previously
created cluster from a new workstation. The command will configure kubectl to
automatically refresh its credentials using the same identity as the gcloud
command-line tool. See [https://cloud.google.com/kubernetes-engine/docs/kubectl](https://cloud.google.com/kubernetes-engine/docs/kubectl)
for kubectl documentation.

**EXAMPLES**

: To get credentials of a cluster named
``my-cluster`` managed in location
``us-west1``, run:
```
gcloud edge-cloud container clusters get-credentials my-cluster --location=us-west1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Edge Container cluster to get credentials. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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
- provide the argument `--location` on the command line.**

**FLAGS**

: **--auth-provider-cmd-path**:
Path to the gcloud executable for the auth provider field in kubeconfig.

**--offline-credential**:
Once specified, an offline credential will be generated for the cluster.

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
gcloud alpha edge-cloud container clusters get-credentials
```