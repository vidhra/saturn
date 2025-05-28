# gcloud redis instances get-auth-string  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string](https://cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string)*

**NAME**

: **gcloud redis instances get-auth-string - show AUTH string for a Memorystore Redis instance**

**SYNOPSIS**

: **`gcloud redis instances get-auth-string` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show AUTH string for a Memorystore Redis instance.
Result is empty if AUTH is disabled for the instance.
This command can fail for the following reasons:

- The instance specified does not exist.
- The active account does not have permission to view the AUTH string

**EXAMPLES**

: To display the AUTH string for an instance with the name
`my-redis-instance` in the default region, run:

```
gcloud redis instances get-auth-string my-redis-instance
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Memorystore Redis
instance you want to view the AUTH string for. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
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
gcloud alpha redis instances get-auth-string
```

```
gcloud beta redis instances get-auth-string
```