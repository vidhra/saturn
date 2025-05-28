# gcloud network-security security-profile-groups  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups)*

**NAME**

: **gcloud network-security security-profile-groups - manage Network Security - Security Profile Groups**

**SYNOPSIS**

: **`gcloud network-security security-profile-groups` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Network Security - Security Profile Groups.

**EXAMPLES**

: To create a Security Profile Group with the name
`my-security-profile-group` (Either a fully specified path or
`--location` and `--organization` flags for SPG should be
specified), `--threat-prevention-profile`
`my-security-profile` and optional description as `optional
description`, run:

```
gcloud network-security security-profile-groups create my-security-profile-group --organization=1234 --location=global --threat-prevention-profile=`organizations/1234/locations/global/securityProfiles/my-security-profile` --description='optional description'
```

To delete an Security Profile Group called
`my-security-profile-group` (Either a fully specified path or
`--location` and `--organization` flags for SPG should be
specified) run:

```
gcloud network-security security-profile-groups delete my-security-profile-group --organization=1234 --location=global
```

To show details of a Security Profile Group named
`my-security-profile-group` (Either a fully specified path or
`--location` and `--organization` flags for SPG should be
specified) run:

```
gcloud network-security security-profile-groups describe my-security-profile-group --organization=1234 --location=global
```

To list Security Profile Groups in specified location and organization, run:

```
gcloud network-security security-profile-groups list --location=global
```

To update an SPG with new Threat prevention profile
`my-new-security-profile` (Either a fully specified path or
`--location` and `--organization` flags for SPG should be
specified), run:

```
gcloud network-security security-profile-groups update my-security-profile-group --organization=1234 --location=global --threat-prevention-profile=`organizations/1234/locations/global/securityProfiles/my-new-security-profile` --description='New Security Profile of type threat prevention'
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/create)`**:
Create a new Security Profile Group.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/delete)`**:
Delete a Security Profile Group.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/describe)`**:
Describe a Security Profile Group.

**`[list](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/list)`**:
List Security Profile groups.

**`[update](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profile-groups/update)`**:
Update a Security Profile Group.

**NOTES**

: These variants are also available:

```
gcloud alpha network-security security-profile-groups
```

```
gcloud beta network-security security-profile-groups
```