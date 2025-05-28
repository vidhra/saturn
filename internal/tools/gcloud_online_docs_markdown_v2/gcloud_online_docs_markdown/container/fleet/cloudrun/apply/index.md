# gcloud container fleet cloudrun apply  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply)*

**NAME**

: **gcloud container fleet cloudrun apply - deploy or update the CloudRun feature**

**SYNOPSIS**

: **`gcloud container fleet cloudrun apply` (`[--gke-cluster](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#--gke-cluster)`=`LOCATION`/`[CLUSTER_NAME](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#CLUSTER_NAME)`     | `[--gke-uri](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#--gke-uri)`=`GKE_URI`     | [`[--context](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#--context)`=`CONTEXT` : `[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#--kubeconfig)`=`KUBECONFIG`]) [`[--config](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#--config)`=`CONFIG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/cloudrun/apply#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deploy or update a user-specified config file of the CloudRun custom resource.
The config file should be a YAML file.

**EXAMPLES**

: To apply the CloudRun YAML file, run:

```
gcloud container fleet cloudrun apply --kubeconfig=/path/to/kubeconfig --config=/path/to/cloud-run-cr.yaml
```

**REQUIRED FLAGS**

: **--gke-cluster**

**OPTIONAL FLAGS**

: **--config**:
The path to CloudRun custom resource config file.

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
gcloud alpha container fleet cloudrun apply
```

```
gcloud beta container fleet cloudrun apply
```