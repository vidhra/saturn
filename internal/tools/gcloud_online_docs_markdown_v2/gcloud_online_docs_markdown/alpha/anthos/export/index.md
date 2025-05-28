# gcloud alpha anthos export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export)*

**NAME**

: **gcloud alpha anthos export - export current configuration of an Anthos cluster**

**SYNOPSIS**

: **`gcloud alpha anthos export` `[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export#CLUSTER)` [`[--project](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export#--project)`=`PROJECT_ID`] [`[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export#--location)`=`LOCATION`] [`[--output-directory](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export#--output-directory)`=`OUTPUT-DIR`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Export current configuration of an Anthos cluster.

**EXAMPLES**

: To export configuration from cluster 'my-cluster' to the local directory
`my-dir` using project 'my-project':

```
gcloud alpha anthos export my-cluster --project=my-project --output-directory=my-dir
```

**POSITIONAL ARGUMENTS**

: **`CLUSTER`**:
The cluster name from which to export the configurations.

**COMMONLY USED FLAGS**

: **--project**:
Project ID. Overrides the default `core/project` property value for
this command invocation.

**OTHER FLAGS**

: **--location**:
Specifies the Google Cloud location to use. If notspecified will use the current
compute/zone property.

**--output-directory**:
The output directory of the cluster resources. If empty will export files to
./CLUSTER_NAME

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta anthos export
```