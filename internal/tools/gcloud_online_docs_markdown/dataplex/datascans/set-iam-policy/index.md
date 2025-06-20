# gcloud dataplex datascans set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/set-iam-policy)*

**NAME**

: **gcloud dataplex datascans set-iam-policy - set the IAM policy to a Dataplex datascan as defined in a JSON or YAML file**

**SYNOPSIS**

: **`gcloud dataplex datascans set-iam-policy` (`[DATASCAN](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/set-iam-policy#DATASCAN)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/set-iam-policy#--location)`=`LOCATION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/datascans/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
`policy.son` and set it for the Dataplex datascan
`test-datascan` defined in location `us-central1`:

```
gcloud dataplex datascans set-iam-policy --location=us-central1 test-datascan policy.json
```

**POSITIONAL ARGUMENTS**

: **Datascan resource - Arguments and flags that define the Dataplex datascan you
want to set IAM policy binding to. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `datascan` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATASCAN`**:
ID of the datascan or fully qualified identifier for the datascan.
To set the `dataScans` attribute:

- provide the argument `datascan` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `datascan` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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

: This variant is also available:

```
gcloud alpha dataplex datascans set-iam-policy
```