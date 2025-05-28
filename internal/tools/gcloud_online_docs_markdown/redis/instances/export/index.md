# gcloud redis instances export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances/export](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export)*

**NAME**

: **gcloud redis instances export - export data from a Memorystore Redis instance to Google Cloud Storage**

**SYNOPSIS**

: **`gcloud redis instances export` `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export#DESTINATION)` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Export data from a Memorystore Redis instance to Google Cloud Storage.

**EXAMPLES**

: To export the instance with the name `my-redis-instance` in region
`us-central1` to Cloud Storage object
gs://my-bucket/my-redis-instance.rdb run:

```
gcloud redis instances export gs://my-bucket/my-redis-instance.rdb my-redis-instance --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`DESTINATION`**:
The Cloud Storage object path to export the instance to. Must have the redis DB
file extension *.rdb`.`

**Instance resource - Arguments and flags that specify the Memorystore Redis
instance you want to export. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
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

**--region`=`REGION``**:
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
gcloud alpha redis instances export
```

```
gcloud beta redis instances export
```