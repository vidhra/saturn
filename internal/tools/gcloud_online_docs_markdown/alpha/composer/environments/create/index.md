# gcloud alpha composer environments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create)*

**NAME**

: **gcloud alpha composer environments create - create and initialize a Cloud Composer environment**

**SYNOPSIS**

: **`gcloud alpha composer environments create` (`[ENVIRONMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#ENVIRONMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--location)`=`LOCATION`) [`[--airflow-configs](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--airflow-configs)`=[`KEY`=`VALUE`,…]] [`[--airflow-database-retention-days](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--airflow-database-retention-days)`=`AIRFLOW_DATABASE_RETENTION_DAYS`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--async)`] [`[--cloud-sql-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--cloud-sql-machine-type)`=`CLOUD_SQL_MACHINE_TYPE`] [`[--cloud-sql-preferred-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--cloud-sql-preferred-zone)`=`CLOUD_SQL_PREFERRED_ZONE`] [`[--composer-internal-ipv4-cidr-block](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--composer-internal-ipv4-cidr-block)`=`COMPOSER_INTERNAL_IPV4_CIDR_BLOCK`] [`[--disable-logs-in-cloud-logging-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--disable-logs-in-cloud-logging-only)`] [`[--disk-size](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--disk-size)`=`DISK_SIZE`] [`[--enable-high-resilience](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-high-resilience)`] [`[--enable-logs-in-cloud-logging-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-logs-in-cloud-logging-only)`] [`[--env-variables](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--env-variables)`=[`NAME`=`VALUE`,…]] [`[--environment-size](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--environment-size)`=`ENVIRONMENT_SIZE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--machine-type)`=`MACHINE_TYPE`] [`[--network-attachment](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--network-attachment)`=`NETWORK_ATTACHMENT`] [`[--node-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--node-count)`=`NODE_COUNT`] [`[--oauth-scopes](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--oauth-scopes)`=[`SCOPE`,…]] [`[--python-version](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--python-version)`=`PYTHON_VERSION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--storage-bucket](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--storage-bucket)`=`STORAGE_BUCKET`] [`[--support-web-server-plugins](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--support-web-server-plugins)`] [`[--tags](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--tags)`=[`TAG`,…]] [`[--web-server-machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-machine-type)`=`WEB_SERVER_MACHINE_TYPE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--zone)`=`ZONE`] [`[--airflow-version](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--airflow-version)`=`AIRFLOW_VERSION`     | `[--image-version](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--image-version)`=`IMAGE_VERSION`] [`[--cloud-sql-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--cloud-sql-ipv4-cidr)`=`CLOUD_SQL_IPV4_CIDR` `[--composer-network-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--composer-network-ipv4-cidr)`=`COMPOSER_NETWORK_IPV4_CIDR` `[--connection-subnetwork](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--connection-subnetwork)`=`CONNECTION_SUBNETWORK` `[--connection-type](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--connection-type)`=`CONNECTION_TYPE` `[--enable-private-endpoint](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-private-endpoint)` `[--enable-private-environment](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-private-environment)` `[--enable-privately-used-public-ips](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-privately-used-public-ips)` `[--master-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--master-ipv4-cidr)`=`MASTER_IPV4_CIDR` `[--web-server-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-ipv4-cidr)`=`WEB_SERVER_IPV4_CIDR`] [`[--cluster-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--cluster-ipv4-cidr)`=`CLUSTER_IPV4_CIDR` `[--cluster-secondary-range-name](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--cluster-secondary-range-name)`=`CLUSTER_SECONDARY_RANGE_NAME` `[--enable-ip-alias](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-ip-alias)` `[--enable-ip-masq-agent](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-ip-masq-agent)` `[--max-pods-per-node](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--max-pods-per-node)`=`MAX_PODS_PER_NODE` `[--services-ipv4-cidr](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--services-ipv4-cidr)`=`SERVICES_IPV4_CIDR` `[--services-secondary-range-name](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--services-secondary-range-name)`=`SERVICES_SECONDARY_RANGE_NAME`] [`[--dag-processor-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--dag-processor-count)`=`DAG_PROCESSOR_COUNT` `[--dag-processor-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--dag-processor-cpu)`=`DAG_PROCESSOR_CPU` `[--dag-processor-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--dag-processor-memory)`=`DAG_PROCESSOR_MEMORY` `[--dag-processor-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--dag-processor-storage)`=`DAG_PROCESSOR_STORAGE`] [`[--disable-cloud-data-lineage-integration](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--disable-cloud-data-lineage-integration)`     | `[--enable-cloud-data-lineage-integration](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-cloud-data-lineage-integration)`] [`[--disable-private-builds-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--disable-private-builds-only)`     | `[--enable-private-builds-only](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-private-builds-only)`] [`[--enable-master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-master-authorized-networks)` `[--master-authorized-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--master-authorized-networks)`=[`NETWORK`,…]] [`[--enable-scheduled-snapshot-creation](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-scheduled-snapshot-creation)` `[--snapshot-creation-schedule](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--snapshot-creation-schedule)`=`SNAPSHOT_CREATION_SCHEDULE` `[--snapshot-location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--snapshot-location)`=`SNAPSHOT_LOCATION` `[--snapshot-schedule-timezone](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--snapshot-schedule-timezone)`=`SNAPSHOT_SCHEDULE_TIMEZONE`] [`[--enable-triggerer](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--enable-triggerer)` `[--triggerer-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--triggerer-count)`=`TRIGGERER_COUNT` `[--triggerer-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--triggerer-cpu)`=`TRIGGERER_CPU` `[--triggerer-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--triggerer-memory)`=`TRIGGERER_MEMORY`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--kms-project)`=`KMS_PROJECT`] [`[--maintenance-window-end](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--maintenance-window-end)`=`MAINTENANCE_WINDOW_END` `[--maintenance-window-recurrence](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--maintenance-window-recurrence)`=`MAINTENANCE_WINDOW_RECURRENCE` `[--maintenance-window-start](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--maintenance-window-start)`=`MAINTENANCE_WINDOW_START`] [`[--max-workers](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--max-workers)`=`MAX_WORKERS` `[--min-workers](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--min-workers)`=`MIN_WORKERS` `[--scheduler-count](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--scheduler-count)`=`SCHEDULER_COUNT` `[--scheduler-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--scheduler-cpu)`=`SCHEDULER_CPU` `[--scheduler-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--scheduler-memory)`=`SCHEDULER_MEMORY` `[--scheduler-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--scheduler-storage)`=`SCHEDULER_STORAGE` `[--web-server-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-cpu)`=`WEB_SERVER_CPU` `[--web-server-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-memory)`=`WEB_SERVER_MEMORY` `[--web-server-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-storage)`=`WEB_SERVER_STORAGE` `[--worker-cpu](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--worker-cpu)`=`WORKER_CPU` `[--worker-memory](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--worker-memory)`=`WORKER_MEMORY` `[--worker-storage](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--worker-storage)`=`WORKER_STORAGE`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--network)`=`NETWORK` : `[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--subnetwork)`=`SUBNETWORK`] [`[--web-server-allow-all](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-allow-all)`     | `[--web-server-allow-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-allow-ip)`=[`description`=`DESCRIPTION`],[`ip_range`=`IP_RANGE`]     | `[--web-server-deny-all](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#--web-server-deny-all)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` If run asynchronously with `--async`, exits
after printing an operation that can be used to poll the status of the creation
operation via:

```
gcloud composer operations describe
```

**EXAMPLES**

: To create an environment called ``env-1`` with
all the default values, run:

```
gcloud alpha composer environments create env-1
```

To create a new environment named ``env-1``
with the Google Compute Engine machine-type
``n1-standard-8``, and the Google Compute
Engine network ``my-network``, run:

```
gcloud alpha composer environments create env-1 --machine-type=n1-standard-8 --network=my-network
```

**POSITIONAL ARGUMENTS**

: **Environment resource - The environment to create. The arguments in this group
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

**FLAGS**

: **--airflow-configs**:
A list of Airflow software configuration override KEY=VALUE pairs to set. For
information on how to structure KEYs and VALUEs, run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference) composer environments
update`.

**--airflow-database-retention-days**:
The number of days for the Airflow database retention period. If set to 0, the
Airflow database retention mechanism will be disabled.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--cloud-sql-machine-type**:
Cloud SQL machine type used by the Airflow database. The list of available
machine types is available here: [https://cloud.google.com/composer/pricing#db-machine-types](https://cloud.google.com/composer/pricing#db-machine-types).

**--cloud-sql-preferred-zone**:
Select cloud sql preferred zone, supported for Composer 2 Environments.

**--composer-internal-ipv4-cidr-block**:
The IP range in CIDR notation to use internally by Cloud Composer. This should
have a netmask length of 20. Can be specified for Composer 3 or greater.

**--disable-logs-in-cloud-logging-only**:
Disable logs in cloud logging only, supported for Composer 2 Environments.

**--disk-size**:
The disk size for each VM node in the environment. The minimum size is 20GB, and
the maximum is 64TB. Specified value must be an integer multiple of gigabytes.
Cannot be updated after the environment has been created. If units are not
provided, defaults to GB.

**--enable-high-resilience**:
Enable high resilience, supported for Composer 2 Environments.

**--enable-logs-in-cloud-logging-only**:
Enable logs in cloud logging only, supported for Composer 2 Environments.

**--env-variables**:
A comma-delimited list of environment variable `NAME=VALUE` pairs to
provide to the Airflow scheduler, worker, and webserver processes. NAME may
contain upper and lowercase letters, digits, and underscores, but they may not
begin with a digit. To include commas as part of a `VALUE`, see
`[gcloud topic
escaping](https://cloud.google.com/sdk/gcloud/reference/topic/escaping)` for information about overriding the delimiter.

**--environment-size**:
Size of the environment. Unspecified means that the default option will be
chosen. `ENVIRONMENT_SIZE` must be one of:
`large`, `medium`, `small`,
`unspecified`.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--machine-type**:
The Compute Engine machine type
(https://cloud.google.com/compute/docs/machine-types) to use for nodes. For
example `--machine-type=n1-standard-1`.

**--network-attachment**:
Cloud Composer Network Attachment, which provides connectivity with a user's VPC
network, supported in Composer 3 environments or greater.

**--node-count**:
The number of nodes to create to run the environment.

**--oauth-scopes**:
The set of Google API scopes to be made available on all of the node VMs.
Defaults to ['https://www.googleapis.com/auth/cloud-platform']. Cannot be
updated.

**--python-version**:
The Python version to be used within the created environment. Supplied value
should represent the desired major Python version. Cannot be updated.
`PYTHON_VERSION` must be one of:

**`2`**:
Created environment will use Python 2

**`3`**:
Created environment will use Python 3

**--service-account**:
The Google Cloud Platform service account to be used by the node VMs. If a
service account is not specified, the "default" Compute Engine service account
for the project is used. Cannot be updated.

**--storage-bucket**:
Name of an exisiting Cloud Storage bucket to be used by the environment.
Supported only for Composer 2.4.X and above.

**--support-web-server-plugins**:
Enable the support for web server plugins, supported in Composer 3 or greater.

**--tags**:
The set of instance tags applied to all node VMs. Tags are used to identify
valid sources or targets for network firewalls. Each tag within the list must
comply with RFC 1035. Cannot be updated.

**--web-server-machine-type**:
machine type used by the Airflow web server. The list of available machine types
is available here: [https://cloud.google.com/composer/pricing](https://cloud.google.com/composer/pricing).

**--zone**:
The Compute Engine zone in which the environment will be created. For example
`--zone=us-central1-a`.

**--airflow-version**

**--cloud-sql-ipv4-cidr**

**--cluster-ipv4-cidr**

**--dag-processor-count**

**--disable-cloud-data-lineage-integration**

**--disable-private-builds-only**

**--enable-master-authorized-networks**

**--enable-scheduled-snapshot-creation**

**--enable-triggerer**

**--kms-key**

**--maintenance-window-end**

**--max-workers**

**--network**

**--web-server-allow-all**

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
gcloud composer environments create
```

```
gcloud beta composer environments create
```