# gcloud alpha compute commitments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update)*

**NAME**

: **gcloud alpha compute commitments update - update Compute Engine commitments**

**SYNOPSIS**

: **`gcloud alpha compute commitments update` `[COMMITMENT](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update#COMMITMENT)` [`[--auto-renew](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update#--auto-renew)`] [`[--custom-end-time](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update#--custom-end-time)`=`CUSTOM_END_TIME`] [`[--plan](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update#--plan)`=`PLAN`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/commitments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update Compute Engine commitments.

**EXAMPLES**

: To enable auto renewal on a commitment called
``commitment-1`` in the
``us-central1`` region, run:

```
gcloud alpha compute commitments update commitment-1 --auto-renew --region=us-central1
```

To disable auto renewal on a commitment called
``commitment-1`` in the
``us-central1`` region, run:

```
gcloud alpha compute commitments update commitment-1 --no-auto-renew --region=us-central1
```

To upgrade the term of a commitment called
``commitment-1`` from 12-month to 36-month, in
the ``us-central1`` region, run:

```
gcloud alpha compute commitments update commitment-1 --plan=36-month --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`COMMITMENT`**:
Name of the commitment to update.

**FLAGS**

: **--auto-renew**:
Enable auto renewal for the commitment.

**--custom-end-time**:
Specifies a custom future end date and extends the commitment's ongoing term.

**--plan**:
Duration of the commitment. `PLAN` must be (only one value
is supported): `36-month`.

**--region**:
Region of the commitment to update. If not specified, you might be prompted to
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
gcloud compute commitments update
```

```
gcloud beta compute commitments update
```