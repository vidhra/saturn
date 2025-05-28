# gcloud pam entitlements  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/entitlements](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements)*

**NAME**

: **gcloud pam entitlements - manage Privileged Access Manager entitlements**

**SYNOPSIS**

: **`gcloud pam entitlements` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The `gcloud pam entitlements` command group lets you manage
Privileged Access Manager (PAM) entitlements.

**EXAMPLES**

: To create a new entitlement with a name of `sample-entitlement`, in a
project named `sample-project`, in location `global`, and
the entitlement configuration stored in a file named
`sample-entitlement.yaml`, run:

```
gcloud pam entitlements create sample-entitlement --project=sample-project --location=global --entitlement-file=sample-entitlement.yaml
```

To create a new entitlement with a name of `sample-entitlement`, in a
folder with ID ``FOLDER_ID``, in location
`global`, and the entitlement configuration stored in a file named
`sample-entitlement.yaml`, run:

```
gcloud pam entitlements create sample-entitlement --folder=FOLDER_ID --location=global --entitlement-file=sample-entitlement.yaml
```

To create a new entitlement with a name of `sample-entitlement`, in
an organization with ID ``ORGANIZATION_ID``, in
location `global`, and the entitlement configuration stored in a file
named `sample-entitlement.yaml`, run:

```
gcloud pam entitlements create sample-entitlement --organization=ORGANIZATION_ID --location=global --entitlement-file=sample-entitlement.yaml
```

To update an entitlement with a name of `sample-entitlement`, in a
project named `sample-project`, in location `global`, and
the new entitlement configuration stored in a file named
`sample-entitlement.yaml`, run:

```
gcloud pam entitlements update sample-entitlement --project=sample-project --location=global --entitlement-file=sample-entitlement.yaml
```

To update an entitlement with a name of `sample-entitlement`, in a
folder with ID ``FOLDER_ID``, in location
`global`, and the new entitlement configuration stored in a file
named `sample-entitlement.yaml`, run:

```
gcloud pam entitlements update sample-entitlement --folder=FOLDER_ID --location=global --entitlement-file=sample-entitlement.yaml
```

To update an entitlement with a name of `sample-entitlement`, in an
organization with ID ``ORGANIZATION_ID``, in
location `global`, and the new entitlement configuration stored in a
file named `sample-entitlement.yaml`, run:

```
gcloud pam entitlements update sample-entitlement --organization=ORGANIZATION_ID --location=global --entitlement-file=sample-entitlement.yaml
```

To describe an entitlement with a name of `sample-entitlement`, in a
project named `sample-project`, and in location `global`,
run:

```
gcloud pam entitlements describe sample-entitlement --project=sample-project --location=global
```

To describe an entitlement with a name of `sample-entitlement`, in a
folder with ID ``FOLDER_ID``, and in location
`global`, run:

```
gcloud pam entitlements describe sample-entitlement --folder=FOLDER_ID --location=global
```

To describe an entitlement with a name of `sample-entitlement`, in an
organization with ID ``ORGANIZATION_ID``, and
in location `global`, run:

```
gcloud pam entitlements describe sample-entitlement --organization=ORGANIZATION_ID --location=global
```

To search for and list all entitlements for which you are a requester, in a
project named `sample-project`, and in location `global`,
run:

```
gcloud pam entitlements search --project=sample-project --location=global --caller-access-type=grant-requester
```

To search for and list all entitlements for which you are an approver, in a
project named `sample-project`, and in location `global`,
run:

```
gcloud pam entitlements search --project=sample-project --location=global --caller-access-type=grant-approver
```

To search for and list all entitlements for which you are a requester, in a
folder with ID ``FOLDER_ID``, and in location
`global`, run:

```
gcloud pam entitlements search --folder=FOLDER_ID --location=global --caller-access-type=grant-requester
```

To search for and list all entitlements for which you are an approver, in a
folder with ID ``FOLDER_ID``, and in location
`global`, run:

```
gcloud pam entitlements search --folder=FOLDER_ID --location=global --caller-access-type=grant-approver
```

To search for and list all entitlements for which you are a requester, in an
organization with ID ``ORGANIZATION_ID``, and
in location `global`, run:

```
gcloud pam entitlements search --organization=ORGANIZATION_ID --location=global --caller-access-type=grant-requester
```

To search for and list all entitlements for which you are an approver, in an
organization with ID ``ORGANIZATION_ID``, and
in location `global`, run:

```
gcloud pam entitlements search --organization=ORGANIZATION_ID --location=global --caller-access-type=grant-approver
```

To list all entitlements in a project named `sample-project` and in
location `global`, run:

```
gcloud pam entitlements list --project=sample-project --location=global
```

To list all entitlements in a folder with ID
``FOLDER_ID`` and in location
`global`, run:

```
gcloud pam entitlements list --folder=FOLDER_ID --location=global
```

To list all entitlements in an organization with ID
``ORGANIZATION_ID`` and in location
`global`, run:

```
gcloud pam entitlements list --organization=ORGANIZATION_ID --location=global
```

To delete an entitlement with a name of `sample-entitlement`, in a
project named `sample-project`, and in location `global`,
run:

```
gcloud pam entitlements delete sample-entitlement --project=sample-project --location=global
```

To delete an entitlement with a name of `sample-entitlement`, in a
folder with ID ``FOLDER_ID``, and in location
`global`, run:

```
gcloud pam entitlements delete sample-entitlement --folder=FOLDER_ID --location=global
```

To delete an entitlement with a name of `sample-entitlement`, in an
organization with ID ``ORGANIZATION_ID``, and
in location `global`, run:

```
gcloud pam entitlements delete sample-entitlement --organization=ORGANIZATION_ID --location=global
```

To export an entitlement with a name of `sample-entitlement`, in a
project named `sample-project`, and in location `global`
to a local YAML file named `sample-entitlement.yaml`, run:

```
gcloud pam entitlements export sample-entitlement --project=sample-project --location=global --destination=sample-entitlement.yaml
```

To export an entitlement with a name of `sample-entitlement`, in a
folder with ID ``FOLDER_ID``, and in location
`global` to a local YAML file named
`sample-entitlement.yaml`, run:

```
gcloud pam entitlements export sample-entitlement --folder=FOLDER_ID --location=global --destination=sample-entitlement.yaml
```

To export an entitlement with a name of `sample-entitlement`, in an
organization with ID ``ORGANIZATION_ID``, and
in location `global` to a local YAML file named
`sample-entitlement.yaml`, run:

```
gcloud pam entitlements export sample-entitlement --organization=ORGANIZATION_ID --location=global --destination=sample-entitlement.yaml
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/create)`**:
Create a new Privileged Access Manager (PAM) entitlement.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/delete)`**:
Delete a Privileged Access Manager (PAM) entitlement.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/describe)`**:
Show details of a Privileged Access Manager (PAM) entitlement.

**`[export](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/export)`**:
Export a Privileged Access Manager (PAM) entitlement into a local YAML file.

**`[list](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/list)`**:
List all Privileged Access Manager (PAM) entitlements under a parent.

**`[search](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search)`**:
Search and list all Privileged Access Manager (PAM) entitlements in a parent for
which you are a requester/approver.

**`[update](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/update)`**:
Update an existing Privileged Access Manager (PAM) entitlement.

**NOTES**

: These variants are also available:

```
gcloud alpha pam entitlements
```

```
gcloud beta pam entitlements
```