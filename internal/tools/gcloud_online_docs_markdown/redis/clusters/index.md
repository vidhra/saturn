# gcloud redis clusters  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters](https://cloud.google.com/sdk/gcloud/reference/redis/clusters)*

**NAME**

: **gcloud redis clusters - manage Memorystore for Redis Cluster instances**

**SYNOPSIS**

: **`gcloud redis clusters` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/redis/clusters#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/redis/clusters#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Memorystore for Redis Cluster instances.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[backup-collections](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backup-collections)`**:
Manage backup collections of Memorystore for Redis Cluster instances.

**`[backups](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/backups)`**:
Manage backups of Memorystore for Redis Cluster instances.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-cluster-endpoints](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/add-cluster-endpoints)`**:
Add more cluster endpoints.

**`[create](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create)`**:
Create a new Memorystore for Redis Cluster instance.

**`[create-backup](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create-backup)`**:
Create a backup of a Redis cluster.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/delete)`**:
Delete a Memorystore for Redis Cluster instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/describe)`**:
Show metadata for a Memorystore for Redis Cluster instance.

**`[detach](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach)`**:
Detach a secondary cluster.

**`[detach-secondaries](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/detach-secondaries)`**:
Detach one or more secondary clusters from the primary cluster.

**`[get-cluster-certificate-authority](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/get-cluster-certificate-authority)`**:
Get the certificate authority information for a Memorystore for Redis Cluster
instance.

**`[list](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/list)`**:
List Memorystore for Redis Cluster instances.

**`[remove-cluster-endpoints](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/remove-cluster-endpoints)`**:
Remove existing Memorystore cluster endpoints.

**`[reschedule-maintenance](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/reschedule-maintenance)`**:
Reschedule maintenance window for a Memorystore for Redis Cluster instance.

**`[switchover](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/switchover)`**:
Switchover to a secondary cluster.

**`[update](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/update)`**:
Update Memorystore Cluster for Redis instance.

**NOTES**

: These variants are also available:

```
gcloud alpha redis clusters
```

```
gcloud beta redis clusters
```