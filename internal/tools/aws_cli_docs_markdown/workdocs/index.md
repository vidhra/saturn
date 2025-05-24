# workdocsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) ]

# workdocs

## Description

The Amazon WorkDocs API is designed for the following use cases:

- File Migration: File migration applications are supported for users who want to migrate their files from an on-premises or off-premises file system or service. Users can insert files into a user directory structure, as well as allow for basic metadata changes, such as modifications to the permissions of files.
- Security: Support security applications are supported for users who have additional security needs, such as antivirus or data loss prevention. The API actions, along with CloudTrail, allow these applications to detect when changes occur in Amazon WorkDocs. Then, the application can take the necessary actions and replace the target file. If the target file violates the policy, the application can also choose to email the user.
- eDiscovery/Analytics: General administrative applications are supported, such as eDiscovery and analytics. These applications can choose to mimic or record the actions in an Amazon WorkDocs site, along with CloudTrail, to replicate data for eDiscovery, backup, or analytical applications.

All Amazon WorkDocs API actions are Amazon authenticated and certificate-signed. They not only require the use of the Amazon Web Services SDK, but also allow for the exclusive use of IAM users and roles to help facilitate access, trust, and permission policies. By creating a role and allowing an IAM user to access the Amazon WorkDocs site, the IAM user gains full administrative visibility into the entire Amazon WorkDocs site (or as set in the IAM policy). This includes, but is not limited to, the ability to modify file permissions and upload any file to any user. This allows developers to perform the three use cases above, as well as give users the ability to grant access on a selective basis using the IAM model.

### Note

The pricing for Amazon WorkDocs APIs varies depending on the API call type for these actions:

- `READ (Get*)`
- `WRITE (Activate*, Add*, Create*, Deactivate*, Initiate*, Update*)`
- `LIST (Describe*)`
- `DELETE*, CANCEL`

For information about Amazon WorkDocs API pricing, see [Amazon WorkDocs Pricing](https://aws.amazon.com/workdocs/pricing/) .

## Available Commands

- [abort-document-version-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/abort-document-version-upload.html)
- [activate-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/activate-user.html)
- [add-resource-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/add-resource-permissions.html)
- [create-comment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-comment.html)
- [create-custom-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-custom-metadata.html)
- [create-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-folder.html)
- [create-labels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-labels.html)
- [create-notification-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-notification-subscription.html)
- [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-user.html)
- [deactivate-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/deactivate-user.html)
- [delete-comment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-comment.html)
- [delete-custom-metadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-custom-metadata.html)
- [delete-document](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-document.html)
- [delete-document-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-document-version.html)
- [delete-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-folder.html)
- [delete-folder-contents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-folder-contents.html)
- [delete-labels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-labels.html)
- [delete-notification-subscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-notification-subscription.html)
- [delete-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-user.html)
- [describe-activities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-activities.html)
- [describe-comments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-comments.html)
- [describe-document-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-document-versions.html)
- [describe-folder-contents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-folder-contents.html)
- [describe-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-groups.html)
- [describe-notification-subscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-notification-subscriptions.html)
- [describe-resource-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-resource-permissions.html)
- [describe-root-folders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-root-folders.html)
- [describe-users](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-users.html)
- [get-current-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-current-user.html)
- [get-document](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document.html)
- [get-document-path](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document-path.html)
- [get-document-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document-version.html)
- [get-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-folder.html)
- [get-folder-path](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-folder-path.html)
- [get-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-resources.html)
- [initiate-document-version-upload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/initiate-document-version-upload.html)
- [remove-all-resource-permissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-all-resource-permissions.html)
- [remove-resource-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-resource-permission.html)
- [restore-document-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/restore-document-versions.html)
- [search-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/search-resources.html)
- [update-document](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document.html)
- [update-document-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document-version.html)
- [update-folder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-folder.html)
- [update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-user.html)