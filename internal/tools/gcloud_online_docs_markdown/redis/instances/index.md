# gcloud redis instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances](https://cloud.google.com/sdk/gcloud/reference/redis/instances)*

**NAME**

: **gcloud redis instances - manage Cloud Memorystore Redis instances**

**SYNOPSIS**

: **`gcloud redis instances` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/redis/instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To create an instance with the name `my-redis-instance`, run:

```
gcloud redis instances create my-redis-instance
```

To delete an instance with the name `my-redis-instance`, run:

```
gcloud redis instances delete my-redis-instance
```

To display the details for an instance with the name
`my-redis-instance`, run:

```
gcloud redis instances describe my-redis-instance
```

To list all the instances, run:

```
gcloud redis instances list
```

To set the label `env` to `prod` for an instance with the
name `my-redis-instance`, run:

```
gcloud redis instances my-redis-instance --update-labels=env=prod
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create)`**:
Create a Memorystore Redis instance.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/redis/instances/delete)`**:
Delete a Redis instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/redis/instances/describe)`**:
Show metadata for a Memorystore Redis instance.

**`[export](https://cloud.google.com/sdk/gcloud/reference/redis/instances/export)`**:
Export data from a Memorystore Redis instance to Google Cloud Storage.

**`[failover](https://cloud.google.com/sdk/gcloud/reference/redis/instances/failover)`**:
Failover a standard tier Cloud Memorystore for Redis instance from the master
node to its replica.

**`[get-auth-string](https://cloud.google.com/sdk/gcloud/reference/redis/instances/get-auth-string)`**:
Show AUTH string for a Memorystore Redis instance.

**`[import](https://cloud.google.com/sdk/gcloud/reference/redis/instances/import)`**:
Import data to a Memorystore Redis instance from Google Cloud Storage.

**`[list](https://cloud.google.com/sdk/gcloud/reference/redis/instances/list)`**:
List Memorystore Redis instances.

**`[reschedule-maintenance](https://cloud.google.com/sdk/gcloud/reference/redis/instances/reschedule-maintenance)`**:
Reschedule maintenance window for a Redis instance.

**`[update](https://cloud.google.com/sdk/gcloud/reference/redis/instances/update)`**:
Update Memorystore Redis instances.

**`[upgrade](https://cloud.google.com/sdk/gcloud/reference/redis/instances/upgrade)`**:
Upgrade a Memorystore for Redis instance to a specified Redis version.

**NOTES**

: These variants are also available:

```
gcloud alpha redis instances
```

```
gcloud beta redis instances
```