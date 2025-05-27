# gcloud container get-server-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/get-server-config](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config)*

**NAME**

: **gcloud container get-server-config - get Kubernetes Engine server config**

**SYNOPSIS**

: **`gcloud container get-server-config` [`[--location](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#--location)`=`LOCATION`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#--region)`=`REGION`     | `[--zone](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#--zone)`=`ZONE`, `[-z](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#-z)` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#ZONE)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#--limit)`=`LIMIT`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/get-server-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get Kubernetes Engine server config.

**EXAMPLES**

: To get the Kubernetes Engine server configuration, run:

```
gcloud container get-server-config
```

**FLAGS**

: **--location**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha container get-server-config
```

```
gcloud beta container get-server-config
```