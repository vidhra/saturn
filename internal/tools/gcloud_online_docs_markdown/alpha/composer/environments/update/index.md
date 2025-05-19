# gcloud alpha composer environments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update)*

**NAME**

: **gcloud alpha composer environments update - update properties of a Cloud Composer environment**

**SYNOPSIS**

: **`gcloud alpha composer environments update` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#ENVIRONMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--location)`=`LOCATION`) (`[--airflow-database-retention-days](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--airflow-database-retention-days)`=`AIRFLOW_DATABASE_RETENTION_DAYS`     | `[--cloud-sql-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--cloud-sql-machine-type)`=`CLOUD_SQL_MACHINE_TYPE`     | `[--disable-high-resilience](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-high-resilience)`     | `[--disable-logs-in-cloud-logging-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-logs-in-cloud-logging-only)`     | `[--disable-private-environment](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-private-environment)`     | `[--enable-high-resilience](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-high-resilience)`     | `[--enable-logs-in-cloud-logging-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-logs-in-cloud-logging-only)`     | `[--enable-private-environment](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-private-environment)`     | `[--environment-size](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--environment-size)`=`ENVIRONMENT_SIZE`     | `[--node-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--node-count)`=`NODE_COUNT`     | `[--support-web-server-plugins](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--support-web-server-plugins)`     | `[--web-server-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--web-server-machine-type)`=`WEB_SERVER_MACHINE_TYPE`     | `[--airflow-version](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--airflow-version)`=`AIRFLOW_VERSION`     | `[--image-version](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--image-version)`=`IMAGE_VERSION`     | `[--clear-maintenance-window](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--clear-maintenance-window)`     | `[--maintenance-window-end](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--maintenance-window-end)`=`MAINTENANCE_WINDOW_END` `[--maintenance-window-recurrence](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--maintenance-window-recurrence)`=`MAINTENANCE_WINDOW_RECURRENCE` `[--maintenance-window-start](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--maintenance-window-start)`=`MAINTENANCE_WINDOW_START`     | `[--disable-cloud-data-lineage-integration](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-cloud-data-lineage-integration)`     | `[--enable-cloud-data-lineage-integration](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-cloud-data-lineage-integration)`     | `[--disable-master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-master-authorized-networks)` `[--enable-master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-master-authorized-networks)` `[--master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--master-authorized-networks)`=[`NETWORK`,…]     | `[--disable-private-builds-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-private-builds-only)`     | `[--enable-private-builds-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-private-builds-only)`     | `[--disable-scheduled-snapshot-creation](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-scheduled-snapshot-creation)`     | `[--enable-scheduled-snapshot-creation](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-scheduled-snapshot-creation)` `[--snapshot-creation-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--snapshot-creation-schedule)`=`SNAPSHOT_CREATION_SCHEDULE` `[--snapshot-location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--snapshot-location)`=`SNAPSHOT_LOCATION` `[--snapshot-schedule-timezone](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--snapshot-schedule-timezone)`=`SNAPSHOT_SCHEDULE_TIMEZONE`     | `[--disable-vpc-connectivity](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-vpc-connectivity)`     | `[--network-attachment](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--network-attachment)`=`NETWORK_ATTACHMENT`     | [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--network)`=`NETWORK` : `[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--subnetwork)`=`SUBNETWORK`]     | `[--max-workers](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--max-workers)`=`MAX_WORKERS` `[--min-workers](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--min-workers)`=`MIN_WORKERS` `[--scheduler-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--scheduler-count)`=`SCHEDULER_COUNT` `[--scheduler-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--scheduler-cpu)`=`SCHEDULER_CPU` `[--scheduler-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--scheduler-memory)`=`SCHEDULER_MEMORY` `[--scheduler-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--scheduler-storage)`=`SCHEDULER_STORAGE` `[--web-server-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--web-server-cpu)`=`WEB_SERVER_CPU` `[--web-server-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--web-server-memory)`=`WEB_SERVER_MEMORY` `[--web-server-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--web-server-storage)`=`WEB_SERVER_STORAGE` `[--worker-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--worker-cpu)`=`WORKER_CPU` `[--worker-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--worker-memory)`=`WORKER_MEMORY` `[--worker-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--worker-storage)`=`WORKER_STORAGE` `[--dag-processor-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--dag-processor-count)`=`DAG_PROCESSOR_COUNT` `[--dag-processor-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--dag-processor-cpu)`=`DAG_PROCESSOR_CPU` `[--dag-processor-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--dag-processor-memory)`=`DAG_PROCESSOR_MEMORY` `[--dag-processor-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--dag-processor-storage)`=`DAG_PROCESSOR_STORAGE` `[--disable-triggerer](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--disable-triggerer)`     | `[--enable-triggerer](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--enable-triggerer)` `[--triggerer-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--triggerer-count)`=`TRIGGERER_COUNT` `[--triggerer-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--triggerer-cpu)`=`TRIGGERER_CPU` `[--triggerer-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--triggerer-memory)`=`TRIGGERER_MEMORY`     | `[--update-airflow-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--update-airflow-configs)`=[`KEY`=`VALUE`,…] `[--clear-airflow-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--clear-airflow-configs)`     | `[--remove-airflow-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--remove-airflow-configs)`=[`KEY`,…]     | `[--update-env-variables](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--update-env-variables)`=[`NAME`=`VALUE`,…] `[--clear-env-variables](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--clear-env-variables)`     | `[--remove-env-variables](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--remove-env-variables)`=[`NAME`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--update-labels)`=[`KEY`=`VALUE`,…] `[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--remove-labels)`=[`KEY`,…]     | `[--update-pypi-packages-from-file](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--update-pypi-packages-from-file)`=`UPDATE_PYPI_PACKAGES_FROM_FILE`     | `[--update-pypi-package](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--update-pypi-package)`=`PACKAGE`[`[EXTRAS_LIST](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#EXTRAS_LIST)`]`[VERSION_SPECIFIER](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#VERSION_SPECIFIER)` `[--clear-pypi-packages](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--clear-pypi-packages)`     | `[--remove-pypi-packages](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--remove-pypi-packages)`=[`PACKAGE`,…]     | `[--update-web-server-allow-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--update-web-server-allow-ip)`=[`description`=`DESCRIPTION`],[`ip_range`=`IP_RANGE`]     | `[--web-server-allow-all](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--web-server-allow-all)`     | `[--web-server-deny-all](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--web-server-deny-all)`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update properties of a Cloud Composer environment.

**EXAMPLES**

: To update the Cloud Composer environment named
``env-1`` to have 8 Airflow workers, and not
have the ``production`` label, run:

```
gcloud alpha composer environments update env-1 --node-count=8 --remove-labels=production
```

**POSITIONAL ARGUMENTS**

: **Environment resource - The environment to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENVIRONMENT`**:
ID of the environment or fully qualified identifier for the environment.
To set the `environment` attribute:

- provide the argument `environment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

**REQUIRED FLAGS**

: **--airflow-database-retention-days**

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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud composer environments update
```

```
gcloud beta composer environments update
```