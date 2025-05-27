# gcloud dataplex tasks update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update)*

**NAME**

: **gcloud dataplex tasks update - update a Dataplex task resource**

**SYNOPSIS**

: **`gcloud dataplex tasks update` (`[TASK](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#TASK)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--display-name)`=`DISPLAY_NAME`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--remove-labels)`=[`KEY`,…]] [`[--execution-args](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--execution-args)`=[`KEY`=`VALUE`,…] `[--execution-project](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--execution-project)`=`EXECUTION_PROJECT` `[--execution-service-account](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--execution-service-account)`=`EXECUTION_SERVICE_ACCOUNT` `[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--kms-key)`=`KMS_KEY` `[--max-job-execution-lifetime](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--max-job-execution-lifetime)`=`MAX_JOB_EXECUTION_LIFETIME`] [`[--notebook](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook)`=`NOTEBOOK` `[--notebook-archive-uris](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-archive-uris)`=[`NOTEBOOK_ARCHIVE_URIS`,…] `[--notebook-file-uris](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-file-uris)`=[`NOTEBOOK_FILE_URIS`,…] `[--notebook-batch-executors-count](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-batch-executors-count)`=`NOTEBOOK_BATCH_EXECUTORS_COUNT` `[--notebook-batch-max-executors-count](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-batch-max-executors-count)`=`NOTEBOOK_BATCH_MAX_EXECUTORS_COUNT` `[--notebook-container-image](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-container-image)`=`NOTEBOOK_CONTAINER_IMAGE` `[--notebook-container-image-java-jars](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-container-image-java-jars)`=[`NOTEBOOK_CONTAINER_IMAGE_JAVA_JARS`,…] `[--notebook-container-image-properties](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-container-image-properties)`=[`KEY`=`VALUE`,…] `[--notebook-vpc-network-tags](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-vpc-network-tags)`=[`NOTEBOOK_VPC_NETWORK_TAGS`,…] `[--notebook-vpc-network-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-vpc-network-name)`=`NOTEBOOK_VPC_NETWORK_NAME`     | `[--notebook-vpc-sub-network-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--notebook-vpc-sub-network-name)`=`NOTEBOOK_VPC_SUB_NETWORK_NAME`     | `[--spark-archive-uris](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-archive-uris)`=[`SPARK_ARCHIVE_URIS`,…] `[--spark-file-uris](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-file-uris)`=[`SPARK_FILE_URIS`,…] `[--batch-executors-count](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--batch-executors-count)`=`BATCH_EXECUTORS_COUNT` `[--batch-max-executors-count](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--batch-max-executors-count)`=`BATCH_MAX_EXECUTORS_COUNT` `[--container-image](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--container-image)`=`CONTAINER_IMAGE` `[--container-image-java-jars](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--container-image-java-jars)`=[`CONTAINER_IMAGE_JAVA_JARS`,…] `[--container-image-properties](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--container-image-properties)`=[`KEY`=`VALUE`,…] `[--container-image-python-packages](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--container-image-python-packages)`=[`CONTAINER_IMAGE_PYTHON_PACKAGES`,…] `[--vpc-network-tags](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--vpc-network-tags)`=[`VPC_NETWORK_TAGS`,…] `[--vpc-network-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--vpc-network-name)`=`VPC_NETWORK_NAME` `[--vpc-sub-network-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--vpc-sub-network-name)`=`VPC_SUB_NETWORK_NAME` `[--spark-main-class](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-main-class)`=`SPARK_MAIN_CLASS`     | `[--spark-main-jar-file-uri](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-main-jar-file-uri)`=`SPARK_MAIN_JAR_FILE_URI`     | `[--spark-python-script-file](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-python-script-file)`=`SPARK_PYTHON_SCRIPT_FILE`     | `[--spark-sql-script](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-sql-script)`=`SPARK_SQL_SCRIPT`     | `[--spark-sql-script-file](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--spark-sql-script-file)`=`SPARK_SQL_SCRIPT_FILE`] [`[--trigger-disabled](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--trigger-disabled)` `[--trigger-max-retires](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--trigger-max-retires)`=`TRIGGER_MAX_RETIRES` `[--trigger-schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--trigger-schedule)`=`TRIGGER_SCHEDULE` `[--trigger-start-time](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#--trigger-start-time)`=`TRIGGER_START_TIME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/tasks/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex task resource with the given configurations.

**EXAMPLES**

: To update a Dataplex task `test-task` within lake
`test-lake` in location `us-central1` and change the
description to `Updated Description`, run:

```
gcloud dataplex tasks update projects/test-project/locations/us-central1/lakes/test-lake/tasks/test-task --description='Updated Description'
```

**POSITIONAL ARGUMENTS**

: **Task resource - Arguments and flags that specify the Dataplex Task you want to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TASK`**:
ID of the task or fully qualified identifier for the task.
To set the `task` attribute:

- provide the argument `task` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
Identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `task` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the task.

**--display-name**:
Display name of the task.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

**--execution-args**

**--notebook**

**--trigger-disabled**

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

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex tasks update
```