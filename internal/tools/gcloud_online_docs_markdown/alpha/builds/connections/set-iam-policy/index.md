# gcloud alpha builds connections set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/set-iam-policy)*

**NAME**

: **gcloud alpha builds connections set-iam-policy - set the IAM policy for a Cloud Build connection**

**SYNOPSIS**

: **`gcloud alpha builds connections set-iam-policy` (`[CONNECTION](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/set-iam-policy#CONNECTION)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/set-iam-policy#--region)`=`REGION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/connections/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Set the IAM policy for a Cloud Build connection as defined
in a JSON or YAML file.
See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'policy.json' and set it for the Connection named 'my-conn':

```
gcloud alpha builds connections set-iam-policy my-conn policy.json --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Connection resource - Cloud Build Connection for which to set IAM policy. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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

**API REFERENCE**

: This command uses the `cloudbuild/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/cloud-build/docs/](https://cloud.google.com/cloud-build/docs/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds connections set-iam-policy
```

```
gcloud beta builds connections set-iam-policy
```