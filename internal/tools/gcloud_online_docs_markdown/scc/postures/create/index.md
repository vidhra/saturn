# gcloud scc postures create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/postures/create](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create)*

**NAME**

: **gcloud scc postures create - create a Cloud Security Command Center posture**

**SYNOPSIS**

: **`gcloud scc postures create` (`[POSTURE](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create#POSTURE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create#--organization)`=`ORGANIZATION`) `[--posture-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create#--posture-from-file)`=`PATH_TO_FILE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/postures/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Security Command Center (SCC) posture. First argument consists of
the parent and name of the posture to be created. The posture details are
provided in YAML file. The file path is mentioned in
`--posture-from-file` flag.
Created posture is returned as the response of the command. LRO operation ID is
printed as the standard output.

**EXAMPLES**

: Create a posture named `posture-foo-1` within parent
`organizations/123/locations/global`(i.e. a posture in organization
`123`, location `global`, with ID
`posture-foo-1`):

```
gcloud scc postures create organizations/123/locations/global/postures/posture-foo-1 --posture-from-file=posture.yaml
```

**POSITIONAL ARGUMENTS**

: **Posture resource - The name of the posture to be created. For example
organizations/<organizationID>/locations/<location>/postures/<postureID>.
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`POSTURE`**:
ID of the posture or fully qualified identifier for the posture.
To set the `posture` attribute:

- provide the argument `posture` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location where the resource exists (for example, global).
To set the `location` attribute:

- provide the argument `posture` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
ID of the organization which is the parent of the resource.
To set the `organization` attribute:

- provide the argument `posture` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line.**

**REQUIRED FLAGS**

: **--posture-from-file**:
YAML file containing the body of the posture to be created. Use a full or
relative path to a local file containing the value of posture.

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
gcloud alpha scc postures create
```