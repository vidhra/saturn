# gcloud oracle-database cloud-exadata-infrastructures describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/describe](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/describe)*

**NAME**

: **gcloud oracle-database cloud-exadata-infrastructures describe - get details of a ExadataInfrastructure**

**SYNOPSIS**

: **`gcloud oracle-database cloud-exadata-infrastructures describe` (`[CLOUD_EXADATA_INFRASTRUCTURE](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/describe#CLOUD_EXADATA_INFRASTRUCTURE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-exadata-infrastructures/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get details of a ExadataInfrastructure.

**EXAMPLES**

: To get a ExadataInfrastructure with id `my-instance` in the location
`us-east4`, run:

```
gcloud oracle-database cloud-exadata-infrastructures describe my-instance --location=us-east4
```

**POSITIONAL ARGUMENTS**

: **CloudExadataInfrastructure resource - The name of the Cloud Exadata
Infrastructure in the following format:
projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}.
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