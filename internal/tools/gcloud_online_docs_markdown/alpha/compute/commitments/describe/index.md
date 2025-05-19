# gcloud alpha compute commitments describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/describe)*

**NAME**

: **gcloud alpha compute commitments describe - describe a Compute Engine commitment**

**SYNOPSIS**

: **`gcloud alpha compute commitments describe` `[COMMITMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/describe#COMMITMENT)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Compute Engine commitment.

**EXAMPLES**

: To describe the commitment called
``commitment-1`` in the
``us-central1`` region, run:

```
gcloud alpha compute commitments describe commitment-1 --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`COMMITMENT`**:
Name of the commitment to describe.

**FLAGS**

: **--region**:
Region of the commitment to describe. If not specified, you might be prompted to
select a region (interactive mode only).
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute commitments describe
```

```
gcloud beta compute commitments describe
```