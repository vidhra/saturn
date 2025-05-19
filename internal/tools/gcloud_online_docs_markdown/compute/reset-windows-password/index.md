# gcloud compute reset-windows-password  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password](https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password)*

**NAME**

: **gcloud compute reset-windows-password - reset and return a password for a Windows machine instance**

**SYNOPSIS**

: **`gcloud compute reset-windows-password` `[INSTANCE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password#INSTANCE_NAME)` [`[--user](https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password#--user)`=`USER`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute reset-windows-password` allows a user to reset and
retrieve a password for a Windows virtual machine instance. If the Windows
account does not exist, this command will cause the account to be created and
the password for that new account will be returned.
For Windows instances that are running a domain controller, running this command
creates a new domain user if the user does not exist, or resets the password if
the user does exist. It is not possible to use this command to create a local
user on a domain-controller instance.
NOTE: When resetting passwords or adding a new user to a Domain Controller in
this way, the user will be added to the built in Admin Group on the Domain
Controller. This will give the user wide reaching permissions. If this is not
the desired outcome then Active Directory Users and Computers should be used
instead.
For all other instances, including domain-joined instances, running this command
creates a local user or resets the password for a local user.
WARNING: Resetting a password for an existing user can cause the loss of data
encrypted with the current Windows password, such as encrypted files or stored
passwords.
The user running this command must have write permission for the Google Compute
Engine project containing the Windows instance.

**EXAMPLES**

: To reset the password for user 'foo' on a Windows instance 'my-instance' in zone
'us-central1-f', run:

```
gcloud compute reset-windows-password my-instance --zone=us-central1-f --user=foo
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_NAME`**:
Name of the instance to operate on. For details on valid instance names, refer
to the criteria documented under the field 'name' at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--user**:
``USER`` specifies the username to get the
password for. If omitted, the username is derived from your authenticated
account email address.

**--zone**:
Zone of the instance to operate on. If not specified, you might be prompted to
select a zone (interactive mode only). `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` attempts to identify the
appropriate zone by searching for resources in your currently active project. If
the zone cannot be determined, `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with
all available Google Cloud Platform zones.
To avoid prompting when this flag is omitted, the user can set the
``compute/zone`` property:

```
gcloud config set compute/zone ZONE
```

A list of zones can be fetched by running:

```
gcloud compute zones list
```

To unset the property, run:

```
gcloud config unset compute/zone
```

Alternatively, the zone can be stored in the environment variable
``CLOUDSDK_COMPUTE_ZONE``.

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
gcloud alpha compute reset-windows-password
```

```
gcloud beta compute reset-windows-password
```