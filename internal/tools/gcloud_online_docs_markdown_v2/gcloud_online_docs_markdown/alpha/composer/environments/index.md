# gcloud alpha composer environments  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments)*

**NAME**

: **gcloud alpha composer environments - create and manage Cloud Composer environments**

**SYNOPSIS**

: **`gcloud alpha composer environments` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` The gcloud alpha composer environments command group lets
you create Cloud Composer environments containing an Apache Airflow setup.
Additionally, the command group supports environment updates including varying
number of machines used to run Airflow, setting Airflow configs, or installing
Python dependencies used in Airflow DAGs. The command group can also be used to
delete Composer environments.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[snapshots](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots)`**:
`(ALPHA)` Save and load snapshots of environment.

**`[storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/storage)`**:
`(ALPHA)` Manage Cloud Storage objects stored as part of Cloud
Composer environments.

**`[user-workloads-config-maps](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/user-workloads-config-maps)`**:
`(ALPHA)` Create and manage user workloads ConfigMaps of environment.

**`[user-workloads-secrets](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/user-workloads-secrets)`**:
`(ALPHA)` Create and manage user workloads Secrets of environment.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[check-upgrade](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/check-upgrade)`**:
`(ALPHA)` Check that upgrading a Cloud Composer environment does not
result in PyPI module conflicts.

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create)`**:
`(ALPHA)` Create and initialize a Cloud Composer environment.

**`[database-failover](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/database-failover)`**:
`(ALPHA)` Run a database failover operation.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete)`**:
`(ALPHA)` Delete one or more Cloud Composer environments.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/describe)`**:
`(ALPHA)` Get details about a Cloud Composer environment.

**`[fetch-database-properties](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties)`**:
`(ALPHA)` Fetch database properties.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list)`**:
`(ALPHA)` List the Cloud Composer environments under a project and
location.

**`[list-packages](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list-packages)`**:
`(ALPHA)` List all PyPI modules installed in an Airflow worker.

**`[list-upgrades](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list-upgrades)`**:
`(ALPHA)` List the Cloud Composer image version upgrades for a
specific environment.

**`[list-workloads](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list-workloads)`**:
`(ALPHA)` List Composer workloads, supported in Composer 3
environments or greater.

**`[restart-web-server](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/restart-web-server)`**:
`(ALPHA)` Restart web server for a Cloud Composer environment.

**`[run](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/run)`**:
`(ALPHA)` Run an Airflow sub-command remotely in a Cloud Composer
environment.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update)`**:
`(ALPHA)` Update properties of a Cloud Composer environment.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud composer environments
```

```
gcloud beta composer environments
```