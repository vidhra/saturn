# gcloud deploy releases create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create)*

**NAME**

: **gcloud deploy releases create - creates a new release, delivery pipeline qualified**

**SYNOPSIS**

: **`gcloud deploy releases create` (`[RELEASE](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#RELEASE)` : `[--delivery-pipeline](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--delivery-pipeline)`=`DELIVERY_PIPELINE` `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--region)`=`REGION`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[--deploy-parameters](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--deploy-parameters)`=[`KEY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--description)`=`DESCRIPTION`] [`[--gcs-source-staging-dir](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--gcs-source-staging-dir)`=`GCS_SOURCE_STAGING_DIR`] [`[--ignore-file](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--ignore-file)`=`IGNORE_FILE`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--override-deploy-policies](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--override-deploy-policies)`=[`POLICY`,…]] [`[--skaffold-version](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--skaffold-version)`=`SKAFFOLD_VERSION`] [`[--to-target](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--to-target)`=`TO_TARGET`] [`[--build-artifacts](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--build-artifacts)`=`BUILD_ARTIFACTS`     | `[--images](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--images)`=[`NAME`=`TAG`,…]] [`[--disable-initial-rollout](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--disable-initial-rollout)`     | `[--enable-initial-rollout](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--enable-initial-rollout)` `[--initial-rollout-annotations](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--initial-rollout-annotations)`=[`KEY`=`VALUE`,…] `[--initial-rollout-labels](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--initial-rollout-labels)`=[`KEY`=`VALUE`,…] `[--initial-rollout-phase-id](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--initial-rollout-phase-id)`=`INITIAL_ROLLOUT_PHASE_ID`] [`[--from-k8s-manifest](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--from-k8s-manifest)`=`FROM_K8S_MANIFEST`     | `[--from-run-manifest](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--from-run-manifest)`=`FROM_RUN_MANIFEST`     | `[--skaffold-file](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--skaffold-file)`=`SKAFFOLD_FILE` `[--source](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#--source)`=`SOURCE`; default="."] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/releases/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new release, delivery pipeline qualified.

**EXAMPLES**

: To create a release with source located at storage URL
`gs://bucket/object.zip` and the first rollout in the first target of
the promotion sequence:

```
gcloud deploy releases create my-release --source=`gs://bucket/object.zip` --delivery-pipeline=my-pipeline --region=us-central1
```

To create a release with source located at current directory and deploy a
rollout to target prod :

```
gcloud deploy releases create my-release --delivery-pipeline=my-pipeline --region=us-central1 --to-target=prod
```

The following command creates a release without a `skaffold.yaml` as
input, and generates one for you:

```
gcloud deploy releases create my-release --delivery-pipeline=my-pipeline --region=us-central1 --from-k8s-manifest=path/to/kubernetes/k8.yaml
```

The current UTC date and time on the machine running the gcloud command can also
be included in the release name by adding $DATE and $TIME parameters:

```
gcloud deploy releases create 'my-release-$DATE-$TIME' --delivery-pipeline=my-pipeline --region=us-central1
```

If the current UTC date and time is set to 2021-12-21 12:02, then the created
release will have its name set as my-release-20211221-1202.
When using these parameters, please be sure to wrap the release name in single
quotes or else the template parameters will be overridden by environment
variables.

**POSITIONAL ARGUMENTS**

: **Release resource - The name of the Release. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `release` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`RELEASE`**:
ID of the release or fully qualified identifier for the release.
To set the `release` attribute:

- provide the argument `release` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--delivery-pipeline**:
The delivery pipeline associated with the release. Alternatively, set the
property [deploy/delivery-pipeline].
To set the `delivery-pipeline` attribute:

- provide the argument `release` on the command line with a fully
specified name;
- provide the argument `--delivery-pipeline` on the command line;
- set the property `deploy/delivery_pipeline`.

**--region**:
The Cloud region for the release. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `release` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**FLAGS**

: **--annotations**:
Annotations to apply to the release. Annotations take the form of key/value
string pairs.
Examples:
Add annotations:

```
gcloud deploy releases create --annotations="from_target=test,status=stable"
```

**--deploy-parameters**:
Deployment parameters to apply to the release. Deployment parameters take the
form of key/value string pairs.
Examples:
Add deployment parameters:

```
gcloud deploy releases create --deploy-parameters="key1=value1,key2=value2"
```

**--description**:
Description of the release.

**--gcs-source-staging-dir**:
A directory in Google Cloud Storage to copy the source used for staging the
build. If the specified bucket does not exist, Cloud Deploy will create one. If
you don't set this field,
`gs://[DELIVERY_PIPELINE_ID]_clouddeploy/source` is used.

**--ignore-file**:
Override the `.gcloudignore` file and use the specified file instead.

**--labels**:
Labels to apply to the release. Labels take the form of key/value string pairs.
Examples:
Add labels:

```
gcloud deploy releases create --labels="commit=abc123,author=foo"
```

**--override-deploy-policies**:
Deploy policies to override

**--skaffold-version**:
Version of the Skaffold binary.

**--to-target**:
Specifies a target to deliver into upon release creation

**--build-artifacts**

**--disable-initial-rollout**

**--from-k8s-manifest**

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
gcloud alpha deploy releases create
```

```
gcloud beta deploy releases create
```