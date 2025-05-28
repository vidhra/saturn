# gcloud functions deploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/functions/deploy](https://cloud.google.com/sdk/gcloud/reference/functions/deploy)*

**NAME**

: **gcloud functions deploy - create or update a Google Cloud Function**

**SYNOPSIS**

: **`gcloud functions deploy` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#NAME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--region)`=`REGION`) [`[--[no-]allow-unauthenticated](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--[no-]allow-unauthenticated)`] [`[--concurrency](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--concurrency)`=`CONCURRENCY`] [`[--docker-registry](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--docker-registry)`=`DOCKER_REGISTRY`] [`[--egress-settings](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--egress-settings)`=`EGRESS_SETTINGS`] [`[--entry-point](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--entry-point)`=`ENTRY_POINT`] [`[--gen2](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--gen2)`] [`[--ignore-file](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--ignore-file)`=`IGNORE_FILE`] [`[--ingress-settings](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--ingress-settings)`=`INGRESS_SETTINGS`] [`[--retry](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--retry)`] [`[--run-service-account](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--run-service-account)`=`RUN_SERVICE_ACCOUNT`] [`[--runtime](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime)`=`RUNTIME`] [`[--runtime-update-policy](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime-update-policy)`=`RUNTIME_UPDATE_POLICY`] [`[--security-level](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--security-level)`=`SECURITY_LEVEL`; default="secure-always"] [`[--serve-all-traffic-latest-revision](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--serve-all-traffic-latest-revision)`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--service-account)`=`SERVICE_ACCOUNT`] [`[--source](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--source)`=`SOURCE`] [`[--stage-bucket](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--stage-bucket)`=`STAGE_BUCKET`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--timeout)`=`TIMEOUT`] [`[--trigger-location](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-location)`=`TRIGGER_LOCATION`] [`[--trigger-service-account](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-service-account)`=`TRIGGER_SERVICE_ACCOUNT`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--binary-authorization](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--binary-authorization)`=`BINARY_AUTHORIZATION`     | `[--clear-binary-authorization](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-binary-authorization)`] [`[--build-env-vars-file](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--build-env-vars-file)`=`FILE_PATH`     | `[--clear-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-build-env-vars)`     | `[--set-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--set-build-env-vars)`=[`KEY`=`VALUE`,…]     | `[--remove-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--remove-build-env-vars)`=[`KEY`,…] `[--update-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--update-build-env-vars)`=[`KEY`=`VALUE`,…]] [`[--build-service-account](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--build-service-account)`=`BUILD_SERVICE_ACCOUNT`     | `[--clear-build-service-account](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-build-service-account)`] [`[--build-worker-pool](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--build-worker-pool)`=`BUILD_WORKER_POOL`     | `[--clear-build-worker-pool](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-build-worker-pool)`] [`[--clear-docker-repository](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-docker-repository)`     | `[--docker-repository](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--docker-repository)`=`DOCKER_REPOSITORY`] [`[--clear-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-env-vars)`     | `[--env-vars-file](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--env-vars-file)`=`FILE_PATH`     | `[--set-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--set-env-vars)`=[`KEY`=`VALUE`,…]     | `[--remove-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--remove-env-vars)`=[`KEY`,…] `[--update-env-vars](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--update-env-vars)`=[`KEY`=`VALUE`,…]] [`[--clear-kms-key](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-kms-key)`     | `[--kms-key](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--kms-key)`=`KMS_KEY`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--remove-labels)`=[`KEY`,…]] [`[--clear-max-instances](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-max-instances)`     | `[--max-instances](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--max-instances)`=`MAX_INSTANCES`] [`[--clear-min-instances](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-min-instances)`     | `[--min-instances](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--min-instances)`=`MIN_INSTANCES`] [`[--clear-secrets](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-secrets)`     | `[--set-secrets](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--set-secrets)`=[`SECRET_ENV_VAR`=`SECRET_VALUE_REF`,/`secret_path`=`SECRET_VALUE_REF`,/`mount_path`:/`secret_file_path`=`SECRET_VALUE_REF`,…]     | `[--remove-secrets](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--remove-secrets)`=[`SECRET_ENV_VAR`,/`secret_path`,/`mount_path`:/`secret_file_path`,…] `[--update-secrets](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--update-secrets)`=[`SECRET_ENV_VAR`=`SECRET_VALUE_REF`,/`secret_path`=`SECRET_VALUE_REF`,/`mount_path`:/`secret_file_path`=`SECRET_VALUE_REF`,…]] [`[--clear-vpc-connector](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--clear-vpc-connector)`     | `[--vpc-connector](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--vpc-connector)`=`VPC_CONNECTOR`] [`[--memory](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--memory)`=`MEMORY` : `[--cpu](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--cpu)`=`CPU`] [`[--trigger-bucket](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-bucket)`=`TRIGGER_BUCKET`     | `[--trigger-http](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-http)`     | `[--trigger-topic](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-topic)`=`TRIGGER_TOPIC`     | `[--trigger-event](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-event)`=`EVENT_TYPE` `[--trigger-resource](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-resource)`=`RESOURCE`     | `[--trigger-event-filters](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-event-filters)`=[`ATTRIBUTE`=`VALUE`,…] `[--trigger-event-filters-path-pattern](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--trigger-event-filters-path-pattern)`=[`ATTRIBUTE`=`PATH_PATTERN`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/functions/deploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create or update a Google Cloud Function.

