# gcloud redis clusters remove-cluster-endpoints  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints)*

**NAME**

: **gcloud redis clusters remove-cluster-endpoints - remove existing Memorystore cluster endpoints**

**SYNOPSIS**

: **`gcloud redis clusters remove-cluster-endpoints` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints#--region)`=`REGION`) `[--cluster-endpoint](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints#--cluster-endpoint)`=[`psc-connection`=`PSC-CONNECTION`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: To remove one cluster endpoint from an existing Redis cluster, two PSC
connections MUST be removed as a pair: one to the Redis cluster's discovery
service attachment and the other to its additional service attachment.
Multiple cluster endpoints COULD be removed simultaneously.
This command can fail for the following reasons:

- The cluster specified does not exist.
- Some connections in the to be removed list do not exist.

**EXAMPLES**

: To remove an endpoint from redis cluster, run:

```
gcloud redis clusters remove-cluster-endpoints my-redis-cluster remove-cluster-endpoints --cluster-endpoint='["psc-connection":[{"psc-connection-id":"$PSC_CONNECTION_ID"},{$ADDITIONAL_PSC_CONNECTION}]]' --cluster_endpoint=$ADDITIONAL_CLUSTER_ENDPOINT $PSCConnectionID SHOULD be extracted from forwarding rules. E.g. 75311697652483351
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the Memorystore Redis
cluster you want to update. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--cluster-endpoint**:
Required, Resource details of a redis cluster endpoint.

**`psc-connection`**:
Sets `psc-connection` value.

**`psc-connection-id`**:
Sets `psc-connection-id` value.

`Shorthand Example:`

```
--cluster-endpoint=psc-connection=[{psc-connection-id=string}] --cluster-endpoint=psc-connection=[{psc-connection-id=string}]
```

`JSON Example:`

```
--cluster-endpoint='[{"psc-connection": [{"psc-connection-id": "string"}]}]'
```

`File Example:`

```
--cluster-endpoint=path_to_file.(yaml|json)
```

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha redis clusters remove-cluster-endpoints
```

```
gcloud beta redis clusters remove-cluster-endpoints
```