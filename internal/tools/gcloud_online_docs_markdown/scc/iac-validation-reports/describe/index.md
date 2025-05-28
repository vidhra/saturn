# gcloud scc iac-validation-reports describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/describe](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/describe)*

**NAME**

: **gcloud scc iac-validation-reports describe - describe a Cloud Security Command Center IaC Validation Report**

**SYNOPSIS**

: **`gcloud scc iac-validation-reports describe` (`[REPORT](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/describe#REPORT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/describe#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/iac-validation-reports/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Security Command Center (SCC) IaC Validation Report. Takes the
name of the report as an argument.
Returns IAC Validation Report as response.

**EXAMPLES**

: Describe an IAC Validation report named
`organizations/123/locations/global/reports/abcef-gh` :

```
gcloud scc iac-validation-reports describe organizations/123/locations/global/reports/abcef-gh
```

```
or, run:
```

```
gcloud scc iac-validation-reports describe abcef-gh --organization=123 --location=global
```

**POSITIONAL ARGUMENTS**

: **Report resource - IAC Validation report to be described. For example
`organizations/123/locations/global/reports/abcef-gh`. The arguments
in this group can be used to specify the attributes of this resource.
This must be specified.

**`REPORT`**:
ID of the report or fully qualified identifier for the report.
To set the `report` attribute:

- provide the argument `report` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location where the resource exists (for example, global).
To set the `location` attribute:

- provide the argument `report` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
ID of the organization which is the parent of the resource.
To set the `organization` attribute:

- provide the argument `report` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

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
gcloud alpha scc iac-validation-reports describe
```