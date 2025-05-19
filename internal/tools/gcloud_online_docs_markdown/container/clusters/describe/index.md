# gcloud container clusters describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe)*

**NAME**

: **gcloud container clusters describe - describe an existing cluster for running containers**

**SYNOPSIS**

: **`gcloud container clusters describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#NAME)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an existing cluster for running containers.

**EXAMPLES**

: To describe an existing cluster, run:

```
gcloud container clusters describe sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of this cluster.

**FLAGS**

: **--location**

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
gcloud alpha container clusters describe
```

```
gcloud beta container clusters describe
```