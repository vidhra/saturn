# gcloud scc iac-validation-reports create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create)*

**NAME**

: **gcloud scc iac-validation-reports create - create a Cloud Security Command Center IaC Validation Report**

**SYNOPSIS**

: **`gcloud scc iac-validation-reports create` `[PARENT](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create#PARENT)` `[--tf-plan-file](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create#--tf-plan-file)`=`PATH_TO_FILE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Security Command Center (SCC) IaC Validation Report. First
argument is the parent of the IaC defined in the plan file. It is followed by
path of the terraform plan file in JSON format.
LRO operation ID is returned as the response of the command.

**EXAMPLES**

: Create an Iac Validation report on parent
`organizations/123/locations/global`:

```
gcloud scc iac-validation-reports create organizations/123/locations/global --tf-plan-file=planFile.json
```

**POSITIONAL ARGUMENTS**

: **`PARENT`**:
Name of the organization where IaC Validation Report is to be created. Format:
organizations/<organizationID>/locations/<location>

**REQUIRED FLAGS**

: **--tf-plan-file**:
Path to a JSON file containing the IaC plan to be validated. Use a full or
relative path to a local file containing the value of tf_plan_file.

**OPTIONAL FLAGS**

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

: This command uses the `securityposture/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: This variant is also available:

```
gcloud alpha scc iac-validation-reports create
```