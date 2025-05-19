# gcloud alpha builds submit  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit)*

**NAME**

: **gcloud alpha builds submit - submit a build using Cloud Build**

**SYNOPSIS**

: **`gcloud alpha builds submit` [[`[SOURCE](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#SOURCE)`] `[--no-source](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--source)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--async)`] [`[--no-cache](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--cache)`] [`[--default-buckets-behavior](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--default-buckets-behavior)`=`DEFAULT_BUCKETS_BEHAVIOR`] [`[--dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--dir)`=`DIR`] [`[--disk-size](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--disk-size)`=`DISK_SIZE`] [`[--gcs-log-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--gcs-log-dir)`=`GCS_LOG_DIR`] [`[--gcs-source-staging-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--gcs-source-staging-dir)`=`GCS_SOURCE_STAGING_DIR`] [`[--git-source-dir](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--git-source-dir)`=`GIT_SOURCE_DIR`] [`[--git-source-revision](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--git-source-revision)`=`GIT_SOURCE_REVISION`] [`[--ignore-file](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--ignore-file)`=`IGNORE_FILE`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--machine-type)`=`MACHINE_TYPE`] [`[--polling-interval](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--polling-interval)`=`POLLING_INTERVAL`; default=1] [`[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--region)`=`REGION`] [`[--revision](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--revision)`=`REVISION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--service-account)`=`SERVICE_ACCOUNT`] [`[--substitutions](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--substitutions)`=[`KEY`=`VALUE`,…]] [`[--suppress-logs](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--suppress-logs)`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--timeout)`=`TIMEOUT`] [`[--worker-pool](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--worker-pool)`=`WORKER_POOL`] [`[--config](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--config)`=`CONFIG`; default="cloudbuild.yaml"     | `[--pack](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--pack)`=[`builder`=`BUILDER`],[`env`=`ENV`],[`image`=`IMAGE`]     | `[--tag](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#--tag)`=`TAG`, `[-t](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#-t)` `[TAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#TAG)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/builds/submit#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Submit a build using Cloud Build.
When the `builds/use_kaniko` property is `True`, builds
submitted with `--tag` will use Kaniko
(https://github.com/GoogleContainerTools/kaniko) to execute builds. Kaniko
executes directives in a Dockerfile, with remote layer caching for faster
builds. By default, Kaniko will cache layers for 6 hours. To override this, set
the `builds/kaniko_cache_ttl` property.

**EXAMPLES**

: To submit a build with source located at storage URL
`gs://bucket/object.zip`:

```
gcloud alpha builds submit "gs://bucket/object.zip" --tag=gcr.io/my-project/image
```

To submit a build with source located at storage URL
`gs://bucket/object.zip` using config file `config.yaml`:

```
gcloud alpha builds submit "gs://bucket/object.zip" --tag=gcr.io/my-project/image --config=config.yaml
```

To submit a build with source from a source manifest:

```
gcloud alpha builds submit "gs://bucket/manifest.json" --tag=gcr.io/my-project/image --config=config.yaml
```

To submit a build with local source `source.tgz` asynchronously:

```
gcloud alpha builds submit "source.tgz" --tag=gcr.io/my-project/image --async
```

To submit a build with source from a Git repository
`https://github.com/owner/repo`:

```
gcloud alpha builds submit "https://github.com/owner/repo" --git-source-revision=main --config=config.yaml
```

To submit a build with source from a 2nd-gen Cloud Build repository resource
`projects/my-project/locations/us-west1/connections/my-conn/repositories/my-repo`:

```
gcloud alpha builds submit "projects/my-project/locations/us-west1/connections/my-conn/repositories/my-repo" --revision=main
```

To submit a build with source from a Developer Connect GitRepositoryLink
resource
`projects/my-project/locations/us-west1/connections/my-conn/gitRepositoryLinks/my-repo-link`:

```
gcloud alpha builds submit "projects/my-project/locations/us-west1/connections/my-conn/gitRepositoryLinks/my-repo-link" --revision=main
```

**POSITIONAL ARGUMENTS**

: **At most one of these can be specified:

**[`SOURCE`]**:
The location of the source to build. The location can be a directory on a local
disk, an archive file (e.g., .zip, .tar.gz) or a manifest file (.json) in Google
Cloud Storage, a Git repo url starting with [http://](http://) or
https://, a 2nd-gen Cloud Build repository resource, or a Developer Connect
GitRepositoryLink resource. If the source is a local directory, this command
skips the files specified in the `--ignore-file`. If
`--ignore-file` is not specified, use`.gcloudignore` file.
If a `.gcloudignore` file is absent and a `.gitignore`
file is present in the local source directory, gcloud will use a generated
Git-compatible `.gcloudignore` file that respects your .gitignored
files. The global `.gitignore` is not respected. For more information
on `.gcloudignore`, see `[gcloud topic
gcloudignore](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore)`.

**--no-source**:
Specify that no source should be uploaded with this build.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--no-cache**:
If set, disable layer caching when building with Kaniko.
This has the same effect as setting the builds/kaniko_cache_ttl property to 0
for this build. This can be useful in cases where Dockerfile builds are
non-deterministic and a non-deterministic result should not be cached.

**--default-buckets-behavior**:
How default buckets are setup. `DEFAULT_BUCKETS_BEHAVIOR`
must be one of: `default-logs-bucket-behavior-unspecified`,
`legacy-bucket`, `regional-user-owned-bucket`.

**--dir**:
Directory, relative to the source root, in which to run the build. This is used
when the build source is a 2nd-gen Cloud Build repository resource, or a
Developer Connect GitRepositoryLink resource. This must be a relative path. If a
step's `dir` is specified and is an absolute path, this value is
ignored for that step's execution.

**--disk-size**:
Machine disk size (GB) to run the build.

**--gcs-log-dir**:
A directory in Google Cloud Storage to hold build logs. If this field is not
set, `gs://[PROJECT_NUMBER].cloudbuild-logs.googleusercontent.com/`
will be created and used or
`gs://[PROJECT_NUMBER]-[builds/region]-cloudbuild-logs` is used when
you set `--default-buckets-behavior` to
`REGIONAL_USER_OWNED_BUCKET`.

**--gcs-source-staging-dir**:
A directory in Google Cloud Storage to copy the source used for staging the
build. If the specified bucket does not exist, Cloud Build will create one. If
you don't set this field, `gs://[PROJECT_ID]_cloudbuild/source` is
used or `gs://[PROJECT_ID]_[builds/region]_cloudbuild/source` is used
when you set `--default-buckets-behavior` to
`REGIONAL_USER_OWNED_BUCKET` and `builds/region` is not
`global`.

**--git-source-dir**:
Directory, relative to the source root, in which to run the build. This must be
a relative path. If a step's `dir` is specified and is an absolute
path, this value is ignored for that step's execution.

**--git-source-revision**:
Revision to fetch from the Git repository such as a branch, a tag, a commit SHA,
or any Git ref to run the build.
Cloud Build uses `git fetch` to fetch the revision from the Git
repository; therefore make sure that the string you provide for
`revision` is parsable by the command. For information on string
values accepted by `git fetch`, see [https://git-scm.com/docs/gitrevisions#_specifying_revisions](https://git-scm.com/docs/gitrevisions#_specifying_revisions).
For information on `git fetch`, see [https://git-scm.com/docs/git-fetch](https://git-scm.com/docs/git-fetch).

**--ignore-file**:
Override the `.gcloudignore` file and use the specified file instead.

**--machine-type**:
Machine type used to run the build. `MACHINE_TYPE` must be
one of: `e2-highcpu-32`, `e2-highcpu-8`,
`e2-medium`, `n1-highcpu-32`, `n1-highcpu-8`.

**--polling-interval**:
Amount of time in seconds to wait between polling build status.

**--region**:
The region of the Cloud Build Service to use. Must be set to a supported region
name (e.g. `us-central1`). If unset, `builds/region`,
which is the default region to use when working with Cloud Build resources, is
used. If builds/region is unset, region is set to `global`. Note:
Region must be specified in 2nd gen repo; `global` is not supported.

**--revision**:
Revision to fetch from the Git repository such as a branch, a tag, a commit SHA,
or any Git ref to run the build. This is used when the build source is a 2nd-gen
Cloud Build repository resource, or a Developer Connect GitRepositoryLink
resource.
Cloud Build uses `git fetch` to fetch the revision from the Git
repository; therefore make sure that the string you provide for
`revision` is parsable by the command. For information on string
values accepted by `git fetch`, see [https://git-scm.com/docs/gitrevisions#_specifying_revisions](https://git-scm.com/docs/gitrevisions#_specifying_revisions).
For information on `git fetch`, see [https://git-scm.com/docs/git-fetch](https://git-scm.com/docs/git-fetch).

**--service-account**:
The service account to use with this build. If unset, the default service
account will be used.

**--substitutions**:
Parameters to be substituted in the build specification.
For example (using some nonsensical substitution keys; all keys must begin with
an underscore):

```
gcloud builds submit . --config config.yaml --substitutions _FAVORITE_COLOR=blue,_NUM_CANDIES=10
```

This will result in a build where every occurrence of
`${_FAVORITE_COLOR}` in certain fields is replaced by "blue", and
similarly for `${_NUM_CANDIES}` and "10".
Only the following built-in variables can be specified with the
`--substitutions` flag: REPO_NAME, BRANCH_NAME, TAG_NAME,
REVISION_ID, COMMIT_SHA, SHORT_SHA.
For more details, see: [https://cloud.google.com/cloud-build/docs/api/build-requests#substitutions](https://cloud.google.com/cloud-build/docs/api/build-requests#substitutions)

**--suppress-logs**:
If set, build logs not streamed to stdout.

**--timeout**:
Maximum time a build is run before it is failed as `TIMEOUT`. It is
specified as a duration; for example, "2h15m5s" is two hours, fifteen minutes,
and five seconds. If you don't specify a unit, seconds is assumed. For example,
"10" is 10 seconds. Overrides the default `builds/timeout` property
value for this command invocation.

**--worker-pool**

**--config**

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
gcloud builds submit
```

```
gcloud beta builds submit
```