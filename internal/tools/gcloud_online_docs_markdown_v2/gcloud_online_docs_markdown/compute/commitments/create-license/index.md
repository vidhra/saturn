# gcloud compute commitments create-license  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license)*

**NAME**

: **gcloud compute commitments create-license - create Compute Engine license-based commitments**

**SYNOPSIS**

: **`gcloud compute commitments create-license` `[COMMITMENT](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#COMMITMENT)` `[--amount](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#--amount)`=`AMOUNT` `[--license](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#--license)`=`LICENSE` `[--plan](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#--plan)`=`PLAN` [`[--cores-per-license](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#--cores-per-license)`=`CORES_PER_LICENSE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/commitments/create-license#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create Compute Engine license-based commitments.

**EXAMPLES**

: To create a commitment called ``commitment-1``
in the ``us-central1`` region with 36-month
plan, sles-sap-12 license, 1-2 cores, run:

```
gcloud compute commitments create-license commitment-1 --plan=36-month --license=https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12 --region=us-central1 --amount=1 --cores-per-license=1-2
```

**POSITIONAL ARGUMENTS**

: **`COMMITMENT`**:
Name of the commitment to create.

**REQUIRED FLAGS**

: **--amount**:
Number of licenses purchased.

**--license**:
Applicable license URI. For example:
`https://www.googleapis.com/compute/v1/projects/suse-sap-cloud/global/licenses/sles-sap-12`

**--plan**:
Duration of the commitment. `PLAN` must be one of:
`12-month`, `36-month`.

**OPTIONAL FLAGS**

: **--cores-per-license**:
Core range of the instance. Must be one of: `1-2`, `3-4`,
`5+`. Required for SAP licenses.

**--region**:
Region of the commitment to create. If not specified, you might be prompted to
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

: These variants are also available:

```
gcloud alpha compute commitments create-license
```

```
gcloud beta compute commitments create-license
```