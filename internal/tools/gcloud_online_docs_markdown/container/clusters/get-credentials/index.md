# gcloud container clusters get-credentials  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials)*

**NAME**

: **gcloud container clusters get-credentials - fetch credentials for a running cluster**

**SYNOPSIS**

: **`gcloud container clusters get-credentials` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#NAME)` [`[--dns-endpoint](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#--dns-endpoint)`] [`[--internal-ip](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#--internal-ip)`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud container clusters get-credentials updates a `kubeconfig` file
with appropriate credentials and endpoint information to point
`kubectl` at a specific cluster in Google Kubernetes Engine.
It takes a project and a zone as parameters, passed through by set defaults or
flags. By default, credentials are written to `HOME/.kube/config`.
You can provide an alternate path by setting the `KUBECONFIG`
environment variable. If `KUBECONFIG` contains multiple paths, the
first one is used.
This command enables switching to a specific cluster, when working with multiple
clusters. It can also be used to access a previously created cluster from a new
workstation.
By default, gcloud container clusters get-credentials will configure kubectl to
automatically refresh its credentials using the same identity as gcloud. If you
are running kubectl as part of an application, it is recommended to use [application
default credentials](https://cloud.google.com/docs/authentication/production). To configure a `kubeconfig` file to use
application default credentials, set the
container/use_application_default_credentials [Cloud SDK property](https://cloud.google.com/sdk/docs/properties) to
true before running gcloud container clusters get-credentials
See [https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
for kubectl usage with Google Kubernetes Engine and [https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
for available kubectl commands.

**EXAMPLES**

: To switch to working on your cluster 'sample-cluster', run:

```
gcloud container clusters get-credentials sample-cluster --location=us-central1-f
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the cluster to get credentials for. Overrides the default
`container/cluster` property value for this command invocation.

**FLAGS**

: **--dns-endpoint**:
Whether to use the DNS-based endpoint for the cluster address.

**--internal-ip**:
Whether to use the internal IP address of the cluster endpoint.

**--location**

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
gcloud alpha container clusters get-credentials
```

```
gcloud beta container clusters get-credentials
```