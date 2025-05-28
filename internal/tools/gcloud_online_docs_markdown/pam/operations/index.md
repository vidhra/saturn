# gcloud pam operations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/operations](https://cloud.google.com/sdk/gcloud/reference/pam/operations)*

**NAME**

: **gcloud pam operations - manage Privileged Access Manager Long Running Operations**

**SYNOPSIS**

: **`gcloud pam operations` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/pam/operations#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/operations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The `gcloud pam operations` command group lets you manage Privileged
Access Manager (PAM) operations.

**EXAMPLES**

: To describe an operation with the full name
``OPERATION_NAME``, run:

```
gcloud pam operations describe OPERATION_NAME
```

To list all operations in a project named `sample-project` and in
location `global`, run:

```
gcloud pam operations list --project=sample-project --location=global
```

To list all operations in a folder with ID
``FOLDER_ID`` and in location
`global`, run:

```
gcloud pam operations list --folder=FOLDER_ID --location=global
```

To list all operations in an organization with ID
``ORGANIZATION_ID`` and in location
`global`, run:

```
gcloud pam operations list --organization=ORGANIZATION_ID --location=global
```

To delete an operation with the full name
``OPERATION_NAME``, run:

```
gcloud pam operations delete OPERATION_NAME
```

To poll an operation with the full name
``OPERATION_NAME``, run:

```
gcloud pam operations wait OPERATION_NAME
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/pam/operations/delete)`**:
Delete a Privileged Access Manager (PAM) long running operation.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/pam/operations/describe)`**:
Show details of a Privileged Access Manager (PAM) long running operation.

**`[list](https://cloud.google.com/sdk/gcloud/reference/pam/operations/list)`**:
List all Privileged Access Manager (PAM) long running operations under a
location.

**`[wait](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait)`**:
Poll a Privileged Access Manager (PAM) long running operation.

**NOTES**

: These variants are also available:

```
gcloud alpha pam operations
```

```
gcloud beta pam operations
```