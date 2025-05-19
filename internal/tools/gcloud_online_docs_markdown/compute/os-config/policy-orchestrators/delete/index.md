# gcloud compute os-config policy-orchestrators delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete)*

**NAME**

: **gcloud compute os-config policy-orchestrators delete - delete a policy orchestrator**

**SYNOPSIS**

: **`gcloud compute os-config policy-orchestrators delete` (`[POLICY_ORCHESTRATOR](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete#POLICY_ORCHESTRATOR)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a policy orchestrator and cancel ongoing rollouts (best-effort).

**EXAMPLES**

: To delete a policy orchestrator `my-orchestrator` in the folder
`123456`:

```
gcloud compute os-config policy-orchestrators delete my-orchestrator --folder=123456
```

**POSITIONAL ARGUMENTS**

: **Policy orchestrator resource - policy orchestrator to delete. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `policy_orchestrator` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [policy_orchestrator_project, policy_orchestrator_folder,
policy_orchestrator_organization].

This must be specified.

**`POLICY_ORCHESTRATOR`**:
ID of the policy_orchestrator or fully qualified identifier for the
policy_orchestrator.
To set the `policy_orchestrator` attribute:

- provide the argument `policy_orchestrator` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--folder**:
Folder of the policy_orchestrator.
To set the `folder` attribute:

- provide the argument `policy_orchestrator` on the command line with a
fully specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type [policy_orchestrator_folder].

**--organization**:
Organization of the policy_orchestrator.
To set the `organization` attribute:

- provide the argument `policy_orchestrator` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type [policy_orchestrator_organization].**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `osconfig/v2` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/osconfig/rest](https://cloud.google.com/compute/docs/osconfig/rest)

**NOTES**

: These variants are also available:

```
gcloud alpha compute os-config policy-orchestrators delete
```

```
gcloud beta compute os-config policy-orchestrators delete
```