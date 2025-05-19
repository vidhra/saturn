# gcloud container clusters get-upgrade-info  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info)*

**NAME**

: **gcloud container clusters get-upgrade-info - get information about upgrades for existing clusters including auto upgrade status, upgrade history, upgrade targets, and end of support timelines**

**SYNOPSIS**

: **`gcloud container clusters get-upgrade-info` `[NAME](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#NAME)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#ZONE)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-upgrade-info#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get information about upgrades for existing clusters including auto upgrade
status, upgrade history, upgrade targets, and end of support timelines.

**EXAMPLES**

: To get upgrade information for an existing cluster, run:

```
gcloud container clusters get-upgrade-info sample-cluster
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
The name of your existing cluster.

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
gcloud alpha container clusters get-upgrade-info
```

```
gcloud beta container clusters get-upgrade-info
```