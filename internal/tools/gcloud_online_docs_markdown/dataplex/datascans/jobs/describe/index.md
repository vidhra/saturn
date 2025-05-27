# gcloud dataplex datascans jobs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe)*

**NAME**

: **gcloud dataplex datascans jobs describe - describe a Dataplex datascan job**

**SYNOPSIS**

: **`gcloud dataplex datascans jobs describe` (`[JOB](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe#JOB)` : `[--datascan](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe#--datascan)`=`DATASCAN` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe#--location)`=`LOCATION`) [`[--view](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe#--view)`=`VIEW`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/jobs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Dataplex datascan job.
Displays all details of a Dataplex job given a valid job ID.

**EXAMPLES**

: To describe a Dataplex job `test-job` running a datascan
`test-datascan` in location `us-central1`, run:

```
gcloud dataplex datascans jobs describe test-job --location=us-central1 --datascan=test-datascan
```

To describe the details of Dataplex job `test-job` running a datascan
`test-datascan` in location `us-central1`, run:

```
gcloud dataplex datascans jobs describe test-job --location=us-central1 --datascan=test-datascan --view=FULL
```

**POSITIONAL ARGUMENTS**

: **Job resource - Arguments and flags that define the Dataplex Job running a
particular Datascan you want to retrieve. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`JOB`**:
ID of the job or fully qualified identifier for the job.
To set the `job` attribute:

- provide the argument `job` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--datascan**:
Datascan ID of the Dataplex datascan resource.
To set the `datascan` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--datascan` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--view**:
Displays spec and result data based on the argument value. The default view is
'basic'. `VIEW` must be one of:

**`basic`**:
Does not include spec and result data in response.

**`full`**:
Includes spec and result data in response.

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
gcloud alpha dataplex datascans jobs describe
```