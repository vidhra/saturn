# gcloud scc posture-deployments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update)*

**NAME**

: **gcloud scc posture-deployments update - update the given Cloud Security Command Center posture deployment**

**SYNOPSIS**

: **`gcloud scc posture-deployments update` (`[POSTURE_DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#POSTURE_DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--description)`=`DESCRIPTION`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--etag)`=`ETAG`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--update-mask)`=`UPDATE_MASK`] [`[--posture-id](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--posture-id)`=`POSTURE_ID` `[--posture-revision-id](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#--posture-revision-id)`=`POSTURE_REVISION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Security Command Center (SCC) posture deployment.
Fields specified in update-mask flag are updated. Updatable fields are
description and posture_name with posture_revision-id. The target_resource for a
posture deployment cannot be updated. The posture deployment to be updated
should be in ACTIVE State. An empty or "`" update-mask implies that
posture-id and posture-revision-id are to be updated. If posture details of
posture deployment need to be updated, then the desired posture needs to be in
ACTIVE state. LRO operation ID is returned as the response of the command.`

**EXAMPLES**

: Update the description of the posture deployment named
`foo-posture-deployment` in the organization
`organizations/123/locations/global`:
```
gcloud scc posture-deployments update organizations/123/locations/global/postureDeployments/foo-posture-deployment --update-mask=description --description="updated-description"
```

Update posture deployment named `foo-posture-deployment` with the
posture named `foo-posture` and revision_id `abcdefgh` in
the organization `organizations/123/locations/global`:
```
gcloud scc posture-deployments update organizations/123/locations/global/postureDeployments/foo-posture-deployment --update-mask=posture_id,posture_revision-id --posture-id=foo-posture --posture-revision-id=abcdefgh
```

```
Update posture deployment named `foo-posture-deployment` with the posture named `foo-posture` and revision_id `abcdefgh` in the organization `organizations/123/locations/global`:
gcloud scc posture-deployments update organizations/123/locations/global/postureDeployments/foo-posture-deployment --posture-id=foo-posture --posture-revision-id=abcdefgh
```

**POSITIONAL ARGUMENTS**

: **Posture deployment resource - The posture deployment to update. For example
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

**--description**:
Updated description of posture deployment.

**--etag**:
Etag is an optional flag. If the provided Etag doesn't match the server
generated Etag, the update operation won't proceed.

**--update-mask**:
Comma-separated string containing list of fields to be updated.

**--posture-id**:
Relative name of the posture to be updated, like
`organizations/<organizationID>/locations/<location>/postures/<postureID>`.

**--posture-revision-id**:
Revision ID of the posture to be updated.

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
gcloud alpha scc posture-deployments update
```