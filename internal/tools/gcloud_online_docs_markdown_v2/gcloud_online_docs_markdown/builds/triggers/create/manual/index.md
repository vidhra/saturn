# gcloud builds triggers create manual  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual)*

**NAME**

: **gcloud builds triggers create manual - create a build trigger with a manual trigger event**

**SYNOPSIS**

: **`gcloud builds triggers create manual` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--trigger-config)`=`PATH`     | [(`[--build-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/" `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--dockerfile-image)`=`DOCKERFILE_IMAGE`]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--description)`=`DESCRIPTION` `[--name](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--service-account)`=`SERVICE_ACCOUNT` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--substitutions)`=[`KEY`=`VALUE`,…] `[--branch](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--branch)`=`BRANCH` | `[--tag](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--tag)`=`TAG` `[--repository](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--repository)`=`REPOSITORY` | [`[--repo](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--repo)`=`REPO` `[--repo-type](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--repo-type)`=`REPO_TYPE` : `[--github-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#--github-enterprise-config)`=`GITHUB_ENTERPRISE_CONFIG`]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/manual#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a build trigger with a manual trigger event.

**EXAMPLES**

: To create a manual trigger that builds off branch `my-branch` in a
GitHub repository named `my-repo`:

```
gcloud builds triggers create manual --name=my-manual-trigger --build-config=cloudbuild.yaml --repo=https://www.github.com/owner/repo --repo-type=GITHUB --branch=my-branch
```

To create a manual trigger that builds off branch `my-branch` in a
2nd-gen GitHub repository resource:

```
gcloud builds triggers create manual --name=my-manual-trigger --build-config=cloudbuild.yaml --repository=projects/my-proj/locations/us-west1/connections/my-conn/repositories/my-repo --branch=my-branch
```

**REQUIRED FLAGS**

: **--trigger-config**

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
gcloud alpha builds triggers create manual
```

```
gcloud beta builds triggers create manual
```