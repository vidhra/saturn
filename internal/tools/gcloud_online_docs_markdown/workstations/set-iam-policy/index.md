# gcloud workstations set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy)*

**NAME**

: **gcloud workstations set-iam-policy - set the IAM policy for a workstation**

**SYNOPSIS**

: **`gcloud workstations set-iam-policy` (`[WORKSTATION](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy#WORKSTATION)` : `[--cluster](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy#--cluster)`=`CLUSTER` `[--config](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy#--config)`=`CONFIG` `[--region](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy#--region)`=`REGION`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/workstations/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for the given workstation as defined in a JSON or YAML file.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'policy.json' and set it for the given workstation:

```
gcloud workstations set-iam-policy WORKSTATION policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **Workstation resource - The workstation for which to display the IAM policy. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKSTATION`**:
ID of the workstation or fully qualified identifier for the workstation.
To set the `workstation` attribute:

- provide the argument `workstation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--cluster**:
The name of the cluster containing the workstation.
To set the `cluster` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--cluster` on the command line;
- set the property `workstations/cluster`.

**--config**:
The name of the config containing the workstation.
To set the `config` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--config` on the command line;
- set the property `workstations/config`.

**--region**:
The name of the region of the workstation.
To set the `region` attribute:

- provide the argument `workstation` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `workstations/region`.**

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

: This command uses the `workstations/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/workstations](https://cloud.google.com/workstations)

**NOTES**

: These variants are also available:

```
gcloud alpha workstations set-iam-policy
```

```
gcloud beta workstations set-iam-policy
```