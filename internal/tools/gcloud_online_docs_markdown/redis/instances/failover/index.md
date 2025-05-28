# gcloud redis instances failover  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover)*

**NAME**

: **gcloud redis instances failover - failover a standard tier Cloud Memorystore for Redis instance from the master node to its replica**

**SYNOPSIS**

: **`gcloud redis instances failover` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover#--async)`] [`[--data-protection-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover#--data-protection-mode)`=`DATA_PROTECTION_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Failover a standard tier Cloud Memorystore for Redis instance from the master
node to its replica.

**EXAMPLES**

: To failover an instance with the name 'my-redis-instance' in region
'us-central-1', run:

```
gcloud redis instances failover my-redis-instance --region=us-central1
```

To failover an instance with the name 'my-redis-instance' in region
'us-central-1' without attempting to limit data loss, run:

```
gcloud redis instances failover my-redis-instance --region=us-central1 --data-protection-mode=force-data-loss
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the standard tier Cloud
Memorystore for Redis instance you want to failover. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Redis region of the instance. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--data-protection-mode**:
Data protection mode to use for the failover. If not specified, defaults to
'limited-data-loss'. `DATA_PROTECTION_MODE` must be one
of:

**`force-data-loss`**:
Failover without data loss protection. Can cause significant data loss.

**`limited-data-loss`**:
Failover with data loss protection that ensures loss is within system
thresholds.

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
gcloud alpha redis instances failover
```

```
gcloud beta redis instances failover
```