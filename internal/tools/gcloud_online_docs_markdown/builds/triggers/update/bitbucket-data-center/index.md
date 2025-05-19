# gcloud builds triggers update bitbucket-data-center  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center)*

**NAME**

: **gcloud builds triggers update bitbucket-data-center - updates Bitbucket Data Center trigger used by Cloud Build**

**SYNOPSIS**

: **`gcloud builds triggers update bitbucket-data-center` (`[TRIGGER](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#TRIGGER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--region)`=`REGION`) (`[--trigger-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--trigger-config)`=`PATH`     | `[--description](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--description)`=`DESCRIPTION` `[--ignored-files](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--ignored-files)`=[`GLOB`,…] `[--included-files](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--included-files)`=[`GLOB`,…] `[--repository](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--repository)`=`REPOSITORY` `[--[no-]require-approval](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--[no-]require-approval)` `[--service-account](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--service-account)`=`SERVICE_ACCOUNT` `[--branch-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--branch-pattern)`=`REGEX`     | `[--tag-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--tag-pattern)`=`REGEX`     | `[--comment-control](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--comment-control)`=`COMMENT_CONTROL` `[--pull-request-pattern](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--pull-request-pattern)`=`REGEX` `[--build-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--build-config)`=`PATH`     | `[--inline-config](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--inline-config)`=`PATH`     | [`[--dockerfile](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--dockerfile)`=`DOCKERFILE` `[--dockerfile-image](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--dockerfile-image)`=`DOCKERFILE_IMAGE` : `[--dockerfile-dir](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--dockerfile-dir)`=`DOCKERFILE_DIR`] `[--clear-substitutions](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--clear-substitutions)`     | `[--remove-substitutions](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--remove-substitutions)`=[`KEY`,…]     | `[--update-substitutions](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#--update-substitutions)`=[`KEY`=`VALUE`,…]) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/builds/triggers/update/bitbucket-data-center#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates Bitbucket Data Center trigger used by Cloud Build.

**EXAMPLES**

: To update the branch pattern of the trigger:

```
gcloud builds triggers update bitbucket-data-center my-trigger --branch-pattern=".*"
```

To update the build config of the trigger:

```
gcloud builds triggers update bitbucket-data-center my-trigger --build-config="cloudbuild.yaml"
```

To update the substitutions of the trigger:

```
gcloud builds triggers update bitbucket-data-center my-trigger --update-substitutions=_REPO_NAME=my-repo,_BRANCH_NAME=master
```

To update the 2nd-gen repository resource of the trigger:

```
gcloud builds triggers update bitbucket-data-center my-trigger --repository=projects/my-project/locations/us-west1/connections/my-conn/repositories/my-repo
```

**POSITIONAL ARGUMENTS**

: **Trigger resource - Build Trigger. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `TRIGGER` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TRIGGER`**:
ID of the trigger or fully qualified identifier for the trigger.
To set the `trigger` attribute:

- provide the argument `TRIGGER` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud location for the trigger.
To set the `region` attribute:

- provide the argument `TRIGGER` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `builds/region`.**

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
gcloud alpha builds triggers update bitbucket-data-center
```

```
gcloud beta builds triggers update bitbucket-data-center
```