**EXAMPLES**

: To deploy a function that is triggered by write events on the document
``/messages/{pushId}``, run:

```
gcloud functions deploy my_function --runtime=python37 --trigger-event=providers/cloud.firestore/eventTypes/document.write --trigger-resource=projects/project_id/databases/(default)/documents/messages/{pushId}
```

See [https://cloud.google.com/functions/docs/calling](https://cloud.google.com/functions/docs/calling)
for more details of using other types of resource as triggers.

**POSITIONAL ARGUMENTS**

: **Function resource - The Cloud Function name to deploy. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the function or fully qualified identifier for the function.
To set the `function` attribute:

- provide the argument `NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the function. Overrides the default
`functions/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `functions/region`.**

**FLAGS**

: **--[no-]allow-unauthenticated**:
If set, makes this a public function. This will allow all callers, without
checking authentication. Use `--allow-unauthenticated` to enable and
`--no-allow-unauthenticated` to disable.

**--concurrency**:
Set the maximum number of concurrent requests allowed per container instance.
Leave concurrency unspecified to receive the server default value.

**--docker-registry**:
(DEPRECATED) Docker Registry to use for storing the function's Docker images.
The option `artifact-registry` is used by default.

```
With the general transition from Container Registry to
Artifact Registry, the option to specify docker registry is deprecated.
All container image storage and management will automatically
transition to Artifact Registry.
For more information, see
https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr
```

`DOCKER_REGISTRY` must be one of:
`artifact-registry`, `container-registry`.

**--egress-settings**:
Egress settings controls what traffic is diverted through the VPC Access
Connector resource. By default `private-ranges-only` will be used.
`EGRESS_SETTINGS` must be one of:
`private-ranges-only`, `all`.

**--entry-point**:
Name of a Google Cloud Function (as defined in source code) that will be
executed. Defaults to the resource name suffix (ID of the function), if not
specified.

**--gen2**:
If enabled, this command will use Cloud Functions (Second generation). If
disabled with `--no-gen2`, Cloud Functions (First generation) will be
used. If not specified, the value of this flag will be taken from the
`functions/gen2` configuration property. If the
`functions/gen2` configuration property is not set, defaults to
looking up the given function and using its generation.

**--ignore-file**:
Override the .gcloudignore file in the source directory and use the specified
file instead. By default, the source directory is your current directory. Note
that it could be changed by the --source flag, in which case your .gcloudignore
file will be searched in the overridden directory. For example,
`--ignore-file=.mygcloudignore` combined with
`--source=./mydir` would point to
`./mydir/.mygcloudignore`

**--ingress-settings**:
Ingress settings controls what traffic can reach the function. By default
`all` will be used. `INGRESS_SETTINGS` must be
one of: `all`, `internal-only`,
`internal-and-gclb`.

**--retry**:
If specified, then the function will be retried in case of a failure.

**--run-service-account**:
The email address of the IAM service account associated with the Cloud Run
service for the function. The service account represents the identity of the
running function, and determines what permissions the function has.
If not provided, the function will use the project's default service account for
Compute Engine.

**--runtime**:
Runtime in which to run the function.
Required when deploying a new function; optional when updating an existing
function.
For a list of available runtimes, run `[gcloud functions runtimes
list](https://cloud.google.com/sdk/gcloud/reference/functions/runtimes/list)`.

**--runtime-update-policy**:
Runtime update policy for the function being deployed. The option
`automatic` is used by default.
`RUNTIME_UPDATE_POLICY` must be one of:
`automatic`, `on-deploy`.

**--security-level**:
Security level controls whether a function's URL supports HTTPS only or both
HTTP and HTTPS. By default, `secure-always` will be used, meaning
only HTTPS is supported. `SECURITY_LEVEL` must be one of:
`secure-always`, `secure-optional`.

**--serve-all-traffic-latest-revision**:
If specified, latest function revision will be served all traffic.

**--service-account**:
The email address of the IAM service account associated with the function at
runtime. The service account represents the identity of the running function,
and determines what permissions the function has.
If not provided, the function will use the project's default service account for
Compute Engine.

**--source**:
Location of source code to deploy.
Location of the source can be one of the following three options:

- Source code in Google Cloud Storage (must be a `.zip` archive),
- Reference to source repository or,
- Local filesystem path (root directory of function source).

Note that, depending on your runtime type, Cloud Functions will look for files
with specific names for deployable functions. For Node.js, these filenames are
`index.js` or `function.js`. For Python, this is
`main.py`.
If you do not specify the `--source` flag:

- The current directory will be used for new function deployments.
- If the function was previously deployed using a local filesystem path, then the
function's source code will be updated using the current directory.
- If the function was previously deployed using a Google Cloud Storage location or
a source repository, then the function's source code will not be updated.

The value of the flag will be interpreted as a Cloud Storage location, if it
starts with `gs://`.
The value will be interpreted as a reference to a source repository, if it
starts with `https://`.
Otherwise, it will be interpreted as the local filesystem path. When deploying
source from the local filesystem, this command skips files specified in the
`.gcloudignore` file (see `[gcloud topic
gcloudignore](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore)` for more information). If the `.gcloudignore`
file doesn't exist, the command will try to create it.
The minimal source repository URL is:
`https://source.developers.google.com/projects/${PROJECT}/repos/${REPO}`
By using the URL above, sources from the root directory of the repository on the
revision tagged `master` will be used.
If you want to deploy from a revision different from `master`, append
one of the following three sources to the URL:

- `/revisions/${REVISION}`,
- `/moveable-aliases/${MOVEABLE_ALIAS}`,
- `/fixed-aliases/${FIXED_ALIAS}`.

If you'd like to deploy sources from a directory different from the root, you
must specify a revision, a moveable alias, or a fixed alias, as above, and
append `/paths/${PATH_TO_SOURCES_DIRECTORY}` to the URL.
Overall, the URL should match the following regular expression:

```
^https://source\.developers\.google\.com/projects/
(?<accountId>[^/]+)/repos/(?<repoName>[^/]+)
(((/revisions/(?<commit>[^/]+))|(/moveable-aliases/(?<branch>[^/]+))|
(/fixed-aliases/(?<tag>[^/]+)))(/paths/(?<path>.*))?)?$
```

An example of a validly formatted source repository URL is:

```
https://source.developers.google.com/projects/123456789/repos/testrepo/
moveable-aliases/alternate-branch/paths/path-to=source
```

**--stage-bucket**:
When deploying a function from a local directory, this flag's value is the name
of the Google Cloud Storage bucket in which source code will be stored. Note
that if you set the `--stage-bucket` flag when deploying a function,
you will need to specify `--source` or `--stage-bucket` in
subsequent deployments to update your source code. To use this flag
successfully, the account in use must have permissions to write to this bucket.
For help granting access, refer to this guide: [https://cloud.google.com/storage/docs/access-control/](https://cloud.google.com/storage/docs/access-control/)

**--timeout**:
The function execution timeout, e.g. 30s for 30 seconds. Defaults to original
value for existing function or 60 seconds for new functions.
For GCF 1st gen functions, cannot be more than 540s.
For GCF 2nd gen functions, cannot be more than 3600s.
See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--trigger-location**:
The location of the trigger, which must be a region or multi-region where the
relevant events originate.

**--trigger-service-account**:
The email address of the IAM service account associated with the Eventarc
trigger for the function. This is used for authenticated invocation.
If not provided, the function will use the project's default service account for
Compute Engine.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.
Label keys starting with `deployment` are reserved for use by
deployment tools and cannot be specified manually.

**--binary-authorization**

**--build-env-vars-file**

**--build-service-account**

**--build-worker-pool**

**--clear-docker-repository**

**--clear-env-vars**

**--clear-kms-key**

**--clear-labels**

**--clear-max-instances**

**--clear-min-instances**

**--clear-secrets**

**--clear-vpc-connector**

**--memory**:
Limit on the amount of memory the function can use.
Allowed values for v1 are: 128MB, 256MB, 512MB, 1024MB, 2048MB, 4096MB, and
8192MB.
Allowed values for GCF 2nd gen are in the format: <number><unit>
with allowed units of "k", "M", "G", "Ki", "Mi", "Gi". Ending 'b' or 'B' is
allowed, but both are interpreted as bytes as opposed to bits.
Examples: 1000000K, 1000000Ki, 256Mb, 512M, 1024Mi, 2G, 4Gi.
By default, a new function is limited to 256MB of memory. When deploying an
update to an existing function, the function keeps its old memory limit unless
you specify this flag.

**--cpu**:
The number of available CPUs to set. Only valid when
`--memory=MEMORY` is specified.
Examples: .5, 2, 2.0, 2000m.
By default, a new function's available CPUs is determined based on its memory
value.
When deploying an update that includes memory changes to an existing function,
the function's available CPUs will be recalculated based on the new memory
unless this flag is specified. When deploying an update that does not include
memory changes to an existing function, the function's "available CPUs" setting
will keep its old value unless you use this flag to change the setting.

**--trigger-topic**

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
gcloud alpha functions deploy
```

```
gcloud beta functions deploy
```