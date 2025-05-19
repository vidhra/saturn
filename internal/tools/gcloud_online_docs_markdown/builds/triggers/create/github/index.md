# gcloud builds triggers create github  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github)*

**NAME**

: **gcloud builds triggers create github - create a build trigger for a GitHub repository**

**SYNOPSIS**

: **`gcloud builds triggers create github` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--trigger-config)`=`PATH`     | [(`[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--branch-pattern)`=`REGEX` | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--tag-pattern)`=`REGEX` | [`[--pull-request-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--pull-request-pattern)`=`REGEX` : `[--comment-control](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--comment-control)`=`COMMENT_CONTROL`; default=`"COMMENTS_ENABLED"`]) (`[--build-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/" `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--dockerfile-image)`=`DOCKERFILE_IMAGE`]) (`[--repository](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--repository)`=`REPOSITORY` | [`[--repo-name](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--repo-name)`=`REPO_NAME` `[--repo-owner](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--repo-owner)`=`REPO_OWNER` : `[--enterprise-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--enterprise-config)`=`ENTERPRISE_CONFIG`]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--description)`=`DESCRIPTION` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--ignored-files)`=[`GLOB`,…] `[--include-logs-with-status](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--include-logs-with-status)` `[--included-files](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--included-files)`=[`GLOB`,…] `[--name](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--service-account)`=`SERVICE_ACCOUNT` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#--substitutions)`=[`KEY`=`VALUE`,…]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/github#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a build trigger for a GitHub repository.

**EXAMPLES**

: To create a push trigger with a 1st-gen repository for all branches:

```
gcloud builds triggers create github --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --repo-owner="GoogleCloudPlatform" --repo-name="cloud-builders" --branch-pattern=".*" --build-config="cloudbuild.yaml"
```

To create a pull request trigger with a 1st-gen repository for master:

```
gcloud builds triggers create github --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --repo-owner="GoogleCloudPlatform" --repo-name="cloud-builders" --pull-request-pattern="^master$" --build-config="cloudbuild.yaml"
```

To create a pull request trigger with a 2nd gen repository for master:

```
gcloud builds triggers create github --name="my-trigger" --repository=projects/my-project/locations/us-central1/connections/my-conn/repositories/my-repo --pull-request-pattern="^master$" --build-config="cloudbuild.yaml" --region=us-central1
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
gcloud alpha builds triggers create github
```

```
gcloud beta builds triggers create github
```