# gcloud composer environments storage dags delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/delete](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/delete)*

**NAME**

: **gcloud composer environments storage dags delete - delete DAG files from an Cloud Composer environment's Cloud Storage bucket**

**SYNOPSIS**

: **`gcloud composer environments storage dags delete` [`[TARGET](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/delete#TARGET)`] (`[--environment](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/delete#--environment)`=`ENVIRONMENT` : `[--location](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/delete#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/composer/environments/storage/dags/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete DAG files from an Cloud Composer environment's Cloud Storage bucket.

**EXAMPLES**

: To delete the dags in the path
``path/to/dags``, for the environment named
``environment-1`` in the location
``us-east1``, run:

```
gcloud composer environments storage dags delete path/to/dags --environment=environment-1 --location=us-east1
```

**POSITIONAL ARGUMENTS**

: **[`TARGET`]**:
A relative path to a file or subdirectory to delete within the dags Cloud
Storage subdirectory. If not specified, the entire contents of the dags
subdirectory will be deleted.

**REQUIRED FLAGS**

: **Environment resource - The environment whose DAGs to delete. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--environment` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--environment**:
ID of the environment or fully qualified identifier for the environment.
To set the `environment` attribute:

- provide the argument `--environment` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Region where Composer environment runs or in which to create the environment.
To set the `location` attribute:

- provide the argument `--environment` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `composer/location`.**

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

: These variants are also available:

```
gcloud alpha composer environments storage dags delete
```

```
gcloud beta composer environments storage dags delete
```