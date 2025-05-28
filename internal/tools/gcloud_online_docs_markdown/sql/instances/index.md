# gcloud sql instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances](https://cloud.google.com/sdk/gcloud/reference/sql/instances)*

**NAME**

: **gcloud sql instances - provide commands for managing Cloud SQL instances**

**SYNOPSIS**

: **`gcloud sql instances` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/sql/instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Provide commands for managing Cloud SQL instances including creating,
configuring, restarting, and deleting instances.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[acquire-ssrs-lease](https://cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease)`**:
Acquires a SQL Server Reporting Services lease on a Cloud SQL instance.

**`[clone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone)`**:
Clones a Cloud SQL instance.

**`[create](https://cloud.google.com/sdk/gcloud/reference/sql/instances/create)`**:
Creates a new Cloud SQL instance.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/sql/instances/delete)`**:
Deletes a Cloud SQL instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/sql/instances/describe)`**:
Displays configuration and metadata about a Cloud SQL instance.

**`[export](https://cloud.google.com/sdk/gcloud/reference/sql/instances/export)`**:
`(DEPRECATED)` Exports data from a Cloud SQL instance.

**`[failover](https://cloud.google.com/sdk/gcloud/reference/sql/instances/failover)`**:
Causes a high-availability Cloud SQL instance to failover.

**`[get-latest-recovery-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time)`**:
Displays the latest recovery time to which a Cloud SQL instance can be restored
to.

**`[import](https://cloud.google.com/sdk/gcloud/reference/sql/instances/import)`**:
`(DEPRECATED)` Imports data into a Cloud SQL instance from Google
Cloud Storage.

**`[list](https://cloud.google.com/sdk/gcloud/reference/sql/instances/list)`**:
Lists Cloud SQL instances in a given project.

**`[patch](https://cloud.google.com/sdk/gcloud/reference/sql/instances/patch)`**:
Updates the settings of a Cloud SQL instance.

**`[promote-replica](https://cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica)`**:
Promotes Cloud SQL read replica to a stand-alone instance.

**`[reencrypt](https://cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt)`**:
Reencrypts a Cloud SQL CMEK instance.

**`[release-ssrs-lease](https://cloud.google.com/sdk/gcloud/reference/sql/instances/release-ssrs-lease)`**:
Releases a SQL Server Reporting Services lease on a Cloud SQL instance.

**`[reset-ssl-config](https://cloud.google.com/sdk/gcloud/reference/sql/instances/reset-ssl-config)`**:
Deletes all client certificates and generates a new server certificate.

**`[restart](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restart)`**:
Restarts a Cloud SQL instance.

**`[restore-backup](https://cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup)`**:
Restores a backup of a Cloud SQL instance.

**`[switchover](https://cloud.google.com/sdk/gcloud/reference/sql/instances/switchover)`**:
Switches over a Cloud SQL instance to one of its replicas.

**NOTES**

: These variants are also available:

```
gcloud alpha sql instances
```

```
gcloud beta sql instances
```