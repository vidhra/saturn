# gcloud scc posture-templates describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe](https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe)*

**NAME**

: **gcloud scc posture-templates describe - describe a Cloud Security Command Center posture template**

**SYNOPSIS**

: **`gcloud scc posture-templates describe` (`[POSTURE_TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe#POSTURE_TEMPLATE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe#--organization)`=`ORGANIZATION`) [`[--revision-id](https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe#--revision-id)`=`REVISION_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Security Command Center (SCC) posture template.
By default, the latest created revision of the posture template is described.
Users must provide revision ID to describe a specific revision.

**EXAMPLES**

: Describe a posture template named
`organizations/123/locations/global/postureTemplates/secure_by_default`
(i.e. a posture in organization `123`, location `global`,
with id `secure_by_default`):

```
gcloud scc posture-templates describe organizations/123/locations/global/postureTemplates/secure_by_default
```

Describe a specific revision `v1.0.0` of posture template named
`organizations/123/locations/global/postureTemplates/secure_by_default`:

```
gcloud scc posture-templates describe organizations/123/locations/global/postureTemplates/secure_by_default --revision-id=v1.0.0
```

**POSITIONAL ARGUMENTS**

: **Posture template resource - Posture template to be described. For example
organizations/<organizationID>/locations/<location>/postureTemplates/<postureTemplateID>.
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`POSTURE_TEMPLATE`**:
ID of the posture_template or fully qualified identifier for the
posture_template.
To set the `posture_template` attribute:

- provide the argument `posture_template` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
ID of the location where the resource exists (for example, global).
To set the `location` attribute:

- provide the argument `posture_template` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
ID of the organization which is the parent of the resource.
To set the `organization` attribute:

- provide the argument `posture_template` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--revision-id**:
ID of the specific posture template revision to be described. If not specified,
latest revision is described.

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
gcloud alpha scc posture-templates describe
```