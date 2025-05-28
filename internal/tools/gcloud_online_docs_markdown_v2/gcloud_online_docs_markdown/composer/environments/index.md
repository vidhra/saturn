# gcloud composer environments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/composer/environments](https://cloud.google.com/sdk/gcloud/reference/composer/environments)*

**NAME**

: **gcloud composer environments - create and manage Cloud Composer environments**

**SYNOPSIS**

: **`gcloud composer environments` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/composer/environments#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/composer/environments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/composer/environments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud composer environments command group lets you create Cloud Composer
environments containing an Apache Airflow setup. Additionally, the command group
supports environment updates including varying number of machines used to run
Airflow, setting Airflow configs, or installing Python dependencies used in
Airflow DAGs. The command group can also be used to delete Composer
environments.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[snapshots](https://cloud.google.com/sdk/gcloud/reference/composer/environments/snapshots)`**:
Save and load snapshots of environment.

**`[storage](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage)`**:
Manage Cloud Storage objects stored as part of Cloud Composer environments.

**`[user-workloads-config-maps](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps)`**:
Create and manage user workloads ConfigMaps of environment.

**`[user-workloads-secrets](https://cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-secrets)`**:
Create and manage user workloads Secrets of environment.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[check-upgrade](https://cloud.google.com/sdk/gcloud/reference/composer/environments/check-upgrade)`**:
Check that upgrading a Cloud Composer environment does not result in PyPI module
conflicts.

**`[create](https://cloud.google.com/sdk/gcloud/reference/composer/environments/create)`**:
Create and initialize a Cloud Composer environment.

**`[database-failover](https://cloud.google.com/sdk/gcloud/reference/composer/environments/database-failover)`**:
Run a database failover operation.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/composer/environments/delete)`**:
Delete one or more Cloud Composer environments.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/composer/environments/describe)`**:
Get details about a Cloud Composer environment.

**`[fetch-database-properties](https://cloud.google.com/sdk/gcloud/reference/composer/environments/fetch-database-properties)`**:
Fetch database properties.

**`[list](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list)`**:
List the Cloud Composer environments under a project and location.

**`[list-packages](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages)`**:
List all PyPI modules installed in an Airflow worker.

**`[list-upgrades](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-upgrades)`**:
List the Cloud Composer image version upgrades for a specific environment.

**`[list-workloads](https://cloud.google.com/sdk/gcloud/reference/composer/environments/list-workloads)`**:
List Composer workloads, supported in Composer 3 environments or greater.

**`[run](https://cloud.google.com/sdk/gcloud/reference/composer/environments/run)`**:
Run an Airflow sub-command remotely in a Cloud Composer environment.

**`[update](https://cloud.google.com/sdk/gcloud/reference/composer/environments/update)`**:
Update properties of a Cloud Composer environment.

**NOTES**

: These variants are also available:

```
gcloud alpha composer environments
```

```
gcloud beta composer environments
```