# gcloud compute service-attachments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe)*

**NAME**

: **gcloud compute service-attachments describe - display details about a Google Compute Engine service attachment**

**SYNOPSIS**

: **`gcloud compute service-attachments describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display details about a Google Compute Engine service attachment.

**EXAMPLES**

: To describe a service attachment, run:

```
gcloud compute service-attachments describe SERVICE_ATTACHMENT_NAME --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the service attachment to describe.

**FLAGS**

: **--region**:
Region of the service attachment to describe. If not specified, you might be
prompted to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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
gcloud alpha compute service-attachments describe
```

```
gcloud beta compute service-attachments describe
```