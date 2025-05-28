# gcloud infra-manager deployments apply  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply)*

**NAME**

: **gcloud infra-manager deployments apply - create or update a deployment**

**SYNOPSIS**

: **`gcloud infra-manager deployments apply` (`[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#DEPLOYMENT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--location)`=`LOCATION`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--annotations)`=[`KEY`=`VALUE`,…]] [`[--artifacts-gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--artifacts-gcs-bucket)`=`ARTIFACTS_GCS_BUCKET`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--async)`] [`[--import-existing-resources](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--import-existing-resources)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--labels)`=[`KEY`=`VALUE`,…]] [`[--quota-validation](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--quota-validation)`=`QUOTA_VALIDATION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--service-account)`=`SERVICE_ACCOUNT`] [`[--tf-version-constraint](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--tf-version-constraint)`=`TF_VERSION_CONSTRAINT`] [`[--worker-pool](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--worker-pool)`=`WORKER_POOL`] [`[--gcs-source](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--gcs-source)`=`GCS_SOURCE`     | `[--git-source-directory](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--git-source-directory)`=`GIT_SOURCE_DIRECTORY` `[--git-source-ref](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--git-source-ref)`=`GIT_SOURCE_REF` `[--git-source-repo](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--git-source-repo)`=`GIT_SOURCE_REPO`     | `[--ignore-file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--ignore-file)`=`IGNORE_FILE` `[--local-source](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--local-source)`=`LOCAL_SOURCE` `[--input-values](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--input-values)`=[`KEY`=`VALUE`,…]     | `[--inputs-file](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#--inputs-file)`=`INPUTS_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/infra-manager/deployments/apply#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command updates a deployment when it already exists, otherwise the
deployment will be created.

**EXAMPLES**

: Create a deployment named `my-deployment` from a storage
`my-bucket`:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --gcs-source="gs://my-bucket" --input-values="project=p1,region=us-central1"
```

Create a deployment named `my-deployment` from git repo
"https://github.com/examples/repository.git", "staging/compute" folder,
"mainline" branch:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --git-source-repo="https://github.com/examples/repository.git" --git-source-directory="staging/compute" --git-source-ref="mainline"
```

Update a deployment's labels:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --git-source-repo="https://github.com/examples/repository.git" --git-source-directory="staging/compute" --git-source-ref="mainline" --labels="env=prod,team=finance"
```

**POSITIONAL ARGUMENTS**

: **Deployment resource - the deployment to create or update. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `DEPLOYMENT` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DEPLOYMENT`**:
ID of the deployment or fully qualified identifier for the deployment.
To set the `deployment` attribute:

- provide the argument `DEPLOYMENT` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the deployment.
To set the `location` attribute:

- provide the argument `DEPLOYMENT` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `infra-manager/location`.**

**FLAGS**

: **--annotations**:
Annotations to apply to the deployment. Existing values are overwritten. To
retain the existing annotations on a deployment, do not specify this flag.
Examples:
Update annotations for an existing deployment:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --gcs-source="gs://my-bucket" --annotations="env=prod,team=finance"
```

Clear annotations for an existing deployment:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --gcs-source="gs://my-bucket" --annotations=""
```

Add an annotation to an existing deployment:

```
First, fetch the current annotations using the `describe` command, then follow the
preceding example for updating annotations.
```

**--artifacts-gcs-bucket**:
user-defined location of Cloud Build logs, artifacts, and Terraform state files
in Google Cloud Storage. Format: `gs://{bucket}/{folder}` A default
bucket will be bootstrapped if the field is not set or empty

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--import-existing-resources**:
By default, Infrastructure Manager will return a failure when Terraform
encounters a 409 code (resource conflict error) during actuation. If this flag
is set to true, Infrastructure Manager will instead attempt to automatically
import the resource into the Terraform state (for supported resource types) and
continue actuation.

**--labels**:
Labels to apply to the deployment. Existing values are overwritten. To retain
the existing labels on a deployment, do not specify this flag.
Examples:
Update labels for an existing deployment:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --gcs-source="gs://my-bucket" --labels="env=prod,team=finance"
```

Clear labels for an existing deployment:

```
gcloud infra-manager deployments apply projects/p1/locations/us-central1/deployments/my-deployment --gcs-source="gs://my-bucket" --labels=""
```

Add a label to an existing deployment:

```
First, fetch the current labels using the `describe` command, then follow the
preceding example for updating labels.
```

**--quota-validation**:
Input to control quota checks for resources in terraform configuration files.
There are limited resources on which quota validation applies. Supported values
are QUOTA_VALIDATION_UNSPECIFIED, ENABLED, ENFORCED

**--service-account**:
User-specified Service Account (SA) to be used as credential to manage
resources. Format:
`projects/{projectID}/serviceAccounts/{serviceAccount}`

**--tf-version-constraint**:
User-specified Terraform version constraint, for example "=1.3.10".

**--worker-pool**:
User-specified Worker Pool resource in which the Cloud Build job will execute.
Format: projects/{project}/locations/{location}/workerPools/{workerPoolId}

**--gcs-source**

**--input-values**

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