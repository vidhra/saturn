# gcloud redis clusters get-cluster-certificate-authority  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/get-cluster-certificate-authority](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/get-cluster-certificate-authority)*

**NAME**

: **gcloud redis clusters get-cluster-certificate-authority - get the certificate authority information for a Memorystore for Redis Cluster instance**

**SYNOPSIS**

: **`gcloud redis clusters get-cluster-certificate-authority` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/get-cluster-certificate-authority#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/get-cluster-certificate-authority#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/get-cluster-certificate-authority#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the certificate authority information for a Memorystore for Redis Cluster
instance.
This command can fail for the following reasons:

- The cluster specified does not exist.
- The active account does not have permission to access the given cluster.

**EXAMPLES**

: To get the metadata for a cluster with the name `my-redis-cluster` in
the default region, run:

```
gcloud redis clusters get-cluster-certificate-authority my-redis-cluster
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the cluster. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
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

**--region**:
The name of the Redis region of the cluster. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

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

**API REFERENCE**

: This command uses the `redis/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/memorystore/docs/redis/](https://cloud.google.com/memorystore/docs/redis/)

**NOTES**

: These variants are also available:

```
gcloud alpha redis clusters get-cluster-certificate-authority
```

```
gcloud beta redis clusters get-cluster-certificate-authority
```