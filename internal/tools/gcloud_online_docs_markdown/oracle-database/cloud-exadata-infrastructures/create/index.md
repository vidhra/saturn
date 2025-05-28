# gcloud oracle-database cloud-exadata-infrastructures create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create)*

**NAME**

: **gcloud oracle-database cloud-exadata-infrastructures create - create a new ExadataInfrastructure**

**SYNOPSIS**

: **`gcloud oracle-database cloud-exadata-infrastructures create` (`[CLOUD_EXADATA_INFRASTRUCTURE](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#CLOUD_EXADATA_INFRASTRUCTURE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--display-name)`=`DISPLAY_NAME`] [`[--gcp-oracle-zone](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--gcp-oracle-zone)`=`GCP_ORACLE_ZONE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--labels)`=[`LABELS`,…]] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--request-id)`=`REQUEST_ID`] [[`[--properties-shape](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--properties-shape)`=`PROPERTIES_SHAPE` : `[--properties-compute-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--properties-compute-count)`=`PROPERTIES_COMPUTE_COUNT` `[--properties-customer-contacts](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--properties-customer-contacts)`=[`email`=`EMAIL`] `[--properties-storage-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--properties-storage-count)`=`PROPERTIES_STORAGE_COUNT` `[--properties-total-storage-size-gb](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--properties-total-storage-size-gb)`=`PROPERTIES_TOTAL_STORAGE_SIZE_GB` `[--maintenance-window-custom-action-timeout-mins](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-custom-action-timeout-mins)`=`MAINTENANCE_WINDOW_CUSTOM_ACTION_TIMEOUT_MINS` `[--maintenance-window-days-of-week](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-days-of-week)`=[`MAINTENANCE_WINDOW_DAYS_OF_WEEK`,…] `[--maintenance-window-hours-of-day](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-hours-of-day)`=[`MAINTENANCE_WINDOW_HOURS_OF_DAY`,…] `[--maintenance-window-is-custom-action-timeout-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-is-custom-action-timeout-enabled)` `[--maintenance-window-lead-time-week](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-lead-time-week)`=`MAINTENANCE_WINDOW_LEAD_TIME_WEEK` `[--maintenance-window-months](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-months)`=[`MAINTENANCE_WINDOW_MONTHS`,…] `[--maintenance-window-patching-mode](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-patching-mode)`=`MAINTENANCE_WINDOW_PATCHING_MODE` `[--maintenance-window-preference](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-preference)`=`MAINTENANCE_WINDOW_PREFERENCE` `[--maintenance-window-weeks-of-month](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#--maintenance-window-weeks-of-month)`=[`MAINTENANCE_WINDOW_WEEKS_OF_MONTH`,…]]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new ExadataInfrastructure.

**EXAMPLES**

: Choose an available system shapes in your location by running `gcloud
oracle-database db-system-shapes list --location=us-east4`. To create
Exadata Infrastructure instance with id `my-instance` in the location
`us-east4` with display-name `my instance`, compute count
`2` and choosen shape "Exadata.FOO", run:

```
gcloud oracle-database cloud-exadata-infrastructures create my-instance --location=us-east4 --display-name="my instance" --properties-shape=Exadata.FOO --properties-compute-count=2 --properties-storage-count=3
```

**POSITIONAL ARGUMENTS**

: **CloudExadataInfrastructure resource - Identifier. The name of the Exadata
Infrastructure resource with the format:
projects/{project}/locations/{region}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `cloud_exadata_infrastructure` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLOUD_EXADATA_INFRASTRUCTURE`**:
ID of the cloudExadataInfrastructure or fully qualified identifier for the
cloudExadataInfrastructure.
To set the `cloud_exadata_infrastructure` attribute:

- provide the argument `cloud_exadata_infrastructure` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the cloudExadataInfrastructure resource.
To set the `location` attribute:

- provide the argument `cloud_exadata_infrastructure` on the command
line with a fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
User friendly name for this resource.

**--gcp-oracle-zone**:
Google Cloud Platform location where Oracle Exadata is hosted.

**--labels**:
Labels or tags associated with the resource.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--request-id**:
An optional ID to identify the request. This value is used to identify duplicate
requests. If you make a request with the same request ID and the original
request is still in progress or completed, the server ignores the second
request. This prevents clients from accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--properties-shape**

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

: This command uses the `oracledatabase/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/oracle/database/docs](https://cloud.google.com/oracle/database/docs)