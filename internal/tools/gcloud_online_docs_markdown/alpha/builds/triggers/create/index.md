# gcloud alpha builds triggers create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create)*

**NAME**

: **gcloud alpha builds triggers create - create build triggers for Google Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds triggers create` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create build triggers for Google Cloud Build.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[bitbucket-cloud](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/bitbucket-cloud)`**:
`(ALPHA)` Create a build trigger for a 2nd-gen Bitbucket Cloud
repository.

**`[bitbucket-data-center](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/bitbucket-data-center)`**:
`(ALPHA)` Create a build trigger for a 2nd-gen Bitbucket Data Center
repository.

**`[bitbucketserver](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/bitbucketserver)`**:
`(ALPHA)` Create a build trigger for a Bitbucket Server repository.

**`[cloud-source-repositories](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/cloud-source-repositories)`**:
`(ALPHA)` Create a build trigger from a Cloud Source Repository.

**`[developer-connect](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/developer-connect)`**:
`(ALPHA)` Create a build trigger for a Developer Connect repository.

**`[github](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/github)`**:
`(ALPHA)` Create a build trigger for a GitHub repository.

**`[gitlab](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/gitlab)`**:
`(ALPHA)` Create a build trigger for a 2nd-gen GitLab repository.

**`[manual](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/manual)`**:
`(ALPHA)` Create a build trigger with a manual trigger event.

**`[pubsub](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/pubsub)`**:
`(ALPHA)` Create a build trigger with a Pub/Sub trigger event.

**`[webhook](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/triggers/create/webhook)`**:
`(ALPHA)` Create a build trigger with a Webhook trigger event.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud builds triggers create
```

```
gcloud beta builds triggers create
```