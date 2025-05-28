# gcloud scc posture-deployments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create)*

**NAME**

: **gcloud scc posture-deployments create - create a Cloud Security Command Center posture deployment**

**SYNOPSIS**

: **`gcloud scc posture-deployments create` (`[POSTURE_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#POSTURE_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--organization)`=`ORGANIZATION`) `[--posture-name](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--posture-name)`=`POSTURE_NAME` `[--posture-revision-id](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--posture-revision-id)`=`POSTURE_REVISION_ID` `[--target-resource](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--target-resource)`=`TARGET_RESOURCE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Security Command Center (SCC) posture deployment. First argument
is the parent of the posture deployment to be created. Second argument is the
name of the posture deployment to be created. It is followed by details of the
posture to be deployed and the target_resource to be deployed on.
LRO operation ID is returned as the response of the command.

**EXAMPLES**

: Create a posture deployment named `posture-deployment-foo-1` within
parent `organizations/123/locations/global` on resource
`folders/456` (i.e. a posture-deployment in organization
`123`, location `global`, with id
`posture-deployment-foo-1`, which deploys posture
`organizations/123/locations/foo-posture` with revision-id
`foo-posture-revision-id` on `folders/456`):

```
gcloud scc posture-deployments create organizations/123/locations/global/postureDeployments/posture-deployment-foo-1 --posture-name=organizations/123/locations/global/foo-posture --posture-revision-id=foo-posture-revision-id --target-resource=projects/456
```

**POSITIONAL ARGUMENTS**

: **Posture deployment resource - The name of the posture deployment to be created.
For example
organizations/<organizationID>/locations/<location>/postureDeployments/<postureDeploymentID>.
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`POSTURE_DEPLOYMENT`**:
ID of the posture_deployment or fully qualified identifier for the
posture_deployment.
To set the `posture_deployment` attribute:

- provide the argument `posture_deployment` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location where the resource exists (for example, global).
To set the `location` attribute:

- provide the argument `posture_deployment` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
ID of the organization which is the parent of the resource.
To set the `organization` attribute:

- provide the argument `posture_deployment` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.**

**REQUIRED FLAGS**

: **--posture-name**:
Posture that needs to be deployed. Format:
organizations/<organizationID>/locations/<location>/postures/<postureID>

**--posture-revision-id**:
Posture revision that needs to be deployed.

**--target-resource**:
Name of the workload on which posture deployment is to be created. It could be
an organization, folder or a project. Possible formats: |
organizations/<organizationID> | folders/<folderID> |
projects/<projectID> The above mentioned IDs need to have numeric format.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
User-provided description of the posture deployment.

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
gcloud alpha scc posture-deployments create
```