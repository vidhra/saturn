# gcloud network-security intercept-deployment-groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/describe](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/describe)*

**NAME**

: **gcloud network-security intercept-deployment-groups describe - describe an Intercept Deployment Group**

**SYNOPSIS**

: **`gcloud network-security intercept-deployment-groups describe` (`[INTERCEPT_DEPLOYMENT_GROUP](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/describe#INTERCEPT_DEPLOYMENT_GROUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an intercept deployment group.
For more examples, refer to the EXAMPLES section below.

**EXAMPLES**

: To get a description of an intercept deployment group called
`my-deployment-group` in project ID `my-project`, run:

```
gcloud network-security intercept-deployment-groups describe my-deployment-group --project=my-project --location=global
```

OR

```
gcloud network-security intercept-deployment-groups describe projects/my-project/locations/global/interceptDeploymentGroups/my-deployment-group
```

**POSITIONAL ARGUMENTS**

: **Intercept deployment group resource - Intercept Deployment Group. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT_GROUP` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INTERCEPT_DEPLOYMENT_GROUP`**:
ID of the intercept deployment group or fully qualified identifier for the
intercept deployment group.
To set the `deployment-group-id` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT_GROUP` on the command
line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the intercept deployment group.
To set the `location` attribute:

- provide the argument `INTERCEPT_DEPLOYMENT_GROUP` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.**

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

**NOTES**

: These variants are also available:

```
gcloud alpha network-security intercept-deployment-groups describe
```

```
gcloud beta network-security intercept-deployment-groups describe
```