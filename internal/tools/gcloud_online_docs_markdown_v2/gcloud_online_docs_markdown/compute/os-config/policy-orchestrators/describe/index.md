# gcloud compute os-config policy-orchestrators describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe)*

**NAME**

: **gcloud compute os-config policy-orchestrators describe - describe a policy orchestrator**

**SYNOPSIS**

: **`gcloud compute os-config policy-orchestrators describe` (`[POLICY_ORCHESTRATOR](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe#POLICY_ORCHESTRATOR)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/policy-orchestrators/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the details of a policy orchestrator.

**EXAMPLES**

: To describe a policy orchestrator `my-orchestrator`:

```
gcloud compute os-config policy-orchestrators describe my-orchestrator
```

**POSITIONAL ARGUMENTS**

: **Policy orchestrator resource - The policy orchestrator to describe. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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
gcloud alpha compute os-config policy-orchestrators describe
```

```
gcloud beta compute os-config policy-orchestrators describe
```