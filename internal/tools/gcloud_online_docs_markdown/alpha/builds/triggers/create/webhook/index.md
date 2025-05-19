# gcloud alpha builds triggers create webhook  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook)*

**NAME**

: **gcloud alpha builds triggers create webhook - create a build trigger with a Webhook trigger event**

**SYNOPSIS**

: **`gcloud alpha builds triggers create webhook` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--trigger-config)`=`PATH`     | [`[--secret](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--secret)`=`SECRET` (`[--build-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/" `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--dockerfile-image)`=`DOCKERFILE_IMAGE`]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--description)`=`DESCRIPTION` `[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--service-account)`=`SERVICE_ACCOUNT` `[--subscription-filter](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--subscription-filter)`=`SUBSCRIPTION_FILTER` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--substitutions)`=[`KEY`=`VALUE`,…] `[--branch](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--branch)`=`BRANCH` | `[--tag](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--tag)`=`TAG` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--repository)`=`REPOSITORY` | [`[--repo](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--repo)`=`REPO` `[--repo-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--repo-type)`=`REPO_TYPE` : `[--github-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#--github-enterprise-config)`=`GITHUB_ENTERPRISE_CONFIG`]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a build trigger with a Webhook trigger event.

**EXAMPLES**

: To create a Webhook trigger that requires secret
`projects/my-project/secrets/my-secret/versions/2` and builds off
branch `my-branch` in a GitHub repository named `my-repo`:

```
gcloud alpha builds triggers create webhook --name=my-webhook-trigger --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --secret=projects/my-project/secrets/my-secret/versions/2 --repo=https://www.github.com/owner/repo --repo-type=GITHUB --branch=my-branch
```

To create a Webhook trigger that requires secret
`projects/my-project/secrets/my-secret/versions/2` and builds off
branch `my-branch` in a 2nd-gen GitHub repository:

```
gcloud alpha builds triggers create webhook --name=my-webhook-trigger --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --secret=projects/my-project/secrets/my-secret/versions/2 --branch=my-branch --repository=projects/my-proj/locations/us-west1/connections/my-conn/repositories/my-repo
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
allowlist. These variants are also available:

```
gcloud builds triggers create webhook
```

```
gcloud beta builds triggers create webhook
```