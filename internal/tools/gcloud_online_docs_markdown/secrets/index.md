# gcloud secrets  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/secrets](https://cloud.google.com/sdk/gcloud/reference/secrets)*

**NAME**

: **gcloud secrets - manage secrets on Google Cloud**

**SYNOPSIS**

: **`gcloud secrets` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/secrets#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/secrets#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/secrets#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Google Secret Manager allows users to store and retrieve secrets such as API
keys, certificates, passwords on Google Cloud. Google Secret Manager is
integrated with Cloud IAM and Cloud Audit Logging so users can manage
permissions on individual secrets and monitor how these are used.
To learn more about Google Secret Manager, visit:

```
https://cloud.google.com/secret-manager/
```

To read API and usage documentation, visit:

```
https://cloud.google.com/secret-manager/docs/
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[locations](https://cloud.google.com/sdk/gcloud/reference/secrets/locations)`**:
Manage locations of users' secrets.

**`[replication](https://cloud.google.com/sdk/gcloud/reference/secrets/replication)`**:
Manage secret replication.

**`[versions](https://cloud.google.com/sdk/gcloud/reference/secrets/versions)`**:
Manage secret versions.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/secrets/add-iam-policy-binding)`**:
Add IAM policy binding to a secret.

**`[create](https://cloud.google.com/sdk/gcloud/reference/secrets/create)`**:
Create a new secret.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/secrets/delete)`**:
Delete a secret.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/secrets/describe)`**:
Describe a secret's metadata.

**`[get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/secrets/get-iam-policy)`**:
Get the IAM policy for the secret.

**`[list](https://cloud.google.com/sdk/gcloud/reference/secrets/list)`**:
List all secret names.

**`[remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/secrets/remove-iam-policy-binding)`**:
Remove IAM policy binding for a secret.

**`[set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/secrets/set-iam-policy)`**:
Set the IAM policy binding for a secret.

**`[update](https://cloud.google.com/sdk/gcloud/reference/secrets/update)`**:
Update a secret's metadata.

**NOTES**

: These variants are also available:

```
gcloud alpha secrets
```

```
gcloud beta secrets
```