# gcloud builds triggers create bitbucketserver  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver)*

**NAME**

: **gcloud builds triggers create bitbucketserver - create a build trigger for a Bitbucket Server repository**

**SYNOPSIS**

: **`gcloud builds triggers create bitbucketserver` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--trigger-config)`=`PATH`     | [`[--bitbucket-server-config-resource](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--bitbucket-server-config-resource)`=`BITBUCKET_SERVER_CONFIG_RESOURCE` `[--project-key](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--project-key)`=`PROJECT_KEY` `[--repo-slug](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--repo-slug)`=`REPO_SLUG` (`[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--branch-pattern)`=`REGEX` | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--tag-pattern)`=`REGEX` | [`[--pull-request-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--pull-request-pattern)`=`REGEX` : `[--comment-control](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--comment-control)`=`COMMENT_CONTROL`; default=`"COMMENTS_ENABLED"`]) (`[--build-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/" `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--dockerfile-image)`=`DOCKERFILE_IMAGE`]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--description)`=`DESCRIPTION` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--ignored-files)`=[`GLOB`,…] `[--included-files](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--included-files)`=[`GLOB`,…] `[--name](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--service-account)`=`SERVICE_ACCOUNT` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#--substitutions)`=[`KEY`=`VALUE`,…]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/create/bitbucketserver#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a build trigger for a Bitbucket Server repository.

**EXAMPLES**

: To create a push trigger for all branches:

```
gcloud builds triggers create bitbucketserver --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --project-key="GoogleCloudPlatform" --repo-slug="cloud-builders" --bitbucket-server-config-resource="projects/1234/locations/global/bitbucketServerConfigs/5678" --branch-pattern=".*" --build-config="cloudbuild.yaml"
```

To create a pull request trigger for main:

```
gcloud builds triggers create bitbucketserver --name="my-trigger" --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --project-key="GoogleCloudPlatform" --repo-slug="cloud-builders" --bitbucket-server-config-resource="projects/1234/locations/global/bitbucketServerConfigs/5678" --pull-request-pattern="^main$" --build-config="cloudbuild.yaml"
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
gcloud alpha builds triggers create bitbucketserver
```

```
gcloud beta builds triggers create bitbucketserver
```