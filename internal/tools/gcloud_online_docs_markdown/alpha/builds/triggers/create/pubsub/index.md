# gcloud alpha builds triggers create pubsub  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub)*

**NAME**

: **gcloud alpha builds triggers create pubsub - create a build trigger with a Pub/Sub trigger event**

**SYNOPSIS**

: **`gcloud alpha builds triggers create pubsub` (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--trigger-config)`=`PATH`     | [`[--topic](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--topic)`=`TOPIC` (`[--build-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--build-config)`=`PATH` | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--inline-config)`=`PATH` | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--dockerfile)`=`DOCKERFILE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--dockerfile-dir)`=`DOCKERFILE_DIR`; default="/" `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--dockerfile-image)`=`DOCKERFILE_IMAGE`]) : `[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--description)`=`DESCRIPTION` `[--name](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--name)`=`NAME` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--region)`=`REGION` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--service-account)`=`SERVICE_ACCOUNT` `[--subscription-filter](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--subscription-filter)`=`SUBSCRIPTION_FILTER` `[--substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--substitutions)`=[`KEY`=`VALUE`,…] `[--branch](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--branch)`=`BRANCH` | `[--tag](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--tag)`=`TAG` `[--repository](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--repository)`=`REPOSITORY` | [`[--repo](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--repo)`=`REPO` `[--repo-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--repo-type)`=`REPO_TYPE` : `[--github-enterprise-config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#--github-enterprise-config)`=`GITHUB_ENTERPRISE_CONFIG`]]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a build trigger with a Pub/Sub trigger event.

**EXAMPLES**

: To create a Pub/Sub trigger that listens to topic `my-topic` and
builds off branch `my-branch` in a GitHub repository named
`my-repo`:

```
gcloud alpha builds triggers create pubsub --name=my-pubsub-trigger --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --topic=projects/my-project/topics/my-topic --repo=https://www.github.com/owner/repo --repo-type=GITHUB --branch=my-branch
```

To create a Pub/Sub trigger that listens to topic `my-topic` and
builds off branch `my-branch` in a 2nd-gen GitHub repository
resource:

```
gcloud alpha builds triggers create pubsub --name=my-pubsub-trigger --service-account="projects/my-project/serviceAccounts/my-byosa@my-project.iam.gserviceaccount.com" --repository=projects/my-proj/locations/us-west1/connections/my-conn/repositories/my-repo --branch=my-branch
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
gcloud builds triggers create pubsub
```

```
gcloud beta builds triggers create pubsub
```