# gcloud pam grants  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/grants](https://cloud.google.com/sdk/gcloud/reference/pam/grants)*

**NAME**

: **gcloud pam grants - manage Privileged Access Manager grants**

**SYNOPSIS**

: **`gcloud pam grants` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/pam/grants#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/grants#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The `gcloud pam grants` command group lets you manage Privileged
Access Manager (PAM) grants.

**EXAMPLES**

: To create a new grant against an entitlement with the full name
``ENTITLEMENT_NAME``, a requested duration of
`1 hour 30 minutes`, a justification of `some
justification`, and two additional email recipients
`abc@example.com` and `xyz@example.com`, run:

```
gcloud pam grants create --entitlement=ENTITLEMENT_NAME --requested-duration=5400s --justification="some justification" --additional-email-recipients=abc@example.com,xyz@example.com
```

To describe a grant with the full name
``GRANT_NAME``, run:

```
gcloud pam grants describe GRANT_NAME
```

To list all grants associated with an entitlement with the full name
``ENTITLEMENT_NAME``, run:

```
gcloud pam grants list --entitlement=ENTITLEMENT_NAME
```

To deny a grant with the full name
``GRANT_NAME`` and a reason `denial
reason`, run:

```
gcloud pam grants deny GRANT_NAME --reason="denial reason"
```

To approve a grant with the full name
``GRANT_NAME`` and a reason `approval
reason`, run:

```
gcloud pam grants approve GRANT_NAME --reason="approval reason"
```

To revoke a grant with the full name
``GRANT_NAME`` and a reason `revoke
reason`, run:

```
gcloud pam grants revoke GRANT_NAME --reason="revoke reason"
```

To search for and list all grants that you have created that are associated with
an entitlement with the full name
``ENTITLEMENT_NAME``, run:

```
gcloud pam grants search --entitlement=ENTITLEMENT_NAME --caller-relationship=had-created
```

To search for and list all grants that you have approved or denied, that are
associated with an entitlement with the full name
``ENTITLEMENT_NAME``, run:

```
gcloud pam grants search --entitlement=ENTITLEMENT_NAME --caller-relationship=had-approved
```

To search for and list all grants that you can approve that are associated with
an entitlement with the full name
``ENTITLEMENT_NAME``, run:

```
gcloud pam grants search --entitlement=ENTITLEMENT_NAME --caller-relationship=can-approve
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[approve](https://cloud.google.com/sdk/gcloud/reference/pam/grants/approve)`**:
Approve a Privileged Access Manager (PAM) grant.

**`[create](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create)`**:
Create a new Privileged Access Manager (PAM) grant.

**`[deny](https://cloud.google.com/sdk/gcloud/reference/pam/grants/deny)`**:
Deny a Privileged Access Manager (PAM) grant.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/pam/grants/describe)`**:
Show details of a Privileged Access Manager (PAM) grant.

**`[list](https://cloud.google.com/sdk/gcloud/reference/pam/grants/list)`**:
List all Privileged Access Manager (PAM) grants associated with an entitlement.

**`[revoke](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke)`**:
Revoke a Privileged Access Manager (PAM) grant.

**`[search](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search)`**:
Search for and list all Privileged Access Manager (PAM) grants you have created,
have approved, or can approve.

**NOTES**

: These variants are also available:

```
gcloud alpha pam grants
```

```
gcloud beta pam grants
```