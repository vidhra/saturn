# gcloud builds connections delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/connections/delete](https://cloud.google.com/sdk/gcloud/reference/builds/connections/delete)*

**NAME**

: **gcloud builds connections delete - delete a Cloud Build Connection**

**SYNOPSIS**

: **`gcloud builds connections delete` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/builds/connections/delete#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/connections/delete#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/builds/connections/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/connections/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud Build Connection.

**EXAMPLES**

: To delete Cloud Build connection ``my-conn`` in
region ``us-central1``, run the following
command:

```
gcloud builds connections delete my-conn --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Connection resource - Cloud Build connection to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTION`**:
ID of the connection or fully qualified identifier for the connection.
To set the `connection` attribute:

- provide the argument `connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Google Cloud region.
To set the `region` attribute:

- provide the argument `connection` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

**FLAGS**

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

**API REFERENCE**

: This command uses the `cloudbuild/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/cloud-build/docs/](https://cloud.google.com/cloud-build/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha builds connections delete
```

```
gcloud beta builds connections delete
```