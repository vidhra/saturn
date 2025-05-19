# gcloud alpha builds triggers create developer-connect  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect)*

**NAME**

: **gcloud alpha builds triggers create developer-connect - create a build trigger for a Developer Connect repository**

**SYNOPSIS**

: **`gcloud alpha builds triggers create developer-connect` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--trigger-config)`=`PATH`     | [(`[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--branch-pattern)`=`REGEX` | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--tag-pattern)`=`REGEX` | [`[--pull-request-pattern](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--pull-request-pattern)`=`REGEX` : `[--comment-control](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--comment-control)`=`COMMENT_CONTROL`; default=`"COMMENTS_ENABLED"`]) (`[--build-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--dockerfile)`=`DOCKERFILE` `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--dockerfile-image)`=`DOCKERFILE_IMAGE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/"]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--description)`=`DESCRIPTION` `[--git-repository-link](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--git-repository-link)`=`GIT_REPOSITORY_LINK` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--ignored-files)`=[`GLOB`,…] `[--included-files](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--included-files)`=[`GLOB`,…] `[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--service-account)`=`SERVICE_ACCOUNT` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#--substitutions)`=[`KEY`=`VALUE`,…]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a build trigger for a Developer Connect repository.

**EXAMPLES**

: To create a push trigger with a DC repository for all branches:

```
gcloud alpha builds triggers create developer-connect --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --git-repository-link="projects/1234/locations/us-central1/connections/myconn/gitRepositoryLinks/mylink" --branch-pattern=".*" --build-config="cloudbuild.yaml" --region=us-central1
```

To create a pull request trigger with a DC repository for main:

```
gcloud alpha builds triggers create developer-connect --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --repository="projects/1234/locations/us-central1/connections/myconn/gitRepositoryLinks/mylink" --build-config="cloudbuild.yaml" --pull-request-pattern="^main$" --region=us-central1
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud beta builds triggers create developer-connect
```