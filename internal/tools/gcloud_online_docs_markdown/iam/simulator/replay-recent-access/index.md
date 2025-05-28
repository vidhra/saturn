# gcloud iam simulator replay-recent-access  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access](https://cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access)*

**NAME**

: **gcloud iam simulator replay-recent-access - determine affected recent access attempts before IAM policy                 change deployment**

**SYNOPSIS**

: **`gcloud iam simulator replay-recent-access` `[RESOURCE](https://cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access#RESOURCE)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Replay the most recent 1,000 access logs from the past 90 days using the
simulated policy. For each log entry, the replay determines if setting the
provided policy on the given resource would result in a change in the access
state, e.g. a previously granted access becoming denied. Any differences found
are returned.

**EXAMPLES**

: To simulate a permission change of a member on a resource, run:

```
gcloud iam simulator replay-recent-access projects/project-id path/to/policy_file.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of policy role and member types.

**POSITIONAL ARGUMENTS**

: **`RESOURCE`**:
Full resource name to simulate the IAM policy for.
See: [https://cloud.google.com/apis/design/resource_names#full_resource_name](https://cloud.google.com/apis/design/resource_names#full_resource_name).

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a Policy. See [the Policy
reference](https://cloud.google.com/iam/reference/rest/v1/Policy) for details.

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