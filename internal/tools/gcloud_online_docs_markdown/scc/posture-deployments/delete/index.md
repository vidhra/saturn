# gcloud scc posture-deployments delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete)*

**NAME**

: **gcloud scc posture-deployments delete - delete a Cloud Security Command Center posture deployment**

**SYNOPSIS**

: **`gcloud scc posture-deployments delete` (`[POSTURE_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete#POSTURE_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud Security Command Center (SCC) posture deployment.

**EXAMPLES**

: Delete the posture deployment named
`organizations/123/locations/global/postureDeployments/posture-deployment-foo`
(i.e. a posture deployment in organization `123`, location
`global`, with id `posture-deployment-foo`):

```
gcloud scc posture-deployments delete organizations/123/locations/global/postureDeployments/posture-deployment-foo
```

Delete the posture deployment named
`organizations/123/locations/global/postureDeployments/posture-deployment-foo`
(i.e. a posture deployment in organization `123`, location
`global`, with id `posture-deployment-foo`) for the ETAG
ABcdO1Rf5clu7Yhlkwgelo7Vl4tiqd7Sy5iP5SdkSVU

```
gcloud scc posture-deployments delete organizations/123/locations/global/postureDeployments/posture-deployment-foo --etag=ABcdO1Rf5clu7Yhlkwgelo7Vl4tiqd7Sy5iI5SdkSVU
```

**POSITIONAL ARGUMENTS**

: **Posture deployment resource - The posture deployment to delete. For example
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
Etag is an optional flag. If the provided Etag doesn't match the server
generated Etag, the delete operation won't proceed.

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
gcloud alpha scc posture-deployments delete
```