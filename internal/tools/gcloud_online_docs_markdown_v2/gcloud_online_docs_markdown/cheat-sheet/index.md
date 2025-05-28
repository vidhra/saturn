# gcloud cheat-sheet  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/cheat-sheet](https://cloud.google.com/sdk/gcloud/reference/cheat-sheet)*

**NAME**

: **gcloud cheat-sheet - display gcloud cheat sheet**

**SYNOPSIS**

: **`gcloud cheat-sheet` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/cheat-sheet#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A roster of go-to `[gcloud](https://cloud.google.com/sdk/gcloud/reference)`
commands for the gcloud tool, Google Cloud's primary command-line tool.

**Getting started**

: Get going with the `[gcloud](https://cloud.google.com/sdk/gcloud/reference)`
command-line tool

- `[gcloud init](https://cloud.google.com/sdk/gcloud/reference/init)`: Initialize,
authorize, and configure the `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` tool.
- `[gcloud version](https://cloud.google.com/sdk/gcloud/reference/version)`: Display
version and installed components.
- `[gcloud components
install](https://cloud.google.com/sdk/gcloud/reference/components/install)`: Install specific components.
- `[gcloud components
update](https://cloud.google.com/sdk/gcloud/reference/components/update)`: Update your Google Cloud CLI to the latest version.
- `[gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set)`
`project`: Set a default Google Cloud project to work on.
- `[gcloud info](https://cloud.google.com/sdk/gcloud/reference/info)`: Display
current `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` tool environment
details.

**Help**

: Google Cloud CLI is happy to help

- `[gcloud help](https://cloud.google.com/sdk/gcloud/reference)`: Search the
`[gcloud](https://cloud.google.com/sdk/gcloud/reference)` tool reference documents
for specific terms.
- `[gcloud feedback](https://cloud.google.com/sdk/gcloud/reference/feedback)`:
Provide feedback for the Google Cloud CLI team.
- `[gcloud topic](https://cloud.google.com/sdk/gcloud/reference/topic)`:
Supplementary help material for non-command topics like accessibility,
filtering, and formatting.

**Personalization**

: Make the Google Cloud CLI your own; personalize your configuration with
properties

- `[gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set)`:
Define a property (like compute/zone) for the current configuration.
- `[gcloud config get](https://cloud.google.com/sdk/gcloud/reference/config/get)`:
Fetch value of a Google Cloud CLI property.
- `[gcloud config list](https://cloud.google.com/sdk/gcloud/reference/config/list)`:
Display all the properties for the current configuration.
- `[gcloud config
configurations create](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create)`: Create a new named configuration.
- `[gcloud config
configurations list](https://cloud.google.com/sdk/gcloud/reference/config/configurations/list)`: Display a list of all available configurations.
- `[gcloud
config configurations activate](https://cloud.google.com/sdk/gcloud/reference/config/configurations/activate)`: Switch to an existing named
configuration.

**Credentials**

: Grant and revoke authorization to Google Cloud CLI

- `[gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login)`:
Authorize Google Cloud access for the `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` tool with Google user credentials
and set current account as active.
- `[gcloud auth
activate-service-account](https://cloud.google.com/sdk/gcloud/reference/auth/activate-service-account)`: Like `[gcloud auth login](https://cloud.google.com/sdk/gcloud/reference/auth/login)` but with
service account credentials.
- `[gcloud auth list](https://cloud.google.com/sdk/gcloud/reference/auth/list)`:
List all credentialed accounts.
- `[gcloud auth
print-access-token](https://cloud.google.com/sdk/gcloud/reference/auth/print-access-token)`: Display the current account's access token.
- `[gcloud auth revoke](https://cloud.google.com/sdk/gcloud/reference/auth/revoke)`:
Remove access credentials for an account.

**Projects**

: Manage project access policies

- `[gcloud projects
describe](https://cloud.google.com/sdk/gcloud/reference/projects/describe)`: Display metadata for a project (including its ID).
- `[gcloud
projects add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)`: Add an IAM policy binding to a
specified project.

**Identity & Access Management**

