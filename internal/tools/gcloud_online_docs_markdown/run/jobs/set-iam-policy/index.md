# gcloud run jobs set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy)*

**NAME**

: **gcloud run jobs set-iam-policy - set the IAM policy for a job**

**SYNOPSIS**

: **`gcloud run jobs set-iam-policy` `[JOB](https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy#JOB)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy#POLICY_FILE)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command replaces the existing IAM policy for a job, given a job and a file
encoded in JSON or YAML that contains the IAM policy. If the given policy file
specifies an "etag" value, then the replacement will succeed only if the policy
already in place matches that etag. (An etag obtain via
`get-iam-policy` will prevent the replacement if the policy for the
job has been subsequently updated.) A policy file that does not contain an etag
value will replace any existing policy for the job.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'policy.json' and set it for a job with identifier 'my-job'

```
gcloud run jobs set-iam-policy --region=us-central1 my-job policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **Job resource - The job for which to set the IAM policy. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `job` on the command line with a fully specified
name;
- provide the argument `--region` on the command line;
- set the property `run/region`;
- specify from a list of available regions in a prompt.

This must be specified.

**`JOB`**:
ID of the job or fully qualified identifier for the job.
To set the `job` attribute:

- provide the argument `job` on the command line.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

**FLAGS**

: **--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

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

: This command uses the `run/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/run/](https://cloud.google.com/run/)

**NOTES**

: These variants are also available:

```
gcloud alpha run jobs set-iam-policy
```

```
gcloud beta run jobs set-iam-policy
```