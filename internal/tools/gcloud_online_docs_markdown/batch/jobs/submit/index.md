# gcloud batch jobs submit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit)*

**NAME**

: **gcloud batch jobs submit - submit a Batch job**

**SYNOPSIS**

: **`gcloud batch jobs submit` [[`[JOB](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#JOB)`] `[--location](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--location)`=`LOCATION`] (`[--config](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--config)`=`PATH_TO_FILE` `[--container-commands-file](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--container-commands-file)`=`CONTAINER_COMMANDS_FILE` `[--container-entrypoint](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--container-entrypoint)`=`CONTAINER_ENTRYPOINT` `[--container-image-uri](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--container-image-uri)`=`CONTAINER_IMAGE_URI`     | `[--script-file-path](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--script-file-path)`=`SCRIPT_FILE_PATH`     | `[--script-text](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--script-text)`=`SCRIPT_TEXT`) [`[--job-prefix](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--job-prefix)`=`JOB_PREFIX`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--machine-type)`=`MACHINE_TYPE`] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--priority)`=`PRIORITY`] [`[--provisioning-model](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--provisioning-model)`=`PROVISIONING_MODEL`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--network)`=`NETWORK` `[--subnetwork](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--subnetwork)`=`SUBNETWORK` : `[--no-external-ip-address](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--external-ip-address)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates and submits a Batch job. After you create and submit the
job, Batch automatically queues, schedules, and executes it.

**EXAMPLES**

: To submit a job with a sample JSON configuration file (config.json) and name
`projects/foo/locations/us-central1/jobs/bar`, run:

```
gcloud batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=config.json
```

To submit a job with a sample YAML configuration file (config.yaml) and name
projects/foo/locations/us-central1/jobs/bar, run:

```
gcloud batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=config.yaml
```

To submit a job through stdin with a sample job configuration and name
`projects/foo/locations/us-central1/jobs/bar`, run:

```
gcloud batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=-
```

```
then input json job config via stdin
{
  job config
}
```

To submit a job through HereDoc with a sample job configuration and name
`projects/foo/locations/us-central1/jobs/bar`, run:

```
gcloud batch jobs submit projects/foo/locations/us-central1/jobs/bar --config=- << EOF
```

```
{
  job config
}
EOF
```

For details about how to define a job's configuration using JSON, see the
projects.locations.jobs resource in the Batch API Reference. If you want to
define a job's configuration using YAML, convert the JSON syntax to YAML.

**POSITIONAL ARGUMENTS**

: **Job resource - The Batch job resource. If --location not specified,the current
batch/location is used. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- job ID is optional and will be generated if not specified with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`JOB`]**:
ID of the job or fully qualified identifier for the job.
To set the `job` attribute:

- provide the argument `JOB` on the command line;
- job ID is optional and will be generated if not specified.

**--location**:
Google Cloud location for the job.
To set the `location` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- job ID is optional and will be generated if not specified with a fully specified
name;
- provide the argument `--location` on the command line;
- set the property `batch/location`.**

**REQUIRED FLAGS**

: **--config**

**OPTIONAL FLAGS**

: **--job-prefix**:
Specify the job prefix. A job ID in the format of job prefix + %Y%m%d-%H%M%S
will be generated. Note that job prefix cannot be specified while JOB ID
positional argument is specified.

**--machine-type**:
Specify the Compute Engine machine type, for example, e2-standard-4. Currently
only one machine type is supported.

**--priority**:
Job priority [0-99] 0 is the lowest priority.

**--provisioning-model**:
Specify the allowed provisioning model for the compute instances.
`PROVISIONING_MODEL` must be one of:

**`SPOT`**:
The SPOT VM provisioning model. Ideal for fault-tolerant workloads that can
withstand preemption.

**`STANDARD`**:
The STANDARD VM provisioning model

**--network**:
The URL for the network resource. Must specify subnetwork as well if network is
specified

**--subnetwork**:
The URL for the subnetwork resource. Must specify network as well if subnetwork
is specified

**--no-external-ip-address**:
Required if no external public IP address is attached to the VM. If no external
public IP address, additional configuration is required to allow the VM to
access Google Services.

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
gcloud alpha batch jobs submit
```

```
gcloud beta batch jobs submit
```