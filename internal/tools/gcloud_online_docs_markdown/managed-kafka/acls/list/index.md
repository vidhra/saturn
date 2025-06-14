# gcloud managed-kafka acls list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list)*

**NAME**

: **gcloud managed-kafka acls list - list all Managed Service for Apache Kafka acls in a given cluster**

**SYNOPSIS**

: **`gcloud managed-kafka acls list` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list#CLUSTER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list#--location)`=`LOCATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list#--limit)`=`LIMIT`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List all Managed Service for Apache Kafka acls in a given cluster. To specify
the maximum number of acls to list, use the --limit flag.

**EXAMPLES**

: To list acls in a cluster named mycluster located in us-central1, run the
following:

```
gcloud managed-kafka acls list mycluster --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Identifies the cluster which contains all the acls to be
listed. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
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
ID of the location of the Managed Service for Apache Kafka resource. See [https://cloud.google.com/managed-service-for-apache-kafka/docs/locations](https://cloud.google.com/managed-service-for-apache-kafka/docs/locations)
for a list of supported locations.
To set the `location` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

**API REFERENCE**

: This command uses the `managedkafka/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/managed-service-for-apache-kafka/docs](https://cloud.google.com/managed-service-for-apache-kafka/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha managed-kafka acls list
```

```
gcloud beta managed-kafka acls list
```