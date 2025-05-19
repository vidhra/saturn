# gcloud compute instances ops-agents policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe)*

**NAME**

: **gcloud compute instances ops-agents policies describe - describe a Google Cloud Observability agents policy for the Ops Agent**

**SYNOPSIS**

: **`gcloud compute instances ops-agents policies describe` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe#POLICY_ID)` `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe#--zone)`=`ZONE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/instances/ops-agents/policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute instances ops-agents policies describe` describes a
policy that facilitates agent management across Compute Engine instances based
on user specified instance filters. This policy installs, specifies versioning,
and removes Ops Agents.
The command returns the content of one policy. For instance:

```
agentsRule:
  packageState: installed
  version: latest
instanceFilter:
  inclusionLabels:
  - labels:
      env: prod
```

If no policies are found, then the command returns a `NOT_FOUND`
error.

**EXAMPLES**

: To describe an agents policy named `ops-agents-test-policy` in the
current project, run:

```
gcloud compute instances ops-agents policies describe ops-agents-test-policy --zone=ZONE
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
ID of the policy.
This ID must contain only lowercase letters, numbers, and hyphens, end with a
number or a letter, be between 1-63 characters, and be unique within the
project.

**REQUIRED FLAGS**

: **--zone**:
Zone of the agents policy.

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
gcloud alpha compute instances ops-agents policies describe
```

```
gcloud beta compute instances ops-agents policies describe
```