: Configuring Cloud Identity & Access Management (IAM) preferences and service
accounts

- `[gcloud iam
list-grantable-roles](https://cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles)`: List IAM grantable roles for a resource.
- `[gcloud iam roles
create](https://cloud.google.com/sdk/gcloud/reference/iam/roles/create)`: Create a custom role for a project or org.
- `[gcloud iam
service-accounts create](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create)`: Create a service account for a project.
- `[gcloud
iam service-accounts add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding)`: Add an IAM policy
binding to a service account.
- `[gcloud
iam service-accounts set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy)`: Replace existing IAM policy
binding.
- `[gcloud iam
service-accounts keys list](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list)`: List a service account's keys.

**Docker & Google Kubernetes Engine (GKE)**

: Manage containerized applications on Kubernetes

- `[gcloud auth
configure-docker](https://cloud.google.com/sdk/gcloud/reference/auth/configure-docker)`: Register the `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` tool as a Docker credential
helper.
- `[gcloud container
clusters create](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create)`: Create a cluster to run GKE containers.
- `[gcloud container
clusters list](https://cloud.google.com/sdk/gcloud/reference/container/clusters/list)`: List clusters for running GKE containers.
- `[gcloud
container clusters get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials)`: Update `kubeconfig` to
get `kubectl` to use a GKE cluster.
- `[gcloud
container images list-tags](https://cloud.google.com/sdk/gcloud/reference/container/images/list-tags)`: List tag and digest metadata for a
container image.

**Virtual Machines & Compute Engine**

: Create, run, and manage VMs on Google infrastructure

- `[gcloud compute zones
list](https://cloud.google.com/sdk/gcloud/reference/compute/zones/list)`: List Compute Engine zones.
- `[gcloud compute
instances describe](https://cloud.google.com/sdk/gcloud/reference/compute/instances/describe)`: Display a VM instance's details.
- `[gcloud compute
instances list](https://cloud.google.com/sdk/gcloud/reference/compute/instances/list)`: List all VM instances in a project.
- `[gcloud compute
disks snapshot](https://cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot)`: Create snapshot of persistent disks.
- `[gcloud compute
snapshots describe](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe)`: Display a snapshot's details.
- `[gcloud compute
snapshots delete](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/delete)`: Delete a snapshot.
- `[gcloud compute ssh](https://cloud.google.com/sdk/gcloud/reference/compute/ssh)`:
Connect to a VM instance by using SSH.

**Serverless & App Engine**

: Build highly scalable applications on a fully managed serverless platform

- `[gcloud app deploy](https://cloud.google.com/sdk/gcloud/reference/app/deploy)`:
Deploy your app's code and configuration to the App Engine server.
- `[gcloud app versions
list](https://cloud.google.com/sdk/gcloud/reference/app/versions/list)`: List all versions of all services deployed to the App Engine
server.
- `[gcloud app browse](https://cloud.google.com/sdk/gcloud/reference/app/browse)`:
Open the current app in a web browser.
- `[gcloud app create](https://cloud.google.com/sdk/gcloud/reference/app/create)`:
Create an App Engine app within your current project.
- `[gcloud app logs
read](https://cloud.google.com/sdk/gcloud/reference/app/logs/read)`: Display the latest App Engine app logs.

**Miscellaneous**

: Commands that might come in handy

- `[gcloud kms decrypt](https://cloud.google.com/sdk/gcloud/reference/kms/decrypt)`:
Decrypt ciphertext (to a plaintext file) using a Cloud Key Management Service
(Cloud KMS) key.
- `[gcloud logging logs
list](https://cloud.google.com/sdk/gcloud/reference/logging/logs/list)`: List your project's logs.
- `[gcloud sql backups
describe](https://cloud.google.com/sdk/gcloud/reference/sql/backups/describe)`: Display info about a Cloud SQL instance backup.
- `[gcloud sql export
sql](https://cloud.google.com/sdk/gcloud/reference/sql/export/sql)`: Export data from a Cloud SQL instance to a SQL file.

**EXAMPLES**

: To view this cheat sheet, run:

```
gcloud cheat-sheet
```

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