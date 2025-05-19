# gcloud artifacts docker upgrade migrate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate)*

**NAME**

: **gcloud artifacts docker upgrade migrate - migrate projects from Container Registry to Artifact Registry**

**SYNOPSIS**

: **`gcloud artifacts docker upgrade migrate` [`[--canary-reads](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--canary-reads)`=`PERCENT`] [`[--copy-only](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--copy-only)`] [`[--from-gcr](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--from-gcr)`=`GCR_HOST`/`[PROJECT_ID](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#PROJECT_ID)`] [`[--input-iam-policy-dir](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--input-iam-policy-dir)`=`DIRECTORY`] [`[--last-uploaded-versions](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--last-uploaded-versions)`=`N`] [`[--max-threads](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--max-threads)`=`MAX_THREADS`; default=8] [`[--output-iam-policy-dir](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--output-iam-policy-dir)`=`DIRECTORY`] [`[--pkg-dev-location](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--pkg-dev-location)`=`PKG_DEV_LOCATION`] [`[--projects](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--projects)`=`PROJECTS`] [`[--recent-images](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--recent-images)`=`NUM_DAYS`] [`[--skip-iam-update](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--skip-iam-update)`] [`[--skip-pre-copy](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--skip-pre-copy)`] [`[--to-pkg-dev](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--to-pkg-dev)`=`PROJECT_ID`/`[REPOSITORY_ID](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#REPOSITORY_ID)`] [`[--no-use-analyze-iam](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#--use-analyze-iam)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/artifacts/docker/upgrade/migrate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Migrate projects from Container Registry to Artifact Registry

**EXAMPLES**

: To migrate a project `my-project` using gcr.io repositories:

```
gcloud artifacts docker upgrade migrate --projects=my-project
```

To migrate several projects using gcr.io repositories:

```
gcloud artifacts docker upgrade migrate --projects=my-project1,my-project2,my-project3
```

To migrate a project using pkg.dev repositories:

```
gcloud artifacts docker upgrade migrate --from-gcr=gcr.io/project1 --to-pkg-dev=project2/repo_name
```

**FLAGS**

: **--canary-reads**:
Send only a percent of reads to Artifact Registry. The rest of reads and all
writes are sent to Container Registry.

**--copy-only**:
Only perform image copying

**--from-gcr**:
Container Registry host + project to copy from. This flag is only used when
migrating to pkg.dev repos. Example: gcr.io/my-project

**--input-iam-policy-dir**:
During the IAM update step, the tool applies all iam policies in the given
directory.

**--last-uploaded-versions**:
Only copy the N most recently uploaded versions of each image. More than N
images may be copied if new images are uploaded during migration.

**--max-threads**:
Max number of images to copy simultaneously. Consider quota usage when
increasing this

**--output-iam-policy-dir**:
Outputs Artifact Registry-equivalent bindings to this directory during IAM
update step and then exits the tool. After any neccesary modifications are made,
the tool can be rerun with --input-iam-policy-dir to continue migration with the
generated bindings.

**--pkg-dev-location**:
The location of the pkg-dev repository you are migrating to. If not specified,
migration is always done to the same multi-region as GCR. Setting this flag can
cause cross-regional copying and lead to billing charges.

**--projects**:
Comma seperated list of Container Registry projects to migrate to Artifact
Registry gcr.io repositories.

**--recent-images**:
Only copy images pulled or pushed in the last NUM_DAYS days. NUM_DAYS must be
between 30 and 90 inclusive.

**--skip-iam-update**:
Migrate without changing iam-policy. Users without Artifact Registry permissions
will not have access to migrated images.

**--skip-pre-copy**:
Skip the initial copy of recent images before enabling redirection.

**--to-pkg-dev**:
Artifact Registry pkg.dev project ID and repository ID to copy to. Example:
my-project/my-repo

**--use-analyze-iam**:
Use analyzeIAMPolicy to get IAM bindings. If false, tooling iterates through IAM
bindings itself, which is slower, but doesn't require anlayzeIAMPolicy quota.
Enabled by default, use `--no-use-analyze-iam` to disable.

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

: This command uses the `artifactregistry/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/artifacts/docs/](https://cloud.google.com/artifacts/docs/)