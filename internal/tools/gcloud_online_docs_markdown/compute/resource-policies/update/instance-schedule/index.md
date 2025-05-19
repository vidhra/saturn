# gcloud compute resource-policies update instance-schedule  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule)*

**NAME**

: **gcloud compute resource-policies update instance-schedule - update a Compute Engine Instance Schedule Resource Policy**

**SYNOPSIS**

: **`gcloud compute resource-policies update instance-schedule` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--description)`=`DESCRIPTION`] [`[--end-date](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--end-date)`=`END_DATE`] [`[--initiation-date](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--initiation-date)`=`INITIATION_DATE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--region)`=`REGION`] [`[--timezone](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--timezone)`=`TIMEZONE`] [`[--vm-start-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--vm-start-schedule)`=`VM_START_SCHEDULE`] [`[--vm-stop-schedule](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#--vm-stop-schedule)`=`VM_STOP_SCHEDULE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update/instance-schedule#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Compute Engine Instance Schedule Resource Policy.

**EXAMPLES**

: To update an instance schedule resource policy with specified parameters:

```
gcloud compute resource-policies update instance-schedule NAME --region=REGION --timezone=UTC --vm-start-schedule="0 7 * * *" --vm-stop-schedule="0 17 * * *"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the resource policy to operate on.

**FLAGS**

: **--description**:
An optional, textual description for the backend.

**--end-date**:
The expiration time of the schedule policy. The timestamp must be an RFC3339
valid string.

**--initiation-date**:
The start time of the schedule policy. The timestamp must be an RFC3339 valid
string.

**--region**:
Region of the resource policy to operate on. If not specified, you might be
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

**--timezone**:
Timezone used in interpreting schedule. The value of this field must be a time
zone name from the tz database [http://en.wikipedia.org/wiki/Tz_database](http://en.wikipedia.org/wiki/Tz_database)

**--vm-start-schedule**:
Schedule for starting the instance, specified using standard CRON format.

**--vm-stop-schedule**:
Schedule for stopping the instance, specified using standard CRON format.

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
gcloud alpha compute resource-policies update instance-schedule
```

```
gcloud beta compute resource-policies update instance-schedule
```